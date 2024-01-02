# Copyright (C) Softhealer Technologies.
from odoo import fields, models

class ResConfigSettiongsInhert(models.TransientModel):
    _inherit = "res.config.settings"

    pos_sh_display_change_in_receipt = fields.Boolean(
        related="pos_config_id.sh_display_change_in_receipt", readonly=False)