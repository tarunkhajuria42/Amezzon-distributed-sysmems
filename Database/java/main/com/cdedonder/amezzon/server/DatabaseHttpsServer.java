package com.cdedonder.amezzon.server;

import com.sun.net.httpserver.HttpsConfigurator;
import com.sun.net.httpserver.HttpsParameters;
import com.sun.net.httpserver.HttpsServer;

import javax.net.ssl.*;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.security.*;
import java.security.cert.CertificateException;
import java.util.Properties;
import java.util.concurrent.Executors;
import java.util.logging.Logger;

public class DatabaseHttpsServer {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private final HttpsServer server;

    public DatabaseHttpsServer(Properties properties) throws IOException {
        server = HttpsServer.create(new InetSocketAddress(properties.getProperty("host"), Integer.parseInt(properties.getProperty("port"))), 0);
        server.createContext("/", new HttpExchangeHandler());
        server.setExecutor(Executors.newFixedThreadPool(Integer.parseInt(properties.getProperty("threads"))));
        try {
            SSLContext sslContext = SSLContext.getInstance("TLS");

            char[] password = properties.getProperty("password").toCharArray();
            KeyStore ks = KeyStore.getInstance(properties.getProperty("keystoreinstance"));
            FileInputStream fis = new FileInputStream(properties.getProperty("keystore"));
            ks.load(fis, password);

            KeyManagerFactory kmf = KeyManagerFactory.getInstance(properties.getProperty("kmf"));
            kmf.init(ks, password);

            TrustManagerFactory tmf = TrustManagerFactory.getInstance(properties.getProperty("tmf"));
            tmf.init(ks);

            sslContext.init(kmf.getKeyManagers(), tmf.getTrustManagers(), null);
            server.setHttpsConfigurator(new HttpsConfigurator(sslContext) {
                @Override
                public void configure(HttpsParameters httpsParameters) {
                    try {
                        SSLContext c = SSLContext.getDefault();
                        SSLEngine engine = c.createSSLEngine();
                        httpsParameters.setNeedClientAuth(false);
                        httpsParameters.setCipherSuites(engine.getEnabledCipherSuites());
                        httpsParameters.setProtocols(engine.getEnabledProtocols());

                        SSLParameters defaultSSLParameters = c.getDefaultSSLParameters();
                        httpsParameters.setSSLParameters(defaultSSLParameters);
                    } catch (NoSuchAlgorithmException e) {
                        LOGGER.severe("Cannot configure HTTPS:\n" + e.getMessage());
                    }
                }
            });
        } catch (NoSuchAlgorithmException | KeyStoreException | CertificateException | UnrecoverableKeyException | KeyManagementException e) {
            LOGGER.severe("Cannot setup database server:\n" + e.getMessage());
        }
    }

    public void start() {
        server.start();
    }
}
