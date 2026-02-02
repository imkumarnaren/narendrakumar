import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Narendrakumar Nagarajan",
    page_icon="📊",
    layout="wide"
)

# --- SIDEBAR: CONTACT & DOWNLOAD ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Placeholder profile icon
    st.header("Narendrakumar Nagarajan")
    st.write("📍 Vancouver, BC, Canada")
    st.write("📧 mail2naren887@gmail.com")
    st.write("📱 +------------")
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/naren887)")
    
    st.divider()
    
    # Download Resume Button (Simulated)
    with open("app.py", "rb") as file: # In real app, replace with path to your PDF
        st.download_button(
            label="📄 Download PDF Resume",
            data=file,
            file_name="Narendrakumar_Resume.pdf",
            mime="application/pdf"
        )
    
    st.info("**Tech Stack of this App:**\n- Python\n- Streamlit\n- Plotly\n- Pandas")

# --- HERO SECTION: METRICS ---
st.title("Data Engineering Manager & Principal Architect")
st.markdown("**Specializing in Azure, Fabric, and Governance at Petabyte Scale**")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Cloud Savings (FinOps)", "$390k / Year", "40% cost reduction")
col2.metric("Data Scale", "50 Billion", "Events per Month")
col3.metric("Security Compliance", "100%", "SFI & GDPR")
col4.metric("Team Size", "12 Engineers", "Data, DevOps, Analytics")

st.divider()

# --- TABBED LAYOUT ---
tab1, tab2, tab3, tab4 = st.tabs(["💼 Experience", "🤖 Chat with Resume", "🛠️ Skills & Tech", "🏆 Projects"])

# --- TAB 1: EXPERIENCE (GANTT CHART) ---
with tab1:
    st.subheader("Career Timeline")
    
    # Data for Timeline
    data = [
        dict(Role="Data Eng Manager (Cyber Defense)", Company="Microsoft (via Infosys)", Start='2024-09-01', End=datetime.today().strftime('%Y-%m-%d'), Type="Leadership"),
        dict(Role="Data Eng Manager (CX Platform)", Company="Microsoft (via Infosys)", Start='2019-05-01', End='2024-08-30', Type="Leadership"),
        dict(Role="Technology Lead", Company="Infosys", Start='2016-08-01', End='2019-04-30', Type="Technical Lead"),
        dict(Role="Senior Software Engineer", Company="Accenture", Start='2014-02-01', End='2016-07-30', Type="Individual Contributor"),
    ]
    df = pd.DataFrame(data)
    
    # Create Gantt Chart
    fig = px.timeline(df, x_start="Start", x_end="End", y="Role", color="Type", hover_name="Company",
                      color_discrete_map={"Leadership": "#0078D4", "Technical Lead": "#5C2D91", "Individual Contributor": "#107C10"})
    fig.update_yaxes(autorange="reversed") # Current role at top
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed Experience Expanders
    with st.expander("📌 **Data Engineering Manager - Microsoft Cyber Defense (Current)**", expanded=True):
        st.write("""
        * **Governance:** Led **Secure Future Initiative (SFI)** achieving 100% compliance across 6 pillars (Identity, Network, etc.).
        * **Innovation:** Architected **TICK Agent** using Azure AI Foundry to automate security triage (-30% manual effort).
        * **Team:** Managing a squad of 12 distributed engineers.
        """)
        
    with st.expander("📌 **Data Engineering Manager - Microsoft CX Platform (2019 - 2024)**"):
        st.write("""
        * **Scale:** Managed telemetry platform processing **50B+ events/month**.
        * **Modernization:** Migrated 100+ pipelines to **Microsoft Fabric** & Databricks (40% perf gain).
        * **FinOps:** Saved **$390k/year** by optimizing Spark clusters and storage lifecycle.
        """)

# --- TAB 2: CHAT WITH RESUME (THE WOW FACTOR) ---
with tab2:
    st.subheader("🤖 Ask my AI Agent")
    st.write("Don't want to read? Just ask a question about my experience. (e.g., *'What is his experience with Fabric?'*)")

    # Simple Keyword-Based Logic (Simulating RAG)
    # NOTE: To make this "Real" AI, you would import OpenAI and use the API key here.
    
    user_query = st.text_input("Ask a question about Narendrakumar:")
    
    if user_query:
        query_lower = user_query.lower()
        response = ""
        
        if "fabric" in query_lower:
            response = "✅ **Yes, deeply experienced.** I led the migration of over 100 pipelines to **Microsoft Fabric** and OneLake, achieving a 40% performance gain. I am also a Microsoft Certified Fabric Analytics Engineer."
        elif "team" in query_lower or "manage" in query_lower:
            response = "👥 **Leadership:** I currently manage a distributed squad of **12 engineers**, including Data Engineers, Analytics Engineers, and DevOps specialists across Vancouver and India."
        elif "cost" in query_lower or "save" in query_lower or "money" in query_lower:
            response = "💰 **FinOps Success:** I optimized Azure compute and storage policies to save the client **$390,000 annually** (approx. 40% of the compute budget)."
        elif "security" in query_lower or "governance" in query_lower:
            response = "🔒 **Security First:** I led the **Secure Future Initiative (SFI)** to 100% compliance using Microsoft Purview and Unity Catalog for RBAC and PII protection."
        else:
            response = "🤖 **AI Response:** Narendrakumar has 15+ years of experience. He specializes in Azure, Databricks, and Governance. Please ask specifically about his Skills, Leadership, or Projects!"
            
        st.success(response)

# --- TAB 3: SKILLS (interactive) ---
with tab3:
    st.subheader("Technical Proficiency")
    
    # Skills Data
    skills_data = {
        "Category": ["Azure Cloud", "Azure Cloud", "Azure Cloud", "Big Data", "Big Data", "Governance", "Governance", "AI/ML", "AI/ML"],
        "Skill": ["Microsoft Fabric", "ADLS Gen2", "Data Factory", "Databricks (Spark)", "Python/PySpark", "Microsoft Purview", "SFI Compliance", "Azure AI Foundry", "Semantic Kernel"],
        "Level": [95, 90, 90, 85, 85, 90, 100, 75, 70]
    }
    df_skills = pd.DataFrame(skills_data)
    
    # Treemap Visual
    fig_skills = px.treemap(df_skills, path=[px.Constant("All Skills"), 'Category', 'Skill'], values='Level',
                            color='Category', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_skills, use_container_width=True)
    
    st.markdown("### Certifications")
    st.markdown("""
    - 🏅 **Microsoft Certified:** Fabric Analytics Engineer Associate (DP-600)
    - 🏅 **Microsoft Certified:** Azure AI Engineer Associate (AI-102)
    """)

# --- TAB 4: PROJECTS ---
with tab4:
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.info("### 🛡️ Secure Future Initiative (SFI)")
        st.write("**Role:** Lead Architect")
        st.write("**Impact:** Achieved 100% compliance across Identity and Network pillars.")
        st.write("**Tech:** Purview, Private Endpoints, Managed Identity.")
        
    with col_p2:
        st.success("### 🤖 TICK Agent (GenAI)")
        st.write("**Role:** Architect & Manager")
        st.write("**Impact:** Reduced security triage time by 30% via self-service natural language queries.")

        st.write("**Tech:** Azure AI Foundry, Semantic Kernel, Python.")

