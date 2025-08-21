import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

# --- 🎨 STYLING ---
st.set_page_config(
    page_title="NVD CVE Dashboard",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        :root {
            --primary: #4a6fa5;
            --secondary: #166088;
            --accent: #4fc3f7;
            --background: #f8fafc;
            --card: #ffffff;
            --text: #2d3748;
            --border: #e2e8f0;
        }
        
        .main {
            background-color: var(--background);
        }
        
        .header {
            color: var(--secondary);
            border-bottom: 2px solid var(--accent);
            padding-bottom: 0.5rem;
        }
        
        .metric-card {
            background: var(--card);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-left: 4px solid var(--accent);
            transition: transform 0.2s;
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        }
        
        .metric-title {
            color: var(--secondary);
            font-size: 0.9rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        }
        
        .metric-value {
            color: var(--primary);
            font-size: 1.8rem;
            font-weight: 700;
        }
        
        .stSelectbox, .stDateInput, .stMultiSelect {
            border-radius: 8px !important;
            border: 1px solid var(--border) !important;
        }
        
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
        }
        
        .sidebar .sidebar-content .stSelectbox, 
        .sidebar .sidebar-content .stDateInput,
        .sidebar .sidebar-content .stMultiSelect {
            background-color: rgba(255,255,255,0.9);
        }
        
        .tab-container {
            background: var(--card);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        
        .dataframe {
            border-radius: 12px !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        }
        
        .footer {
            color: var(--secondary);
            font-size: 0.8rem;
            text-align: center;
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border);
        }
    </style>
""", unsafe_allow_html=True)

# --- 📊 DATA LOADING ---
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_data():
    url = 'https://services.nvd.nist.gov/rest/json/cvehistory/2.0/?changeStartDate=2021-08-04T13:00:00.000%2B01:00&changeEndDate=2021-10-22T13:36:00.000%2B01:00' 
    response = requests.get(url)
    data = response.json()
    
    records = []
    for change_item in data.get("cveChanges", []):
        change = change_item["change"]
        cve_id = change.get("cveId")
        created = change.get("created")
        event = change.get("eventName")
        source = change.get("sourceIdentifier")
        change_id = change.get("cveChangeId")

        for detail in change.get("details", []):
            records.append({
                "CVE_ID": cve_id,
                "Date": created,
                "Event": event,
                "Change_ID": change_id,
                "Source": source,
                "Action": detail.get("action"),
                "Type": detail.get("type"),
                "Old_Value": detail.get("oldValue", None),
                "New_Value": detail.get("newValue", None)
            })
    
    df = pd.DataFrame(records)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    df['Severity'] = df['Type'].apply(lambda x: 'CVSS' if 'CVSS' in str(x) else 'Other')
    return df

df = load_data()

# --- 🎚 SIDEBAR CONTROLS ---
with st.sidebar:
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 2rem;">
            <img src="https://nvd.nist.gov/images/nvd_logo.svg" width="180" style="margin-bottom: 1rem;">
            <h2 style="color: white; margin: 0;">CVE Dashboard</h2>
            <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem; margin: 0.5rem 0 0 0;">Track vulnerability changes in real-time</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Filters")
    
    date_range = st.date_input(
        "Select Date Range",
        value=[datetime(2021, 8, 1), datetime(2021, 10, 22)],
        min_value=datetime(2021, 1, 1),
        max_value=datetime.now()
    )
    
    selected_actions = st.multiselect(
        "Action Types",
        options=df['Action'].unique(),
        default=df['Action'].unique()
    )
    
    severity_filter = st.selectbox(
        "Severity Level",
        options=["All", "CVSS Only", "Other"]
    )
    
    st.markdown("---")
    st.markdown("""
        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.7);">
            <p>Data from the National Vulnerability Database</p>
            <p>Updated: {}</p>
        </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M")), unsafe_allow_html=True)

# Apply filters
filtered_df = df.copy()
if len(selected_actions) > 0:
    filtered_df = filtered_df[filtered_df['Action'].isin(selected_actions)]
if severity_filter == "CVSS Only":
    filtered_df = filtered_df[filtered_df['Severity'] == 'CVSS']
elif severity_filter == "Other":
    filtered_df = filtered_df[filtered_df['Severity'] == 'Other']

