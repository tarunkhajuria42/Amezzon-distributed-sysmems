package com.cdedonder.amezzon.parser.classhandler;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.Person;
import com.cdedonder.amezzon.database.data.PersonDAO;
import com.cdedonder.amezzon.parser.InternalResponse;
import com.cdedonder.amezzon.parser.request.DeleteRequest;
import com.cdedonder.amezzon.parser.request.GetRequest;
import com.cdedonder.amezzon.parser.request.PutRequest;

import java.io.IOException;

public class PersonClassHandler extends AbstractClassHandler {

    public PersonClassHandler(DataAccesContext dac) {
        super(dac);
    }

    @Override
    public InternalResponse put(PutRequest putRequest) {
        InternalResponse response = new InternalResponse();
        try {
            Person person = objectMapper.readValue(putRequest.getJsonstring(), Person.class);
            PersonDAO personDAO = getDataAccessContext().getPersonDAO();

            getDataAccessContext().startTransaction();

            if (personDAO.exist(person)) {
                personDAO.update(person);
            } else {
                personDAO.create(person);
            }

            getDataAccessContext().commitTransaction();

            response.setResponseCode(200);
        } catch (IOException e) {
            response.setResponseCode(400);
            response.setResponseBody("Malformed request, could not process.");
        } catch (DataAccessException f) {
            response.setResponseCode(409);
            response.setResponseBody("Internal conflict");
        }
        return response;
    }

    @Override
    public InternalResponse get(GetRequest getRequest) {
        return null;
    }

    @Override
    public InternalResponse delete(DeleteRequest deleteRequest) {
        InternalResponse response = new InternalResponse();
        try {
            Person person = objectMapper.readValue(deleteRequest.getJsonstring(), Person.class);
            PersonDAO personDAO = getDataAccessContext().getPersonDAO();

            getDataAccessContext().startTransaction();

            personDAO.delete(person);

            getDataAccessContext().commitTransaction();

            response.setResponseCode(200);
        } catch (IOException e) {
            response.setResponseCode(400);
            response.setResponseBody("Malformed request, could not process.");
        } catch (DataAccessException f) {
            response.setResponseCode(409);
            response.setResponseBody("Internal conflict");
        }
        return response;
    }
}
