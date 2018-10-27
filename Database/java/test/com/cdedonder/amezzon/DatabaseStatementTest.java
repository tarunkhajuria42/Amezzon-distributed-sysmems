package com.cdedonder.amezzon;

import com.cdedonder.amezzon.parser.dto.DatabaseStatementRequest;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.Test;

import java.util.ArrayList;

public class DatabaseStatementTest {

    @Test
    public void testDeparseRequest() throws Exception{
        DatabaseStatementRequest request = new DatabaseStatementRequest();
        request.setTransaction_token("444");

        DatabaseStatementRequest.StatementWrapper w1 = new DatabaseStatementRequest.StatementWrapper();
        w1.setStatement("SELECT");
        w1.setStatement_id(1);

        request.setStatement_list(new ArrayList<DatabaseStatementRequest.StatementWrapper>(){{
            add(w1);
            add(w1);
        }});

        ObjectMapper objectMapper = new ObjectMapper();
        System.out.println(objectMapper.writeValueAsString(request));
    }
}
