"""
This file defines the User class, which encapsulates all relevant information for a user of the job application program. 
The User class stores details such as name, username, password, and job preferences, and provides methods for handling 
user-specific operations.
"""

import inquirer

class User():
    def __init__(self, first_name=None, last_name=None, username=None, password=None, job_preferences=None, qualifications=None):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}" if first_name and last_name else None
        self.username = username
        self.password = password
        self.job_preferences = job_preferences if job_preferences is not None else []
        self.qualifications = qualifications if qualifications is not None else {}

    def set_user_info(self):
        """Prompt user to enter their personal information."""
        self.first_name = input("Enter your first name as it appears on your LinkedIn profile: ")
        self.last_name = input("Enter your last name as it appears on your LinkedIn profile: ")
        self.full_name = f"{self.first_name} {self.last_name}"
        self.username = input("Enter your LinkedIn email/phone: ")
        self.password = input("Enter your LinkedIn password: ")

    def set_job_preferences(self):
        job_arrangement_question = [
            inquirer.Checkbox('job_arrangement',
                message="What is your preferred work arrangement?",
                choices=['On-Site', 'Hybrid', 'Remote'],)]
        
        add_job_question = [
            inquirer.List('add_job',
                message="Do you want to add another job search?",
                choices=['yes', 'no'])]

        add_more = True
        while add_more:
            title = input("Enter job title: ")
            location = input("Enter job location: ")
            job_arrangement_answer = inquirer.prompt(job_arrangement_question)

            self.job_preferences.append({'title': title, 'location': location, 'job_arrangement': job_arrangement_answer['job_arrangement']})

            add_job_answer = inquirer.prompt(add_job_question)
            add_more = add_job_answer['add_job'] == 'yes'

    def set_job_qualifications(self):
        years = input("Enter the number of years of experience you have: ")
        skills = self.set_skills()
        self.qualifications = {'years': years, 'skills': skills}
    
    def set_skills(self):
        add_skill_question = [
            inquirer.List('add_skill',
                message="Do you want to add another job search?",
                choices=['yes', 'no'])]
        skills = []
        add_more = True

        while add_more:
            #Change the quesion
            skills.append(input("Enter a skill for your new job: "))

            add_job_answer = inquirer.prompt(add_skill_question)
            add_more = add_job_answer['add_skill'] == 'yes'
    
    def display_info(self):
        job_preferences_str = "\n\n".join([
            f"Title: {job['title']}\nLocation: {job['location']}\nWork Arrangement: {', '.join(job['job_arrangement'])}"
            for job in self.job_preferences
        ])

        qualifications_str = "\n\n".join(f"Years of Experience: {self.qualifications['years']}\nSkills: {', '.join(self.qualifications['skills'])}")
        return f"Name: {self.first_name} {self.last_name}\nUsername: {self.username}\nPassword: {self.password}\n\nJob Preferences:\n{job_preferences_str}\n\nQualifications:\n{qualifications_str}"
