# -*- coding: utf-8 -*-

from openerp import models


class mailserver(models.Model):
    """"""

    _name = 'infrastructure.mailserver'
    _description = 'mailserver'
    _inherit = ['ir.mail_server']


mailserver()