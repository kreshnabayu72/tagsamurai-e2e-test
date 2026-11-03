---
id: TC-FA-CAT-E2E-204-isi-berkas-xlsx-download-tabel-assets-kolom-baru
title: "Isi Berkas XLSX Download Tabel Assets: Transformasi Data Kolom Baru dan Kolom Hidden Tidak Ikut"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-668
coverage:
  web: automated
---

# Isi Berkas XLSX Download Tabel Assets: Transformasi Data Kolom Baru dan Kolom Hidden Tidak Ikut

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): tag aktif `Laptop Dell - 1` RFID dan QR, `Laptop Dell - 2` NFC, `Laptop Dell - 3` tanpa tag; UoM `Laptop Dell` Symbol `pcs` dan `Laptop HP` Symbol `set`; Policy Transaksi `Laptop Dell` Borrow On dan Assign On, `Laptop HP` hanya Transfer On; Last Scanned `Laptop Dell - 1` 2026-10-10 14:30 dan `Laptop Dell - 2` 2026-09-01 09:00; Asset Value (Commercial) `Laptop Dell - 1` 15000000.00, `Laptop Dell - 2` 0; Warranty Expiry `Laptop Dell - 1` 2027-03-15.
- Data Pre-setup #56 (Custom Field, lisensi FA-7 aktif): Purchasing `Nilai Kontrak` (Number; `Laptop Dell - 1` 5000, `Laptop Dell - 2` 0, `Laptop HP - 1` 250); General `Warna Casing` (Text, Scope Specific Asset Name `Laptop Dell`; `Laptop Dell - 1` `Silver`) dan Accounting `Kode Anggaran` (Text; `Laptop Dell - 1` `ANG-01`) dipakai sebagai precondition TC (kolom dicentang), tidak diasersi. Disediakan tim FE.
- Kemampuan teknis: membaca isi berkas unduhan XLSX (nama kolom, tipe dan nilai sel); disediakan tim FE/BE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Spec dimulai dari kolom bawaan; kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai di hook `before` dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-668: Download transformasi data kolom baru dan kolom Hidden tidak ikut

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Buka Setup Column lewat header kolom Actions (⋯), centang `Measurement`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Warranty Expiry`, `Warna Casing`, `Nilai Kontrak`, dan `Kode Anggaran`, lalu klik `[Save]`
4. Klik Download > `Download as XLSX`
5. Verifikasi berkas `Category-Assets.xlsx` terunduh
6. Buka berkas `Category-Assets.xlsx`
7. Verifikasi kolom TAG ditulis label tipe tag dipisah koma+spasi tanpa Tag Code (`RFID, QR` untuk `Laptop Dell - 1`, `NFC` untuk `Laptop Dell - 2`)
8. Verifikasi kolom TAG `Laptop Dell - 3` ditulis `-`
9. Verifikasi kolom Measurement ditulis Symbol (`pcs`, `set`)
10. Verifikasi Transactional Policy ditulis label transaksi yang On dipisah koma+spasi (`Borrow, Assign` untuk `Laptop Dell`, `Transfer` untuk `Laptop HP`)
11. Verifikasi Asset Value ditulis nilai numerik asli tanpa simbol dan pemisah ribuan sebagai sel angka di XLSX (`15000000`; nol ditulis `0`)
12. Verifikasi sel Asset Value tanpa nilai ditulis `-` (bukan `—`)
13. Verifikasi Last Scanned dan Warranty Expiry mengikuti Date Format dan Time Format General Settings
14. Verifikasi Custom Field ditulis sesuai Data Type (`Nilai Kontrak` numerik)
15. Verifikasi kolom `Category` tidak ada di berkas
16. Buka Setup Column, hilangkan centang `Measurement`, lalu klik `[Save]`
17. Klik Download > `Download as XLSX`
18. Buka berkas `Category-Assets.xlsx`
19. Verifikasi kolom `Measurement` yang disembunyikan tidak ikut ter-export pada unduhan kedua

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka Popup Detail).
- Spec ini tergolong kelas f (prinsip 13 bagian 3): objek ujinya isi berkas XLSX (tipe dan nilai sel).
- Post Condition TC-FA-CAT-668 (konfigurasi kolom dikembalikan lewat `[Reset to Default]` lalu `[Save]`) tidak punya langkah observasi di TC dan tidak diasersi; pemulihan dilakukan hook `after` dengan menghapus preferensi kolom di browser (S-09).
- Temuan untuk QA:
  - TC-FA-CAT-668 menyebut kolom `Asset Value` tetapi TC-FA-CAT-698 menetapkan dua kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)`; spec memakai `Asset Value (Commercial)` karena nilai Pre-setup #55 adalah buku Commercial.
  - TC-FA-CAT-668 Expected b menyebut Transactional Policy ditulis `-` bila semua Off, tetapi tidak ada aset `Laptop` dengan semua policy Off pada Pre-setup #55 (hanya `Office Chair` di `Furniture`); klausa itu tidak diasersi.
  - TC-FA-CAT-668 menyebut format kolom Last Scanned dan Warranty Expiry mengikuti General Settings tanpa nilai sampel; spec hanya mengasersi format.
  - Nama env var `FA_FS_PASSWORD` untuk akun Full Sensitive adalah usulan (TC tidak menyebut nama env var); perlu konfirmasi tim.
