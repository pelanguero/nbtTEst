import zlib
dr=[0,1,2,4,8,4,8]
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
arch=open("r.0.0.mca",mode="rb")
ffile=open("region.txt",mode="w")
debugchun=open("region.xtx",mode="w")
salto=3
base=0
def tagarraay(chunkk):
  #refactor me pls
  tiipo=int.from_bytes(chunkk.read(1),byteorder="big",signed=True)
  tamanho=int.from_bytes(chunkk.read(4),byteorder="big",signed=True)
  print(tiipo)
  print(tamanho)
  print(chunkk.tell())
def Inarraay(cchunk):
  tag=cchunk.read(1)
  snombre=int.from_bytes(cchunk.read(2),byteorder="big")
  nombree=""
  try:
      nombree=cchunk.read(snombre).decode("utf-8")
  except:
      print(str(tag)+"|"+nombree,file=debugchun)
  print(str(tag)+"|"+nombree,file=debugchun)
  
  paysize=int.from_bytes(cchunk.read(4),byteorder="big")
  cchunk.read(paysize)

def nombrar(cchunk,profundidad=1):
  for t in range(profundidad):
    tipo=int.from_bytes(cchunk.read(1),byteorder="big",signed=True)
  
    print(str(tipo)+" "+str(cchunk.tell()),file=debugchun)
    if tipo==end:
      continue
    if tipo==bytte:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big",signed=True)
      nombree=cchunk.read(sizzee).decode("utf-8")
      print(str(tipo)+"|"+nombree,file=debugchun)
      cchunk.read(1)
    
    elif tipo==short:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=cchunk.read(sizzee).decode("utf-8")
      print(str(tipo)+"|"+nombree,file=debugchun)
      cchunk.read(2)
      
    elif tipo==intt:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=cchunk.read(sizzee).decode("utf-8")
      print(str(tipo)+"|"+nombree,file=debugchun)
      cchunk.read(4)
    
    elif tipo==longg:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=cchunk.read(sizzee).decode("utf-8")
      print(str(tipo)+"|"+nombree,file=debugchun)
      cchunk.read(8)
      
    elif tipo==floatt:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=cchunk.read(sizzee).decode("utf-8")
      print(str(tipo)+"|"+nombree,file=debugchun)
      cchunk.read(4)
      
    elif tipo==ddouble:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=""
      try:
        nombree=cchunk.read(sizzee).decode("utf-8")
      except:
        print(str(tipo)+"|"+nombree,file=debugchun)
      print(str(tipo)+"|"+nombree,file=debugchun)
      cchunk.read(8)
      
    elif tipo==byteArray:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=""
      try:
        nombree=cchunk.read(sizzee).decode("utf-8")
      except:
        print(str(tipo)+"|"+nombree,file=debugchun)
      print(str(tipo)+"|"+nombree,file=debugchun)
      tamanno=int.from_bytes(cchunk.read(4),byteorder="big")
      cchunk.read(tamanno)
      
    elif tipo==strring:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=""
      try:
        nombree=cchunk.read(sizzee).decode("utf-8")
      except:
        print(str(tipo)+"|"+nombree,file=debugchun)
      print(str(tipo)+"|"+nombree,file=debugchun)
      
      pou=int.from_bytes(cchunk.read(2),byteorder="big",signed=False)
      cchunk.read(pou)
      
    elif tipo==listt:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=""
      try:
        nombree=cchunk.read(sizzee).decode("utf-8")
      except:
        print(str(tipo)+"|"+nombree,file=debugchun)
      print(str(tipo)+"|"+nombree,file=debugchun)
      tagarraay(cchunk)
      
    elif tipo==compuesta:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=""
      try:
        nombree=cchunk.read(sizzee).decode("utf-8")
      except:
        print(str(tipo)+"|"+nombree,file=debugchun)
      print(str(tipo)+"|"+nombree,file=debugchun)
      
    elif tipo==intArray:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=""
      try:
        nombree=cchunk.read(sizzee).decode("utf-8")
      except:
        print(str(tipo)+"|"+nombree,file=debugchun)
      print(str(tipo)+"|"+nombree,file=debugchun)
      tano=int.from_bytes(cchunk.read(4),byteorder="big")
      int.from_bytes(cchunk.read(tano*4),byteorder="big")
      
    elif tipo==longArray:
      sizzee=int.from_bytes(cchunk.read(2),byteorder="big")
      nombree=""
      try: 
        nombree=cchunk.read(sizzee).decode("utf-8")
      except:
        print(str(tipo)+"|"+nombree,file=debugchun)
      print(str(tipo)+"|"+nombree,file=debugchun)
      tano=int.from_bytes(cchunk.read(4),byteorder="big")
      int.from_bytes(cchunk.read(tano*8),byteorder="big")
    
  
  

for h in range(1024):
    byte=arch.read(salto)
    byyte=arch.read(1)
    if h==1:
        print(str(int.from_bytes(byte,byteorder="big"))+"|"+str(int.from_bytes(byyte,byteorder="big")),file=ffile)
        arch.seek(int.from_bytes(byte,byteorder="big")*4096)
        size=int.from_bytes(arch.read(4),byteorder="big")
        print(size)
        arch.read(1)
        tama=zlib.decompress(arch.read(size-1))
        pest=open("chunk.br",mode="wb+")
        pest.write(tama)
        print("este es"+str(pest.tell()))
        temptan=pest.tell()
        pest.seek(0)
        nombrar(pest,temptan)
        pest.close()
        for pp in range(len(tama)):
          byytte=tama[pp:pp+1]
          print(str(int.from_bytes(byytte,"big"))+"|"+byytte.hex()+"|"+str(byytte),file=ffile)
        arch.seek(h*4)
    
      

    
    
arch.close()
ffile.close()
debugchun.close()

