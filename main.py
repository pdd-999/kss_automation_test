from random import uniform
import requests
import json
import os
import glob
import tqdm
import shutil
from form_spec import SB_KV_TYPE_INIT
import sys
import docbase
import unicodedata
import unidecode
import itertools
SAVE_PATH = "bo_chung_tu_signature"
shutil.rmtree('bo_chung_tu_signature', ignore_errors=True)
os.makedirs(SAVE_PATH, exist_ok=True)

def get_id(file_path):
    url = "http://35.80.29.178:8989/api/ocr_file/"

    payload={}
    file_name = file_path.split('/')[-1]
    ext = file_name.split('.')[-1]
    files=[
        ('file',(file_name,open(file_path,'rb'),f'image/{ext}'))
    ]
    headers = {
        'Authorization': 'Token bdcad6da12cdd8827c3913ae464143a906b822b2'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return json.loads(response.text)['output']['id'], file_name.replace(f'.{ext}','')

def process_bo_chung_tu(id, file_name, file_type):
    url = f"http://35.80.29.178:8989/api/chung_tu_detail/{id}__0:0/"

    payload = ""
    headers = {
        'Authorization': 'Token bdcad6da12cdd8827c3913ae464143a906b822b2',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    dict_response = json.loads(response.text)['output']
    # with open(f"{SAVE_PATH}/{file_type}/{file_name}.json", 'w', encoding='utf-8') as f:
    #     json.dump(dict_response, f, ensure_ascii=False, indent=4)
    return dict_response

def process_get_id(file_path):
    id, file_name = get_id(file_path)
    file_type = file_path.split('/')[2]
    file_info = {
        'file_type': file_type,
        'file_name': file_name
    }
    return (id, file_info)

def process_get_bo_chung_tu(item):
    id, file_name, file_type = item
    dict_response = process_bo_chung_tu(id, file_name, file_type)
    code = verify(dict_response, file_type)
    file_info = {
        'file_type': file_type,
        'file_name': file_name,
        'code': code
    }

    return (id, file_info)    

def verify(dict_response, file_type):
    for spec in SB_KV_TYPE_INIT:
        if spec["short_name"] == file_type:
            break
    all_keys = [kv["short_name"] for kv in spec["key_values"]]
    code = {}
    if 'detail' in dict_response.keys():
        if dict_response["detail"] == 'Not found.':
            code = 'Not found.'
            return code
            
    ##### Check signature #####
    sigs = dict_response["signatures"]
    missing_sigs = []
    wrong_titles = []
    location_full = []
    location_only = []
    location_name = []

    for sig in sigs:
        title = sig["class_title"]
        if title is None:
            title = sig["title"]
        
        norm_title = simplify(title)
        if norm_title not in titles[file_type]:
            wrong_titles.append(title)

        if sig["image_only"] is None or sig["image_name"] is None:
            missing_sigs.append(title)
        
        if sig["location_full"] is not None:
            location_full.append(sig["location_full"])

        if sig["location_name"] is not None:
            location_name.append(sig["location_name"])

        if sig["location_only"] is not None:
            location_only.append(sig["location_only"])

    location_full.sort()
    location_name.sort()
    location_only.sort()

    if len(location_full) != len(list(k for k,_ in itertools.groupby(location_full))):
        code.append("Duplicate signature")
    elif len(location_name) != len(list(k for k,_ in itertools.groupby(location_name))):
        code.append("Duplicate signature")
    elif len(location_only) != len(list(k for k,_ in itertools.groupby(location_only))):
        code.append("Duplicate signature")

    ##### Check kv #####
    kvs = dict_response["key_values"]
    missing_keys = []
    wrong_keys = []
    for kv in kvs:
        if kv["file_type_kv"]["short_name"] not in all_keys:
            wrong_keys.append(kv["file_type_kv"]["short_name"])
        else:
            if kv["file_type_kv"]["type"] != 'TABLE' and kv["file_type_kv"]["type"] != 'ROW':
                if kv["value"] is None:
                    missing_keys.append(kv["file_type_kv"]["short_name"])

    ##### Check stamp #####
    wrong_stamps = []
    for stamp in dict_response["stamps"]:
        if stamp["class_type"] not in stamps[file_type]:
            wrong_stamps.append(stamp["class_type"])

    code['missing_sigs'] = missing_sigs
    code['wrong_titles'] = wrong_titles
    code['missing_keys'] = missing_keys
    code['wrong_keys'] = wrong_keys
    code['wrong_stamps'] = wrong_stamps

    return code

def simplify(text):
	# text = unicode(text, "utf-8")
    text = unidecode.unidecode(text)
    return str(text).lower()

if __name__=='__main__':
    file_list = glob.glob('random_kss_samples/merged_dataset/phieu_hach_toan/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/phieu_hach_toan_giai_ngan/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/phieu_mua_ngoai_te/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/bang_ke_tinh_lai/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/phieu_chi_tat_toan_so_tiet_kiem/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/phieu_chi/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/giay_nop_tien/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/giay_gui_tien_tiet_kiem/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/giay_rut_tien/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/giay_nop_tien_vao_ngan_sach_nha_nuoc/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/phieu_dieu_chuyen_tien_mat_noi_bo/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/phieu_chi_cua_nghiep_vu_lenh_dieu_chuyen_hang_dac_biet/*.jpg') \
        + glob.glob('random_kss_samples/merged_dataset/lenh_dieu_chuyen_hang_dac_biet/*.jpg') \

    global titles
    titles = {}
    titles["phieu_hach_toan"] = ['nguoi lap', 'kiem soat', 'giam doc', 'tong giam doc']
    titles["phieu_hach_toan_giai_ngan"] = ['lap phieu', 'kiem soat', 'giam doc']
    titles["phieu_mua_ngoai_te"] = ['khach hang', 'thu quy', 'giao dich vien', 'nguoi phe duyet']
    titles["bang_ke_tinh_lai"] = ['nguoi nhap lieu', 'nguoi kiem soat', 'nguoi phe duyet']
    titles["phieu_chi_tat_toan_so_tiet_kiem"] = ['nguoi nhan tien', 'thu quy', 'nguoi nhap lieu', 'nguoi kiem soat', 'nguoi phe duyet']
    titles["phieu_chi"] = ['nguoi nhan', 'thu quy', 'kiem soat', 'giam doc', 'teller']
    titles["giay_nop_tien"] = ['nguoi nop tien', 'thu quy', 'cashier', 'giao dich vien', 'teller', 'nguoi phe duyet', 'authoriser']
    titles["giay_gui_tien_tiet_kiem"] = ['nguoi gui tien', 'thu quy', 'nguoi nhap lieu', 'nguoi kiem soat', 'nguoi phe duyet']
    titles["giay_rut_tien"] = ['nguoi nop tien', 'thu quy', 'cashier', 'giao dich vien', 'teller', 'nguoi phe duyet', 'authoriser']
    titles["giay_nop_tien_vao_ngan_sach_nha_nuoc"] = ['doi tuong nop tien', 'ngan hang (KBNN)']
    titles["phieu_dieu_chuyen_tien_mat_noi_bo"] = []
    titles["phieu_chi_cua_nghiep_vu_lenh_dieu_chuyen_hang_dac_biet"] = ['nguoi nhan tien', 'nguoi giao tien', 'gddv', 'tngdv']
    titles["lenh_dieu_chuyen_hang_dac_biet"] = []


    global stamps
    stamps = {}
    stamps["phieu_hach_toan"] = []
    stamps["phieu_hach_toan_giai_ngan"] = []
    stamps["phieu_mua_ngoai_te"] = ['DA_CHI_TIEN']
    stamps["bang_ke_tinh_lai"] = []
    stamps["phieu_chi_tat_toan_so_tiet_kiem"] = ['DA_CHI_TIEN']
    stamps["phieu_chi"] = ['DA_CHI_TIEN']
    stamps["giay_nop_tien"] = ['DA_THU_TIEN']
    stamps["giay_gui_tien_tiet_kiem"] = ['DA_THU_TIEN', 'TIEN_MAT']
    stamps["giay_rut_tien"] = ['DA_CHI_TIEN']
    stamps["giay_nop_tien_vao_ngan_sach_nha_nuoc"] = ['DAU_TRON_DO', 'DA_NHAN_CHUNG_TU', 'DAU_TRON_XANH']
    stamps["phieu_dieu_chuyen_tien_mat_noi_bo"] = ['DA_CHI_TIEN']
    stamps["phieu_chi_cua_nghiep_vu_lenh_dieu_chuyen_hang_dac_biet"] = ['DA_CHI_TIEN']
    stamps["lenh_dieu_chuyen_hang_dac_biet"] = ['DA_CHI_TIEN', 'DAU_TRON_DO']

    global TOTAL
    TOTAL = len(file_list)
    
    if sys.argv[1] == '--get-id':
        ##### Push file to db and get id #####
        result = []
        for file in tqdm.tqdm(file_list):
            result.append(process_get_id(file))

        file_dict = {}
        for item in result:
            file_dict[str(item[0])] = item[1]

        with open(f"id_list.json", 'w', encoding='utf-8') as f:
            json.dump(file_dict, f, ensure_ascii=False, indent=4)
    elif sys.argv[1] == '--get-bo-chung-tu':
        ##### Process bo chung tu #####
        with open(f"id_list.json","r") as f:
            id_list = json.load(f)

        bag = []
        for key in id_list.keys():
            id = key
            file_name = id_list[id]["file_name"]
            file_type = id_list[id]["file_type"]
            # os.makedirs(f"{SAVE_PATH}/{file_type}", exist_ok=True)

            bag.append((id, file_name, file_type))

        file_dict = {}
        for item in tqdm.tqdm(bag):
            result = process_get_bo_chung_tu(item)
            file_dict[str(result[0])] = result[1]

        with open(f"test_list.json", 'w', encoding='utf-8') as f:
            json.dump(file_dict, f, ensure_ascii=False, indent=4)