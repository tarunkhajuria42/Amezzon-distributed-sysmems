package com.cdedonder.amezzon.parser.classhandler;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.parser.InternalResponse;
import com.cdedonder.amezzon.parser.request.DeleteRequest;
import com.cdedonder.amezzon.parser.request.GetRequest;
import com.cdedonder.amezzon.parser.request.PutRequest;

public class ProductTypeClassHandler extends AbstractClassHandler {

    public ProductTypeClassHandler(DataAccesContext dac) {
        super(dac);
    }

    @Override
    public InternalResponse put(PutRequest putRequest) {
        return null;
    }

    @Override
    public InternalResponse get(GetRequest getRequest) {
        return null;
    }

    @Override
    public InternalResponse delete(DeleteRequest deleteRequest) {
        return null;
    }
}
