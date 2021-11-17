# Discusser

This django-application is specifically designed for discussing topics or anything related to programming. User can register or login simultaneously from this site and can create room from which She/He can choose topics of room for eg. Django,Python and name of room for eg. why is django so much popular? and the user can specifically comment on that room for eg. Django is popular due to its pragmatic design and ease of use. Other users can view this room and can message accordingly.

The user can also edit their rooms as well as their profile from settings.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate

# You may want to change the name `projectname`.
$ git clone https://github.com/Saumya-ranjan/Discusser.git projectname

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

## ScreenShots:

##### Home Page

![Alt text](/screenshots/ss1.png?raw=true "Optional Title")

#### Update User Page

![Alt text](/screenshots/ss2.png?raw=true "Optional Title")

#### Message Room

![Alt text](/screenshots/ss3.png?raw=true "Optional Title")

#### Browse Topics

![Alt text](/screenshots/ss4.png?raw=true "Optional Title")

#### Edit your Profile

![Alt text](/screenshots/ss5.png?raw=true "Optional Title")

#### search rooms specifically:

![Alt text](/screenshots/ss6.png?raw=true "Optional Title")
![Alt text](/screenshots/ss7.png?raw=true "Optional Title")
