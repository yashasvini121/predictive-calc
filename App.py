import streamlit as st

st.set_page_config(page_title="Predictive Calc - Machine Learning Models", page_icon="🤖")

st.title("Welcome to Predictive Calc!")

st.markdown("""
## Explore Cutting-Edge Machine Learning Models
**Predictive Calc** offers a powerful suite of machine learning models designed to assist you in making informed decisions. Whether it's predicting house prices, determining loan eligibility, or evaluating health risks, we have you covered.
""")

st.markdown("""
## Why Choose Predictive Calc? """)
features = [
    {
        "title": "Accurate Predictions",
        "icon": "🔍",
        "description": "Harness cutting-edge machine learning algorithms that provide reliable and precise predictions."
    },
    {
        "title": "User-Friendly Interface",
        "icon": "💻",
        "description": "Enjoy a seamless, intuitive experience with models designed for practical applications across various domains."
    },
    {
        "title": "Comprehensive Calculators",
        "icon": "📊",
        "description": "Access a diverse set of models for financial analysis, health assessments, security checks, and more, all in one place."
    },
    {
        "title": "Health & Financial Insights",
        "icon": "🏥💰",
        "description": "From estimating house prices and checking loan eligibility to evaluating health risks like Parkinson’s and stress levels, Predictive Calc offers essential tools for everyday decision-making."
    },
    {
        "title": "Enhanced Document Analysis & Language Tools",
        "icon": "📄🌐",
        "description": "With a built-in text summarizer and translator, streamline your reading experience and break language barriers effortlessly. PDF Malware Detection also helps keep your documents safe."
    }
]

