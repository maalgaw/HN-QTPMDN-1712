# -*- coding: utf-8 -*-
{
    'name': "nhan_su",

    'summary': """
        Hồ sơ nhân viên: liên hệ, trạng thái làm việc, lịch sử công tác, chứng chỉ, đánh giá.""",

    'description': """
        Quản lý danh sách nhân viên, đơn vị, chức vụ, lịch sử công tác và chứng chỉ.
        Hỗ trợ trạng thái làm việc, ngày vào làm và lưu trữ bản ghi (active).
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Human Resources',
    'version': '0.2',
    'application': True,

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/chuc_vu.xml',
        'views/don_vi.xml',
        'views/nhan_vien.xml',
        'views/lich_su_cong_tac.xml',
        'views/chung_chi_bang_cap.xml',
        'views/danh_sach_chung_chi_bang_cap.xml',
        'views/danh_gia_nhan_vien_view.xml',
        'views/menu.xml',
    ],
}
