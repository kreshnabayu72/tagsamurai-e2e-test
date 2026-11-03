---
id: TC-AC-RP-E2E-086-download-berkas-role-detail-dan-changelog
title: "Download Isi Berkas: Role Detail, Filename Title-Case, dan Changelog per Varian"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-284
  - TC-AC-RP-285
  - TC-AC-RP-314
coverage:
  web: automated
---

# Download Isi Berkas: Role Detail, Filename Title-Case, dan Changelog per Varian

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #15 (penugasan peran individual), dan #18 (riwayat Changelog seed). Role Detail yang dipakai: `Manage hardware stock` (Global Role), `Manage wallet & pricing` (Group Role), dan `Manage device master data` (Global Role).
- Kemampuan teknis: membaca nama dan isi berkas yang terunduh (CSV dan XLSX: nilai sel, urutan kolom) dari folder unduhan browser (disediakan tim FE); tidak memakai klien HTTP.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis bersuffix `+{runId}-<NNN>` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-284: Download Role Detail Global menulis CRUD Yes, No, dan tanda tidak berlaku

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage hardware stock` lalu klik `Detail`
3. Klik ikon Download, lalu klik Download as XLSX
4. Verifikasi berkas `Role-Permission-Manage-Hardware-Stock.xlsx` terunduh
5. Verifikasi isi berkas: kolom C, R, dan D bernilai `Yes` atau `No`
6. Verifikasi isi berkas: kolom U bernilai `-`

### TC-AC-RP-285: Filename Download Role Detail mengikuti nama role Title-Case

7. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
8. Pada section Group Role, klik `⋯` pada baris `Manage wallet & pricing` lalu klik `Detail`
9. Klik ikon Download, lalu klik Download as CSV
10. Verifikasi berkas `Role-Permission-Manage-Wallet-And-Pricing.csv` terunduh

### TC-AC-RP-314: Download Changelog per varian

11. Buka halaman `Settings > Role & Permission`
12. Klik ikon Changelog
13. Klik ikon Download, lalu klik Download as CSV
14. Verifikasi tidak ada toast sukses yang tampil
15. Verifikasi berkas `Changelog-Role-Permission-Total-Control.csv` terunduh
16. Tutup modal Changelog
17. Klik tab `System`
18. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
19. Klik ikon Changelog
20. Klik ikon Download, lalu klik Download as CSV
21. Verifikasi tidak ada toast sukses yang tampil
22. Verifikasi berkas `Changelog-Role-Permission-Manage-Device-Master-Data.csv` terunduh
23. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness f (isi berkas unduhan); nama berkas dan isi sel dibaca dari berkas yang terunduh.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 7, 11, 16, 23.
- Asersi absence toast sukses diletakkan segera setelah pemicu Download, sebelum Verifikasi berkas terunduh yang menjadi anchor positifnya (bagian 8b butir 11).
- Langkah "Ulangi pada Detail `Manage device master data`" TC-AC-RP-314 ditulis sebagai rangkaian langkah penuh (langkah 17 sampai 23), bukan rujukan.
- Langkah "Klik ikon Download, lalu klik Download as ..." membuka popover Download lalu memilih format sebagai satu aksi (PRD §4.2e; pola spec 085 langkah 1 dan 3); popover tidak diasersi di spec ini karena Expected TC tidak memuatnya.
- Temuan untuk QA:
  - TC-AC-RP-284 tidak menyebut baris atau nama kolom berkas yang dibaca untuk nilai `Yes`/`No`/`-`; spec mengasersi seluruh sel kolom C, R, D dan kolom U pada berkas.
