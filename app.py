import streamlit as st
import pandas as pd
import graphviz
import plotly.express as px
from datetime import datetime
from groq import Groq
import PyPDF2
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Narendrakumar Nagarajan",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 1. GLOBAL HTML/CSS VARIABLES (FLUSH LEFT)
# ==========================================

# --- TIMELINE HTML ---
TIMELINE_HTML = """
<style>
.timeline-container { border-left: 4px solid #e0e0e0; margin-left: 20px; padding-left: 30px; position: relative; }
.timeline-item { margin-bottom: 40px; position: relative; }
.timeline-dot { width: 20px; height: 20px; background-color: #0078D4; border-radius: 50%; position: absolute; left: -42px; top: 5px; border: 4px solid white; box-shadow: 0 0 0 1px #e0e0e0; }
.timeline-date { font-weight: bold; color: #0078D4; font-size: 14px; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px; }
.timeline-title { font-size: 18px; font-weight: 700; color: #ffffff; margin-bottom: 8px; }
.timeline-desc { color: #c0c0c0; font-size: 15px; line-height: 1.6; }
.highlight { background-color: #262730; padding: 2px 6px; border-radius: 4px; font-weight: 600; font-size: 0.9em; color: #ffffff; border: 1px solid #444; }
</style>

<div class="timeline-container">
<div class="timeline-item">
<div class="timeline-dot" style="background-color: #8B5CF6;"></div>
<div class="timeline-date">Sep 2024 – Present</div>
<div class="timeline-title">Technology Lead / Principal Data Engineer & Squad Lead (Cyber Defense)</div>
<div class="timeline-desc">
Leading the integration of <b>Generative AI</b> into Security Operations at Microsoft.
<ul>
<li>Architected the <span class="highlight">TICK Agent</span> using Azure AI Foundry & Semantic Kernel.</li>
<li>Led the <b>Secure Future Initiative (SFI)</b> achieving 100% compliance across the Data Estate.</li>
<li>Standardized "Golden Path" CI/CD templates for a squad of 10+ engineers.</li>
</ul>
</div>
</div>

<div class="timeline-item">
<div class="timeline-dot" style="background-color: #0078D4;"></div>
<div class="timeline-date">May 2019 – Aug 2024</div>
<div class="timeline-title">Staff Data Engineer & Platform Manager (CX Platform)</div>
<div class="timeline-desc">
Managed a hyper-scale telemetry platform processing <span class="highlight">50 Billion+ events/month</span>.
<ul>
<li>Orchestrated the migration of <b>100+ pipelines</b> to Microsoft Fabric & OneLake.</li>
<li>Optimized Databricks clusters to save <b>$390k/year</b> (FinOps).</li>
<li>Built and mentored a high-performing team of <b>12 engineers</b>.</li>
</ul>
</div>
</div>

<div class="timeline-item">
<div class="timeline-dot" style="background-color: #2ecc71;"></div>
<div class="timeline-date">Aug 2016 – Apr 2019</div>
<div class="timeline-title">Tech Lead & Cloud Architect (Infosys)</div>
<div class="timeline-desc">
Led the strategic migration from on-premise Legacy stacks to <b>Azure Cloud</b>.
<ul>
<li>Architected the "R3" migration to Azure SQL & ADF, saving $150k annually.</li>
<li>Designed complex <b>Star Schema</b> models for Power BI used by 500+ daily users.</li>
</ul>
</div>
</div>

<div class="timeline-item">
<div class="timeline-dot" style="background-color: #95a5a6;"></div>
<div class="timeline-date">Accenture 2014 – 2016</div>
<div class="timeline-title">Senior Software Engineer</div>
<div class="timeline-desc">
Built the rigorous backend engineering foundation in <b>C#, .NET, and SQL Server</b>.
<ul>
<li>Designed financial ETL systems for <b>Accenture</b>.</li>
<li>Developed HL7 healthcare parsers for <b>Carevoyant</b>.</li>
</ul>
</div>
</div>
</div>

<div class="timeline-item">
<div class="timeline-dot" style="background-color: #95a5a6;"></div>
<div class="timeline-date">Medall 2010 – 2011</div>
<div class="timeline-title">Senior Software Engineer (Accenture & Medall)</div>
<div class="timeline-desc">
Built the rigorous backend engineering foundation in <b>C#, .NET, and SQL Server</b>.
<ul>
<li>Designed financial ETL systems for <b>Accenture</b>.</li>
<li>Developed HL7 healthcare parsers for <b>Carevoyant</b>.</li>
</ul>
</div>
</div>
</div>
"""

