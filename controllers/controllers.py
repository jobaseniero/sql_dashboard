# -*- coding: utf-8 -*-
# from odoo import http


# class SqlDashboard(http.Controller):
#     @http.route('/sql_dashboard/sql_dashboard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sql_dashboard/sql_dashboard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sql_dashboard.listing', {
#             'root': '/sql_dashboard/sql_dashboard',
#             'objects': http.request.env['sql_dashboard.sql_dashboard'].search([]),
#         })

#     @http.route('/sql_dashboard/sql_dashboard/objects/<model("sql_dashboard.sql_dashboard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sql_dashboard.object', {
#             'object': obj
#         })
