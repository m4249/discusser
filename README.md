# Discusser

This django-application is specifically designed for discussing topics. User can register or login simultaneously from this site and can create room from which She/He can choose topics of the room for eg. Django,Python and name of room for eg. why is django so much popular? simultaneously user can add description too. Other users can view this room and can message accordingly.

The user can also edit their rooms as well as their profile from settings.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```

## Features

- Users can create room of their own
- Other users can message in a room the user created.
- Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
# discusser
