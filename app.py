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
        background-color: #848484;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: 500;
        
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
    st.write("📱 +1 (***) ***-****")
    st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/naren887)")
    
    st.markdown("---")
    st.markdown("### 📥 Actions")
    # In a real app, you would load the actual PDF file here
    with open("app.py", "rb") as file:
        st.download_button("📄 Download Resume PDF", data=file, file_name="Narendrakumar_Data_Engg_Manager1.pdf")

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
        dict(Role="Technology Lead - CAN", Company="Infosys", Client="Microsoft", Start='2019-05-02', End=datetime.today().strftime('%Y-%m-%d'), Category="Leadership"),
        dict(Role="Technology Lead", Company="Infosys",Client="Microsoft", Start='2016-08-01', End='2019-05-01', Category="Tech Lead"),
        dict(Role="Senior Software Engineer", Company="Accenture", Start='2014-02-14', End='2016-07-26', Category="Engineering"),
        dict(Role="Software Engineer - Grade 3", Company="Carevoyant", Start='2011-12-05', End='2014-01-31', Category="Engineering"),
        dict(Role="Software Engineer", Company="Medall", Start='2010-09-13', End='2011-11-30', Category="Engineering"),
    ]
    df_timeline = pd.DataFrame(timeline_data)
    fig = px.timeline(df_timeline, x_start="Start", x_end="End", y="Company", color="Category",text ="Role",
                      color_discrete_map={"Leadership": "#0078D4", "Tech Lead": "#8B5CF6", "Engineering": "#10B981"})
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Detailed Roles")
    
    with st.expander("🔹 **Technical Program Manager (Cyber Defense Engineering) | Microsoft (via Infosys)** | *Sep 2025 - Present*", expanded=True):
        st.markdown("""
        * **Strategic Execution:** Managing a cross-functional squad of **10+ engineers**. Improved delivery velocity by implementing DataOps (automated testing, CI/CD).
        * **Governance (SFI):** Led the **Secure Future Initiative**, achieving **100% compliance** across Identity and Network pillars.
        * **Reliability:** Established "Golden Path" pipeline standards for the Security Data Lake.
        """)
    
    with st.expander("🔹 **Reporting Team Lead (CE&S BI) | Microsoft (via Infosys)** | *Sep 2025 - Present*", expanded=True):
        st.markdown("""
        * **Strategic Execution:** Managing a cross-functional squad of **10+ engineers**. Improved delivery velocity by implementing DataOps (automated testing, CI/CD).
        * **Governance (SFI):** Led the **Secure Future Initiative**, achieving **100% compliance** across Identity and Network pillars.
        * **Reliability:** Established "Golden Path" pipeline standards for the Security Data Lake.
        """)
        
    with st.expander("🔹 **Technical Program Manager (GIGA XBOX) | Microsoft (via Infosys)** | * OCT 2024 - Aug 2025*"):
        st.markdown("""
        * **Massive Scale:** Owned telemetry platform processing **50 Billion+ events/month**.
        * **Modernization:** Orchestrated migration of **100+ pipelines** to **Microsoft Fabric** and OneLake (40% perf gain).
        * **FinOps:** Reduced Azure spend by **$240K-$390K/year** via cluster policies and spot instances.
        * **Team Building:** Mentored 12 engineers, transitioning Senior DEs into Tech Leads.
        * **Automation:** Deprecated manual deployments for fully automated Azure DevOps pipelines.
        """)

    with st.expander("🔹 **Technology Lead | Microsoft (via Infosys)** | *Aug 2016 - Apr 2019*"):
        st.markdown("""
        * **Cloud Migration:** Architected "R3" BI migration (SQL On-prem to Azure PaaS), saving **$150K/year**.
        * **Data Modeling:** Designed Star Schema for 150+ entities and delivered 40+ Power BI dashboards (500+ DAU).
        * **Quality:** Improved Data Freshness SLA from 85% to 99.9%.
        """)

     with st.expander("🔹 **Technology Lead | Microsoft (via Infosys)** | *Aug 2016 - Apr 2019*"):
        st.markdown("""
        * **Cloud Migration:** Architected "R3" BI migration (SQL On-prem to Azure PaaS), saving **$150K/year**.
        * **Data Modeling:** Designed Star Schema for 150+ entities and delivered 40+ Power BI dashboards (500+ DAU).
        * **Quality:** Improved Data Freshness SLA from 85% to 99.9%.
        """)

# --- TAB 2: SKILLS (TREEMAP) ---
with tabs[1]:
     technical_skills = {
    "01": ("Modern Data Stack", "Microsoft Fabric, Databricks (Spark), Synapse, ADLS Gen2, Snowflake, Power BI"),
    "02": ("Data Engineering Langs", "Python, PySpark, SQL (T-SQL, KQL), C#, Go (Learning)"),
    "03": ("Architecture Patterns", "Lakehouse (Delta), Medallion (Bronze/Silver/Gold), Event-Driven, Streaming"),
    "04": ("AI & GenAI Ops", "Azure AI Foundry, Semantic Kernel, RAG Patterns, Vector DBs, Copilot Studio"),
    "05": ("DevOps & Cloud Infra", "Azure DevOps (CI/CD), Terraform (IaC), Docker, Kubernetes, Git")
}

