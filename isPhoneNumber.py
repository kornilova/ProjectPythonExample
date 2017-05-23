import re
#http://www.regexpal.com/
def isPhoneNumber(phoneNumber):
    phoneNumberRegex= re.compile(r'\d{3}-\d{3}-\d{2}-\d{2}')
    #mo=phoneNumberRegex.search(phoneNumber)
    list=phoneNumberRegex.findall(phoneNumber)
    print(list);


isPhoneNumber('refdf 495-123-12-12\nefrwerwer 345-345-34-34')

