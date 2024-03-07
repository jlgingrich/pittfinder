# `pittfinder`

A simple and easy-to-use API for [find.pitt.edu](https://find.pitt.edu)! Allows you to find people at the University of Pittsburgh via name, phone number, username, or email and returns public directory information.

## Disclaimers

**This project is not associated with the University of Pittsburgh nor does it allow access to private or restricted information.**

### Rate Limiting
To avoid being rate-limited to 10 requests per 10 minutes, connect to PittNet via on-campus `WIRELESS-PITTNET` or the [GlobalProtect VPN](https://services.pitt.edu/TDClient/33/Portal/KB/ArticleDet?ID=293).

### Acceptable Use
> Information obtained from the University of Pittsburgh Directory Service may not be used to provide addresses for mailings to students, faculty or staff. This phone book is provided for information of the University of Pittsburgh community and those who have specific interest in reaching individual students, faculty or staff. Any solicitation of business, information, contributions or other responses from individuals listed in this publication by mail, telephone or other means is forbidden.
>
> https://find.pitt.edu/


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

## Developers

TBD
