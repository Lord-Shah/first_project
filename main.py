import streamlit as st
from google import genai
from dotenv import load_dotenv
import time
load_dotenv()
client = genai.Client()
st.set_page_config(
    page_title="Travel Assistant",
    page_icon="🧳",
    layout="wide",
    
)
st.title("🧳Travel Assistant 🗺")
dest= st.text_input("✈️ Where to?")
days= st.number_input("⌛️ How long does this trip last?", min_value=1, max_value=20)
budget = st.selectbox("Select your budget.", ("Luxury: Over ₹5,00,000", "Moderate: Over ₹3,00,000", "Standard: Over ₹1,00,000"))
trip_type= st.radio("Companions?", ["Family", "Friends", "Plus One", "Solo"])
data= st.text_area("Enter any additional pointers or notes.")
prompt=f"""You are a travel planner. You will
plan a trip to {dest} for {str(days)} number of days. Keep in mind {data}
With a budget of {budget}, travelling with {trip_type}Let the plan be detailed, crisp
and bullet format for day after day. Make is SFW and polite, but not too amiable either."""
page_bg_css = """
<style>
/* Animated Emerald Green Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #064e3b, #047857, #065f46, #022c22);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Inter', sans-serif;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating particle effect simulation */
.stApp::before {
    content: "";
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-image: radial-gradient(white 1px, transparent 0);
    background-size: 50px 50px;
    opacity: 0.15;
    animation: drift 60s linear infinite;
    pointer-events: none;
}

@keyframes drift {
    from { background-position: 0 0; }
    to { background-position: 1000px 1000px; }
}

/* --- FORCE ALL GENERAL TEXT & LABELS TO GOLDEN --- */
.stApp, .stApp *, 
h1, h2, h3, h4, h5, h6, 
p, label, span, div, li, 
.stMarkdown, .stSelectbox, .stRadio, .stSpinner {
    color: #FFD700 !important;
}

/* Titles & Headers extra glow */
h1, h2, h3, h4, h5, h6 {
    text-shadow: 0px 0px 8px rgba(255, 215, 0, 0.4);
}

/* Glassmorphism Container */
.travel-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 215, 0, 0.3);
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    color: #FFD700 !important;
}

/* --- TEXT INPUT BOXES (Black typed text inside light gold background) --- */
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    background-color: rgba(255, 250, 235, 0.95) !important;
    color: #000000 !important;
    border: 1.5px solid #FFD700 !important;
    border-radius: 8px;
}

.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: rgba(120, 90, 0, 0.7) !important;
}

/* --- SELECTBOX & DROPDOWN OPTIONS (Golden theme) --- */
div[data-baseweb="select"] > div {
    background-color: rgba(6, 78, 59, 0.8) !important;
    border: 1px solid #FFD700 !important;
    color: #FFD700 !important;
}

/* --- BUTTON STYLING (Golden contrast) --- */
.stButton button, .stButton button p, .stButton button span {
    color: #000000 !important;
}

.stButton button {
    background: linear-gradient(135deg, #FFD700, #FFA500) !important;
    border: none !important;
    font-weight: 700 !important;
    box-shadow: 0px 4px 12px rgba(255, 215, 0, 0.3);
}

.stButton button:hover {
    background: linear-gradient(135deg, #FFE55C, #FFB733) !important;
    color: #000000 !important;
}
</style>
"""

# Inject CSS into Streamlit
st.markdown(page_bg_css, unsafe_allow_html=True)
if st.button("All Set!"):
    st.success(f"The hols to {dest} last {days} days. Cheers to the good times!!!")
    interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
            )
    with st.spinner("Almost there...", show_time=True):
        time.sleep(5)
    st.write(interaction.output_text)