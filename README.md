## fyle-ifsc-loopkup


#### Deploy

* heroku create
* heroku addons:create heroku-postgresql:hobby-dev
* git push heroku master

#### Libraries and SDKs

* Flask
* Gunicorn
* SQLAlchemy
* Postgres

#### APIs

```
GET
https://fyle-ifsc-loopkup.herokuapp.com/bank/branch?bank_name={name}&city={city}

GET
https://fyle-ifsc-loopkup.herokuapp.com/bank/branch/{ifsc}

Example

https://fyle-ifsc-loopkup.herokuapp.com/bank/branch/sbin0001339
https://fyle-ifsc-loopkup.herokuapp.com/bank/branch?bank_name=state%20bank%20of%20india&city=mumbai
```

