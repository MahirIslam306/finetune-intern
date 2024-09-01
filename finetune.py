# finetune.py
# Mahir Islam
# 8/2/2024
# Python 3.11.1
# Uploads training data from jsonl file to OpenAI with the purpose of creating a
# finetuned model.

import os
from openai import OpenAI

#input_jsonl_file = 'input_data.jsonl'
input_jsonl_file = 'training_data.jsonl'
MY_KEY = '<ADD_IT>'
client = OpenAI(
  api_key =  MY_KEY
  #api_key=os.environ.get("OPENAI_API_KEY")
)

file = client.files.create(
  file=open(input_jsonl_file, "rb"),
  purpose="fine-tune"
)

print("File has been uploaded to OpenAI with id ", file.id)
# file-VFYYUrKK7huitpk9Dt75Jyah

ft_job = client.fine_tuning.jobs.create(
  training_file=file.id,
  model="gpt-3.5-turbo"
)

print("Fine Tune Job has been created with id ", ft_job.id)
# ftjob-lOVMmYRp5irUoqcA2ucZLEue
