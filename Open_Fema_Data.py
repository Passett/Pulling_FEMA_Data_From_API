#Import dependencies
import json
import requests
import csv

#File path for finished output 
File_Path=r'C:\Users\richardp\Desktop\OpenFEMA_Data\Open_FEMA_Data.csv'

print("We are pulling your data now. We will let you know once this action is complete.")

#Pull API data, set limit to 10 bajillion
response_API=requests.get("https://www.fema.gov/api/open/v1/PublicAssistanceFundedProjectsDetails.json?$limit=10000000")
Raw_Data=response_API.text

#Load API data as string and pull the FEMA data for Florida
json_file=json.loads(Raw_Data)
json_data=json_file["PublicAssistanceFundedProjectsDetails"]
filtered_data=[data for data in json_data if data['state'] =='Florida']

#Convert JSON data to csv format
with open (File_Path, "w", encoding="utf-8", newline='') as f:
    field_names=filtered_data[0].keys()
    writer=csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    for data in filtered_data:
        writer.writerow(data)

f.close()
 
print("Download complete!")