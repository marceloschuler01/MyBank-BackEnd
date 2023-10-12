from Infra.config.connection import DBConnectionHandler

def with_db_connection(f):
    def with_connection_(*args, **kwargs):
        try:
            conn = kwargs['conn']
        except KeyError:
            conn = None
        if not conn:
            with DBConnectionHandler() as db:
                print("Opening Connection")
                try:
                    kwargs['conn'] = db
                    result = f(*args, **kwargs)
                except:
                    db.session.rollback()
                    print("SQL failed")
                    raise
                else:
                    print("Commiting!")
                    db.session.commit()
                return result
        result = f(*args, **kwargs)
        return result
    return with_connection_
