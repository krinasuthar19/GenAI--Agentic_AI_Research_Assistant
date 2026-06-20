import streamlit as st
from graph import app

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Agentic AI Research Assistant",
    page_icon="🔬",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.main{
padding-top:0rem;
}

.stApp{
background: linear-gradient(
135deg,
#0f172a,
#111827,
#1e293b
);
}

.hero{
text-align:center;
padding:20px;
}

.title{
font-size:55px;
font-weight:800;

background: linear-gradient(
90deg,
#00f5ff,
#6a5cff,
#ff4ecd
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
font-size:18px;
color:#cbd5e1;
}

.glass{

background: rgba(255,255,255,0.08);

backdrop-filter: blur(14px);

padding:25px;

border-radius:25px;

border:1px solid rgba(255,255,255,0.15);

margin-top:20px;
}

.tech{

background: rgba(255,255,255,0.06);

padding:12px;

border-radius:15px;

text-align:center;

font-weight:600;

}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown("""
<div class='hero'>

<div class='title'>
🔬 Agentic AI Research Assistant
</div>

<div class='subtitle'>
Search • Analyze • Generate • Critique
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("⚙️ Workflow")

    st.success("🔎 Research Agent")

    st.info("🌐 Content Extraction")

    st.warning("✍️ Report Generation")

    st.error("🧐 Quality Evaluation")

    st.divider()

    st.markdown("### 🛠 Tech Stack")

    st.write("• LangGraph")

    st.write("• LangChain")

    st.write("• Mistral AI")

    st.write("• Tavily")

    st.write("• BeautifulSoup")

    st.write("• LCEL")

# ---------------- INPUT ----------------

topic = st.text_input(
    "",
    placeholder="🔍 Ask me to research anything..."
)

# ---------------- BUTTON ----------------

if st.button(
    "🚀 Generate Research Report",
    use_container_width=True
):

    if topic:

        with st.spinner("🧠 Agents are working..."):

            result = app.invoke({
                "topic":topic
            })

        st.success("Workflow Completed")

        # ---------- METRICS ----------

        c1,c2,c3,c4 = st.columns(4)

        c1.metric("🔎 Search","Done")

        c2.metric("🌐 Scrape","Done")

        c3.metric("✍️ Report","Done")

        c4.metric("🧐 Review","Done")

        # ---------- REPORT ----------

        col1,col2 = st.columns([3,1])

        with col1:

            st.markdown("""
            <div class='glass'>
            <h2>📄 Research Report</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(result["report"])

        with col2:

            st.markdown("""
            <div class='glass'>
            <h2>📝 Critic Feedback</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(result["feedback"])

        st.divider()

        st.markdown("### ⚡ Powered By")

        t1,t2,t3,t4,t5,t6 = st.columns(6)

        t1.markdown("<div class='tech'>LangGraph</div>",unsafe_allow_html=True)

        t2.markdown("<div class='tech'>LangChain</div>",unsafe_allow_html=True)

        t3.markdown("<div class='tech'>Mistral</div>",unsafe_allow_html=True)

        t4.markdown("<div class='tech'>Tavily</div>",unsafe_allow_html=True)

        t5.markdown("<div class='tech'>BeautifulSoup</div>",unsafe_allow_html=True)

        t6.markdown("<div class='tech'>LCEL</div>",unsafe_allow_html=True)

    else:

        st.warning("Please enter a topic.")