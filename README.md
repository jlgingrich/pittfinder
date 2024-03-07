# `pittfinder`

A simple and easy-to-use API for [find.pitt.edu](https://find.pitt.edu)!

## Requirements

```text
python = "^3.10"
selectolax = "^0.3.20"
requests = "^2.31.0"
pathlib = "^1.0.1"
```

To avoid being rate-limited, connect to PittNet via a local connection to `WIRELESS-PITTNET` or using the [GlobalProtect VPN](https://services.pitt.edu/TDClient/33/Portal/KB/ArticleDet?ID=293).

## Examples

```py
import pittfinder

# Get search results for a query
res = pittfinder.search('"Test, Student"')
# res = [{'Email': 'helpdesk@pitt.edu',
#         'Name': 'Test, Student',
#         'Office Location Address': '717 Cathedral of Learning',
#         'Office Mailing Address': '717 Cathedral of Learning',
#         'Office Phone': '(412) 624-8859',
#         'Vcard ID': '247134',
#         'Web Page': 'technology.pitt.edu'}]

# Download the search result
pittfinder.download_query_response('"Test, Student"')
# ./"Test,_Student".json
# [
#     {
#         "Email": "helpdesk@pitt.edu",
#         "Name": "Test, Student",
#         "Office Location Address": "717 Cathedral of Learning",
#         "Office Mailing Address": "717 Cathedral of Learning",
#         "Office Phone": "(412) 624-8859",
#         "Vcard ID": "247134",
#         "Web Page": "technology.pitt.edu"
#     }
# ]
```

## Development

TBD
