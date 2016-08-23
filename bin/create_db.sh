#!/usr/bin/env bash
DB_NAME=test_pgfulltext
DB_USER=test_pgfulltext
DB_PASSWORD=test_pgfulltext

#sudo apt-get install binutils libproj-dev gdal-bin libgdal1
#sudo apt-get install postgresql-9.4
#sudo apt-get install postgis
#sudo apt-get install postgresql-9.4-postgis-2.1

#sudo service postgresql restart

sudo -u postgres psql -c "CREATE USER ${DB_USER} WITH LOGIN CREATEDB PASSWORD '${DB_PASSWORD}';" || return 0
sudo -u postgres psql -c "CREATE DATABASE ${DB_NAME} WITH OWNER ${DB_USER};"

sudo -u postgres psql -c "ALTER  ROLE  ${DB_USER} WITH SUPERUSER;"

#sudo -u postgres psql ${DB_NAME} -c "CREATE EXTENSION unaccent;"
#sudo -u postgres psql ${DB_NAME} -c "CREATE EXTENSION postgis_topology;"