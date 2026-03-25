# -*- coding: utf-8 -*-
{
    'name': "quan_ly_cong_viec",

    'summary': """
        Quản lý công việc theo dự án: tiên quyết giữa các việc, Kanban, timesheet và AI hỗ trợ.""",

    'description': """
        Công việc gắn dự án (du_an), quan hệ tiên quyết (finish-to-start, chống vòng lặp),
        nhật ký tiến độ, ghi nhận thời gian, tài nguyên, đánh giá.
        Tích hợp tùy chọn Gemini AI (cấu hình trong Cài đặt).
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Project',
    'version': '0.4',
    'application': True,

    # any module necessary for this one to work correctly
    # Phụ thuộc vào module quản lý dự án mới để dùng model du_an
    'depends': ['base', 'nhan_su', 'quan_ly_du_an'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/dashboard_data.xml',
        'views/res_config_settings_view.xml',
        'views/dashboard_view.xml',
        'views/giai_doan_cong_viec_view.xml',
        'views/cong_viec_view.xml',
        'views/nhat_ky_cong_viec_view.xml',
        'views/danh_gia_nhan_vien_quan_ly_cong_viec.xml',
        'views/menu.xml',
    ],
    
    'icon': '/quan_ly_cong_viec/static/description/image.png',
    
    'assets': {
        'web.assets_backend': [
            '/quan_ly_cong_viec/static/css/dashboard.css',
        ],
    },

    'post_init_hook': 'quan_ly_cong_viec.hooks.post_init_hook',
}

