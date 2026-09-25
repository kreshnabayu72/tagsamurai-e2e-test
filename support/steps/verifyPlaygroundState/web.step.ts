export default async function () {
  await PlaygroundPage.open();
  await PlaygroundPage.visibleElement.shouldBeVisible();
  await PlaygroundPage.enabledButton.shouldBeEnabled();
  await PlaygroundPage.termsCheckbox.shouldBeChecked();
}
