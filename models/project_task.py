# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

PRIORITY_RANGE = [(str(i), str(i)) for i in range(1, 11)]
DEVELOPER_GROUP = "development_project.group_development_project_developer"


class Task(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    @api.depends()
    def _compute_currency(self):
        for task in self:
            curr = task.create_uid.company_id.currency_id or self.env.user.company_id.currency_id
            task.currency_id = curr

    developer_ids = fields.Many2many(
        string="Developer", comodel_name="res.users", relation="res_users_project_task_rel",
        domain=lambda self: [("groups_id", "in", self.env.ref(DEVELOPER_GROUP).id)])
    custom_priority = fields.Selection(PRIORITY_RANGE, string="Priority", default="1")
    bonus = fields.Float(string="Bonus")
    bonus_deadline = fields.Datetime(string="Bonus deadline")
    estimated_total_hours = fields.Integer(string="Estimated total hours")
    estimated_expense = fields.Float(string="Estimated expense")
    estimated_income = fields.Float(string="Estimated income")
    currency_id = fields.Many2one("res.currency", compute="_compute_currency", string="Currency")
