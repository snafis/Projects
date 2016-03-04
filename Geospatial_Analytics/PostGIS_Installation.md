

# How to install PostGIS on Mac OS X

[**PostGIS** ][1]is a powerful extension to the [PostgreSQL database][2] that adds support for geometry types and [geospatial functions][3] such as point, line, polygon, distance, area, union, intersection, etc.

PostGIS can handle large amounts of data. It is at[ the core of CartoDB][4] and plays nicely with [QGIS][5],[ Tilemill / Mapbox Studio][6] and [GDAL][7].

In this tutorial, we will see how to install PostGIS on Mac OS X. We'll use [Homebrew ][8]to install the required packages, so make sure you have[ ][8][Homebrew installed][8] on your system.

 

To install PostgreSQL open the terminal and run the following command:

     brew install postgres

You should see something like this:

![homebrew-install-postgresql][9]

By default the postgresql server will be installed under: **/usr/local/var/postgres**

 

Back in the terminal run:

    brew install postgis

Once again, homebrew will inform us about the progress:

![homebrew-install-postgis][10]

 

 

To **Start the server**, we will use the [command line utility **pg_ctl**][11]. In the terminal, run:

    pg_ctl -D /usr/local/var/postgres start

 

Let's **check if postgres is running**:

    export PGDATA='/usr/local/var/postgres'

    pg_ctl status

You should see something similar to:

![postgresql-running][12]

 

If that's a fresh installation, we need to[ initialize the database cluster][13]:

    initdb /usr/local/var/postgres

![postgresql-initdb][14]

Now we can **create a new database.** Let's call it **postgis_test**

    createdb postgis_test

 

We'll use the[** psql** command line][15] utility to connect to the database that we've just created:

    psql postgis_test

If everything goes well, we should see the psql command prompt:

![psql-prompt][16]

 

 

To **enable PostGIS**, execute the following command:

    CREATE EXTENSION postgis;

If everything is OK, we should see:

![psql-postgis-extension][17]

 

Let's** check if we have [PostGIS support][18]**:

    SELECT PostGIS_Version();

 

 

To **quit psql, **type the following command:

    q

 

By now, you should have a working postgresql server with PostGIS support enabled. Here are a few more commands that you can find useful:

 

**Stop postgresql:**

    pg_ctl -D /usr/local/var/postgres stop -s -m fast

 

**Start postgresql **and** use a log file**

     pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

 

**Check if postgres is installed:**

    brew info postgres

 

To **drop the database** run:

    dropdb postgis_test

 

**Delete the PostgreSQL cluster:**

    rm -rf /usr/local/var/postgres/

 

From within psql, we can use the following command to** list all tables in our database**:

    dt

[1]: http://postgis.net/
[2]: http://www.postgresql.org/
[3]: http://postgis.net/docs/PostGIS_Special_Functions_Index.html
[4]: http://docs.cartodb.com/cartodb-platform/sql-api.html
[5]: http://www.gistutor.com/quantum-gis/20-intermediate-quantum-gis-tutorials/34-working-with-your-postgis-layers-using-quantum-gis-qgis.html
[6]: https://www.mapbox.com/tilemill/docs/guides/postgis-work/
[7]: http://www.gdal.org/drv_pg.html
[8]: http://brew.sh/
[9]: http://morphocode.com/wp-content/uploads/2014/11/homebrew-install-postgresql.png
[10]: http://morphocode.com/wp-content/uploads/2014/11/homebrew-install-postgis.png
[11]: http://www.postgresql.org/docs/9.3/static/app-pg-ctl.html
[12]: http://morphocode.com/wp-content/uploads/2014/11/postgresql-running.png
[13]: http://www.postgresql.org/docs/9.3/static/app-initdb.html
[14]: http://morphocode.com/wp-content/uploads/2014/11/postgresql-initdb.png
[15]: http://www.postgresql.org/docs/9.2/static/app-psql.html
[16]: http://morphocode.com/wp-content/uploads/2014/11/psql-prompt1.png
[17]: http://morphocode.com/wp-content/uploads/2014/11/psql-postgis-extension.png
[18]: http://postgis.net/docs/PostGIS_Version.html
  
