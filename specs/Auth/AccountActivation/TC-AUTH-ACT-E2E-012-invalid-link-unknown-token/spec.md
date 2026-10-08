---
id: TC-AUTH-ACT-E2E-012-invalid-link-unknown-token
title: "Halaman Invalid Link untuk Token Tidak Dikenal atau Salah Bentuk"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-09
  - TC-AUTH-ACT-79
  - TC-AUTH-ACT-80
  - TC-AUTH-ACT-81
  - TC-AUTH-ACT-82
coverage:
  web: automated
---

# Halaman Invalid Link untuk Token Tidak Dikenal atau Salah Bentuk

## Prerequisites

- Akun aktor seeding: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Tanpa login: semua TC berjalan di halaman publik tanpa sesi aktif di browser.
- Tidak ada password atau token rahasia di spec atau fixture. Token `unknown-token-12345` adalah nilai uji yang memang tidak dikenal sistem.
- Hook `before` (seeding API) membuat user `Surya Anggraini` (`suryaanggraini+{runId}-012@qwertysystem.net`) untuk TC-AUTH-ACT-82, Pending Activation dengan token Active, dan menyimpan link aktivasinya; hook `after` menghapus user itu (tetap jalan walau seeding gagal sebagian).
- TC-AUTH-ACT-80 dan TC-AUTH-ACT-81: alamat `/activate` tanpa parameter token dan `/activate?token=` dibuka langsung.
- Kemampuan teknis: mengubah URL secara langsung (memotong nilai parameter `token`).

## Test Steps

### TC-AUTH-ACT-09: Link dengan token tidak dikenal menampilkan halaman 404 tanpa respons akses ditolak

1. Buka link aktivasi dengan token yang tidak dikenal `unknown-token-12345` → halaman `Auth > Account Activation > Invalid Link` tampil
2. Verifikasi Title "Activation Link Expired" tampil pada halaman Invalid Link
3. Verifikasi Tidak ada toast, dialog, atau halaman akses ditolak (forbidden) dan tidak ada redirect ke Login

### TC-AUTH-ACT-79: Screening halaman Invalid Link varian Expired untuk token tidak dikenal

4. Buka link aktivasi dengan token `unknown-token-12345` → halaman `Auth > Account Activation > Invalid Link` tampil
5. Susuri halaman dari atas ke bawah
6. Verifikasi **Header**: Card (Elevated) single-column; ilustrasi 404/expired
7. Verifikasi **Body**: Title "Activation Link Expired"; Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
8. Verifikasi **Footer**: tidak ada CTA (tidak ada button "Go to Login") dan tidak ada aksi destruktif; form Set Password tidak ditampilkan

### TC-AUTH-ACT-80: Link aktivasi tanpa parameter token menampilkan halaman Invalid Link varian Expired

9. Buka alamat halaman aktivasi tanpa parameter `token` (mis. `/activate`)
10. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil: Title "Activation Link Expired", Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
11. Verifikasi Tidak ada button CTA (tidak ada "Go to Login") pada halaman dan form Set Password tidak ditampilkan

### TC-AUTH-ACT-81: Link aktivasi dengan parameter token kosong menampilkan halaman Invalid Link varian Expired

12. Buka alamat halaman aktivasi dengan parameter token kosong (mis. `/activate?token=`)
13. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil: Title "Activation Link Expired", Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
14. Verifikasi Tidak ada button CTA (tidak ada "Go to Login") pada halaman dan form Set Password tidak ditampilkan

### TC-AUTH-ACT-82: Token yang terpotong menampilkan halaman Invalid Link varian Expired

15. Buka link aktivasi user `Surya Anggraini` di browser → halaman `Auth > Account Activation > Set Password` tampil
16. Salin link aktivasi, lalu potong 5 karakter terakhir dari nilai parameter `token`
17. Buka link yang sudah dipotong
18. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil: Title "Activation Link Expired", Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
19. Verifikasi Tidak ada button CTA (tidak ada "Go to Login") pada halaman dan form Set Password tidak ditampilkan
20. Verifikasi Token asli user `Surya Anggraini` tetap Active

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- TC-AUTH-ACT-09 dan TC-AUTH-ACT-79 memakai alur yang sama (buka `unknown-token-12345`, cek Title Expired); keduanya dipertahankan sesuai TC sumber dan asersinya berbeda (TC-09: tanpa toast/forbidden/redirect; TC-79: screening halaman), sehingga keduanya tetap diuji.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
