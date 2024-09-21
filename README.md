# README.md

## Job-Hunter-3000: Automated LinkedIn Outreach and Job Application Tool

Job-Hunter-3000 is a Python-based application designed to streamline job searching and networking on LinkedIn. The tool automates the process of scraping job listings, managing user profiles, and sending personalized LinkedIn messages to foster professional connections. This tool aims to optimize the job search process by handling the repetitive tasks, allowing users to focus on building meaningful relationships and landing their next role.

### Features

- **Automated LinkedIn Login**: Logs into LinkedIn and handles different login scenarios (e.g., already signed in, saved profile, manual login).
- **Job Scraping**: Extracts job listings based on user-defined preferences, such as company, job title, and location.
- **Automated LinkedIn Outreach**: Scrapes LinkedIn profiles, sends personalized connection requests or messages, and follows up on unanswered requests.
- **Rate Limiting & Compliance**: Mimics human behavior by controlling message frequency and applying time delays to avoid LinkedIn detection.
- **Follow-Up System**: Automatically sends follow-up messages after a set period if no response is received.
- **User Profile Management**: Stores user details, including job preferences and qualifications, to personalize applications and networking.
- **Analytics & Tracking**: Tracks the success of messages and job applications, allowing users to refine their outreach strategy.

### Directory Structure

- **`utils`**: Contains utility functions and classes for LinkedIn interactions and scraping.
- **`career_tools`**: Contains modules for managing job applications and networking.

### Plans
1. LinkedIn Scraper & Messenger
    - Log in to LinkedIn account ✅
    - Get all open positions info ✅
    - Reach out to people that work at the companies with "personalized" messages (Don't ask for referral, it doesn't work anymore. Lean into it, build the relationship first, find common ground, AND then ask for a referral)
    - Log everything in a database

2. Google Recruiter Email Scraper
    - Find recruiters' emails via google (there's an instagram video that shows how to do it)
    - Email them some "personalized" note saying that I am interested in X position (there's also a video on instagram that talks about how to reach out to recruiters)
    - Log everthing in a database

3. Auto-Apply Feature
    - Automate job applications for positions found on LinkedIn using autofill plugins (Simplify, Jobfill, etc.)

4. AI Integration
    - Add machine learning models to:
        - Evaluate job qualifications
        - Tailor messages to company employees and recruiters based on user profiles
     
6. React Web App
    - Build a react web app and give access to friends


### How to Run Tests

To run the unit tests for LinkedIn functions, use the following command:

```sh
python3 -m unittest tests/linkedin_functions_unittests.py
