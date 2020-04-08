#funciones que devuelven strings con el formato
#necesario para un CLI cisco
import time
import telnetlib
import socket

def conection(user, passw, enpassw, host,ret=1,port=23):

    tn = telnetlib.Telnet(host,port)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\r\n")
    tn.read_until(b"Password: ",2)
    tn.write(passw.encode('ascii') + b"\r\n")
    tn.write(b"\r\n")
    tn.write(b"en\r\n"+str.encode(enpassw)+b"\r\n")

    time.sleep(1)
    if ret == 0: #pasar 0 si se quiere que devuelva el estado de la conexión
        out = tn.read_until(b"%",2).decode("ascii")
        tn.close()
        return out
    else:
        return tn

def staticroute(tn, dest, mask, src, dist="0",no=False):

    tn.write(b"conf t\r\n\r\n")
    if no: #if delete
        tn.write(b"no ")
    tn.write(b"ip route " + str.encode(dest) + b" " + str.encode(mask) + b" " + str.encode(src) + b" " + str.encode(dist) + b"\r\n")
    time.sleep(2)
    out = tn.read_very_eager()
    tn.close()
  #  return out

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def veriftIP(s): #ip as parameter, return True if ip is valid, False otherwise
    try:
        if validate_ip(s) == False:
            raise socket.error
        socket.inet_aton(s)
        return True
    except socket.error:
        return False

def gethostname(tn):
    hostname = tn.read_until(b">")
    hostname = hostname[find_nth(hostname, b"\r\n", 2) + 2:len(hostname) - 1]
    tn.close()
    return hostname.decode("ascii")

def sethostname(tn,hostname):
    tn.write(b"conf t\r\nhostname "+str.encode(hostname)+b"\r\n")
    time.sleep(1)
    tn.close()

def confospf(tn,pro,net,wild,area,no=False):

    tn.write(b"conf t\r\nrouter ospf "+str.encode(pro)+b"\r\n")
    time.sleep(0.5)
    if no: #if delete
        tn.write(b"no ")
    tn.write(b"network " + str.encode(net) + b" " + str.encode(wild) + b" area " + str.encode(area) + b"\r\n")
    time.sleep(0.5)
    out = tn.read_very_eager().decode("ascii")
    tn.close()
    return out

def confRip(tn,net,ver,no=False):
    tn.write(b"conf t\r\nrouter rip\r\n")
    time.sleep(0.5)
    if no:  # if delete
        tn.write(b"no ")
    tn.write(b"network " + str.encode(net) + b"\r\n")
    if no:  # if delete
        tn.write(b"no ")
    tn.write(b"version "+str.encode(ver))
    time.sleep(0.5)
    out = tn.read_very_eager().decode("ascii")
    tn.close()
    return out

def interfaceConfig(tn,int,desc,ip,mask,swmode,vlan,shut,adddesc=False,addip=False,addswmode=False,addaccess=False,addshut=False,no=False):
    tn.write(b"conf t\r\ninterface " + str.encode(int) + b"\r\n")
    if no: #if delete
        tn.write(b"no ")
    if adddesc:
        tn.write(b"description "+str.encode(desc)+b"\r\n")
    if no: #if delete
        tn.write(b"no ")
    if addip:
        tn.write(b"ip add " + str.encode(ip) + b" " + str.encode(mask) + b"\r\n")
    if no: #if delete
        tn.write(b"no ")
    if addswmode:
        tn.write(b"sw mode " + str.encode(swmode) + b"\r\n")
    if no: #if delete
        tn.write(b"no ")
    if addaccess:
        tn.write(b"sw access vlan "+str.encode(vlan)+b"\r\n")
    if addshut:
        tn.write(str.encode(shut)+b" shutdown"+b"\r\n")
    time.sleep(1)
    #out = tn.read_very_eager().decode("ascii")
    tn.close()

