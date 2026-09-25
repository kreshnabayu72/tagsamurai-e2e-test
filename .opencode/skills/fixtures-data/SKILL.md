---
name: fixtures-data
description: TestSpectra test data fixtures — JSON, documents, images, and media under fixtures/, auto-typed globally under Fixture.* with zero imports, and how to reference/upload/refactor them from test scripts, steps, and hooks. Use whenever a test needs static mock data (credentials, catalog items, payloads, locales) or binary files (images, PDFs, documents) for file uploads.
---

# Skill: Fixture & Test Data Management

Use this skill whenever a test case, shared step, or hook needs static data or binary files — user credentials, product catalogs, mock API payloads, localization strings, images (`.png`, `.jpg`, `.svg`), documents (`.pdf`, `.docx`, `.csv`), or media files.

---

## 1. Directory & Supported File Types

```
workspace-root/
└── fixtures/
    ├── users.json               # JSON data (user roles & credential sets)
    ├── products.json            # JSON data (catalog items & SKU metadata)
    ├── apiPayloads.json         # JSON data (mock response payloads)
    ├── sampleImage.png          # Image fixture for avatar & photo uploads
    ├── sampleDocument.pdf       # Document fixture for PDF/report uploads
    ├── exportData.csv           # Tabular CSV data fixture
    ├── vectorIcon.svg           # Vector graphics fixture
    └── sampleVideo.mp4          # Media video fixture
```

### Supported File Formats

| Category                | Extensions                                                                               | Global `Fixture.*` Type          | Runtime Value                          | Common Use Case                                                                |
| :---------------------- | :--------------------------------------------------------------------------------------- | :------------------------------- | :------------------------------------- | :----------------------------------------------------------------------------- |
| **Structured JSON**     | `.json`                                                                                  | `typeof import('.../file.json')` | Parsed JS `Object` / `Array`           | Auth credentials, API response payloads, seed data, localization dictionaries. |
| **Image Assets**        | `.png`, `.jpg`, `.jpeg`, `.svg`, `.webp`, `.gif`, `.ico`, `.bmp`                         | `string`                         | File path (E2E) / Data URL (Component) | Avatar uploads, photo attachments, canvas/OCR tests, visual baselines.         |
| **Documents & Text**    | `.pdf`, `.csv`, `.tsv`, `.txt`, `.md`, `.xml`, `.html`, `.doc`, `.docx`, `.xls`, `.xlsx` | `string`                         | File path (E2E) / Data URL (Component) | Document uploads, invoice validation, tabular CSV feeds.                       |
| **Media & Audio/Video** | `.mp4`, `.webm`, `.mov`, `.mp3`, `.wav`, `.ogg`                                          | `string`                         | File path (E2E) / Data URL (Component) | Media player testing, streaming verification, file upload inputs.              |
| **Archives & Binaries** | `.zip`, `.tar`, `.gz`, `.bin`, `.dat`                                                    | `string`                         | File path (E2E) / Data URL (Component) | Compressed archive uploads, binary attachments.                                |

---

## 2. Ambient Typing (Zero Import)

The `TypeGenerator` watches `fixtures/` and emits `.testspectra/types/fixtures.d.ts` automatically whenever a fixture file is created, modified, or removed:

```typescript
declare global {
  namespace Fixture {
    // JSON files provide full object property autocomplete
    const users: typeof import('../../fixtures/users.json');
    const products: typeof import('../../fixtures/products.json');

    // Non-JSON fixtures are typed as string
    const sampleImage: string;
    const sampleDocument: string;
    const exportData: string;
  }
}
```

Never hand-write this file, and never `import` a fixture file directly — always access it via the global `Fixture.<fileBaseName>` namespace, exactly like Page Objects and `Step.*`.

---

## 3. Usage & Examples

### A. Working with JSON Data in Tests

```typescript
it('should login with admin credentials from fixture', async () => {
  await Spectra.navigate('/auth/login');
  await LoginPage.emailInput.type(Fixture.users.admin.email, { clearFirst: true });
  await LoginPage.passwordInput.type(Fixture.users.admin.password);
  await LoginPage.submitButton.click();

  await DashboardPage.welcomeMsg.shouldContainText(Fixture.users.admin.name);
});
```

### B. File Uploads with Non-JSON Fixtures

In both Component testing and E2E testing, pass non-JSON fixtures directly into `.upload()` or `.setValue()`. Original file names and MIME types are automatically preserved:

```typescript
it('should upload image and document fixtures', async () => {
  await Spectra.navigate('/profile');

  // Upload image fixture (.png)
  await ProfilePage.avatarInput.upload(Fixture.sampleImage);
  await ProfilePage.uploadedAvatarName.shouldContainText('sampleImage');

  // Upload document fixture (.pdf)
  await ProfilePage.documentInput.upload(Fixture.sampleDocument);
  await ProfilePage.uploadedDocName.shouldContainText('sampleDocument');
});
```

### C. In Shared Steps

```typescript
// support/steps/loginUser/web.step.ts
export default async function (userType: 'admin' | 'standardUser' = 'standardUser') {
  const user = Fixture.users[userType];
  await Spectra.navigate('/auth/login');
  await LoginPage.emailInput.type(user.email, { clearFirst: true });
  await LoginPage.passwordInput.type(user.password);
  await LoginPage.submitButton.click();
}
```

### D. Mocking with `Spectra.intercept`

```typescript
// Mock API responses with JSON fixtures
await Spectra.intercept('GET', '/api/users', Fixture.users);

// Mock file downloads with PDF fixtures
await Spectra.intercept('GET', '/downloads/report.pdf', {
  body: Fixture.sampleDocument,
  headers: { 'Content-Type': 'application/pdf' },
});
```

---

## 4. Renaming a Fixture

Never rename a fixture file by hand. Use:

```bash
spectra refactor fixture sampleImage brandLogo
```

This renames `fixtures/sampleImage.png` $\rightarrow$ `fixtures/brandLogo.png`, rewrites every `Fixture.sampleImage` reference across `specs/**/*.test.ts`, `support/steps/**/*.step.ts`, and `hooks/**` to `Fixture.brandLogo`, and regenerates `.testspectra/types/fixtures.d.ts` immediately with 0 TypeScript compilation errors.
