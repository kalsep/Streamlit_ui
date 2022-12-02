''' Import Libraries '''
import numexpr

numexpr.set_num_threads(numexpr.detect_number_of_cores())
# print(numexpr.detect_number_of_cores())

import os
# os.environ['NUMEXPR_MAX_THREADS'] = numexpr.detect_number_of_cores()

import warnings

warnings.filterwarnings('ignore')

import re
import xlwt
from xlwt import Workbook
from datetime import datetime
import datetime
import sys
import jwt
import time
import uuid
import base64
import getpass
import itertools
import numpy as np
import pandas as pd
from PIL import Image
from pytz import timezone
from excel_fast_load import excel_fast_load
from datetime import date, datetime, timedelta

from openpyxl import load_workbook, Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

from zeep import Client
from zeep.wsse import UsernameToken
from zeep.helpers import serialize_object
# from zeep.wsdl.utils import etree_to_string

import matplotlib
#
# from lxml import etree

import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')

import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli
import streamlit.components.v1 as html
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
from st_aggrid import GridOptionsBuilder, AgGrid

''' Define Path '''
if 'win' in sys.platform:
    path = "C:\\Users\\" + getpass.getuser() + "\\OneDrive - Accenture\\Documents\\Projects\\Workday\\WRT's FIles Versions\\1 Oct - Copy"
else:
    path = '/home/pravin/Desktop/1 Oct - Copy'
