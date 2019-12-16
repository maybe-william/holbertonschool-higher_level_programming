#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from relationship_state import Base, State
from relationship_city import City

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

    my_state = State(name='California')
    my_city = City(name='San Francisco', state_id=my_state.id)
    my_state.cities.append(my_city)
    session.add(my_state)
    session.commit()
    session.close()
