# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    sh_display_change_in_receipt = fields.Boolean(
        "Display Change In Receipt ?")
