# Reguler expression : 

# text = "i am a data"

import re 

# text = "CarDekho brings a complete range of new cars in 2023 in India with prices. 9283627829 You can search cars by applying filters such as by price, by bodytype, by brand, by seating capacity & more. 9286102835 Also, stay updated with 8273927308coming cars, electric cars in India, compare cars in your price range and stay tuned to  9272873621the latest car news."


# ptrn = "\d\d\d\d\d\d\d\d\d\d"
#   \(\d{3}\)-\d{3}-\d{4}-\d{3}
# ptrn = "\d{10}"


# matches = re.search(ptrn, text)
# matches = re.finditer(ptrn, text)
# matches = re.findall(ptrn, text)

# print(matches)




# for i in matches:
#     print(i)



text = "CarDekho brings a complete range of new cars in 2023 in India with prices. 9283627829 resmYou can search cars by applying filters such as by price, by bodytype, by brand, by seating capacity & more. rkkm 9286102835 Also, stay updated with 8273927308coming cars, electric cars in India, compare cars in your price range and stay tuned to  9272873621the latest car news. room"


# ptrn = "aaaaaaaa"

# # mtch = re.sub(ptrn, "aaaaaaaa", text)
# mtch = re.match(ptrn, text)

# print(mtch)


# WILDCARD

ptrn = "r..m"

math = re.findall(ptrn, text)

print(math)

