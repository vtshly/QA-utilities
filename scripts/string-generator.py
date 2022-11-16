import os
import secrets
import string
import clipboard

input1 = os.environ['ESPANSO_STRLENGTH_LENGTH'] ## Injecting arguments from Espanso input form into python script variable

stringLength = int(input1)
vString = ''.join((secrets.choice(string.ascii_letters + string.digits) for i in range(stringLength)))

## genStrWithPunctuation = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(vNumber)))

print(vString)
# output 6Tg7gw5T

clipboard.copy(vString) ## Copy result into system clipboard. To find by the clipboard history later
