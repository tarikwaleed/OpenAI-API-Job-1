import pandas as pd
import openai
from dotenv import load_dotenv
import os
from prompts import prompts

load_dotenv()  # load environment variables from .env file

api_key = os.environ.get("OPENAI_API_KEY")
org_id = os.environ.get("ORG_ID")

openai.api_key = os.environ["OPENAI_API_KEY"]

model_engine = "davinci"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompts,
    # max_tokens=64,
    # n=5,
    # stop="\n",
    # temperature=0.7,
    # presence_penalty=0.5,
    # frequency_penalty=0.5,
)
output_df = pd.DataFrame([choice.text for choice in completions.choices], columns=["Generated Text"])
output_df.to_csv("answers.csv", index=False)

