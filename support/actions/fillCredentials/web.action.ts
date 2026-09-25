export default async function (this: any, email: string, token: string) {
  await this.get("#demo-email-input-pg").type(email);
  await this.get("#demo-token-input-pg").type(token);
}
