---
id: TC-AC-ACC-E2E-019-anchor-dan-group-viewer-partner-mitra-timur
title: "Anchor dan Group Client Lintas Jaringan untuk Viewer Partner CV Mitra Timur"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-568
coverage:
  web: automated
---

# Anchor dan Group Client Lintas Jaringan untuk Viewer Partner CV Mitra Timur

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-AST-1 | Partner Total Control (CV Mitra Timur) | `totalControlPartnerTimur_automated_cvMitraTimur@qwertysystem.net` | `Spectra.env.AC_CLIENT_PARTNER_TIMUR_TC_PASSWORD` |

- Login di hook `before` spec ini (Partner Total Control, A-AST-1); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Pre-setup `C-10` `PT Lintas Jaringan` (dibuat Principal dengan Partner CV Mitra Sejati; CV Mitra Timur ditambahkan via Change Partner oleh Principal; Group tidak di-assign CV Mitra Timur) hanya dibaca.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-568: Anchor per viewer: Partner jaringan lain melihat dirinya sebagai Anchor dan Group tanpa assignment Partner

1. Ketik Search `PT Lintas Jaringan`, tekan Enter
2. Lihat sel Managed By dan Group baris `PT Lintas Jaringan`
3. Verifikasi Managed By `PT Lintas Jaringan` diawali `CV Mitra Timur`
4. Verifikasi Managed By `PT Lintas Jaringan` tidak memuat `CV Mitra Sejati`
5. Verifikasi Group `PT Lintas Jaringan` adalah `—`
6. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: viewer lain atas Client yang sama ada di spec 013, 015, dan 017.
- Temuan untuk QA:
  - Tidak ada temuan baru pada TC sumber spec ini.
