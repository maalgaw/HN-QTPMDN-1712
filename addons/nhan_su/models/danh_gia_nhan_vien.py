# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DanhGiaNhanVien(models.Model):
    _name = 'danh_gia_nhan_vien'
    _description = 'Đánh Giá Nhân Viên'

    nhan_vien_id = fields.Many2one('nhan_vien', string='Nhân Viên', required=True, ondelete='cascade')
    diem_so = fields.Selection([(str(i), str(i)) for i in range(1, 11)], string='Điểm Số', required=True)
    nhan_xet = fields.Text(string='Nhận Xét')
    ngay_danh_gia = fields.Datetime(string='Ngày Đánh Giá', default=fields.Datetime.now, required=True)

    @api.constrains('diem_so')
    def _check_diem_so(self):
        for record in self:
            if not (1 <= int(record.diem_so) <= 10):
                raise ValidationError("Điểm số phải nằm trong khoảng từ 1 đến 10.")
