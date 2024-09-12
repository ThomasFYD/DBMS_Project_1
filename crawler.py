import requests

# URL of the data file
url = 'https://www.education.pa.gov/Documents/Data%20and%20Statistics/Loan%20Cancellation/Public/0506%20Public%20Schools%20Percent%20Low%20Income.xls'

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

