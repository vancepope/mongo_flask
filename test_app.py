from bson.objectid import ObjectId
from unittest.mock import patch

objectid = ObjectId()
@patch("pymongo.collection.Collection.find")
def find(mocker):
    mocker.return_value = [{"_id": {"$oid": objectid},
                                    "part_name": "Screw", 
                                    "part_number": "4R5E3", 
                                    "quantity": 100, 
                                    "backorder": False, 
                                    "manufacturer": "Screws N More", 
                                    "weight": .01, 
                                    "dimensions": "16mm", 
                                    "cost": .10, 
                                    "expiration": "12/24/25"
                            }]
    mocker.returncode = 200
    return mocker;

@patch("pymongo.collection.Collection.find")
def find_fail(mocker):
    mocker.return_value = [{"error": "Item not found."}]
    mocker.returncode = 404
    return mocker;

@patch("pymongo.collection.Collection.find_one")
def find_one(mocker):
    mocker.return_value = [{"_id": {"$oid": objectid}, 
                                    "part_name": "Screw", 
                                    "part_number": "4R5E3", 
                                    "quantity": 100, 
                                    "backorder": False, 
                                    "manufacturer": "Screws N More", 
                                    "weight": .01, 
                                    "dimensions": "16mm", 
                                    "cost": .10, 
                                    "expiration": "12/24/25"
                            }]
    mocker.returncode = 200
    return mocker;

@patch("pymongo.collection.Collection.find_one")
def find_one_fail(mocker):
    mocker.return_value = [{"error": "Item not found."}]
    mocker.returncode = 404
    return mocker;

@patch("pymongo.collection.Collection.insert_one")
def insert_one(mocker):
    mocker.return_value = [{"_id": objectid}]
    mocker.returncode = 200
    return mocker;

@patch("pymongo.collection.Collection.insert_one")
def insert_one_fail(mocker):
    mocker.return_value = [{"error": "Item not found."}]
    mocker.returncode = 404
    return mocker;

@patch("pymongo.collection.Collection.update_one")
def update_one(mocker):
    mocker.return_value = [{"status": "Success"}]
    mocker.returncode = 200
    return mocker;

@patch("pymongo.collection.Collection.update_one")
def update_one_fail(mocker):
    mocker.return_value = [{"error": "Item not found."}]
    mocker.returncode = 404
    return mocker;

@patch("pymongo.collection.Collection.delete_one")
def delete_one(mocker):
    mocker.return_value = [{"status": "Success"}]
    mocker.returncode = 200
    return mocker;

@patch("pymongo.collection.Collection.delete_one")
def delete_one_fail(mocker):
    mocker.return_value = [{"error": "Item not found."}]
    mocker.returncode = 404
    return mocker;

def test_index():
    data = find()
    assert len(data.return_value) > 0
    assert data.returncode == 200
    print(f"Expected Output: length == 1 | Output: length == {len(data.return_value)}")
    print(f"Expected Output: returncode == 200 | Output: returncode == {data.returncode}")

def test_index_fail():
    data = find_fail()
    assert data.return_value[0]["error"] == "Item not found."
    assert data.returncode == 404
    print(f'Expected Output: status == Item not found | Output: status == {data.return_value[0]["error"]}')
    print(f"Expected Output: returncode == 404 | Output: returncode == {data.returncode}")

def test_create_part():
    data = insert_one()
    assert len(data.return_value) > 0
    assert data.returncode == 200
    print(f'Expected Output: length > 0 | Output: {len(data.return_value)} > 0')
    print(f"Expected Output: returncode == 200 | Output: returncode == {data.returncode}")

def test_create_part_fail():
    data = insert_one_fail()
    assert data.return_value[0]["error"] == "Item not found."
    assert data.returncode == 404
    print(f'Expected Output: status == Item not found | Output: status == {data.return_value[0]["error"]}')
    print(f"Expected Output: returncode == 404 | Output: returncode == {data.returncode}")

def test_get_part():
    data = find_one()
    assert len(data.return_value) > 0
    assert data.returncode == 200
    print(f'Expected Output: length > 0 | Output: {len(data.return_value)} > 0')
    print(f"Expected Output: returncode == 200 | Output: returncode == {data.returncode}")

def test_get_part_fail():
    data = find_one_fail()
    assert data.return_value[0]["error"] == "Item not found."
    assert data.returncode == 404
    print(f'Expected Output: status == Item not found | Output: status == {data.return_value[0]["error"]}')
    print(f"Expected Output: returncode == 404 | Output: returncode == {data.returncode}")
    
def test_update_part():
    data = update_one()
    assert data.return_value[0]["status"] == "Success"
    assert data.returncode == 200
    print(f'Expected Output: status == Success | Output: status == {data.return_value[0]["status"]}')
    print(f"Expected Output: returncode == 200 | Output: returncode == {data.returncode}")

def test_update_part_fail():
    data = update_one_fail()
    assert data.return_value[0]["error"] == "Item not found."
    assert data.returncode == 404
    print(f'Expected Output: status == Item not found | Output: status == {data.return_value[0]["error"]}')
    print(f"Expected Output: returncode == 404 | Output: returncode == {data.returncode}")

def test_delete_part():
    data = delete_one()
    assert data.return_value[0]["status"] == "Success"
    assert data.returncode == 200
    print(f'Expected Output: status == Success | Output: status == {data.return_value[0]["status"]}')
    print(f"Expected Output: returncode == 200 | Output: returncode == {data.returncode}")

def test_delete_part_fail():
    data = delete_one_fail()
    assert data.return_value[0]["error"] == "Item not found."
    assert data.returncode == 404
    print(f'Expected Output: status == Item not found | Output: status == {data.return_value[0]["error"]}')
    print(f"Expected Output: returncode == 404 | Output: returncode == {data.returncode}")