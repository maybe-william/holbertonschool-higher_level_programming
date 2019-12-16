#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    x = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3])
    engine = create_engine(x, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    q = session.query(City).order_by(City.id)
    for row in q.all():
        q2 = session.query(State).filter(State.id == row.state_id)
        row2 = q2.first()
        if row2:
            print(str(row2.name) + ": (" + str(row.id) + ") " + str(row.name))
