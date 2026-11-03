---
id: TC-AC-DC-E2E-092-defense-request-langsung-validasi-server
title: "Defense-in-Depth: Request Langsung Melanggar Validasi Server Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-250
  - TC-AC-DC-251
  - TC-AC-DC-252
  - TC-AC-DC-253
coverage:
  web: automated
---
# Defense-in-Depth: Request Langsung Melanggar Validasi Server Ditolak

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control (Pre-setup #1); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name).

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Total Control (`Budi Santoso`) | #1 `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Kemampuan teknis: sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web) dan klien HTTP; disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data Dinamis (dibuat spec ini lewat API di hook `before` oleh Total Control #1): node `Pemindai Nama {runId}-092` dan `Pemindai Ganda {runId}-092` (leaf di bawah `Handheld Reader`); node `Induk Rujuk {runId}-092` (di bawah `Handheld Reader`) dengan anak `Anak Rujuk {runId}-092`; Device Name `DN-{runId}-092` yang merujuk `Anak Rujuk {runId}-092` (nilai field wajib Device Name selain Category disediakan tim FE).
- Data Pre-setup: #14 (Pohon Uji Kategori; `Rantai L5` dan `Rantai L6` hanya dibaca). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- State global: Hierarchy Depth Limit entitas uji (Pre-setup #18, nilai awal 50) diatur ke 5 di langkah 9 dan dipulihkan ke 50 di langkah 20; hook `after` memulihkannya ke 50 sebagai cadangan. Kemampuan mengatur Hierarchy Depth Limit (Lifecycle Settings) disediakan tim FE/BE; Pre-setup #9 tercatat berhak mengubah Lifecycle Settings.
- Hook `after`: menghapus semua node (dan Device Name) yang dibuat spec ini, termasuk node hasil aksi UI yang dikenali dari sufiks `{runId}-092`, lewat API dari anak ke induk; cleanup tidak berasumsi seeding berhasil penuh.
- Seeding dan cleanup menambah entri Changelog dan log audit permanen (Create dan Delete atas node bersufiks); entri itu tidak diasersi. Asersi Changelog tidak bertambah untuk request yang sama berada di spec 098 (S-05).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-250: Request langsung dengan nama All Categories ditolak server

1. Kirim request create dengan parent `Pemindai Nama {runId}-092` dan nama "All Categories" memakai token Total Control
2. Kirim request update nama `Pemindai Nama {runId}-092` menjadi "all categories" memakai token Total Control
3. Verifikasi kedua request ditolak server
4. Muat ulang halaman Device Name
5. Expand `Hardware`
6. Expand `Handheld Reader`
7. Verifikasi nama `Pemindai Nama {runId}-092` tidak berubah
8. Verifikasi tidak ada node bernama "All Categories" di bawah `Pemindai Nama {runId}-092`

### TC-AC-DC-251: Request langsung melampaui Hierarchy Depth Limit ditolak server

9. Atur Hierarchy Depth Limit entitas uji menjadi 5 di Lifecycle Settings
10. Kirim request create nama "Bypass Depth {runId}-092" dengan parent `Rantai L5` memakai token Total Control
11. Verifikasi request ditolak server
12. Muat ulang halaman Device Name
13. Expand `Hardware`
14. Expand `Smart Fixed Reader`
15. Expand `Rantai L3`
16. Expand `Rantai L4`
17. Expand `Rantai L5`
18. Verifikasi `Rantai L6` tampil di bawah `Rantai L5`
19. Verifikasi tidak ada node "Bypass Depth {runId}-092" di bawah `Rantai L5`
20. Pulihkan Hierarchy Depth Limit entitas uji ke 50

### TC-AC-DC-252: Request langsung dengan nama duplikat di parent yang sama ditolak server

21. Kirim request create nama "pemindai ganda {runId}-092" dengan parent `Handheld Reader` memakai token Total Control
22. Verifikasi request ditolak server
23. Muat ulang halaman Device Name
24. Expand `Hardware`
25. Expand `Handheld Reader`
26. Verifikasi hanya satu node `Pemindai Ganda {runId}-092` (tanpa memandang huruf besar-kecil) di bawah `Handheld Reader`

### TC-AC-DC-253: Request langsung menghapus node yang dirujuk Device Name ditolak server

27. Kirim request delete node `Induk Rujuk {runId}-092` (anak `Anak Rujuk {runId}-092` dirujuk Device Name `DN-{runId}-092`) memakai token Total Control
28. Verifikasi request ditolak server
29. Muat ulang halaman Device Name
30. Expand `Hardware`
31. Expand `Handheld Reader`
32. Expand `Induk Rujuk {runId}-092`
33. Verifikasi `Induk Rujuk {runId}-092` dan `Anak Rujuk {runId}-092` tetap ada

## Notes

- Mode: FE+BE. K-1: Expected TC-AC-DC-250 sampai 253 berupa penolakan server dan state data; TC tetap di spec FE+BE walau tumpang tindih dengan `tc-settings-device-category-backend.md`. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Request langsung dikirim lewat klien HTTP, tidak melewati browser (8b butir 1); asersi hanya penolakan server dan state data. Muat ulang halaman Device Name dan pemeriksaan tree adalah observasi state data seperti langkah TC.
- Langkah penghubung: langkah 5, 6, 13 sampai 17, 24, 25, 30 sampai 32 (expand tree sesudah muat ulang; pohon dianggap kembali tertutup sesudah muat ulang), 9 dan 20 (mengatur dan memulihkan state global Hierarchy Depth Limit, S-09).
- S-05: klausa "Changelog tidak bertambah" pada Expected b TC-AC-DC-250, Expected TC-AC-DC-251, 252, dan 253 diasersi sebagai absence kelas g di spec 098 (P-5 a: request langsung menjadi pemicu, baseline Changelog dicatat sendiri per TC); spec ini hanya mengasersi penolakan server dan state tree.
- Anchor absence: nama node milik spec yang tidak berubah (TC-AC-DC-250), `Rantai L6` (TC-AC-DC-251), dan keberadaan node pembanding mendahului asersi "tidak ada node" (8b butir 2).
- Temuan untuk QA:
  - Target aksi tulis dan hapus memakai node milik spec bersufiks `{runId}-092` (S-06, S-12); TC memakai node literal Pre-setup #14 (`Rugged Scanner` pada TC-AC-DC-250, `Barcode Handheld` pada TC-AC-DC-252, dan `Industrial Scanner` dengan `Rugged`, `Rugged Kit`, `TS-200`, `TS-210` pada TC-AC-DC-253; nama pada request diberi sufiks `{runId}-092` kecuali "All Categories" yang menjadi objek uji) sebagai target. Hasil TC identik karena node milik spec adalah node user-created dengan perilaku yang sama; node literal Pre-setup hanya dibaca.
  - Asersi TC-AC-DC-252 ("hanya satu node `Barcode Handheld`") bergantung pada nama literal; spec memakai node milik spec bernama `Pemindai Ganda {runId}-092` dan mengirim nama yang sama dengan huruf kecil. Bila QA ingin asersi tetap pada nama literal Pre-setup, butuh keputusan pengecualian.
  - TC-AC-DC-251 memakai node literal `Rantai L5` (kedalaman 5, dibaca saja) karena rantai kedalaman hanya ada di Pre-setup #14; request create ditolak sehingga rantai tidak berubah. TC tidak menyebut aktor yang mengubah Hierarchy Depth Limit; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-AC-DC-250, 252, dan 253 Expected a tidak menyebut status respons; asersi mengikuti kalimat TC tanpa kode status. Mekanisme klien HTTP dan endpoint tidak dikarang (S-13).
  - Post Condition TC-AC-DC-250 sampai 253 ('-') tidak punya langkah observasi dan tidak diasersi.
