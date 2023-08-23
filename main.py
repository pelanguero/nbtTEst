import gzip
import zlib
end=0
bytte=1
short=2
intt=3
longg=4
floatt=5
ddouble=6
byteArray=7
strring=8
listt=9
compuesta=10
intArray=11
longArray=12
arch=gzip.open("level.dat",mode="rb")
byte=arch.read(1)
for p in range(100):
    print(str(int.from_bytes(byte,"big"))+"|"+byte.hex()+"|"+str(byte))
    byte=arch.read(1)
arch.close()