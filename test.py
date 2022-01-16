from datetime import datetime

text="11/24/2021 8:11 AM"
fmt="%d/%m/%Y %-I:%M %p"

print(datetime.strptime(text, fmt))