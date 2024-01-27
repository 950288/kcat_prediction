from zeep import Client
import hashlib
import os

prev_path = os.getcwd()

output_path = os.path.join(prev_path, "./data_collecting/output")

os.chdir(output_path)

wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"

email = "xxxx@gmail.com"

password = "yourpassword"

password = hashlib.sha256(password.encode("utf-8")).hexdigest()

credentials = (email, password)

client = Client(wsdl)

ECstring = client.service.getEcNumbersFromTurnoverNumber(*credentials)
print(ECstring)

# for EC in ECstring:
#     print(EC)
#     client.service.getTurnoverNumber(*credentials,"ecNumber*" + EC, "turnoverNumber*", "turnoverNumberMaximum*", "substrate*", "commentary*", "organism*", "ligandStructureId*", "literature*")
#     # KcatString = [{'EC': Kcat['EC'],'substrate': Kcat['substrate'], 'Kcat': Kcat['turnoverNumber']} for Kcat in KcatString]
#     print(KcatString)

# print (ECstring)

# if resultString:
#     fid = open("output.txt","w")
#     fid.write(str(resultString))
#     fid.close()

