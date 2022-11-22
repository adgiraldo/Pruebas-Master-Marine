# Part of Odoo. See LICENSE file for full co
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class InheritStockPicking(models.Model):
    # pass
    _inherit = 'stock.picking'
    # default_supplier = fields.Boolean(name="default supplier")
    
    # @api.onchange('default_supplier')
    # def _check_default_supplier(self):
    #     selected = 0
    #     product_template = self.product_tmpl_id
    #     seller_ids = product_template.seller_ids
    #     for records in seller_ids:
    #         print(records.default_supplier)
    #         if records.default_supplier:
    #             selected += 1
    #     if(selected > 1):
    #         raise ValidationError('to much default suppliers')