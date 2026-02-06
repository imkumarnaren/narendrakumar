import os
from datetime import datetime

import pandas as pd
import plotly.express as px
import PyPDF2
import streamlit as st
from groq import Groq

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Narendrakumar Nagarajan | Data & AI Engineering Manager",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# GLOBAL HTML/CSS (FLUSH LEFT)
# ==========================================

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
    <div class="timeline-dot" style="background-color: #0078D4;"></div>
    <div class="timeline-date">Sep 2025 – Present</div>
    <div class="timeline-title">Technology Lead (Infosys) — Engineering Delivery Lead (Microsoft Cyber Defense Engineering)</div>
    <div class="timeline-desc">
      Leading delivery for security-first data/automation platforms supporting cyber defense.
      <ul>
        <li>Program/engineering leadership for <span class="highlight">ARIS</span> (Microsoft Foundry, Logic Apps, Synapse, ADLS Gen2, Kusto).</li>
        <li>Drive <b>production readiness</b>, release governance, RAID, and zero-downtime delivery for mission-critical systems.</li>
        <li>Security execution: <b>SFI-aligned</b> engineering, credential hygiene, and delivery governance across vendor workstreams.</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background-color: #8B5CF6;"></div>
    <div class="timeline-date">Sep 2024 – Aug 2025</div>
    <div class="timeline-title">Technology Lead (Infosys) — SFI Execution Lead (Microsoft Gaming)</div>
    <div class="timeline-desc">
      Security-first engineering leadership across data engineering, data science, and services teams.
      <ul>
        <li>Achieved <span class="highlight">100% SFI compliance</span> across all 6 security pillars via KPI closure and governance.</li>
        <li>Led threat modeling, tenant security assessments, secrets hygiene, cross-tenant auth patterns, and network hardening (NSG/NSP).</li>
        <li>Enabled 50+ stakeholders with remediation playbooks and execution cadence.</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background-color: #2ecc71;"></div>
    <div class="timeline-date">May 2019 – Aug 2024</div>
    <div class="timeline-title">Technology Lead (Infosys) — Data Platform Lead / Product Manager (Microsoft CX&S)</div>
    <div class="timeline-desc">
      Built and scaled an enterprise telemetry lakehouse processing <span class="highlight">50B+ events/month</span>.
      <ul>
        <li>Led <span class="highlight">Microsoft Fabric migration</span> of <b>100+ pipelines</b> with <b>zero downtime</b> and <b>40% performance improvement</b>.</li>
        <li>FinOps: delivered <span class="highlight">$240K/year</span> savings via Databricks optimization and reduced infra spend by <b>40%</b>.</li>
        <li>Managed and mentored <b>8 Infosys data engineers</b>; peak leadership <b>12</b> (direct + matrix).</li>
        <li>Implemented GDPR-aligned retention/privacy controls and automated reliability (80% less manual intervention).</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background-color: #95a5a6;"></div>
    <div class="timeline-date">Aug 2016 – Apr 2019</div>
    <div class="timeline-title">Technology Lead (Infosys) — Data Platform Lead & Architect</div>
    <div class="timeline-desc">
      Modernized BI and reporting platforms; enabled Azure adoption at scale.
      <ul>
        <li>On-prem to Azure migration saving <span class="highlight">$150K/year</span> in server maintenance.</li>
        <li>Designed data models for <b>150+ entities</b> and delivered <b>40+ Power BI dashboards</b> for 500+ stakeholders.</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background-color: #95a5a6;"></div>
    <div class="timeline-date">Feb 2014 – Jul 2016</div>
    <div class="timeline-title">Senior Software Engineer — Accenture</div>
    <div class="timeline-desc">
      Built high-volume financial ETL and automation.
      <ul>
        <li>Designed end-to-end SSIS ETL for royalty calculation and distribution.</li>
        <li>Built automated test data tooling reducing QA cycle time by <b>20%</b>.</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background-color: #95a5a6;"></div>
    <div class="timeline-date">Dec 2011 – Jan 2014</div>
    <div class="timeline-title">Software Engineer — Carevoyant</div>
    <div class="timeline-desc">
      Healthcare interoperability and backend engineering.
      <ul>
        <li>Developed HL7 parsers and SSIS ingestion for EHR interoperability.</li>
        <li>Optimized SQL Server stored procedures and built WCF services for throughput-critical workflows.</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background-color: #95a5a6;"></div>
    <div class="timeline-date">Sep 2010 – Nov 2011</div>
    <div class="timeline-title">Software Engineer — Medall Healthcare</div>
    <div class="timeline-desc">
      Data warehousing and enterprise reporting.
      <ul>
        <li>Built data marts, ETL (SSIS), reporting (SSRS), and analysis models (SSAS).</li>
      </ul>
    </div>
  </div>

