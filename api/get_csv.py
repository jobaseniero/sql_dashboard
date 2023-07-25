import csv
import xmlrpc.client
from datetime import datetime

url='http://172.22.0.3:8069'
db = 'erp.obanana.com'
username = 'jobaseniero@gmail.com'
password = 'Obanana2023'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
if uid:
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    model_name = 'dashboard.main'
    
    # Get a list of all record ids in the model
    record_ids = models.execute_kw(db, uid, password, model_name, 'search', [[]])
    
    # Delete each record using the unlink method
    for record_id in record_ids:
        models.execute_kw(db, uid, password, model_name, 'unlink', [[record_id]])

    with open('/home/obananapay/erp/addons/sql_dashboard/api/export.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            print("....row.....", row)
            status = 'open' if row[2] == 'Open' else 'close'
            date_created_str = row[8]  # Assuming date_created is in the 9th column (index 8)
            date_created = datetime.strptime(date_created_str, '%Y/%m/%d').strftime('%Y-%m-%d')
            vals = {
                'number': row[0],
                'subject': row[1],
                'status': status,
                'ticket_priority': row[3],
                'ticket_creator': row[4],
                'team_name': row[5],
                'firstname': row[6],
                'lastname': row[7],
                'date_created': date_created
            }

            created_id = models.execute_kw(db, uid, password, model_name, 'create', [vals])
            print("created record ->", created_id)


