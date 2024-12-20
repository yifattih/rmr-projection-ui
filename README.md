# Resting Metabolic Rate Projection Web App

## Overview
The RMR Projection Web App helps users calculate their Resting Metabolic Rate (RMR) and project changes over time based on weight loss goals. This application uses the Mifflin-St Jeor equations for precise calculations and provides a user-friendly interface for data input and visualization.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Features](#features)
3. [Contribution Guide](#contribution-guide)
4. [Code of Conduct](#code-of-conduct)
5. [Technical Overview](#technical-overview)
6. [Future Work](#future-work)
7. [License](#license)

---

## Getting Started
How to Use the Application
1. **Access the Web App**
  - Visit [RMR Projection Web App](https://rmr-projection.example.com)
2. **Input Your Details**
  - Age
  - Weight
  - Height
  - Desired weight loss rate
  - Projection duration (in weeks)
3. **Submit**
  - Calculations and vizualization are performed in real time
4. **View Results**
  - Current RMR values by activity level
  - Projected changes in RMR over the chosen duration and by activity levels

---

## Features
- **Interactive RMR Calculator**: Input parameters like age, weight, height, and weight loss rate
- **Projections Over Time**: Visualize RMR changes with a time
- **Responsive UI**: Modern and intuitive interface for seamless usage across devices
- **Microservices Architecture**: Backend and frontend services operate independently, ensuring scalability and maintainability
- **Deployed on Google Cloud Platform**: Ensures reliability and performance

---

## Contribution Guide
### How to Contribute
Contributions to enhance features, fix bugs, and improve documentation are always welcome
For seamless and effective cnontribution please follow the [Contribution Guidelines](CONTRIBUTING.md)

### Code of Conduct
- Be respectful and constructive in communication
- Adhere to the [Code of Conduct](CODE_OF_CONDUCT.md)

---

## Technical Overview
The app leverages a streamlined DevOps pipeline to ensure seamless development, testing, and deployment processes Here’s an overview of the stack and CI/CD practices in place:

### Architecture
The application follows a **microservices architecture**
1. **Backend Microservie**
  - RESTful API for RMR calculations
  - Modular Python code with clear validation and error handling
2. **Frontend Microservie**
  - Single-page application
  - Interactive user interface for input and result visualization

### Tech Stack
- **Version Control**
  - **System**: GitHub
  - GitHub repository for each microservice and deplyment management
    - [Backend](https://github.com/yifattih/rmr-projection-api-model)
      - RESTful API 
      - Built with FastAPI
      - Provides endpoints for RMR calculations
    - [Frontend](https://github.com/yifattih/rmr-projection-client-browser)
      - Fully responsive and interactive single-page experience
      - Built with HTML, CSS, and jQuery
      - Static files served with Flask
    - [Deplyment Manager](https://github.com/yifattih/rmr-projection-iac)
        - Infrastructure as Code
        - Built with Terraform
- **Containerization**:
  - Docker is used to containerize the application
  - Docker Compose used in development environment to orchestrate the application services
  - Consistent environments across software lifecycle: development, testing, and deployment
- **CI/CD Pipeline**:
  - **GitHub Actions**: Automates the build, test, and delivery processes
  - **Linting and Static Analysis**: Integrated with **SonarCloud** for code quality and security analysis
  - **Test Coverage**: Coverage reports generated through **Codecov**, ensuring unit and integration tests cover critical functionality
  - **Automated Testing**: Unit and integration tests run on every push, pull request, and before deployment to catch issues early
- **Deployment**: 
  - **Infrastructure as Code (IaC)**: Managed with Terraform
  - **Containerization**: Docker images hosted on GCP Artifact Registry
  - **Orchestration**: Serverless with GCP Cloud Run
  - **CI/CD Pipeline**: GitHub Actions triggers builds, tests, reports, logging and deployments
  - **Deployment Strategy**: Automated and manual blue-green deployment strategy for zero-downtime
  - **Rollback Strategy**: Automated and manual instant reversion rollback on deployment failures
- **Observability**
  - **Monitoring and Alerting**: Prometheus for time series data. Grafana dashboards for visualization
  - **Logging**: Centralized logs via Google Cloud Logging

---

## Future Work
- Expanded Metrics: Track additional metrics like Total Daily Energy Expenditure (TDEE)
- Enhanced Visualization: Provide more detailed and interactive data visualizations
- Authentication, user accounts creation, and user data persistance for a more personalized experience
- Recommendations and prediction systems: Future implementation using [Neural Networks and other AI models](https://ui.adsabs.harvard.edu/abs/2024IEEEA..12o6050A/abstract)

---

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/yifattih/rmr-projection-api-model/blob/main/LICENSE) file for details

---

[![Continuous Integration](https://github.com/yifattih/rmr-projection-api-model/actions/workflows/ci_release.yml/badge.svg)](https://github.com/yifattih/rmr-projection-api-model/actions/workflows/ci_release.yml)
[![Deployment](https://github.com/yifattih/rmr-projection-iac/actions/workflows/deploy.yaml/badge.svg)](https://github.com/yifattih/rmr-projection-iac/actions/workflows/deploy.yaml)
[![Codecov](https://codecov.io/gh/yifattih/rmr-projection-api-model/graph/badge.svg?token=7CK07XM5W4)](https://codecov.io/gh/yifattih/rmr-projection-api-model)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=yifattih_bmr_calculator&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=yifattih_bmr_calculator)