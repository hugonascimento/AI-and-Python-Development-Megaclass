# Write a program to find and replace all email addresses in a string using regex
import re

# Function to find and replace email addresses in a given text
def find_and_replace_emails(text, new_localpart, new_domain):
    # Regex pattern to match email addresses
    email_pattern = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

    # Replace email addresses with the new local part and domain
    return re.sub(
        email_pattern,
        # Lambda function to construct the new email address
        lambda match: f"{new_localpart if new_localpart else match.group(1)}@{new_domain}",
        text,
    )

# Function to handle user input and replace emails in the provided text
def replace_emails_in_input(text):
    # Check if the input text is empty
    if text == "":
        print(
            "\nNo text provided. Using the default example text.\nMy email is hugo@hugo.com, you can send me some if you want.\n"
        )
        # Default example text
        text = "My email is hugo@hugo.com, you can send me some if you want."

    # Prompt the user for a new local part of the email
    replacement_localpart = input(
        "Enter a new email (before @) or press Enter to keep it: "
    )
    # Prompt the user for a new domain of the email
    replacement_domain = input(
        "Enter a new domain for the email (after @) or press Enter to use default (example.com): "
    )

    # Use default domain if the user did not provide one
    if replacement_domain == "":
        replacement_domain = "example.com"

    # Replace emails in the text using the helper function
    new_text = find_and_replace_emails(text, replacement_localpart, replacement_domain)

    return new_text

# Main execution block
print(
    # Prompt the user for input text and display the corrected text
    f"The corrected text is: {replace_emails_in_input(input('Enter a Text with email address or press Enter to use the example: '))}"
)
