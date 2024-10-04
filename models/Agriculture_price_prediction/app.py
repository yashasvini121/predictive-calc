import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go
from datetime import timedelta

# Set the page configuration
st.set_page_config(page_title="Agricultural Price Forecasting", layout="wide")

# Custom CSS for enhanced UI with background image and semi-transparent overlay
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

        .main {
            background-image: url("https://wallpapercave.com/wp/wp9212753.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
            position: relative;
            font-family: 'Roboto', sans-serif;
        }
        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.7); /* Slightly more transparent overlay */
            z-index: 1;
        }
        .sidebar .sidebar-content {
            background-color: rgba(255, 255, 255, 0.9); /* Solid background for sidebar */
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #ddd;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton button {
            background-color: #007BFF;
            color: white;
            border-radius: 8px;
            padding: 12px;
            font-weight: 500;
            border: none;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        h1 {
            color: #003366;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 2; /* Ensure text is above overlay */
        }
        h3 {
            color: #333333;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
            position: relative;
            z-index: 2; /* Ensure text is above overlay */
        }
        footer {
            color: #555555;
            text-align: center;
            padding: 15px 0;
            font-size: 14px;
            border-top: 1px solid #ddd;
            position: relative;
            z-index: 2; /* Ensure text is above overlay */
        }
        .stats-box {
            background-color: rgba(255, 255, 255, 0.9); /* Solid background for statistics */
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #ddd;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Add an overlay div
st.markdown('<div class="overlay"></div>', unsafe_allow_html=True)

# Title with gradient and shadow
st.markdown("<h1 style='text-align: center;'>Agricultural Price Forecasting</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center;'>Predict and Visualize Commodity Prices Based on Rainfall and Temperature</h3>",
    unsafe_allow_html=True)

# Sidebar for user inputs with better organization
st.sidebar.markdown("<h2 style='color: #0056b3;'>User Inputs</h2>", unsafe_allow_html=True)

with st.sidebar.expander("Select Parameters", expanded=True):
    state = st.selectbox("Select State", ["Mumbai"],
                         help="Choose the state for which you want to forecast prices.")
    commodity = st.selectbox("Select Commodity", ["Tur", "Moong", "Urad", "Masur"],
                             help="Choose the commodity to analyze.")
    days_to_predict = st.slider("Select number of days to predict", min_value=1, max_value=60, value=30,
                                help="Select the number of days for price forecasting.")
    rainfall = st.slider("Enter Rainfall (in inches)", min_value=0, max_value=600, value=25,
                         help="Enter the rainfall amount in inches.")
    temperature = st.slider("Enter Temperature (in °C)", min_value=-5, max_value=50, value=20,
                            help="Enter the temperature in degrees Celsius.")

# File paths
file_path_delhi = 'Data\\agrodelhhi.xlsx'  # Replace with the path to your Excel file for Delhi
file_path_mumbai_tur = 'Data\\MumbaiTurExcl.xlsx'  # Replace with the path to your Excel file for Mumbai Tur
file_path_mumbai_masur = 'Data\\Mumbai_masur.xlsx'  # Replace with the path to your Excel file for Mumbai Masur
file_path_mumbai_moong = 'Data\\Mumbai_moong.xlsx'  # Replace with the path to your Excel file for Mumbai Moong
file_path_mumbai_urad = 'Data\\Mumbai_urad_.xlsx'  # Replace with the path to your Excel file for Mumbai Urad


# Load data
@st.cache_data
def load_data(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')  # Use openpyxl for .xlsx files
        df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y')  # Adjust format if needed
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please check the file path.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


# Prediction logic
def predict_prices(df, commodity, days_to_predict, rainfall, temperature):
    # Prepare the Data for Prophet
    df_prophet = df[['date', 'modal_price']].rename(columns={'date': 'ds', 'modal_price': 'y'})
    # Initialize and train the Prophet model
    model = Prophet()
    model.fit(df_prophet)
    # Create a future dataframe for predictions
    future = model.make_future_dataframe(periods=days_to_predict)
    # Make predictions
    forecast = model.predict(future)

    # Rename columns for clarity
    forecast = forecast.rename(columns={'ds': 'date', 'yhat': 'Price Prediction'})

    # Define optimal ranges for rainfall and temperature for each commodity
    optimal_ranges = {
        "Apple": {"rainfall": (30, 35), "temperature": (15, 25)},
        "Tur": {"rainfall": (25, 35), "temperature": (20, 30)},
        "Moong": {"rainfall": (20, 30), "temperature": (25, 35)},
        "Urad": {"rainfall": (20, 30), "temperature": (25, 35)},
        "Masur": {"rainfall": (20, 30), "temperature": (20, 30)},
    }

    # Apply rainfall and temperature-based price adjustment only to forecasted data
    if commodity in optimal_ranges:
        # Get the optimal ranges
        optimal_rainfall = optimal_ranges[commodity]["rainfall"]
        optimal_temperature = optimal_ranges[commodity]["temperature"]

        # Forecast adjustments
        future_dates = forecast['date']

        # Rainfall adjustments
        if rainfall < optimal_rainfall[0]:  # Below Essential Range
            adjustment_factor = 1 + (optimal_rainfall[0] - rainfall) * 0.01
            adjustment_factor = min(adjustment_factor, 1.3)  # Cap at 30% increase
        elif rainfall > optimal_rainfall[1]:  # Above Essential Range
            adjustment_factor = 1 + (rainfall - optimal_rainfall[1]) * 0.01
            adjustment_factor = min(adjustment_factor, 1.3)  # Cap at 30% increase
        else:  # Within Essential Range
            adjustment_factor = 0.95  # Decrease price slightly by 5%

        # Temperature adjustments
        if optimal_temperature[0] <= temperature <= optimal_temperature[1]:  # Optimal temperature range
            temperature_adjustment = 0.95  # Decrease price slightly by 5%
        else:
            # Outside optimal range, increase prices slightly (simulate reduced production)
            if temperature < optimal_temperature[0]:
                temperature_adjustment = 1 + (optimal_temperature[0] - temperature) * 0.02  # Mild increase
            elif temperature > optimal_temperature[1]:
                temperature_adjustment = 1 + (temperature - optimal_temperature[1]) * 0.02  # Mild increase
            temperature_adjustment = min(temperature_adjustment, 1.3)  # Cap at 30% increase

        # Apply both adjustments to the forecast
        forecast.loc[
            forecast['date'] > df['date'].max(), 'Price Prediction'] *= adjustment_factor * temperature_adjustment

    return forecast


# Show the data visualization and predictions only after the user clicks "Submit"
if st.sidebar.button("Submit"):
    # Determine the file path based on user inputs
    if state == "Delhi" and commodity == "Apple":
        df = load_data(file_path_delhi)
    elif state == "Mumbai":
        if commodity == "Tur":
            df = load_data(file_path_mumbai_tur)
        elif commodity == "Masur":
            df = load_data(file_path_mumbai_masur)
        elif commodity == "Moong":
            df = load_data(file_path_mumbai_moong)
        elif commodity == "Urad":
            df = load_data(file_path_mumbai_urad)
    else:
        df = None

    if df is not None:
        # Apply prediction logic
        forecast = predict_prices(df, commodity, days_to_predict, rainfall, temperature)

        # Plot results using Plotly
        fig = go.Figure()

        # Historical data
        fig.add_trace(go.Scatter(x=df['date'], y=df['modal_price'], mode='markers', name='Historical Price',
                                 marker=dict(color='blue', size=8)))

        # Forecasted price
        fig.add_trace(
            go.Scatter(x=forecast['date'], y=forecast['Price Prediction'], mode='lines', name='Forecasted Price',
                       line=dict(color='red')))

        # Add trendlines and seasonality (if applicable)
        fig.update_layout(title=f'{commodity} Price Forecast',
                          xaxis_title='Date',
                          yaxis_title='Price',
                          template='plotly_white')

        # Remove numbering from date and format date
        fig.update_xaxes(tickformat='%Y-%m-%d')

        # Show plot
        st.plotly_chart(fig, use_container_width=True)

        # Show future predictions
        st.write(f"Predicted prices for the next {days_to_predict} days:")
        st.write(forecast[['date', 'Price Prediction']].tail(days_to_predict))

        # Export the forecast to a CSV file and provide a download link
        csv = forecast[['date', 'Price Prediction']].to_csv(index=False)
        st.download_button(
            label="Download Forecast Data as CSV",
            data=csv,
            file_name=f"{commodity}_forecast.csv",
            mime="text/csv",
        )

        # Add feedback form
        # st.write("**Feedback:**")
        # feedback = st.text_area("Please provide your feedback or suggestions:")
        # if st.button("Submit Feedback"):
        #     st.write("Thank you for your feedback!")

# Footer
st.markdown("<footer>© 2024 Developed by Stunning_Hunters.Agricultural Price Forecasting. All rights reserved.</footer>", unsafe_allow_html=True)
