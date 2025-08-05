# app/db.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get URI from environment
MONGO_URI = os.getenv("MONGODB_URI")

# Path to the Amazon DocumentDB CA certificate
CA_CERT_PATH = os.path.join(os.path.dirname(__file__), "..", "certs", "global-bundle.pem")

# Create MongoDB client with TLS
client = MongoClient(MONGO_URI, tls=True, tlsCAFile=CA_CERT_PATH)

# Choose database name (will be created if not exists)
db = client["myappdb"]
collection = db["items"]  # you may need to add this if it's missing
