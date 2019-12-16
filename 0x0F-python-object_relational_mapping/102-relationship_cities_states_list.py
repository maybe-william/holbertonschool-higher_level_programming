#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from relationship_city import Base, City, State

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
    for r in q.all():
        print(str(r.id) + ": " + str(r.name) + " -> " + str(r.state.name))
