'''
This is the main file that will be executed to start the GUI application.
'''
from gui import GUI
import os
from dotenv import load_dotenv
def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    gui = GUI(api_key)
    gui.run()
if __name__ == "__main__":
    main()