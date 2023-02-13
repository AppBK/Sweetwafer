#!/bin/bash



# Delete the current database
psql -c "DROP DATABASE dev"

# Delete the Migrations folder for old database
rm -r ./migrations

# Create a new database
psql -c "CREATE DATABASE dev"

# Create new Migrations folder for
flask db init

# Overwrite the default env.py
cat ../env.py.example >| ../migrations/env.py

# Create new migrations file in ./migrations/versions
flask db migrate -m 'create all'

# Apply the new migration to the new database
flask db upgrade

# Seed the new database
flask seed all
