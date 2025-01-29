# AQUAS
This repository contains the source code, documentation, and guidelines for contributing for the AQUAS project, where we're designing an autonomous robot to detect and clear Harmful Algal Blooms (HABs)

## Coding Standards ##
Follow naming conventions and clean coding principles.
* Use meaningful commit messages.
* Write unit tests for new features and bug fixes.
* Keep functions and methods modular.

## Repo structure ##
For now, our repo is separated by "legacy" or old code used in F22-S23, and project files that we are stil working on. 
If you are working on a new project that doesn't fall under any of the current project files, create a new directory, and use underscores in place of spaces and lowercase.

## Getting Started

### Cloning the Repository

To get a local copy of the repository, run:

```sh
git clone https://github.com/AQUAS-mission/aquas.git
```

### Setting Up

1. Navigate to the project directory:
   ```sh
   cd aquas
   ```
2. Install necessary dependencies (if applicable):
   ```sh
   npm install  # For JavaScript-based projects
   pip install -r requirements.txt  # For Python-based projects
   ```

## Contribution Guidelines

### Pull Request Process

1. **Fork** the repository and create a new branch:
   ```sh
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them with a descriptive message:
   ```sh
   git commit -m "Add feature: description of the feature"
   ```
3. Push your changes to your forked repository:
   ```sh
   git push origin feature/your-feature-name
   ```
4. Open a **Pull Request** to merge into `main`.
5. Wait for code review and address any feedback.

## Git Workflow

### Pull the Latest Changes

Before starting work, always pull the latest changes from the main branch:

```sh
git pull origin main
```

### Staging, Committing, and Pushing Changes

1. Check modified files:
   ```sh
   git status
   ```
2. Add specific files or all changes:
   ```sh
   git add <file_name>
   git add .
   ```
3. Commit with a meaningful message:
   ```sh
   git commit -m "Fix: brief message about the change"
   ```
4. Push to your branch:
   ```sh
   git push origin <branch_name>
   ```


## Download

You can download this README as a `.README` file:

```sh
curl -o AQUAS.README https://raw.githubusercontent.com/AQUAS-mission/aquas/main/README.md
```

