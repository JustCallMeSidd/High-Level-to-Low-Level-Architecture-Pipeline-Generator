import streamlit as st
from prompt import FINAL_PROMPT
from llm_client import generate_architecture

st.set_page_config(page_title="Architecture Generator", layout="wide")

# Custom CSS for modern grey/black theme with animations
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Title styling with fade-in animation */
    h1 {
        color: #ffffff !important;
        font-weight: 700 !important;
        text-align: center;
        padding: 2rem 0;
        animation: fadeInDown 0.8s ease-out;
        background: linear-gradient(135deg, #ffffff 0%, #a0a0a0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
        border: 2px solid #3a3a3a !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #666666 !important;
        box-shadow: 0 0 20px rgba(100, 100, 100, 0.3) !important;
        transform: translateY(-2px);
    }
    
    .stTextArea label {
        color: #cccccc !important;
        font-weight: 600 !important;
        font-size: 18px !important;
    }
    
    /* Button styling with hover animation */
    .stButton button {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%) !important;
        color: #ffffff !important;
        border: 2px solid #3a3a3a !important;
        border-radius: 12px !important;
        padding: 0.75rem 3rem !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #3a3a3a 0%, #2a2a2a 100%) !important;
        border-color: #666666 !important;
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(100, 100, 100, 0.3) !important;
    }
    
    /* Success/Warning messages */
    .stSuccess, .stWarning {
        background-color: #2a2a2a !important;
        border-radius: 12px !important;
        border-left: 4px solid #666666 !important;
        animation: slideInRight 0.5s ease-out;
    }
    
    .stSuccess p, .stWarning p {
        color: #ffffff !important;
    }
    
    /* Markdown headers */
    h3 {
        color: #cccccc !important;
        font-weight: 600 !important;
        margin-top: 2rem !important;
        animation: fadeIn 0.6s ease-out;
    }
    
    /* Code block styling */
    .stCodeBlock {
        background-color: #1a1a1a !important;
        border: 2px solid #3a3a3a !important;
        border-radius: 12px !important;
        animation: fadeIn 0.8s ease-out;
    }
    
    .stCodeBlock code {
        color: #e0e0e0 !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-color: #666666 !important;
        border-right-color: transparent !important;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Placeholder text */
    .stTextArea textarea::placeholder {
        color: #666666 !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a1a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #3a3a3a;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #4a4a4a;
    }
</style>
""", unsafe_allow_html=True)
st.title("🧠")
st.title("High → Low Level Architecture Generator")

requirement = st.text_area(
    "Enter Business Requirement",
    height=200,
    placeholder="Example: Build an online food delivery system..."
)

if st.button("Generate Architecture"):
    if not requirement.strip():
        st.warning("Please enter a business requirement.")
    else:
        with st.spinner("Generating architecture..."):
            full_prompt = FINAL_PROMPT.format(requirement=requirement)
            result = generate_architecture(full_prompt)

        st.success("Architecture Generated Successfully")
        st.markdown("### 📐 Generated Architecture")
        st.code(result, language="markdown")