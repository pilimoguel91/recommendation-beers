# Databricks notebook source
import ast
import numpy as np
import requests
import pandas as pd

from datetime import datetime
from itertools import chain
from requests.structures import CaseInsensitiveDict


# COMMAND ----------

beers_json_pdf = pd.read_json(f'beers.json')
beers

beers_json_sdf =spark.createDataFrame(beers_json_pdf) 

beers_json_sdf.createOrReplaceTempView("beers_json_sql")


# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT * FROM beers_sql
