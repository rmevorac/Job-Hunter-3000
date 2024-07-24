# README.md

## Job-Hunter-3000

Job-Hunter-3000 is a Python-based application designed to automate job searches and networking on LinkedIn. This tool allows users to streamline the process of finding and applying for jobs by scraping job listings, managing user profiles, and automating LinkedIn interactions.

### Features

- **Automated LinkedIn Login**: Logs into LinkedIn and handles different login scenarios (e.g., already signed in, saved profile, manual login).
- **Job Scraping**: Extracts job listings based on user preferences.
- **User Profile Management**: Stores and manages user details, including job preferences and qualifications.

### Directory Structure

- **`utils`**: Contains utility functions and classes for LinkedIn interactions and scraping.
- **`career_tools`**: Contains modules for managing job applications and networking.

### How to Run Tests

To run the unit tests for LinkedIn functions, use the following command:

```sh
python3 -m unittest tests/linkedin_functions_unittests.py
