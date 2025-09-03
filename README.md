# Weather Forecasting ML Project

👩‍💻 **Author: Lauren Malka**  
3rd-year Data Science student at the College of Management, Israel.  
Passionate about Machine Learning, Data Analysis, and building AI-driven solutions.  
Currently focused on applied ML projects in time series forecasting, anomaly detection, and model explainability.  

---

# Weather Forecasting ML Project

This project develops a machine learning pipeline to forecast daily temperature using weather data collected from the **Ashalim station (Israel)**, covering the period **2022 – April 2025**.

## Project Structure
- `weather_forecast_ml.ipynb` – Main notebook with full pipeline (EDA, anomaly detection, time series forecasting, fairness/bias analysis, model evaluation).  
- `requirements.txt` – Python dependencies for reproducing the results.  
- `*.csv` – Processed datasets and model evaluation outputs.  
- `scraper_telaviv_2024_2025.py` – Data collection script.  

## Key Steps
1. **Exploratory Data Analysis (EDA)** – Temperature, humidity, pressure, and wind speed distributions.  
2. **Anomaly Detection** – Identification of unusual values in the time series.  
3. **Time Series Forecasting** – ARIMA with Fourier terms for seasonality, plus ML models (Linear Regression, Decision Tree, RandomForest).  
4. **Model Explainability and Fairness** – Comparison of errors across months and seasons.  
5. **Model Evaluation** – RMSE, MAE, sMAPE, and statistical comparisons.  

## Results
- The tuned **RandomForest** achieved the best performance, capturing seasonal trends and short-term fluctuations with average errors of ~2–3 °C.  
- Compared to baselines, RandomForest reduced MAE by ~14% over Linear Regression.

📬 For collaborations or project inquiries, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/laurenmalka) or GitHub.
