package com.cdedonder.amezzon.parser.classhandler;

import com.cdedonder.amezzon.parser.InternalResponse;
import com.cdedonder.amezzon.parser.request.DeleteRequest;
import com.cdedonder.amezzon.parser.request.GetRequest;
import com.cdedonder.amezzon.parser.request.PutRequest;

public interface ClassHandler {

    InternalResponse put(PutRequest putRequest);

    InternalResponse get(GetRequest getRequest);

    InternalResponse delete(DeleteRequest deleteRequest);
}
