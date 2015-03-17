Q&A
===

A minimalist Flask app for polling the audience. 

Testing
-------

Use Flask's server.::

    $ virtualenv v
    $ source v/bin/activate
    $ pip install -r requirements.txt
    $ python hello.py

Deployment
----------

Do not use Flask's built-in server in production. 

Make a secret key that only ``hello.wsgi`` and ``hello.py`` know, such as a
chunk of ``pwgen`` output. Use that secret key to replace both instances of
``'TODO FIXME PUT A SECRET KEY HERE'``.  

If your app is deployed to a directory other than ``/var/www/poll/``, change
the path in ``hello.wsgi`` accordingly. 

If you're using Apache, you'll have a pretty standard configuration file for
the poll. It would be in
``/etc/apache2/sites/available/poll.yourdomain.tld.conf`` if you're using
Ubuntu. It might look something like this:::

    <VirtualHost *:80>
        ServerName poll.yourdomain.tld
        ServerAdmin admin@yourdomain.tld
        WSGIScriptAlias / /var/www/poll/hello.wsgi
        <Directory /var/www/poll/>
                Order allow,deny
                Allow from all
        </Directory>
        Alias /static /var/www/poll/static
        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>

Then ``a2ensite`` the config file to activate it, and ``service apache2 reload`` to reload apache and make the changes take effect. 

