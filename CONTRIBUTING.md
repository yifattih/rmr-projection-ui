# Contributing to the BMR Calculator Web App

Follow these guidelines to make your contributions seamless and effective.

## Branching Strategy

This project follows a structured branching model:

- **`main`**: Production-ready code. Merging into this branch triggers a release.
- **`beta`**: For user testing. Merging triggers deployment to a testing environment.
- **`alpha`**: For internal testing. Merging triggers deployment to a testing environment.
- **`dev`**: Continuous integration branch for new features and bug fixes.
- **`feat/feature-name`**: Feature or bug-fix branches used during active development.

### Where Should You Contribute?

Contributors should create their branches off the **`dev`** branch and submit Pull Requests (PRs) back to **`dev`**. Ensure your changes are isolated to their purpose, and commit messages are clean and descriptive.

## Setting Up Your Environment

### Prerequisites

- Install [Docker](https://www.docker.com/)
- If you are on Windows, configure your computer to use the Linux File system
- Install [VS Code](https://code.visualstudio.com/)
- Install VS Code [Devcontainers extension](https://code.visualstudio.com/docs/devcontainers/containers)
- Ensure Docker engine is running

## Development Workflow

1. **Fork and Clone the Repository**
    - Fork the repository to your GitHub account.
    - Open the project repo locally following the Devcontainers extension to **clone repository in container volume**
2. **Create a Feature Branch**
    - Create a branch for your contribution:
        - Make sure your branch name follows the required format
        
        ```bash
        git checkout -b feat/<your-feature-name> dev
        
        ```
        
3. **Write and Test Code**
    - Follow the project’s code style and standards (e.g., flake8, black).
    - Add or update tests if applicable.
    - Test your changes locally.
4. **Commit Messages**
    - Use the [commit convention](COMMIT_CONVENTION.md)
        
        ```bash
        <type>(<scope>): <description>
        
        [optional body]
        
        [optional footer]
        ```
        
    - Examples
        
        ```
        feat(ui): improve input form styling
        fix(backend): handle edge case for BMR calculation
        
        ```
        
5. **Push and Create a Pull Request**
    - Push your branch to your fork
        
        ```bash
        git push origin feat/your-feature-name
        
        ```
        
    - Open a PR to the **`dev`** branch of the original repository
    - Fill out the PR template with detailed information of changes or new implementations

## Pull Request Guidelines

- Ensure all commits pass CI checks.
- Rebase your branch onto `dev` to avoid merge conflicts:
    
    ```bash
    git fetch upstream
    git rebase upstream/dev
    
    ```
    
- Squash commits if needed to maintain a clean commit history.
- Add detailed descriptions in your PRs, including:
    - What problem does this solve?
    - Relevant issue(s) (if applicable).
    - Testing steps.

## Testing

This project uses `pytest` for backend testing and GitHub Actions for CI. Run tests locally before submitting your PR:

- **Run Tests**
    
    ```bash
    pytest
    
    ```
    
- **Check Linting and apply formmating**
    
    ```bash
    flake8
    black --check .
    black .
    
    ```