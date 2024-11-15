import unittest
import atendimentoService
import horarios
import json
import HtmlTestRunner

class TestAtendimentoClass(unittest.TestCase):
    def test_nome_professor_predio_um(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO1)
        self.assertEqual(atendimentoPredio.getNomeProfessor(), 'Chris Lima')
        
    def test_nome_professor_predio_dois(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO2)
        self.assertEqual(atendimentoPredio.getNomeProfessor(), 'Renzo Mesquita')
        
    def test_horario_atendimento_predio_um(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO1)
        self.assertEqual(atendimentoPredio.getHorarioAtendimento(), 'Segunda:17:30')
            
    def test_horario_atendimento_predio_tres(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO3)
        self.assertEqual(atendimentoPredio.getHorarioAtendimento(), 'Segunda:13:30')
    
    def test_periodo_atendimento_predio_quatro(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO3)
        self.assertEqual(atendimentoPredio.getPeriodo(), 'integral')
            
    def test_periodo_atendimento_predio_seis(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO6)
        self.assertEqual(atendimentoPredio.getPeriodo(), 'noturno')
        
    def test_sala_atendimento_predio_quatro(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO4)
        self.assertEqual(atendimentoPredio.getSala(), '18')
    
    def test_sala_atendimento_predio_um(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO1)
        self.assertEqual(atendimentoPredio.getSala(), '1')
        
    def test_numero_predio_seis(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO6)
        predios = atendimentoPredio.getPredio()
        self.assertEqual(predios[0], '6')
        
    def test_mensagem_sucesso(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.PREDIO6)
        self.assertEqual(atendimentoPredio.getInfo(), 'success')
    
    def test_numero_grande(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.NUMERO_MAIOR)
        self.assertEqual(atendimentoPredio.getInfo(), 'Número deve ser menor que 25!')
        
    def test_numero_grande(self):
        atendimentoPredio = atendimentoService.montarAtendimento(horarios.NUMERO_MENOR)
        self.assertEqual(atendimentoPredio.getInfo(), 'Número deve ser maior que 1!')
        
    def test_json_invalido(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            atendimentoPredio = atendimentoService.montarAtendimento("{\"nomeDoProfessor\": \"Chris Lima\", \"horarioDeAtendimento\": \"Segunda:17:30\"")
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_report'))