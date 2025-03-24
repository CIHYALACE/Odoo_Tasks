from odoo import models, fields

class Department(models.Model):
    _name = "hms.department"
    _rec_name = "name"
    _description = "Hospital Management Department"

    name = fields.Char(string="Name")
    capacity = fields.Integer(string="Capacity")
    is_opened = fields.Boolean(string="Is Opened")
    patient_ids = fields.One2many(comodel_name="hms.patient", inverse_name="department_id", string="Patients")