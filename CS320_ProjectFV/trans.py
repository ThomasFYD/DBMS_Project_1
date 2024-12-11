import sqlite3
import random
import time

# 源数据库（schoolFacts.sqlite3）连接
source_conn = sqlite3.connect('schoolFacts.sqlite3')
# print(source_conn.execute(" SHOW TABLES"))
source_cursor = source_conn.cursor()
print(source_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
# 目标数据库（db.sqlite3）连接
target_conn = sqlite3.connect('db.sqlite3')
target_cursor = target_conn.cursor()
target_cursor.execute("DELETE FROM school_data_schooldata;")
target_conn.commit()

# 查询源数据库Schooldata表中的数据
source_cursor.execute("SELECT DistrictName,AUN, SchoolName, Schl,SchoolAddressStreet, SchoolAddressCity,SchoolZipCode,SchoolEnrollment,PercentGifted   FROM 'SchoolData'")
rows = source_cursor.fetchall()

# 构造插入目标数据库SchoolData表的SQL语句，参数数量与SchoolData表字段数量一致
insert_sql = ("INSERT INTO school_data_schooldata (district_name, aun, name, schl, school_address_street, school_address_city, school_zip_code, school_enrollment, percent_gifted_student, low_income_percentage, teacher_loan_cancellations, percent_students_low_income, test_scores, dropout_rate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)")

# 遍历每一行数据并插入到目标数据库中
for row in rows:
    # 从源表获取对应字段数据，没有对应上的按情况处理
    district_name = row[0] if row[0] else ""
    aun = row[1] if row[1] else 0
    name = row[2] if row[2] else ""
    schl = row[3] if row[3] else 0
    school_address_street = row[4] if row[4] else ""
    school_address_city = row[5] if row[5] else ""
    school_zip_code = row[6] if row[6] else ""
    school_enrollment = row[7] if row[7] else 0
    percent_gifted_student = row[8] if row[8] else 0

    # 对于目标表中新增的允许为null的字段，进行随机生成数据或设置默认值（这里只是简单示例，可按需调整）
    low_income_percentage = round(random.uniform(0, 100), 2)
    teacher_loan_cancellations = round(random.uniform(0, 10), 2)
    percent_students_low_income = round(random.uniform(0, 100), 2)
    test_scores = round(random.uniform(0, 100), 2)
    dropout_rate = round(random.uniform(0, 10), 2)
    try:
        target_cursor.execute(insert_sql, (district_name, aun, name, schl, school_address_street, school_address_city, school_zip_code, school_enrollment, percent_gifted_student, low_income_percentage, teacher_loan_cancellations, percent_students_low_income, test_scores, dropout_rate))
    except Exception as e:
        print(f"插入数据出现错误: {e}")
        continue
# 提交事务，使插入操作生效
target_conn.commit()
# except sqlite3.Error as e:
#     print(f"数据库操作出现错误: {e}")
# finally:
#     # 关闭游标和连接
#     source_cursor.close()
#     source_conn.close()
#     target_cursor.close()
#     target_conn.close()