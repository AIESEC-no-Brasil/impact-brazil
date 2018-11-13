# Impact Brazil

## Configuration
1. Create `backend/config.py`
```python
db_host = DB_HOST  # Optional
dbname = DB_NAME
dbuser = DB_USER
dbpass = DB_PASSWORD
prod = False  # True on Prod 
entity_gis_id = 1606  # ID of Brazil on GIS
secret_key = SECRET_KEY  # Set a secret key for Django here
```

2. In `frontend/src/config.js`, change config.api to the URL of the Django server

## Backend Setup
1. Upload `backend/` to your instance
2. Run `pip install -r requirements.txt`
3. Set up `crontab` to refresh the opportunities database periodically list, example below
```bash
0 */2 * * * /home/ec2-user/impact/backend/venv/bin/python3 /home/ec2-user/impact/backend/manage.py acquire_opps
```

## Frontend setup
1. Run `npm install` in `frontend/`
2. Run `npm run build` in `frontend/`
3. Upload `frontend/dist/*` to your htdocs directory

## Serving
1. Install mod_wsgi for apache
2. Load mod_wsgi in httpd.conf
3. Configure Apache to serve Django server, example below
```apache
<VirtualHost _default_:80>
        Alias /static/admin /home/ec2-user/impact/backend/venv/lib/python3.6/site-packages/django/contrib/admin/static/admin
        <Directory /home/ec2-user/impact/backend/venv/lib/python3.6/site-packages/django/contrib/admin/static/admin>
                Require all granted

        <Directory /home/ec2-user/impact/backend/backend>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIDaemonProcess backend python-home=/home/ec2-user/impact/backend/venv python-path=/home/ec2-user/impact/backend
        WSGIProcessGroup backend
        WSGIScriptAlias /api /home/ec2-user/impact/backend/backend/wsgi.py

</VirtualHost>
```
4. In `htdocs/`, create `.htaccess` to ensure HistoryMode is being handled in Vue
```apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteBase /
  RewriteRule ^index\.html$ - [L]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule . /index.html [L]
</IfModule>
```
5. Restart httpd
