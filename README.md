# Stock Price Predictor
This is a web-based application to predict stock prices using a custom linear regression model. The app fetches stock data from Yahoo Fiance and uses Streamlit for a user-friendly interface.

## Features
- **Interactive Input**: Users can spercify stock symbols, start dates, and endd dates for predictions.
- **Data Fetching**: Retrieves stock data from Yahoo Finance.
- **Moving Average Calculation**: Calculates the 50-dau moving average for predictive modeling.
- **Linear Regression**: Includes are custom implementation of linear regression.
- **Future Predictions**: Predicts stock prices for up to 7 days into the future of the requested data.
- **Visualization**: Displays actual vs. predicted prices through graphs and tables.

## Tech Stack
- **Python**: Core programming language.
- **Steamlit**: For building an interactive interface.
- **Yahoo Finanace API**: For fetching stock market data.
- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation and analysis.

## Setup and Installation
1. **Clone the Repository**:
  - git clone https://github.com/jkramer321/stock-price-predictor.git
2. **Install Dependencies**: Install required libraries
  - pip install -r requirements.txt
3. **Run the Application**:
  - streamlit run StockPredictor.py
4.  **Access the App**: Open the URL provided in the terminal (usually http://localhost:8501).

## How It Works
1. **User Input**:
  - Enter the stock symbol.
  - Specify the start and end dates for histoical data.
2. **Data Processing**:
  - Fetches stock data from Yahoo Finance.
  - Calculates the 50-day mocing average and splits data into training and testing sets.
3. **Model Training**:
  - Trains a linear regfression model using the moving average to predict closing prices.
4. **Prediction and Visualization**:
  - Compares actual vs. predicted prices.
  - Forecasts and displays future stock prices.

## License
-   This project is licensed under the MIT License.
