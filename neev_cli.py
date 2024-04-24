import json
import os
import subprocess
from landing_generator import generate_landing_page
from auth_generator import get_auth_page_config
     

def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def create_django_project(config):
    os.makedirs(config['title_of_project'], exist_ok=True)
    os.chdir(config['title_of_project'])
    # Creating the Django project
    subprocess.run(["django-admin", "startproject", "core", "."])
    
    # Create additional apps if needed
    if config['additional_apps']:
        for app in config['additional_apps']:
            subprocess.run(["python", "manage.py", "startapp", app])

    # create authentication app if needed
    if config['auth_app_needed']:
        os.makedirs('accounts', exist_ok=True)
        # copy the account app files
        subprocess.run(["cp", "-r", "accounts", "accounts"])
        
    
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

    with open('core/settings.py', 'r+') as settings:
        # find the existing DATABASES setting and replace it with the new one
        settings.seek(0)
        settings_data = settings.read()
        db_string_to_replace= '''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
        settings_data = settings_data.replace(db_string_to_replace, database_settings)

        # find templates directory setting and replace it with the new one
        settings_data = settings_data.replace("'DIRS': [],", "'DIRS': [BASE_DIR / 'templates'],")

        # exisiting installed apps
        apps_to_replace = '''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]'''
        # find the installed apps and replace it with the new one
        new_apps = "".join([f"'{app}',\n" for app in config['additional_apps']])
        new_apps = f"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    {new_apps}
]"""
        settings_data = settings_data.replace(apps_to_replace, new_apps)

        # add static and media settings from config
        settings_data += f"""
STATICFILES_DIRS = [BASE_DIR / '{config['static_dir']}']
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
"""
        settings.seek(0)
        settings.write(settings_data)

    # create templates directory
    os.makedirs('templates', exist_ok=True)
    # create accounts folder in templates if auth app is needed
    os.makedirs('templates/accounts', exist_ok=True)
    
    login_template = {
        1: 'templates/authentication/login1'
    }

    # create static directory
    os.makedirs(config['static_dir'], exist_ok=True)

    # create media directory
    os.makedirs(config['media_dir'], exist_ok=True)

    # create landing pages
    landing_pages = generate_landing_page()
    landing_page_settings = landing_pages[config['landing_page_templates']]
    if os.path.exists(landing_page_settings['folder']):
        subprocess.run(["cp", "-r", landing_page_settings['assets'], config['static_dir']])
        # copy the landing page file to the templates directory
        subprocess.run(["cp", landing_page_settings['file'], "templates"])
        os.rename(f"templates/{landing_page_settings['file']}", f"templates/index.html")
    
    # create auth page
    auth_pages = get_auth_page_config()
    auth_page_settings = auth_pages[config['auth_template_choice']]
    # COPY CSS to static directory
    subprocess.run(["cp", auth_page_settings['login_css'], config['static_dir']+"/css/"])
    subprocess.run(["cp", auth_page_settings['register_css'], config['static_dir']+"/css/"])
    # COPY images to static directory
    subprocess.run(["cp", auth_page_settings['login_bg'], config['static_dir']+"/images/"])
    subprocess.run(["cp", auth_page_settings['register_bg'], config['static_dir']+"/images/"])
    # COPY login and register html files to templates directory as login.html and register.html
    subprocess.run(["cp", auth_page_settings['login_dir']+"/"+auth_page_settings['login_file'], "templates/login.html"])
    subprocess.run(["cp", auth_page_settings['register_dir']+"/"+auth_page_settings['register_file'], "templates/register.html"])

    

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