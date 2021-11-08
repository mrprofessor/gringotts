# gringotts
A password manager named after the famous wizarding bank.

## Design

< Add picture here >

### Tools used 

1. Backend application Framework - Flask
2. Application server: uWSGI
3. Web server: NGINX (possibly)
4. Frontend - React (No Redux)
5. Database - A local file (**NOT A DB**)
6. Deployment - Docker


### Backend APIs 

1. List all the passwords

```
    GET /api/passwords/
```

2. Get one particular password
```
    GET /api/passwords/:id/
```

3. Create one password

```
    POST /api/passwords/:id/
    
    Payload:
        {
           "name": "random_name"
           "password": "password"
        }
```

4. Update one password

```
    PUT /api/passwords/:id/
    
    Payload:
        {
           "name": "random_name"
           "password": "password"
        }
```

5. Delete a password

```
    DELETE /api/passwords/:id/
```

### Password storage file

Since one of the requirements is not to use a database, we have to use a local
file and store the passwords in key-value format. Designing a performant system
for this will only resemble building another key-value db like redis. 

So I have choosen to use an JSON file for this purpose. There are good libraries
to manipulate the JSON data.

To encrypt the data/file at rest, [Cryptography](https://pypi.org/project/cryptography/)
is used.

Structure of an single entry:

``` json
{

    "unique_id": {
        "name": "drop.com",
        "password": "you_got_pwned"
    }

}
```

### Encryption at rest

~~It might be a ludicrous idea, but I would like to use double encryption to store the passwords.~~

1. ~~The first key is the user key. It will only encrypt the passwords and names.~~
2. The second key will be stored in the environment. This will be used to
encrypt the JSON file. (start with this in the beginning)

Only cons to this method is that if the user looses the key, it would be
impossible to re-generate it again.


## Development

Steps to run the backend app

```
cd flask
docker build -t gringotts .
docker run  -e CONFIG_ENV="development"  -e CRYPTO_KEY="aWV0tnyeoDbWPjmAKjwV_Q6dAPTy_wjdVJGf-iwJjfY="  -p 5000:5000 gringotts
```
