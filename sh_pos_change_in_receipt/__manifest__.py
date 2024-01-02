# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

{
    "name": "POS Change Display In Receipt | POS Change Amount Display In Receipt Screen",
    "version": "16.0.1",
    "category": "Point of Sale",
    "license": "OPL-1",
    "depends": ['base', 'sale', 'point_of_sale'],
    'author': 'Softhealer Technologies',
    'website': 'https://www.softhealer.com',
    "support": "support@softhealer.com",
    'summary': "POS Change Display In Receipt,Point Of Sale Change Amount Display In Receipt,Visible Change Amount In Receipt,Change Amount Receipt,Order Change Amount Display,Point Of Sale Change Display In Receipt,Change In Receipt Screen Odoo",
    "description": """Currently in odoo pos when a customer gives order amount possible amount more so in that case we need to give a change to the customer. change amount currently visible at payment screen but once payment proceeds and pos screen change to receipt screen that time we can not find how much change needs to give to a customer. So this module makes pos cashier work easy to remember how much change needs to give to the customer.""",

    "data": [
        'views/res_config_settings.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'sh_pos_change_in_receipt/static/src/css/pos.css',
            'sh_pos_change_in_receipt/static/src/xml/receipt_screen.xml',
        ],
       
    },
    "images": ['static/description/background.png'],
    "auto_install": False,
    "installable": True,
    "price": 20,
    "currency": "EUR"
}
