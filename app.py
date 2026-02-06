import streamlit as st
import pandas as pd
import graphviz
import plotly.express as px
from datetime import datetime
from groq import Groq
import PyPDF2

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
    /* Main Background */
    .main {
        background-color: #0e1117; /* Matches Streamlit Dark Mode default */
    }
    
    /* METRIC CARD STYLING - NUCLEAR OPTION */
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        color: #000000 !important; /* Force parent text black */
    }

    /* Target EVERY element inside the metric card */
    div[data-testid="stMetric"] * {
        color: #2c3e50 !important; /* Force all child text dark blue */
    }

    /* Specific override for the label to be slightly lighter */
    div[data-testid="stMetricLabel"] p, 
    div[data-testid="stMetricLabel"] div,
    div[data-testid="stMetricLabel"] span {
        color: #6c757d !important; /* Grey for "Scale Managed" */
    }

    /* Specific override for the delta indicator (green arrow) */
    div[data-testid="stMetricDelta"] div,
    div[data-testid="stMetricDelta"] svg {
        color: #10B981 !important; /* Keep Green */
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: PROFILE & CONTACT ---
with st.sidebar:
    st.markdown("## 👨‍💻 Narendrakumar Nagarajan")
    st.markdown("""
    **Open to:**
    - Data Engineering Manager
    - Principal Data & AI Engineer
    - Staff Data & AI Engineer
    - Senior Data & AI Engineer
    """)
    st.caption("Enterprise Data Platforms, Fabric & AI")
    
    # Placeholder Avatar
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120) 
    
    st.markdown("---")
    st.markdown("### 📍 Contact")
    st.write("🏙️ Vancouver, BC, Canada")
    st.write("📧 mail2naren887@gmail.com")
    #st.write("📱 +1 (604) 401-9816") 
    st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/naren887)")
    
    st.markdown("---")
    st.markdown("### 📥 Actions")
    # Placeholder for PDF download
    # Inside Sidebar
    with open("Narendrakumar_Resume.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Download Official Resume",
            data=pdf_file,
            file_name="Narendrakumar_Nagarajan_Resume.pdf",
            mime="application/pdf"
        )
        
 # INTERACTIVE AI SIMULATION
    # --- SMARTER SEARCH LOGIC ---
    st.markdown("---")
st.subheader("💬 Chat with Narendra's AI Agent")



