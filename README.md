# ADDRESS BOOK

Simple Flask aplication for managing very simple contacts. Can be used as a base for further development. 

## Getting Started



### Prerequisites

For prerequisites instalation run 

```
pip install -r requirements.txt
```

Also for production please use PostgreSQL database instead of SQLite

### Installing


Initialize the db

```
flask db init
```

Prepare the db migration

```
flask db migrate
```

Set proper DATABASE_URL in `Config.py`


Run database upgrade
```
flask db upgrade
```

Run the application

```
flask run
```

Address book app should be running on `http://127.0.0.1:5000/ `


## Contributing

Please read [this](https://www.contributor-covenant.org/version/1/4/code-of-conduct) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Karol Majchrzak** - *Initial work* - [PurpleBooth](https://github.com/BeardyBarber)

See also the list of [contributors](https://github.com/BeardyBarber/AddressBook/contributors) who participated in this project.

## License

This project is licensed under the APACHE License. For further information please read [LICENCE.MD](https://github.com/BeardyBarber/AddressBook/blob/master/LICENSE) 
