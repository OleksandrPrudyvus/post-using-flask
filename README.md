# Post App

Post App is a simple web application for managing post and tag.
1. In this project the following actions were implemented on the posts: adding, editing and deleting.

2. If your role is admin, you can create role and tag.

3. User registration, editing and deletion functions have been created.

4. User roles have been created to manage the site.
***
### Start using the application

Python must already be installed
***
### Deployment

1. Clone the repo: 
   
   * `git clone https://github.com/OleksandrPrudyvus/post-using-flask`
    
2. Create the virtual environment in project:

   * `cd post-using-flask`

   * `python -m venv venv`
   
   * `source venv/bin/activate`
   
3. Install project requirements:

   * `pip install -r requirements.txt`

4. Run the migration scripts to create database schema:
       
   * `flask db init` - further use is optional, in case of intentional reinstallation
   
   * `flask db migrate`
     
   * `flask db update`
***
##### After these steps you should see the home page of the application

