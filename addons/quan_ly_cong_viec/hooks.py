# -*- coding: utf-8 -*-
"""Đảm bảo Dashboard luôn có bản ghi và action trỏ đúng (DB cũ / cài lại)."""


def post_init_hook(cr, registry):
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    Dashboard = env['dashboard']
    d = Dashboard.search([], limit=1)
    if not d:
        d = Dashboard.create({})
    try:
        action = env.ref('quan_ly_cong_viec.action_dashboard')
        if action.res_id != d.id:
            action.sudo().write({'res_id': d.id})
    except Exception:
        pass
