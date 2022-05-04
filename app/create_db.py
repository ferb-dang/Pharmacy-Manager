from db.engine import engine
import dbmodels



print("Đã tạo thành công database")
dbmodels.Base.metadata.create_all(engine)
