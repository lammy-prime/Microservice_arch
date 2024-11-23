import jwt, datetime, os
from dotenv import load_dotenv
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

# config
load_dotenv() 
server.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
server.config["MYSQL_USER"] = os.getenv("MYSQL_HOST")
server.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_HOST")
server.config["MYSQL_DB"] = os.getenv("MYSQL_HOST")
server.config["MYSQL_PORT"] = os.getenv("MYSQL_HOST")


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing details", 401
    
    #Check db for username and password