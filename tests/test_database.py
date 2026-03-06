from src.database.db_manager import initialize_database


def test_database_init():
    initialize_database()
    assert True