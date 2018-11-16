from dto.ErrorMessage import ErrorMessageList
from dto.GenericDto import GenericDto
from dto.database.Statements import StatementList
from resource.StaticResource import ACTION_DB_STATEMENT


class DataBaseStatementDto(object):
    class GetRequest(GenericDto.CustomRequest):
        def __init__(self):
            GenericDto.CustomRequest.__init__(
                self, action=ACTION_DB_STATEMENT, data=self.Data(

                )
            )

        class Data(StatementList):
            def __init__(self, statement_list=None):
                StatementList.__init__(self, statement_list=statement_list)

    class GetResponse(GenericDto.CustomResponse):
        def __init__(self, error_messages=None, result_list=None):
            GenericDto.CustomResponse.__init__(
                self, data=self.Data(
                    error_messages=error_messages,
                    result_list=result_list
                )
            )

        class Data(ErrorMessageList):
            def __init__(self, error_messages=None, result_list = None):
                ErrorMessageList.__init__(self, error_messages=error_messages)
                if result_list is None:
                    result_list = []
                self.result_list = result_list
