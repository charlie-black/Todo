# Todo
Create a folder named Todo
In your command prompt or terminal navigate to the directory of the project you just created.(cd Todo)
Create virtual environment using the following command (py -m virtualenv env)
Activate the virtual environment using this command(env\Scripts\activate)
Then install the packages 
 - pip install django
 - pip install djangorestframework
Create a django project using this command(django-admin startproject api ) where api is the name of the project
Navigate into the the project you have just created(cd api)
Create an app inside the directory(python manage.py startapp todo)
Navigate to the settings.py and add our todo app and rest_framework in the installed apps
then create a super user using this command (python manage.py createsuperuser) insert your name, then email and password dont forget this password as it is going to be needed during login
Then run (python manage.py makemigrations) and then run(python manage.py migrate) to migrate the db
Now navigate to our todo app and create a model(data structure of todo)
   -create a class Todo which will have 3 fields, title, description bool completed

Now that we have our models we need to create a serializer this will take our model data and convert it into json
create a new file serializers.py in our todo app and create the serializer as below

lets go into our views.py now and create our view sets we are going to create only one view that will handle everything for us. Create as shown below
create a file urls.py in the todo app and implement as below

under api directory select urls.py and add the following lines as below
Navigate to the admin.py and register the app as follows

in the settings.py create your postgres database credentials after you have created the database in postgres

Save and start server with the following command(python manage.py runserver)



