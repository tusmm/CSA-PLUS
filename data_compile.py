import gspread
import time
import os


gc = gspread.service_account(filename="credentials.json")
gsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/10Md0RhjnPVyUNR_grxa46mNGy_dZoMT_Dbd8nUdMrLk/edit?usp=sharing")
wsheet = gsheet.get_worksheet(0)
# gets google sheet and worksheet

wsheet.update("A1", "Names")
wsheet.update("B1", "Scoring")
# adds titles

iter = 2

for file in os.listdir("comments"):  # iterates through comment files
    file_data = file.split(",")

    name = file_data[0].split("-")[-1].strip() + ", " + file_data[1].split()[0]
    # extracts student name from comment file names

    if name[-4:] == ".txt":
        name = name[:-4]

    wsheet.update("A" + str(iter), name)
    # adds student name to worksheet

    with open(os.path.join("comments", file), "r") as f:  # adds student comments/scoring to google sheet
        wsheet.update("B" + str(iter), f.read())
    
    iter += 1
    time.sleep(1)
    # waits 1 second to comply with API rate limits 