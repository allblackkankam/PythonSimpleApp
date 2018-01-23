
Alpha ={"E":"A","V":"B","T":"C","A":"D","S":"E","D":"F","F":"G","B":"H",
"L":"I", "W":"J", "Y":"K","P":"L","O":"M","R":"N","C":"O","Z":"P","U":"Q",
"N":"R","X":"S","G":"T","M":"U","K": "V","J":"W", "I":"X", "Q":"Y","H":"Z" }

message = raw_input("Enter Your Message: ").upper()
encrypt = " "
for letter in message:
	if letter in Alpha:
		encrypt += Alpha[letter]
	else: 
		encrypt += letter
print encrypt,
