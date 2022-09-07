
# potatoCash
A shared expenses application written in Python, built using Django. 

- [potatoCash](#potatocash)
  - [Inspirations](#inspirations)
  - [Features](#features)
    - [Core](#core)
      - [Shared Expenses](#shared-expenses)
      - [Notifications](#notifications)
      - [Expense Prediction/Insights](#expense-predictioninsights)
      - [UI](#ui)
      - [User Management](#user-management)
      - [Audit log](#audit-log)
    - [Extended](#extended)
      - [References](#references)

## Inspirations
- [Beem](https://www.beemit.com.au)
- [IHateMoney](https://ihatemoney.org)
- [Cospend](https://apps.nextcloud.com/apps/cospend)

## Features
### Core
These features should be prioritorised for intial release.
#### Shared Expenses
- Split expenses between users and groups.
- Document upload
- Image capture
#### Notifications
  - Email and SMS.
  - Customisable notifcation preferences.
#### Expense Prediction/Insights
  - Estimate your weekly, monthly, yearly.
  - To work our "hypothetical" expenses without commitment to add. "Calculator"
#### UI
- Responsive web app
- As simple a UI/UX as possible. 
#### User Management
- Invite users by email
- Group administration
- Guest access via one time email link
#### Audit log
- User actions
- User sign in

### Extended
These features should be aimed for future releases. 
- Automated invoice reading/expense creation. 
  - via email? from attachment?
- API
- Native mobile app.
- EFTPOS API integration? Mimic functionality of Beem. 

#### References
https://www.w3schools.com/django/django_models.php
https://bulma.io/documentation/overview/classes/
https://realpython.com/django-user-management/
https://learndjango.com/tutorials/django-login-and-logout-tutorial