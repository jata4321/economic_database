from models.model import Country, Macro, SessionLocal
import streamlit as st

st.subheader("Database operation")


class Operator:
    def __init__(self, session_instance: SessionLocal, model) -> None:
        self.model = model
        self.session = session_instance

    def __str__(self) -> str:
        return f"Database operation on ({self.model})"

    def create_record(self, **kwargs) -> None:
        instance = self.session.query(self.model).filter_by(**kwargs).first()
        if instance:
            st.warning("⚠️Record already exists!")
        else:
            instance = self.model(**kwargs)
            self.session.add(instance)
            self.session.commit()
            st.success("🎉Record added!" )

    def read_record(self, **kwargs):
        return self.session.query(self.model).get(**kwargs)

    def read_all_records(self):
        return self.session.query(self.model).all()

    def update_record(self, **kwargs):
        instance = self.session.query(self.model).get(**kwargs)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            self.session.commit()
            return instance
        return None

    def delete_record(self, **kwargs):
        instance = self.session.query(self.model).get(**kwargs)
        if instance:
            self.session.delete(instance)
            self.session.commit()
            return True
        return False

# Create a new session
session = SessionLocal()

# Instantiate Operator class for Country, Macro model
country_db_operator = Operator(session, Country)
macro_db_operator = Operator(session, Macro)


tab1, tab2, tab3 = st.tabs(["Add country", "Add macro", "Add data"])

with tab1:
    with st.form("add_country", clear_on_submit=True, enter_to_submit=False):
        country_name = st.text_input("Country name:")
        country_code = st.text_input("Country code:")
        submit_country = st.form_submit_button("Submit Country")
        if submit_country:
            country_db_operator.create_record(name=country_name.capitalize(), code=country_code.upper())

with tab2:
    with st.form("add_macro", clear_on_submit=True, enter_to_submit=False):
        macro_name = st.text_input("Macro name:")
        country_name = country_db_operator.read_all_records()
        country_dict = {country.name: country.id for country in country_name}
        country_id = st.selectbox("Country:", list(country_dict.keys()))
        submitted_macro = st.form_submit_button("Submit")
        if submitted_macro:
            macro_db_operator.create_record(name=macro_name.upper(), country_id=country_dict[country_id])
