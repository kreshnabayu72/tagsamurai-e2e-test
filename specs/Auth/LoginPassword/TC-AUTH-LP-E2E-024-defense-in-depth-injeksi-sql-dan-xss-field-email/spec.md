---
id: TC-AUTH-LP-E2E-024-defense-in-depth-injeksi-sql-dan-xss-field-email
title: Defense-in-Depth, injeksi SQL dan XSS pada field Email
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-144
  - TC-AUTH-LP-145
coverage:
  web: automated
---

# Defense-in-Depth, injeksi SQL dan XSS pada field Email

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- Environment uji terisolasi khusus pengujian otomatis.
- Password valid `Spectra.env.AUTH_PASSWORD` tersedia di environment variables.
- Data fixture `Fixture.authLoginPassword` tersedia untuk nilai email valid, format tidak valid, batas karakter, dan payload injection.
- Endpoint reCAPTCHA dapat diselesaikan otomatis atau dilewati melalui token bypass uji automation.

## Test Steps

### Injeksi SQL ditolak sebagai format email tidak valid

1. Buka halaman Login with Password di browser web
2. Isi password `Spectra.env.AUTH_PASSWORD` pada field Password
3. Ganti isi field Email dengan string injeksi SQL `' OR 1=1 --`
4. Selesaikan reCAPTCHA lalu klik tombol [Log in]
5. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
6. Verifikasi tidak ada error server 500 atau kebocoran data database

### Injeksi script (XSS) ditampilkan sebagai teks murni tanpa eksekusi

7. Ganti isi field Email dengan string script `<script>alert(1)</script>`
8. Selesaikan reCAPTCHA lalu klik tombol [Log in]
9. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
10. Verifikasi teks ditampilkan sebagai teks murni tanpa ada dialog alert atau eksekusi script

## Notes

- Validasi format Email menolak payload tidak aman (`' OR 1=1 --`, `<script>`) sehingga tidak dieksekusi maupun direfleksikan ke user; server tidak menghasilkan 500 atau kebocoran data (TC-AUTH-LP-144, TC-AUTH-LP-145, PRD `V-AUTHLP-02`, `V-AUTHLP-03`).
- Spec ini dipecah dari E2E-001 agar uji keamanan injeksi terisolasi dari uji screening dan validasi format biasa (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).