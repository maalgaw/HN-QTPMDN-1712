# -*- coding: utf-8 -*-
{
    'name': "quan_ly_du_an",

    'summary': """
        Dự án, tài nguyên, rủi ro, đánh giá, AI gợi ý; thống kê công việc khi có module công việc.""",

    'description': """
        Quản lý dự án (du_an): team, tiến độ, tài nguyên, rủi ro, biểu mẫu, đánh giá, tích hợp AI.
        Liên kết nhân sự (nhan_su). Nút thống kê công việc hiển thị khi cài quan_ly_cong_viec.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Project',
    'version': '0.2',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'nhan_su'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/du_an_view.xml',
        'views/tai_nguyen_view.xml',
        'views/du_an_ai_view.xml',
        'views/res_config_settings_view.xml',
        'views/menu.xml',
    ],

    'demo': [],
}


