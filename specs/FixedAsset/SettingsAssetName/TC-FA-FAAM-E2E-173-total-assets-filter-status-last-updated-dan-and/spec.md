---
id: TC-FA-FAAM-E2E-173-total-assets-filter-status-last-updated-dan-and
title: "Tab Total Assets Filter: Status, Last Updated, AND Brand-Group, dan Filter Brand-Model Service Vehicle"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-514
  - TC-FA-FAAM-515
  - TC-FA-FAAM-516
  - TC-FA-FAAM-666
coverage:
  web: automated
---

# Tab Total Assets Filter: Status, Last Updated, AND Brand-Group, dan Filter Brand-Model Service Vehicle

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26).
- Data: `Service Vehicle` (Total Asset 8: `AST-1001` sampai `AST-1004` Brand `Isuzu` model `D-Max` Group `Head Office`, `AST-1005` sampai `AST-1008` Brand `Toyota` model `Hilux` Group `Warehouse`, Status `Active`; Pre-setup #14, #26c).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Kemampuan teknis: tanggal Last Updated sebuah aset `Dell Latitude` dibaca dari sel tabel sebelum Filter dipakai (TC-FA-FAAM-515).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-514: Filter Status multi-select dengan opsi nilai badge distinct

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik Filter, buka dropdown Status
3. Verifikasi opsi Status sama dengan nilai badge distinct yang tampil pada tabel
4. Pilih Status `Borrowed` dan `Missing`, klik `[Apply]`
5. Verifikasi sedikitnya satu baris tampil pada hasil
6. Verifikasi hasil OR dalam field: seluruh baris berstatus `Borrowed` atau `Missing`

### TC-FA-FAAM-515: Filter Last Updated date range inklusif

7. Klik `[Clear Field]` pada Filter Panel (membersihkan Status), klik `[Apply]`
8. Catat tanggal Last Updated sebuah aset sebagaimana tampil pada tabel
9. Klik Filter, pilih rentang satu hari pada tanggal yang dicatat, klik `[Apply]`
10. Verifikasi aset yang diperbarui pada hari itu tampil
11. Verifikasi hanya aset yang diperbarui pada hari itu tampil

### TC-FA-FAAM-666: Filter Brand dan Model/Type menyaring aset Service Vehicle

12. Tutup popup Detail, klik nama `Service Vehicle`, klik tab `Total Assets (8)`
13. Klik Filter, pilih Brand `Isuzu`, klik `[Apply]`
14. Verifikasi hanya 4 aset ber-Brand `Isuzu` (model `D-Max`) tampil
15. Klik Filter, klik `[Clear Field]`, pilih Model/Type `Hilux`, klik `[Apply]`
16. Verifikasi hanya 4 aset ber-model `Hilux` (Brand `Toyota`) tampil

### TC-FA-FAAM-516: Filter Brand dan Group bersamaan berlaku AND

17. Klik Filter, klik `[Clear Field]`, pilih Brand `Isuzu` dan Group `Warehouse`, klik `[Apply]`
18. Verifikasi Title `No results found`
19. Verifikasi Description `Try adjusting your search or filter.`
20. Klik Filter, ganti Group menjadi `Head Office`, klik `[Apply]`
21. Verifikasi hanya `AST-1001` sampai `AST-1004` tampil (4 baris)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 514, 515 (`Dell Latitude`), lalu 666 dan 516 (`Service Vehicle`; 666 sebelum 516 karena 516 membersihkan filter 666 lewat `[Clear Field]`).
- Langkah penghubung: `[Clear Field]` dan `[Apply]` untuk membersihkan filter antar blok TC (S-09), mencatat tanggal Last Updated, dan menutup popup Detail sebelum berpindah fixture.
- Asersi "hanya ... tampil" menyebut baris yang tampil (anchor positif pada surface yang sama); empty state `No results found` pada blok TC-FA-FAAM-516 adalah anchor positif atas hasil Filter.
- Temuan untuk QA:
  - TC-FA-FAAM-515: hari yang dipilih dan daftar aset yang diharapkan tidak disebut TC; spec membaca tanggal dari sel tabel.
  - TC-FA-FAAM-514 Expected b menyebut hasil OR tanpa daftar baris yang diharapkan.
