---
id: TC-FA-GRP-E2E-213-tab-assets-search-per-kolom-brand-model-type-dan-category
title: "Tab Assets Search per Kolom Brand, Model/Type, dan Category"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1067
  - TC-FA-GRP-1068
  - TC-FA-GRP-1157
coverage:
  web: automated
---

# Tab Assets Search per Kolom Brand, Model/Type, dan Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Tabel "Kolom uji" (parameter langkah 4 sampai 14; keyword adalah potongan nilai kolom dari data Warehouse A dengan variasi Brand, Model/Type, dan Category):

| Kolom | Keyword huruf kecil | Keyword huruf KAPITAL | Keyword tanpa match |
|---|---|---|---|
| Brand | Fixture.settingsGroups.searchBrandKecil | Fixture.settingsGroups.searchBrandKapital | Fixture.settingsGroups.searchTanpaMatch |
| Model/Type | Fixture.settingsGroups.searchModelKecil | Fixture.settingsGroups.searchModelKapital | Fixture.settingsGroups.searchTanpaMatch |
| Category | Fixture.settingsGroups.searchCategoryKecil | Fixture.settingsGroups.searchCategoryKapital | Fixture.settingsGroups.searchTanpaMatch |

- Kolom curated Category tersembunyi secara default; langkah 2 menampilkannya lewat Setup Column sebagai precondition TC-1157 (dipakai sebagai precondition, tidak diasersi). Preferensi kolom yang tersimpan dihapus di hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).

## Test Steps

### TC-FA-GRP-1067, 1068, 1157: Search per kolom Brand, Model/Type, dan Category

1. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
2. Tampilkan kolom Category lewat Setup Column, klik [Save]
3. Untuk setiap baris tabel "Kolom uji" (langkah 4 sampai 14)
4. Pastikan kolom pada baris tabel tampil
5. Ketik Search keyword huruf kecil baris tabel, tekan Enter
6. Verifikasi sedikitnya satu baris tampil
7. Verifikasi setiap baris yang tampil memiliki nilai kolom yang mengandung substring keyword
8. Verifikasi baris pembanding yang nilai kolomnya tidak mengandung substring (`Fixture.settingsGroups.searchBarisPembanding`) tidak tampil
9. Ganti isi kotak search dengan keyword huruf KAPITAL baris tabel, tekan Enter
10. Verifikasi sedikitnya satu baris tampil
11. Verifikasi himpunan baris yang tampil identik dengan hasil keyword huruf kecil pada langkah 6
12. Ganti isi kotak search dengan keyword tanpa match baris tabel, tekan Enter
13. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
14. Klik `(←)` pada kotak Search

## Notes

- Iterasi: langkah 4 sampai 14 diulang untuk 3 baris tabel "Kolom uji" (Brand, Model/Type, Category); parameter tiap iterasi ada di tabel Prerequisites (8b butir 7). Ekspansi 3 + 3 x 11 = 36 langkah; alasan di atas sekitar 35: satu kelas harness dan satu dataset, ketiga kolom memakai langkah identik sehingga ekspansi berasal dari iterasi per kolom.
- Langkah penghubung (S-03): langkah 1 membuka Popup Detail Group Tab Assets; langkah 2 menampilkan kolom Category sebagai precondition TC-1157; langkah 14 (klik `(←)`) mereset Search sebelum iterasi berikutnya (S-09). Langkah "Pastikan kolom tampil" adalah aksi tanpa asersi dari langkah TC-1067 dan TC-1068 dan diterapkan sama pada Category.
- Temuan untuk QA:
  - TC-1067, 1068, 1157: Tabel Data Uji dengan nilai konkret tidak ada; keyword memakai fixture yang disediakan tim FE/BE.
  - TC-1157: kolom Category tersembunyi default; precondition d tidak menyebut cara menampilkannya sehingga spec memakai Setup Column.
