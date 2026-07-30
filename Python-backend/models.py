from database import engine
from sqlalchemy import text


def get_all_employee():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT * FROM employee")
        )

        employee = []

        for row in result:
            employee.append(dict(row._mapping))

        return employee