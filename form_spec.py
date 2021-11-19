from docbase import PatternType
from docbase.kv import ValueType

SB_KV_TYPE_INIT = [
    {
        "name": "Phiếu hạch toán",
        "short_name": "phieu_hach_toan",
        "code": "OCR01",
        "title": {
            "pattern": "PHIẾU HẠCH TOÁN",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "TÊN TÀI KHOẢN",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "SỐ TIỀN",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "PHIẾU HẠCH TOÁN GIẢI NGÂN",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "PHIẾU HẠCH TOÁN NGOẠI BẢNG TSBD",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "KIÊM PHIẾU HẠCH TOÁN",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "VÀ PHIẾU HẠCH TOÁN",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "key_values": [
            {
                "name": "Số giao dịch",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "TT2034203029"
            },
            {
                "name": "Ngày bút toán",
                "short_name": "issue_date",
                "urd_ref_id": 2,
                "value_type": ValueType.DATE,
                "example": "07/12/2020"
            },
            {
                "name": "Bảng giao dịch",
                "short_name": "table_transaction",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 3,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Loại giao dịch",
                                "short_name": "account_type",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 3.0,
                                "example": "TK No" # TK Co
                            },
                            {
                                "name": "Số tài khoản",
                                "short_name": "account_number",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 3.1,
                                "example": "00007105483"
                            },
                            {
                                "name": "Tên chủ tài khoản",
                                "short_name": "account_name",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 3.2,
                                "example": "TKTT VND - VU HOANG KIM"
                            },
                            {
                                "name": "Số tiền",
                                "short_name": "account_amount",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 3.3,
                                "example": 5000000.00
                            },
                            {
                                "name": "Đơn vị tiền tệ",
                                "short_name": "account_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 3.4,
                                "example": "VND"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Nội dung giao dịch",
                "short_name": "details",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "VU HOANG KIM RUT TIEN"
            },
            {
                "name": "Số tiền bằng số",
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 6,
                "example": 5000000.00
            },
            {
                "name": "Đơn vị tiền tệ",
                "short_name": "currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 7,
                "example": "VND"
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "nam muoi nghin dong chan"
            },
        ]
    },
    {
        "name": "Ủy nhiệm chi", # Bỏ không trích xuất KV
        "short_name": "uy_nhiem_chi",
        # "code": "OCR17",
        "title": {
            "pattern": "UỶ NHIỆM CHI",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "PAYMENT (ORDER|ONDER)",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
            },
            {
                "pattern": "Nội dung",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
            }
        ],
        "must_exclude_pattern": [],
        "key_values": []
    },
    {
        "name": "Giấy nộp tiền vào ngân sách nhà nước",
        "short_name": "giay_nop_tien_vao_ngan_sach_nha_nuoc",
        "code": "OCR02",
        "title": {
            "pattern": "Giấy nộp tiền vào ngân sách nhà Nước",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Người nộp thuế",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Mã số thuế",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
        ],
        "must_exclude_pattern": [],
        "key_values": [
            {
                "name": "Ngày tạo",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 2,
                "example": "14/7/2020"
            },
            {
                "name": "Số tài khoản nợ",
                "short_name": "debit_account",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "003 001 1348 1909"
            },
            {
                "name": "Số tài khoản có",
                "short_name": "credit_account",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "7111"
            },
            {
                "name": "Số tiền bằng số",
                "short_name": "amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 5,
                "example": 91795860
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 6,
                "example": "Chín mươi mốt triệu bảy trăm chín mươi lăm ngàn tám trăm sáu mươi đồng"
            },
            {
                "name": "Địa chỉ",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 7,
                "example": "Hoàng Mai, Hoàng Ninh"
            },
            {
                "name": "Bảng nội dung",
                "short_name": "details_table",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 9,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Nội dung",
                                "short_name": "details",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 9.1,
                                "example": "Tiền thuế sử dụng đất phi nông nghiệp nộp cho 5 năm từ 2017 đến 2021 theo Thông báo số 1601/TB-CCTKV ngày 9/7/2020"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Người nộp thuế",
                "short_name": "tax_payer",
                "value_type": ValueType.STR,
                "urd_ref_id": 10,
                "example": "CN Tổng công ty công nghiệp ô tô Việt Nam - CTCP - Nhà máy ô tô Đồng Vàng 1"
            },
            {
                "name": "Mã số thuế",
                "short_name": "tax_code",
                "value_type": ValueType.INT,
                "urd_ref_id": 11,
                "example": "0100104429-004"
            },
            {
                "name": "Tỉnh, TP (phần người nộp thuế)",
                "short_name": "tax_payer_province_city",
                "value_type": ValueType.STR,
                "urd_ref_id": 13,
                "example": "Bắc Giang"
            },
            {
                "name": "Đề nghị NH",
                "short_name": "propose_bank",
                "value_type": ValueType.STR,
                "urd_ref_id": 14,
                "example": "Seabank - CN Hà Nội"
            },
            {
                "name": "Tỉnh, TP (tại KBNN)",
                "short_name": "state_treasury_province_city",
                "value_type": ValueType.STR,
                "urd_ref_id": 15,
                "example": "Bắc Giang"
            },
            {
                "name": "Tại KBNN",
                "short_name": "at_state_treasury",
                "value_type": ValueType.STR,
                "urd_ref_id": 18,
                "example": "Kho bạc Nhà nước huyện Việt Yên"
            },
        ]
    },
    {
        "name": "Giấy Đề nghị kiêm Lệnh điều chuyển hàng đặc biệt",
        "short_name": "giay_de_nghi_kiem_lenh_dieu_chuyen_hang_dac_biet",
        "code": "OCR03",
        "title": {
            "pattern": "Đề nghị kiêm Lệnh điều chuyển hàng đặc biệt",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "kiêm lệnh điều chuyển hàng đặc biệt",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "HĐB",
                "pattern_type": PatternType.RAW
            },
            {
                "pattern": "Cán bộ",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
        ],
        "must_exclude_pattern": [],
        "key_values": [
            {
                "name": "Ngày tạo",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 1,
                "example": "30/06/2020"
            },
            {
                "name": "Điều chuyển HĐB từ",
                "short_name": "transfer_from",
                "value_type": ValueType.STR,
                "urd_ref_id": 2,
                "example": "Cụm KQTT Đại An"
            },
            {
                "name": "Điều chuyển HĐB đến",
                "short_name": "transfer_to",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "CN Hà Đông"
            },
            {
                "name": "Phương tiện vận chuyển",
                "short_name": "transportation",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "Ô tô chuyên dụng"
            },
            {
                "name": "Bảng hàng đặc biệt",
                "short_name": "table_product",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 5,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Loại tiền",
                                "short_name": "currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 5.1,
                                "example": "VND",
                            },
                            {
                                "name": "Số tiền bằng số",
                                "short_name": "amount",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 5.2,
                                "example": 624833975,
                            },
                            {
                                "name": "Số tiền bằng chữ",
                                "short_name": "amount_text",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 5.3,
                                "example": "Sáu Trăm Hai Mươi Bốn Triệu Tám Trăn Ba Mươi Nghìn Chín Trăm Bảy Mươi Lăm VND Chẵn",
                            },
                        ]
                    },
                ]
            },
            {
                "name": "Họ tên cán bộ áp tải HĐB",
                "short_name": "delivery_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 14,
                "example": "Trần Thị Thanh Huyền"
            },
            {
                "name": "Số CMT cán bộ áp tải HĐB",
                "short_name": "delivery_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 15,
                "example": "011936182"
            },
            {
                "name": "Chức vụ cán bộ áp tải HĐB",
                "short_name": "delivery_position",
                "value_type": ValueType.STR,
                "urd_ref_id": 16,
                "example": "Chuyên viên quỹ"
            },
            {
                "name": "Ngày cấp CMT CB áp tải HĐB",
                "short_name": "delivery_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 17,
                "example": "13/11/2006"
            },
            {
                "name": "Nơi cấp CMT CB áp tải",
                "short_name": "delivery_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 18,
                "example": "CA Hà Nội"
            },
            {
                "name": "Họ tên cán bộ bàn giao",
                "short_name": "handover_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 19,
                "example": "Quách Thu Hường"
            },
            {
                "name": "Chức vụ cán bộ bàn giao",
                "short_name": "handover_position",
                "value_type": ValueType.STR,
                "urd_ref_id": 20,
                "example": "TQ kiêm TKT"
            },
            {
                "name": "Họ tên Công an/Bảo vệ",
                "short_name": "security_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 21,
                "example": "Nguyễn Trọng Sang"
            },
            {
                "name": "CMT công an/bảo vệ",
                "short_name": "security_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 22,
                "example": "010755808"
            },
            {
                "name": "Ngày cấp CMT công an/bảo vệ",
                "short_name": "security_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 23,
                "example": "30/05/2007"
            },
            {
                "name": "Nơi cấp CMT công an/bảo vệ",
                "short_name": "security_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 24,
                "example": "CA Hà Nội"
            },
            {
                "name": "Họ tên lái xe",
                "short_name": "driver_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 25,
                "example": "Đinh Văn Dũng"
            },
            {
                "name": "CMT lái xe",
                "short_name": "driver_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 26,
                "example": "011514242"
            },
            {
                "name": "Ngày cấp CMT lái xe",
                "short_name": "driver_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 27,
                "example": "03/03/2008"
            },
            {
                "name": "Nơi cấp CMT lái xe",
                "short_name": "driver_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 28,
                "example": "CA Hà Nội"
            },
        ]
    },
    {
        "name": "Đề nghị điều chuyển hàng đặc biệt",
        "short_name": "de_nghi_dieu_chuyen_hang_dac_biet",
        "code": "OCR04",
        "title": {
            "pattern": "Đề nghị điều chuyển hàng đặc biệt",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Điều chuyển hàng đặc biệt",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "HĐB",
                "pattern_type": PatternType.RAW
            },
            {
                "pattern": "Phương tiện vận chuyển",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "Cán bộ giao",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Cán bộ áp tải",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Công an",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Lái xe",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "key_values": [
            {
                "name": "Ngày tạo",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 1,
                "example": "10/11/2020"
            },
            {
                "name": "Điều chuyển HĐB từ",
                "short_name": "transfer_from",
                "value_type": ValueType.STR,
                "urd_ref_id": 2.1,
                "example": "Cụm KQTT"
            },
            {
                "name": "Điều chuyển HĐB đến",
                "short_name": "transfer_to",
                "value_type": ValueType.STR,
                "urd_ref_id": 2.2,
                "example": "ĐVKD"
            },
            {
                "name": "Phương tiện vận chuyển",
                "short_name": "transportation",
                "value_type": ValueType.STR,
                "urd_ref_id": 2.3,
                "example": ""
            },
            {
                "name": "Bảng hàng đặc biệt",
                "short_name": "table_product",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 3,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Loại tiền",
                                "short_name": "currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 3.1,
                                "example": "VND",
                            },
                            {
                                "name": "Số tiền bằng số",
                                "short_name": "amount",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 3.2,
                                "example": 7000000000,
                            },
                            {
                                "name": "Số tiền bằng chữ",
                                "short_name": "amount_text",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 3.3,
                                "example": "Bảy tỷ đồng",
                            },

                        ]
                    }
                ]
            },
        ]
    },
    {
        "name": "Lệnh điều chuyển hàng đặc biệt",
        "short_name": "lenh_dieu_chuyen_hang_dac_biet",
        "code": "OCR05",
        "title": {
            "pattern": "Lệnh điều chuyển hàng đặc biệt",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Điều chuyển hàng đặc biệt",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "HĐB",
                "pattern_type": PatternType.RAW
            },
            {
                "pattern": "Phương tiện vận chuyển",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Cán bộ giao",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Công an",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Lái xe",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "ĐỀ NGHỊ",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "key_values": [
            {
                "name": "Ngày giao dịch",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 1,
                "example": "10/11/2020"
            },
            {
                "name": "Điều chuyển HĐB từ",
                "short_name": "transfer_from",
                "value_type": ValueType.STR,
                "urd_ref_id": 2,
                "example": "Cụm sở giao dịch"
            },
            {
                "name": "Điều chuyển HĐB đến",
                "short_name": "transfer_to",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "Trung tâm khách hàng cao cấp Miền Bắc"
            },
            {
                "name": "Phương tiện vận chuyển",
                "short_name": "transportation",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": ""
            },
            # Điều chuyển hàng đặc biệt
            {
                "name": "Bảng hàng đặc biệt",
                "short_name": "table_product",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 5,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example": [
                            {
                                "name": "Loại tiền",
                                "short_name": "product_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 5.1,
                                "example": "VND",
                            },
                            {
                                "name": "Số tiền bằng số",
                                "short_name": "product_amount",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 5.2,
                                "example": 7000000000,
                            },
                            {
                                "name": "Số tiền bằng chữ",
                                "short_name": "product_amount_text",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 5.3,
                                "example": "Bảy tỷ đồng"

                            }
                        ]
                    }
                ]
            },
            # Xác nhận giao dịch/ kiêm phiếu thu, phiếu giao nhận
            {
                "name": "Bảng hàng xác nhận",
                "short_name": "table_confirmation",
                "value_type": ValueType.LIST,
                "urd_ref_id": 17,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.TABLE,
                        "example":[
                            {
                                "name": "Loại tiền",
                                "short_name": "confirm_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 17.1,
                                "example": "VND",
                            },
                            {
                                "name": "Số lượng",
                                "short_name": "confirm_amount",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 17.2,
                                "example": 7000000000,
                            },
                            {
                                "name": "Bằng chữ",
                                "short_name": "confirm_amount_text",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 17.3,
                                "example": "Bảy tỷ đồng",
                            },
                        ]
                    }
                ]
            },
            {
                "name": "Họ tên cán bộ bàn giao",
                "short_name": "handover_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 26,
                "example": "Cao Thanh Hằng"
            },
            {
                "name": "Chức vụ cán bộ bàn giao",
                "short_name": "handover_position",
                "value_type": ValueType.STR,
                "urd_ref_id": 27,
                "example": "CV Quỹ"
            },
            {
                "name": "Họ tên cán bộ áp tải HĐB",
                "short_name": "delivery_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 28,
                "example": "Cao Thanh Hằng"
            },
            {
                "name": "Chức vụ cán bộ áp tải HĐB",
                "short_name": "delivery_position",
                "value_type": ValueType.STR,
                "urd_ref_id": 29,
                "example": "CV Quỹ"
            },
            {
                "name": "Số CMT cán bộ áp tải HĐB",
                "short_name": "delivery_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 30,
                "example": "001193004518"
            },
            {
                "name": "Ngày cấp CMT CB áp tải HĐB",
                "short_name": "delivery_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 31,
                "example": "07/10/2015"
            },
            {
                "name": "Nơi cấp CMT CB áp tải",
                "short_name": "delivery_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 32,
                "example": "CA Hà Nội"
            },
            {
                "name": "Họ tên Công an/Bảo vệ",
                "short_name": "security_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 33,
                "example": "Mai Văn Chanh"
            },
            {
                "name": "CMT công an/bảo vệ",
                "short_name": "security_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 34,
                "example": "145518562"
            },
            {
                "name": "Ngày cấp CMT công an/bảo vệ",
                "short_name": "security_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 35,
                "example": "16/07/2008"
            },
            {
                "name": "Nơi cấp CMT công an/bảo vệ",
                "short_name": "security_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 40,
                "example": "Hưng Yên"
            },
            {
                "name": "Họ tên lái xe",
                "short_name": "driver_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 36,
                "example": ""
            },
            {
                "name": "CMT lái xe",
                "short_name": "driver_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 37,
                "example": ""
            },
            {
                "name": "Ngày cấp CMT lái xe",
                "short_name": "driver_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 38,
                "example": ""
            },
            {
                "name": "Nơi cấp CMT lái xe",
                "short_name": "driver_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 41,
                "example": ""
            },
        ]
    },
    {
        "name": "Phiếu mua ngoại tệ",
        "short_name": "phieu_mua_ngoai_te",
        "code": "OCR06",
        "title": {
            "pattern": "Phiếu mua ngoại tệ",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Số ngoại tệ mua",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Loại tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Tỷ giá",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [],
        "key_values": [
            {
                "name": "Số giao dịch",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "TT21095033523"
            },
            {
                "name": "Ngày giao dịch",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 2,
                "example": "05/04/2021"
            },
            {
                "name": "Người bán",
                "short_name": "seller_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "DAO THI THUY LIEN"
            },
            {
                "name": "Số tiền",
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 4,
                "example": 100.00
            },
            {
                "name": "Loại tiền",
                "short_name": "currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "USD"
            },
            {
                "name": "Tỷ giá",
                "short_name": "exchange_rate",
                "value_type": ValueType.INT,
                "urd_ref_id": 6,
                "example": 22987
            },
            {
                "name": "Số tiền quy đổi",
                "short_name": "exchange_amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 7,
                "example": 2298000
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "Hai triệu, hai trăm chín mươi tám nghìn đồng"
            },
            {
                "name": "Địa chỉ khách hàng",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 13,
                "example": "3632 CT12B KIM VAN KIM LU DAI KIM QUAN HOANG MAI HA NOI"
            },
            {
                "name": "User",
                "short_name": "user_inputter",
                "value_type": ValueType.STR,
                "urd_ref_id": 14,
                "example": "VANTTT"
            },
            {
                "name": "Nội dung",
                "short_name": "details",
                "value_type": ValueType.STR,
                "urd_ref_id": 16,
                "example": "BAN 100 USD TG 22980"
            },
            {
                "name": "Bảng hạch toán",
                "short_name": "table_accounting",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 17,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example": [
                            {
                                "name": "Hạch toán",
                                "short_name": "accounting_type",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 17.0,
                                "example": "TK Co" # TK No,
                            },
                            {
                                "name": "Số tài khoản",
                                "short_name": "account_number",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 17.1,
                                "example": "VND100199990043"
                            },
                            {
                                "name": "Tên chủ tài khoản",
                                "short_name": "account_name",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 17.2,
                                "example": "TK VND QUY CHINH KIM VAN"
                            },
                            {
                                "name": "Số tiền",
                                "short_name": "accounting_amount",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 17.3,
                                "example": 2298000.00,
                            },
                            {
                                "name":"Đơn vị tiền tệ",
                                "short_name": "accounting_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 17.4,
                                "example": "VND"
                            },
                        ]
                    }
                ]
            },
            {
                "name": "GTTT/Hộ chiếu",
                "short_name": "id_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 19,
                "example": "030184006782"
            },
            {
                "name": "Ngày cấp",
                "short_name": "id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 20,
                "example": "26/06/2017"
            },
            {
                "name": "Nơi cấp",
                "short_name": "id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 21,
                "example": "TP HO CHI MINH"
            },
            {
                "name": "Số điện thoại",
                "short_name": "phone_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 22,
                "example": "0865627158"
            },
            {
                "name": "Mã KH",
                "short_name": "customer_code",
                "value_type": ValueType.STR,
                "urd_ref_id": 23,
                "example": "14248294"
            },
            {
                "name": "Số tiền bảng kê ngoại tệ",
                "short_name": "foreign_amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 24,
                "example": 100.00
            },
            {
                "name": "Loại tiền bảng kê ngoại tệ",
                "short_name": "foreign_currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 28,
                "example": "USD"
            },
            {
                "name": "Số tiền bảng kê ngoại tệ bằng chữ",
                "short_name": "foreign_amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 25,
                "example": "Một trăm đô la Mỹ"
            },
            {
                "name": "Số tiền bảng kê VND",
                "short_name": "vnd_amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 26,
                "example": 2298000
            },
            {
                "name": "Số tiền bảng kê VND bằng chữ",
                "short_name": "vnd_amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 27,
                "example": "Hai triệu, hai trăm chín mươi tám nghìn đồng"
            },
        ]
    },
    {
        "name": "Phiếu chi",
        "short_name": "phieu_chi",
        "code": "OCR07",
        "title": {
            "pattern": "Phiếu chi",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Người nhận",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "(CMND|CMT|GTTT|TTT|JTT|TTI)",
                "pattern_type": PatternType.RAW
            },
            {
                "pattern": "Địa chỉ",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "TO RECEIVE MONEY",
                "pattern_type": PatternType.REMOVE_ACCENT
            },
            {
                "pattern": "Kiêm (p|n)hiếu tính lãi",
                "pattern_type": PatternType.REMOVE_ACCENT
            }
        ],
        "key_values": [
            {
                "name": "Số bút toán",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "FT20318143645990"
            },
            {
                "name": "Ngày",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 2,
                "example": "13/11/2020"
            },
            {
                "name": "Tổng số tiền chi cho khách hàng",
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 3,
                "example": 502.58
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "Năm trăm linh hai Đô la Mỹ và năm mươi tám cent"
            },
            {
                "name": "Loại tiền tệ",
                "short_name": "currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "USD"
            },
            {
                "name": "Số tài khoản ghi nợ",
                "short_name": "credit_account",
                "value_type": ValueType.STR,
                "urd_ref_id": 6,
                "example": "USD1136100360135",
            },
            {
                "name": "Tên TK",
                "short_name": "account_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 7,
                "example": "TK TAM UNG TT WU USD - SB TAN PHAT"
            },
            {
                "name": "Số tiền ghi nợ TK",
                "short_name": "credit_amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 8,
                "example": 502.58,
            },
            {
                "name": "Người nhận tiền",
                "short_name": "receiver_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 14,
                "example": "NGUYEN NGOC THUY LINH"
            },
            {
                "name": "Nội dung",
                "short_name": "details",
                "value_type": ValueType.STR,
                "urd_ref_id": 15,
                "example": "CHI TRA WU KH NGUYEN NGOC THUY LINH, MTCN: 099-636-3711"
            },
            {
                "name": "Số CMT",
                "short_name": "id_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 16,
                "example": "C3952451"
            },
            {
                "name": "Địa chỉ",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 17,
                "example": "L15 CXVH BEN VAN DON, P6. Q.4"
            },
        ]
    },
    {
        # Có 2 loại to receive-customer receipt và to receive-agent receipt, khác title nhưng nội dung giống hệt nhau
        "name": "Phiếu nhận tiền",
        "short_name": "phieu_nhan_tien",
        "code": "OCR08",
        "title": {
            "pattern": "To Receive",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "(Receiver|Kecelver)",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Sender",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "MTCN",
                "pattern_type": PatternType.RAW
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "TO RECEIVE MONEY",
                "pattern_type": PatternType.REMOVE_ACCENT
            },
        ],
        "key_values": [
            {
                "name": "Mã số chuyển tiền",
                "short_name": "transfer_code",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "170-147-3652"
            },
            {
                "name": "Tên người nhận",
                "short_name": "receiver_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 2,
                "example": "NGUYEN VAN QUANG"
            },
            {
                "name": "Tên người gửi",
                "short_name": "sender_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "THUY THANH PHAM"
            },
            {
                "name": "Số tiền",
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 4,
                "example": 14371000.00
            },
            {
                "name": "Loại tiền tệ",
                "short_name": "currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "Vietnamese Dong"
            },
            {
                "name": "Ngày thực hiện",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 8,
                "example": "10/3/2023"
            },
        ]
    },
    {
        "name": "Giấy nộp tiền",
        "short_name": "giay_nop_tien",
        "code": "OCR09",
        "title": {
            "pattern": "Giấy nộp tiền",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Người nộp tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "CMND",
                "pattern_type": PatternType.RAW
            },
            {
                "pattern": "Số (tiền|nên) bằng chữ",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Số tài khoản",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "Người nhận tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Giấy rút tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "key_values": [
            {
                "name": "Số bút toán",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "TT2108400393"
            },
            {
                "name": "Ngày",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 2,
                "example": "25/03/2021"
            },
            {
                "name": "User",
                "short_name": "user_inputter",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "HUYENNT7"
            },
            {
                "name": "Người nộp tiền",
                "short_name": "depositor_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "VU THI HIEN"
            },
            {
                "name": "Số CMND/Hộ chiếu",
                "short_name": "id_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "001177007237"
            },
            {
                "name": "Số điện thoại",
                "short_name": "phone_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 6,
                "example": "0383369016"
            },
            {
                "name": "Số tiền bằng số",
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 7,
                "example": 226000000.00
            },
            {
                "name": "Đơn vị tiền tệ",
                "short_name": "currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "VND"
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 9,
                "example": "Hai trăm hai mươi sáu triệu đồng"
            },
            {
                "name": "Số tài khoản ghi có",
                "short_name": "credit_account",
                "value_type": ValueType.STR,
                "urd_ref_id": 10,
                "example": "04300014123476"
            },
            {
                "name": "Tên tài khoản ghi có",
                "short_name": "credit_account_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 11,
                "example": "TK TGTT VND VU THI HIEN."
            },
            {
                "name": "Nội dung",
                "short_name": "details",
                "value_type": ValueType.STR,
                "urd_ref_id": 12,
                "example": "VU THI HIEN NOP TK"
            },
            {
                "name": "Bảng hạch toán",
                "short_name": "table_accounting",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 13,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example": [
                            {
                                "name": "Hạch toán",
                                "short_name": "accounting_type",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 13.0,
                                "example": "TK Co" # TK No,
                            },
                            {
                                "name": "Số tài khoản",
                                "short_name": "account_number",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 13.1,
                                "example": "04300014123476"
                            },
                            {
                                "name": "Tên chủ tài khoản",
                                "short_name": "account_name",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 13.2,
                                "example": "TK TGTT VND VU THI HIEN."
                            },
                            {
                                "name": "Số tiền",
                                "short_name": "accounting_amount",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 13.3,
                                "example": 226000000.00,
                            },
                            {
                                "name":"Đơn vị tiền tệ",
                                "short_name": "accounting_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 13.4,
                                "example": "VN"
                            },
                        ]
                    }
                ]
            },
            {
                "name": "Mã khách hàng",
                "short_name": "customer_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 15,
                "example": "14123476"
            },
            {
                "name": "Ngày cấp CMT",
                "short_name": "id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 16,
                "example": "26/11/2015"
            },
            {
                "name": "Nơi cấp",
                "short_name": "id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 17,
                "example": "CCS DKQL CU TRU DLQG"
            },
            {
                "name": "Địa chỉ",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 18,
                "example": "SO NHA 29 TO 9A YEN HOA"
            },
            {
                "name": "Số tiền bằng số trên bảng kê",
                "short_name": "listing_amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 19,
                "example": 226000000
            },
            {
                "name": "Số tiền bằng chữ trên bảng kê",
                "short_name": "listing_amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 20,
                "example": "Hai trăm hai mươi sáu triệu đồng"
            },
        ]
    },
    {
        "name": "Giấy rút tiền",
        "short_name": "giay_rut_tien",
        "code": "OCR10",
        "title": {
            "pattern": "Giấy rút tiền",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Người nhận tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "CMND",
                "pattern_type": PatternType.RAW
            },
            {
                "pattern": "Số tiền bằng ch(ữ|o)",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Số tài khoả(n|i)",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "Người nộp tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Giấy nộp tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "key_values": [
            {
                "name": "Số bút toán",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "TT2108303358"
            },
            {
                "name": "Ngày giao dịch",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 2,
                "example": "24/03/2021"
            },
            {
                "name": "User",
                "short_name": "user_inputter",
                "value_type": ValueType.STR,
                "urd_ref_id": 22,
                "example": "VANTTT"
            },
            {
                "name": "Người lĩnh tiền",
                "short_name": "full_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "NGUYEN THI THUYEN"
            },
            {
                "name": "Nội dung",
                "short_name": "details",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "NGUYEN THI HUYEN RUT TIEN TK"
            },
            {
                "name": "Số tiền bằng số",
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 5.1,
                "example": 5000000.00
            },
            {
                "name": "Đơn vị tiền tệ",
                "short_name": "currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 5.2,
                "example": "VND"
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 5.3,
                "example": "Năm triệu đồng"
            },
            {
                "name": "CMND/Hộ chiếu",
                "short_name": "id_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 6,
                "example": "112368769"
            },
            {
                "name": "Ngày cấp",
                "short_name": "id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 7,
                "example": "15/08/2007"
            },
            {
                "name": "Nơi cấp",
                "short_name": "id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "HA NOI"
            },
            {
                "name": "Số điện thoại",
                "short_name": "phone_number",
                "value_type": ValueType.INT,
                "urd_ref_id": 9,
                "example": "0368987376"
            },
            {
                "name": "Địa chỉ",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 12,
                "example": "P MO LAO HA DONG"
            },
            {
                "name": "Số tài khoản ghi nợ",
                "short_name": "credit_account",
                "value_type": ValueType.STR,
                "urd_ref_id": 13,
                "example": "000000001991"
            },
            {
                "name": "Tên tài khoản ghi nợ",
                "short_name": "credit_account_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 14,
                "example": "NGUYEN THI HUYEN"
            },
            {
                "name": "Mã khách hàng",
                "short_name": "customer_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 21,
                "example": "13992729"
            },
            # {
            #     "name": "Bảng hạch toán",
            #     "short_name": "table_accounting",
            #     "value_type": ValueType.TABLE,
            #     "urd_ref_id": 10,
            #     "example": [
            #         {
            #             "name": "Row",
            #             "short_name": "row",
            #             "value_type": ValueType.LIST,
            #             "example": [
            #                 {
            #                     "name": "Hạch toán",
            #                     "short_name": "accounting_type",
            #                     "value_type": ValueType.STR,
            #                     "urd_ref_id": 10.0,
            #                     "example": "TK Co" # TK No,
            #                 },
            #                 {
            #                     "name": "Số tài khoản",
            #                     "short_name": "account_number",
            #                     "value_type": ValueType.STR,
            #                     "urd_ref_id": 10.1,
            #                     "example": "VND1000199990043"
            #                 },
            #                 {
            #                     "name": "Tên chủ tài khoản",
            #                     "short_name": "account_name",
            #                     "value_type": ValueType.STR,
            #                     "urd_ref_id": 13.2,
            #                     "example": "TK VND QUY CHINH KIM VAN"
            #                 },
            #                 {
            #                     "name": "Số tiền",
            #                     "short_name": "accounting_amount",
            #                     "value_type": ValueType.FLOAT,
            #                     "urd_ref_id": 13.3,
            #                     "example": 5000000.00,
            #                 },
            #                 {
            #                     "name":"Đơn vị tiền tệ",
            #                     "short_name": "accounting_currency",
            #                     "value_type": ValueType.STR,
            #                     "urd_ref_id": 13.4,
            #                     "example": "VND"
            #                 },
            #             ]
            #         }
            #     ]
            # },
            {
                "name": "Số tiền bằng số trên bảng kê",
                "short_name": "listing_amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 16,
                "example": 5000000
            },
            {
                "name": "Số tiền bằng chữ trên bảng kê",
                "short_name": "listing_amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 15,
                "example": "Năm triệu đồng"
            },
        ]
    },
    {
        "name": "Phiếu hạch toán giải ngân",
        "short_name": "phieu_hach_toan_giai_ngan",
        "code": "OCR11",
        "title": {
            "pattern": "Phiếu hạch toán giải ngân",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "TÊN TÀI KHOẢN",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "SỐ TIỀN",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Giải ngân",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [],
        "key_values": [
            {
                "name": "Số giao dịch",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 12,
                "example": "LD2033500209"
            },
            {
                "name": "Ngày hiệu lực HĐ",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 13,
                "example": "30/11/2020"
            },
            {
                "name": "Bảng hạch toán",
                "short_name": "table_accounting",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 1,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Loại giao dịch",
                                "short_name": "account_type",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 1.0,
                                "example": "TK Có" # TK Nợ
                            },
                            {
                                "name": "Số tài khoản",
                                "short_name": "account_number",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 1.1,
                                "example": "VND1142600060043"
                            },
                            {
                                "name": "Tên chủ tài khoản",
                                "short_name": "account_name",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 1.2,
                                "example": "TK CHO TT TIN DUNG KIM VAN"
                            },
                            {
                                "name": "Số tiền",
                                "short_name": "account_amount",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 1.3,
                                "example": 210000000.00
                            },
                            {
                                "name": "Đơn vị tiền tệ",
                                "short_name": "account_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 1.4,
                                "example": ""
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Nội dung",
                "short_name": "details",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "Giải ngân cho khách hàng PHAN THI LUAN"
            },
            {
                "name": "Số tiền bằng số",
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 6,
                "example": 210000000.00
            },
            {
                "name": "Đơn vị tiền tệ",
                "short_name": "currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 7,
                "example": "VND"
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "Hai tram muoi trieu dong"
            },
        ]
    },
    {
        "name": "Đề nghị vay vốn kiêm Hợp đồng cho vay, Hợp đồng bảo đảm và Khế ước nhận nợ",
        "short_name": "de_nghi_vay_von_kiem_hop_dong_cho_vay_hop_dong_bao_dam_va_khe_uoc_nhan_no",
        "title": {
            "pattern": "Đề nghị vay vốn kiêm Hợp đồng cho vay, Hợp đồn(\,)?(g bảo đảm)? (Tôn giáo\:)?(\(?(Mẫu biểu|Mẩu cầu|Mao viếu|Massiều)\:? 01\)?)?( (Ngày hiệu lực\:))?( (Lần ban hành\/sửa đổi\:))?(SeABank duri)? và Khế ước nhận (nợ)?",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [],
        "must_exclude_pattern": [],
        "key_values": [
            # =========== PHAN A ===========
            {
                "name": "Kính gửi",
                "short_name": "dear",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "Ngân hàng TMCP Đông Nam Á - SeABank Văn Quán (Sau đây gọi là Bên cho vay hoặc SeABank)",
            },
            {
                "name": "Địa chỉ",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 2,
                "example": "108 Nguyễn Khuyến Văn Quán Hà Đông hà Nội",
            },
            {
                "name": "Tên người đại diện",
                "short_name": "representative",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "Nguyễn Việt Anh",
            },
            {
                "name": "Chức vụ",
                "short_name": "position",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "Giám Đốc",
            },
            {
                "name": "Tên bên vay",
                "short_name": "borrower_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "Tạ Thị Hường",
            },
            {
                "name": "GTTT/Hộ chiếu bên vay",
                "short_name": "borrower_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 6,
                "example": "001183018747",
            },
            {
                "name": "Ngày cấp CMND bên vay",
                "short_name": "id_date_issue",
                "value_type": ValueType.DATE,
                "urd_ref_id": 7,
                "example": "20/09/2016",
            },
            {
                "name": "Nơi cấp CMT bên vay",
                "short_name": "id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "CCS",
            },
            {
                "name": "Địa chỉ bên vay",
                "short_name": "borrower_address",
                "value_type": ValueType.STR,
                "urd_ref_id": 9,
                "example": "P101 TT Dược tổ 34 Đại Kim, Hoàng Mai, Hà Nội",
            },
            {
                "name": "Số điện thoại bên vay",
                "short_name": "borrower_phone_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 10,
                "example": "0912368383",
            },
            {
                "name": "Số tài khoản bên vay",
                "short_name": "borrower_account_num",
                "value_type": ValueType.STR,
                "urd_ref_id": 11,
                "example": "05500014696769",
            },
            {
                "name": "Số tiền vay",
                "short_name": "amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 12,
                "example": 640000000,
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 13,
                "example": "Sáu trăm bốn mươi triệu đồng",
            },
            # =========== CHECKMARK ===========
            {
                "name": "Mục đích vay",
                "short_name": "debt_purpose",
                "value_type": ValueType.STR,
                "urd_ref_id": 14,
                "example": "Bù đắp phần vốn tự có, nguồn tài chính mà bên vay đã sử dụng để thực hiện phương án phục vụ đời sống",
            },
            # =================================
            {
                "name": "Thời hạn vay",
                "short_name": "debt_duration",
                "value_type": ValueType.STR,
                "urd_ref_id": 15,
                "example": "23 ngày"
            },
            {
                "name": "Ngày bắt đầu vay",
                "short_name": "debt_start_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 16,
                "example": "14/07/2020"
            },
            {
                "name": "Ngày kết thúc vay",
                "short_name": "debt_end_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 17,
                "example": "05/08/2020"
            },
            {
                "name": "Phương thức cho vay",
                "short_name": "debt_mode",
                "value_type": ValueType.STR,
                "urd_ref_id": 18,
                "example": "Cho vay từng lần"
            },
            {
                "name": "Tổng nhu cầu vốn",
                "short_name": "total_capital_need",
                "value_type": ValueType.INT,
                "urd_ref_id": 19,
                "example": 640000000
            },
            {
                "name": "Vốn tự có",
                "short_name": "equity_capital",
                "value_type": ValueType.INT,
                "urd_ref_id": 21,
                "example": 0
            },
            {
                "name": "Vốn đề xuất vay SeABank",
                "short_name": "proposed_capital",
                "value_type": ValueType.INT,
                "urd_ref_id": 22,
                "example": 640000000
            },
            # =========== CHECKMARK ===========
            {
                "name": "Nguồn trả nợ",
                "short_name": "debt_repayment_source",
                "value_type": ValueType.STR,
                "urd_ref_id": 20,
                "example": "Sử dụng khoản tiền gửi tại SeABank được dùng làm tài sản bảo đảm"
            },
            # =================================
            {
                "name": "Nhu cầu vốn",
                "short_name": "capital_need",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 23,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example": [
                            {
                                "name": "Số thứ tự",
                                "short_name": "ordinal_number",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 23.1,
                                "example": 1
                            },
                            {
                                "name": "Loại hàng",
                                "short_name": "product_type",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 23.2,
                                "example": "Cây cảnh",
                            },
                            {
                                "name": "Số lượng",
                                "short_name": "product_quantity",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 24,
                                "example": 1,
                            },
                            {
                                "name": "Đơn giá",
                                "short_name": "amount",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 27,
                                "example": 640000000,
                            },
                            {
                                "name": "Thành tiền",
                                "short_name": "total_amount",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 26,
                                "example": 640000000
                            },
                        ]
                    },
                ]
            },
            {
                "name": "Tổng nhu cầu vốn",
                "short_name": "total_capital_need_in_tab",
                "value_type": ValueType.INT,
                "urd_ref_id": 25,
                "example": 640000000
            },
            {
                "name": "Lãi suất",
                "short_name": "interest_rate",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 28,
                "example": 6.8
            },
            # =========== CHECKMARK ===========
            {
                "name": "Phương thức giải ngân sau khi xử lý tài sản bảo đảm",
                "short_name": "disbursement_method",
                "value_type": ValueType.STR,
                "urd_ref_id": 29,
                "example": "Giải ngân vào tài khoản Bên vay tại SeABank (đã nêu rõ tại mục I) (Chỉ áp dụng đối với mục đích vay: Bù đắp phần vốn tự có, nguồn tài chính mà bên vay đã sử dụng để thực hiện phương án phục vụ đời sống)",
            },
            # =================================
            {
                "name": "Thông tin tài sản đảm bảo",
                "short_name": "guarantee_infor",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 30,
                "example": [
                    { 
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "STT",
                                "short_name": "collateral_ordinal_number",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 30.1,
                                "example": 1,
                            },
                            {
                                "name": "Số hiệu tài sản đảm bảo",
                                "short_name": "collateral_id",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 30.2,
                                "example": "SC2174785",
                            },
                            {
                                "name": "Số dư tiền gửi tài sản đảm bảo",
                                "short_name": "collateral_balance",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 31,
                                "example": 700000000,
                            },
                            {
                                "name": "Chủ sở hữu tài sản đảm bảo",
                                "short_name": "collateral_owner",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 32,
                                "example": "Tạ Thị Hường",
                            },
                            {
                                "name": "Kỳ hạn tài sản đảm bảo",
                                "short_name": "collateral_duration",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 36,
                                "example": "03 thang",
                            },
                            {
                                "name": "Ngày phát hành tài sản đảm bảo",
                                "short_name": "collateral_issue_date", 
                                "value_type": ValueType.DATE,
                                "urd_ref_id": 33,
                                "example": "05/05/2020",
                            },
                            {
                                "name": "Ngày đến hạn tài sản đảm bảo",
                                "short_name": "collateral_expiration",
                                "value_type": ValueType.DATE,
                                "urd_ref_id": 34,
                                "example": "05/08/2020",
                            },
                            {
                                "name": "Đơn vị phát hành",
                                "short_name": "collateral_issuer",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 35,
                                "example": "SeABank Văn Quán",
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Tổng số dư tiền gửi tài sản bảo đảm bằng số",
                "short_name": "collateral_amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 37,
                "example": 700000000,
            },
            {
                "name": "Tổng số dư tiền gửi tài sản bảo đảm bằng chữ",
                "short_name": "collateral_amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 38,
                "example": "Bảy trăm triệu đồng chẵn"
            },
            # =========== CHECKMARK ===========
            {
                "name": "Bên hoàn trả tiền",
                "short_name": "pay_back",
                "value_type": ValueType.STR,
                "urd_ref_id": 39,
                "example": "Bên vay",
            },
            # =================================
            {
                "name": "Ngày tháng (phần A bên vay ký xác nhận)",
                "short_name": "signature_date_borrower",
                "value_type": ValueType.DATE,
                "urd_ref_id": 41,
                "example": "13/07/2020"
            },
            # =========== PHAN B ===========
            {
                "name": "Xác nhận số tiền vay",
                "short_name": "confirm_amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 44,
                "example": 640000000,
            },
            # ============= CHECKMARK==============
            {
                "name": "Xác nhận mục đích vay",
                "short_name": "confirm_purpose",
                "value_type": ValueType.STR,
                "urd_ref_id": 45,
                "example": "Bù đắp phần vốn tự có, nguồn tài chính mà bên vay đã sử dụng để thực hiện phương án phục vụ đời sống",
            },
            # =================================
            {
                "name": "Xác nhận lãi suất",
                "short_name": "confirm_interest_rate",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 46,
                "example": 6.8,
            },
            {
                "name": "Xác nhận thời hạn vay",
                "short_name": "confirm_debt_duration",
                "value_type": ValueType.STR,
                "urd_ref_id": 47,
                "example": "23 ngày",
            },
            {
                "name": "Xác nhận ngày bắt đầu vay",
                "short_name": "confirm_debt_start_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 48,
                "example": "14/07/2020",
            },
            {
                "name": "Xác nhận ngày kết thúc vay",
                "short_name": "confirm_debt_end_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 49,
                "example": "05/08/2020",
            },
            {
                "name": "Xác nhận tài sản đảm bảo",
                "short_name": "confirm_collateral",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 50,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Xác nhận tài sản đảm bảo stt",
                                "short_name": "confirm_collateral_ordinal_number",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 50.1,
                                "example": 1,
                            },
                            {
                                "name": "Xác nhận số hiệu tài sản đảm bảo",
                                "short_name": "confirm_collateral_serial",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 50.2,
                                "example": "SC2174785",
                            },
                            {
                                "name": "Xác nhận chủ sở hữu tài sản đảm bảo",
                                "short_name": "confirm_collateral_owner",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 51,
                                "example": "Tạ Thị Hường"
                            },
                            {
                                "name": "Xác nhận số dư tiền gửi tài sản đảm bảo",
                                "short_name": "confirm_collateral_balance",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 52,
                                "example": 700000000,
                            },
                            {
                                "name": "Xác nhận ngày phát hành tài sản đảm bảo",
                                "short_name": "confirm_collateral_issue_date",
                                "value_type": ValueType.DATE,
                                "urd_ref_id": 53,
                                "example": "05/05/2020",
                            },
                            {
                                "name": "Xác nhận ngày đến hạn tài sản đảm bảo",
                                "short_name": "confirm_collateral_expiration",
                                "value_type": ValueType.DATE,
                                "urd_ref_id": 54,
                                "example": "05/08/2020", 
                            }, 
                            {
                                "name": "Xác nhận đơn vị phát hành",
                                "short_name": "confirm_collateral_issuer",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 55,
                                "example": "SeABank Văn Quán",
                            },
                        ]
                    },
                ]
            },
            {
                "name": "Xác nhận tổng số dư tiền gửi tài sản đảm bảo bằng số",
                "short_name": "confirm_collateral_amount",
                "value_type": ValueType.INT,
                "urd_ref_id": 56,
                "example": 700000000,
            },
            {
                "name": "Xác nhận tổng số dư tiền gửi tài sản đảm bảo bằng chữ",
                "short_name": "confirm_collateral_amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 57,
                "example": "Bảy trăm triệu đồng chẵn",
            },
            {
                "name": "Xác nhận ngày giải ngân",
                "short_name": "confirm_disbursement",
                "value_type": ValueType.DATE,
                "urd_ref_id": 58,
                "example": "13/07/2020",
            },
            {
                "name": "Ngày tháng (phần B bên ngân hàng ký xác nhận)",
                "short_name": "signature_date_bank",
                "value_type": ValueType.DATE,
                "urd_ref_id": 42,
                "example": "13/07/2020"
            },
            # =========== PHAN C ===========
            {
                "name": "Thẩm định số tiền vay",
                "short_name": "debt_appraisal",
                "value_type": ValueType.INT,
                "urd_ref_id": 59,
                "example": 640000000
            },
            # =========== CHECKMARK ===========
            {
                "name": "Thẩm định mục đích",
                "short_name": "purpose_appraisal",
                "value_type": ValueType.STR,
                "urd_ref_id": 60,
                "example": "Bù đắp phần vốn tự có, nguồn tài chính mà bên vay đã sử dụng để thực hiện phương án phục vụ đời sống",
            },
            # =================================
            {
                "name": "Thẩm định lãi suất",
                "short_name": "interest_rate_appraisal",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 61,
                "example": 6.8,
            },
            {
                "name": "Thẩm định thời hạn vay",
                "short_name": "debt_duration_appraisal",
                "value_type": ValueType.STR,
                "urd_ref_id": 62,
                "example": "23 ngày",
            },
            {
                "name": "Thẩm định ngày bắt đầu vay",
                "short_name": "debt_start_date_appraisal",
                "value_type": ValueType.DATE,
                "urd_ref_id": 63,
                "example": "14/07/2020",
            },
            {
                "name": "Thẩm định ngày kết thúc vay",
                "short_name": "debt_end_date_appraisal",
                "value_type": ValueType.DATE,
                "urd_ref_id": 64,
                "example": "05/08/2020",
            },
            {
                "name": "Thẩm định tài sản bảo đảm",
                "short_name": "collateral_appraisal",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 65,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Thẩm định STT tài sản đảm bảo",
                                "short_name": "collateral_ordial_number_appraisal", 
                                "value_type": ValueType.INT,
                                "urd_ref_id": 65.1,
                                "example": 1,
                            },
                            {
                                "name": "Thẩm định số hiệu tài sản đảm bảo",
                                "short_name": "collateral_serial_appraisal",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 65.2,
                                "example": "SC2174785",
                            },
                            {
                                "name": "Thẩm định chủ sở hữu tài sản đảm bảo",
                                "short_name": "collateral_owner_appraisal",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 66,
                                "example": "Tạ Thị Hường",
                            },
                            {
                                "name": "Thẩm định số dư tiền gửi tài sản đảm bảo",
                                "short_name": "collateral_balance_appraisal",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 67,
                                "example": 700000000,
                            },
                            {
                                "name": "Thẩm định ngày phát hành tài sản đảm bảo",
                                "short_name": "collateral_issue_date_appraisal",
                                "value_type": ValueType.DATE,
                                "urd_ref_id": 68,
                                "example": "05/05/2020",
                            },
                            {
                                "name": "Thẩm định ngày đến hạn tài sản đảm bảo",
                                "short_name": "collateral_expiration_appraisal",
                                "value_type": ValueType.DATE,
                                "urd_ref_id": 69,
                                "example": "05/08/2020",
                            },
                            {
                                "name": "Thẩm định đơn vị phát hành tài sản đảm bảo", 
                                "short_name": "collateral_issuer_appraisal",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 70,
                                "example": "SeABank Văn Quán",
                            },
                        ]
                    },
                ]
            },
            {
                "name": "Thẩm định tổng số dư tiền gửi tài sản đảm bảo bằng số",
                "short_name": "collateral_amount_appraisal",
                "value_type": ValueType.INT,
                "urd_ref_id": 71,
                "example": 700000000,
            },
            {
                "name": "Thẩm định tổng số dư tiền gửi tài sản đảm bảo bằng chữ",
                "short_name": "guarantee_appraisal_amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 72,
                "example": "Bảy trăm triệu đồng chẵn",
            },
            {
                "name": "Phương thức giải ngân",
                "short_name": "disbursement_mode",
                "value_type": ValueType.STR,
                "urd_ref_id": 78,
                "example": "Định kỳ",
            },
            {
                "name": "Tỷ lệ cho vay",
                "short_name": "ltv_ratio",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 73,
                "example": 0,
            },
            # =========== CHECKMARK ===========
            {
                "name": "Đánh giá các điều kiện cho vay",
                "short_name": "loan_condition_evaluate",
                "value_type": ValueType.STR,
                "urd_ref_id": 79,
                "example": "Đáp ứng"
            },
            # =================================
            {
                "name": "Tổng số dư theo SP SeaValue",
                "short_name": "total_seavalue_loan",
                "value_type": ValueType.INT,
                "urd_ref_id": 80,
                "example": 0
            },
            # =========== CHECKMARK ===========
            {
                "name": "Thẩm quyền phê duyệt khoản vay",
                "short_name": "loan_approve_authority",
                "value_type": ValueType.STR,
                "urd_ref_id": 81,
                "example": "Thuộc thẩm quyền phê duyệt của ĐVKD"
            },
            # =================================
            {
                "name": "Ngày nhận đủ hồ sơ tại GDV",
                "short_name": "document_receipt_date_GDV",
                "value_type": ValueType.DATE,
                "urd_ref_id": 77,
                "example": "13/07/2020",
            },
            {
                "name": "Ngày hoàn thành tại GDV",
                "short_name": "document_complete_date_GDV",
                "value_type": ValueType.DATE,
                "urd_ref_id": 82,
                "example": "13/07/2020",
            },
            {
                "name": "Ngày nhận đủ hồ sơ tại TN GDV",
                "short_name": "document_receipt_date_TNGDV",
                "value_type": ValueType.DATE,
                "urd_ref_id": 83,
                "example": "13/07/2020",
            },
            {
                "name": "Ngày hoàn thành tại TN GDV",
                "short_name": "document_complete_date_TNGDV",
                "value_type": ValueType.DATE,
                "urd_ref_id": 84,
                "example": "13/07/2020",
            },
        ]
    },
    {
        "name": "Giấy gửi tiền tiết kiệm",
        "short_name": "giay_gui_tien_tiet_kiem",
        "code": "OCR13",
        "title": {
            "pattern": "Giấy gửi tiết kiệm",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Người gửi tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Sản phẩm tiền gửi",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Kỳ",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "hạn",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "hình thức nhận lãi",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [],
        "key_values": [
            {
                "name": "Số giao dịch",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "000048010630"
            },
            {
                "name": "Số sổ",
                "short_name": "book_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 10,
                "example": "AP0039802"
            },
            {
                "name": "Ngày giao dịch",
                "short_name": "issuee_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 2,
                "example": "25/03/2021"
            },
            {
                "name": "User",
                "short_name": "user",
                "value_type": ValueType.STR,
                "urd_ref_id": 23,
                "example": "DOANBT"
            },
            {
                "name": "Tên người gửi",
                "short_name": "name",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "NGUYEN THI NO"
            },
            {
                "name": "Số GTTT",
                "short_name": "id_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "013055903"
            },
            {
                "name": "Ngày cấp",
                "short_name": "id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 5,
                "example": "26/03/2008"
            },
            {
                "name": "Nơi cấp",
                "short_name": "issuee_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 6,
                "example": "HA NOI"
            },
            {
                "name": "Mã khách hàng",
                "short_name": "customer_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 7,
                "example": "15317239"
            },
            {
                "name": "Địa chỉ",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "SO 204 N3 TO 21 PHUONG DAI KIM QUAN HOANG MAI HA NOI"
            },
            {
                "name": "Số điện thoại",
                "short_name": "phone_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 9,
                "example": "0373212195"
            },
            {
                "name": "Số tiền bằng số",  # ĐỀ NGHỊ GỬI TIẾT KIỆM SỐ TIỀN
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 11,
                "example": 185578000.00
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 12,
                "example": "Một trăm tám mươi lăm triêu, năm trăm bảy mươi tám nghìn đồng"
            },
            {
                "name": "Lãi suất",
                "short_name": "interest_rate",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 13,
                "example": 6.39
            },
            {
                "name": "Sản phẩm tiền gửi", 
                "short_name": "product_type",
                "value_type": ValueType.STR,
                "urd_ref_id": 14,
                "example": "Khác"
            },
            {
                "name": "Kỳ hạn",
                "short_name": "product_term",
                "value_type": ValueType.STR,
                "urd_ref_id": 15,
                "example": "36 thang/18 thang/15 thang/13 thang/12 thang"
            },
            {
                "name": "Hình thức gửi tiền",
                "short_name": "deposite_method",
                "value_type": ValueType.STR,
                "urd_ref_id": 16,
                "example": "1 - Tiền mặt"
            },
            {
                "name": "Hình thức nhận lãi",
                "short_name": "receiving_interest_method",
                "value_type": ValueType.STR,
                "urd_ref_id": 17,
                "example": "1 - Tiền mặt"
            },
            {
                "name": "Nội dung",
                "short_name": "details",
                "value_type": ValueType.STR,
                "urd_ref_id": 21,
                "example": "Gửi tiết kiệm"
            },
            {
                "name": "Bảng hạch toán",
                "short_name": "table_accounting",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 22,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example": [
                            {
                                "name": "Hạch toán",
                                "short_name": "accounting_type",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 22.0,
                                "example": "TK No" # TK Co
                            },
                            {
                                "name": "Số tài khoản",
                                "short_name": "account_number",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 22.1,
                                "example": "VND1000104500043"
                            },
                            {
                                "name": "Tên tài khoản",
                                "short_name": "account_name",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 22.2,
                                "example": "TK VND TELLER DOANBT"
                            },
                            {
                                "name": "Số tiền",
                                "short_name": "account_amount",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 22.3,
                                "example": 185578000.00,
                            },
                            {
                                "name":"Loại tiền",
                                "short_name": "accounting_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 22.4,
                                "example": "VND"
                            },
                        ]
                    },
                ]
            },
        ]
    },
    {
        "name": "Phiếu chi tất toán sổ tiết kiệm",
        "short_name": "phieu_chi_tat_toan_so_tiet_kiem",
        "code": "OCR14",
        "title": {
            "pattern": "Phiếu chi tất toán sổ tiết kiệm",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Người nhận tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "TỪ NGÀY",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "ĐẾN NGÀY",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "SỐ NGÀY",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "SỐ DƯ",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "LÃI SUẤT",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "TIỀN LÃI",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "Kiêm phiếu tính lãi không kỳ hạn",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "key_values": [
            {
                "name": "Sổ giao dịch",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "000049508637"
            },
            {
                "name": "Ngày giao dịch",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 2,
                "example": "25/03/2021"
            },
            {
                "name": "User",
                "short_name": "user_inputter",
                "value_type": ValueType.STR,
                "urd_ref_id": 20,
                "example": "DOANBT"
            },
            {
                "name": "Tên người nhận tiền",
                "short_name": "receiver_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "NGUYEN THI NO"
            },
            {
                "name": "Số CMND",
                "short_name": "customer_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "001201000770"
            },
            {
                "name": "Địa chỉ",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "SO 204 N3 TO 21 PHUONG DAI KIM QUAN HOANG MAI HA NOI"
            },
            {
                "name": "Số sổ",
                "short_name": "book_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 6,
                "example": "SC2279320"
            },
            {
                "name": "Kỳ hạn",
                "short_name": "product_term",
                "value_type": ValueType.STR,
                "urd_ref_id": 7,
                "example": "6 thang"
            },
            {
                "name": "Sản phẩm",
                "short_name": "product_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "TIET KIEM PHAT LOC"
            },
            {
                "name": "Bảng lãi suất",
                "short_name": "interest_rate_table",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 9,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Lãi suất",
                                "short_name": "interest_rate",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 9.1,
                                "example": 6.25
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Tổng số tiền thanh toán còn lại",
                "short_name": "amount",
                "value_type": ValueType.FLOAT,
                "urd_ref_id": 10,
                "example": 82479452.0
            },
            {
                "name": "Đơn vị tiền tệ",
                "short_name": "currency",
                "value_type": ValueType.STR,
                "urd_ref_id": 10.1,
                "example": "VND"
            },
            {
                "name": "Số tiền bằng chữ",
                "short_name": "amount_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 11,
                "example": "Tám mươi hai triệu, bốn trăm bảy mươi chín nghìn, bốn trăm năm mươi hai đồng"
            },
            {
                "name": "Mã khách hàng",
                "short_name": "customer_code",
                "value_type": ValueType.STR,
                "urd_ref_id": 15,
                "example": "15317239"
            },
            {
                "name": "Ngày cấp",
                "short_name": "id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 16,
                "example": "26/03/2008"
            },
            {
                "name": "Nơi cấp",
                "short_name": "id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 17,
                "example": "HA NOI"
            },
            {
                "name": "Bảng hạch toán",
                "short_name": "table_accounting",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 18,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example": [
                            {
                                "name": "Hạch toán",
                                "short_name": "accounting_type",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 18.0,
                                "example": "TK No" # TK Co
                            },
                            {
                                "name": "Số tài khoản",
                                "short_name": "account_number",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 18.1,
                                "example": "000049508637"
                            },
                            {
                                "name": "Tên tài khoản",
                                "short_name": "account_name",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 18.2,
                                "example": "NGUYEN THI NO PL6T"
                            },
                            {
                                "name": "Số tiền",
                                "short_name": "account_amount",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 18.3,
                                "example": 82479452.00,
                            },
                            {
                                "name":"Loại tiền",
                                "short_name": "accounting_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 18.4,
                                "example": "VND"
                            },
                        ]
                    },
                ]
            },
        ]
    },
    {
        "name": "Bảng kê tính lãi",
        "short_name": "bang_ke_tinh_lai",
        "code": "OCR15",
        "title": {
            "pattern": "Bảng kê tính lãi",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Từ ngày",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Đến ngày",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Số ngày",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Số (d|b)ư",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Lãi suất",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Tiền lãi",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
        ],
        "must_exclude_pattern": [
            {
                "pattern": "Phiếu chi",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
        ],
        "key_values": [
            {
                "name": "Sổ giao dịch",
                "short_name": "ref",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "000041410264"
            },
            {
                "name": "Ngày giao dịch",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 2.1,
                "example": "24/03/2021"
            },
            {
                "name": "User",
                "short_name": "user_inputter",
                "value_type": ValueType.STR,
                "urd_ref_id": 2.2,
                "example": "VANTTT"
            },
            {
                "name": "Tên khách hàng",
                "short_name": "customer_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "DAO THI VIET ANH"
            },
            {
                "name": "Số GTTT",
                "short_name": "customer_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 4,
                "example": "026191000486"
            },
            {
                "name": "Địa chỉ",
                "short_name": "address",
                "value_type": ValueType.STR,
                "urd_ref_id": 5,
                "example": "P3146 CT12A KIM VAN KIM LU QUAN HOANG MAI HA NOI"
            },
            {
                "name": "Số sổ",
                "short_name": "book_number",
                "value_type": ValueType.STR,
                "urd_ref_id": 6,
                "example": "AP0034308"
            },
            {
                "name": "Kỳ hạn",
                "short_name": "product_term",
                "value_type": ValueType.STR,
                "urd_ref_id": 7,
                "example": "36 thang"
            },
            {
                "name": "Tên sản phẩm",
                "short_name": "product_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "TIEN GUI AN PHAT"
            },
            {
                "name": "Bảng lãi suất",
                "short_name": "interest_rate_table",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 9,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Lãi suất",
                                "short_name": "interest_rate",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 9.1,
                                "example": 0.1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Bảng hạch toán",
                "short_name": "table_accounting",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 13,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example": [
                            {
                                "name": "Hạch toán",
                                "short_name": "accounting_type",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 13.0,
                                "example": "TK No" # TK Co
                            },
                            {
                                "name": "Số tài khoản",
                                "short_name": "account_number",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 18.1,
                                "example": "000041410264"
                            },
                            {
                                "name": "Tên tài khoản",
                                "short_name": "account_name",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 18.2,
                                "example": "DAO THI VIET ANH AP"
                            },
                            {
                                "name": "Số tiền",
                                "short_name": "account_amount",
                                "value_type": ValueType.FLOAT,
                                "urd_ref_id": 18.3,
                                "example": 230031507.00,
                            },
                            {
                                "name":"Loại tiền",
                                "short_name": "accounting_currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 18.4,
                                "example": "VND"
                            },
                        ]
                    },
                ]
            },
        ]
    },
    {
        "name": "Phiếu điều chuyển tiền mặt nội bộ",
        "short_name": "phieu_dieu_chuyen_tien_mat_noi_bo",
        "code": "OCR16",
        "title": {
            "pattern": "Phiếu điều chuyển tiền mặt nội bộ",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [],
        "must_exclude_pattern": [],
        "key_values": [
            {
                "name": "Người giao tiền",
                "short_name": "deliver_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 1,
                "example": "Mai Thị Kiều Trang",
            },
            {
                "name": "Ngày",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 7,
                "example": "18/8/2020"
            },
            {
                "name": "CMND/ Hộ chiếu/CCCD người giao",
                "short_name": "deliver_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 8,
                "example": "101247336",
            },
            {
                "name": "Nơi cấp CMT người giao tiền",
                "short_name": "deliver_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 17,
                "example": "CA Quảng Ninh",
            },
            {
                "name": "Ngày cấp CMT người giao tiền",
                "short_name": "deliver_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 18,
                "example": "16/03/2012"
            },
            {
                "name": "Người nhận tiền",
                "short_name": "receiver_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 9,
                "example": "Nguyễn Thị Ngọc Quế",
            },
            {
                "name": "CMND/ Hộ chiếu/CCCD người nhận tiển",
                "short_name": "receiver_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 10,
                "example": "013314860",
            },
            {
                "name": "Nơi cấp CMT người nhận tiền",
                "short_name": "receiver_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 19,
                "example": "CA Hà Nội",
            },
            {
                "name": "Ngày cấp CMT người nhận tiền",
                "short_name": "receiver_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 20,
                "example": "12/11/2010"
            },
            {
                "name": "Bảng giao dịch",
                "short_name": "table_transaction",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 2,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Loại tiền tệ",
                                "short_name": "currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 2.1,
                                "example": "VND"
                            },
                            {
                                "name": "Số tiền bằng số",
                                "short_name": "amount",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 2.2,
                                "example": 6000000
                            },
                            {
                                "name": "Số tiền bằng chữ",
                                "short_name": "amount_text",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 2.3,
                                "example": "Sáu triệu đồng chẵn",
                            },
                        ]
                    }
                ]
            },
        ]
    },
    {
        "name": "Phiếu chi của nghiệp vụ Lệnh điều chuyển hàng đặc biệt",
        "short_name": "phieu_chi_cua_nghiep_vu_lenh_dieu_chuyen_hang_dac_biet",
        "code": "OCR17",
        "title": {
            "pattern": "PHIẾU CHI",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [],
        "must_exclude_pattern": [],
        "key_values": [
            {
                "name": "Ngày tháng",
                "short_name": "issue_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 1,
                "example": "25/01/2021"
            },
            {
                "name": "Họ tên người nhận tiền",
                "short_name": "receiver_name",
                "value_type": ValueType.STR,
                "urd_ref_id": 2,
                "example": "Nguyễn Thị Hoà Hải",
            },
            {
                "name": "CMND/Hộ chiếu",
                "short_name": "receiver_id",
                "value_type": ValueType.STR,
                "urd_ref_id": 3,
                "example": "034179009179",
            },
            {
                "name": "Ngày cấp",
                "short_name": "receiver_id_date",
                "value_type": ValueType.DATE,
                "urd_ref_id": 23,
                "example": "05/07/2020"
            },
            {
                "name": "Nơi cấp",
                "short_name": "receiver_id_place",
                "value_type": ValueType.STR,
                "urd_ref_id": 24,
                "example": "CCSDKQLCTVDLQGVDC",
            },
            {
                "name": "Bảng giao dịch",
                "short_name": "table_transaction",
                "value_type": ValueType.TABLE,
                "urd_ref_id": 5,
                "example": [
                    {
                        "name": "Row",
                        "short_name": "row",
                        "value_type": ValueType.LIST,
                        "example":[
                            {
                                "name": "Loại tiền",
                                "short_name": "currency",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 5.1,
                                "example": "VND"
                            },
                            {
                                "name": "Tổng số",
                                "short_name": "amount",
                                "value_type": ValueType.INT,
                                "urd_ref_id": 5.2,
                                "example": 280510556
                            },
                            {
                                "name": "Số tiền bằng chữ",
                                "short_name": "amount_text",
                                "value_type": ValueType.STR,
                                "urd_ref_id": 5.2,
                                "example": "Hai Trăm Tám Mươi Triệu Năm Trăm Mười Nghìn Năm Trăm Năm Mươi Sáu Đồng Chẵn",
                            },
                        ]
                    }
                ]
            },
            {
                "name": "Số tiền bằng số bảng kê các loại tiền chi VND",
                "short_name": "amount_vnd_total",
                "value_type": ValueType.INT,
                "urd_ref_id": 20.1,
                "example": 280510556
            },
            {
                "name": "Số tiền bằng chữ bảng kê các loại tiền chi VND",
                "short_name": "amount_vnd_total_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 20.2,
                "example": "Hai Trăm Tám Mươi Triệu Năm Trăm Mười Nghìn Năm Trăm Năm Mươi Sáu Đồng Chẵn",
            },
            {
                "name": "Số tiền bằng số bảng kê các loại tiền chi USD",
                "short_name": "amount_usd_total",
                "value_type": ValueType.INT,
                "urd_ref_id": 21.1,
                "example": 4326
            },
            {
                "name": "Số tiền bằng chữ bảng kê các loại tiền chi USD",
                "short_name": "amount_usd_total_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 21.2,
                "example": "Bốn Nghìn Ba Trăm Hai Mươi Sáu đô la mỹ chẵn",
            },
            {
                "name": "Số tiền bằng số bảng kê các loại tiền chi EUR",
                "short_name": "amount_eur_total",
                "value_type": ValueType.INT,
                "urd_ref_id": 22.1,
                "example": 6245
            },
            {
                "name": "Số tiền bằng chữ bảng kê các loại tiền chi EUR",
                "short_name": "amount_eur_total_text",
                "value_type": ValueType.STR,
                "urd_ref_id": 22.2,
                "example": "Sáu Nghìn Hai Trăm Bốn Mươi Lăm euro chẵn",
            }
        ]
    },
    {
        "name": "Đơn đề nghị rút tiền sổ tiết kiệm",
        "short_name": "don_de_nghi_rut_tien_so_tiet_kiem",
        "title": {
            "pattern": "Đơn đề nghị rút tiền sổ tiết kiệm",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Người đề nghị",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Số tiền rút",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "rút tiền sổ tiết kiệm",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [],
        "key_values": []
    },
    {
        "name": "Phiếu chi rút tiền sổ tiết kiệm",
        "short_name": "phieu_chi_rut_tien_so_tiet_kiem",
        "title": {
            "pattern": "Phiếu chi rút tiền sổ tiết kiệm",
            "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE,
        },
        "must_include_pattern": [
            {
                "pattern": "Kiêm phiếu tính lãi không kỳ hạn",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "Người nhận tiền",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "TỪ NGÀY",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "ĐẾN NGÀY",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "SỐ NGÀY",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "SỐ DƯ",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "LÃI SUẤT",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            },
            {
                "pattern": "TIỀN LÃI",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "must_exclude_pattern": [
            {
                "pattern": "tất toán",
                "pattern_type": PatternType.REMOVE_ACCENT_AND_LOWERCASE
            }
        ],
        "key_values": []
    }
]

OCR_TYPE_INIT = [
    {
        "name": "Chứng từ Seabank",
        "short_name": "sb_document",
        "file_types": SB_KV_TYPE_INIT
    }
]
