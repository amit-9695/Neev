import json

def get_project_config():
    print("Please enter your Django project configuration details:")
   
    # Collecting project configuration details
    config = {}
    title = input("Enter the title of your project: ")
    if title:
        config['title_of_project'] = title
    else:
        config['title_of_project'] = "Neev Project"
    summary = input("Enter a brief summary of your project in one line: ")
    config['summary'] = summary
    author = input("Enter the author of the project: ")
    if author:
        config['author'] = author
    else:
        config['author'] = "neev_user"
    email = input("Enter the email of the author: ")
    if email:
        config['email'] = email
    else:
        config['email'] = ""
    database_type = input("Enter the type of database you want to use (postgresql, mysql): ")
    if database_type:
        config['database_type'] = database_type
    else:
        config['database_type'] = "mysql"
    db_name = input("Enter the name of the database: ")
    if db_name:
        config['db_name'] = db_name
    else:
        config['db_name'] = "mydatabase"
    db_user = input("Enter the username of the database: ")
    if db_user: config['db_user'] = db_user
    else: config['db_user'] = "root"
    db_password = input("Enter the password of the database: ")
    if db_password: config['db_password'] = db_password
    else: config['db_password'] = ""
    db_host = input("Enter the host of the database: ")
    if db_host:config['db_host'] = db_host
    else: config['db_host'] = "localhost"
    db_port = input("Enter the port of the database: ")
    if db_port:config['db_port'] = db_port
    else: config['db_port'] = "3306"
    is_auth_app_needed = input("Do you want to create an authentication app? ([yes]/no): ") or "yes"
    if is_auth_app_needed.lower() == "yes" or not is_auth_app_needed:
        config['auth_app_needed'] = True
        auth_template_choice = input("Choose the authentication app template ([1], 2 ): ") or "1"
        config['auth_template_choice'] = auth_template_choice
    else:
        config['auth_app_needed'] = False
    need_apps = input("Do you want to create any additional apps? ([yes]/no): ") or "yes"
    if need_apps.lower() == "yes" or not need_apps:
        config['additional_apps'] = []
        apps = input("Enter the names of the additional apps separated by commas: ")
        if apps:
            config['additional_apps'] = [name.strip() for name in apps.split(',')]
    else:
        config['additional_apps'] = []
    print("Please enter the details of the static and media directories:")
    static_dir = input("Enter the name of the static directory (should not be static): ")
    if static_dir:config['static_dir'] = static_dir
    else: config['static_dir'] = "assets"
    media_dir = input("Enter the name of the media directory: ")
    if media_dir: config['media_dir'] = media_dir
    else: config['media_dir'] = "media"
    # condition for landing page needed or not
    is_landing_page_needed = input("Do you want to create a landing page? ([yes]/no): ") or "yes"
    if is_landing_page_needed.lower() == "yes" or not is_landing_page_needed:
        config['landing_page_needed'] = True
        landing_page_templates = input("Choose the landing page template ([1], 2, 3, 4,5): ") or "1"
        config['landing_page_templates'] = landing_page_templates
    else:
        config['landing_page_needed'] = False
    
    activate_vcs = input("Do you want to activate version control (git)? ([yes]/no): ")
    if activate_vcs.lower() == "yes" or not activate_vcs:
        config['vcs'] = True
    else:
        config['vcs'] = False
    
    # Write the configuration to a JSON file
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

    print("Configuration saved successfully!")

if __name__ == "__main__":
    get_project_config()
