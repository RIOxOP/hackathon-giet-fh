from search_good import is_in_top_domains
from domain_analysis import domain_analysis
from search_bad import is_in_fraud_urls

url = "http://www.sinduscongoias.com.br/index.html"

# If domain is in top_domains, return 95

if is_in_top_domains(url):
    print(95)
elif is_in_fraud_urls(url):
    print(10)   
else:
    domain_analysis(url)