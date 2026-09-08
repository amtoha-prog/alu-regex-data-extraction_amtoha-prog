import re

import json

# Defining regex patterns
patterns = {
    'email': r'\b[A-Za-z0-9.]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b',
    'phone': r'\+?\d{1,3}[\s.-]?\(?\d{2,3}\)?[\s.-]?\d{2,4}[\s.-]?\d{2,4}',
    'url': r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?',
    'hashtag': r'#[A-Za-z0-9_]+'  ,  
    'credit_card': r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
}
# Read the input file
with open ('input/raw-text.txt', 'r') as f:
    raw_text=f.read()

extracted_data = {
    'emails': [],
    'phones': [],
    'urls':[],
    'hashtags': [],
    'credit_cards': []

}
# Find all emails
print("Searching for emails...")
for match in re.finditer(patterns['email'], raw_text):
    email = match.group()  
    extracted_data['emails'].append(email)  
    print(f"  Found: {email}")

# Find all phone numbers
print("\n Searching for phone numbers...")
for match in re.finditer(patterns['phone'], raw_text):
    phone = match.group()
    extracted_data['phones'].append(phone)
    print(f"  Found: {phone}")

# Find all URLs
print("\nSearching for URLs...")
for match in re.finditer(patterns['url'], raw_text):
    url = match.group()
    extracted_data['urls'].append(url)
    print(f"  Found: {url}")

# Find all hashtags
print("\nSearching for hashtags...")
for match in re.finditer(patterns['hashtag'], raw_text):
    hashtag = match.group()
    extracted_data['hashtags'].append(hashtag)
    print(f"  Found: {hashtag}")

# Find all credit cards
print("\nSearching for credit card numbers...")
for match in re.finditer(patterns['credit_card'], raw_text):
    card = match.group()
    extracted_data['credit_cards'].append(card)
    print(f"  Found: {card}")