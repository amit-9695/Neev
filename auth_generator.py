import os
def get_auth_page_config():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return {
        '1' : {
            "login_dir": "templates/authentication/login1",
            "register_dir": "templates/authentication/register1",
            'login_file': base_dir + '/templates/authentication/login1/login.html',
            'register_file': base_dir + '/templates/authentication/register1/register.html',
            'login_css': base_dir + '/templates/authentication/login1/login.css',
            'register_css': base_dir + '/templates/authentication/register1/register.css',
            'login_bg': '',
            'register_bg': base_dir + '/templates/authentication/register1/register_bg.jpg',
        },
        '2' : {
            "login_dir": "templates/authentication/login2",
            "register_dir": "templates/authentication/register2",
            'login_file': base_dir + '/templates/authentication/login2/login2.html',
            'register_file': base_dir + '/templates/authentication/register2/register2.html',
            'login_css': base_dir + '/templates/authentication/login2/login2.css',
            'register_css': '',
            'login_bg': base_dir + '/templates/authentication/login2/login2_bg.jpg',
            'register_bg': '',
        }, # type: ignore
        
        '3' : { 
            "login_dir": "templates/authentication/login3",
            "register_dir": "templates/authentication/register1",
            'login_file': base_dir + '/templates/authentication/login3/login3.html',
            'register_file': base_dir + '/templates/authentication/register1/register.html',
            'login_css': base_dir + '/templates/authentication/login3/login3.css',
            'register_css': base_dir + '/templates/authentication/register1/register.css',
            'login_bg': base_dir + '/templates/authentication/login3/bg-1.jpg',
            'register_bg': base_dir + '/templates/authentication/register1/register_bg.jpg',
            'login_js': base_dir + '/templates/authentication/login3/bootstrap.min.js, ' + base_dir + '/templates/authentication/login3/jquery.min.js, ' + base_dir + '/templates/authentication/login3/popper.min.js, ' + base_dir + '/templates/authentication/login3/login3.js',

        },
    }
