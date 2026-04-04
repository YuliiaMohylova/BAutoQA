package org.convertedApiTests;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

public class GetUsersApiTest {

    private static final String BASE_URI = "https://gorest.co.in";

    @Test
    public void shouldGetUsers() {
        Response response = RestAssured
                .given()
                .log().all()
                .baseUri(BASE_URI)
                .accept(ContentType.JSON)
                .when()
                .get("/public/v2/users")
                .then()
                .log().all()
                .statusCode(200)
                .extract()
                .response();

        Assert.assertTrue(response.contentType().contains(ContentType.JSON.toString()),
                "Response content type should be JSON.");
        Assert.assertEquals(response.getHeader("Content-Type"), "application/json; charset=utf-8",
                "Unexpected Content-Type header.");
        Assert.assertFalse(response.asString().isBlank(), "Response body should not be empty.");
        Assert.assertFalse(response.jsonPath().getList("$").isEmpty(), "Users list should not be empty.");
        Assert.assertNotNull(response.jsonPath().get("[0].id"), "First user id should be present.");
        Assert.assertNotNull(response.jsonPath().get("[0].name"), "First user name should be present.");
        Assert.assertNotNull(response.jsonPath().get("[0].email"), "First user email should be present.");
        Assert.assertNotNull(response.jsonPath().get("[0].gender"), "First user gender should be present.");
        Assert.assertNotNull(response.jsonPath().get("[0].status"), "First user status should be present.");
    }
}
