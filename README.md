# To seed database
<ul>
<li>ensure mariadb is installed</li> 
<li>ensure a Database named <code>fishtrak</code> exists</li> 
<li>ensure you have a user and password for mysql on localhost, and that your user has full privileges on the fishtrak database</li> 
<li>run: <code>mysql -u [username] -p -h localhost fishtrak < path/to/DDL.sql</code></li>
</ul>

# To run application locally
from the main project directory:
```bash
uvicorn app.main:app --reload
```

# Testing 
let's use pytest and write test alongside each file being tested. See main.py for an example