import argparse
import subprocess
import json
import os
from requirement_generator import generate as generate_requirements

def install_requirements(project_name):
    """Install the required packages using pip."""
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    generate_requirements()
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

def create_django_project():
    """Create a Django project."""
    subprocess.run(["django-admin", "startproject", 'config', '.'], check=True)

def setup_directories(project_name):
    """Create additional directories for the Django project."""
    os.makedirs(os.path.join(project_name, "templates"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "config"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "assets"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "shop"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "media"), exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Setup a new Django project with Neev.")
    parser.add_argument("--install", help="Install project requirements.", action="store_true")
    parser.add_argument("--create", help="Create a new Django project.", action="store_true")
    parser.add_argument("--setup", help="Set up project directories.", action="store_true")

    args = parser.parse_args()

    if args.install:
        install_requirements(config['title_of_project'])

    if args.create:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            create_django_project()

    if args.setup:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            setup_directories(config['title_of_project'])

if __name__ == "__main__":
    main()
