base_url = "https://dict.leo.org/"

print("Ctrl + C to exit")

while True:
    url = input("Enter url: ")
    complete_url = base_url.rstrip("/") + "/" + url.lstrip("/")
    print(complete_url)
