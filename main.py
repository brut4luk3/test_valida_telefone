import unittest
import requests
import json
from reportlab.pdfgen import canvas

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'  # Coloque a URL correta da sua API
        self.test_data = [
            # Argentina
            {'telefone': '+5491112345678'},
            {'telefone': '+5492219876543'},
            {'telefone': '+5491165432198'},
            # Bolívia
            {'telefone': '+59171234567'},
            {'telefone': '+59176234567'},
            {'telefone': '+59167234567'},
            # Brasil
            {'telefone': '+5511987654321'},
            {'telefone': '+5511912345678'},
            {'telefone': '+5511976543210'},
            # Chile
            {'telefone': '+56912345678'},
            {'telefone': '+56987654321'},
            {'telefone': '+56945678912'},
            # Colômbia
            {'telefone': '+573123456789'},
            {'telefone': '+573987654321'},
            {'telefone': '+573214365870'},
            # Costa Rica
            {'telefone': '+50612345678'},
            {'telefone': '+50698765432'},
            {'telefone': '+50674125896'},
            # Cuba
            {'telefone': '+5351234567'},
            {'telefone': '+5359876543'},
            {'telefone': '+5354567891'},
            # República Dominicana
            {'telefone': '+18091234567'},
            {'telefone': '+18291234567'},
            {'telefone': '+18091234567'},
            # Equador
            {'telefone': '+59391234567'},
            {'telefone': '+59381234567'},
            {'telefone': '+59371234567'},
            # Guatemala
            {'telefone': '+50212345678'},
            {'telefone': '+50298765432'},
            {'telefone': '+50274125896'},
            # Honduras
            {'telefone': '+50412345678'},
            {'telefone': '+50498765432'},
            {'telefone': '+50474125896'},
            # México
            {'telefone': '+5211234567890'},
            {'telefone': '+5219876543210'},
            {'telefone': '+5217418529630'},
            # Nicarágua
            {'telefone': '+50512345678'},
            {'telefone': '+50598765432'},
            {'telefone': '+50574125896'},
            # Panamá
            {'telefone': '+50761234567'},
            {'telefone': '+50761234567'},
            {'telefone': '+50761234567'},
            # Paraguai
            {'telefone': '+595961234567'},
            {'telefone': '+595961234567'},
            {'telefone': '+595961234567'},
            # Peru
            {'telefone': '+51912345678'},
            {'telefone': '+51998765432'},
            {'telefone': '+51974125896'},
            # Porto Rico
            {'telefone': '+17871234567'},
            {'telefone': '+17871234567'},
            {'telefone': '+17871234567'},
            # Uruguai
            {'telefone': '+59891234567'},
            {'telefone': '+59881234567'},
            {'telefone': '+59871234567'},
            # Venezuela
            {'telefone': '+584121234567'},
            {'telefone': '+584198765432'},
            {'telefone': '+584174825963'},
        ]

    def test_valida_telefone(self):
        pdf = canvas.Canvas('relatorio.pdf')
        y = 700  # Posição inicial da primeira linha do relatório

        for i, data in enumerate(self.test_data):
            response = requests.post(f'{self.base_url}/api/valida_telefone_latam', json=data)
            result = json.loads(response.content)

            telefone = data['telefone']
            valid = result['valid']
            region = result['regiao']

            region_name = {
                'AR': 'Argentina',
                'BO': 'Bolívia',
                'BR': 'Brasil',
                'CL': 'Chile',
                'CO': 'Colômbia',
                'CR': 'Costa Rica',
                'CU': 'Cuba',
                'DO': 'República Dominicana',
                'EC': 'Equador',
                'GT': 'Guatemala',
                'HN': 'Honduras',
                'MX': 'México',
                'NI': 'Nicarágua',
                'PA': 'Panamá',
                'PY': 'Paraguai',
                'PE': 'Peru',
                'PR': 'Porto Rico',
                'UY': 'Uruguai',
                'VE': 'Venezuela'
            }.get(region, 'Desconhecida')

            pdf.drawString(100, y, f'Região: {region_name}')
            pdf.drawString(100, y - 20, f'Telefone: {telefone}')
            pdf.drawString(100, y - 40, f'Válido: {valid}')
            pdf.line(50, y - 50, 550, y - 50)  # Linha horizontal

            y -= 70  # Espaçamento vertical entre os testes

            if y <= 50:
                pdf.showPage()
                y = 700  # Reinicia a posição vertical na nova página

        pdf.save()

if __name__ == '__main__':
    unittest.main()