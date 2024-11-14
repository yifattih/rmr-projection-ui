# Basal Metabolic Rate (BMR) Calculator Web App
---

This is a **single-page web application** designed to calculate and visualize Basal Metabolic Rate (BMR) changes over time. The app helps users monitor their BMR, offering insights into how lifestyle changes, body metrics, or other factors can impact daily energy expenditure at rest.

### Access the App
---

You can try out the BMR Calculator through this link: [BMR Calculator Web App](https://bmr-calculator-prod-366291964646.us-central1.run.app)

## Features
---

- **Data Input Form**: Input your personal details (age, weight, height, etc.) for BMR calculation in a user-friendly form.
- **BMR Calculation**: The backend service calculates your BMR based on established scientific formulas.
- **Data Visualization**: View your BMR changes over time through interactive visualizations.

## Tech Stack
---

The app leverages a streamlined DevOps pipeline to ensure seamless development, testing, and deployment processes. Here’s an overview of the stack and CI/CD practices in place:

- **Backend**: Python Flask application, providing API endpoints for BMR calculations.
- **Frontend**: HTML, CSS, and jQuery for a responsive and interactive single-page experience.
- **Containerization**: Docker is used to containerize the application, ensuring consistent environments across development, testing, and deployment.
- **CI/CD Pipeline**: GitHub Actions automates the build, test, and deployment processes:
  - **Linting and Static Analysis**: Integrated with **SonarCloud** for code quality and security analysis.
  - **Test Coverage**: Coverage reports generated through **Codecov**, ensuring unit and integration tests cover critical functionality.
  - **Automated Testing**: Unit and integration tests run on every pull request and before deployment to catch issues early.
- **Deployment**: Google Cloud Run (staging environment) enables scalable, serverless deployment of Docker containers:
  - **Staging and Testing**: The app is deployed to a free staging environment on Google Cloud Run, allowing safe feature testing and bug fixing.
  - **Continuous Delivery**: Each push to the main branch triggers an automated deployment to the staging environment, with plans to add a production environment in the future.
- **Rollback Strategy**: Automated rollback to the last stable version on Google Cloud Run in the event of a failed deployment or severe bug.

## Usage Guide
---

1. **Input Data**: Complete the form with relevant personal information to generate an accurate BMR calculation.
2. **Calculate BMR**: After submitting your details, the app calculates your BMR, giving you insights into your daily calorie needs at rest.
3. **Visualize Changes**: Track BMR fluctuations over time, using visualizations to monitor the effects of lifestyle and health changes.

## Future Improvements
---

- **Expanded Metrics**: Track additional metrics like Total Daily Energy Expenditure (TDEE).
- **Enhanced Visualization**: Provide more detailed and interactive data visualizations.
- **User Accounts**: Implement user authentication for a more personalized experience.

## License
---

This project is licensed under the MIT License. See the `LICENSE` file for more details.


[![CI/CD Pipeline](https://github.com/yifattih/bmr_calculator/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/yifattih/bmr_calculator/actions/workflows/ci-cd.yml)
![Codecov](https://img.shields.io/codecov/c/gh/yifattih/bmr_calculator)
![Sonar Quality Gate](https://img.shields.io/sonar/quality_gate/yifattih_bmr_calculator?server=https%3A%2F%2Fsonarcloud.io)
