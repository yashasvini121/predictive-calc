import streamlit as st

st.set_page_config(page_title="Predictive Calc - Machine Learning Models", page_icon="🤖")

st.title("Welcome to Predictive Calc!")

st.markdown("""
## Explore Cutting-Edge Machine Learning Models
**Predictive Calc** offers a powerful suite of machine learning models designed to assist you in making informed decisions. Whether it's predicting house prices, determining loan eligibility, or evaluating health risks, we have you covered.
""")

st.markdown("""
## Why Choose Predictive Calc? 
""")

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

# Calculator information in a structured format, including the new Churn Prediction Calculator
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
    # Existing calculators...

    # New entry for the Churn Prediction Calculator
    {
        "name": "Churn Prediction",
        "description": "Assess the likelihood of customer churn based on their profile and service usage patterns.",
        "details": """
            ### Introduction
            Customer churn prediction is essential for subscription-based businesses, as it enables proactive measures to retain customers. This calculator uses demographic, account, and service data to assess a customer's likelihood of discontinuing service.

            ### Dataset Information
            The dataset includes various factors such as:
            - **Demographics**: Age, gender, partner status, and dependents.
            - **Account Details**: Tenure, contract type, paperless billing, and payment method.
            - **Service Usage**: Phone and internet service usage, streaming services, and tech support.

            ### Key Features
            - **Proactive Retention**: Identify high-risk customers for targeted retention strategies.
            - **Insightful Analytics**: Understand patterns and factors contributing to customer churn.
            - **Adaptability**: Designed for telecom and other subscription-based businesses.
        """
    },

    # Other calculators...
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

st.markdown("## Get Started Today!")
st.markdown("Explore our calculators and take control of your predictive analytics journey!")

st.write("Developed with ❤️ by Yashasvini Sharma | [Github](https://www.github.com/yashasvini121) | [LinkedIn](https://www.linkedin.com/in/yashasvini121/)")
