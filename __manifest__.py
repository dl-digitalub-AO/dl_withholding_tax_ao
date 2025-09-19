{
    'name': 'Retenção na Fonte Angola',
    'version': '15.0.1.0.0',
    'summary': 'Gestão de Retenção na Fonte (Angola)',
    'description': """
Módulo para suportar Retenção na Fonte em Angola.
- Configuração de retenções
- Aplicação em faturas
- Impressão em faturas e recibos
    """,
    'author': 'DIGITALUB ANGOLA',
    'website': 'https://digitalub.ao',
    'category': 'Accounting',
    'depends': ['account', 'opc_certification_ao'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/withholding_tax_data.xml',
        'views/withholding_tax_views.xml',
        'views/account_move_views.xml',
        'views/res_partner_views.xml',
        'views/withholding_report_wizard_views.xml',
        'report/reports.xml',
        'report/report_withholding.xml',
        'report/report_payment_receipt.xml',
    ],
    'installable': True,
    'application': True,
}