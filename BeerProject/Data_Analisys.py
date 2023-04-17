# Databricks notebook source
import ast
import numpy as np
import requests
import pandas as pd

from datetime import datetime
from itertools import chain
from requests.structures import CaseInsensitiveDict


# COMMAND ----------

# MAGIC %run ./main.py

# COMMAND ----------

pd.read_json(f'beers.json').count()
