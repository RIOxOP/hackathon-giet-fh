def is_in_fraud_urls(url, filename="fraud-urls.txt"):
  with open(filename, 'r') as file:
    for line in file:
      fraud_url = line.strip()  # Remove trailing newline character
      if url.startswith(fraud_url):
        return True
  return False