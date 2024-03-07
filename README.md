# `pittfinder`

A simple and easy-to-use API for [find.pitt.edu](https://find.pitt.edu)!

To avoid being rate-limited, connect to PittNet via on-campus `WIRELESS-PITTNET` or the [GlobalProtect VPN](https://services.pitt.edu/TDClient/33/Portal/KB/ArticleDet?ID=293).

## Examples

```py
import pittfinder
from pittfinder import download

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
download.download_query_response('"Test, Student"')
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
