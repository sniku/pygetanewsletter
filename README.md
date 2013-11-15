pygetanewsletter
================

Simple python API integration for getanewsletter.com

Example usage:

```python
GAN_USERNAME = ''
GAN_PASSWORD = ''
LIST_ID = ''  # get this calling gan.api.attributes.listing(gan.username, gan.encrypted_password)
API_KEY = ''  # get this from the website. Go to Contacts->API & Forms

gan = GAN(GAN_USERNAME, GAN_PASSWORD)

# Try to login
if gan.login():

    # List all supported methods
    gan.list_supported_methods()

    print '\n\n List all newsletters'
    newsletters = gan.api.newsletter.listing(gan.username, gan.encrypted_password)
    for newsletter in newsletters:
        print newsletter

    print '\n\nList all attributes'
    newsletters = gan.api.attributes.listing(gan.username, gan.encrypted_password)
    for newsletter in newsletters:
        print newsletter

    print '\n\nAdd new attributes'
    gan.api.attributes.create(gan.username, gan.encrypted_password, 'test_city')
    gan.api.attributes.create(gan.username, gan.encrypted_password, 'shoe_size')

    print '\n\nCreate/Update contact'
    contact = gan.api.contacts.create(gan.username, gan.encrypted_password, 'john.doe@example.com', 'John', 'Doe', {'test_city': 'Stockholm', 'shoe_size': '44'}, 3)
    print contact

    print '\n\nView single contact'
    contact = gan.api.contacts.show(gan.username, gan.encrypted_password, 'john.doe@example.com', True)
    print contact

    print '\n\nAdd new subscription'
    print gan.api.subscriptions.add(gan.username, gan.encrypted_password,
            'john.doe@example.com', LIST_ID,
            'John', 'Doe', False, API_KEY, True)

    print '\n\nView subscriptions'
    subscriptions = gan.api.subscriptions.listing(gan.username, gan.encrypted_password, LIST_ID, 0, 100)
    for subscription in subscriptions:
        print subscription


    print '\n\nDelete subscription, contact, attributes'
    print gan.api.contacts.delete(gan.username, gan.encrypted_password, 'john.doe@example.com')
    print gan.api.attributes.delete(gan.username, gan.encrypted_password, 'test_city')
    print gan.api.attributes.delete(gan.username, gan.encrypted_password, 'shoe_size')

    print '\n\nView Latest report'
    reports = gan.api.reports.listing(gan.username, gan.encrypted_password)

    if reports:
        print reports[0]
    else:
        print 'No reports found'


```
