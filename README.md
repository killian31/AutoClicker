# AutoClicker
Short python code for an auto-clicker (or auto typing a letter on the keyboard) using pyautogui.
The user provides the delay (in seconds) between the clicks (or between the 10 presses of keyboard), and the number of clicks desired.
For a precise number of clicks, use the clicker mode. For large and fast keyboard actions, use the auto-press (less precise because it does 10 actions at a time).

The program will launch after a 3 seconds countdown to allow the user to put the mouse wherever it is needed.
The program will provide the start time of the process, the time at wich all the clicks have been done and the duration of the process at the end.

## Install with pyenv and Poetry

Create and activate a new virtualenv with 
```bash
pyenv virtualenv 3.12.0 autoclick
pyenv activate autoclick
```

Then install the project with
```bash
pip install poetry
poetry install
```

## Run the AutoClicker

```bash
poetry run python ClickerBot.py
```
