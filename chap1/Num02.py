str1 = "パトカー"
str2 = "タクシー"
new_str = ""
for i in range(0,len(str1)):
    split_str = (str1 + str2)[i::4]
    new_str += split_str
print(new_str)