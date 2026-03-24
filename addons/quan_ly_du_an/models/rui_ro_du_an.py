from odoo import models, fields


class RuiRoDuAn(models.Model):
    _name = 'rui_ro_du_an'
    _description = 'Rủi Ro Dự Án'
    _order = 'create_date desc'

    ten_rui_ro = fields.Char(string='Tên Rủi Ro', required=True)
    muc_do_nghiem_trong = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung Bình'),
        ('cao', 'Cao'),
    ], string='Mức Độ Nghiêm Trọng', required=True, default='trung_binh')
    trang_thai = fields.Selection([
        ('dang_theo_doi', 'Đang Theo Dõi'),
        ('da_xay_ra', 'Đã Xảy Ra'),
        ('da_khac_phuc', 'Đã Khắc Phục'),
    ], string='Trạng Thái', required=True, default='dang_theo_doi')
    bien_phap_xu_ly = fields.Text(string='Biện Pháp Xử Lý')

    du_an_id = fields.Many2one(
        'du_an',
        string='Dự Án',
        ondelete='cascade',
        required=True,
    )
    nguoi_chiu_trach_nhiem_id = fields.Many2one(
        'nhan_vien',
        string='Người Chịu Trách Nhiệm',
        ondelete='set null',
    )
