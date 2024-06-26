import os
def get_landing_page_config():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return {
        '1' : {
            'folder': base_dir+ r'\templates\Landing_Pages\Landing1',
            'file': base_dir + r'\templates\Landing_Pages\Landing1\landing1.html',
            'rename': 'index.html',
            'assets': base_dir + r'\templates\Landing_Pages\Landing1\assets'
        },
        '2' : {
            'folder': base_dir + r'\templates\Landing_Pages\Landing2',
            'file': base_dir + r'\templates\Landing_Pages\Landing2\index.html',
            'assets': base_dir + r'\templates\Landing_Pages\Landing2\assets'
        },
        '3' : {
            'folder':base_dir + r'\templates\Landing_Pages\Landing3',
            'file': base_dir + r'\templates\Landing_Pages\Landing3\landing3.html',
            'rename': 'index.html',
            'assets': base_dir + r'\templates\Landing_Pages\Landing3\dist'
        },
        '4' : {
            'folder': base_dir + r'\templates\Landing_Pages\Landing4',
            'file': base_dir + r'\templates\Landing_Pages\Landing4\landing4.html',
            'rename': 'index.html',
            'assets': base_dir + r'\templates\Landing_Pages\Landing4\assets'
        },
    }