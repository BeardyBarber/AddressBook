# ADDRESS BOOK

A clean Flask aplication for storing and managing basic contacts' information. It can be used as a base for further development. 

## Getting Started



### Prerequisites

My Address Book app was developed in Python 3, using a number of dependencies. You can install them by executing the below command in the project folder. I recommend setting up a virtual environment first.

```
pip install -r requirements.txt
```

Also, for production please use PostgreSQL database instead of SQLite (see `instance/config.py`).

### Installation

Edit the variables in `instance\config.py` or your `Environment` variables - more [info](https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables).

##### Initialize the database

```
flask db init
```

##### Prepare the database migration

```
flask db migrate
```


##### Execute the database upgrade
```
flask db upgrade
```

##### Run the application

```
flask run
```

Address book app should be running on `http://127.0.0.1:5000/`


## Contributing

Please read [this](https://www.contributor-covenant.org/version/1/4/code-of-conduct) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Karol Majchrzak** - *Initial work* - [BeardyBarber](https://github.com/BeardyBarber)

See also the list of [contributors](https://github.com/BeardyBarber/AddressBook/contributors) who participated in this project.

## License

This project is licensed under the APACHE License. For further information please read [LICENCE.MD](https://github.com/BeardyBarber/AddressBook/blob/master/LICENSE) 
