from models.model import Country, SessionLocal
import streamlit as st

# st.title("Database operation")

class DatabaseOperator:
    def __init__(self, table) -> None:
        self.table = table

    def __str__(self) -> str:
        return f"Database operation on ({self.table})"

    def add_record(self, *args, **kwargs):
        name = kwargs.get("name")
        code = kwargs.get("code")
        with SessionLocal() as session:
            new_record = self.table(name=name, code=code)
            session.add(new_record)
            session.commit()

        st.success("Record added!")

    def read_record(self, *args, **kwargs):
        ...

    def update_record(self, *args, **kwargs):
        ...

    def delete_record(self, *args, **kwargs):
        ...

addition1 = DatabaseOperator(Country)
print(addition1.__str__())
addition1.add_record(name="Polska", code="POL")
