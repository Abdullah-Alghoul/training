from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class RestoButton(models.Model):
    _name = 'resto.button'
    _rec_name = 'tanpa_kolom_name'

    tanpa_kolom_name = fields.Char(string='Tanpa Kolom Nama')

    # A. Popup
    @api.multi
    def popup_1(self):
        raise UserError('Popup dari Python')

    @api.multi
    def popup_2(self):
        utc_date_now = datetime.now()
        local_date_now = fields.Datetime.context_timestamp(self.with_context(tz=self.env.user.tz), utc_date_now)
        message = 'Popup dari Python : %s' % (local_date_now)
        raise UserError(message)

    @api.multi
    def popup_3(self):
        utc_date_now = datetime.now()
        local_date_now = fields.Datetime.context_timestamp(self.with_context(tz=self.env.user.tz), utc_date_now)
        message = 'Popup dari Python : %s' % (local_date_now.date())
        raise UserError(message)

    @api.multi
    def popup_4(self):
        utc_date_now = datetime.now()
        local_date_now = fields.Datetime.context_timestamp(self.with_context(tz=self.env.user.tz), utc_date_now)
        message = 'Popup dari Python : %s' % (local_date_now.time())
        raise UserError(message)

    @api.multi
    def browse_1(self):
        resto_order_model = self.env['ark.resto.order']
        result = resto_order_model.browse(1)
        message = 'Popup dari Python : %s' % (result)
        raise UserError(message)

    @api.multi
    def browse_2(self):
        resto_order_model = self.env['ark.resto.order']
        result = resto_order_model.browse(1).name
        message = 'Popup dari Python : %s' % (result)
        raise UserError(message)

    @api.multi
    def browse_3(self):
        resto_order_model = self.env['ark.resto.order']
        message = resto_order_model.browse(1).date_order
        message = 'Popup dari Python : %s' % (message)
        raise UserError(message)

    @api.multi
    def browse_4(self):
        resto_order_model = self.env['ark.resto.order']
        result = resto_order_model.browse(1000)
        message = 'Popup dari Python : %s' % (result)
        raise UserError(message)

    @api.multi
    def browse_5(self):
        resto_order_model = self.env['ark.resto.order']
        result = resto_order_model.browse(1000).name
        message = 'Popup dari Python : %s' % (result)
        raise UserError(message)

    @api.multi
    def search_1(self):
        rom = self.env['ark.resto.order']
        search_query = [('customer', '=', 'Radit')]
        order_docs = rom.search(search_query)
        message = 'Popup dari Python : %s' % (order_docs)
        raise UserError(message)

    @api.multi
    def search_2(self):
        rom = self.env['ark.resto.order']
        search_query = [('line', '=', 'Milkshake')]
        order_docs = rom.search(search_query)
        message = 'Popup dari Python : %s' % (order_docs)
        raise UserError(message)

    @api.multi
    def search_3(self):
        rom = self.env['ark.resto.order']
        search_query = [('line', 'ilike', 'Milkshake')]
        order_docs = rom.search(search_query)
        message = 'Popup dari Python : %s' % (order_docs)
        raise UserError(message)

    @api.multi
    def search_4(self):
        rom = self.env['ark.resto.order']
        search_query = [('amount_total', '<', 50000)]
        order_docs = rom.search(search_query)
        message = 'Popup dari Python : %s' % (order_docs)
        raise UserError(message)

    @api.multi
    def search_5(self):
        rom = self.env['ark.resto.order']
        search_query = [('to_check', '=', True)]
        order_docs = rom.search(search_query)
        message = 'Popup dari Python : %s' % (order_docs)
        raise UserError(message)

    @api.multi
    def write_1(self):
        rom = self.env['ark.resto.order']
        search_query = [] # All ~ WHERE 1 = 1
        order_docs = rom.search(search_query)
        for order_doc in order_docs:
            order_doc.write({
                'to_check': False,
            })

    @api.multi
    def write_2(self):
        rom = self.env['ark.resto.order']
        search_query = []
        order_docs = rom.search(search_query)
        for order_doc in order_docs:
            order_doc.write({
                'to_check': True,
            })

    @api.multi
    def write_3(self):
        rom = self.env['ark.resto.order']
        search_query = []
        search_query = [('pay_method', '=', 'gopie')]
        order_docs = rom.search(search_query)
        for order_doc in order_docs:
            order_doc.write({
                'pay_method': 'volvo',
            })

