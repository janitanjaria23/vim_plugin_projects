import imaplib, re


def gmail_checker(username, password):
    i = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        i.login(username, password)
        x, y = i.status('To Me', '(MESSAGES UNSEEN)')
        messages = int(re.search('MESSAGES\s+(\d+)', y[0]).group(1))
        unseen = int(re.search('UNSEEN\s+(\d+)', y[0]).group(1))
        return messages, unseen
    except Exception as err:
        return False, 0


def main():
    messages, unseen = gmail_checker('username@gmail.com', 'password')
    print "%i messages, %i unseen" % (messages, unseen)


main()
