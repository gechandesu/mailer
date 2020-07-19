mailer is a simple utility for sending mail through a local mail server.

It has a console interface and is designed to send email notifications.
It's suggested that the utility will be used in conjunction with other scripts on the server.

```
Optional arguments:
  -h, --help            show this help message and exit
  -f MAIL_FROM, --mail-from MAIL_FROM
                        mail sender
  -t MAIL_TO, --mail-to MAIL_TO
                        mail recipient
  -s SUBJECT, --subject SUBJECT
                        mail subject
  -m MESSAGE, --message MESSAGE
                        message text
  -q, --quiet           quiet (no output)
  -v, --version         print version and exit
```

mailer supports message templates.

just pass it the `-m'<template file>' and it will find the template in the config folder.
If the template does not exist, then the text that you specified in quotes for the `-m` argument will be sent.

You can change the folder for storing templates in `config/config.py`.
This file also contains other default values:

```
TEMPLATES_PATH = "config/"
HEADERS = "headers.template"
MAIL_FROM = "notify@example.com"
MAIL_TO = "root@example.org"
SUBJECT = "Mail from mailer.py\n\n"
TEMPLATE = "default.message"
```

These values are used when no arguments are specified for the mailer.

`config/` folder also contains message headers in `headers.template` file.
