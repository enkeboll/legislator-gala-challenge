from abstractus import assign_guests_to_tables

def test_assign_guests_to_tables():
    # Test case 1
    num_tables = 2
    guest_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
    planner_preferences = [
        {"preference": "avoid", "guests": ["Bob", "Charlie"]},
        {"preference": "pair", "guests": ["David", "Eve"]},
    ]
    # assert bob and charlie not together
    assert all(['Charlie' not in table for table in assign_guests_to_tables(num_tables, guest_list, planner_preferences).values() if 'Bob' in table])
    # assert David and Eve are together
    assert all(['Eve' in table for table in assign_guests_to_tables(num_tables, guest_list, planner_preferences).values() if 'David' in table])

    # Test case 2
    num_tables = 3
    guest_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Gina", "Harry"]
    planner_preferences = [
        {"preference": "avoid", "guests": ["Bob", "Charlie"]},
        {"preference": "pair", "guests": ["David", "Eve"]},
        {"preference": "pair", "guests": ["Gina", "Harry"]},
    ]
    # assert bob and charlie not together
    assert all(['Charlie' not in table for table in assign_guests_to_tables(num_tables, guest_list, planner_preferences).values() if 'Bob' in table])
    # assert David and Eve are together
    assert all(['Eve' in table for table in assign_guests_to_tables(num_tables, guest_list, planner_preferences).values() if 'David' in table])
    # assert Gina and Harry are together
    assert all(['Harry' in table for table in assign_guests_to_tables(num_tables, guest_list, planner_preferences).values() if 'Gina' in table])

test_assign_guests_to_tables()