def confDHCP(tn,pool,fro,to,net,mask,default,dns,no,addexc,addnet,adddefault,adddns):
    tn.write(b"conf t\r\n")
    if no:  # if delete
        tn.write(b"no ")
    if addexc:
        tn.write(b"ip dhcp excluded-address " + str.encode(fro) + b" " + str.encode(to) + b"\r\n")
    tn.write(b"ip dhcp pool " + str.encode(pool) + b"\r\n")
    if no:  # if delete
        tn.write(b"no ")
    if addnet:
        tn.write(b"network " + str.encode(net) + b" " + str.encode(mask) + b"\r\n")
    if no:  # if delete
        tn.write(b"no ")
    if adddefault:
        tn.write(b"default-router " + str.encode(default) + b"\r\n")
    if no:  # if delete
        tn.write(b"no ")
    if adddns:
        tn.write(b"dns-server " + str.encode(dns) + b"\r\n")
    time.sleep(1)
    # out = tn.read_very_eager().decode("ascii")
    tn.close()

def showDHCP(tn):
    tn.write(b"\r\nshow ip dhcp pool\r\n")
    time.sleep(1)
    tn.write(b" " + b" " + b" " + b" ")
    tn.read_until(b"#")
    out = tn.read_very_eager().decode("ascii")
    return out

def showver(tn):
    tn.write(b"\r\nshow ver\r\n")
    tn.write(b" ")
    time.sleep(1)
    out = tn.read_very_eager().decode("ascii")
    out = out[out.find("@cisco.com")+15:out.find("Configuration")-3]
    tn.close()
    return out

def showroutes(tn):
    tn.write(b"\r\nshow run | section ip route\r\n")
    time.sleep(1)
    tn.read_until(b"#")
    out = tn.read_very_eager().decode("ascii")
    return out

def showinterfaces(tn):
    tn.write(b"\r\nshow run | section int\r\n")
    time.sleep(1)
    tn.write(b" " + b" " + b" " + b" ")
    time.sleep(1)
    tn.write(b" " + b" " + b" " + b" ")
    tn.read_until(b"#")
    out = tn.read_very_eager().decode("ascii")
    return out

def showarp(tn):
    tn.write(b"\r\nshow arp\r\n")
    time.sleep(1)
    tn.write(b" " + b" " + b" " + b" ")
    tn.read_until(b"#")
    out = tn.read_very_eager().decode("ascii")
    return out

def showIPPROTO(tn):
    tn.write(b"\r\nshow ip protocols\r\n")
    time.sleep(1)
    tn.write(b" " + b" " + b" " + b" ")
    tn.read_until(b"#")
    out = tn.read_very_eager().decode("ascii")
    return out

def showrun(tn):
    tn.write(b"\r\nshow run\r\n")
    time.sleep(1)
    tn.write(b" "+b" "+b" "+b" ")
    time.sleep(1)
    tn.write(b" "+b" "+b" "+b" ")
    time.sleep(0.5)
    tn.read_until(b"#")
    out = tn.read_very_eager().decode("ascii")
    return out

def showvlan(tn):
    tn.write(b"\r\nshow vlan brief\r\n")
    time.sleep(1)
    tn.write(b" " + b" " + b" " + b" ")
    tn.read_until(b"#")
    out = tn.read_very_eager().decode("ascii")
    return out
# kk = staticroute(conection("cisco","cisco","1.1.1.50"),"10.0.0.0","255.255.255.0","10.0.1.1","50").decode("ascii")
# print(kk)

# #print(conection("kl","kl","1.1.1.50",0))
#confospf(conection("cisco","cisco","cisco","1.1.1.50"),"1","0.0.0.0","0.0.0.0","0")
# # hostname = gethostname(conection("cisco","cisco","1.1.1.50"))
#print(interfaceConfig(conection("cisco","cisco","cisco","1.1.1.200"),"ethernet 0/0","","","","access","20","no",False,False,True,True,True))