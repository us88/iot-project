# IoT Project

## Setup

First, you just have to create a virtual environment and install dependencies:

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Once that's done, you'll need to run migrations locally and create a super user:

```sh
python manage.py migrate
python manage.py createsuperuser
```

The super user details don't matter, just use "moe" for the username and "password" for the password.

## Running

```sh
python manage.py runserver
```

## Quick Demo

Once the application is running:

1. Visit http://localhost:8000/devices/123123 -- you should see a "Device not found" message.
2. Run the following CURL command:
```sh
curl -X POST http://localhost:8000/devices/send \
     -u moe:password \
     -H "Content-Type: application/json" \
     -d '{"fCnt": 100, "data": "AQ==", "devEUI": "123123"}'
```
3. Refresh the page at http://localhost:8000/devices/123123 and you will see a single payload, and the device in a "passing" state.
4. Run the following CURL command:
```sh
curl -X POST http://localhost:8000/devices/send \
     -u moe:password \
     -H "Content-Type: application/json" \
     -d '{"fCnt": 101, "data": "AA==", "devEUI": "123123"}'
```
5. Refresh the page at http://localhost:8000/devices/123123 and you will see a second payload, and the device in a "failing" state.
6. You can repeat any of the above CURL commands to test that the uniqueness of `fCnt` is honored. You should receive a 400 status code.
