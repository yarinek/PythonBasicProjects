import pyshorteners as ps 

url = "..."

u = ps.Shortener().tinyurl.short(url)

print(u)
