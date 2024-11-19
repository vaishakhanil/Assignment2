import unittest
from pymongo import MongoClient
from app import MONGO_USERNAME, MONGO_PASSWORD

# Test 2: Database Read Operation - 
# Write a unit test to check the correct connection of a MongoDB read operation.
class MongoDBConnectionTest(unittest.TestCase):
    
    def test_mongo_connection(self):
        # Constructing the MongoDB URI, getting the MONGO_USERNAME AND PASSWORD FROM THE APP
        URI = "mongodb+srv://{}:{}@assignment2cluster.5lvu5.mongodb.net/?retryWrites=true&w=majority&appName=assignment2Cluster".format(MONGO_USERNAME, MONGO_PASSWORD)
        
        # Creating MongoClient, timeout in 5 seconds for testing
        client = MongoClient(URI, serverSelectionTimeoutMS=5000)
        
        try:
            # Try to ping the database to verify the connection
            client.admin.command('ping')

            # If no exception is raised, connection is successful
            self.assertTrue(True)

        except Exception as e:
            # If Error is thrown Fail with Error
            self.fail(f"MongoDB connection failed: {e}")

        finally:
            
            # Ensure MongoClient is closed to avoid resource warnings
            client.close()

if __name__ == "__main__":
    unittest.main()
