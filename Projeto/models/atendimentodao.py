import json
from datetime import datetime
from models.atendimento import Atendimento

class AtendimentoDAO:
    def __init__(self):
        self.arquivo = "atendimentos.json"

    def abrir(self):
        objetos = []
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                lista_dict = json.load(f)
                for d in lista_dict:
                    try:
                        dt = datetime.strptime(d["data"], "%d/%m/%Y %H:%M")
                    except Exception:
                        dt = d["data"]
                    
                    obj = Atendimento(
                        d["id"],
                        dt,
                        d["queixa_principal"],
                        d["historico_saude"],
                        d["avaliacao"],
                        d["prescricao"],
                        d["id_horario"]
                    )
                    objetos.append(obj)
        except FileNotFoundError:
            pass
        return objetos

    def salvar(self, objetos):
        lista_dict = []
        for obj in objetos:
            data_val = obj.get_data()
            if isinstance(data_val, datetime):
                data_val = data_val.strftime("%d/%m/%Y %H:%M")
            
            dict_obj = {
                "id": obj.get_id(),
                "data": data_val,
                "queixa_principal": obj.get_queixa_principal(),
                "historico_saude": obj.get_historico_saude(),
                "avaliacao": obj.get_avaliacao(),
                "prescricao": obj.get_prescricao(),
                "id_horario": obj.get_id_horario()
            }
            lista_dict.append(dict_obj)
            
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(lista_dict, f, ensure_ascii=False, indent=4)

    def inserir(self, obj):
        objetos = self.abrir()
        id = 1
        if len(objetos) > 0:
            id = max(a.get_id() for a in objetos) + 1
        obj.set_id(id)
        objetos.append(obj)
        self.salvar(objetos)

    def listar(self):
        return self.abrir()

    def listar_id(self, id):
        objetos = self.abrir()
        for a in objetos:
            if a.get_id() == id:
                return a
        return None

    def atualizar(self, obj):
        objetos = self.abrir()
        for i, a in enumerate(objetos):
            if a.get_id() == obj.get_id():
                objetos[i] = obj
                break
        self.salvar(objetos)

    def excluir(self, obj):
        objetos = self.abrir()
        objetos = [a for a in objetos if a.get_id() != obj.get_id()]
        self.salvar(objetos)