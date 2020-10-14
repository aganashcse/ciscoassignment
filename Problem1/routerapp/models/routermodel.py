from db import db


class Router(db.Model):
    __tablename__ = 'routers'
    sapid = db.Column(db.Integer, primary_key=True,
                      unique=True, nullable=False)
    loopback = db.Column(db.String(30))
    hostname = db.Column(db.String(30))
    routertype = db.Column(db.String(5))
    macaddress = db.Column(db.String(17))

    def __init__(self, sapid, loopback, hostname, routertype, macaddress):
        self.sapid = sapid
        self.loopback = loopback
        self.hostname = hostname
        self.routertype = routertype
        self.macaddress = macaddress

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_record(self):
        db.session.commit()

    def json(self):
        return {"sapid": self.sapid, "loopback": self.loopback, "hostname": self.hostname, "routertype": self.routertype, "macaddress": self.macaddress}

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

    @classmethod
    def find_by_sapid(cls, sapid):
        return cls.query.filter_by(sapid=sapid).first()

    @classmethod
    def get_all_routers(cls):
        return cls.query.order_by(Router.sapid).all()
