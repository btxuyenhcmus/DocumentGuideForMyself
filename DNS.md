# Các tip cấ u hình domain
## Setup domain
```
A record - @ - IP
A record - www - IP
```
## Setup subdomain
```
A record - sub - IP
A record - www.sub - IP
```
## Setup email
Create 5 MX record with following content:
```
MX Record - @ - ASPMX.L.GOOGLE.COM.
MX Record - @ - ALT1.ASPMX.L.GOOGLE.COM.
MX Record - @ - ALT2.ASPMX.L.GOOGLE.COM.
MX Record - @ - ALT2.ASPMX.L.GOOGLE.COM.
MX Record - @ - ASPMX3.GOOGLEMAIL.COM.
```
