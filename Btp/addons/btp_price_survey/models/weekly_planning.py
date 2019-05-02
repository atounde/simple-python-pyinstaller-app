# -*- coding: utf-8 -*-
from odoo import models, fields, api


class WeeklyPlanning(models.Model):
    _name = 'btp_price_survey.weekly_planning'

    monday_quantity = fields.Float('Lundi', default=0)
    tuesday_quantity = fields.Float('Mardi', default=0)
    wednesday_quantity = fields.Float('Mercredi', default=0)
    thursday_quantity = fields.Float('Jeudi', default=0)
    friday_quantity = fields.Float('Vendredi', default=0)
    saturday_quantity = fields.Float('Samedi', default=0)
    sunday_quantity = fields.Float('Dimanche', default=0)