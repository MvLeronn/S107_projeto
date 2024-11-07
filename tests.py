import unittest
import atendimentoService

class TestAtendimentoClass(unittest.TestCase):
    def verificarNomeProfessorPredioUm(self):
        atendimento = atendimentoService(horarios.PREDIO1)
        self.assertEqual(atendimento.getNomeProfessor, 'Chris Lima')
    
if __name__ == '__main__':
    unittest.main()