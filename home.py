import streamlit as st
import re
import json

ACCOUNTS_FILE = 'accounts.json'

with open(ACCOUNTS_FILE, 'r') as a:
	accounts = json.load(a)

st.title('Welcome to Chat Time Fun!') 
