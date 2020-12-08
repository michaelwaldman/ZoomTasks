How to run: <br />
Step 1.
`pip3 install requirements.txt` <br />
or <br />
`pip install -r requirements.txt` <br />

Step 2.
For /TaskApp/settings.py, change EMAIL_HOST_USER and EMAIL_HOST_PASSWORD to your own outlook email/password. You can also change EMAIL_HOST if you use other STMP servers.

Step 3.
`python3 manage.py migrate` <br />
or <br />
`python manage.py migrate` <br />

`python3 manage.py runserver` <br />
or <br />
`python manage.py runserver` <br />