# Right Side: Leadership & Strategy Skills
leadership_skills = {
    "06": ("Engineering Leadership", "Managing 10-12 Engineers, Hiring, Performance Mgmt, DataOps Culture"),
    "07": ("Strategy & Roadmap", "Platform Modernization (Fabric Migration), Capacity Planning, OKR Alignment"),
    "08": ("Governance & Security", "Microsoft Purview, Unity Catalog, SFI Compliance, PII Protection, Zero Trust"),
    "09": ("FinOps & Efficiency", "Cloud Cost Optimization ($390k savings), Compute/Storage Lifecycle Mgmt"),
    "10": ("Operational Excellence", "Defining SLAs/SLOs, Data Quality Frameworks, Incident Response standards")
}

# --- 2. Initialize Graphviz ---
# 'neato' or 'twopi' engines are often good for radial layouts, 
# but 'dot' with rankdir=LR gives a clean left-to-right flow like the example image.
graph = graphviz.Digraph(engine='dot')

# --- 3. Global Styling Attributes ---
graph.attr(rankdir='LR',  # Left to Right layout
           splines='polyline', # Straight lines with bends looks cleaner here
           nodesep='0.4',      # Spacing between nodes
           ranksep='2.0',      # Spacing between ranks (left, center, right columns)
           bgcolor='#FFFFFF')  # Background color

# Default node style
graph.attr('node', shape='box', style='filled, rounded', fontname='Helvetica', penwidth='2', margin='0.2')
# Default edge style
graph.attr('edge', fontname='Helvetica', penwidth='1.5', color='#555555', arrowhead='none')


# --- 4. Create the Center Node ---
# Using HTML-like label for rich formatting within the node
center_label = <<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD><FONT POINT-SIZE="16"><B>NARENDRAKUMAR</B></FONT></TD></TR>
  <TR><TD>Data Eng Manager &amp; Architect</TD></TR>
  <TR><TD><I>Core Competencies Hub</I></TD></TR>
</TABLE>>

graph.node('CENTER', label=center_label, shape='circle', 
           fillcolor='#2c3e50', fontcolor='white', width='2.5', height='2.5', fixedsize='true')


# --- 5. Create Left Side Nodes (Technical) & Connections ---
# Using a blue/cyan color scheme for technical skills
for key, (title, details) in technical_skills.items():
    node_id = f"L_{key}"
    # HTML Label for structured content (Number | Title | Details)
    label = <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5" BGCOLOR="#0078D4">
      <TR>
        <TD WIDTH="30" BGCOLOR="#005a9e"><FONT COLOR="white"><B>{key}</B></FONT></TD>
        <TD ALIGN="LEFT" BGCOLOR="#E6F2FF">
          <FONT POINT-SIZE="12"><B>{title}</B></FONT><BR/>
          <FONT POINT-SIZE="10">{details}</FONT>
        </TD>
      </TR>
    </TABLE>>
    
    graph.node(node_id, label=label, color='#0078D4', fillcolor='white')
    graph.edge(node_id, 'CENTER', color='#0078D4') # Connect to center


# --- 6. Create Right Side Nodes (Leadership) & Connections ---
# Using an orange/purple scheme for leadership skills
for key, (title, details) in leadership_skills.items():
    node_id = f"R_{key}"
    # HTML Label similar to above
    label = <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5" BGCOLOR="#D83B01">
      <TR>
        <TD ALIGN="RIGHT" BGCOLOR="#FDF3F0">
          <FONT POINT-SIZE="12"><B>{title}</B></FONT><BR/>
          <FONT POINT-SIZE="10">{details}</FONT>
        </TD>
        <TD WIDTH="30" BGCOLOR="#A42E01"><FONT COLOR="white"><B>{key}</B></FONT></TD>
      </TR>
    </TABLE>>
    
    graph.node(node_id, label=label, color='#D83B01', fillcolor='white')
    # Note: connecting FROM center TO right node helps guide the layout engine
    graph.edge('CENTER', node_id, color='#D83B01') 

# --- 7. Render the Graph in Streamlit ---
st.graphviz_chart(graph, use_container_width=True)

# --- TAB 3: AI & LEADERSHIP ---
with tabs[2]:
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### 🤖 Showcase: 'Agent'")
        st.info("""
        **Problem:** Manual triage of massive security logs was too slow.
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
            st.success("🤖 **AI Ready:** I architected the 'TICK Agent' using Azure AI Foundry and Semantic Kernel to automate security triage.")
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













