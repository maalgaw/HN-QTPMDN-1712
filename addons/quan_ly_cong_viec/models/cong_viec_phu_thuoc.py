# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class CongViecPhuThuoc(models.Model):
    """Quan hệ tiên quyết: công việc này chỉ được coi là có thể triển khai
    khi các công việc tiên quyết đã hoàn thành (finish-to-start)."""

    _name = 'cong_viec_phu_thuoc'
    _description = 'Phụ thuộc tiên quyết giữa công việc'
    _order = 'cong_viec_id, id'

    cong_viec_id = fields.Many2one(
        'cong_viec',
        string='Công việc (phụ thuộc)',
        required=True,
        ondelete='cascade',
        index=True,
        help='Công việc phải chờ các tiên quyết xong trước.',
    )
    tien_quyet_id = fields.Many2one(
        'cong_viec',
        string='Phải hoàn thành trước',
        required=True,
        ondelete='cascade',
        index=True,
    )
    ghi_chu = fields.Char(string='Ghi chú')

    _sql_constraints = [
        (
            'uniq_cv_tien_quyet',
            'unique(cong_viec_id, tien_quyet_id)',
            'Quan hệ tiên quyết này đã được khai báo.',
        ),
    ]

    @api.model
    def _graph_path_exists(self, start, end, line_records):
        """Cạnh có hướng P → D: P phải xong trước D (từ dòng tien_quyet_id=P, cong_viec_id=D).
        Kiểm tra có đường đi từ start → end theo hướng cạnh đó không."""
        if not start or not end:
            return False
        if start.id == end.id:
            return True
        visited = set()
        stack = [start.id]
        while stack:
            cur = stack.pop()
            if cur == end.id:
                return True
            if cur in visited:
                continue
            visited.add(cur)
            succ_ids = line_records.filtered(lambda l: l.tien_quyet_id.id == cur).mapped(
                'cong_viec_id'
            ).ids
            stack.extend(s for s in succ_ids if s not in visited)
        return False

    @api.constrains('cong_viec_id', 'tien_quyet_id')
    def _check_phu_thuoc_hop_le(self):
        PhuThuoc = self.env['cong_viec_phu_thuoc']
        for record in self:
            d = record.cong_viec_id
            p = record.tien_quyet_id
            if not d or not p:
                continue
            if d.id == p.id:
                raise ValidationError('Không thể đặt công việc tiên quyết chính nó.')
            if d.project_id != p.project_id:
                raise ValidationError('Hai công việc phải cùng một dự án.')
            others = PhuThuoc.search([('id', 'not in', record.ids)])
            # Thêm cạnh P → D: tạo chu trình nếu đã có đường D → ... → P (trên đồ thị hiện có)
            if PhuThuoc._graph_path_exists(d, p, others):
                raise ValidationError(
                    'Thêm quan hệ này tạo vòng phụ thuộc (chu trình tiên quyết).'
                )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records.mapped('cong_viec_id').invalidate_recordset(
            ['du_dieu_kien_tien_quyet', 'so_tien_quyet_chua_xong']
        )
        records.mapped('tien_quyet_id').invalidate_recordset(['so_cong_viec_chi_doi_nay'])
        return records

    def write(self, vals):
        old_dep = self.mapped('cong_viec_id')
        old_preds = self.mapped('tien_quyet_id')
        res = super().write(vals)
        (old_dep | self.mapped('cong_viec_id')).invalidate_recordset(
            ['du_dieu_kien_tien_quyet', 'so_tien_quyet_chua_xong']
        )
        (old_preds | self.mapped('tien_quyet_id')).invalidate_recordset(['so_cong_viec_chi_doi_nay'])
        return res

    def unlink(self):
        deps = self.mapped('cong_viec_id')
        preds = self.mapped('tien_quyet_id')
        res = super().unlink()
        deps.invalidate_recordset(['du_dieu_kien_tien_quyet', 'so_tien_quyet_chua_xong'])
        preds.invalidate_recordset(['so_cong_viec_chi_doi_nay'])
        return res
