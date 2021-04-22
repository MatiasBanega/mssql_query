{

     'name': "MS SQL Query",
     'author': "Fasil",
     'version': '0.1',
     'sequence': -1,
     'website': 'https://www.malludynamics.com',
     'summary': """
             Designed by Fasil""",
     'description': """
             
         """,
     'depends': ['base'],
     'data': [
         'security/ir.model.access.csv',
         'security/security.xml',
         'views/mssql_query.xml',
     ],
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False,

}