#!/usr/bin/env python
import re
import sys


def chunk(l,n):
    return (l[i:i+n] for i in xrange(0, len(l), n))


def is_disposable_email(email):
    emails = [line.strip() for line in open('domain-list.txt')]
    
    """
    Chunk it!
    Regex parser doesn't deal with hundreds of groups
    """
    for email_group in chunk(emails, 20):
        regex = "(.*" + ")|(.*".join(email_group) + ")"
        if re.match(regex, email):
            return True
    
    return False
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("You must supply at least 1 email\n")
    
    for email in sys.argv[1:]:
        if is_disposable_email(email):
            sys.stderr.write("{email} appears to be a disposable address\n".format(email=email))