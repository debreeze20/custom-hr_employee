# -*- coding: utf-8 -*-
{
    'name': "shofidoodex",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/referensi_penjualan.xml',
        'data/referensi_member.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/jenisbarang_view.xml',
        'views/barang_view.xml',
        'views/manusia_view.xml',
        'views/pelanggan_view.xml',
        'views/karyawan_view.xml',
        'views/bag_kebersihan_view.xml',
        'views/bag_accounting_view.xml',
        'views/bag_kasir_view.xml',
        'views/penjualan_view.xml',
        'views/supplier_view.xml',
        'views/pembelian_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
