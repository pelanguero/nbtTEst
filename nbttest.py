import nbtlib
import json
import zlib

file=open("r.-2.0.mca","rb")
pointer=0
header=[]
while(pointer<4096):
    file.seek(pointer)
    temp=[]
    offset=file.read(3)
    temp.append(int.from_bytes(offset))
    pointer=pointer+3
    file.seek(pointer)
    size=file.read(1)
    temp.append(int.from_bytes(size))
    pointer=pointer+1
    header.append(temp)
pointer=0
while(pointer<len(header)):
    pos=(header[pointer][0]*4096)+5
    file.seek(pos)
    out=open("outt.nbt","wb")
    chunk=zlib.decompress(file.read((header[pointer][1]*4096)))
    out.write(chunk)
    out.close()
    nbt=nbtlib.load("outt.nbt")
    chunkz=37//16
    chunkx=-727//16
    chunky=68//16
    print(nbt["xPos"])
    print(nbt["zPos"])
    pointer=pointer+1
    if nbt["xPos"]==chunkx and nbt["zPos"]==chunkz:
        print("true")
        #print(nbt)
        pointer=20000
        pprointer=0
        while(pprointer<len(nbt["sections"])-1):
            subchunk=nbt["sections"][pprointer]
            if chunky==nbt["sections"][pprointer]["Y"]:
              print("/*"+str(pprointer)+"*/")
              temdp=nbt["sections"][pprointer] 
              print(temdp.keys())
            pprointer=pprointer+1

file.close()
