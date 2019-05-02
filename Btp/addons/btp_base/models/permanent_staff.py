# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PermanentStaff(models.Model):
    _name = 'btp_base.permanent_staff'

    code = fields.Char('Code', copy=False, size=16)
    name = fields.Char('Nom', required=True)
    monthly_pay = fields.Float('Salaire mensuel', required=True)
    profession_id = fields.Many2one('btp_base.profession', string='Profession', required=True)

    _sql_constraints = [
        ('code_uniq', 'unique(code)', "Ce code existe déjà.\n Veuillez choisir un autre code pour continuer!"),
    ]

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('btp_base.permanent_staff')
        permanent_staff = super(PermanentStaff, self).create(vals)
        return permanent_staff

    @api.multi
    @api.depends('code')
    def name_get(self):
        result = []
        for employee in self:
            result.append((employee.id, '%s' % (employee.code )))
        return result

    @api.one
    @api.constrains('monthly_pay')
    def _check_monthly_pay(self):
        if self.monthly_pay <= 0:
            raise ValidationError("Attention, le salaire de l'employé(e) doit être strictement positif\n Veuillez corriger pour continuer!.")