# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Purchase - Manual Currency",
    "version": "17.0.1.0.0",
    "category": "Purchase Management",
    "summary": "Allows to manual currency of Purchase",
    "author": "Ecosoft, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/purchase-workflow",
    "license": "AGPL-3",
    "depends": ["purchase", "account_manual_currency"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/purchase_views.xml",
    ],
    "installable": True,
    "maintainer": ["Saran440"],
}