# Display features in a structured card format
for feature in features:
    st.markdown(
        f"""
        <div style='
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            display: flex;
            align-items: center;
			color: black;
        '>
            <span style='font-size: 2em; margin-right: 15px;'>{feature["icon"]}</span>
            <div>
                <h4 style='margin: 0; color:black;'>{feature["title"]}</h4>
                <p style='margin: 5px 0; color:black;'>{feature["description"]}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown("## Available Calculators")

# Calculator information in a structured format
calculators = [
    {
        "name": "Income Estimator",
        "description": "Estimate the annual income based on socio-economic and demographic information.",
        "details": """
        This calculator uses demographic and socio-economic variables to predict income level, providing insights into income patterns.
        """
    },
    {
        "name": "Gold Price Predictor",
        "description": "Predict future gold prices using various financial metrics.",
        "details": """
            ### Introduction
            The Gold Price Predictor leverages financial metrics and machine learning algorithms to forecast the price of gold (GLD). Gold prices are influenced by various economic factors, and this tool aims to provide accurate predictions based on historical data.

            ### Gold Price Dataset
            The dataset used for this model contains daily financial data, including stock market indices, commodity prices, and currency exchange rates. The goal is to predict the gold price (GLD) using features such as the S&P 500 Index (SPX), crude oil price (USO), silver price (SLV), and the EUR/USD exchange rate.

            ### Additional Variable Information
            - **SPX**:  The S&P 500 index value, which tracks the performance of 500 large companies listed on stock exchanges in the United States.
            - **USO**:  The price of United States Oil Fund (USO), which reflects crude oil prices.
            - **SLV**:  The price of iShares Silver Trust (SLV), which reflects silver prices.
            - **EUR/USD**:  The Euro-to-U.S. Dollar exchange rate, which indicates the strength of the euro relative to the U.S. dollar.
            - **GLD**:  The price of SPDR Gold Shares (GLD), which is the target variable representing gold prices.
        """
    },
    {
        "name": "House Price Estimator",
        "description": "Predict the price of a house based on various features.",
        "details": """
        Using historical and current market data, this tool predicts the house price based on features like location, size, and amenities.
        """
    },
    {
        "name": "Loan Eligibility",
        "description": "Check your eligibility for various types of loans based on your financial profile.",
        "details": """
        This calculator assesses loan eligibility by analyzing credit scores, income, and other relevant financial details.
        """
    },
    {
        "name": "Parkinson's Disease",
        "description": "Assess your risk of Parkinson's Disease with advanced ML algorithms.",
        "details": """
            ### Introduction
            Parkinson's disease (PD) is a progressive neurodegenerative disorder that primarily affects movement. It often starts with subtle symptoms such as tremors, stiffness, and slow movement.

            ### Oxford Parkinson's Disease Detection Dataset (UCI ML Repository)
            The dataset contains biomedical voice measurements from 31 people, 23 of whom have Parkinson's disease (PD). The main goal is to differentiate between healthy individuals and those with PD using the "status" column, where 0 indicates healthy and 1 indicates PD.

            ### Additional Variable Information
            - **MDVP_Fo(Hz)**:  Average vocal fundamental frequency.
            - **MDVP_Fhi(Hz)**:  Maximum vocal fundamental frequency.
            - **MDVP_Flo(Hz)**:  Minimum vocal fundamental frequency.
            - **MDVP_Jitter(%)**, **MDVP_Jitter(Abs)**, **MDVP_RAP**, **MDVP_PPQ**, **Jitter_DDP**:  Measures of variation in fundamental frequency.
            - **MDVP_Shimmer**, **MDVP_Shimmer(dB)**, **Shimmer_APQ3**, **Shimmer_APQ5**, **MDVP_APQ**, **Shimmer_DDA**:  Measures of variation in amplitude.
            - **NHR**, **HNR**:  Noise-to-tonal ratio measures in the voice.
            - **status**:  Health status of the subject (1 - Parkinson's, 0 - healthy).
            - **RPDE**, **D2**:  Nonlinear dynamical complexity measures.
            - **DFA**:  Signal fractal scaling exponent.
            - **spread1**, **spread2**, **PPE**:  Nonlinear measures of fundamental frequency variation.
        """
    },
    {
    "name": "Sleep Disorder Prediction",
    "description": "Assess your risk of developing a sleep disorder using advanced ML algorithms.",
    "details": """
        ### Introduction
        Sleep disorders can have a significant impact on an individual's overall health and well-being. These disorders often result from a combination of poor sleep habits, lifestyle factors, stress, and underlying medical conditions.

        ### Sleep Health and Lifestyle Dataset
        The dataset consists of sleep, lifestyle, and health metrics collected from 400 individuals. The main goal is to predict the likelihood of an individual having a sleep disorder using the "Sleep Disorder" column, which contains categorical values indicating the presence or absence of a sleep disorder.

        """
},
    {
        "name": "PDF Malware Detector",
        "description": "Identify and alert users about potential malware in PDF files.",
        "details": """
            ### Overview  
            The PDF Malware Detector scans uploaded PDF files for malicious content, ensuring user safety and data protection.

            ### Key Features  
            - **File Upload**: Simple drag-and-drop interface for easy file submission.  
            - **Malware Detection**: Comprehensive analysis to detect harmful elements within PDFs.  
            - **File Size Limit**: Supports files up to 200MB.

            ### Use Cases  
            Perfect for users needing to verify the integrity of PDF documents before opening or sharing.
        """
    },
    {
        "name": "Stress Level Detector",
        "description": "Analyze your mental stress levels based on social media interactions.",
        "details": """
        The model uses text analysis on social media data to identify signs of stress, helping users understand their mental health patterns.
        """
    },
    {
        "name": "Text Summarizer",
        "description": "Save time with concise, professional summaries of lengthy texts.",
        "details": """
        Generate quick and comprehensive summaries of lengthy documents, ideal for students, researchers, and professionals.
        """
    },
    {
        "name": "Real-Time Language Translator",
        "description": "Translate spoken language into other languages instantly for seamless communication.",
        "details": """
            ### Overview  
            The Real-Time Language Translator uses advanced speech recognition and NLP to provide immediate translations between languages, enhancing communication in diverse settings.

            ### Key Features  
            - **Instant Translation**: Real-time spoken language translation.
            - **Multiple Languages**: Supports a variety of source and target languages.
            - **User-Friendly Interface**: Easy to navigate for all users.

            ### Use Cases  
            Ideal for travel, business meetings, and language learning, breaking down language barriers effortlessly.
        """
    },
    {
        "name": "Business Performance Forecaster",
        "description": "Forecast business profits based on various investment areas for better financial planning and budget allocation.",
        "details": """
            ### Overview  
            The Business Performance Forecaster predicts company profit based on investment in R&D, administration, and marketing, using machine learning to analyze investment patterns and optimize budget allocation.

            ### Key Features  
            - **Profit Prediction**: Provides an estimated profit based on investment data.
            - **Investment Analysis**: Evaluates how different spending areas impact overall profit.
            - **Multi-Input Support**: Accounts for multiple variables like R&D, administration, and marketing expenses.

            ### Use Cases  
            Useful for companies looking to plan budgets, assess the impact of investments, and improve decision-making processes in financial forecasting.
        """
    }
]

# Define shades of blue for calculators
blue_shades = [
        "#D1E8E2",  # Light Blue
        "#A0D6E0",  # Soft Blue
        "#7FB3E8",  # Sky Blue
]

# Display calculators in a table layout with two columns per row
for i in range(0, len(calculators), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(calculators):
                calc = calculators[i + j]
                # Use modulo to cycle through the blue shades
                color_index = (i + j) % len(blue_shades)
                color = blue_shades[color_index]
                with col:
                    # Styled container for heading and description with different blue shades
                    st.markdown(
                        f"""
                        <div style='
                            background-color: {color};
                            border-radius: 10px;
                            padding: 15px;
                            margin-bottom: 10px;
                        '>
                            <h3 style='margin: 0; color: black;'>{calc['name']}</h3>
                            <p style='margin: 5px 0; color: black;'>{calc['description']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    # More Info expander
                    with st.expander("More Info"):
                        st.write(calc["details"])
                    st.markdown("---")

calculator_inputs = {
    "Income Estimator": ["Age", "Education Level", "Occupation", "Work Experience (years)", "Region"],
    "Gold Price Predictor": ["S&P 500 Index (SPX)", "Crude Oil Price (USO)", "Silver Price (SLV)", "EUR/USD Exchange Rate"],
    "House Price Estimator": ["Location", "Size (sq ft)", "Number of Bedrooms", "Number of Bathrooms", "Property Type"],
    "Loan Eligibility": ["Credit Score", "Annual Income", "Loan Amount", "Loan Term (years)", "Employment Status"],
    "Parkinson's Disease Risk": ["MDVP_Fo(Hz)", "MDVP_Jitter(%)", "MDVP_Shimmer(dB)", "NHR", "HNR", "DFA"],
    "Sleep Disorder Prediction": ["Average Sleep Hours", "Exercise Frequency (per week)", "Stress Level", "Diet Quality", "Caffeine Intake (cups per day)"],
    "PDF Malware Detector": ["File Name", "File Size (MB)", "File Type"],
    "Stress Level Detector": ["Number of Daily Social Media Posts", "Sentiment of Posts", "Average Post Length (words)"],
    "Text Summarizer": ["Text Length (words)", "Document Type", "Desired Summary Length (%)"],
    "Real-Time Language Translator": ["Source Language", "Target Language", "Speech Speed (words per minute)"],
    "Business Performance Forecaster": ["R&D Spend", "Administration Cost", "Marketing Spend", "Region", "Number of Employees"]
}

#Selecting a model to compare
st.subheader("Comparison Mode")
selected_model = st.selectbox("Select a calculator to compare", list(calculator_inputs.keys()))

if selected_model:
    num_inputs = st.slider(f"Select number of input sets for {selected_model} comparison", min_value=2, max_value=5, value=2)

    st.markdown(f"### {selected_model} - Comparison Mode")
    inputs = []
    input_prompts = calculator_inputs[selected_model]

    for i in range(num_inputs):
        st.markdown(f"### Input Set {i + 1}")
        input_data = {}
        for prompt in input_prompts:
            input_data[prompt] = st.text_input(f"{prompt} (Input {i + 1})", key=f"{prompt}_{i}")
        inputs.append(input_data)

    # Display results side-by-side
    if st.button("Compare Results"):
        st.markdown("### Comparison Results")
        cols = st.columns(num_inputs)
        for i, col in enumerate(cols):
            with col:
                st.write(f"Input Set {i + 1}:")
                for k, v in inputs[i].items():
                    st.write(f"{k}: {v}")
                st.write("Result: (Prediction placeholder)")

st.markdown("## Get Started Today!")
st.markdown("Explore our calculators and take control of your predictive analytics journey!")

st.write("Developed with ❤️ by Yashasvini Sharma | [Github](https://www.github.com/yashasvini121) | [LinkedIn](https://www.linkedin.com/in/yashasvini121/)")
