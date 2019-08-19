# Portfolio-Website-using-Django
This is website I developed while learning Django from https://realpython.com/get-started-with-django-1/. The idea is theirs. I just coded it. 

This is a simple portfolio website that I developed from the tutorial at the above mentioned link. 

You can download all the files and you can run them after some commands. 

First you will have to migrate to the test_project folder in your terminal.

After that run the following commands :

python manage.py makemigrations projects
python manage.py migrate projects
python manage.py makemigrations blog
python manage.py migrate 

and after doing all this, you can run :

python manage.py runserver

and then visit localhost:8000/blog/ in your browser, you should see the blog home page.

Thanks. 
