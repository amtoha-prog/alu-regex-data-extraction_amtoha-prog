import re

import json

# Defining regex patterns
pattern = {
    'email': r'\b[A-Za-z0-9.]+ @[A-Za-z0-9]+\.[A-Za-z]{2,}\b',
    'phone': r'\+?\d{1,3}[\s.-]?\(?\d{2,3}\)?[\s.-]?\d{2,4}[\s.-]?\d{2,4}',
    'url': r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?',
    'hashtag': r'#[A-Za-z0-9_]+'    

}
