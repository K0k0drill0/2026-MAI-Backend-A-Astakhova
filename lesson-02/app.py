import random
import string
import time


def generate_password():
    length = random.randint(8, 16)
    special_chars = "#.,!@&^%*"

    required = [
        random.choice(string.digits),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(special_chars),
    ]

    alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase + special_chars
    rest = [random.choice(alphabet) for _ in range(length - len(required))]

    password_chars = required + rest
    random.shuffle(password_chars)
    return "".join(password_chars)


def application(environ, start_response):
    password = generate_password()
    time.sleep(0.05)

    body = password.encode("utf-8")
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ]
    start_response(status, headers)
    return [body]
