from sqlalchemy import Column, Integer, String


from base import Base

class Chainsaw(Base):


   # creating a table
    __tablename__ = 'record_holder'

    # creating the columns
    id = Column(Integer, primary_key=True)
    record_name = Column(String)
    country = Column(String)
    number_of_catches = Column(Integer)

    def __repr__(self):
        return 'record_holder: id = {} Chainsaw_Juggling_Record_Holder = {} Country = {}  Number_of_catches = {}'.format(self.id, self.record_name, self.country, self.number_of_catches)
