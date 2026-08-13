import psycopg2
from fastapi import FastAPI
from starlette import status

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="test",
    user="postgres",
    password="shabir123"
)
cursor = conn.cursor()

get_app = FastAPI()
@get_app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    cursor.execute("SELECT * FROM customer WHERE id >= %s", (customer_id,))

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


post_app = FastAPI()
@post_app.post("/insert-customer", status_code=status.HTTP_201_CREATED)
def post_customer(customer: Customer):
    try:
        cursor.execute("INSERT INTO customer (id, name, address, city, state, zip) VALUES"
                       "(%s, %s, %s, %s, %s, %s)",
                       (
                           customer.id,
                           customer.name,
                           customer.address,
                           customer.city,
                           customer.state,
                           customer.zip
                       ))
        conn.commit()
        return {"message": "Customer created"}
    except Exception:
        conn.rollback()
        raise

conn1 = psycopg2.connect(
    host="localhost",
    port=5432,
    database="northwind",
    user="postgres",
    password="shabir123"
)
cursor1 = conn.cursor()

app_countries = FastAPI()


@app_countries.get("/countries")
def get_countries(country_population: int, continent: str):
    cursor1.execute("SELECT name, population, continent FROM country WHERE population <= %s AND continent = %s",
                    (country_population, continent))
    return cursor1.fetchall()


from datetime import date

app_order = FastAPI()


@app_order.get("/customer/{customer_id}")
def get_customer_order(customer_id: str, required_date: date):
    cursor1.execute("SELECT customer_id, ship_name FROM orders WHERE customer_id = %s AND required_date = %s",
                    (customer_id, required_date))
    return cursor1.fetchall()
