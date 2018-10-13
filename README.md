# Issue Tracker

[![Build Status](https://travis-ci.org/sarahloh/p5-issue-tracker.svg?branch=master)](https://travis-ci.org/sarahloh/p5-issue-tracker)

The Issue Tracker tracks tickets describing a user’s issue.

Issues come in two varieties:

- ‘bugs’ (which are fixed for free)
- ‘features’ (which are developed if enough money is collected)

Users can upvote bugs and feature requests and comment on raised issues.


## UX

- As a user, I want to create a ticket for a bug, so that it can be fixed.
- As a user, I want to create a ticket for a feature, so that it can be implemented.
- As a user, I want to view the tickets I have created, so that I can track their status.
- As a user, I want to upvote tickets, so that I can they will be dealt with faster.
- As a user, I want to comment on a ticket, so that the developer will have extra information about a bug or feature.

## Features

- Login - allows users to login by completing a form
- Register - allows users to register by completing a form
- Logout - allows users to logout by clicking a button
- Create a ticket - allows users to create a new ticket by completing a form
- View tickets - allows users to view all tickets by visiting the home page
- View user tickets - allows a user to view the tickets they created by visiting their profile page
- Comment on a ticket - allows users to comment on a ticket by completing a form
- Upvote a bug - allows users to upvote a bug by clicking a button
- Upvote a feature - allows users to upvote a feature by clicking a button and making a payment using a form


## Technologies Used

**Backend**

- [Python3](https://www.python.org)
- [pip3](https://pip.pypa.io/en/stable/)
- [Django](https://www.djangoproject.com)
- [Stripe](https://www.djangoproject.com)

**Frontend**

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
- [Bootstrap v4.1.1](https://getbootstrap.com/docs/4.1/)

**Version Control**

- [Git](https://git-scm.com)
- [Github](https://github.com)

## Testing

Responsive design using Bootstrap tested on Chrome using developer tools, and Safari on desktop and mobile.

1. Login form:
    1. Go to the "Login" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

2. Register form:
    1. Go to the "Register" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with all inputs valid and verify that a success message appears.

3. Logout:
    1. Click the logout button and verify that a logout success message appears.

4. Create a ticket:
    1. Go to the "Create Ticket" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with all inputs valid and verify that site redirects to new ticket page.

5. Comment on a ticket:
    1. Try to submit the empty form and verify that an error message about the required fields appears
    2. Try to submit the form with all inputs valid and verify that the comment appears on the ticket page.

6. Upvote a bug:
    1. Click on the upvote icon beside a ticket and verify that the icon changes to solid and upvotes increases by one.

7. Upvote a feature:
    1. Click on the upvote icon beside a feature and verify that the site redirects to the payment page.


## Deployment

Deployed to Heroku - https://sl-issue-tracker.herokuapp.com/

## Credits

Stripe integration added with help from this tutorial -

http://zabana.me/notes/how-to-integrate-stripe-with-your-django-app.html

