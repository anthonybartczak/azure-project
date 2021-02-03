## Requirements:

* Microsoft Azure account with an active subscription
* Python 3,6+
* Azure CLI

## How to deploy the app using Azure App Service and Postgre SQL

1. Log in via Azure CLI:\
`az login`

2. Clone the repository:\
`git clone https://github.com/anthonybartczak/azure-project`

3. Open your terminal in the designated folder and run:\
`py integration.py`

4. When prompted, enter the requested details

5. Wait for the job to finish - you should receive the generated JSON response

6. Connect to your app's SSH:\
```https://<app-name>.scm.azurewebsites.net/webssh/host```

7. Run the following commands:
```python
# Change to the app folder
cd  $APP_PATH

# Activate the venv
source /antenv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create the super user (follow prompts)
python manage.py createsuperuser
```

8. Log in the admin section of your app:\
`https://<app-name>.azurewebsites.net/admin`

9. You can now create blog posts using the `Add post` button placed inside the side menu.