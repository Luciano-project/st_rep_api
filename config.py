import dotenv
import os

dotenv.load_dotenv()

REPLICATE_API_KEY = str(os.getenv("REPLICATE_API_KEY"))