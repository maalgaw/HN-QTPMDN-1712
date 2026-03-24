from odoo import models, fields


class TaiLieuCongViec(models.Model):
    """Tài liệu đính kèm công việc (tách bảng riêng, không dùng ir.attachment trực tiếp làm nghiệp vụ)."""

    _name = 'tai_lieu_cong_viec'
    _description = 'Tài Liệu Đính Kèm Công Việc'
    _order = 'ngay_tai_len desc, id desc'

    ten_tai_lieu = fields.Char(string='Tên Tài Liệu', required=True)
    file_dinh_kem = fields.Binary(string='File Đính Kèm', attachment=True)
    ten_file = fields.Char(string='Tên File')
    ngay_tai_len = fields.Date(
        string='Ngày Tải Lên',
        default=fields.Date.context_today,
        required=True,
    )
    nguoi_tai_len_id = fields.Many2one(
        'nhan_vien',
        string='Người Tải Lên',
        ondelete='set null',
    )
    cong_viec_id = fields.Many2one(
        'cong_viec',
        string='Công Việc',
        ondelete='cascade',
        required=True,
    )
    # Mức 3 (tùy chọn): lưu link cloud thay cho/kèm file — có thể bổ sung API Drive sau
    link_luu_tru_ngoai = fields.Char(string='Đường Dẫn / Link Lưu Trữ Ngoài')
