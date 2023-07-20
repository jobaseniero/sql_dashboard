
from odoo import models, fields, api


class DashboardMain(models.Model):
    _name = 'dashboard.main'
    _description = 'SQL Dashboard'

    number = fields.Char('Number')
    subject = fields.Text('Subject')
    status = fields.Selection([
          ('open', 'Open'),
          ('close', 'Close'),
          ('resolved', 'Resolved'),
          ('archived', 'Archived'),
          ('deleted', 'Deleted'),
          ], string='Status', default='open')
    
    ticket_creator = fields.Char('Ticket Creator')
    team_name = fields.Char('Team Name')
    firstname = fields.Char('First Name')
    lastname = fields.Char('Last Name')

