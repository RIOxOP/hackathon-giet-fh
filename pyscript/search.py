from urllib.parse import urlparse

def is_in_top_domains(url, filename="top-domains.txt"):
    # Extract domain from url
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)

    with open(filename, 'r') as file:
        for line in file:
            # Extract domain from top domain url
            top_domain_url = line.strip()  # Remove trailing newline character
            top_domain = '{uri.netloc}'.format(uri=urlparse(top_domain_url))

            if domain == top_domain:
                return True
    return False
