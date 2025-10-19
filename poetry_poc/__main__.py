import requests


def main() -> None:
    resp = requests.get("https://google.com", timeout=5)
    print("Poetry está funcionando!", resp.status_code)


if __name__ == "__main__":
    main()
