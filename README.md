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

### Plans
1. LinkedIn Scraper & Messenger
    - Log in to LinkedIn account ✅
    - Get all open positions info
    - Reach out to people that work at the companies with "personalized" messages (Don't ask for referral, it doesn't work anymore. Lean into it, build the relationship first, find common ground, AND then ask for a referral)
    - Log everything in a database

2. Build recruiter google email scraper
    - Find recruiters' emails on google (there's an instagram video that shows how to do it)
    - Email them some "personalized" note saying that I am interested in X position (there's also a video on instagram that talks about how to reach out to recruiters)
    - Log everthing in a database

3. Auto apply
    - Apply for positions that were found on linkedin using one of the autofill applications plugins (if possible)

4. Add AI component
    - Train a model to determine if the user is qualified for a position
    - To tailor personalized messages to company employees & recruiters


### How to Run Tests

To run the unit tests for LinkedIn functions, use the following command:

```sh
python3 -m unittest tests/linkedin_functions_unittests.py
