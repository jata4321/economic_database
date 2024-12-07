import streamlit as st

st.title("Economic database")
st.subheader("presentation of economic data")

def main():
    page = st.Page('./pages/maintenance/dbase_operate.py', title='Database operation',
                   icon='⚠')
    pg = st.navigation(
        {'Database operation': [page]}
    )

    pg.run()

if __name__ == "__main__":
    main()