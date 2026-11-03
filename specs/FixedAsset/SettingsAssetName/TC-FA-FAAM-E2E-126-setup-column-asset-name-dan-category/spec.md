---
id: TC-FA-FAAM-E2E-126-setup-column-asset-name-dan-category
title: "Setup Column: Ceklis dan Geser Kelas Asset Name dan Category"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-404
  - TC-FA-FAAM-405
  - TC-FA-FAAM-410
  - TC-FA-FAAM-411
coverage:
  web: automated
---

# Setup Column: Ceklis dan Geser Kelas Asset Name dan Category

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-404: Setup Column ceklis dan unceklis kelas Asset Name (text link)
1. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
2. Uncheck kolom `Asset Name`
3. Verifikasi kolom `Asset Name` hilang dari Live Preview dan dari tabel di balik modal
4. Check kembali kolom `Asset Name`
5. Verifikasi kolom `Asset Name` muncul kembali di Live Preview dan di tabel di balik modal
6. Uncheck kolom `Asset Name`, lalu klik `[Save]`
7. Verifikasi kolom `Asset Name` tersembunyi di tabel
8. Tekan F5
9. Verifikasi kolom `Asset Name` tetap tersembunyi setelah F5
10. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-405: Setup Column geser urutan kelas Asset Name (text link)
11. Buka Popup Setup Column
12. Drag kolom `Asset Name` satu posisi ke atas
13. Verifikasi urutan kolom `Asset Name` berubah di Live Preview dan di tabel
14. Klik `[Save]`
15. Tekan F5
16. Verifikasi urutan baru kolom `Asset Name` tetap setelah Save dan F5
17. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-410: Setup Column ceklis dan unceklis kelas Category (badge)
18. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
19. Uncheck kolom `Category`
20. Verifikasi kolom `Category` hilang dari Live Preview dan dari tabel di balik modal
21. Check kembali kolom `Category`
22. Verifikasi kolom `Category` muncul kembali di Live Preview dan di tabel di balik modal
23. Uncheck kolom `Category`, lalu klik `[Save]`
24. Verifikasi kolom `Category` tersembunyi di tabel
25. Tekan F5
26. Verifikasi kolom `Category` tetap tersembunyi setelah F5
27. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-411: Setup Column geser urutan kelas Category (badge)
28. Buka Popup Setup Column
29. Drag kolom `Category` satu posisi ke atas
30. Verifikasi urutan kolom `Category` berubah di Live Preview dan di tabel
31. Klik `[Save]`
32. Tekan F5
33. Verifikasi urutan baru kolom `Category` tetap setelah Save dan F5
34. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Popup Setup Column dan pemulihan konfigurasi kolom (hapus preferensi kolom di browser lalu F5) di akhir blok supaya blok berikutnya mulai dari konfigurasi bawaan (S-09).
- Persistensi "tersimpan di `localStorage`" diamati lewat F5 (tersembunyi atau urutan tetap), bukan lewat pembacaan penyimpanan browser.
- Pada TC-FA-FAAM-404 dan TC-FA-FAAM-405 kolom `Asset Name` diuji dengan Hide pada Popup Setup Column; kolom dipertahankan oleh aturan satu kolom tersisa (TC-FA-FAAM-427).
- Temuan untuk QA: TC-FA-FAAM-405 meminta kolom `Asset Name` digeser satu posisi ke atas; bila `Asset Name` sudah berada di urutan pertama kolom data, geser ke atas tidak mengubah urutan. TC tidak menyebut urutan awal kolom.
