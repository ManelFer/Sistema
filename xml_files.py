import os
import xml.etree.ElementTree as Et

class Read_xml():
    def __init__(self, directory):
        self.directory = directory
    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory) if arq.lower().endswith(".xml")]
    

    # leitura do xml
    def nfe_data(self, xml):
        root = Et.parse(xml).getroot()
        nsNfe = {"ns": "http://www.portalfiscal.inf.br/nfe"}

        #dados da nfe
        Nfe = self.check_none(root.find("./ns:NFe/ns:infNfe/ns:ide/ns:nNF",nsNfe))
        serie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:serie", nsNfe)) #2
        data_emissao = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhEmi", nsNfe))
        data_emissao = F"{data_emissao[8:10]}/{data_emissao[5:7]}/{data_emissao[:4]}"
    
    #
    def check_none(self, var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace('.',',')
            except:
                return var.text

    def format_cnpj(self, cnpj):
        try:
            # formatação de um cnpj
            cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]} - {cnpj[12:14]}'
            return cnpj
        except:
            return