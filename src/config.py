import os
import dotenv

dotenv.load_dotenv('../.env')

DB_NAME = os.environ.get('POSTGRES_DB', 'med_center')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT', '5432')