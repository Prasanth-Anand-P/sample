from dotenv import load_dotenv
import os

load_dotenv()

MYPASS = os.getenv("MYPASS")
if MYPASS == "ABCD":
  print("Working")
else:
  print("not working")
