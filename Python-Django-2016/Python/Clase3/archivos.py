import string
import random

# fo = File-Open  
# Se puede cambiar el nombre
fo = open("foo.txt", "wb")
fo.write("Python es el mejor lenguaje.\nEs genial!!\n")
for i in range(100):
    texto = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for i in range(10))
    fo.write("%s" % texto)
fo.close()

fo2 = open("foo.txt", "r+")
srti = fo2.read()
print srti
fo2.close()
