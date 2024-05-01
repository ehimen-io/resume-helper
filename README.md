# resume-helper
## Description

An AI assisted resume helper to streamline the process of tailoring resumes to jobs.

It will:
1. Generate bullet points relevant to the job posting
2. Estimate the years of experience needed for the job
3. List the tech stack needed to be a successful applicant

In addition, `resume-helper` also features a chat interface to ask questions about your resume and your chances of getting the job.

## Installation

This project requires Python 3.7 or higher. 

1. Clone the repository:
    ```
    git clone https://github.com/ehimen-io/resume-helper.git
    cd resume-helper
    ```

2. Create a virtual environment (optional, but recommended):
    ```
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Configuration

This project uses the `python-dotenv` package for environment variables.
> At this time, It is important to have an OpenAI API key to run this project.
> Navigate to https://platform.openai.com/docs/quickstart to understand how to create your own API key.

1. Copy the `.env.example` file and create a new `.env` file:
    ```
    cp .env.example .env
    ```

2. Open the `.env` file and set your environment variables (specifically your OpenAI API key).

## Running the Project

After installing the dependencies and setting up the environment variables, you can run the project with:
```
python main.py
```

## Usage
After running the project:
1. Copy the job description into `/resources/job.txt`
2. Copy your resume into `/resources/resume.txt`
3. Type `g` and press `Enter` to generate resume bullet points, tech stack and deduce the years of experience 
4. Type `c` and press `Enter` to enter the chat interface:
   1. Type `qc` and press `Enter` while in the chat interface to exit the chat
5. Type `q` and press `Enter` at any point to exit the application

## Feature requests
Please open an issue for all feature requests and bugs.

