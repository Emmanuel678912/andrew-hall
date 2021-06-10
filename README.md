# How To Use The IPAddressing Web Application

This is a README file explaining how to use this application.

# Installation
* To use this project or open it you will need to have [Python] (https://www.python.org/downloads/release/python-392/) installed on your computer. Ideally, get Python 3.9.2 because that's the version that I used.

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

7. Open up the command line (Command Prompt on Windows, Terminal on Mac or Command line on Linux) and cd into the project directory where manage.py is.

8. Type `python manage.py makemigrations` and press Enter.

9. Type `python manage.py migrate` and press Enter.

10. Type python manage.py runserver.

11. Open up a web browser then type localhost:8000 in the search bar.

12. The project should be up and running.

# How To Use

1. Open up a command line (Command Prompt on Windows, Terminal on Mac or Command line on Linux).

2. Cd into the project directory where the manage.py file is located.

3. Type `python manage.py runserver` and press Enter.

4. Open up a browser and type localhost:8000 into the search bar.

* You should see a page with yellow boxes. (This is the input page.)

* The menu allows you to view the other pages. Click on the "Generate Data" link to view the generate page
and click on the "View Tables" link to view the database tables.


# How To Create An Administrator

* The admin section allows you to view each table. You will need to create an admin account to use the admin panel.

1. Open up a command line (Command Prompt on Windows, Terminal on Mac or Command line on Linux).

2. Cd into the project directory where the manage.py file is located.

3. Type `python manage.py createsuperuser` and press Enter.

4. Enter a username and password (email isn't necessary). 

* The password doesn't show when you type it, this is fine. It's a security measure.

5. Open up a browser and type localhost:8000/admin into the search bar.

6. Use the username and password you created to login to your admin account.

7. Click on each table to view the data.

# Testing

* Each page adds data to the corresponding tables as outline in the django-template.docx file. But, you may want to change some things. 

* Fill in each section and test out whether the print statements are being generated.

* When you enter data into the input page it is automatically saved to its respective table. You can open up the MYSQL workbench to view the data, open up the tables in the admin section or head to the View tables page in the app.

* If the server is running whilst you are trying to generate print statements, you will need to turn it off. Press CTRL+C to turn it off. You will then see the print statements in the command line.
