from zeep import Client
from zeep.wsse.username import UsernameToken

client = Client(<wsdl_url>, wsse=UsernameToken(<username>, <password>)
