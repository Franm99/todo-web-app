"""
-> templates/base.html
Contains all the boilerplate code that will be inherited all along 
the webpage. This is a good technique to reuse code.
-----------------------

--------------------
DIRECTORY GUIDELINES
--------------------

admin.py
--------
- Register models into the Django Administration tool.
- Create superusers.
- Logging in and using the web application.

apps.py
-------
- Configure the attributes of the applications.
Users do not usually configure app attributes. Default config is normally enough to run the app.

models.py
---------
MOST IMPORTANT FILE WITHIN THE APP FILE STRUCTURE.
- Define models as classes.
Models define the structure of the database. They will set the design and relationship between data tables.

views.py
--------
Interface for the user to interact with the app.
- Define views as classes.

urls.py
-------
- Link views to urls that the user will be accessing to.

tests.py
--------
- Unit tests for the app.
- Complex functioning.

"""