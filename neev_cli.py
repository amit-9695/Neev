import json
import os
import subprocess

def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def create_django_project(config):
    # Creating the Django project
    subprocess.run(["django-admin", "startproject", config['title_of_project']])
    
    # Change into the project directory
    os.chdir(config['title_of_project'])

    # Setting up the database settings
    database_settings = f"""
DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.{config['database_type']}',
        'NAME': '{config['db_name']}',
        'USER': '{config['db_user']}',
        'PASSWORD': '{config['db_password']}',
        'HOST': '{config['db_host']}',
        'PORT': '{config['db_port']}',
    }}
}}
"""
    # Append database settings to settings.py
    with open('settings.py', 'a') as settings:
        settings.write(database_settings)

    # Create additional apps if needed
    if config['additional_apps']:
        for app in config['additional_apps']:
            subprocess.run(["python", "manage.py", "startapp", app])

    # Setup version control if required
    if config['vcs']:
        subprocess.run(["git", "init"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Initial commit"])

    print("Django project setup complete.")

def main():
    config = load_config()
    create_django_project(config)

if __name__ == "__main__":
    main()