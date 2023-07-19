## Installation method 1 (Run application locally)

1. Clone this Repo

   `git clone (https://github.com/sophatahsher/inheritace-logistic-system-fastapi)`
2. Cd into the Fast-Api folder

   `cd inheritace-logistic-system-fastapi`
3. Create a virtual environment

   `python3 -m venv venv`
4. Activate virtualenv

   `source venv/bin/activate`

   For zsh users

   `source venv/bin/activate.zsh`

   For bash users

   `source venv/bin/activate.bash`

   For fish users

   `source venv/bin/activate.fish`

5. Install the required packages

   `python -m pip install -r requirements.txt`
6. Start the app

   ```shell
   python main.py
   ```

   7b. Start the app using Uvicorn

   ```shell
   uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8002