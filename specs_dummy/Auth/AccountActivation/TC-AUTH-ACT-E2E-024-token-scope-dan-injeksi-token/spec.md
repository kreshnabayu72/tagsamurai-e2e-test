---
id: TC-AUTH-ACT-E2E-024-token-scope-dan-injeksi-token
title: "Token scope: token milik user lain tidak berlaku dan token berisi injeksi/skrip ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-113
  - TC-AUTH-ACT-119
  - TC-AUTH-ACT-120
coverage:
  web: automated
---

# Token scope: token milik user lain tidak berlaku dan token berisi injeksi/skrip ditolak

## Prerequisites

- Browser publik tanpa sesi login.
- Sesi login Role: Total Control (Global Settings) di browser admin, untuk memeriksa badge pada `Global Settings > User > Login User`.
- 2 user seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run): user A dan user B untuk TC-AUTH-ACT-113; kasus token injeksi memakai nilai token karangan tanpa user.
- Akses API read-only untuk memverifikasi hanya user A yang berubah status dan token user B tetap Active.

## Test Steps

### Token berisi pola injeksi SQL diperlakukan tidak valid (TC-AUTH-ACT-119)

1. Buka link aktivasi dengan nilai token `' OR '1'='1` (di-URL-encode).
2. Verifikasi halaman Invalid Link varian Expired tampil: Title "Activation Link Expired" dan Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
3. Verifikasi tidak ada button CTA (tidak ada "Go to Login") dan form Set Password tidak ditampilkan.
4. Verifikasi tidak ada pesan error teknis atau detail sistem pada halaman.

### Token berisi skrip HTML tidak dieksekusi dan dianggap tidak valid (TC-AUTH-ACT-120)

5. Buka link aktivasi dengan nilai token `<script>alert(1)</script>` (di-URL-encode).
6. Verifikasi halaman Invalid Link varian Expired tampil: Title "Activation Link Expired" dan Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
7. Verifikasi tidak ada button CTA dan form Set Password tidak ditampilkan.
8. Verifikasi tidak ada dialog skrip yang muncul dan teks token tidak ditampilkan di halaman.

### Token milik user A tidak dapat mengaktifkan user B (TC-AUTH-ACT-113)

9. Buka link aktivasi user A (token A), lakukan Set Password dengan `Aman#Sandi8` pada kedua field, lalu klik button "Set Password" sampai Activation Success tampil.
10. Pada browser admin, buka `Global Settings > User > Login User` dan cari user A serta user B.
11. Verifikasi hanya user A yang tidak lagi berbadge Pending Activation; user B tetap berbadge Pending Activation.
12. Buka link aktivasi user B (token B) di browser.
13. Verifikasi halaman Set Password tampil dengan Subtitle "Set a password to log in for <email user B>." (token B tetap valid).
14. Verifikasi via API bahwa hanya user A yang Activated, sedangkan user B tetap Pending Activation dengan token Active.

## Notes

- Kasus token karangan (non-destruktif) didahulukan; aktivasi user A diletakkan terakhir karena mengonsumsi token.
- Kebutuhan dua user seeding dan sesi admin dicatat di Prerequisites.
