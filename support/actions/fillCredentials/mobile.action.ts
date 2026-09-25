export default async function (this: any, email: string, token: string) {
  await this.get("~pg-email-input").type(email);
  await this.get("~pg-token-input").type(token);
}
