import streamlit as st
import json

from snowflake.snowpark import Session, version, Window, Row
