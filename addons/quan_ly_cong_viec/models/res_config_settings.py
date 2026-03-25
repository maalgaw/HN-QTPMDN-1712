# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    qlcv_ai_enabled = fields.Boolean(
        string='Bật AI (Quản lý công việc)',
        config_parameter='quan_ly_cong_viec.ai_enabled',
    )
    qlcv_ai_api_key = fields.Char(
        string='API Key',
        config_parameter='quan_ly_cong_viec.ai_api_key',
    )
    qlcv_ai_base_url = fields.Char(
        string='Base URL',
        config_parameter='quan_ly_cong_viec.ai_base_url',
        default='https://generativelanguage.googleapis.com/v1beta',
    )
    qlcv_ai_model = fields.Char(
        string='Model',
        config_parameter='quan_ly_cong_viec.ai_model',
        default='gemini-2.5-flash',
    )
    qlcv_ai_timeout = fields.Integer(
        string='Timeout (giây)',
        config_parameter='quan_ly_cong_viec.ai_timeout',
        default=30,
    )
