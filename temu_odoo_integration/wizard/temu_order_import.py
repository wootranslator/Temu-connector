from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class TemuOrderImport(models.TransientModel):
    _name = 'temu.order.import'
    _description = 'Import Orders from Temu'

    connector_id = fields.Many2one('temu.connector', string='Connector', required=True)
    date_from = fields.Datetime(string='Date From')
    date_to = fields.Datetime(string='Date To')

    def _find_or_create_partner(self, order_data):
        """Deduplicate partners by name/email/temu_id (if available)."""
        Partner = self.env['res.partner']
        # In a real API, we might have a temu_partner_id or email
        email = order_data.get('email')
        name = order_data.get('partner_name')
        
        partner = False
        if email:
            partner = Partner.search([('email', '=', email)], limit=1)
        
        if not partner and name:
            partner = Partner.search([('name', '=', name)], limit=1)
            
        if not partner:
            partner = Partner.create({
                'name': name,
                'email': email,
                'is_company': False,
            })
        return partner

    def action_import_orders(self):
        """Main logic to fetch and create orders."""
        self.ensure_one()
        # This is a skeleton logic. In a real scenario, this would call the Temu API service.
        _logger.info("Starting Temu order import for connector %s", self.connector_id.name)
        
        # Simulated API Response
        mock_orders = [
            {
                'order_id': 'TEMU-12345',
                'partner_name': 'Juan Perez',
                'sku': 'PROD-001',
                'qty': 2,
                'price': 15.50,
                'payment_method': 'Credit Card',
                'shipping_method': 'Standard',
                'region': 'ES',
                'transaction_id': 'TXN-998877',
                'payment_status': 'paid',
                'email': 'juan.perez@example.com',
            }
        ]
        
        for order_data in mock_orders:
            # 1. Check if order exists
            existing = self.env['sale.order'].search([('temu_order_id', '=', order_data['order_id'])])
            if existing:
                continue
            
            # 2. Map SKU
            mapping = self.env['temu.mapping.product'].search([
                ('connector_id', '=', self.connector_id.id),
                ('temu_sku', '=', order_data['sku'])
            ], limit=1)
            
            product = mapping.product_id if mapping else self.env['product.product'].search([('default_code', '=', order_data['sku'])], limit=1)
            
            if not product:
                _logger.warning("Product not found for SKU %s", order_data['sku'])
                continue
            
            # 3. Handle Partner (Deduplicated)
            partner = self._find_or_create_partner(order_data)
            
            # 4. Create Sale Order
            sale_order = self.env['sale.order'].create({
                'partner_id': partner.id,
                'temu_order_id': order_data['order_id'],
                'temu_transaction_id': order_data.get('transaction_id'),
                'is_temu_order': True,
                'order_line': [(0, 0, {
                    'product_id': product.id,
                    'product_uom_qty': order_data['qty'],
                    'price_unit': order_data['price'],
                })]
            })
            
            # 5. Handle Fiscal Mapping (Simplified)
            fiscal_mapping = self.env['temu.mapping.fiscal'].search([
                ('connector_id', '=', self.connector_id.id),
                ('temu_region', '=', order_data['region'])
            ], limit=1)
            if fiscal_mapping:
                sale_order.fiscal_position_id = fiscal_mapping.fiscal_position_id
            
            # 6. Handle Shipping Mapping
            shipping_mapping = self.env['temu.mapping.shipping'].search([
                ('connector_id', '=', self.connector_id.id),
                ('temu_shipping_method', '=', order_data['shipping_method'])
            ], limit=1)
            if shipping_mapping:
                sale_order.carrier_id = shipping_mapping.carrier_id.id
            
            # 7. Workflow: Auto-confirm if paid
            if self.connector_id.auto_confirm_paid_orders and order_data.get('payment_status') == 'paid':
                _logger.info("Auto-confirming paid order %s", sale_order.name)
                sale_order.action_confirm()
                
                # Logic to create payment/invoice could go here
                # (Creating a dummy journal entry or payment register if mapping exists)
                self._handle_payment_creation(sale_order, order_data)

    def _handle_payment_creation(self, sale_order, order_data):
        """Register payment if mapping exists."""
        payment_mapping = self.env['temu.mapping.payment'].search([
            ('connector_id', '=', self.connector_id.id),
            ('temu_payment_method', '=', order_data.get('payment_method'))
        ], limit=1)
        
        if payment_mapping:
            # Simulated payment registration
            _logger.info("Registering payment for order %s using journal %s", sale_order.name, payment_mapping.journal_id.name)
            # In Odoo 18, we would create account.payment or bank statement line
            
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Import Complete'),
                'message': _('Orders have been processed.'),
                'sticky': False,
            }
        }
