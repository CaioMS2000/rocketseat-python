from sqlalchemy import Engine
from .connection import db_connection_handler

def test_connection():
    assert db_connection_handler.get_engine() is None
    
    db_connection_handler.coonnect()

    engine = db_connection_handler.get_engine()
    
    assert engine is not None
    assert isinstance(engine, Engine)