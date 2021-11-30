import pymysql

conn = None
cur = None

# 데이터 베이스 접속
conn = pymysql.connect(
    host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
)

# 커서
cur = conn.cursor()

# userTBL의 회원 데이터 Insert
sql = ""
# userID, name, birthYear, addr
userID = ""
name = ""
birthYear = ""
addr = ""

while True:
    userID = input("사용자 ID ==> ")
    if userID == "":
        break
    name = input("사용자 이름 ==> ")
    birthYear = input("사용자 출생년도 ==> ")
    addr = input("사용자 주소 ==> ")

    sql = (
        "INSERT INTO userTBL (userID, name, birthYear, addr, mDate) VALUE "
        "('"
        + userID
        + "', '"
        + name
        + "', "
        + birthYear
        + ", '"
        + addr
        + "', CURDATE())"
    )
    cur.execute(sql)

conn.commit()
conn.close()
