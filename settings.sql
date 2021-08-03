DROP DATABASE IF EXISTS coffeeholic;
CREATE DATABASE coffeeholic;
CREATE USER coffeeholicuser WITH PASSWORD 'coffeeholic';
GRANT ALL PRIVILEGES ON DATABASE coffeeholic TO coffeeholicuser;