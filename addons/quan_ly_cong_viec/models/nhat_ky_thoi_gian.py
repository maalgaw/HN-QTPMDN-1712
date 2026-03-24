from odoo import models, fields, api
from odoo.exceptions import ValidationError


class NhatKyThoiGian(models.Model):
    _name = 'nhat_ky_thoi_gian'
    _description = 'Ghi Nhận Thời Gian (Timesheet)'
    _order = 'ngay_thuc_hien desc, id desc'

    ngay_thuc_hien = fields.Date(
        string='Ngày Thực Hiện',
        required=True,
        default=fields.Date.context_today,
    )
    mo_ta = fields.Char(string='Mô Tả Công Việc', required=True)
    so_gio = fields.Float(string='Số Giờ', required=True, digits=(16, 2))

    cong_viec_id = fields.Many2one(
        'cong_viec',
        string='Công Việc',
        ondelete='cascade',
        required=True,
    )
    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân Viên',
        ondelete='restrict',
        required=True,
    )

    @api.constrains('so_gio')
    def _check_so_gio(self):
        for record in self:
            if record.so_gio <= 0:
                raise ValidationError('Số giờ phải lớn hơn 0.')

    @api.constrains('nhan_vien_id', 'cong_viec_id')
    def _check_nhan_vien_trong_cong_viec(self):
        for record in self:
            if not record.cong_viec_id or not record.nhan_vien_id:
                continue
            if record.nhan_vien_id not in record.cong_viec_id.nhan_vien_ids:
                raise ValidationError(
                    'Nhân viên ghi nhận phải thuộc danh sách nhân viên tham gia công việc.'
                )
