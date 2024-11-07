import json
from atendimento import Atendimento

def montarAtendimento(predio):
    json_atendimento = json.loads(predio)
    nomeProfessor = json_atendimento['nomeDoProfessor']
    horarioDeAtendimento = json_atendimento['horarioDeAtendimento']
    periodo = json_atendimento['periodo']
    sala = json_atendimento['sala']
    predio = json_atendimento['predio']
    info = json_atendimento['info']
    atendimentoPredio = Atendimento(nomeProfessor, horarioDeAtendimento, periodo, sala, predio, info)
    return atendimentoPredio