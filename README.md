# Blog API
[![Build Status](https://travis-ci.org/olawalejarvis/blog_api_tutorial.svg?branch=part3)](https://travis-ci.org/olawalejarvis/blog_api_tutorial) [![Coverage Status](https://coveralls.io/repos/github/olawalejarvis/blog_api_tutorial/badge.svg?branch=part3)](https://coveralls.io/github/olawalejarvis/blog_api_tutorial?branch=part3)

## Installation
  - Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/) and [MariaDB](https://mariadb.org//) on your machine
  - Clone the repository `$ git clone https://github.com/trewpog/FlaskWebApp.git`
  - Change into the directory `$ cd /FlaskWebApp`
  - Activate the project virtual environment with `$ pipenv shell` command
  - Install all required dependencies with `$ pipenv install`
  - Export the required environment variables
      ```
      $ export FLASK_ENV=development
      $ export DATABASE_URL=mysql+pymysql://blog:blog@localhost:3333/blog
      $ export JWT_SECRET_KEY=itsmylife
      ```
    
  - Start the app with `python run.py`
  
  ```
    python -m pip install --upgrade python-dotenv flask flask-sqlalchemy mariadb flask-migrate flask-script marshmallow flask-bcrypt pyjwt
  ```

## Docker
    
    docker run --name flask_blog -p 3333:3306 -e MYSQL_ROOT_PASSWORD=blog -e MYSQL_DATABASE=blog -e MYSQL_USER=blog -e MYSQL_PASSWORD=blog -d mariadb

## POSTS
- Part 1: https://www.codementor.io/olawalealadeusi896/restful-api-with-python-flask-framework-and-postgres-db-part-1-kbrwbygx5
- Part 2: https://www.codementor.io/olawalealadeusi896/building-a-restful-blog-apis-using-python-and-flask-part-2-l9y8awusp
- Part 3: https://www.codementor.io/olawalealadeusi896/building-a-restful-blog-apis-using-python-and-flask-part-3-lx7rt8pfk
