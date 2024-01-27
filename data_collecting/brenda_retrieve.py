from zeep import Client
import hashlib
import os
import time

prev_path = os.getcwd()

output_path = os.path.join(prev_path, "./data_collecting/output")

os.chdir(output_path)

wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"

email = "xxxx@gmail.com"

password = "yourpassword"

password = hashlib.sha256(password.encode("utf-8")).hexdigest()

credentials = (email, password)

client = Client(wsdl)

EClist = client.service.getEcNumbersFromTurnoverNumber(*credentials)
print(EClist)

# time.sleep(1)

# while succes < 10:
#     try:
#         Kcat = client.service.getTurnoverNumber(*credentials,"ecNumber*3.6.1.56", "turnoverNumber*", "substrate*", "organism*")
#         print(Kcat)
#         succes = 10
        
#     except:
#         time.sleep(1)
#         succes += 1

for ECnumber in EClist:
    print(ECnumber)
    client.service.getTurnoverNumber(*credentials,"ecNumber*" + ECnumber, "turnoverNumber*", "turnoverNumberMaximum*", "substrate*", "commentary*", "organism*", "ligandStructureId*", "literature*")
    print(KcatString)

# print (ECstring)

# if resultString:
#     fid = open("output.txt","w")
#     fid.write(str(resultString))
#     fid.close()

