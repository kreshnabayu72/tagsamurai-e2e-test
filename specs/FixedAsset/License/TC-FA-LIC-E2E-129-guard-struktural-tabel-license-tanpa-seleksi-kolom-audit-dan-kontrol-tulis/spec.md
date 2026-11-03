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
4. Verifikasi daftar kolom Subscription History tidak memuat `Modified By` dan `Last Updated`
5. Tutup popup Setup Column dengan `×`
6. Verifikasi pada baris dan header Subscription History tidak ada kontrol ubah (aksi tulis) apa pun

### Tab All License: Allocation History (T-FALIC-04)

7. Klik sub-tab `Allocation History`
8. Verifikasi tabel Allocation History tidak punya kolom checkbox dan tidak ada Bulk Action Bar
9. Klik header kolom Actions `⋯` pada tabel Allocation History
10. Klik `Setup Column...`
11. Verifikasi daftar kolom Allocation History tidak memuat `Modified By`
12. Verifikasi `Last Updated` ada sebagai kolom data pada daftar kolom Allocation History
13. Tutup popup Setup Column dengan `×`
14. Verifikasi pada baris dan header Allocation History tidak ada kontrol ubah (aksi tulis) apa pun

### Tab Concurrent User: Active Sessions (T-FALIC-02)

15. Klik Tab `Concurrent User`
16. Verifikasi tabel Active Sessions tidak punya kolom checkbox dan tidak ada Bulk Action Bar
17. Klik header kolom Actions `⋯` pada tabel Active Sessions
18. Klik `Setup Column...`
19. Verifikasi daftar kolom Active Sessions tidak memuat `Modified By` dan `Last Updated`
20. Tutup popup Setup Column dengan `×`
21. Verifikasi pada baris dan header Active Sessions satu-satunya kontrol tulis adalah tombol `[Force Logout]`

### Tab Allocation Quota: Group License Allocation (T-FALIC-03)

22. Klik Tab `Allocation Quota`
23. Verifikasi tabel Group License Allocation (node `All Groups`, Section 2) tidak punya kolom checkbox dan tidak ada Bulk Action Bar
24. Klik header kolom Actions `⋯` pada tabel Group License Allocation
25. Klik `Setup Column...`
26. Verifikasi daftar kolom Group License Allocation tidak memuat `Modified By` dan `Last Updated`
27. Tutup popup Setup Column dengan `×`
28. Verifikasi satu-satunya kontrol tulis pada Tab `Allocation Quota` adalah tombol ikon `[Edit]` pada Allocated Quota
29. Verifikasi tidak ada kontrol ubah ledger Asset License, ledger Add-on, Allocation History, atau Subscription History pada seluruh tab dan sub-tab yang ditelusuri

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-83, 84, 439). Tidak ada TC hanya-BE di spec ini.
- Urutan dan penggabungan TC: ketiga TC menelusuri empat tabel yang sama, sehingga langkah dikelompokkan per tabel (bukan per TC) untuk menghindari navigasi berulang (S-10). Langkah 1, 8, 16, 23 memetakan TC-83; langkah 2 sampai 5, 9 sampai 13, 17 sampai 20, 24 sampai 27 memetakan TC-84; langkah 6, 14, 21, 28, 29 memetakan TC-439.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 5, 13, 20, 27 (menutup popup Setup Column dengan `×`), serta klik sub-tab dan tab (langkah 7, 15, 22).
- TC-83 butir a "aksi hanya individual" dibuktikan lewat langkah 21 dan 28 (satu-satunya kontrol tulis pada baris tabel adalah aksi individual `[Force Logout]` dan `[Edit]`).
- Temuan untuk QA:
  - TC-84 menyebut "Buka Column Visibility" tanpa menyebut item menu; spec memakai `Setup Column...` dari header kolom Actions `⋯` mengikuti TC-FA-LIC-595.
  - TC-439 meminta menelusuri "setiap baris dan header" tanpa daftar kontrol yang dianggap kontrol ubah; spec mengasersi atas kontrol aksi tulis (tombol aksi, menu aksi baris) dan tidak atas kontrol navigasi seperti Search, Filter, Download, dan Changelog.
