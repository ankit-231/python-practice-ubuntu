def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response(
        "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
    )
    return iter([data])


# if __name__ == "__main__":
#     from wsgiref.simple_server import make_server

#     httpd = make_server("", 8002, app)
#     httpd.serve_forever()
