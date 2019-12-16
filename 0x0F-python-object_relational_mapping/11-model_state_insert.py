#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State

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

    my_state = State(name='Louisiana')
    session.add(my_state)
    session.commit()
    q = session.query(State).order_by(State.id)
    q = q.filter(State.name == "Louisiana")
    row = q.first()
    if row:
        print(str(row.id))

    session.close()
