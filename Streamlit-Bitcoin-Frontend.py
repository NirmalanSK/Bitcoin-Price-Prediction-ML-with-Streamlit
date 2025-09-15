import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load trained model and scaler
with open('random_forest_model.pkl', 'rb') as f:
    model_rf = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def predict_btc_price(input_data):
    """Scale input and predict using the model"""
    input_scaled = scaler.transform(input_data)
    predictions = model_rf.predict(input_scaled)
    return predictions

def main():
    st.title("Predict BTC Close Price")
    st.write("Choose an option: enter values manually or upload a CSV file.")

    # Option to choose manual input or CSV upload
    option = st.radio("Select input method:", ("Manual Input", "Upload CSV"))

    if option == "Manual Input":
        st.sidebar.header("Input Features")
        usdt_close = st.sidebar.number_input("USDT Close Price", min_value=0.0, format="%.2f")
        usdt_volume = st.sidebar.number_input("USDT Volume", min_value=0.0, format="%.2f")
        bnb_close = st.sidebar.number_input("BNB Close Price", min_value=0.0, format="%.2f")
        bnb_volume = st.sidebar.number_input("BNB Volume", min_value=0.0, format="%.2f")

        # Create input dataframe
        input_df = pd.DataFrame({
            'USDT_Close': [usdt_close],
            'USDT_Volume': [usdt_volume],
            'BNB_Close': [bnb_close],
            'BNB_Volume': [bnb_volume]
        })

        if st.button("Predict BTC Close Price"):
            prediction = predict_btc_price(input_df)[0]
            st.success(f"Predicted BTC Close Price: {prediction:.2f}")

    elif option == "Upload CSV":
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            input_df = pd.read_csv(uploaded_file)
            required_cols = ['USDT_Close', 'USDT_Volume', 'BNB_Close', 'BNB_Volume']
            if not all(col in input_df.columns for col in required_cols):
                st.error(f"CSV must contain columns: {required_cols}")
            else:
                st.write("Input Data:")
                st.dataframe(input_df)

                if st.button("Predict BTC Close Price"):
                    predictions = predict_btc_price(input_df)
                    input_df['Predicted_BTC_Close'] = predictions
                    st.success("Predictions Completed!")
                    st.dataframe(input_df)

                    # Allow downloading predictions
                    csv = input_df.to_csv(index=False)
                    st.download_button(
                        label="Download Predictions as CSV",
                        data=csv,
                        file_name='btc_predictions.csv',
                        mime='text/csv'
                    )

if __name__ == "__main__":
    main()
