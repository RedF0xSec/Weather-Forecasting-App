import streamlit as st
import joblib
import pandas as pd
from PIL import Image
from datetime import datetime

# Load the model and transformer
@st.cache_resource
def load_model_and_transformer(transformer_path, model_path):
    transformer = joblib.load(transformer_path)
    model = joblib.load(model_path)
    return transformer, model

# Make predictions
def inference(weather_data, transformer, model):

    # Get the feature names expected by the transformer
    if hasattr(transformer, 'get_feature_names_out'):
        expected_features = transformer.get_feature_names_out()
    else:
        expected_features = transformer.feature_names_in_

    # Ensure input data aligns with the expected features
    aligned_data = {col: weather_data.get(col, 0) for col in expected_features}

    # Ensure proper types for numeric columns
    numeric_columns = ['precipitation', 'temp_max', 'temp_min', 'wind']
    for col in numeric_columns:
        if col in aligned_data:
            aligned_data[col] = float(aligned_data[col])

    # Ensure 'year', 'month', 'day' are integers
    date_columns = ['year', 'month', 'day']
    for col in date_columns:
        if col in aligned_data:
            aligned_data[col] = int(aligned_data[col])

    # Create a DataFrame with the aligned data, excluding 'date'
    try:
        df = pd.DataFrame([aligned_data], columns=expected_features)
    except KeyError as e:
        st.write("KeyError in aligning columns:", e)
        st.write("Aligned data:", aligned_data)
        st.write("Expected features:", expected_features)
        raise

    # Apply transformation
    try:
        transformed_data = transformer.transform(df)

        # Ensure transformed data is a DataFrame with proper columns
        transformed_df = pd.DataFrame(transformed_data, columns=expected_features[:transformed_data.shape[1]])
    except Exception as e:
        st.write("Error during transformation:", e)
        st.write("Transformer details:", transformer)
        raise

    # Predict using the transformed data
    try:
        prediction = model.predict(transformed_df)[0]
    except Exception as e:
        st.write("Error during prediction:", e)
        st.write("Model details:", model)
        raise

    class_mapping = {
        0: "Drizzle",
        1: "Fog",
        2: "Rain",
        3: "Snow",
        4: "Sun"
    }

    result = f"The weather prediction is: {class_mapping[prediction]}"

    # Save result to a log file
    with open('logs/weather_prediction.log', 'a') as f:
        f.write(result + '\n')

    return result

# HomePage
st.title('Weather Forecasting App')
st.write('The data for the following example is originally from Kaggle to analyze and build predictive models of weather conditions based on accompanying conditions. This tool cannot be a substitute for official weather forecasts.')
image = Image.open('imgs/weatherpanel.png')
st.image(image, use_container_width=True)
st.write('Please fill in the details about the current weather indices in the left sidebar and click the button below!')

# Ottieni la data corrente
current_date = datetime.now()
current_day = current_date.day
current_month = current_date.month
current_year = current_date.year

# Input features
temperature_max = st.sidebar.slider("Maximum Temperature (°C)", -50, 50, 20)
temperature_min = st.sidebar.slider("Minimum Temperature (°C)", -50, 50, 10)
precipitation = st.sidebar.slider("Precipitation (mm)", 0, 10, 0)
wind_speed = st.sidebar.slider("Wind Speed (m/s)", 0, 50, 5)
day = st.sidebar.number_input("Day of the Month", 1, 31, current_day)
month = st.sidebar.number_input("Month", 1, 12, current_month)
year = int(st.sidebar.number_input("Year", 2000, 2100, current_year))

# Prepare the weather data
weather_data = {
    'precipitation': precipitation,
    'temp_max': temperature_max,
    'temp_min': temperature_min,
    'wind': wind_speed,
    'day': day,
    'month': month,
    'year': year
}

# Main
if st.button('Predict Weather'):
    # Load transformer and model
    transformer, model = load_model_and_transformer('models/transformer.joblib', 'models/model.joblib')

    # Perform inference
    result = inference(weather_data, transformer, model)
    st.write(result)
