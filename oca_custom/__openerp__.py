# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today: Odoo Community Association (OCA)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'OCA Custom Settings',
    'summary': 'Custom Settings for OCA Instance',
    'version': '10.0.0.0.0',
    'category': 'Custom',
    'author': [
        'GRAP',
        'Akretion',
        'Odoo Community Association (OCA)',
    ],
    'depends': [
        'github_connector',
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'installable': True,
}
