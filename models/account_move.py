from odoo import api, fields, models, _

class AccountMoveInherit(models.Model):
    _name = "account.move"
    _inherit = 'account.move'

    invoicing_type = fields.Selection(selection=[
            ('services', 'Services'),
            ('mdc', 'Mobilization and Demobilization Charges'),
            ('mds', 'Missing and Damage Sales'),
    ], string='Invoice Type', store=True, readonly=False, copy=True)

    job_order = fields.Many2one('sale.order', required=True)

    name_order = fields.Char(related='job_order.partner_id.name', store=True)

    gstn = fields.Char(related='job_order.customer_branch.gstn', store=True)

    godown = fields.Char(related='job_order.godown.name', store=True)

    @api.onchange('job_order')
    def partner_id_add(self):
        self.partner_id = self.job_order.partner_id

    # @api.onchange('name')
    # def return_customer(self):
    #     self.partner_id = self.env['sale.order'].search([('job_order', '=', self.name)]).partner_id