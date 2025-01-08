import streamlit as st
import pickle

# Load the model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

# Header Section
st.set_page_config(page_title="Email Spam Classifier", page_icon="📧")
st.title("📧 Email Spam Classifier")
st.markdown("""
Welcome to the **Email Spam Classification App**!  
This tool leverages **Machine Learning** to help you identify whether an email is spam or legitimate (ham).  
Whether you're battling email clutter or ensuring important messages aren't lost, this app is here to help!  
""")

# Sidebar for additional details
st.sidebar.title("ℹ️ About the App")
st.sidebar.markdown("""
This application uses a pre-trained **ML model** to classify emails based on their content.  
### How it works:
1. **Input**: Paste the email text in the box provided.  
2. **Process**: The app converts text into numerical data using a vectorizer.  
3. **Predict**: The trained model predicts whether the email is spam or not.  
""")

# Input Section
st.markdown("### 📝 Enter Your Email Content Below")
user_input = st.text_area(
    label="Paste the email text you want to classify:",
    height=200,
    placeholder="e.g., 'You’ve won a $1000 gift card! Click here to claim your prize...'"
)

# Classification Button
if st.button("🚀 Classify Email"):
    if user_input.strip():  # Ensure input is provided
        st.markdown("### 📊 Classification Result")
        
        # Process and predict
        data = [user_input]
        vectorized_data = cv.transform(data).toarray()
        result = model.predict(vectorized_data)
        
        # Display results with detailed messages
        if result[0] == 0:
            st.success("✅ **Result**: This email is **NOT SPAM**. It appears to be legitimate!")
            st.markdown("""
            **Next Steps**:  
            - Feel free to respond if the sender is trusted.  
            - Always verify the sender's email address for security.  
            """)
        else:
            st.error("⚠️ **Result**: This email is classified as **SPAM**.")
            st.markdown("""
            **Tips to Stay Safe**:  
            - Avoid clicking on suspicious links or attachments.  
            - Mark such emails as spam in your inbox to block future emails.  
            - If unsure, contact the sender through verified channels.  
            """)
    else:
        st.warning("⚠️ Please enter the email content before classification.")

# Footer with helpful tips
st.markdown("""
---
### Quick Email Safety Tips:
- Be cautious of emails that request sensitive information.  
- Check for spelling errors and generic greetings (e.g., "Dear User").  
- Use spam filters and antivirus software to enhance email security.  
""")

# Add footer branding
st.markdown("""
---
#### Developed by: [Satkar Garje](#) 
""")
