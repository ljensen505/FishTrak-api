# To seed database
<ul>
<li>ensure mysql is installed and running (both mysql and mariad are known to work)</li> 
<li>ensure a Database named <code>fishtrak</code> exists</li> 
<li>ensure you have a user and password for mysql on localhost, and that your user has full privileges on the fishtrak database</li> 
<li>run: <code>mysql -u [username] -p fishtrak < sql/DDL.sql</code></li>
</ul>

# To run application locally
This must be run with python3.11 or later, with which you can create a virtual environment and install from requirements.txt as you see fit. Be sure to look at the <code>example.env</code> file and create a <code>.env</code> file in the same directory with correct values.

from the main project directory:
```bash
uvicorn app.main:app --reload
```

# Testing
```bash
pytest
``` 
or, to run with output: 
```bash
pytest -rP
```
