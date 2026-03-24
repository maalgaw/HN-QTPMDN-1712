from odoo import models, fields


class TaiLieuMauDuAn(models.Model):
    _name = 'tai_lieu_mau_du_an'
    _description = 'Tài Liệu Biểu Mẫu Dự Án'

    du_an_id = fields.Many2one(
        'du_an',
        string='Dự Án',
        ondelete='cascade',
        required=True,
    )
    ten_tai_lieu = fields.Char(string='Tên Tài Liệu', required=True)
    file_dinh_kem = fields.Binary(string='File Đính Kèm', required=True, attachment=True)
    ten_file = fields.Char(string='Tên File')
    ngay_tai_len = fields.Date(
        string='Ngày Tải Lên',
        default=fields.Date.context_today,
    )
