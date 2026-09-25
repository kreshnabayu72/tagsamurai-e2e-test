export default async function () {
  await PlaygroundPage.open();
  await PlaygroundPage.hiddenElement.shouldBeVisible();
  await PlaygroundPage.existingElement.shouldExist();
}
