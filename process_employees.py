
import mysql.connector
from getpass import getpass


def fetch_employees(batch_size=1000):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter MySQL root password: "),
        database="employees"
    )

    cursor = connection.cursor(buffered=False)

    try:
        cursor.execute(
            "SELECT emp_no, first_name, last_name FROM employees"
        )

        while True:
            batch = cursor.fetchmany(batch_size)

            if not batch:
                break

            for employee in batch:
                yield employee

    finally:
        cursor.close()
        connection.close()


def main():
    count = 0

    for employee in fetch_employees():
        if count < 10:
            print(employee)

        count += 1

    print(f"Total employees processed: {count}")


if __name__ == "__main__":
    main()
