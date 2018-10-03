package com.cdedonder.amezzon.parser.request;

public class DeleteRequest {

    private String objectclass;
    private String jsonstring;
    private boolean cascade;

    public String getObjectclass() {
        return objectclass;
    }

    public void setObjectclass(String objectclass) {
        this.objectclass = objectclass;
    }
}
