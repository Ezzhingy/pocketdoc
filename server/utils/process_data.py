from google_sheets import read_google_sheet
from utils.get_database import get_database

def process_data():
    res = read_google_sheet()
    last_row = res[-1]
    time = last_row[0] # Retrieves the time col in table
    summary = last_row[3] # Retrieves the summary col in table

    dbname = get_database()
    collection_name = dbname["transcript"]
    db_transcripts = list(collection_name.find())
    if len(db_transcripts) == 0:
        collection_name.insert_one({"time": time, "summary": summary})
    else:
        db_time = db_transcripts[0]["time"] # There should only be one transcript in array
        if (db_time != time):
            collection_name.delete_many({})
            collection_name.insert_one({"time": time, "summary": summary})
            print("DELETED AND UPDATED")

    
    
