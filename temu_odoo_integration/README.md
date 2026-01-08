# Temu Odoo 18 Integration

This module integrates Odoo 18 with the Temu marketplace, allowing for seamless order import, product mapping, and shipment tracking.

## Features

- **Order Import**: Automatic and manual import of orders from Temu.
- **Deduplication**: Automatically checks for existing contacts by name or email.
- **Product Mapping**: Map Temu SKUs to Odoo Internal References or Barcodes.
- **Fiscal Mapping**: Map Temu regions to Odoo Fiscal Positions.
- **Payment Mapping**: Map Temu payment methods to Odoo Payment Journals.
- **Shipping Mapping**: Map Temu shipping methods to Odoo Delivery Carriers.
- **Workflow Automation**: Auto-confirm orders that are marked as paid in Temu.
- **Shipment Tracking**: Synchronize tracking numbers from Odoo back to Temu.
- **Sandbox Support**: Test your integration safely using the Temu Sandbox environment.

## Installation

1. Copy this folder into your Odoo `addons` directory.
2. Ensure the `delivery` module is installed in Odoo.
3. Restart Odoo and update the Apps list.
4. Install **Temu Odoo Integration**.

## Configuration

1. Go to **Temu Integration > Configuration > Connectors**.
2. Create a new connector and select the **Environment** (Sandbox or Production).
3. Enter your **Client ID**, **Client Secret**, and **Access Token**.
4. Configure your mappings in the **Mappings** menu.
5. In the **Workflow** tab, enable **Auto-confirm Paid Orders** if desired.

## Usage

- Use the **Import Orders** wizard under **Operations** to fetch new orders.
- Validate Pickings in Odoo to trigger tracking synchronization back to Temu.

## License
Licensed under LGPL-3.
