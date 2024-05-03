# run the two python code files continuously config_setup.py and neev_cli.py
config_setup.py
neev_cli.py
```
I want to run the two python code files continuously in the background. I have tried the following code but it is not working.

```
# Path: templates/neev.sh
# run the two python code files continuously config_setup.py and neev_cli.py
python3 config_setup.py &
python3 neev_cli.py &
```
I have also tried the following code but it is not working.

```
# Path: templates/neev.sh
# run the two python code files continuously config_setup.py and neev_cli.py
nohup python3 config_setup.py &
nohup python3 neev_cli.py &


