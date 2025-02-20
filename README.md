# README

#### Description

A python program to automate resume creation using a standarized json resume format and the python-docx library

#### Summary

I got sick of dealing with word documents, so I created this program to make it easier to edit and manage resume data, which is the important part. Editing data with a WYSIWYG editor like Word or god forbid Libre Office is a bit of a pain. You make a change, it messes up your formatting etc. Latex is great but is very involved and not really necessary for something like a simple resume. In short, make the machines do the work.

Eventually I'd like to add some locally hosted AI so you could feed it a job description, and then have it cross reference your json data and prioritize certain keywords and give you ratings based on those words. That'll come later. For now, just basic data and automated formatting.

#### Setup

I've provided a default_resume.json. It has some default properties that you can fill out.

The current properties are name, contact, summary, education, experience, skills, projects, publications, and certifications. Feel free to add or remove properties as needed, but be aware that you'll need to modify code for the time being to account for those changes.

Eventually, I'll have it set up so that you can programmatically look for different properties, and make it a bit cleaner to interact with. Messing with anything assumes you know what you're doing.

#### How to run

If you have UV installed, the environment is set up so that it comes with the necessary dependencies including python and the docx library. To run, simply invoke ``uv run resume_generator.py`` in the directory.

If you're not using UV, you need to pip install python-docx or add it to your virtual environment.

The generated document will be saved to the resume_docx directory
