# Coverage E2E — Auth > Account Activation

Sumber: `auth/account-activation/TestCases/tc-account-activation.md` (94 TC aktif). Suite: `specs/auth2/AccountActivation/`. Status semua spec: `draft`, belum ada script.

**Verifikasi lint:** `npx spectra lint --strict specs/auth2/AccountActivation` → `✓ 21 specs and 1 suites verified. 0 lint errors found.`

**Aturan seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, spec e2e merangkap TC FE. Semua TC masuk spec kecuali hanya-BE. Spec yang butuh kondisi terpicu (intercept untuk error/timeout, concurrency, viewport mobile, simulasi race) ditandai kebutuhan mock di `Prerequisites`. Hambatan teknis dicatat di `Prerequisites`, bukan menjadi alasan mengeluarkan TC.

**Nomor folder.** Prefix `TC-AUTH-ACT-E2E-` berasal dari `AUTH` + `ACT` (Account Activation). Nomor adalah urutan spec (`001`–`021`), bukan nomor TC sumber, sehingga tidak sama dengan nomor TC granular. Nomor bersifat forward-only: kalau spec dipecah menjadi beberapa spec, spec pecahan memakai nomor urut baru di tengah rentang, dan spec setelahnya ikut bergeser. Hubungan spec lama → spec hasil split dicatat di bagian [Catatan split](#catatan-split).

**Verifikasi duplikasi:** 80 TC granular terreferensi tepat 1 spec, 0 duplikasi. Nama folder setiap spec sama persis dengan `id` di frontmatter `spec.md`.

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-ACT-E2E-001 | Screening trigger Activation Email: pembuatan user (GS>User & Admin Console), template email verbatim, snapshot Full Name, token hash SHA-256 (64 hex), raw token 43 char Base64URL, expires_at +24h, zero-logging trigger | 1–9, 93 | web |
| TC-AUTH-ACT-E2E-002 | Token valid: render Set Password, loading state, GET idempotent, subtitle email penuh | 10, 17–19 | web |
| TC-AUTH-ACT-E2E-003 | Token expired & superseded → 404 "Activation Link Expired" | 11, 13 | web |
| TC-AUTH-ACT-E2E-004 | Token consumed → 404 "Link Already Used" + CTA "Go to Login" | 12 | web |
| TC-AUTH-ACT-E2E-005 | Token malformed/tidak dikenal/injection-like + user deleted → 404 generik, anti-kebocoran | 14–15 | web |
| TC-AUTH-ACT-E2E-006 | Server error saat validasi GET (5xx/timeout) → error state + [Try Again], bukan 404 (mock) | 16 | web |
| TC-AUTH-ACT-E2E-007 | Password Policy & real-time checklist: boundary 8/72/73, upper/lower/number/special/spaces, update per keystroke, karakter khusus valid | 20–31 | web |
| TC-AUTH-ACT-E2E-008 | Validasi Confirm Password: Password kosong, Confirm kosong, mismatch | 32–34 | web |
| TC-AUTH-ACT-E2E-009 | Toggle show/hide + independen per field, aksesibilitas keyboard eye icon, ketiadaan CAPTCHA, button selalu enabled | 35–39 | web |
| TC-AUTH-ACT-E2E-010 | Happy path aktivasi, double-click prevention, retry setelah network timeout (mock) | 40–42 | web |
| TC-AUTH-ACT-E2E-011 | Concurrency/race: token dikonsumsi di tab lain, resend mid-fill | 43–44 | web |
| TC-AUTH-ACT-E2E-012 | Server error submit (5xx/timeout), 422 re-check policy, 409/404 mid-flight (mock) | 45, 48, 49 | web |
| TC-AUTH-ACT-E2E-013 | Atomicity: rollback penuh saat partial failure (fault injection) | 46 | web |
| TC-AUTH-ACT-E2E-014 | Zero-logging aksi Set Password (sukses & gagal) di 4 surface | 47 | web |
| TC-AUTH-ACT-E2E-015 | Activation Success, reload after success → 404 Used, browser back behavior, Go to Login dari success & 404 Used, zero-logging CTA | 50–56 | web |
| TC-AUTH-ACT-E2E-016 | Halaman 404 aktivasi: copy verbatim Expired/Used, anti-kebocoran penyebab teknis, tidak ada aksi destruktif | 57–60 | web |
| TC-AUTH-ACT-E2E-017 | Resend basic: token baru dibuat & token lama superseded, link lama 404 Expired, link baru berfungsi | 61–63 | web |
| TC-AUTH-ACT-E2E-018 | Multiple resend (semua token sebelumnya superseded), race submit-vs-resend, zero-logging konsekuensi resend | 64–66 | web |
| TC-AUTH-ACT-E2E-019 | Non-logging internal: buka link / set password / consume / resend / tampil 404 tidak dicatat di 4 surface | 67–70 | web |
| TC-AUTH-ACT-E2E-020 | Cross-module: login user `Pending Activation` dicatat modul Login dengan Note "Account is not activated" | 71 | web |
| TC-AUTH-ACT-E2E-021 | Responsive & A11y (L: 85–91) + Plan Gating (M: 92) | 85–92 | web |

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| 1–9, 93 | TC-AUTH-ACT-E2E-001 | FE+BE |
| 10, 17–19 | TC-AUTH-ACT-E2E-002 | FE+BE |
| 11, 13 | TC-AUTH-ACT-E2E-003 | FE+BE |
| 12 | TC-AUTH-ACT-E2E-004 | FE+BE |
| 14–15 | TC-AUTH-ACT-E2E-005 | FE+BE |
| 16 | TC-AUTH-ACT-E2E-006 | FE+BE (mock intercept) |
| 20–31 | TC-AUTH-ACT-E2E-007 | FE+BE |
| 32–34 | TC-AUTH-ACT-E2E-008 | FE+BE |
| 35–39 | TC-AUTH-ACT-E2E-009 | FE+BE |
| 40–42 | TC-AUTH-ACT-E2E-010 | FE+BE (mock utk retry timeout) |
| 43–44 | TC-AUTH-ACT-E2E-011 | FE+BE |
| 45, 48, 49 | TC-AUTH-ACT-E2E-012 | FE+BE (mock intercept) |
| 46 | TC-AUTH-ACT-E2E-013 | FE+BE (fault-injection setup) |
| 47 | TC-AUTH-ACT-E2E-014 | FE+BE |
| 50–56 | TC-AUTH-ACT-E2E-015 | FE+BE |
| 57–60 | TC-AUTH-ACT-E2E-016 | FE+BE |
| 61–63 | TC-AUTH-ACT-E2E-017 | FE+BE |
| 64–66 | TC-AUTH-ACT-E2E-018 | FE+BE |
| 67–70 | TC-AUTH-ACT-E2E-019 | FE+BE |
| 71 | TC-AUTH-ACT-E2E-020 | FE+BE (cross-module) |
| 85–92 | TC-AUTH-ACT-E2E-021 | FE+BE (mock utk plan gating jika perlu) |

## Catatan split

Lima spec awal dipecah karena tiap sub-topic punya setup data, kebutuhan mock, dan tingkat sensitivitas urutan yang berbeda (mock vs non-mock, concurrency vs flow normal, cross-module, fault-injection). Pemecahan memakai nomor urut baru sehingga spec setelahnya ikut bergeser:

| Spec lama | Spec hasil split |
|---|---|
| 002 validasi link aktivasi | 002 link valid · 003 expired/superseded · 004 consumed · 005 invalid generik · 006 server error (mock) |
| 004 confirm/toggle/a11y | 008 confirm password · 009 toggle/a11y/no-CAPTCHA/button state |
| 005 konsumsi token | 010 happy path/double-submit/retry · 011 concurrency/race · 012 server error/422/409 · 013 atomicity · 014 zero-logging |
| 008 resend invalidasi | 017 resend basic · 018 multiple resend/race/zero-logging |
| 009 non-logging | 019 non-logging internal · 020 cross-module login |

Spec yang tidak dipecah karena topiknya tunggal dan saling terkait erat: 001 (trigger email), 007 (Password Policy), 015 (Activation Success + navigasi), 016 (halaman 404 copy), 021 (responsive/A11y/plan gating).

## TC belum dipetakan

TC 72–84 dan 93–94 tidak dipetakan ke spec e2e pada suite ini. Sebagian di antaranya merupakan TC backend-only atau non-regresi yang berada di file `tc-account-activation-backend.md`, dan sebagian lain perlu konfirmasi cakupan bersama tim QA sebelum dipetakan.
