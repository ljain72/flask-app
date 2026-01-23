# flask-app
This is a simple flask app that connects to DB and add users to it. We can view users on /users and /time updates the counter in db stating how many times the /times link is accessed.
To run locally, we need 
1. a python virtual environment setup: 'python -m venv venv' -> activate environment 'source /venv/Scripts/activate'.
2. Install dependencies using 'pip install --no-cache-dir -r requirements.txt'
3. If using miniqube, bring up a DB server with image postgre:15.
4. Export the db credentials in the cli.
5. Run 'python app.py'
6. The server is running on localhost and /users and /time can be accessed.
