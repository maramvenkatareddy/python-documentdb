# Application is running on EC2 and Amazon DocumentDB is hosted as a managed service in aws
# To check the network connection between ec2 and db using telnet command whcih i mentioned below,
telnet documentdbendpoint portnumber

Pre-requisites:
==============
1. Install the python, pip and venv if not already installed using below commands
     1. sudo apt update
     2. sudo apt install python3.12 -y
     3. sudo apt install python3.12-pip -y
     4. sudo apt install python3.12-venv -y
2. Install the bundle pem file on to the server and move to the certs folder
3. Change the endpoint of documentdb in .env file
4. Switch to the folder using the below command
     cd python-documentdb

# Install the dependencies for application
pip install -r requirements.txt

# Run the application using below command
uvicorn app.main:app --host 0.0.0.0 --port 8080

# CRUD operations on Db
Post:
====
curl -X POST http://localhost:8080/items -H "Content-Type: application/json" -d '{"CloudTechnology": "AWS", "description": "Amazon Web Services", "MarketValue": 40}'
  
GET:
====
curl -X GET http://localhost:8080/items/

PUT:
====
curl -X PUT http://localhost:8080/items/<item Id >

Delete:
=======
curl -X DELETE http://localhost:8080/items/<item Id >