# --- 📊 DASHBOARD LAYOUT ---
st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
        <h1 style="margin: 0; color: var(--secondary);">NVD CVE Change History</h1>
        <span style="margin-left: auto; background: var(--accent); color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.9rem; font-weight: 500;">
            Real-time Monitoring
        </span>
    </div>
    <p style="color: var(--text); margin-top: -0.5rem; margin-bottom: 2rem;">
        Track and analyze changes to Common Vulnerabilities and Exposures (CVE) records from the National Vulnerability Database
    </p>
""", unsafe_allow_html=True)

# Row 1: Key Metrics
st.markdown("### Overview Metrics")
col1, col2, col3, col4 = st.columns(4)
with col1:
    with st.container():
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Total Changes</div>
                <div class="metric-value">{:,}</div>
            </div>
        """.format(len(filtered_df)), unsafe_allow_html=True)
        
with col2:
    with st.container():
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Unique CVEs</div>
                <div class="metric-value">{:,}</div>
            </div>
        """.format(filtered_df['CVE_ID'].nunique()), unsafe_allow_html=True)
        
with col3:
    with st.container():
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Most Active Month</div>
                <div class="metric-value">{}</div>
            </div>
        """.format(filtered_df['Month'].value_counts().idxmax()), unsafe_allow_html=True)
        
with col4:
    with st.container():
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Top Source</div>
                <div class="metric-value">{}</div>
            </div>
        """.format(filtered_df['Source'].value_counts().idxmax()), unsafe_allow_html=True)

# Row 2: Main Visualizations
st.markdown("""
    <div style="margin: 2rem 0 1rem 0;">
        <h3 class="header">Change Activity Overview</h3>
    </div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📈 Monthly Trends", "🌡 Activity Heatmap", "📋 Raw Data"])

with tab1:
    with st.container():
        fig = px.bar(
            filtered_df.groupby(['Month', 'Action']).size().reset_index(name='Count'),
            x='Month',
            y='Count',
            color='Action',
            title="Monthly CVE Changes by Action Type",
            barmode='stack',
            color_discrete_sequence=px.colors.sequential.Blues_r,
            template='plotly_white'
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified',
            xaxis_title=None,
            yaxis_title="Number of Changes",
            legend_title="Action Type"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    with st.container():
        pivot_table = filtered_df.pivot_table(index='Month', columns='Action', aggfunc='size', fill_value=0)
        plt.figure(figsize=(10, 6))
        sns.set_style("white")
        ax = sns.heatmap(pivot_table, annot=True, fmt='d', cmap='Blues', linewidths=.5, cbar_kws={'label': 'Number of Changes'})
        plt.title("CVE Change Action Heatmap Over Time", pad=20)
        plt.xticks(rotation=45)
        st.pyplot(plt)

with tab3:
    with st.container():
        st.dataframe(
            filtered_df.sort_values('Date', ascending=False),
            column_config={
                "Date": st.column_config.DatetimeColumn(
                    "Date",
                    format="YYYY-MM-DD HH:mm"
                ),
                "CVE_ID": st.column_config.LinkColumn(
                    "CVE ID",
                    display_text="View Details",
                    help="Links to NVD database"
                )
            },
            hide_index=True,
            use_container_width=True
        )

# Row 3: Additional Insights
st.markdown("""
    <div style="margin: 2rem 0 1rem 0;">
        <h3 class="header">Detailed Analysis</h3>
    </div>
""", unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    with st.container():
        st.markdown("#### Severity Distribution")
        severity_fig = px.pie(
            filtered_df,
            names='Severity',
            hole=0.3,
            color_discrete_sequence=['#4a6fa5', '#4fc3f7'],
            template='plotly_white'
        )
        severity_fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5
            )
        )
        st.plotly_chart(severity_fig, use_container_width=True)

with col6:
    with st.container():
        st.markdown("#### Top 10 CVEs by Changes")
        top_cves = filtered_df['CVE_ID'].value_counts().head(10).reset_index()
        top_cves.columns = ['CVE ID', 'Changes']
        
        fig = px.bar(
            top_cves,
            x='Changes',
            y='CVE ID',
            orientation='h',
            color='Changes',
            color_continuous_scale='Blues',
            text='Changes',
            template='plotly_white'
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            yaxis_title=None,
            xaxis_title="Number of Changes",
            coloraxis_showscale=False,
            height=400
        )
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Data sourced from the National Vulnerability Database (NVD) API | Last updated: {}</p>
        <p style="font-size: 0.7rem; color: var(--secondary);">© 2023 NVD CVE Dashboard | v2.0</p>
    </div>
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)