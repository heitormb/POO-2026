from models.convenio import Convenio
from models.dao import DAO
import json

class ConvenioDAO(DAO):
    def __init__(self):
        super().__init__("convenios.json")

    def _abrir(self):  
        try:  
            arquivo = open(self._arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = Convenio.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def _salvar(self):    
        arquivo = open(self._arquivo, mode = "w")
        json.dump(self._objetos, arquivo, default = Convenio.to_json, indent = 2)
        arquivo.close()