</div>
"""

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
  <div class="insight-title">Engineering Leadership</div>
  <div class="insight-text">
    People manager for 8 Infosys engineers (2019–2024); currently lead 3 direct reports and matrix execution for 6 Microsoft FTEs. Own sprint cadence, prioritization, and delivery accountability.
  </div>
</div>

<div class="insight-card" style="border-left-color: #2ecc71;">
  <span class="score-badge" style="background-color: #2ecc71;">5/5</span>
  <div class="insight-title">Data Platform Ownership (Scale + Reliability)</div>
  <div class="insight-text">
    Built/ran platforms processing 50B+ events/month. Zero-downtime migration of 100+ pipelines; automated monitoring/remediation reduced manual intervention by 80%.
  </div>
</div>

<div class="insight-card" style="border-left-color: #f59e0b;">
  <span class="score-badge" style="background-color: #f59e0b;">5/5</span>
  <div class="insight-title">FinOps / Cost Governance</div>
  <div class="insight-text">
    Delivered $390K+/year savings ($240K/year Databricks optimization + $150K/year migration savings). Drove policy-based controls and engineering cost discipline.
  </div>
</div>

<div class="insight-card" style="border-left-color: #8B5CF6;">
  <span class="score-badge" style="background-color: #8B5CF6;">5/5</span>
  <div class="insight-title">Security-first Engineering (SFI)</div>
  <div class="insight-text">
    Achieved 100% SFI compliance across all 6 pillars. Led threat modeling, secrets hygiene, tenant isolation guidance, network hardening, and KPI closure governance.
  </div>
</div>
"""

# ==========================================
# APP LOGIC
# ==========================================


@st.cache_data
def get_pdf_text(filename: str):
    try:
        with open(filename, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
            return text.strip()
    except FileNotFoundError:
        return None


def load_groq_client():
    # Support both Streamlit Cloud secrets and env var usage
    api_key = None
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
    if not api_key:
        api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return None
    return Groq(api_key=api_key)


# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## Narendrakumar Nagarajan")
    st.caption("Data & AI Engineering Manager | Fabric | Databricks | Security-first delivery")

    st.markdown("**Target Roles:**")
    st.markdown(
        "- Data & AI Engineering Manager\n"
        "- Data Platform Manager\n"
        "- Data Engineering Manager\n"
    )

    st.markdown("---")
    st.markdown("### Location")
    st.write("Vancouver, BC, Canada")

    st.markdown("### Profiles")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/naren887)")

    st.markdown("---")
    st.markdown("### Download")
    resume_filename = "Narendrakumar_Resume.pdf"
    if os.path.exists(resume_filename):
        with open(resume_filename, "rb") as pdf_file:
            st.download_button(
                label="Download Resume (PDF)",
                data=pdf_file,
                file_name="Narendrakumar_Nagarajan_Resume.pdf",
                mime="application/pdf",
            )
    else:
        st.warning("Resume PDF not found. Add 'Narendrakumar_Resume.pdf' to the app folder/repo root.")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Professional Summary")
    st.markdown(
        """
I’m a **Data & AI Engineering Manager / Data Platform Leader** with **15+ years** building secure, enterprise-scale platforms on Azure.

- Built and operated telemetry platforms processing **50B+ events/month**
- Led **100+ pipeline migrations** to **Microsoft Fabric** with **zero downtime** and **40% performance improvement**
- Delivered **$390K+/year savings** through Databricks optimization (**$240K/yr**) and migration outcomes (**$150K/yr**)
- Led teams up to **12 engineers** (people management + matrix leadership), with hands-on governance: **architecture reviews, PR approvals, code reviews**
- Drove **100% SFI compliance** across all 6 pillars via threat modeling, KPI closure, and secure engineering patterns
        """.strip()
    )

