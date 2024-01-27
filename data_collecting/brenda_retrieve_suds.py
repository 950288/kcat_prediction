from suds.client import Client
from suds.transport.https import HttpAuthenticated
import hashlib
import os

prev_path = os.getcwd()

output_path = os.path.join(prev_path, "./data_collecting/output")

os.chdir(output_path)

wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"

email = "xxxx@gmail.com"

password = "yourpassword"

password = hashlib.sha256(password.encode("utf-8")).hexdigest()

print(password)

credentials = (email, password)

client = Client(wsdl)
# print(client)
parameters = (*credentials ,"ecNumber*1.1.1.1","organism*Homo sapiens","kmValue*",
              "kmValueMaximum*","substrate*","commentary*","ligandStructureId*","literature*" )
resultString = client.service.getKmValue(*parameters)

print (resultString)

ECstring = client.service.getEcNumbersFromTurnoverNumber(*credentials)
print(ECstring)

# for EC in ECstring:
#     print(EC)
#     result = client.service.getTurnoverNumber(*credentials,"ecNumber*"+EC, "turnoverNumber*", "turnoverNumberMaximum*", "substrate*", "commentary*", "organism*", "ligandStructureId*", "literature*")
#     # KcatString = [{'EC': Kcat['EC'],'substrate': Kcat['substrate'], 'Kcat': Kcat['turnoverNumber']} for Kcat in result]
#     print(KcatString)
