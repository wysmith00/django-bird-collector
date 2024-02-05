CREATE DATABASE birdcollector;

CREATE USER bird_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE birdcollector TO bird_admin;
