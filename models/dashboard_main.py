from datetime import datetime
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
    
    ticket_priority = fields.Selection([
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('emergency', 'Emergency'),
        ], string='Ticket Priority', default='low')

    ticket_creator = fields.Char('Ticket Creator')
    team_name = fields.Char('Team Name')
    firstname = fields.Char('First Name')
    lastname = fields.Char('Last Name')
    date_created = fields.Date('Date Created')

    days_since_creation = fields.Integer(
        compute='_compute_days_since_creation',
        string='Days Since Creation',
    )

    creation_date_group = fields.Selection([
        ('today', 'Today'),
        ('this_week', 'This Week'),
        ('this_month', 'This Month'),
        ('three_months', '3 Months'),
        ('three_plus_months', '3+ Months'),
    ], compute='_compute_creation_date_group', string='Creation Date Group', store=True)

    @api.depends('date_created')
    def _compute_days_since_creation(self):
        for record in self:
            if record.date_created:
                # Get today's date
                today = datetime.now().date()

                # Calculate the difference in days
                creation_date = fields.Datetime.from_string(record.date_created).date()
                difference = (today - creation_date).days

                record.days_since_creation = difference
            else:
                record.days_since_creation = 0
    
    @api.depends('days_since_creation')
    def _compute_creation_date_group(self):
        for record in self:
            if record.days_since_creation == 0:
                record.creation_date_group = 'today'
            elif 1 <= record.days_since_creation <= 7:
                record.creation_date_group = 'this_week'
            elif 8 <= record.days_since_creation <= 30:
                record.creation_date_group = 'this_month'
            elif 31 <= record.days_since_creation <= 90:
                record.creation_date_group = 'three_months'
            else:
                record.creation_date_group = 'three_plus_months'

