from db import db


class Router(db.Model):
    __tablename__ = 'routers'
    loopback = db.Column(db.String(30), primary_key=True)
    hostname = db.Column(db.String(30))
    routertype = db.Column(db.String(5))

    def __init__(self, loopback, hostname, routertype):
        self.loopback = loopback
        self.hostname = hostname
        self.routertype = routertype

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_record(self):
        db.session.commit()

    def json(self):
        return {"loopback": self.loopback, "hostname": self.hostname, "routertype": self.routertype}

    def delete_router(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_loopbackip(cls, loopback):
        return cls.query.filter_by(loopback=loopback).first()

    @classmethod
    def find_by_type(cls, routertype):
        # returns list of all routers with given type
        return cls.query.filter_by(routertype=routertype).all()

    @classmethod
    def getjson(cls, router_list):
        return {'router_list': [data.json() for data in router_list]}

    @classmethod
    def find_by_ip_range(cls, from_ip, to_ip):
        return cls.query.filter(Router.loopback >= from_ip, Router.loopback <= to_ip).all()
