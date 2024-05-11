import os
def get_auth_page_config():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return {
        '1' : {
            "login_dir": "templates/authentication/login1",
            "register_dir": "templates/authentication/register1",
            'login_file': base_dir + '/templates/authentication/login1/login1.html',
            'register_file': base_dir + '/templates/authentication/register1/register.html',
            'login_css': base_dir + '/templates/authentication/login1/login1.css',
            'register_css': base_dir + '/templates/authentication/register1/register.css',
            'login_bg': base_dir + '/templates/authentication/login1/bg-1.jpg',
            'register_bg': base_dir + '/templates/authentication/register1/register_bg.jpg',
            'login_js': base_dir + '/templates/authentication/login1/main.js',
        },
        '2' : {
            "login_dir": "templates/authentication/login2",
            "register_dir": "templates/authentication/register2",
            'login_file': base_dir + '/templates/authentication/login2/login2.html',
            'register_file': base_dir + '/templates/authentication/register2/register2.html',
            'login_css': base_dir + '/templates/authentication/login2/login2.css',
            'register_css': base_dir + '/templates/authentication/register2/register2.css',
            'login_bg': base_dir + '/templates/authentication/login2/login2_bg.jpg',
            'register_bg': base_dir + '/templates/authentication/register2/form-v6.jpg',
        }, # type: ignore
    }