# --- FUNCTION TO READ PDF ---
def get_pdf_text(filename):
    try:
        with open(filename, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        return None

# 1. LOAD THE RESUME TEXT
# Make sure this filename matches exactly what you uploaded to GitHub!
resume_filename = "Narendrakumar_Resume.pdf" 
pdf_text = get_pdf_text(resume_filename)

# 2. CHAT INTERFACE
if pdf_text:
    user_query = st.text_input("Ask me anything about Narendra's experience:", 
                               placeholder="Ex: What is his experience with Azure?")
    
    if user_query:
        # Check for API Key
        if "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
            client = Groq(api_key=api_key)
            
            try:
                with st.spinner("Reading resume and thinking..."):
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system", 
                                "content": f"You are a helpful assistant for Narendrakumar. Answer questions strictly based on the following resume text. If the answer is not in the text, say you don't know. \n\nRESUME TEXT:\n{pdf_text}"
                            },
                            {
                                "role": "user", 
                                "content": user_query
                            }
                        ],
                        model="llama-3.3-70b-versatile", # The new supported model
                    )
                    
                    st.success(f"**AI Response:** {chat_completion.choices[0].message.content}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("⚠️ Groq API Key not found in Secrets.")
else:
    st.error(f"⚠️ Could not find '{resume_filename}'. Please upload it to your GitHub repository.")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Professional Summary")
    st.markdown("""
    <p class="big-font">
    Hands-on Technical Leader with 15+ years of experience architecting and operating petabyte-scale Lakehouse platforms on Azure. A rare "Player-Coach" who combines Principal-level architecture skills (GenAI, Fabric, Distributed Systems) with Engineering Management capabilities (leading 12+ engineers, roadmap strategy, hiring).<br>
    <br>Proven track record of delivering business-critical insights for Microsoft, managing platforms processing 50 Billion+ events/month. Expert in modernizing legacy stacks to Microsoft Fabric and Azure Databricks (100+ pipeline migrations), driving FinOps efficiency ($390K/year savings), and implementing GenAI Agents for security operations. Passionate about building high-performance "DataOps" cultures and "Golden Path" standards.
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
        dict(Role="Technology Lead - CAN", Company="Infosys", Start='2019-05-02', End=datetime.today().strftime('%Y-%m-%d'), Category="Leadership"),
        dict(Role="Technology Lead", Company="Infosys", Start='2016-08-01', End='2019-05-01', Category="Tech Lead"),
        dict(Role="Senior Software Engineer", Company="Accenture", Start='2014-02-14', End='2016-07-26', Category="Engineering"),
        dict(Role="Software Engineer Grade-3", Company="Carevoyant", Start='2011-12-05', End='2014-01-31', Category="Engineering"),
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
    
    with st.expander("🔹 **Technical Program Manager (CX Platform) | Microsoft (via Infosys)** | *May 2019 - Aug 2024*"):
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
    # NOTE: '&' MUST be written as '&amp;' for Graphviz to work
    technical_skills = {
        "01": ("Modern Data Stack", "Microsoft Fabric, Databricks (Spark), Synapse, ADLS Gen2, Snowflake, Power BI"),
        "02": ("Data Engineering Langs", "Python, PySpark, SQL (T-SQL, KQL), C#, Go (Learning)"),
        "03": ("Architecture Patterns", "Lakehouse (Delta), Medallion (Bronze/Silver/Gold), Event-Driven, Streaming"),
        "04": ("AI &amp; GenAI Ops", "Azure AI Foundry, Semantic Kernel, RAG Patterns, Vector DBs, Copilot Studio"), 
        "05": ("DevOps &amp; Cloud Infra", "Azure DevOps (CI/CD), Terraform (IaC), Docker, Kubernetes, Git")
    }

    # Right Side: Leadership & Strategy Skills
    leadership_skills = {
        "06": ("Engineering Leadership", "Managing 10-12 Engineers, Hiring, Performance Mgmt, DataOps Culture"),
        "07": ("Strategy &amp; Roadmap", "Platform Modernization (Fabric Migration), Capacity Planning, OKR Alignment"),
        "08": ("Governance &amp; Security", "Microsoft Purview, Unity Catalog, SFI Compliance, PII Protection, Zero Trust"),
        "09": ("FinOps &amp; Efficiency", "Cloud Cost Optimization ($390k savings), Compute/Storage Lifecycle Mgmt"),
        "10": ("Operational Excellence", "Defining SLAs/SLOs, Data Quality Frameworks, Incident Response standards")
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
    for key, (title, details) in technical_skills.items():
        node_id = f"L_{key}"
        label = f"""<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5" BGCOLOR="#0078D4">
          <TR>
            <TD WIDTH="30" BGCOLOR="#005a9e"><FONT COLOR="white"><B>{key}</B></FONT></TD>
            <TD ALIGN="LEFT" BGCOLOR="#E6F2FF">
              <FONT POINT-SIZE="12"><B>{title}</B></FONT><BR/>
              <FONT POINT-SIZE="10">{details}</FONT>
            </TD>
          </TR>
        </TABLE>>"""
        
        graph.node(node_id, label=label, color='#0078D4', fillcolor='white')
        graph.edge(node_id, 'CENTER', color='#0078D4')

    # Create Right Nodes
    for key, (title, details) in leadership_skills.items():
        node_id = f"R_{key}"
        label = f"""<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5" BGCOLOR="#D83B01">
          <TR>
            <TD ALIGN="RIGHT" BGCOLOR="#FDF3F0">
              <FONT POINT-SIZE="12"><B>{title}</B></FONT><BR/>
              <FONT POINT-SIZE="10">{details}</FONT>
            </TD>
            <TD WIDTH="30" BGCOLOR="#A42E01"><FONT COLOR="white"><B>{key}</B></FONT></TD>
          </TR>
        </TABLE>>"""
        
        graph.node(node_id, label=label, color='#D83B01', fillcolor='white')
        graph.edge('CENTER', node_id, color='#D83B01')

    # Render Graph
    st.graphviz_chart(graph, use_container_width=True)

# --- TAB 3: AI & LEADERSHIP ---
# --- INSIDE TAB 3 ---
with tabs[2]:
    st.subheader("⚖️ Leadership & Technical Balance")
    
    # Data for Radar Chart
    categories = ['Strategic Vision', 'People Management', 'Cloud Architecture', 
                  'Coding/Hands-on', 'FinOps/Cost Optimization', 'Governance/SFI']
    values = [5, 5, 5, 4, 5, 5]  # Scale of 1-5

    df_radar = pd.DataFrame(dict(
        r=values,
        theta=categories
    ))

    fig_radar = px.line_polar(df_radar, r='r', theta='theta', line_close=True,
                              title="Competency Radar (Scale 1-5)")
    
    fig_radar.update_traces(fill='toself', line_color='#0078D4')
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 5])
        ),
        showlegend=False,
        height=400
    )
    
    col_radar1, col_radar2 = st.columns([1, 1])
    with col_radar1:
        st.plotly_chart(fig_radar, use_container_width=True)
    with col_radar2:
        st.info("""
        **Interpretation:**
        * **5/5 Strategy & Governance:** Ready to lead SFI compliance and roadmap planning.
        * **4/5 Coding:** I still merge PRs and review architectural code (Python/Terraform).
        * **5/5 FinOps:** Deep expertise in saving money ($390k/yr) via optimizations.
        """)
    
   

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



















