package com.cdedonder.amezzon.database.data;

import java.lang.reflect.Field;
import java.util.logging.Logger;

final class ReflectToString {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    static String toString(Object obj) {
        try {
            Class<?> classObject = obj.getClass();
            Field[] fields = classObject.getDeclaredFields();
            StringBuilder sb = new StringBuilder(classObject.getCanonicalName());
            for (Field f : fields) {
                sb.append(f.getName()).append(": ").append(f.get(obj)).append("\n");
            }
            return sb.toString();
        } catch (IllegalAccessException e) {
            LOGGER.severe("Cannot use reflection for 'toString': " + e.getMessage());
        }
        return "";
    }
}
