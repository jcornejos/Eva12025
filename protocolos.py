OSPF=110
RIP=120
EIGRP=90
BGP=20

pregunta = str(input("De que protocolo desea saber su AD(Distancia Administrativa)?:"))

if pregunta == str("OSPF):"):
    print("El AD de OSPf es "+ str(OSPF))
elif pregunta == str("RIP"):
    print("El AD de RIP es "+ str(RIP))
elif pregunta == str("EIGRP"):
    print("El AD de EIGRP es "+ str(EIGRP))
elif pregunta == str("BGP"):
    print("El AD de BGP es "+ str(BGP))
else:
    print("Porfavor escriba de forma correcta el nombre del protocolo (OSPF, RIP, EIGRP o BGP)")