from db import SessionLocal
from models import User
from db import engine, Base
from models import User

Base.metadata.create_all(bind=engine)

# Create a database session
db = SessionLocal()

# Create (Insert)
new_user = User(name="Pramod", email="pramod@example.com")
db.add(new_user)
db.commit()
db.refresh(new_user)  # Refresh to get updated fields (like id)
print("Inserted:", new_user.id, new_user.name)


# Read (Select)
users = db.query(User).all()
for user in users:
    print(user.name, user.email)

# Update
user = db.query(User).filter(User.name == "Pramod").first()
user.email = "naikpramod@example.com"
db.commit()

# Delete
# db.delete(user)
# db.commit()

# Close the session
db.close()