# --- SKILLS CSS ---
SKILLS_CSS = """
<style>
.skill-container { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 10px; }
.skill-column { display: flex; flex-direction: column; gap: 15px; }
.skill-card { background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 10px; padding: 20px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); transition: transform 0.2s; }
.skill-card:hover { transform: translateY(-2px); box-shadow: 4px 4px 10px rgba(0,0,0,0.1); }
.card-header { font-weight: 700; color: #2c3e50; font-size: 16px; margin-bottom: 12px; border-bottom: 2px solid #f0f2f6; padding-bottom: 8px; }
.badge-container { display: flex; flex-wrap: wrap; gap: 8px; }
.skill-badge { background-color: #f0f2f6; color: #2c3e50; padding: 5px 12px; border-radius: 15px; font-size: 13px; font-weight: 500; border: 1px solid #d1d5db; }
.tech-header { color: #0078D4; border-bottom-color: #0078D4; }
.lead-header { color: #D83B01; border-bottom-color: #D83B01; }
@media (prefers-color-scheme: dark) {
    .skill-card { background-color: #1e1e1e; border-color: #333; }
    .card-header { color: #ffffff; }
    .skill-badge { background-color: #2d2d2d; color: #e0e0e0; border-color: #444; }
}
@media (max-width: 768px) { .skill-container { grid-template-columns: 1fr; } }
</style>
"""

# --- LEADERSHIP INSIGHTS HTML ---
LEADERSHIP_HTML = """
<style>
.insight-card {
    background-color: #1e2126;
    border-left: 4px solid #0078D4;
    padding: 15px;
    margin-bottom: 15px;
    border-radius: 5px;
}
.insight-title {
    font-weight: bold;
    color: #ffffff;
    font-size: 16px;
    margin-bottom: 5px;
}
.insight-text {
    color: #c0c0c0;
    font-size: 14px;
}
.score-badge {
    float: right;
    background-color: #0078D4;
    color: white;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 12px;
}
</style>

<div class="insight-card">
    <span class="score-badge">5/5</span>
    <div class="insight-title">Strategy & Governance</div>
    <div class="insight-text">
        Defining the "Golden Path" for 50B+ events. Leading SFI compliance across the entire data estate.
    </div>
</div>

<div class="insight-card" style="border-left-color: #2ecc71;">
    <span class="score-badge" style="background-color: #2ecc71;">5/5</span>
    <div class="insight-title">FinOps Mastery</div>
    <div class="insight-text">
        Deep expertise in unit economics. Saved $390k/yr by optimizing cluster policies and storage lifecycles.
    </div>
</div>

<div class="insight-card" style="border-left-color: #8B5CF6;">
    <span class="score-badge" style="background-color: #8B5CF6;">4/5</span>
    <div class="insight-title">Hands-on Coding</div>
    <div class="insight-text">
        I still merge PRs. I focus on high-leverage architectural code (Terraform modules, Base Classes) rather than daily tickets.
    </div>
</div>
"""

# ==========================================
# 2. APP LOGIC
# ==========================================

# --- HELPER FUNCTIONS ---
@st.cache_data
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

# --- SIDEBAR ---
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
    
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120) 
    
    st.markdown("---")
    st.markdown("### 📍 Contact")
    st.write("🏙️ Vancouver, BC, Canada")
    st.write("📧 mail2naren887@gmail.com")
    st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/naren887)")
    
    st.markdown("---")
    st.markdown("### 📥 Actions")
    
    resume_filename = "Narendrakumar_Resume.pdf"
    if os.path.exists(resume_filename):
        with open(resume_filename, "rb") as pdf_file:
            st.download_button(
                label="📄 Download Official Resume",
                data=pdf_file,
                file_name="Narendrakumar_Nagarajan_Resume.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Resume PDF not found in repo.")

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
    st.markdown("### 🚀 Impact at a Glance")
    m1, m2 = st.columns(2)
    m1.metric("Scale Managed", "50 Billion+", "Events / Month")
    m2.metric("Cloud Savings", "$390k+", "Per Year (FinOps)")
    m3, m4 = st.columns(2)
    m3.metric("Compliance", "100%", "SFI & GDPR")
    m4.metric("Team Size", "12+", "Engineers Led")

