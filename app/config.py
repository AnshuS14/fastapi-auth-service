import os
from dotenv import load_dotenv

# Step 1: Load .env file
load_dotenv()

# Step 2: Read variables
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
)

# Step 3: Validate important values
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is missing in .env file")
    