import requests


base_url = "https://supremecourt.gov.np/court/patanhc/cause_list_detail"

bench_ids = [
    "252884",
    "252862",
    "252886",
    "252869",
    "252866",
    "252860",
    "252859",
    "252880",
    "252874",
    "252864",
    "252888",
    "252890",
    "252893",
    "252895",
    "252900",
    "252876",
    "252897",
]
bench_nos = [
    "१",
    "१",
    "३",
    "४",
    "४",
    "४",
    "४",
    "५",
    "६",
    "६",
    "७",
    "८",
    "९",
    "१०",
    "११",
    "११",
    "१२",
]

for bench_id, bench_no in zip(bench_ids, bench_nos):

    payload = {
        "bench_id": bench_id,
        "bench_no": bench_no,
        "hearing_date": "20820318",
    }

    files = [
        ("bench_id", (None, bench_id)),
        ("bench_no", (None, bench_no)),
        ("hearing_date", (None, "20820318")),
    ]
    response = requests.post(base_url, files=files)

    print(response.status_code, response.text)

    with open(f"general/{bench_no}.html", "a") as f:
        f.write(response.text)

# payload = {
#     "bench_id": "252884",
#     "bench_no": "१",
#     "hearing_date": "20820318",
# }

# files = [
#     ("bench_id", (None, "252884")),
#     ("bench_no", (None, "१")),
#     ("hearing_date", (None, "20820318")),
# ]
# response = requests.post(base_url, files=files)

# print(response.status_code, response.text)
