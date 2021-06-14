# How To Use The IPAddressing Web Application

This is a README file explaining how to use this application.

# Installation
* To use this project or open it you will need to have Python installed on your computer. Ideally, get [Python 3.9.2](https://www.python.org/downloads/release/python-392/) because that's the version that I used.

1. Click the green "Code" button
2. Either Click Download Zip or follow the cloning instructions
3. If you clicked Download Zip:
    * Extract files from zip
4. If you cloned the repository:
    * Open up the repository in a code editor
5. Head to the settings.py file and change the database settings
    * Find the follow section of the file:
    ```
    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'andrewhall',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'USER': 'root',
            'PASSWORD': 'SatoTatsuhiro891',
        }
    }
    ```
6. Change the USER and PASSWORD to the password that you have set for your MYSQL workbench.

* You need to activate the virtual environment to use the program. Follow these short steps:

    - Open up the command line.
    - Head to where the folder "venv" is.
    - On Windows: type "cd venv/Scripts"
    - Type activate.bat. 
    - If the virtual environement is active you will see (venv) in the command line.

7. Open up the command line (Command Prompt on Windows, Terminal on Mac or Command line on Linux) and cd into the project directory where manage.py is.

8. Type `python manage.py makemigrations` and press Enter.

9. Type `python manage.py migrate` and press Enter.

10. Type `python manage.py runserver`.

11. Open up a web browser then type localhost:8000 in the search bar.

12. The project should be up and running.

# How To Use

1. Open up a command line (Command Prompt on Windows, Terminal on Mac or Command line on Linux).

* You need to activate the virtual environment to use the program. Follow these short steps:

    - Open up the command line.
    - Head to where the folder "venv" is.
    - On Windows: type "cd venv/Scripts"
    - Type activate.bat. 
    - If the virtual environement is active you will see (venv) in the command line.

2. Cd into the project directory where the manage.py file is located.

3. Type `python manage.py runserver` and press Enter.

4. Open up a browser and enter localhost:8000 into the search bar.

* You should see a page with yellow boxes. (This is the input page.)

* The menu allows you to view the other pages. Click on the "Generate Data" link to view the generate page
and click on the "View Tables" link to view the database tables.


# How To Create An Administrator

* The admin section allows you to view each table. You will need to create an admin account to use the admin panel.

1. Open up a command line (Command Prompt on Windows, Terminal on Mac or Command line on Linux).

* You need to activate the virtual environment to use the program. Follow these short steps:

    - Open up the command line.
    - Head to where the folder "venv" is.
    - On Windows: type "cd venv/Scripts"
    - Type activate.bat. 
    - If the virtual environement is active you will see (venv) in the command line.

2. Cd into the project directory where the manage.py file is located.

3. Type `python manage.py createsuperuser` and press Enter.

4. Enter a username and password (email isn't necessary). 

* The password doesn't show when you type it, this is fine. It's a security measure.

5. Open up a browser and enter localhost:8000/admin into the search bar.

6. Use the username and password you created to login to your admin account.

7. Click on each table to view the data.

# How To Delete All Table Rows For A Specific Table

1. Open up the command line.

* You need to activate the virtual environment to use the program. Follow these short steps:

    - Open up the command line.
    - Head to where the folder "venv" is.
    - On Windows: type "cd venv/Scripts"
    - Type activate.bat. 
    - If the virtual environement is active you will see (venv) in the command line.
    - On Mac or Linux type "source venv/bin/activate"


2. Cd into the project directory where the manage.py file is located.

3. Type `python manage.py runserver`.

4. Open up a browser and enter localhost:8000/admin into the search bar.

5. Login to the Admin panel using the username and password you created in # How To Create An Administrator.

6. Once you're logged in, you should see two sections "Authentication and Authorization" and "IPLOOKUP".

7. IPLOOKUP is where the tables are.

8. Click on the table corresponding to the name of the table you want to clear. 

9. Click to select all rows. (An option should appear that will allow you to select all rows.)

10. Click the dropdown and select the only option.

11. Click "Go".


# How To Delete Everything In The Database

* PLEASE NOTE: Once the data is deleted you may not be able to use the Generate Data and View Tables. This is because all the tables are empty. This is not an issue. You can add default values in the admin panel or in the MYSQL Workbench.

1. Open up the command line.

* You need to activate the virtual environment to use the program. Follow these short steps:

    - Open up the command line.
    - Head to where the folder "venv" is.
    - On Windows: type "cd venv/Scripts"
    - Type activate.bat. 
    - If the virtual environement is active you will see (venv) in the command line.
    - On Mac or Linux type "source venv/bin/activate"

2. Cd into the project directory where the manage.py file is located.

3. Type `python manage.py flush`.

4. Follow the instructions.

# Testing

* Each page adds data to the corresponding tables as outline in the django-template.docx file. But, you may want to change some things. 

* Fill in each section and test out whether the print statements are being generated.

* When you enter data into the input page it is automatically saved to its respective table. You can open up the MYSQL workbench to view the data, open up the tables in the admin section or head to the View tables page in the app.

* If the server is running whilst you are trying to generate print statements, you will need to turn it off. Press CTRL+C to turn it off. You will then see the print statements in the command line.

