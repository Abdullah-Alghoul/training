from odoo import models, fields

class ArkCafeOrder(models.Model):
	_name = 'ark.cafe.order'

	# A. Order Detail
	name = fields.Char(string='Nota')
	customer = fields.Char(string='Pelanggan')

	date_order = fields.Datetime(string='Date Order')
	date_paid = fields.Date(string='Date Paid')
	user = fields.Char(string='Kasir')

	# B. Payment
	currency = fields.Selection(string='Mata Uang',
		selection=[
			('rp', 'Rupiah'),
			('usd', 'Dollar'),
		],
	)
	pay_method = fields.Selection(string='Bayar via',
		selection=[
			('cash', 'Tunai'),
			('debit', 'Debit'),
			('credit', 'Credit'),
			('gopie', 'Go-Pie'),
			('volvo', 'Volvo'),
		],
	)
	pay_ref = fields.Char(string='Pay Ref.')
	amount_total = fields.Integer(string='Total Tagihan')

	# C. Order Line
	line = fields.Text(string='Order Line')

	# D. Other Info
	to_check = fields.Boolean(string='Check?', help="Kalau ada yg aneh mau dikonfirmasi dulu")