with col2:
    st.markdown("### Impact at a Glance")
    m1, m2 = st.columns(2)
    m1.metric("Scale", "50B+", "events/month")
    m2.metric("Savings", "$390K+", "per year")
    m3, m4 = st.columns(2)
    m3.metric("SFI", "100%", "compliance")
    m4.metric("Team", "12", "peak led")

st.divider()

# --- CHAT AGENT ---
st.subheader("Resume Q&A Agent")
st.caption("Answers strictly from your resume PDF using RAG-style grounding (resume text only).")

if os.path.exists("Narendrakumar_Resume.pdf"):
    pdf_text = get_pdf_text("Narendrakumar_Resume.pdf")
    if pdf_text:
        user_query = st.text_input(
            "Ask a question:",
            placeholder="Example: What is his experience with Microsoft Fabric and Databricks cost optimization?",
        )
        if user_query:
            client = load_groq_client()
            if not client:
                st.warning("Groq API key missing. Add GROQ_API_KEY to Streamlit secrets or environment variables.")
            else:
                try:
                    with st.spinner("Analyzing resume..."):
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {
                                    "role": "system",
                                    "content": (
                                        "You are a helpful assistant answering questions strictly using the resume text. "
                                        "If the answer is not in the text, say you don't know.\n\n"
                                        f"RESUME TEXT:\n{pdf_text}"
                                    ),
                                },
                                {"role": "user", "content": user_query},
                            ],
                            model="llama-3.3-70b-versatile",
                        )
                        st.success(chat_completion.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.error("Could not extract text from the PDF. Ensure the PDF contains selectable text (not only images).")
else:
    st.info("Upload 'Narendrakumar_Resume.pdf' to enable Q&A and the download button.")

st.divider()

# --- TABS ---
tabs = st.tabs(["Experience", "Skills", "Leadership", "Education"])

# --- TAB 1: EXPERIENCE ---
with tabs[0]:
    st.subheader("Professional Journey")
    st.markdown(TIMELINE_HTML, unsafe_allow_html=True)

    st.markdown("### Signature Case Studies")

    with st.expander("Project: 50B+ event telemetry platform + Fabric migration (100+ pipelines)", expanded=False):
        st.markdown(
            """
**Context:** Enterprise telemetry platform processing **50B+ events/month** for global support channels.

**What I led:**
- Execution leadership for **100+ pipeline migration** to **Microsoft Fabric**
- Release readiness + phased rollout to maintain **zero downtime**
- Performance + reliability improvements across ingestion and analytics

**Results:**
- **40% performance improvement**
- Reduced operational burden through standardization and automation
            """.strip()
        )

    with st.expander("Project: Databricks optimization + cost governance (FinOps)", expanded=False):
        st.markdown(
            """
**Problem:** High and unpredictable Databricks spend due to suboptimal clusters and job patterns.

**What I did:**
- Cluster right-sizing + usage governance
- PySpark performance tuning and operational automation
- Cost-aware engineering practices

**Results:**
- **$20K+/month savings** (**$240K/year**)
- **40% reduction** in infrastructure spending
            """.strip()
        )

    with st.expander("Project: Security-first engineering with SFI (100% compliance)", expanded=False):
        st.markdown(
            """
**Scope:** Led compliance execution across all **6 SFI pillars**.

**What I drove:**
- Threat modeling sessions and remediation planning
- Secrets hygiene and authentication patterns
- Network hardening (NSG/NSP) and vulnerability management governance

**Results:**
- **100% SFI compliance** with measurable KPI closure
            """.strip()
        )

# --- TAB 2: SKILLS ---
with tabs[1]:
    st.subheader("Technical & Leadership Skills")
    st.markdown(SKILLS_CSS, unsafe_allow_html=True)

    skill_data = {
        "Technical": [
            {
                "title": "Data Platforms",
                "skills": ["Microsoft Fabric", "Azure Databricks", "Synapse Analytics", "ADLS Gen2", "Kusto (KQL)", "Azure Data Factory"],
            },
            {
                "title": "Engineering",
                "skills": ["Python", "PySpark", "SQL (T-SQL)", "KQL", "CI/CD (Azure DevOps)", "Git"],
            },
            {
                "title": "Automation & Integration",
                "skills": ["Logic Apps", "Azure Functions", "REST APIs", "Event Hubs", "Cosmos DB", "Power BI"],
            },
            {
                "title": "AI Enablement",
                "skills": ["Azure AI Foundry / Microsoft Foundry", "OpenAI/LLM integration", "Copilot patterns", "Agentic workflows"],
            },
        ],
        "Leadership": [
            {
                "title": "Engineering Management",
                "skills": ["People management", "Matrix leadership", "Sprint ceremonies", "Backlog prioritization", "Stakeholder management"],
            },
            {
                "title": "Technical Governance",
                "skills": ["Architecture reviews", "PR approvals", "Code reviews", "Release readiness", "Production readiness"],
            },
            {
                "title": "Security & Compliance",
                "skills": ["Secure Future Initiative (SFI)", "Threat modeling", "Secrets hygiene", "Tenant isolation", "Network hardening (NSG/NSP)"],
            },
            {
                "title": "FinOps / Cost Optimization",
                "skills": ["Databricks optimization", "$240K/year savings", "Cost governance", "Right-sizing", "Automation"],
            },
        ],
    }

    def render_cards(groups, header_class):
        html = ""
        for group in groups:
            badges = "".join([f'<span class="skill-badge">{s}</span>' for s in group["skills"]])
            html += f"""
<div class="skill-card">
  <div class="card-header {header_class}">{group['title']}</div>
  <div class="badge-container">{badges}</div>
</div>
"""
        return html

    tech_html = render_cards(skill_data["Technical"], "tech-header")
    lead_html = render_cards(skill_data["Leadership"], "lead-header")

    st.markdown(
        f"""
<div class="skill-container">
  <div class="skill-column">
    <h3 style="text-align:center; color:#0078D4;">Technical</h3>
    {tech_html}
  </div>
  <div class="skill-column">
    <h3 style="text-align:center; color:#D83B01;">Leadership</h3>
    {lead_html}
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# --- TAB 3: LEADERSHIP ---
with tabs[2]:
    st.subheader("Leadership Snapshot")

    col_radar1, col_radar2 = st.columns([3, 2])

    with col_radar1:
        categories = [
            "People Management",
            "Delivery / Execution",
            "Platform Architecture",
            "Hands-on Governance",
            "FinOps",
            "Security (SFI)",
        ]
        values = [5, 5, 5, 5, 5, 5]

        df_radar = pd.DataFrame(dict(r=values, theta=categories))
        fig_radar = px.line_polar(df_radar, r="r", theta="theta", line_close=True)
        fig_radar.update_traces(
            fill="toself", line_color="#0078D4", fillcolor="rgba(0, 120, 212, 0.3)"
        )
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 5], gridcolor="#333", tickfont=dict(color="gray")),
                angularaxis=dict(tickfont=dict(size=14, color="white")),
                bgcolor="rgba(0,0,0,0)",
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            height=500,
            margin=dict(l=40, r=40, t=20, b=20),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_radar2:
        st.markdown("### Leadership DNA")
        st.markdown(LEADERSHIP_HTML, unsafe_allow_html=True)

# --- TAB 4: EDUCATION ---
with tabs[3]:
    st.subheader("Certifications & Education")
    col_e1, col_e2 = st.columns(2)

    with col_e1:
        st.markdown("**Certifications**")
        st.write("Microsoft Certified: Fabric Analytics Engineer Associate (DP-600)")
        st.write("Microsoft Certified: Azure AI Engineer Associate (AI-102)")
        st.write("Microsoft Certified: Azure AI Fundamentals (AI-900)")

    with col_e2:
        st.markdown("**Education**")
        st.write("Bachelor of Engineering (B.E.), Computer Science")
        st.write("Anna University, Chennai, India (2010)")

st.markdown("---")
st.caption(f"© {datetime.now().year} Narendrakumar Nagarajan | Built with Streamlit")
