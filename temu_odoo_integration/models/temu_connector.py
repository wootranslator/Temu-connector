from odoo import models, fields, api

class TemuConnector(models.Model):
    _name = 'temu.connector'
    _description = 'Temu Connector Configuration'

    name = fields.Char(string='Name', required=True)
    client_id = fields.Char(string='Client ID', required=True)
    client_secret = fields.Char(string='Client Secret', required=True, groups="base.group_system")
    access_token = fields.Char(string='Access Token', groups="base.group_system")
    environment = fields.Selection([
        ('production', 'Production'),
        ('sandbox', 'Sandbox'),
    ], string='Environment', default='sandbox', required=True)
    auto_confirm_paid_orders = fields.Boolean(string='Auto-confirm Paid Orders', default=False, help="Automatically confirm sale orders if a valid payment transaction is found.")
    api_url = fields.Char(string='API URL', compute='_compute_api_url', store=True, readonly=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], string='Status', default='draft')

    @api.depends('environment')
    def _compute_api_url(self):
        for record in self:
            if record.environment == 'production':
                record.api_url = 'https://open-api.temu.com'
            else:
                record.api_url = 'https://open-api.temu-sandbox.com'

    def action_confirm(self):
        self.state = 'confirmed'

    def action_draft(self):
        self.state = 'draft'
