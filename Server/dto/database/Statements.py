class StatementList(object):
    def __init__(self, statement_list=None):
        if statement_list is None:
            self.statement_list = []
        else:
            self.statement_list = statement_list

    def get_statement_list(self):
        return self.statement_list

    def set_statement_list(self, statement_list):
        self.statement_list = statement_list

    def add_statement(self, statement_id, statement):
        self.statement_list.append(
            Statement(
                statement_id=statement_id,
                statement=statement
            )
        )


class Statement(object):
    def __init__(self, statement_id=None, statement=None):
        self.statement_id = statement_id
        self.statement = statement

    def get_statement(self):
        return self.statement

    def set_statement(self, statement):
        self.statement = statement

    def get_statement_id(self):
        return self.statement_id

    def set_statement_id(self, statement_id):
        self.statement_id = statement_id
