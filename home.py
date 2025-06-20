import streamlit as st
import re

ACCOUNTS_FILE = 'accounts.json'

try:
	with open(ACCOUNTS_FILE, 'r') as a:
		accounts = json.load(a)
except JSONDecodeError:
	st.warrning('There are no current accounts.')

st.title('Welcome to Chat Time Fun!') 
