def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email