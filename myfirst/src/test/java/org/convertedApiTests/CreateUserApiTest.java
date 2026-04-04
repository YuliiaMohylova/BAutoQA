package org.convertedApiTests;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.LinkedHashSet;
import java.util.Properties;
import java.util.Set;
import java.util.UUID;

public class CreateUserApiTest {

    private static final String BASE_URI = "https://gorest.co.in";

    @Test
    public void shouldCreateUser() {
        String token = resolveToken();
        String email = "tenali.ramakrishna+" + UUID.randomUUID() + "@191ce.com";
        String expectedName = "Tenali Ramakrishna";
        String expectedGender = "male";
        String expectedStatus = "active";
        String requestBody = """
                {
                  "name": "%s",
                  "gender": "%s",
                  "email": "%s",
                  "status": "%s"
                }
                """.formatted(expectedName, expectedGender, email, expectedStatus);

        Response response = RestAssured
                .given()
                .log().all()
                .baseUri(BASE_URI)
                .contentType(ContentType.JSON)
                .accept(ContentType.JSON)
                .header("Authorization", "Bearer " + token)
                .body(requestBody)
                .when()
                .post("/public/v2/users")
                .then()
                .log().all()
                .statusCode(201)
                .extract()
                .response();

        Integer id = response.jsonPath().getInt("id");
        String actualName = response.jsonPath().getString("name");
        String actualGender = response.jsonPath().getString("gender");
        String actualEmail = response.jsonPath().getString("email");
        String actualStatus = response.jsonPath().getString("status");

        Assert.assertTrue(response.contentType().contains(ContentType.JSON.toString()),
                "Response content type should be JSON.");
        Assert.assertNotNull(id, "Created user id should be present.");
        Assert.assertTrue(id > 0, "Created user id should be positive.");
        Assert.assertEquals(actualName, expectedName, "User name mismatch.");
        Assert.assertEquals(actualGender, expectedGender, "User gender mismatch.");
        Assert.assertEquals(actualEmail, email, "User email mismatch.");
        Assert.assertEquals(actualStatus, expectedStatus, "User status mismatch.");
        Assert.assertEquals(response.getHeader("Content-Type"), "application/json; charset=utf-8",
                "Unexpected Content-Type header.");
        Assert.assertFalse(response.asString().isBlank(), "Response body should not be empty.");
    }

    private String resolveToken() {
        String token = System.getProperty("gorest.token");
        if (token == null || token.isBlank()) {
            token = System.getenv("GOREST_TOKEN");
        }
        if (token == null || token.isBlank()) {
            token = readTokenFromLocalProperties();
        }

        if (token == null || token.isBlank()) {
            throw new IllegalStateException(
                    "GoRest token is missing. Set -Dgorest.token=<token>, GOREST_TOKEN, "
                            + "or add gorest.token=<token> to local.properties in the project root."
            );
        }

        return token;
    }

    private String readTokenFromLocalProperties() {
        Path propertiesPath = findLocalPropertiesPath();
        if (propertiesPath == null) {
            return null;
        }

        Properties properties = new Properties();
        try (InputStream inputStream = Files.newInputStream(propertiesPath)) {
            properties.load(inputStream);
            return properties.getProperty("gorest.token");
        } catch (IOException e) {
            throw new IllegalStateException("Failed to read local.properties.", e);
        }
    }

    private Path findLocalPropertiesPath() {
        Set<Path> searchRoots = new LinkedHashSet<>();
        searchRoots.add(Paths.get("").toAbsolutePath());
        searchRoots.add(Path.of(System.getProperty("user.dir")).toAbsolutePath());
        searchRoots.add(Path.of("src", "test", "java").toAbsolutePath());

        for (Path root : searchRoots) {
            Path current = root;
            while (current != null) {
                Path candidate = current.resolve("local.properties");
                if (Files.exists(candidate)) {
                    return candidate;
                }
                current = current.getParent();
            }
        }

        return null;
    }
}
