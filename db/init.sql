CREATE USER backend WITH LOGIN PASSWORD 'backend';
CREATE DATABASE backend WITH OWNER backend;
ALTER ROLE backend createdb;
