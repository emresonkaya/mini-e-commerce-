import json
import os 

class JsonHandler:
    #this class will handle all file op (read and write)for the system act as a bridge betwween program and json files 
    #staticmethod 
    def load_data(filename):
        #read data from json returns as emptiy if the file doesnt exist or corrupt
        if not os.path.exists(filename):
            return[]
        
        try:
            with open(filename, 'r', encoding='utf-8' ) as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
        

    #staticmethod2 
    def save_data(filename, data):
        #writes data to Json file
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving file {filename}: {e}")
            return False

