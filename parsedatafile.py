# parsedatafile.py
# Mahir Islam
# 8/5/2024
# Python 3.11.1
# Goes through txt file line by line and creates a jsonl file from it.
# Currently just prints the values.

import os
import json

data_file = "intern_ft_project_org_data.txt"
file = open(data_file, "r")

line = file.readline()

system_prompt = line[line.rfind('=') + 1:].strip()

count = 0

training_data = open('training_data.jsonl', 'w')
for line in file:
    #print("STARTING********* ....")
    user_content = line[:line.rfind('```json{')-1].strip()
    assistant_content = line[line.rfind('```json{') + 7:].strip()
    count = count+1
    #print("Line #: ", count)
    '''
    try:
        assistant_content = json.loads(assistant_content)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print("Line: " + str(count) + " Content: " + assistant_content)
        continue
    '''
    data_line_list = {
                        "messages":
                        [
                            {
                                "role": "system",
                                "content": system_prompt
                            },
                            {
                                "role": "user",
                                "content": user_content
                            },
                            {
                                "role": "assistant",
                                "content": assistant_content
                            }
                        ]
                     }
    #training_data.write("LINE :"+str(count)+" :" )
    json.dump(data_line_list, training_data)
    training_data.write('\n')

training_data.close()    
#for item in data_line_list:
#    print(item)
#    print()

'''
for line in file:
        print(line[:line.rfind('```json{')-1].strip() )
        print(line[line.rfind('```json{')+7:])
'''
