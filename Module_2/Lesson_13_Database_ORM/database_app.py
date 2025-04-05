# database_app.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the base class for declarative class definitions
Base = declarative_base()

class User(Base):
    """
    Model representing a user in the database.
    """
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

def main():
    """
    Main function to demonstrate connecting to a SQLite database,
    creating tables, adding a new User, and querying the data.
    """
    # Create a SQLite engine (the database file will be named 'users.db')
    engine = create_engine('sqlite:///users.db', echo=True)
    
    # Create all tables defined by models (if they do not already exist)
    Base.metadata.create_all(engine)
    
    # Configure a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Insert a new user
        new_user = User(name="Alice", email="alice@example.com")
        session.add(new_user)
        session.commit()
        print("New user added successfully.")
        
        # Query the database for all users
        users = session.query(User).all()
        print("Users in the database:")
        for user in users:
            print(user)
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()
