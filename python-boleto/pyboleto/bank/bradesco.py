# -*- coding: utf-8 -*-
"""
    pyboleto.bank.bradesco
    ~~~~~~~~~~~~~~~~~~~~~~

    Lógica para boletos do banco Bradesco.

    :copyright: © 2011 - 2012 by Eduardo Cereto Carvalho
    :license: BSD, see LICENSE for more details.

"""
from pyboleto.data import BoletoData, CustomProperty


class BoletoBradesco(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Bradesco
    '''

    nosso_numero = CustomProperty('nosso_numero', 11)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 7)

    def __init__(self):
        super(BoletoBradesco, self).__init__()

        self.codigo_banco = "237"
        self.logo_image = "logo_bancobradesco.jpg"
        self.carteira = '06'
        self.local_pagamento = 'Pagável Preferencialmente ' +\
            'na Rede Bradesco ou Bradesco Expresso.'

    def format_nosso_numero(self):
        return "%s/%s-%s" % (
            self.carteira,
            self.nosso_numero,
            self.dv_nosso_numero
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
        return dv

    @property
    def campo_livre(self):
        content = '{0:.4}{1:.2}{2:.11}{3:.7}{4:.1}'.format(
            self.agencia_cedente.split('-')[0],
            self.carteira.zfill(2),
            self.nosso_numero.zfill(11),
            self.conta_cedente.split('-')[0],
            '0'
            )
        return content
