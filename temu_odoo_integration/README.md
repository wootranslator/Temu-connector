# Temu Odoo 18 Integration

This module integrates Odoo 18 with the Temu marketplace, allowing for seamless order import, product mapping, and shipment tracking.

## Features

- **Marketplaces Dashboard**: A Kanban view to manage all your Temu connections with real-time statistics (Pending, Total Orders).
- **Order Import**: Automatic and manual import of orders from Temu with custom **Order Prefixes**.
- **Sales Team Assignment**: Automatically assigns imported orders to a dedicated "Temu | Marketplace" sales team.
- **Deduplication**: Robust contact deduplication by VAT (CIF/NIF), email, or name.
- **Product Mapping**: Map Temu SKUs to Odoo Products.
- **Fiscal Mapping**: Map Temu regions to Odoo Fiscal Positions.
- **Payment Mapping**: Map Temu payment methods to Odoo Payment Journals and register payments automatically.
- **Shipping Mapping**: Map Temu shipping methods to Odoo Delivery Carriers with API synchronization.
- **Workflow Automation**: Auto-confirm orders based on payment status.
- **Shipment Tracking**: Synchronize tracking numbers from Odoo back to Temu.
- **Sandbox Support**: Test your integration safely using the Temu Sandbox environment.

## Installation

1. Copy this folder into your Odoo `addons` directory.
2. Ensure the `delivery`, `sale_management`, `stock`, `crm`, and `account` modules are installed.
3. Restart Odoo and update the Apps list.
4. Install **Temu Odoo Integration**.

## Configuration

1. Go to **Temu Integration > Configuration > Marketplaces**.
2. Create a new Marketplace and select the **Environment** (Sandbox or Production).
3. Enter your **Client ID**, **Client Secret**, and **Access Token**.
4. Configure your mappings (SKU, Shipping, Tax, etc.) in the **Mappings** menu.
5. Use the **Sync Shipping Methods** button in the Marketplace form to fetch available methods from Temu.

## Usage

- Access the **Marketplaces Dashboard** for a quick overview and quick actions.
- Use the **Import Orders** wizard under **Orders** to fetch new orders manually.
- Validate Pickings in Odoo to trigger tracking synchronization back to Temu.

## License
Licensed under LGPL-3.
