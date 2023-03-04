from src.config.database import db
from flask_sqlalchemy import SQLAlchemy
from injector import inject
import operator

from src.shared.models.filter_model import ListFilterModel

class BaseRepository():

    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db
        self._model = None
        self._auto_commit = False
        # self._session_factory = orm.scoped_session(
        #     orm.sessionmaker(
        #         autocommit=False,
        #         autoflush=False,
        #         bind=self._db.get_engine(),
        #     ),
        # )
        self.session = self.db.session

    @property
    def model(self) -> db.Model:
        return self._model
    
    @model.setter
    def model(self, model: db.Model):
        self._model = model

    @property
    def auto_commit(self) -> bool:
        return self._auto_commit
    
    @auto_commit.setter
    def auto_commit(self, auto_commit):
        self._auto_commit = auto_commit

    def format_filters(self, filters_model: ListFilterModel, entity) -> list:
        
        filter_list = []
        op_dict = {
            '>': operator.gt,
            '<': operator.lt,
            '==':operator.eq
        }
        list_filter_model = filters_model.filters
        for filter in list_filter_model:
            
            filter_list.append(op_dict.get(filter.operation)(getattr(entity, filter.entity_attr), filter.value))
        
        return filter_list

    def save(self):

        # with self.session as session, session.begin():
        self.session.add(self.model)
        self.session.flush()
        self.session.expunge_all()
        self.session.commit()
        
    def commit(self):...