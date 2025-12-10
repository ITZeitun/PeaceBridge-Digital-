import os
from dotenv import load_dotenv
LOGIN_REDIRECT_URL = 'index'  # where to go after login
LOGOUT_REDIRECT_URL = 'login' # already handled in your LogoutView


load_dotenv()

DAR_CONSUMER_KEY = os.getenv("DAR_CONSUMER_KEY")
DAR_CONSUMER_SECRET = os.getenv("DAR_CONSUMER_SECRET")
DAR_SHORTCODE = os.getenv("DAR_SHORTCODE")
DAR_PASSKEY = os.getenv("DAR_PASSKEY")
DAR_CALLBACK_URL = os.getenv("DAR_CALLBACK_URL")
