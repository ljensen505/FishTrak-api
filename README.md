# To seed database
<ul>
<li>ensure mariadb is installed</li> 
<li>ensure a Database named <code>fishtrak</code> exists</li> 
<li>ensure you have a user and password for mysql on localhost, and that your user has full privileges on the fishtrak database</li> 
<li>run: <code>mysql -u [username] -p -h localhost fishtrak < path/to/DDL.sql</code></li>
</ul>

# To run application locally
This must be run with python3.11 or later, with which you can create a virtual environment and install from requirements.txt as you see fit

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