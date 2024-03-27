import requests
from backend_contact import send_email

# Ensure your API key is included in the URL
api_key = "c67d19eb481749fc9b540e35915579c3"
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"

response = requests.get(url)
content = response.json()

# Check if the response contains the expected 'articles' key
if "articles" in content:
    # Initialize an empty string to store the body of the email
    body = ""

    for article in content["articles"]:
        # Check if description exists, if not, assign an empty string
        description = article["description"] if article["description"] else ""
        # Concatenate the title, description, URL, and additional lines
        body += f"{article['title']}\n{description}\n{article['url']}\n\n"

    # Define the subject for the email
    subject = "Top Business Headlines from NewsAPI"

    # Call the send_email function with the subject and message
    send_email(subject, body)  # This line sends the email
else:
    print("Error: Unable to retrieve articles from NewsAPI.")

