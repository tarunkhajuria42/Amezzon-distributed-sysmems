package com.cdedonder.amezzon.database.data;

import java.lang.reflect.Field;
import java.util.logging.Logger;

final class ReflectEquals {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    static boolean equals(Object obj1, Object obj2) {
        if (!obj1.getClass().equals(obj2.getClass())) return false;
        Class<?> classObject = obj1.getClass();
        Field[] fields = classObject.getDeclaredFields();
        try {
            for (Field f : fields) {
                f.setAccessible(true);
                if (!f.get(obj1).equals(f.get(obj2))) return false;
            }
        } catch (IllegalAccessException e) {
            LOGGER.severe("Cannot use reflection to check 'equals':\n" + e.getMessage());
        }
        return true;
    }
}
