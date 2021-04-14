To run the project

1. Clone it
2. install python 
3. install virtualenv : pip install virtualenv
4 . create virtualenv : virtualenv venv ( venv is name)
5. activate venv (check on net for windows)
6. install packages in venv : pip install -r requirements.txt (after opening project folder)
7. type python manage.py makemigrations
8. type python manage.py migrate
9. type python manage.py createsuperuser (and fill the details)
10. python manage.py runserver

admin site:  http://127.0.0.1:8000/admin/

username : admin

password : #Root123

signup page http://127.0.0.1:8000/register/