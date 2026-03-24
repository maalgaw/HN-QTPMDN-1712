from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DanhGiaDuAn(models.Model):
    _name = 'danh_gia_du_an'
    _description = 'Đánh Giá Dự Án'
    _order = 'ngay_danh_gia desc, id desc'

    ten_dot_danh_gia = fields.Char(
        string='Tên Đợt Đánh Giá',
        help='Ví dụ: Sau thiết kế, Sau UAT, Tổng kết dự án',
    )
    du_an_id = fields.Many2one(
        'du_an',
        string='Dự Án',
        ondelete='cascade',
        required=True,
    )
    nguoi_danh_gia_id = fields.Many2one(
        'nhan_vien',
        string='Người Đánh Giá',
        ondelete='restrict',
        required=True,
    )
    ngay_danh_gia = fields.Datetime(
        string='Ngày Đánh Giá',
        required=True,
        default=fields.Datetime.now,
    )
    diem_so = fields.Selection(
        [(str(i), str(i)) for i in range(1, 11)],
        string='Điểm Số (1–10)',
        required=True,
    )
    nhan_xet = fields.Text(string='Nhận Xét')

    @api.constrains('diem_so')
    def _check_diem_so(self):
        for record in self:
            if not record.diem_so:
                continue
            v = int(record.diem_so)
            if not (1 <= v <= 10):
                raise ValidationError('Điểm số phải từ 1 đến 10.')

    @api.constrains('nguoi_danh_gia_id', 'du_an_id')
    def _check_nguoi_thuoc_du_an(self):
        for record in self:
            if not record.du_an_id or not record.nguoi_danh_gia_id:
                continue
            du_an = record.du_an_id
            nv = record.nguoi_danh_gia_id
            hop_le = nv in du_an.nhan_vien_ids
            if du_an.nguoi_phu_trach_id and nv == du_an.nguoi_phu_trach_id:
                hop_le = True
            if not hop_le:
                raise ValidationError(
                    'Người đánh giá phải là người phụ trách dự án hoặc nhân viên tham gia dự án.'
                )
