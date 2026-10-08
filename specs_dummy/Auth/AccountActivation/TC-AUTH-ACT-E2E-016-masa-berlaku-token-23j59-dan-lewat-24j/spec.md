---
id: TC-AUTH-ACT-E2E-016-masa-berlaku-token-23j59-dan-lewat-24j
title: "Boundary masa berlaku token aktivasi: 23 jam 59 menit masih valid, 25 jam kedaluwarsa"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-86
  - TC-AUTH-ACT-87
coverage:
  web: automated
---

# Boundary masa berlaku token aktivasi: 23 jam 59 menit masih valid, 25 jam kedaluwarsa

## Prerequisites

- Browser publik tanpa sesi login.
- `Mode: mock` — kemampuan membuat fixture token dengan usia tertentu: menggeser waktu server uji atau menyetel `issued_at` token secara langsung; kebutuhan ini disiapkan tim FE untuk automation.
- 2 user seeding milik automation, dibuat lewat API di hook `before` (email unik per run), dengan usia token yang di-set langsung saat seeding:
  - User A dengan token berusia 25 jam (melewati batas 24 jam).
  - User B dengan token berusia 23 jam 59 menit (masih di bawah batas).
- Akses API read-only untuk memverifikasi `issued_at` kedua token sesuai fixture.

## Test Steps

### Link berusia lebih dari 24 jam menampilkan varian Expired (TC-AUTH-ACT-86)

1. Verifikasi via API bahwa token user A berusia 25 jam dan masih berstatus Active.
2. Buka link aktivasi user A di browser.
3. Verifikasi halaman Invalid Link varian Expired tampil: Title "Activation Link Expired" dan Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
4. Verifikasi tidak ada button CTA (tidak ada "Go to Login") dan form Set Password tidak ditampilkan.

### Link berusia 23 jam 59 menit masih menampilkan form (TC-AUTH-ACT-87)

5. Verifikasi via API bahwa token user B berusia 23 jam 59 menit dan berstatus Active.
6. Buka link aktivasi user B di browser.
7. Verifikasi halaman `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for <email user B>."
8. Verifikasi halaman Invalid Link tidak tampil.
9. Kosongkan field tanpa menekan button "Set Password" (token user B tidak dikonsumsi).

## Notes

- Usia token dibuat lewat fixture pada saat seeding, bukan dengan menunggu; kebutuhan fixture waktu dicatat di Prerequisites sebagai bahan tim FE.
- Kedua kasus hanya membuka link tanpa submit sehingga token tetap Active dan tidak ada data yang berubah; urutan dari kasus kedaluwarsa ke kasus valid.
