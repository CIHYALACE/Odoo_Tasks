from odoo import models, fields

class Doctors(models.Model):
    _name = "hms.doctor"
    _rec_name = "first_name"
    _description = "Hospital Management Doctors"

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    Image = fields.Image(string="Image")
    patient_id = fields.Many2many(comodel_name="hms.patient", string="Patient")