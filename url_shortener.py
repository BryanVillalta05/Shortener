import pyshorteners

link = input("Pega tu link acá --> ")

shortener= pyshorteners.Shortener()

output= shortener.tinyurl.short(link)

print(output)
