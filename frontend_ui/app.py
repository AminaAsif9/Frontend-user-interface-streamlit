import streamlit as st

st.set_page_config(page_title="LlamaEval", page_icon=":llama:", layout="wide")

# CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- HEADER  ----
with st.container():
    st.subheader("Welcome to :llama:")
    st.title("LlamaEval: Quick Evaluation Dashboard")
    st.write(
        "This tool allows you to input the Llama model output, and it will give you a basic evaluation score."
    )

with st.container():
    st.write("---")
    

# main
st.write("Select Llama models to evaluate and specify a task.")

# combo box for model selection
models = st.multiselect("Select Llama Models", ["Meta Llama Vision Free", "Meta Llama 3.2 90B Instruct Turbo", "Qwen2.5 7B Instruct Turbo", "Custom-Llama"])

task = st.text_input("Enter Evaluation Task")

# evaluation button
if st.button("Run Evaluation") and models and task:
    st.write("Evaluating selected models on the specified task...")
    
    # Panel to show models response and output
    for model in models:

        with st.expander(f"Model: {model} - Task: '{task}'"):
            # Mock result (replace with API integration)
            model_response = f"Mock response from {model} for the task '{task}'"
            expected_output = f"Expected output for the task: [expected result ]"
            
            st.subheader("Model Response")
            st.write(model_response)
            
            st.subheader("Expected Output")
            st.write(expected_output)
            
    # Score Board Panel
    st.write("## Evaluation Scores")
    st.write("---")
    
    # scores, get them from the API response
    scores = {
        "Llama-3": 88.4,
        "Llama-13B": 92.1,
        "Llama-65B": 95.3,
    }
    
    # Display
    score_board = {
        "Model": list(scores.keys()),
        "Score": list(scores.values())
    }
    
    # score table
    st.table(score_board)