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

# --- FUNCTION TO READ PDF (Cached for Performance) ---
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

# --- CUSTOM CSS FOR "10/10" LOOK ---
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        color: #000000 !important;
    }
    div[data-testid="stMetric"] * { color: #2c3e50 !important; }
    div[data-testid="stMetricLabel"] p, div[data-testid="stMetricLabel"] div, div[data-testid="stMetricLabel"] span { color: #6c757d !important; }
    div[data-testid="stMetricDelta"] div, div[data-testid="stMetricDelta"] svg { color: #10B981 !important; }
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

# --- TOP SECTION: CHAT WITH RESUME (AI AGENT) ---
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

# --- TABS FOR DETAILED VIEW ---
tabs = st.tabs(["💼 Experience", "🛠️ Skills", "🤖 AI & Leadership", "🎓 Education"])

# --- TAB 1: EXPERIENCE (TIMELINE FIXED) ---
with tabs[0]:
    st.subheader("🛤️ Professional Journey")
    
    # WE USE A SINGLE MARKDOWN CALL HERE TO PREVENT RAW TEXT OUTPUT
    st.markdown("""
    <style>
        .timeline-container { border-left: 4px solid #e0e0e0; margin-left: 20px; padding-left: 30px; position: relative; }
        .timeline-item { margin-bottom: 40px; position: relative; }
        .timeline-dot { width: 20px; height: 20px; background-color: #0078D4; border-radius: 50%; position: absolute; left: -42px; top: 5px; border: 4px solid white; box-shadow: 0 0 0 1px #e0e0e0; }
        .timeline-date { font-weight: bold; color: #0078D4; font-size: 14px; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px; }
        .timeline-title { font-size: 18px; font-weight: 700; color: #2c3e50; margin-bottom: 8px; }
        .timeline-desc { color: #555; font-size: 15px; line-height: 1.6; }
        .highlight { background-color: #f0f2f6; padding: 2px 6px; border-radius: 4px; font-weight: 600; font-size: 0.9em; }
    </style>
    
    <div class="timeline-container">
        
        <div class="timeline-item">
            <div class="timeline-dot" style="background-color: #8B5CF6;"></div>
            <div class="timeline-date">Sep 2024 – Present</div>
            <div class="timeline-title">Principal Data Engineer & Squad Lead (Cyber Defense)</div>
            <div class="timeline-desc">
                Leading the integration of <b>Generative AI</b> into Security Operations at Microsoft.
                <ul>
                    <li>Architected the <span class="highlight">TICK Agent</span> using Azure AI Foundry & Semantic Kernel.</li>
                    <li>Led the <b>Secure Future Initiative (SFI)</b> achieving 100% compliance.</li>
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
            <div class="timeline-date">2010 – 2016</div>
            <div class="timeline-title">Senior Software Engineer (Accenture & Medall)</div>
            <div class="timeline-desc">
                Built the rigorous backend engineering foundation in <b>C#, .NET, and SQL Server</b>.
                <ul>
                    <li>Designed financial ETL systems for <b>Accenture</b>.</li>
                    <li>Developed HL7 healthcare parsers for <b>Carevoyant</b>.</li>
                </ul>
            </div>
