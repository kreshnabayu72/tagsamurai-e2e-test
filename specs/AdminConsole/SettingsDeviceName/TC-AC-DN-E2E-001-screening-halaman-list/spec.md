---
id: TC-AC-DN-E2E-001-screening-halaman-list
title: "Screening Halaman Device Name List: Header, Body, Footer, Selector, Breadcrumb, Sub-tab, Row Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-1
  - TC-AC-DN-2
  - TC-AC-DN-3
  - TC-AC-DN-4
  - TC-AC-DN-8
coverage:
  web: automated
---

# Screening Halaman Device Name List: Header, Body, Footer, Selector, Breadcrumb, Sub-tab, Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Device Name inti (#16, baris pertama `Barcode Station`, baris `Barcode Station` memiliki row action), dan seed 120 Device Name (#17). Seluruhnya baca-saja; tidak ada data Dinamis.

## Test Steps

### TC-AC-DN-1: Screening halaman Device Name List: Header, Body, dan Footer

1. Verifikasi Breadcrumb `Settings > Device > Device Name`
2. Verifikasi tidak ada Page Title terpisah di bawah Breadcrumb
3. Verifikasi sub-tab `Device Name (aktif) | Device SKU`
4. Verifikasi Table Tools `Search | Filter | Download | Changelog | [+ Device Name]`
5. Verifikasi kolom tabel `Checkbox (unsortable) | Device Name (sortable) | Category (sortable) | Brand (sortable) | Model/Type (sortable) | Measurement (sortable) | Last Modified (sortable) | Column Visibility (⋯) (unsortable — header klik = buka overlay Column Visibility, body per baris = row action menu)`
6. Verifikasi Category Sidebar tampil terbuka di sisi kanan halaman, sejajar dengan tabel, lengkap dengan Floating toggle di tepi kiri panel
7. Verifikasi baris pertama pada halaman 1: Barcode Station
8. Verifikasi Pagination: selector jumlah data per halaman bernilai 10, navigasi halaman, dan input nomor halaman

### TC-AC-DN-2: Selector jumlah data per halaman menampilkan opsi 10, 25, 50, dan 100

9. Klik selector jumlah data per halaman di Footer
10. Verifikasi Overlay Page Size memuat opsi `10 | 25 | 50 | 100` dan nilai terpilih saat ini 10
11. Verifikasi tidak ada opsi "All" pada Overlay Page Size
12. Tekan Esc untuk menutup Overlay Page Size

### TC-AC-DN-3: Breadcrumb: segmen pertama dan terakhir bukan tautan, segmen tengah dapat diklik

13. Verifikasi Breadcrumb tampil `Settings > Device > Device Name`
14. Hover segmen `Settings`
15. Klik segmen `Settings`
16. Verifikasi segmen `Settings` (pertama) berupa label statis; klik tidak memindahkan halaman dan halaman tetap `Settings > Device > Device Name`
17. Hover segmen `Device Name`
18. Klik segmen `Device Name`
19. Verifikasi segmen `Device Name` (terakhir) berupa label statis; klik tidak memindahkan halaman dan halaman tetap `Settings > Device > Device Name`
20. Hover segmen `Device`
21. Verifikasi segmen `Device` (tengah) tampil sebagai elemen yang dapat diklik (kursor menunjukkan elemen dapat diklik)

### TC-AC-DN-4: Pindah sub-tab dari Device Name ke Device SKU lalu kembali ke Device Name

22. Klik sub-tab `Device SKU`
23. Verifikasi sub-tab `Device Name | Device SKU (aktif)`
24. Verifikasi Breadcrumb tetap mengawali `Settings > Device`
25. Klik sub-tab `Device Name`
26. Verifikasi sub-tab `Device Name (aktif) | Device SKU`
27. Verifikasi List Device Name tampil dengan Table Tools `Search | Filter | Download | Changelog | [+ Device Name]`

### TC-AC-DN-8: Screening overlay row action: Detail, Edit, Delete beserta ikon dan severity

28. Klik ikon `⋯` pada baris `Barcode Station`
29. Verifikasi Overlay Row Action memuat opsi berurutan `Detail | Edit | Delete`
30. Verifikasi ikon `Detail` = FileInfoLine, ikon `Edit` = Edit2Line, ikon `Delete` = DeleteBin6Line
31. Verifikasi `Detail` dan `Edit` berseverity dark
32. Verifikasi `Delete` berseverity danger (merah) dan berada paling bawah
33. Tekan Esc untuk menutup Overlay Row Action

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Semua TC dalam spec ini tanpa aksi tulis.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC mengikuti screening di awal (TC-AC-DN-1), lalu selector, Breadcrumb, sub-tab, dan row action di akhir; tiap TC mengamati halaman yang sama tanpa membuka ulang halaman.
- Langkah penghubung (S-03): langkah 12 dan 33 menutup overlay agar TC berikutnya mulai dari halaman bersih.
- TC-AC-DN-3: langkah hover `Device` diasersi sebagai kursor yang menunjukkan elemen dapat diklik; klik segmen `Device` tidak dilakukan karena TC tidak memintanya.
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
