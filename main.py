from urllib.request import Request, urlopen

def fetch_random_dad_joke() -> str:
    """
    Conflict!!

    Made in the master branch. yaaaay

    """
    req = Request(
        url="https://icanhazdadjoke.com/",
        headers={
            "Accept": "text/plain",
            "User-Agent": "Workshop"
        }
    )
    return urlopen(req).read().decode("utf-8")

print(fetch_random_dad_joke())

