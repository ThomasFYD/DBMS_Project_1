import requests

# URL of the data file
url = 'https://futurereadypa.org/home/getdatafile?id=15'

# Make a request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a file (assumed to be binary data like Excel)
    output_file = 'downloaded_data.xlsx'

    # Open a file in binary write mode
    with open(output_file, 'wb') as file:
        file.write(response.content)

    print(f"Data has been saved to {output_file}")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

