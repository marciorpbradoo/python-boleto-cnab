# -*- coding: utf-8 -*-
"""
    pyboleto.bank.bankofamerica
    ~~~~~~~~~~~~~~~~~~~~~~

    Lógica para boletos do banco Bank Of America.

    :copyright: © 2011 - 2012 by Eduardo Cereto Carvalho
    :license: BSD, see LICENSE for more details.

"""
from pyboleto.data import BoletoData, CustomProperty


class BoletoBankOfAmerica(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Bank Of America
    '''

    nosso_numero = CustomProperty('nosso_numero', 11)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 7)
#     numero_conveio = CustomProperty('numero_convenio', 10)
    

    def __init__(self):
        super(BoletoBankOfAmerica, self).__init__()

        self.codigo_banco = "755"
        self.logo_image = "logo_bankofamerica.jpg"
        self.carteira = '02'
        self.local_pagamento = 'PAGAVEL EM QUALQUER BANCO ATE O VENCIMENTO'

    def format_nosso_numero(self):
        print "passou format_nosso_numero"
        return "%s" % (
            str(self.nosso_numero[1:len(self.nosso_numero)-1] + "024")
        )


    @property
    def dv_nosso_numero(self):
        resto2 = self.modulo11(self.carteira + self.nosso_numero, 7, 1)
        digito = 11 - resto2
        if digito == 10:
            dv = 'P'
        elif digito == 11:
            dv = 0
        else:
            dv = digito
        return ''

    @property
    def campo_livre(self):
#         content = '{0:.10}{2:.11}{3:.7}{4:.1}'.format(
#             #self.numero_convenio[0],
#             "0349026921")
#             self.nosso_numero.zfill(11),
#             self.conta_cedente.split('-')[0],
#             )
        print self.nosso_numero
        content = "000349026921" + self.nosso_numero[1:-1] + "024"
        return content
