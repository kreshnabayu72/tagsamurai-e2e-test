---
id: TC-FA-LIC-E2E-129-guard-struktural-tabel-license-tanpa-seleksi-kolom-audit-dan-kontrol-tulis
title: "Guard Struktural Tabel License: Tanpa Seleksi, Tanpa Kolom Audit, dan Kontrol Tulis Terbatas"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-83
  - TC-FA-LIC-84
  - TC-FA-LIC-439
coverage:
  web: automated
---

# Guard Struktural Tabel License: Tanpa Seleksi, Tanpa Kolom Audit, dan Kontrol Tulis Terbatas

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: kuota dan hierarki #12, riwayat #13, sesi aktif #14; hanya dibaca, tidak diubah. Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Setup Column dibuka hanya untuk dibaca dan ditutup dengan `×` tanpa `[Save]`, sehingga tidak ada preferensi kolom yang tersimpan.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Tab All License: Subscription History (T-FALIC-01)

1. Verifikasi tabel Subscription History tidak punya kolom checkbox dan tidak ada Bulk Action Bar
2. Klik header kolom Actions `⋯` pada tabel Subscription History
3. Klik `Setup Column...`
4. Verifikasi daftar kolom Subscription History memuat kolom `Subscription ID`, `Plan`, `Type`, `Status`, `Start Date`, `End Date`, `Plan Owner`
5. Verifikasi daftar kolom Subscription History tidak memuat `Modified By` dan `Last Updated`
6. Tutup popup Setup Column dengan `×`
7. Verifikasi tabel Subscription History memuat sedikitnya satu baris
8. Verifikasi pada baris dan header Subscription History tidak ada kontrol ubah (aksi tulis) apa pun

### Tab All License: Allocation History (T-FALIC-04)

9. Klik sub-tab `Allocation History`
10. Verifikasi tabel Allocation History tidak punya kolom checkbox dan tidak ada Bulk Action Bar
11. Klik header kolom Actions `⋯` pada tabel Allocation History
12. Klik `Setup Column...`
13. Verifikasi daftar kolom Allocation History memuat kolom data `Allocation ID`
14. Verifikasi daftar kolom Allocation History tidak memuat `Modified By`
15. Verifikasi `Last Updated` ada sebagai kolom data pada daftar kolom Allocation History
16. Tutup popup Setup Column dengan `×`
17. Verifikasi tabel Allocation History memuat sedikitnya satu baris
18. Verifikasi pada baris dan header Allocation History tidak ada kontrol ubah (aksi tulis) apa pun

### Tab Concurrent User: Active Sessions (T-FALIC-02)

19. Klik Tab `Concurrent User`
20. Verifikasi tabel Active Sessions tidak punya kolom checkbox dan tidak ada Bulk Action Bar
21. Klik header kolom Actions `⋯` pada tabel Active Sessions
22. Klik `Setup Column...`
23. Verifikasi daftar kolom Active Sessions memuat kolom `User Name`, `Email`, `Position`, `Division`, `IP Address`, `Device / OS`, `Browser`, `Login Time`, `Last Activity`
24. Verifikasi daftar kolom Active Sessions tidak memuat `Modified By` dan `Last Updated`
25. Tutup popup Setup Column dengan `×`
26. Verifikasi pada baris dan header Active Sessions satu-satunya kontrol tulis adalah tombol `[Force Logout]`

### Tab Allocation Quota: Group License Allocation (T-FALIC-03)

27. Klik Tab `Allocation Quota`
28. Verifikasi tabel Group License Allocation (node `All Groups`, Section 2) tidak punya kolom checkbox dan tidak ada Bulk Action Bar
29. Klik header kolom Actions `⋯` pada tabel Group License Allocation
30. Klik `Setup Column...`
31. Verifikasi daftar kolom Group License Allocation memuat kolom `Group Name`, `Group Code`, `Allocated Quota`, `Allocated to Subgroups`, `Used by This Group`, `Reserved by This Group`, `Remaining Quota`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`
32. Verifikasi daftar kolom Group License Allocation tidak memuat `Modified By` dan `Last Updated`
33. Tutup popup Setup Column dengan `×`
34. Verifikasi satu-satunya kontrol tulis pada Tab `Allocation Quota` adalah tombol ikon `[Edit]` pada Allocated Quota
35. Verifikasi tidak ada kontrol ubah ledger Asset License, ledger Add-on, Allocation History, atau Subscription History pada seluruh tab dan sub-tab yang ditelusuri

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-83, 84, 439). Tidak ada TC hanya-BE di spec ini.
- Urutan dan penggabungan TC: ketiga TC menelusuri empat tabel yang sama, sehingga langkah dikelompokkan per tabel (bukan per TC) untuk menghindari navigasi berulang (S-10). Langkah 1, 10, 20, 28 memetakan TC-83; langkah 2 sampai 6, 11 sampai 16, 21 sampai 25, 29 sampai 33 memetakan TC-84; langkah 8, 18, 26, 34, 35 memetakan TC-439.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 6, 16, 25, 33 (menutup popup Setup Column dengan `×`), serta klik sub-tab dan tab (langkah 9, 19, 27).
- Anchor absence (bagian 8b butir 2): langkah 4, 23, dan 31 adalah klausa TC-84 a (daftar kolom tiap tabel) yang sekaligus membuktikan daftar kolom sudah termuat sebelum asersi absence `Modified By` dan `Last Updated` (langkah 5, 24, dan 32). Langkah 13 adalah `Verifikasi` kolom data `Allocation ID` sebagai anchor tambahan (S-03) karena TC-84 b tidak memuat daftar kolom T-FALIC-04 sebelum asersi absence `Modified By` (langkah 14). Langkah 7 dan 17 adalah `Verifikasi` sedikitnya satu baris pada Subscription History dan Allocation History sebagai anchor absence kontrol ubah (S-03).
- TC-83 butir a "aksi hanya individual" dibuktikan lewat langkah 26 dan 34 (satu-satunya kontrol tulis pada baris tabel adalah aksi individual `[Force Logout]` dan `[Edit]`).
- Temuan untuk QA:
  - TC-84 butir b tidak memuat daftar kolom T-FALIC-04 sebagai anchor sebelum absence `Modified By`; spec menambahkan anchor sendiri (langkah 13) dengan kolom `Allocation ID` dari Setup Column tabel itu.
  - TC-84 menyebut "Buka Column Visibility" tanpa menyebut item menu; spec memakai `Setup Column...` dari header kolom Actions `⋯` mengikuti TC-FA-LIC-595.
  - TC-439 meminta menelusuri "setiap baris dan header" tanpa daftar kontrol yang dianggap kontrol ubah; spec mengasersi atas kontrol aksi tulis (tombol aksi, menu aksi baris) dan tidak atas kontrol navigasi seperti Search, Filter, Download, dan Changelog.
