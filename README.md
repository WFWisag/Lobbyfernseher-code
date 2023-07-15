# Diashowsystem for Lobby-TV

This is the sourcecode for a diashowsystem including an RSS-feed.

## Techstack

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask

## Installation

1. Clone the repository
2. Install the requirements

Reqirements:

- Python 3.x (as up to date as possible)
- Python Flask

3. Create a file called `SECRETKEY.txt` in the `/src/app/`-directory and paste a secret key in it. You can generate a secret key with the following command in the Python shell:

```python
import os
os.urandom(12)
```

4. Create one or more user accounts in the `users.json` file in the `/src/app/data/`-directory. The file should look like this:

```json
{
  "users": [
    {
      "username": "username",
      "password": "password"
    }
  ]
}
```

5. Run the `main.py` file in the `/src/`-directory with Python. The server will start on port 5000. So you can access the website with `localhost:5000`. If you want to change the port, you can do this in the `main.py` file, by changing the value of `port` in the `app.run()` function.

Additional:
If you want to automatically open the website in fullscreen mode on startup, you can add the following line to the `main.py` file, **if used on a Raspberry Pi**:

```python
from app import create_app
# Add this line
import os
# ----------------

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # and this line too:
    os.system("chromium-browser --start-fullscreen localhost:5000")
    # ------------------
```

## Usage

1. Login with your user account. When you are successfully logged in, you will be redirected to the dashboard.

2. On the Dashboard you can go to the configuration of the Slider. There you can add and delete slides, change the duration of the images displayed in the slider.

_Note: If you want to change the order of the images and videos, how they are displayed, then you have to rename them manually. It could be done like following:_

`- 01_img.jgp`
`- 02_img.jpg`
`- 03_video.mp4`

3. After the configuration of the slider, you go back to the dashboard and click on the link to the slider. It should automatically start the slider.

4. To escape the slider, you have to press the `ESC`-key on your keyboard.

**NOTE: This software is still in development! Some feautures such as the implementation of a RSS-Feed are planed!**
