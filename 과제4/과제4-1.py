import json

# (1) 데이터 들어가 있는 딕셔너리 생성
ssu_date = {
    "school": "숭실대학교",
    "president": "장범식",
    "opened_year": 1897,
    "student": {
        "name": "김소현",
        "location": "Jinhae",
        "age": 20,
        "birth_date": "2005.02.04"
    }
}

# (2) 딕셔너리를 JSON 형식으로 변환
json_string = json.dumps(ssu_date, ensure_ascii=False, indent=4)
print(json_string)

# (3) JSON 변환 결과를 원래 객체로 복원
restored_ssu_date = json.loads(json_string)

