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

            if (putRequest.isUpdate()) {
                if (personDAO.exist(person)) {
                    personDAO.update(person);
                } else {
                    response.setResponseCode(201);
                }
            } else {
                if (personDAO.exist(person)) {
                    response.setResponseCode(211);
                } else {
                    personDAO.create(person);
                }
            }
            getDataAccessContext().commitTransaction();
            response.setResponseCode(100);
        } catch (IOException e) {
            response.setResponseCode(321);
        } catch (DataAccessException f) {
            response.setResponseCode(500);
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

            if (personDAO.exist(person)) {
                personDAO.delete(person);
            } else {
                response.setResponseCode(201);
            }

            getDataAccessContext().commitTransaction();

            response.setResponseCode(100);
        } catch (IOException e) {
            response.setResponseCode(321);
        } catch (DataAccessException f) {
            response.setResponseCode(500);
        }
        return response;
    }
}
