# -*- coding: utf-8 -*-
from openerp import fields, models, api, _

class AduanasTiposTransporte(models.Model):
    _name = 'aduanas.tipos_transporte'

    name = fields.Char(
            string= 'Nombre',
        )
    code = fields.Char(
            string="Código",
        )
