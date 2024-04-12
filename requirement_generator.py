# generates requirements.txt file for the project and add all the django requirements to it.
def generate():
    """Generate a requirements.txt file for the Django project."""
    with open("requirements.txt", "w") as requirements_file:
        requirements_file.write("django\n")
        requirements_file.write("pillow\n")
        requirements_file.write("django-crispy-forms\n")
        requirements_file.write("django-extensions\n")
        requirements_file.write("django-filter\n")
        requirements_file.write("django-rest-framework\n")
        requirements_file.write("gunicorn\n")
        requirements_file.write("psycopg2\n")
        requirements_file.write("whitenoise\n")
    
    print("Requirements file generated successfully!")

if __name__ == "__main__":
    generate()