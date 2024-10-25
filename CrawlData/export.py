import pandas as pd
from sqlalchemy import create_engine

# Tạo đối tượng SQLAlchemy engine
engine = create_engine('mysql+pymysql://root:1234@localhost/pbl3')

# sql = 'SELECT JOB_NAME,SALARY,POSTED_DATE_AT, DESCRIPTION, SOURCE_PICTURE FROM info_recruitment_detail'

# maketing
sql = 'SELECT DISTINCT ird.JOB_NAME,ird.SALARY,ird.POSTED_DATE_AT,ird.DESCRIPTION,ird.SOURCE_PICTURE FROM info_recruitment_detail ird JOIN company cn ON ird.COMPANY_ID = cn.ID JOIN career cr ON cr.ID = cn.CAREER_ID WHERE cr.NAME LIKE "Business"'



# Thực hiện truy vấn và lưu kết quả vào DataFrame
df = pd.read_sql(sql, engine)

# Lưu DataFrame vào file CSV
df.to_csv('C:\\Users\\ASUS\\OneDrive\\Máy tính\\pbl3_source_code\\ProjectTuyenDung\\QLVLCrawlData\\it.csv', index=False, sep=';')
