emails = sorted(set([line.strip() for line in open("email_domains.txt")]))

for email in emails:
    print("'{email}',".format(email=email))
