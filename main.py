import pandas as pd
import requests
import json
import csv

def search(query, api_key, cse_id, **kwargs):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
    }
    params.update(kwargs)
    response = requests.get(url, params=params)
    return json.loads(response.text)

# Your site, for example "example.com"
site = "domain.com"

# Google API key and Custom Search Engine ID
api_key = "AIzaSyDttEgxQFDeP80-Yo_kDGXdUzGGQwIXXXX"
cse_id = "833fd49e4f0cXXXXX"

# Upload CSV file
# uploaded = files.upload()

# Read the CSV file
df = pd.read_csv('input.csv')  # Assuming the columns are 'keyword', 'target_page'

# Create a new dataframe to store results
results_df = pd.DataFrame()

for index, row in df.iterrows():
    # search query
    query = f"site:{site} {row['keyword']} -inurl:{row['target_page']}"

    # get the search results
    results = search(query, api_key, cse_id)

    # Extract the URLs of the search results
    link_list = [result['link'] for result in results.get('items', [])]

    # If less than 10 links are returned, fill the rest with None
    while len(link_list) < 10:
        link_list.append(None)

    # Append the list of links to the results dataframe
    results_df = pd.concat([results_df, pd.Series(link_list, name=index)], axis=1)

# Transpose the results dataframe and set column names
results_df = results_df.transpose()
results_df.columns = [f'link{i+1}' for i in range(10)]

# Concatenate the original dataframe with the results dataframe
df = pd.concat([df, results_df], axis=1)

# Write the updated dataframe to a CSV file and download it
df.to_csv('output.csv', index=False)
# files.download('output.csv'
