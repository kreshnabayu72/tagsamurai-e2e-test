it("Verify uploading image and document fixtures to file input", async () => {
  await PlaygroundPage.open();

  // 1. Upload sample image fixture
  await PlaygroundPage.fileInput.upload(Fixture.sampleImage);
  await PlaygroundPage.uploadedFilename.shouldContainText("sampleImage");

  // 2. Upload sample PDF document fixture
  await PlaygroundPage.fileInput.upload(Fixture.sampleDocument);
  await PlaygroundPage.uploadedFilename.shouldContainText("sampleDocument");
});
