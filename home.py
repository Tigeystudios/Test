import streamlit as st
import re
import json

ACCOUNTS_FILE = 'accounts.json'

with open(ACCOUNTS_FILE, 'r') as a:
	accounts = json.load(a)

def register_page():
	new_un = st.text_input()
	new_pw = st.text_input()
	submitted = st.form_submit_button("Register")

	if submitted:
		accounts = st.session_state.accounts
	        if username in accounts:
	            st.error("Username already exists. Please choose a different one.")
	        if not username:
	            st.error("Username cannot be empty.")
	        if len(new_pw) < 6:
	            st.error("Password must be at least 6 characters long.")
	        if not re.search(r"[a-z]", new_pw):
	            st.error("Password must contain at least one lowercase letter.")
	        if not re.search(r"[A-Z]", new_pw):
	            st.error("Password must contain at least one uppercase letter.")
	        if not re.search(r"\d", new_pw):
	            st.error("Password must contain at least one digit.")
	        if not re.search(r"[!@#$%^&*()_+={}\[\]|\\:;'<>,.?/`~-]", new_pw):
	            st.error("Password must contain at least one special character.")

def login_page():
	pass

def friend_select_page():
	pass

def text_friend_page():
	pass

def main():
	reg = st.button('Register An Account')
	if reg:
		register_page()
	log = st.button('Login')
	if log:
		login_page()

main()
