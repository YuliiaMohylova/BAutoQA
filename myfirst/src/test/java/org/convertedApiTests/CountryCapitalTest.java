package org.convertedApiTests;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

import javax.xml.parsers.DocumentBuilderFactory;
import java.io.StringReader;

public class CountryCapitalTest {

    private static final String BASE_URI = "http://webservices.oorsprong.org";
    private static final String COUNTRY_INFO_NS = "http://www.oorsprong.org/websamples.countryinfo";

    @Test
    public void shouldReturnCapitalForUkraine() {
        String requestBody = """
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
                               xmlns:m="http://www.oorsprong.org/websamples.countryinfo">
                    <soap:Body>
                        <m:CapitalCity>
                            <m:sCountryISOCode>UA</m:sCountryISOCode>
                        </m:CapitalCity>
                    </soap:Body>
                </soap:Envelope>
                """;

        Response response = RestAssured
                .given()
                .log().all()
                .baseUri(BASE_URI)
                .header("Content-type", "text/xml")
                .header("Accept-Charset", "utf-8")
                .header("SOAPAction", "\"\"")
                .body(requestBody)
                .when()
                .post("/websamples.countryinfo/CountryInfoService.wso")
                .then()
                .log().all()
                .statusCode(200)
                .extract()
                .response();

        String responseBody = response.asString();
        String capital = extractCapitalCity(responseBody);

        Assert.assertFalse(responseBody.isBlank(), "Response body should not be empty.");
        Assert.assertTrue(responseBody.contains("CapitalCityResponse"),
                "SOAP response should contain CapitalCityResponse.");
        Assert.assertEquals(capital, "Kiev", "Capital city for UA should match the SOAP response.");
    }

    private String extractCapitalCity(String responseBody) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            factory.setNamespaceAware(true);

            Document document = factory.newDocumentBuilder()
                    .parse(new InputSource(new StringReader(responseBody)));

            NodeList capitalNodes = document.getElementsByTagNameNS(COUNTRY_INFO_NS, "CapitalCityResult");
            Assert.assertEquals(capitalNodes.getLength(), 1,
                    "SOAP response should contain exactly one CapitalCityResult element.");

            return capitalNodes.item(0).getTextContent().trim();
        } catch (Exception e) {
            throw new IllegalStateException("Failed to parse SOAP response.", e);
        }
    }
}
