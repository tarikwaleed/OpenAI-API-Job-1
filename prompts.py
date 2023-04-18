import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('questions.csv')

# Extract the 'Question' column as a list of strings
questions = df['Question'].tolist()

# Build a list of prompts by appending a question mark to each question
prompts = [q  for q in questions]
