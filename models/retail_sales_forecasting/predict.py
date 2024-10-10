from models.retail_sales_forecasting.model import predict

def get_prediction(store_number, department_number, date, is_holiday):
    """
    Prepares the input data and calls the predict function from model.py.
    """
    # Prepare the input data as a dictionary
    input_data = {
        "store_number": store_number,
        "department_number": department_number,
        "date": date,  # Date is in 'YYYY-MM-DD' format
        "is_holiday": is_holiday
    }

    # Call the predict function
    result = predict(input_data)
    return result

