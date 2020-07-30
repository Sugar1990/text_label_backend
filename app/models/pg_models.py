# -*- coding: utf-8 -*-
from .. import db


# 配置项
class TreeSet(db.Model):
    __tablename__ = 'tree_set'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String)
    type = db.Column(db.String)
    name = db.Column(db.String)
    parent_id = db.Column(db.Integer)

    def __repr__(self):
        return '<TreeSet %r>' % self.name

    @staticmethod
    def get_task_types():
        return TreeSet.query.filter_by(domain='task_type').all()


# 任务表
class Task(db.Model):
    __tablename__ = 'task'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String)
    task_type_id = db.Column(db.Integer)
    task_status_id = db.Column(db.Integer)
    review_user_id = db.Column(db.Integer)
    label_user_id = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<TreeSet %r>' % self.name

    def get_task_type_name(self):
        ts = TreeSet.query.filter_by(id=self.task_type_id).first()
        return ts.name if ts else ''

    def get_task_status_name(self):
        ts = TreeSet.query.filter_by(id=self.task_status_id).first()
        return ts.name if ts else ''

    def get_review_user_name(self):
        return str(self.review_user_id)

    def get_label_user_name(self):
        return str(self.label_user_id)
