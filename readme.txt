# Django Online Admission Management System

To run the project:
1. Create a virual environment and activate it.
2. Run cmd "pip install requirements.txt".
3. Go to directory where manage.py is located.
4. Now run "python manage.py runserver".
5. Finally, To open website go to http://127.0.0.1:8000/






Some useful cmds for deployment

git remote -v
git add .
git commit -m "message"
heroku login
git push heroku master
heroku run python3 manage.py migrate
heroku run python3 manage.py collectstatic
