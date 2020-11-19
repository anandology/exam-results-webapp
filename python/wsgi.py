"""
API to serve the exam results.

USAGE:

    gunicorn wgi:app
"""
import pandas as pd
import numpy as np
import os
import json

filename = os.getenv("DATA_PATH", "data.csv")
df = pd.read_csv(filename, index_col="roll_number")

STATUS_200 = "200 OK"
STATUS_422 = "422 Unprocessable Entity"

def query(roll_no):
    row = get_row(roll_no)
    if not row:
        return STATUS_422, {"error": "Invalid Roll Number"}
    return STATUS_200, dict(row)

def get_row(roll_no):
    if not roll_no:
        return

    try:
        roll_no = int(roll_no)
    except ValueError:
        return None

    try:
        row = df.loc[roll_no]
        return {k: convert(v) for k, v in row.items()}
    except KeyError:
        return None

def convert(x):
    if isinstance(x, np.number):
        return int(x)
    else:
        return x

def parse_query(environ):
    qs = environ.get("QUERY_STRING", "")
    pairs = [kv.split("=", 1) for kv in qs.split("&") if "=" in kv]
    return {k: v for k, v in pairs}

status = {
    200: "200 OK"
}

def app(environ, start_response):
    """WSGI application to server the API.
    """
    q = parse_query(environ)
    roll_no = q.get("roll_no")
    status, response = query(roll_no)
    start_response(status, [('Content-Type', 'application/json')])
    response_bytes = json.dumps(response).encode('utf-8')
    return [response_bytes]
