# Weather Forecasting App - Group04

This project predicts the weather conditions (rain, snow, sun, fog, or drizzle) using a machine learning model.
**Authors**: Giuseppe Biscardi (0622702315), Elena Falcone (0622702314)

---

## Folder Structure

### Main
- **`app_pipeline.py`**: Main script for the weather forecasting pipeline.
- **`Dockerfile`**: Configuration file for Docker.
- **`data/`**: Contains datasets for weather analysis.
- **`models/`**: Pretrained models for predictions.
- **`notebooks/`**: Jupyter notebooks for analysis and experiments.
- **`k8sweatherdeployment.yaml`**: Kubernetes configuration for deployment without ingress.
- **`k8sweatherdeploymentwithingress.yaml`**: Kubernetes configuration for deployment with ingress.
- **`Report.pdf`**: Descriptive report of the project.
- **`requirements.txt`**: List of required Python dependencies.
- **`TRACCIA.pdf`**: Document with the project task.

### `data/`
- **`seattle-weather-cleaned.csv`**: Cleaned dataset for weather analysis.
- **`seattle-weather.csv`**: Original dataset with raw weather data.

### `imgs/`
- **`weatherpanel.png`**: Representative image of the app's panel.

### `kubernetes-configuration/`
- **`cluster_rolebinding.yaml`**: Configuration for cluster role binding.
- **`dashboard-adminuser.yaml`**: Configuration for admin user in the Kubernetes dashboard.
- **`metrics-server.yaml`**: Configuration for the metrics server to monitor the cluster.
- **`weather-app-config-with-port-mapping.yaml`**: Kubernetes configuration with port mapping.

### `models/`
- **`model.joblib`**: Trained model for weather forecasting.
- **`scaler.joblib`**: Scaler for data normalization.
- **`transformer.joblib`**: Transformer for data preprocessing.

### `NGINX/`
- **`APDosLogConf.yaml`**: NGINX configuration for logging DoS attacks.
- **`APDosPolicy.yaml`**: NGINX policy to mitigate DoS attacks.
- **`DosProtectedResource.yaml`**: Configuration to protect NGINX resources from DoS.

### `notebooks/`
- **`Weather_Forecasting_Choosing_the_Model.ipynb`**: Notebook for selecting the best model.
- **`Weather_Forecasting_Offline_Data_Analisys_and_Prepocessing.ipynb`**: Notebook for offline data analysis and preprocessing.
- **`Weather_Forecasting_Pipeline.ipynb`**: Notebook with the implementation of the forecasting pipeline.