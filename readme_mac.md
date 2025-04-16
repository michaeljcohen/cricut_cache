✅ Step 1: Install Homebrew (if not already installed)
* Open Terminal, then paste:
  * /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

✅ Step 2: Install Python via Homebrew
* brew install python

✅ Step 3: Confirm Installation
* python3 --version
* pip3 --version

✅ Step 4: Set Up python Alias (Optional, but Nice)
* To use python instead of python3, add this to your shell config (e.g., ~/.zshrc or ~/.bash_profile):
  * alias python=python3
  * alias pip=pip3

  * source ~/.zshrc  # or source ~/.bash_profile

✅ Step 5: Install psutil (used in your script)
* pip install psutil
