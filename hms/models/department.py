from odoo import models, fields

class Department(models.Model):
    _name = "hms.department"
    _rec_name = "name"

    name = fields.Char(string="Name")
    capacity = fields.Integer(string="Capacity")
    is_opened = fields.Boolean(string="Is Opened")
    patients = fields.One2many(comodel_name="hms.patient", inverse_name="department_id", string="Patients")