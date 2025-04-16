Automate Clearing of Cricut Cache
---------------------------------

  
  

### Verify python is installed

To open Command Prompt -

*   Press Win + R, type "cmd", and hit Enter. A black window will appear.

Then type
*   "python --version" and press enter
*   "pip --version" and press enter

If they are not installed (if either of them gives you anything other than a version number)

*   Go to [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
*   Download the latest version for Windows.
*   Run the installer with these options:
    *   Check "Add Python to PATH"
    *   Click "Install Now"

### Download the scripts

Right click on the two links below and "Save link as" and save the files to your Desktop folder  
(you can save it anywhere else, but in the steps below you'll need to cd to that folder instead - if you don't know what that means, keep it on your Desktop :)

*   [requirements.txt](https://raw.githubusercontent.com/michaeljcohen/cricut_cache/refs/heads/main/requirements.txt)
*   [resetcricut.py](https://raw.githubusercontent.com/michaeljcohen/cricut_cache/refs/heads/main/resetcricut.py)



### Run it the first time

Open Command Prompt again

*   Press Win + R, type "cmd", and hit Enter. A black window will appear.

    *   type "cd Desktop" and press enter
    *   type "pip install -r requirements.txt" and press enter (this will run for 30-60 seconds)
    *   type "python resetcricut.py" and press enter

If Cricut launches congratulations! You're finished! P.S. Don't delete these files

### Making it a bit simpler
*   Double click on "resetcricut.py" on your desktop
    * If it asks how you want to open it, select python and check the "always use this option" checkbox
      
### Runing it every time
From now on you can just double click the resetcricut.py icon on your desktop and it will launch Design Space


If you have issues, either create a new issue [here](https://github.com/michaeljcohen/cricut_cache/issues) or message me on reddit
