def extract_username_domain(email_address):
    parts = email_address.split("@")
    username = parts[0]
    domain = parts[1]
    return username, domain

# Example usage
email = "22cs453@kpriet.ac.in"
username, domain = extract_username_domain(email)
print("User name:", username)
print("Domain name:", domain)
