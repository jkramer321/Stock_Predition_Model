import yfinance as yf
import streamlit as st
import pandas as pd
from linear_regression import Linear_Regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from datetime import timedelta


#defining a stock symbol from the user
stock_symbol = st.text_input("Enter a stock symbol", "AAPL");


#set the title of the web app
st.title('Stock Price Predictor')


#getting start date from the user
start_date = st.date_input("Start date", pd.to_datetime('2020-01-01'));

#getting end date from the user
end_date = st.date_input("End date", pd.to_datetime('2021-01-01'));

# Get the data for the stock AAPL
stock_data = yf.download(stock_symbol, start=start_date, end=end_date);


#checking if the data is not empty
if not stock_data.empty:

    #calculating the moving average
    stock_data['50_MA'] = stock_data['Close'].rolling(50).mean();

    # Dropping rows with NaN values (due to moving average calculation)
    stock_data = stock_data.dropna()

    # Train-test split
    X = stock_data[['50_MA']]
    y = stock_data['Close']

    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    #create a linear regression model
    model = Linear_Regression()
    #fit the model
    model.fit(X_train, y_train)

    #make predictions
    predictions = model.predict(X_test)

    # Compare predictions with actual values
    results = pd.DataFrame({'Actual': y_test, 'Predicted': predictions},index=X_test.index)
    st.write("Actual vs Predicted:")
    st.write(results.head())

    # Calculate the Mean Squared Error
    mse = mean_squared_error(y_test, predictions)
    st.write('Mean Squared Error:', mse)

    # Plotting the actual vs predicted values
    st.line_chart(results)

    # Predict the final value for the end_date
    final_value_input = stock_data[['50_MA']].iloc[-1].values.reshape(-1, 1)  # Get the last available moving average
    final_prediction = model.predict(final_value_input)[0]  # Predict the final close value

    # Display the predicted value at the end date
    st.write(f"Predicted closing price for {end_date}: {final_prediction:.2f}")

    # Forecasting future values
    st.write("Future Predictions:")
    num_future_days = 7  # Number of days to predict into the future
    future_dates = [end_date + timedelta(days=i) for i in range(1, num_future_days + 1)]
    future_ma = [final_value_input[0][0] for _ in range(num_future_days)]  # Assumes constant moving average
    future_predictions = model.predict(np.array(future_ma).reshape(-1, 1))

    # Create a dataframe for the future dates and predictions
    future_data = pd.DataFrame({'Date': future_dates, 'Predicted Close': future_predictions})
    st.write(future_data);

    # Plotting the future predictions
    st.line_chart(future_data.set_index('Date'))

    
    # Otherwise, display an error message
else:
    # Display an error message if the data is empty
    st.write("No data found for the given stock symbol and date range")


