from odoo import models, fields

class Patient(models.Model):
    _name = "hms.patient"
    _rec_name = "first_name"
    _description = "Hospital Management Patient"

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    birth_date = fields.Date(string="Birth Date")
    history = fields.Text(string="Medical History")
    cr_ratio = fields.Float(string="CR Ratio")
    blood_type = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ], string="Blood Type")
    pcr = fields.Boolean(string="PCR Test")
    image = fields.Image(string="Image")
    address = fields.Char(string="Address")
    age = fields.Integer(string="Age")
    department_id = fields.Many2one(comodel_name="hms.department", string="Department")
    department_capacity = fields.Integer(string="Department Capacity", related="department_id.capacity")
    doctor_id = fields.Many2many(comodel_name="hms.doctor", string="Doctor")