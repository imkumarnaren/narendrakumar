import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Narendrakumar Nagarajan | Data Engineering Manager",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR "10/10" LOOK ---
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: 500;
        color: #5f6368;
    }
    .highlight {
        color: #0078D4; /* Azure Blue */
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: PROFILE & CONTACT ---
with st.sidebar:
    st.markdown("## 👨‍💻 Narendrakumar Nagarajan")
    st.markdown("**Data Engineering Manager**")
    st.caption("Enterprise Data Platforms, Fabric & AI")
    
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120) # Placeholder Avatar
    
    st.markdown("---")
    st.markdown("### 📍 Contact")
    st.write("🏙️ Vancouver, BC, Canada")
    st.write("📧 mail2naren887@gmail.com")
    st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/naren887)")
    
    st.markdown("---")
    st.markdown("### 📥 Actions")
    # In a real app, you would load the actual PDF file here
    with open("app.py", "rb") as file:
        st.download_button("📄 Download Resume PDF", data=file, file_name="Narendrakumar_Data_Engg_Manager.pdf")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Architecting Petabyte-Scale Data Platforms")
    st.markdown("""
    <p class="big-font">
    Hands-on <b>Data Engineering Manager</b> with 15+ years of experience. 
    Specializing in <b>Microsoft Fabric</b>, <b>Databricks</b>, and <b>GenAI</b>. 
    Proven track record of leading squads to deliver <b>$390k+</b> in FinOps savings and scaling platforms to <b>50B+ events/month</b>.
    </p>
    """, unsafe_allow_html=True)

with col2:
    # KPI CARDS
    st.markdown("### 🚀 Impact at a Glance")
    m1, m2 = st.columns(2)
    m1.metric("Scale Managed", "50 Billion+", "Events / Month")
    m2.metric("Cloud Savings", "$390k+", "Per Year (FinOps)")
    
    m3, m4 = st.columns(2)
    m3.metric("Compliance", "100%", "SFI & GDPR")
    m4.metric("Team Size", "12+", "Engineers Led")

st.divider()

# --- TABS FOR DETAILED VIEW ---
tabs = st.tabs(["💼 Professional Experience", "🛠️ Technical Skills", "🤖 AI & Leadership", "🎓 Education"])

# --- TAB 1: EXPERIENCE (TIMELINE & DETAILS) ---
with tabs[0]:
    st.subheader("Career Timeline")
    
    # Timeline Data
    timeline_data = [
        dict(Role="Mgr: Microsoft Cyber Defense", Company="Infosys", Start='2024-09-01', End=datetime.today().strftime('%Y-%m-%d'), Category="Leadership"),
        dict(Role="Mgr: Microsoft CX Platform", Company="Infosys", Start='2019-05-01', End='2024-08-30', Category="Leadership"),
        dict(Role="Tech Lead: Microsoft CX", Company="Infosys", Start='2016-08-01', End='2019-04-30', Category="Tech Lead"),
        dict(Role="Senior Software Engineer", Company="Accenture", Start='2014-02-01', End='2016-07-30', Category="Engineering"),
        dict(Role="Software

