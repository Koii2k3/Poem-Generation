import streamlit as st
from transformers import pipeline


st.set_page_config(
    page_title="AIVN - RAG with Llama Index",
    page_icon="./static/aivn_favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.image("./static/aivn_logo.png", width=300)

st.title("Vietnamese Poem Generation")
st.write("The used model is GPT-2 trained on Vietnamese poems: thangduong0509/gpt2_viet_poem_generation")

with st.expander("Hướng dẫn sử dụng"):
    st.write("""
    1. Nhập một vài từ hoặc câu làm gợi ý cho bài thơ
    2. Điều chỉnh các thông số để thay đổi cách sinh thơ:
       - Temperature: Giá trị cao hơn tạo ra kết quả đa dạng hơn
       - Top-k: Số lượng từ có xác suất cao nhất để chọn ở mỗi bước
       - Top-p: Ngưỡng xác suất tích lũy để chọn từ
       - Repetition penalty: Điều chỉnh để tránh lặp lại
    3. Nhấn nút "Sinh thơ" để tạo bài thơ
    4. Bạn có thể tải về bài thơ đã sinh bằng nút "Tải về bài thơ"
    """)

prompt_input = st.text_area("Nhập vài từ hoặc câu để bắt đầu:", 
                          value="Con sông quê tôi đẹp\n", 
                          height=100)

col1, empty_col, col2 = st.columns([0.5, 0.5, 1.0]) 
with col1:
    max_length = st.slider("Max Output Tokens:", 10, 200, 75)
    temperature = st.slider("Temperature:", 0.1, 1.5, 0.8)
    top_k = st.slider("Top-k:", 1, 100, 50)
    top_p = st.slider("Top-p:", 0.1, 1.0, 0.95)
    repetition_penalty = st.slider("Repetition Penalty:", 1.0, 2.0, 1.2)
    
with empty_col:
    st.empty()

with col2:
    if st.button("Sinh thơ"):
        with st.spinner("Đang sinh thơ..."):
            try:
                # Khởi tạo model
                generator = pipeline('text-generation', 
                                    model='thangduong0509/gpt2_viet_poem_generation')
                
                # Sinh thơ
                results = generator(
                    prompt_input,
                    max_new_tokens=max_length,
                    do_sample=True,
                    top_k=top_k,
                    top_p=top_p,
                    temperature=temperature,
                    repetition_penalty=repetition_penalty
                )
                
                # Hiển thị kết quả
                generated_text = results[0]['generated_text']
                st.subheader("Bài thơ đã sinh:")
                
                # Hiển thị từng dòng
                for line in generated_text.split('\n'):
                    st.write(line)
                
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {str(e)}")

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        color: #555;
    }
    </style>
    <div class="footer">
        2024 AI VIETNAM | Made by <a href="https://github.com/Koii2k3/Basic-RAG-LlamaIndex" target="_blank">Koii2k3</a>
    </div>
    """,
    unsafe_allow_html=True
)