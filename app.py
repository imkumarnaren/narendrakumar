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

# --- 1. GLOBAL VARIABLES (FLUSH LEFT TO PREVENT HTML ERRORS) ---

# TIMELINE HTML
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
<div class="timeline-title">Principal Data Engineer & Squad Lead (Cyber Defense)</div>
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
<div class="timeline-date">2010 – 2016</div>
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

# SKILLS CSS (FLUSH LEFT)
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
    .skill-card { background-color: #1e1e1e; border-color
