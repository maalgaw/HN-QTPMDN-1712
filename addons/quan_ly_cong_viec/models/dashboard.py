from odoo import models, fields, api
from odoo.exceptions import UserError


class Dashboard(models.Model):
    _name = 'dashboard'
    _description = 'Thống Kê Tổng Quan'

    so_luong_nhan_vien = fields.Integer(string="Số lượng nhân viên", compute="_compute_tong_quan", store=False)
    so_luong_du_an = fields.Integer(string="Số lượng dự án", compute="_compute_tong_quan", store=False)
    so_luong_cong_viec = fields.Integer(string="Số lượng công việc", compute="_compute_tong_quan", store=False)
    so_luong_cong_viec_hoan_thanh = fields.Integer(
        string="Công việc đã hoàn thành", compute="_compute_tong_quan", store=False
    )
    phan_tram_hoan_thanh = fields.Float(
        string="Tiến độ trung bình dự án (%)", compute="_compute_tong_quan", store=False, digits=(16, 1)
    )
    so_luong_danh_gia = fields.Integer(string="Số lượng đánh giá", compute="_compute_tong_quan", store=False)

    du_an_hoan_thanh = fields.Integer(string="Dự án đã hoàn thành", compute="_compute_tong_quan", store=False)
    du_an_dang_thuc_hien = fields.Integer(string="Dự án đang thực hiện", compute="_compute_tong_quan", store=False)
    du_an_chua_bat_dau = fields.Integer(string="Dự án chưa bắt đầu", compute="_compute_tong_quan", store=False)
    du_an_tam_dung = fields.Integer(string="Dự án tạm dừng", compute="_compute_tong_quan", store=False)

    @api.depends()
    def _compute_tong_quan(self):
        DuAn = self.env['du_an']
        CongViec = self.env['cong_viec']
        for record in self:
            record.so_luong_nhan_vien = self.env['nhan_vien'].search_count([])
            du_an_records = DuAn.search([])
            record.so_luong_du_an = len(du_an_records)
            record.so_luong_cong_viec = CongViec.search_count([])
            record.so_luong_cong_viec_hoan_thanh = CongViec.search_count([('trang_thai_cong_viec', '=', 'hoan_thanh')])
            record.so_luong_danh_gia = self.env['danh_gia_nhan_vien'].search_count([])

            if du_an_records:
                pts = [d.phan_tram_du_an for d in du_an_records]
                record.phan_tram_hoan_thanh = sum(pts) / len(pts)
            else:
                record.phan_tram_hoan_thanh = 0.0

            record.du_an_hoan_thanh = sum(1 for d in du_an_records if d.tien_do_du_an == 'hoan_thanh')
            record.du_an_dang_thuc_hien = sum(1 for d in du_an_records if d.tien_do_du_an == 'dang_thuc_hien')
            record.du_an_chua_bat_dau = sum(1 for d in du_an_records if d.tien_do_du_an == 'chua_bat_dau')
            record.du_an_tam_dung = sum(1 for d in du_an_records if d.tien_do_du_an == 'tam_dung')

    @api.model_create_multi
    def create(self, vals_list):
        if self.search_count([]) >= 1:
            raise UserError('Chỉ cần một bản ghi Dashboard tổng quan. Dùng menu Dashboard để xem.')
        return super().create(vals_list)

    def unlink(self):
        raise UserError('Không xóa bản ghi Dashboard tổng quan.')
