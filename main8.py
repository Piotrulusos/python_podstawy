# slicing = create a substring by extracting elements form another string
# slicing = utwórz substring wyodrębniając elementy z innego stringa
#           indexing[] or slice()
#           [start:stop:step] [odkąd:dokąd:co_ile]
# name = "Piotr Kowalczyk"
#
# first_name = name[:5] # przedział (] !!!
# last_name = name[6:] # puste to do konca/od poczatku
# funky_name = name[::5]
# reversed_name = name[::-1]
#
# print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)  # każdy index ma negatywny index czyli od prawej i od -1

print(website1[slice])
print(website2[slice])
