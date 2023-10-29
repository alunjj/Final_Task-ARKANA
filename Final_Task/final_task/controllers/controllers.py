# -*- coding: utf-8 -*-
# from odoo import http


# class FinalTask(http.Controller):
#     @http.route('/final_task/final_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/final_task/final_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('final_task.listing', {
#             'root': '/final_task/final_task',
#             'objects': http.request.env['final_task.final_task'].search([]),
#         })

#     @http.route('/final_task/final_task/objects/<model("final_task.final_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('final_task.object', {
#             'object': obj
#         })
