import psycopg2
from psycopg2.errors import UniqueViolation
from fastapi import FastAPI
from starlette import status
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="test",
    user="postgres",
    password="shabir123"
)
from psycopg2.extras import RealDictCursor
cursor = conn.cursor(cursor_factory=RealDictCursor)
app = FastAPI()

# endpoint with only path parameter
@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    cursor.execute("SELECT * FROM customer WHERE id = %s", (customer_id,))

    row = cursor.fetchall()

    return row


from pydantic import BaseModel
class Customer(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    zip: str



# end point with body
@app.post("/insert-customer", status_code=status.HTTP_201_CREATED)
def post_customer(customer: Customer):
    try:
        cursor.execute(
            """INSERT INTO customer
               (id, name, address, city, state, zip)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (
                customer.id,
                customer.name,
                customer.address,
                customer.city,
                customer.state,
                customer.zip
            )
        )
        conn.commit()
        return {"message": "Customer created"}

    except UniqueViolation:
        conn.rollback()
        return {"message": "Customer with this ID already exists"}


conn1 = psycopg2.connect(
    host="localhost",
    port=5432,
    database="world",
    user="postgres",
    password="shabir123"
)



#  endpoint wth only query parameters
cursor1 = conn1.cursor()
@app.get("/countries")
def get_countries(country_population: int, continent: str):
    cursor1.execute("SELECT name, population, continent FROM country WHERE population <= %s AND continent = %s",
                    (country_population, continent))
    return cursor1.fetchall()


conn2 = psycopg2.connect(
    host="localhost",
    port=5432,
    database="northwind",
    user="postgres",
    password="shabir123"
)
cursor2 = conn2.cursor()

from datetime import date
# endpoints with path parameter and query parameter
@app.get("/customer/{customer_id}")
def get_customer_order(customer_id: str, required_date: date):
    cursor2.execute("SELECT customer_id, ship_name FROM orders WHERE customer_id = %s AND required_date = %s",
                    (customer_id, required_date))
    return cursor2.fetchall()




