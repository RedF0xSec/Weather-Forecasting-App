# Weather Forecasting Web Application

## Overview
This project focuses on the **containerization** of a weather forecasting web application, which uses machine learning to predict weather conditions based on historical data. While the machine learning model (trained using an imbalanced dataset from Seattle) plays a role in the application, the core emphasis is on the deployment and scalability of the system through Docker and Kubernetes.

The application was containerized using **Docker** to ensure portability across different environments and deployed in a **Kubernetes** cluster to ensure scalability and high availability. By utilizing **Horizontal Pod Autoscaler (HPA)**, the system can dynamically adjust its resource allocation based on CPU utilization, ensuring efficient performance even during peak loads.

## Key Features
- **Containerization**: The entire application is packaged into Docker containers, ensuring consistency and simplicity in deployment across various environments.
- **Kubernetes Deployment**: The application is deployed within a Kubernetes cluster to provide scalability and fault tolerance, making it capable of handling high traffic volumes.
- **Horizontal Pod Autoscaler (HPA)**: HPA is configured to scale the application dynamically by adjusting the number of replicas based on CPU utilization, optimizing resource usage.
- **Performance and Stress Testing**: The system underwent stress testing using **JMeter**, proving its capacity to handle up to 50,000 daily requests with peaks of 2,000 concurrent users while maintaining an average response time of less than 3 seconds and a 0% error rate.
- **Security**: Container security assessments were conducted using **Docker Scout**, identifying and mitigating potential vulnerabilities (such as CVE-2024-5206, CVE-2024-6345, CVE-2023-5752). The application also uses an **NGINX Ingress Controller** for enhanced security, including rate limiting and traffic shaping to defend against DoS attacks.

## System Architecture
- **Docker Containers**: The application is packaged into Docker containers, making it easy to deploy and manage in various environments, from local development to production in a Kubernetes cluster.
- **Kubernetes Cluster**: Ensures that the application can scale automatically based on the load, providing high availability and redundancy.
- **Weather Forecasting Model**: While the machine learning model predicts weather conditions based on historical data (using techniques like feature engineering and XGBoost), the primary focus is on its scalable and secure deployment.

## Security & Performance
- **Vulnerability Scanning**: Security assessments using Docker Scout ensure the integrity of the system by identifying and mitigating container vulnerabilities.
- **NGINX Ingress**: An NGINX Ingress Controller is used to implement additional security layers like rate limiting and traffic shaping to protect against denial-of-service (DoS) attacks.

## Future Enhancements
- **Expanded Dataset**: Integrate weather data from additional regions to improve prediction accuracy.
- **Improved Model Optimization**: Enhance the machine learning model to handle a wider range of weather events.
- **Advanced Security Features**: Introduce encryption for data transmission and further enhance authentication mechanisms.

For more details, check out the full documentation in the repository.
