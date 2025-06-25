import os

class Database:
    def __init__(self, name):
        self.name = name
        self.tables = {}
        if not os.path.exists(f'{name}.db'):
            with open(f'{name}.db', 'w') as db_file:
                db_file.write('')  # 빈 파일 생성

    def create_table(self, table_name, attributes):
        if table_name in self.tables:
            print(f"테이블 {table_name}이(가) 이미 존재합니다.")
            return
        self.tables[table_name] = Table(table_name, attributes)
        self._update_db_file()

    def delete_table(self, table_name):
        if table_name not in self.tables:
            print(f"테이블 {table_name}이(가) 존재하지 않습니다.")
            return
        self.tables[table_name].delete()
        del self.tables[table_name]
        self._update_db_file()

    def _update_db_file(self):
        with open(f'{self.name}.db', 'w') as db_file:
            for table in self.tables:
                db_file.write(f'{table}\n')

class Table:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.records = []  # 테이블 내용 레코드의 리스트로 구성
        if not os.path.exists(f'{self.name}.tbl'):
            with open(f'{self.name}.tbl', 'w') as table_file:
                table_file.write(','.join(attributes) + '\n')

    def add_record(self, record):
        self.records.append(record)
        self._save_to_file()

    def delete_record(self, attribute, value):
        self.records = [r for r in self.records if r[attribute] != value]
        self._save_to_file()

    def clear_records(self):
        self.records = []
        self._save_to_file()

    def get_records(self):
        return self.records

    def find_record(self, attribute, value):
        return [r for r in self.records if r[attribute] == value]

    def _save_to_file(self):
        with open(f'{self.name}.tbl', 'w') as table_file:
            table_file.write(','.join(self.attributes) + '\n')
            for record in self.records:
                table_file.write(','.join(record[attr] for attr in self.attributes) + '\n')

    def delete(self):
        if os.path.exists(f'{self.name}.tbl'):
            os.remove(f'{self.name}.tbl')

def main():
    db = Database('고객정보DB')
    db.create_table('고객정보', ['고객아이디', '고객이름', '직업', '주소', '전화번호', '포인트'])

    while True:
        print("\n1. 고객정보 입력\n2. 고객정보 수정\n3. 고객정보 삭제\n4. 고객아이디로 조회\n5. 고객이름으로 조회\n6. 특정 지역명으로 조회\n7. 종료")
        choice = input("선택: ")

        if choice == '1':
            add_customer_info(db)
        elif choice == '2':
            update_customer_info(db)
        elif choice == '3':
            delete_customer_info(db)
        elif choice == '4':
            search_by_id(db)
        elif choice == '5':
            search_by_name(db)
        elif choice == '6':
            search_by_location(db)
        elif choice == '7':
            break
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

def add_customer_info(db):
    record = {}  # 레코드 속성을 키, 내용을 값으로 하는 딕셔너리 구성
    record['고객아이디'] = input("고객아이디: ")
    record['고객이름'] = input("고객이름: ")
    record['직업'] = input("직업: ")
    record['주소'] = input("주소: ")
    record['전화번호'] = input("전화번호: ")
    record['포인트'] = input("포인트: ")

    db.tables['고객정보'].add_record(record)
    print("고객 정보가 추가되었습니다.")

def update_customer_info(db):
    customer_id = input("Id: ")
    records = db.tables['고객정보'].find_record('고객아이디', customer_id)
    if records:
        record = records[0]
        print("정보입력화면")
        record['고객이름'] = input(f"고객이름 ({record['고객이름']}): ") or record['고객이름']
        record['직업'] = input(f"직업 ({record['직업']}): ") or record['직업']
        record['주소'] = input(f"주소 ({record['주소']}): ") or record['주소']
        record['전화번호'] = input(f"전화번호 ({record['전화번호']}): ") or record['전화번호']
        record['포인트'] = input(f"포인트 ({record['포인트']}): ") or record['포인트']
        db.tables['고객정보']._save_to_file()
        print("고객 정보가 수정되었습니다.")
    else:
        print("없는 고객에 대한 정보입니다.")

def delete_customer_info(db):
    customer_id = input("Id: ")
    records = db.tables['고객정보'].find_record('고객아이디', customer_id)
    if records:
        db.tables['고객정보'].delete_record('고객아이디', customer_id)
        print("고객님의 정보를 삭제하겠습니다.")
    else:
        print("없는 고객에 대한 정보입니다.")

def search_by_id(db):
    customer_id = input("Id: ")
    records = db.tables['고객정보'].find_record('고객아이디', customer_id)
    if records:
        print(records[0])
    else:
        print("없는 고객에 대한 정보입니다.")

def search_by_name(db):
    customer_name = input("고객 이름: ")
    records = db.tables['고객정보'].find_record('고객이름', customer_name)
    if records:
        for record in records:
            print(record)
    else:
        print("없는 고객에 대한 정보입니다.")

def search_by_location(db):
    location = input("지역명: ")
    records = db.tables['고객정보'].find_record('주소', location)
    if records:
        for record in records:
            print(record)
    else:
        print("없는 고객에 대한 정보입니다.")

if __name__ == "__main__":
    main()
