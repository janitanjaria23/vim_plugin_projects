import imaplib, re
import sys


def gmail_checker(username, password):
    imap_object = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        imap_object.login(username, password)
        response_status, response_info = imap_object.status('To Me', '(MESSAGES UNSEEN)')
        messages = int(re.search('MESSAGES\s+(\d+)', response_info[0]).group(1))
        unseen = int(re.search('UNSEEN\s+(\d+)', response_info[0]).group(1))
        return messages, unseen
    except Exception as err:
        return False, 0


def main():
    user_name = 'username@gmail.com'
    password = 'password'
    messages, unseen = gmail_checker(user_name, password)
    print "Total Messages: %d" % messages
    print "Unseen Messages: %d" % unseen


main()
