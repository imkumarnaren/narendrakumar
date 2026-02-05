import streamlit as st
import pandas as pd
import graphviz
import plotly.express as px
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Narendrakumar Nagarajan",
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
        background-color: #ffffff; /* Changed to white for better contrast */
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #e0e0e0;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: 500;
        color: #4a4a4a;
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
    st.write("📱 +1 (604) 401-9816") 
    st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/naren887)")
    
    st.markdown("---")
    st.markdown("### 📥 Actions")
    # In a real app, ensure the PDF exists in the directory
    with open(__file__, "rb") as file:
        st.download_button("📄 Download Resume PDF", data=file, file_name="Narendrakumar_Resume.pdf")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Professional Summary")
    st.markdown("""
    <p class="big-font">
    Hands on - Data Engineering Manager with 15+ years of experience in architecting and operating petabyte-scale Lakehouse platforms in Azure. 
    Proven people manager leading cross-functional squads (10 - 12 engineers: Data, DevOps, Analytics) to deliver business-critical insights and AI-ready datasets. 
    Deep expertise in Microsoft Fabric, Databricks, and Azure Data Services; successfully executed 100+ pipeline migrations to Fabric with zero data loss, achieving a 40% performance gain. 
    Delivered $390K+/year in cloud savings through FinOps, drove 100% SFI/GDPR compliance, and championed SLO-driven reliability and "Golden Path" standards to accelerate delivery across high-volume telemetry platforms (50B+ events/month).
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
        dict(Role="Tech Lead (Cyber)", Company="Infosys", Client="Microsoft", Start='2024-09-01', End=datetime.today().strftime('%Y-%m-%d'), Category="Leadership"),
        dict(Role="Tech Lead (CX)", Company="Infosys", Client="Microsoft", Start='2019-05-02', End='2024-08-30', Category="Leadership"),
        dict(Role="Technology Lead", Company="Infosys", Client="Microsoft", Start='2016-08-01', End='2019-05-01', Category="Tech Lead"),
        dict(Role="Senior Software Engineer", Company="Accenture", Start='2014-02-14', End='2016-07-26', Category="Engineering"),
        dict(Role="Software Engineer", Company="Carevoyant", Start='2011-12-05', End='2014-01-31', Category="Engineering"),
    ]
    df_timeline = pd.DataFrame(timeline_data)
    
    # Plotly Timeline
    fig = px.timeline(df_timeline, x_start="Start", x_end="End", y="Company", color="Category", text="Role",
                      color_discrete_map={"Leadership": "#0078D4", "Tech Lead": "#8B5CF6", "Engineering": "#10B981"})
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Detailed Roles")
    
    with st.expander("🔹 **Technical Program Manager (Cyber Defense Engineering) | Microsoft (via Infosys)** | *Sep 2024 - Present*", expanded=True):
        st.markdown("""
        * **Strategic Execution:** Managing a cross-functional squad of **10+ engineers**. Improved delivery velocity by implementing DataOps (automated testing, CI/CD).
        * **Governance (SFI):** Led the **Secure Future Initiative**, achieving **100% compliance** across Identity and Network pillars.
        * **Reliability:** Established "Golden Path" pipeline standards for the Security Data Lake.
        * **AI Innovation:** Architected **TICK Agent** using Azure AI Foundry.
        """)
    
    with st.expander("🔹 **Technical Program Manager (GIGA XBOX) | Microsoft (via Infosys)** | *Oct 2024 - Aug 2025*"):
        st.markdown("""
        * **Massive Scale:** Owned telemetry platform processing **50 Billion+ events/month**.
        * **Modernization:** Orchestrated migration of **100+ pipelines** to **Microsoft Fabric** and OneLake (40% perf gain).
        * **FinOps:** Reduced Azure spend by **$240K-$390K/year** via cluster policies and spot instances.
        * **Team Building:** Mentored 12 engineers, transitioning Senior DEs into Tech Leads.
        """)

    with st.expander("🔹 **Technology Lead | Microsoft (via Infosys)** | *Aug 2016 - Apr 2019*"):
        st.markdown("""
        * **Cloud Migration:** Architected "R3" BI migration (SQL On-prem to Azure PaaS), saving **$150K/year**.
        * **Data Modeling:** Designed Star Schema for 150+ entities and delivered 40+ Power BI dashboards (500+ DAU).
        * **Quality:** Improved Data Freshness SLA from 85% to 99.9%.
        """)

# --- TAB 2: SKILLS (GRAPHVIZ) ---
with tabs[1]:
    st.subheader("🕸️ Visual Skills Ecosystem")

    # Left Side: Technical Hard Skills
    technical_skills = {
        "01": ("Modern Data Stack"),  
        "02": ("Data Engineering Langs"),
        "03": ("Architecture Patterns"),
        "04": ("AI &amp GenAI Ops"),
        "05": ("DevOps &amp Cloud Infra")
    }

    # Right Side: Leadership & Strategy Skills
    leadership_skills = {
        "06": ("Engineering Leadership"),
        "07": ("Strategy &amp Roadmap"),
        "08": ("Governance & Security"),
        "09": ("FinOps &amp Efficiency"),
        "10": ("Operational Excellence")
    }

    # Initialize Graphviz
    graph = graphviz.Digraph(engine='dot')

    # Global Styling
    graph.attr(rankdir='LR', splines='polyline', nodesep='0.4', ranksep='2.0', bgcolor='#FFFFFF')
    graph.attr('node', shape='box', style='filled, rounded', fontname='Helvetica', penwidth='2', margin='0.2')
    graph.attr('edge', fontname='Helvetica', penwidth='1.5', color='#555555', arrowhead='none')

    # Create Center Node
    center_label = """<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
      <TR><TD><FONT POINT-SIZE="16"><B>NARENDRAKUMAR</B></FONT></TD></TR>
      <TR><TD>Data Eng Manager &amp; Architect</TD></TR>
      <TR><TD><I>Core Competencies Hub</I></TD></TR>
    </TABLE>>"""
    
    graph.node('CENTER', label=center_label, shape='circle', 
               fillcolor='#2c3e50', fontcolor='white', width='2.5', height='2.5', fixedsize='true')

    # Create Left Nodes
    for key, (title) in technical_skills.items():
        node_id = f"L_{key}"
        label = f"""<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="3" BGCOLOR="#0078D4">
          <TR>
            <TD WIDTH="25" BGCOLOR="#005a9e"><FONT COLOR="white"><B>{key}</B></FONT></TD>
            <TD ALIGN="LEFT" BGCOLOR="#E6F2FF">
              <FONT POINT-SIZE="10"><B>{title}</B></FONT><BR/>
            </TD>
          </TR>
        </TABLE>>"""
        
        graph.node(node_id, label=label, color='#0078D4', fillcolor='white')
        graph.edge(node_id, 'CENTER', color='#0078D4')

    # Create Right Nodes
    for key, (title) in leadership_skills.items():
        node_id = f"R_{key}"
        label = f"""<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="3" BGCOLOR="#D83B01">
          <TR>
            <TD ALIGN="RIGHT" BGCOLOR="#FDF3F0">
              <FONT POINT-SIZE="10"><B>{title}</B></FONT><BR/>
            </TD>
            <TD WIDTH="25" BGCOLOR="#A42E01"><FONT COLOR="white"><B>{key}</B></FONT></TD>
          </TR>
        </TABLE>>"""
        
        graph.node(node_id, label=label, color='#D83B01', fillcolor='white')
        graph.edge('CENTER', node_id, color='#D83B01')

    # Render Graph
    st.graphviz_chart(graph, use_container_width=True)

# --- TAB 3: AI & LEADERSHIP ---
with tabs[2]:
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### 🤖 Showcase: 'TICK Agent'")
        st.info("""
        **Problem:** Manual triage of massive security logs was too slow.
        **Solution:** Architected a GenAI retrieval system using Azure AI Foundry.
        **Result:** Reduced manual investigation time by ~30%.
        """)
        
    with c2:
        st.markdown("### 👔 Core Leadership Strengths")
        st.write("""
        - **Data Strategy:** Roadmap planning, migration to Fabric, aligning with OKRs.
        - **Governance:** Databricks Unity Catalog, Microsoft Purview, SFI Compliance.
        - **FinOps:** Reducing unit cost of data through compute/storage optimization.
        - **Operational Excellence:** Managing SLAs/SLOs and Incident Response.
        """)
    
    # INTERACTIVE AI SIMULATION
    st.markdown("---")
    st.subheader("💬 Ask My Resume (AI Simulation)")
    st.caption("Ask questions like: 'What is your experience with Fabric?' or 'How much money did you save?'")
    
    query = st.text_input("Type your question here...")
    if query:
        q = query.lower()
        if "fabric" in q:
            st.success("✅ **Expertise:** I have successfully executed **100+ pipeline migrations** to Microsoft Fabric with zero data loss, achieving a **40% performance gain**.")
        elif "save" in q or "cost" in q or "finops" in q:
            st.success("💰 **FinOps:** I delivered **$390K+/year** in cloud savings by optimizing Spark clusters and storage lifecycle management.")
        elif "team" in q or "lead" in q:
            st.success("👥 **Leadership:** I manage a cross-functional squad of **10-12 engineers** (Data, DevOps, Analytics) and foster a high-performance DataOps culture.")
        elif "ai" in q or "genai" in q:
            st.success("🤖 **AI Ready:** I architected the 'Agent' using Azure AI Foundry and Semantic Kernel to automate security triage.")
        else:
            st.warning("I can answer questions about my Skills, Experience, FinOps savings, or Leadership style!")

# --- TAB 4: EDUCATION ---
with tabs[3]:
    st.markdown("### 🎓 Certifications & Education")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown("**Certifications**")
        st.write("🏅 **Microsoft Certified:** Fabric Analytics Engineer Associate (DP-600)")
        st.write("🏅 **Microsoft Certified:** Azure AI Engineer Associate (AI-102)")
        st.write("🏅 **Microsoft Certified:** Azure AI Fundamentals (AI-900)")
        
    with col_e2:
        st.markdown("**Education**")
        st.write("🎓 **Bachelor of Engineering (B.E.), Computer Science**")
        st.write("Anna University, Chennai, India (2010)")

st.markdown("---")
st.caption("© 2026 Narendrakumar Nagarajan | Built with Python & Streamlit")





