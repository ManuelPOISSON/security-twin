# create the database model

from sqlalchemy import create_engine, inspect, Engine
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

# from playground import Base
from .model import Base
from .db_connect import connection_cred

engine_base_path = f"mysql+pymysql://{connection_cred['username']}:{connection_cred['password']}@{connection_cred['host']}:{connection_cred['port']}/"  # noqa E231


def reset_db(db_name: str, delete_only: bool = False) -> Engine:
    # Create an engine to connect to the MySQL server (without specifying a database)
    engine = create_engine(engine_base_path)
    inspect(engine)
    print(f"reseting db {db_name} in ", inspect(engine).get_schema_names())
    # delete database if it exists
    with engine.connect() as connection:
        connection.execute(text(f"DROP DATABASE IF EXISTS {db_name}"))
    if delete_only:
        return engine

    # Connect to the server and create the database if it does not exist
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))

    # Create an engine to connect to the MySQL database
    engine = create_engine(f"{engine_base_path}{db_name}")

    # Create all tables in the database
    Base.metadata.create_all(engine)

    return engine


def print_non_empty_tables(
    table_name_filter: str = None, engine: Engine | None = None
) -> None:
    if engine is None:
        # Create an engine to connect to the MySQL database
        engine = create_engine(f'{engine_base_path}{connection_cred["db_name"]}')
    print(f"{table_name_filter=}")
    # Create a session
    with Session(engine) as session:
        inspector = inspect(engine)
        print(inspector.get_schema_names())
        for table_name in inspector.get_table_names():
            if table_name_filter is not None and (
                table_name_filter.lower() not in table_name.lower()
            ):
                continue
            table = Base.metadata.tables[table_name]
            count = session.query(table).count()
            if count > 0:
                print(f"Table: {table_name}")
                for row in session.query(table).all():
                    print(row)
                print("\n")
    print("=" * 10)


def delete_database(bd_name: str) -> None:
    # Create an engine to connect to the MySQL server (without specifying a database)
    engine = create_engine(engine_base_path)
    with engine.connect() as connection:
        connection.execute(text(f"DROP DATABASE IF EXISTS {bd_name}"))


if __name__ == "__main__":
    import logging

    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # reset_db(connection_cred["db_name"])
    delete_database("todell")
    print("Successfully reset the database")
