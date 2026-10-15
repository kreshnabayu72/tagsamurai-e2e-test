---
id: TC-AC-PP-E2E-012-role-matrix-positif-read-only-detail-download
title: "Role Matrix Positif: Read Only Mengeksekusi Detail Versi dan Download CSV"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-23
  - TC-AC-PP-24
coverage:
  web: automated
---

# Role Matrix Positif: Read Only Mengeksekusi Detail Versi dan Download CSV

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-AC-PP-23, TC-AC-PP-24 | Read Only (Principal, "Manage privacy policy" Read saja) | Dewi Lestari | `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` |

- Login akun Read Only dilakukan di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; nama env `AC_RO_PASSWORD` dan `AC_TC_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`; selain `AC_TC_PASSWORD`, nama itu belum terdaftar.
- Dataset Riwayat A (Version 3 Active/John Doe 10 Aug 2026 pukul 20:30 UTC, Version 2/John Doe 02 Jul 2026, Version 1/Jane Smith 15 Jan 2026 dengan akun sudah dihapus) di-seed di hook `before` lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat versi append-only) dan dikembalikan ke Riwayat A di hook `after`. Spec tidak membuat atau mengubah versi.
- Kemampuan teknis: penangkapan unduhan file browser untuk TC-AC-PP-24 (nama file).
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).

## Test Steps

### TC-AC-PP-23: Read Only mengeksekusi Detail versi Superseded sampai konten tampil

1. Buka Settings > Privacy Policy
2. Klik `[⋯]` pada baris `Version 2`
3. Pilih `Detail`
4. Tunggu konten termuat
5. Verifikasi `Settings > Privacy Policy > Popup Privacy Policy Detail` terbuka
6. Verifikasi info bar menampilkan `Version 2`
7. Verifikasi info bar menampilkan `Published At`
8. Verifikasi info bar menampilkan `Published By` `John D` sebagai komponen user dengan ikon user generik
9. Hover `John D` pada info bar
10. Verifikasi tooltip `John Doe` tampil
11. Verifikasi konten tampil rendered read-only
12. Verifikasi footer modal kosong
13. Klik `[✕]` pada header modal

### TC-AC-PP-24: Read Only mengeksekusi Download CSV sampai file terunduh

14. Klik icon Download di toolbar
15. Pilih "Download as CSV"
16. Verifikasi file `Privacy-Policy-Version-History.csv` terunduh
17. Verifikasi tidak ada toast sukses

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a konvensi): role Read Only dengan aksi baca yang tetap tersedia. Eksekusi Publish oleh Default User ada di spec `TC-AC-PP-E2E-013-role-matrix-positif-default-user-publish`; spec ini tidak membuat data sehingga dipisah dari spec Publish.
- Langkah penghubung: langkah 13 (menutup modal Detail lewat `[✕]`, tanpa dialog karena modal bersih) sebelum TC-AC-PP-24.
- Langkah 9 (hover `John D`) adalah aksi yang diperlukan agar tooltip `John Doe` pada Expected b TC-AC-PP-23 dapat diasersi.
- Temuan untuk QA: TC-AC-PP-23 Expected b menyebut `Published At` tanpa nilai tanggal; spec mengasersi keberadaan label dan nilai tanggal ditentukan Date Format General Settings (`02 Jul 26` pada `dd MMM yy`, sesuai TC-AC-PP-27). Post Condition kedua TC ("Tidak ada perubahan data") tidak punya langkah observasi sehingga tidak diasersi.
