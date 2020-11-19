# Exam Results App

Web Application to serve results of a exam provided the roll number of the student.

This app is built to demonstrate that such applications can be run even on a $5 digital ocean droplet and can serve fairly large amount of requests.

# USAGE

Create python virtualenv.

```
$ cd python
$ python3 -m venv venv
$ source venv/bin/activate
```

Install Python dependencies.

```
$ pip install -r python/requirements.txt
```

Generate sample data.

```
$ python gendata.py
```

Start gunicorn server:

```
$ gunicorn -b :8080 wsgi:app
```

