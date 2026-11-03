---
id: TC-FA-FAAM-E2E-140-download-isi-berkas-teks-category-tag-type
title: "Download List: Isi Berkas Kelas Teks, Category, TAG Type, Brand, dan Default Addon-Label"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-446
  - TC-FA-FAAM-447
  - TC-FA-FAAM-448
  - TC-FA-FAAM-449
  - TC-FA-FAAM-450
coverage:
  web: automated
---

# Download List: Isi Berkas Kelas Teks, Category, TAG Type, Brand, dan Default Addon-Label

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Code `DLAT`, UoM `Unit`), `Ergonomic Chair` (Pre-setup #11, Code `CHR-01`, UoM `Pcs`), `MacBook Pro` (Pre-setup #12, Code `MBP`, UoM `Unit`), `Warehouse Pallet` (Pre-setup #13, `Non-TAG`), `Service Vehicle` (Pre-setup #14), dan baris ber-Category `Laptop` (anak `Electronics`; nama baris tidak tertulis di Pre-setup).
- Kemampuan teknis: mengunduh berkas dari browser dan membaca isi berkas XLSX atau CSV (sel, encoding, nama sheet) lewat pembaca berkas; disediakan tim FE/BE.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### Unduh berkas
1. Klik icon Download lalu `Download as XLSX`
2. Buka berkas `Asset-Names.xlsx`
### TC-FA-FAAM-446: Download List kelas Asset Name, Code, UoM (teks)
3. Bandingkan baris `Dell Latitude`, `Ergonomic Chair`, dan `MacBook Pro` dengan List
4. Verifikasi kolom Asset Name berisi teks nama apa adanya: `Dell Latitude`, `Ergonomic Chair`, `MacBook Pro`
5. Verifikasi kolom Code berisi teks Code apa adanya: `DLAT`, `CHR-01`, `MBP`
6. Verifikasi kolom UoM berisi Unit Name, bukan Symbol: `Unit`, `Pcs`, `Unit`
### TC-FA-FAAM-447: Download List kelas Category (hierarki penuh)
7. Lihat baris ber-Category anak `Laptop`
8. Verifikasi sel Category berisi hierarki penuh dari root `Electronics > Laptop`
### TC-FA-FAAM-448: Download List kelas TAG Type (label ikon)
9. Lihat baris `Dell Latitude` dan `Warehouse Pallet`
10. Verifikasi sel TAG Type baris `Dell Latitude` berisi `RFID, QR` memakai accessibility label dipisah `, `
11. Verifikasi sel TAG Type baris `Warehouse Pallet` berisi `Non-TAG`
### TC-FA-FAAM-449: Download List kelas Brand dan Model/Type (nama penuh, banyak nilai)
12. Lihat baris `Service Vehicle` dan `Dell Latitude`
13. Verifikasi sel Brand baris `Service Vehicle` berisi `Isuzu, Toyota` (nama penuh, dipisah `, `)
14. Verifikasi sel Model/Type baris `Dell Latitude` berisi seluruh model penuh `3310, 5420, 7420` dipisah `, `
15. Verifikasi sel Model/Type baris `Dell Latitude` tanpa `+N more`
16. Verifikasi sel Model/Type baris `Dell Latitude` tanpa hierarki
### TC-FA-FAAM-450: Download List kelas Default Addon dan Default Label (label badge)
17. Lihat baris `Dell Latitude`
18. Verifikasi sel Default Addon berisi `Audit, Maintenance` berupa teks label tanpa warna
19. Verifikasi sel Default Label berisi `Finance, High Priority` berupa teks label tanpa warna

## Notes

- Satu berkas XLSX diunduh sekali dan dipakai oleh kelima blok karena TC-FA-FAAM-446 sampai 450 memakai aksi unduh yang sama pada tabel tanpa Search dan Filter; isi berkas identik di antara blok.
- Langkah "Bandingkan" dan "Lihat baris" adalah langkah penghubung (aksi tanpa `Verifikasi`) yang mengarahkan pembacaan sel.
- Spec ini hanya mengasersi isi sel berkas (kelas f); nama berkas, daftar kolom, dan jumlah baris diasersi di spec 142.
- Temuan untuk QA: Expected TC-FA-FAAM-448 menulis sel TAG Type `Dell Latitude` sebagai `RFID, QR`, sedangkan kunci sort TC-FA-FAAM-391 menulis `QR, RFID` untuk baris yang sama; urutan label dalam satu sel tidak konsisten antar TC. TC-FA-FAAM-447 menyebut baris `Laptop` tanpa nama Asset Name.
