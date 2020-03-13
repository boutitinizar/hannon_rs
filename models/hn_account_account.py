from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class KSResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ks_enable_discount = fields.Boolean(string="Retenue à la source")
    ks_sales_discount_account = fields.Many2one('account.account',
                                                string="RS Vente")
    ks_purchase_discount_account = fields.Many2one('account.account',
                                                   string="RS Achat")
    ks_accounting_present = fields.Boolean(compute='ks_check_charts_of_accounts')
    hn_amount_rs = fields.Float(string="Montant %")


    def get_values(self):
        ks_res = super(KSResConfigSettings, self).get_values()
        ks_res.update(
            ks_enable_discount=self.env['ir.config_parameter'].sudo().get_param('ks_enable_discount'),
            ks_sales_discount_account=int(self.env['ir.config_parameter'].sudo().get_param('ks_sales_discount_account')),
            ks_purchase_discount_account=int(self.env['ir.config_parameter'].sudo().get_param('ks_purchase_discount_account')),
            hn_amount_rs=float(self.env['ir.config_parameter'].sudo().get_param('hn_amount_rs')),

        )
        return ks_res

    def set_values(self):
        super(KSResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('ks_enable_discount', self.ks_enable_discount)
        if self.ks_enable_discount:
            self.env['ir.config_parameter'].set_param('hn_amount_rs', self.hn_amount_rs)
            self.env['ir.config_parameter'].set_param('ks_sales_discount_account',
                                                      self.ks_sales_discount_account.id)
            self.env['ir.config_parameter'].set_param('ks_purchase_discount_account',
                                                      self.ks_purchase_discount_account.id)