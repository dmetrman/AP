from CarRentalSchema import (
    Session,
    car,
    user,
    order,
    status)

session = Session()


customStatus = status(status_id=1, name="pending")
session.add(customStatus)
session.commit()

print(session.query(status).all())
session.close()
print("Great")