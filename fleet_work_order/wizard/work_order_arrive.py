# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models, fields


class WorkOrderArive(models.TransientModel):
    _name = "fleet.work.order.arrive"
    _description = "Work Order Arrive"

    date_arrive = fields.Datetime(
        string="Date Arrive",
        required=True,
        default=fields.Datetime.now(),
    )
    end_odometer = fields.Float(
        string="Ending Odometer",
        required=True,
    )

    @api.multi
    def button_arrive(self):
        self.ensure_one()
        self._arrive(self)

    @api.model
    def _arrive(self, wizard):
        order_ids = self.env.context["active_ids"]
        order = self.env["fleet.work.order"].browse(order_ids)

        order._action_arrive(order,
                             date_arrive=wizard.date_arrive,
                             ending_odometer=wizard.end_odometer,
                             )
