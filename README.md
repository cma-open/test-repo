# User and developer instructions

This repository contains a Python package that requires specific conda environments. 
The conda environments and additional resources are stored in separate repositories, 
which are linked as submodules.

## Table of Contents

- Installation
- Usage
- Development Setup
- Keeping Repositories in Sync

## Installation

### Prerequisites

- Git
- Miniconda or Anaconda

### Clone the Repository

First, clone this repository along with its submodules. 
The submodules contain the conda environment files needed for this project.

```bash
git clone --recurse-submodules git@github.com:cma-open/test-repo.git  # ssh
# git clone --recursive-submodules https://github.com/cma-open/test-repo.git # https
cd test-repo
```

### Set Up the Conda Environments
Navigate to the submodule directories and create the conda environments:

```bash
cd scripts/conda
./create-conda-environment.sh
```

### Install the Package
Return to the main repository directory and install the package:

```bash
# Activate the conda environment
conda activate projects-environment
# Install the package into the activated environment
pip install .
```

## Usage

Once the package is installed and the conda environments are activated, 
you can use the package as follows:

```bash
# Activate the conda environment
conda activate projects-environment
python -m trepo
```

## Development Setup

### Linking Repositories with Submodules
This project uses Git submodules to link the main repository with the repositories 
containing the conda environment files and shell scripts.
Here’s how the repositories are configured to work together:

Add Repo B and Repo C as Submodules in Repo A:

cd path/to/repoA
git submodule add git@yourcompany.com:username/repoB.git path/to/repoB
git submodule add git@yourcompany.com:username/repoC.git path/to/repoC
git submodule update --init --recursive

Within the checked out repo these settings can be confirmed in the following files. 

### Configuration Files:

```bash
.gitmodules:
[submodule "path/to/repoB"]
    path = path/to/repoB
    url = git@yourcompany.com:username/repoB.git
[submodule "path/to/repoC"]
    path = path/to/repoC
    url = git@yourcompany.com:username/repoC.git
.git/config:
[submodule "path/to/repoB"]
    url = git@yourcompany.com:username/repoB.git
[submodule "path/to/repoC"]
    url = git@yourcompany.com:username/repoC.git
```

### Setting Up for Development
If you want to contribute to the development of this package, follow these steps:

Fork the repository on your internal Git platform.
Clone your fork to your local machine, including the submodules:
```bash
git clone --recurse-submodules git@yourcompany.com:yourusername/repoA.git
cd repoA
```

Set up the conda environments:
```bash
cd path/to/repoB/scripts
c./create-conda.environment.sh
conda activate myenv
cd ../..
```

Install the package in editable mode:
```bash
pip install -e .
```

### Running Tests
To run the tests, make sure the conda environment is activated and then use pytest:

```bash
conda activate myenv  # Activate the appropriate environment
pytest
```

## Keeping Repositories in Sync
When working with submodules, it's important to keep the main repository (Repo A) and 
the submodule repositories (Repo B and Repo C) in sync, especially if they are worked 
on separately. Here are some tips to manage this:

### Pulling Updates:

To pull the latest changes from all repositories, use:
```bash
git pull --recurse-submodules
git submodule update --remote
```

### Making Changes in Repo B or Repo C:

If you make changes in Repo B or Repo C, commit and push those changes in the 
respective repository first:

```bash
cd path/to/repoB  # or path/to/repoC
git add .
git commit -m "Your commit message"
git push origin main
```

### Updating Repo A with Changes from Repo B or Repo C:

After updating Repo B or Repo C, update the submodule reference in Repo A:

```bash
cd path/to/repoA
git submodule update --remote path/to/repoB
git submodule update --remote path/to/repoC
git add path/to/repoB path/to/repoC
git commit -m "Update submodules to latest versions"
git push origin main
```

### Cloning and Updating Submodules:

When cloning Repo A, always use the --recurse-submodules flag 
to ensure submodules are cloned:
```bash
git clone --recurse-submodules git@yourcompany.com:username/repoA.git
cd repoA
# To update submodules after cloning, use:
git submodule update --init --recursive
```

By following these steps, you can ensure that all repositories remain in sync and 
that any changes made in one repository are properly reflected in the others.


