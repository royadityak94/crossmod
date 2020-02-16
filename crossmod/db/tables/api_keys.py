from sqlalchemy import Column, Integer, String
import crossmod
from crossmod.db.base import Base

'''
    Schema:
        api_key_db:
            * API Key ID:               (column_name: id)
            * API Key:                  (column_name: api_key)
            * API Key Access Level:     (column_name: access_level)      (Access Level 0-5 which determines rate limit, tied to api_key)
'''

class ApiKeyTable(Base):
      __tablename__ = 'api_key_db'
      id = Column(Integer, primary_key = True)
      api_key = Column(String(40))
      access_level = Column(Integer)