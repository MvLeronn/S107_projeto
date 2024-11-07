class Atendimento:
    def __init__(self, nomeProfessor, horarioAtendimento, periodo, sala, predio, info):
        self.nomeProfessor = nomeProfessor
        self.horarioAtendimento = horarioAtendimento
        self.periodo = periodo
        self.sala = sala
        self.predio = predio
        self.info = info
    
    def getNomeProfessor(self):
        return self.nomeProfessor
    
    def getHorarioAtendimento(self):
        return self.horarioAtendimento
    
    def getPeriodo(self):
        return self.periodo
    
    def getSala(self):
        return self.sala
    
    def getInfo(self):
        return self.info
    
    def getPredio(self):
        return self.predio