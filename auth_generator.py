def get_auth_page_config():
    return {
        '1' : {
            "login_dir": "templates/authentication/login1",
            "register_dir": "templates/authentication/register1",
            'login_file': 'login1.html',
            'register_file': 'register1.html',
            'login_css': 'login.css',
            'register_css': 'register.css',
            'login_bg': '',
            'register_bg': 'register_bg.jpg',
        },
        '2' : {
            "login_dir": "templates/authentication/login2",
            "register_dir": "templates/authentication/register2",
            'login_file': 'login2.html',
            'register_file': 'register2.html',
            'login_css': 'login2.css',
            'register_css': '',
            'login_bg': 'login2_bg.jpg',
            'register_bg': '',
        } # type: ignore
    }
