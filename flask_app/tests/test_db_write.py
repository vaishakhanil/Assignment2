import unittest
from pymongo import MongoClient
from app import MONGO_USERNAME, MONGO_PASSWORD

# Test 3: Database Write Operation
# Unit test for a MongoDB write operation
class MongoDBWriteOperationTest(unittest.TestCase):
    
    def setUp(self):
        # Constructing the MongoDB URI, getting the MONGO_USERNAME AND PASSWORD FROM THE APP
        URI = "mongodb+srv://{}:{}@assignment2cluster.5lvu5.mongodb.net/?retryWrites=true&w=majority&ssl=true&appName=assignment2Cluster".format(MONGO_USERNAME, MONGO_PASSWORD)
        
        # Creating MongoClient, timeout in 5 seconds for testing
        self.client = MongoClient(URI, serverSelectionTimeoutMS=5000)

        # Setting DB and Collection
        self.db = self.client.shop_db
        self.collection = self.db.products
    
    def test_insert_document(self):

        # Creating a product to insert
        product = {
            "name": "House",
            "tag": "Test",
            "price": 999.99,
            "image_path": "images/house.jpg"
        }
        
        # Insert the product into the database
        result = self.collection.insert_one(product)
        
        # Verify the insertion
        # Query the database to check if the document is present
        inserted_product = self.collection.find_one({"_id": result.inserted_id})
        
        # Assertions to verify the document
        self.assertIsNotNone(inserted_product, "The document was not inserted.")
        self.assertEqual(inserted_product["name"], product["name"], "Product name does not match.")
        self.assertEqual(inserted_product["tag"], product["tag"], "Product tag does not match.")
        self.assertEqual(inserted_product["price"], product["price"], "Product price does not match.")
        self.assertEqual(inserted_product["image_path"], product["image_path"], "Product image path does not match.")
        
        # Cleanup: Remove the inserted document after the test
        self.collection.delete_one({"_id": result.inserted_id})

    # Clean up
    def tearDown(self):
        # Close the client connection
        self.client.close()

if __name__ == "__main__":
    unittest.main()
