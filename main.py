import langchain
from dotenv import load_dotenv
load_dotenv()
langchain

import os

print(os.environ.get("DB_NAME"))

def main():
    print("Hello from chatbi-project!")


if __name__ == "__main__":
    main()