st.divider()

# --- CHAT AGENT ---
st.subheader("💬 Chat with Narendra's Resume Agent")
st.info("💡 **Ask me anything!** This agent uses RAG (Retrieval Augmented Generation) to answer questions based strictly on my resume PDF.")

if os.path.exists(resume_filename):
    pdf_text = get_pdf_text(resume_filename)
    if pdf_text:
        user_query = st.text_input("Type your question here:", placeholder="Ex: What is his experience with Azure Fabric and FinOps?")
        if user_query:
            if "GROQ_API_KEY" in st.secrets:
                api_key = st.secrets["GROQ_API_KEY"]
                client = Groq(api_key=api_key)
                try:
                    with st.spinner("Analyzing resume..."):
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {"role": "system", "content": f"You are a helpful assistant for Narendrakumar. Answer questions strictly based on the following resume text. If the answer is not in the text, say you don't know. \n\nRESUME TEXT:\n{pdf_text}"},
                                {"role": "user", "content": user_query}
                            ],
                            model="llama-3.3-70b-versatile",
                        )
                        st.success(f"**AI Response:** {chat_completion.choices[0].message.content}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("⚠️ Groq API Key not found in Secrets. Please add it to .streamlit/secrets.toml")
else:
    st.error(f"⚠️ Could not find '{resume_filename}'. Please upload the PDF to your GitHub repository root folder.")

st.divider()

# --- TABS ---
tabs = st.tabs(["💼 Experience", "🛠️ Skills", "⚖️ Leadership", "🎓 Education"])

# --- TAB 1: EXPERIENCE ---
with tabs[0]:
    st.subheader("🛤️ Professional Journey")
    st.markdown(TIMELINE_HTML, unsafe_allow_html=True)
    
    st.markdown("### 🔥 Signature Project Case Studies")
    st.caption("A technical deep-dive into my three most impactful architectural challenges.")

    with st.expander("🚀 Project: The 50-Billion Event Migration to Fabric", expanded=False):
        st.markdown("""
        **The Challenge:** Our legacy telemetry platform (processing 50B+ events/month) was suffering from high latency and spiraling Azure storage costs. We needed to migrate 100+ pipelines without data loss.
        
        **The Architecture:**
        * **Migration Strategy:** Designed a "Dual-Write" pattern to run parallel ingestion into both Legacy (ADLS Gen1) and **Microsoft Fabric (OneLake)**.
        * **Optimization:** implemented **Z-Ordering** and partition pruning on Delta Tables to handle the massive volume.
        
        **The Impact:**
        * **Performance:** Query speeds improved by **40%**.
        * **Reliability:** Ingestion failures dropped near-zero due to the ACID guarantees of Delta Lake.
        """)

    with st.expander("🛡️ Project: 'TICK' - GenAI for Cyber Defense", expanded=False):
        st.markdown("""
        **The Challenge:** Security analysts were drowning in logs. Manual triage of a single threat alert took 20+ minutes.
        
        **The Solution (Agentic AI):**
        * **RAG Architecture:** Built a retrieval system using **Azure AI Foundry** and **Semantic Kernel**.
        * **Logic:** The agent fetches logs from Kusto (KQL), contextualizes them against threat intel feeds, and summarizes the "Blast Radius" for analysts.
        
        **The Impact:**
        * **Efficiency:** Automated 30% of Tier-1 triage tasks.
        * **Speed:** Reduced "Mean Time to Respond" (MTTR) significantly.
        """)

    with st.expander("💰 Project: The $390k FinOps Transformation", expanded=False):
        st.markdown("""
        **The Challenge:** Uncontrolled Databricks cluster usage was bleeding budget. Engineers were spinning up massive GPU clusters for small ETL jobs.
        
        **The Fix:**
        * **Governance:** Implemented **Cluster Policies** to restrict instance types and enforce auto-termination.
        * **Spot Instances:** Migrated fault-tolerant workloads to Azure Spot Instances (80% cheaper).
        
        **The Impact:**
        * **Hard Savings:** **$390,000 USD** saved annually.
        * **Culture:** Instilled a "Cost-Aware Engineering" mindset across the squad.
        """)

# --- TAB 2: SKILLS ---
with tabs[1]:
    st.subheader("🚀 Technical & Leadership Ecosystem")
    st.markdown(SKILLS_CSS, unsafe_allow_html=True)
    
    skill_data = {
        "Technical Architecture 🛠️": [
            {"title": "Modern Data Stack", "skills": ["Microsoft Fabric", "Databricks", "Synapse", "Snowflake", "ADLS Gen2", "OneLake"]},
            {"title": "Languages & Core", "skills": ["Python", "PySpark", "SQL (T-SQL/KQL)", "C#", "Delta Lake"]},
            {"title": "AI & GenAI", "skills": ["Azure AI Foundry", "Semantic Kernel", "RAG Patterns", "Vector DBs", "LLMOps"]},
            {"title": "DevOps & Cloud", "skills": ["Azure DevOps", "Terraform (IaC)", "Docker", "Kubernetes", "CI/CD Pipelines"]},
        ],
        "Strategic Leadership ⚖️": [
            {"title": "Engineering Management", "skills": ["Squad Leadership (10+)", "Hiring & Mentoring", "Performance Reviews", "DataOps Culture"]},
            {"title": "Strategy & Governance", "skills": ["Platform Migration", "SFI Compliance", "Zero Trust Security", "Capacity Planning"]},
            {"title": "FinOps & Efficiency", "skills": ["Cloud Cost Optimization", "Budget Forecasting", "Spot Instance Strategy", "$390k/yr Savings"]},
            {"title": "Operational Excellence", "skills": ["SLA/SLO Definition", "Incident Response", "Root Cause Analysis", "Golden Path Standards"]},
        ]
    }

    tech_html = ""
    for group in skill_data["Technical Architecture 🛠️"]:
        badges = "".join([f'<span class="skill-badge">{s}</span>' for s in group["skills"]])
        tech_html += f"""<div class="skill-card">
<div class="card-header tech-header">{group['title']}</div>
<div class="badge-container">{badges}</div>
</div>"""

    lead_html = ""
    for group in skill_data["Strategic Leadership ⚖️"]:
        badges = "".join([f'<span class="skill-badge">{s}</span>' for s in group["skills"]])
        lead_html += f"""<div class="skill-card">
<div class="card-header lead-header">{group['title']}</div>
<div class="badge-container">{badges}</div>
</div>"""

    st.markdown(f"""
<div class="skill-container">
<div class="skill-column">
<h3 style="text-align:center; color:#0078D4;">Technical Architecture</h3>
{tech_html}
</div>
<div class="skill-column">
<h3 style="text-align:center; color:#D83B01;">Strategic Leadership</h3>
{lead_html}
</div>
</div>
""", unsafe_allow_html=True)

# --- TAB 3: LEADERSHIP DASHBOARD (FIXED) ---
with tabs[2]:
    st.subheader("⚖️ Executive Competency Radar")
    
    col_radar1, col_radar2 = st.columns([3, 2])
    
    with col_radar1:
        # PLOTLY CHART
        categories = ['Strategic Vision', 'People Management', 'Cloud Architecture', 
                      'Coding/Hands-on', 'FinOps/Cost Optimization', 'Governance/SFI']
        values = [5, 5, 5, 4, 5, 5]
        
        df_radar = pd.DataFrame(dict(r=values, theta=categories))
        
        fig_radar = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
        # BUG FIX: changed fill_color to fillcolor
        fig_radar.update_traces(fill='toself', line_color='#0078D4', fillcolor='rgba(0, 120, 212, 0.3)')
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 5], gridcolor='#333', tickfont=dict(color='gray')),
                angularaxis=dict(tickfont=dict(size=14, color='white', weight='bold')),
                bgcolor='rgba(0,0,0,0)'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            height=500,
            margin=dict(l=40, r=40, t=20, b=20)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_radar2:
        st.markdown("### 🔍 Leadership DNA")
        # USE THE GLOBAL HTML VARIABLE TO PREVENT INDENTATION ERRORS
        st.markdown(LEADERSHIP_HTML, unsafe_allow_html=True)

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

