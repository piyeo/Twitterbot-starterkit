import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("CUSTOMER_KEY")
CS = os.environ.get("CUSTOMER_SECRET")
AT = os.environ.get("ACCESS_TOKEN")
AS = os.environ.get("ACCESS_SECRET")