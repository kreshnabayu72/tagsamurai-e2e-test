it("Mock and assert POST API requests using browser.intercept", async () => {
  // Navigate to API POST section
  await MatchersPage.open("api-post");

  // Setup POST API interception with status 201 — the app posts to the host demo server's
  // self-hosted endpoint (http://localhost:5200/api/posts), transparently routed through the
  // worker's mock proxy via the device's global HTTP proxy set up at bootstrap.
  Spectra.clearMocks();
  await Spectra.intercept(
    "api/posts",
    "POST",
    Fixture.apiData.mockPostResponse,
    { statusCode: 201 }
  );

  // Fill in form fields from Fixture
  await MatchersPage.postTitleInput.type(Fixture.apiData.mockNewPost.title);
  await MatchersPage.postBodyInput.type(Fixture.apiData.mockNewPost.body);

  // Submit POST form
  await MatchersPage.submitPostButton.click();

  // Assert response elements and status
  await MatchersPage.postStatusBadge.shouldHaveText("201 Created");
  await MatchersPage.postSuccessBanner.shouldBeVisible();
  await MatchersPage.postResponseJson.shouldContainText(Fixture.apiData.mockNewPost.title);
});
