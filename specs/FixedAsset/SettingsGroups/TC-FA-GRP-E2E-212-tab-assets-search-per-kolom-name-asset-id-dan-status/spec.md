---
id: TC-FA-GRP-E2E-212-tab-assets-search-per-kolom-name-asset-id-dan-status
title: "Tab Assets Search per Kolom Name, Asset ID, dan Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-678
  - TC-FA-GRP-679
  - TC-FA-GRP-680
coverage:
  web: automated
---

# Tab Assets Search per Kolom Name, Asset ID, dan Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Tabel "Kolom uji" (parameter langkah 3 sampai 13; setiap keyword adalah potongan nilai kolom yang bersangkutan dari data Warehouse A; keyword Name memuat potongan bagian Increment):

| Kolom | Keyword huruf kecil | Keyword huruf KAPITAL | Keyword tanpa match |
|---|---|---|---|
| Name | Fixture.settingsGroups.searchNameKecil | Fixture.settingsGroups.searchNameKapital | Fixture.settingsGroups.searchTanpaMatch |
| Asset ID | Fixture.settingsGroups.searchAssetIdKecil | Fixture.settingsGroups.searchAssetIdKapital | Fixture.settingsGroups.searchTanpaMatch |
| Status | Fixture.settingsGroups.searchStatusKecil | Fixture.settingsGroups.searchStatusKapital | Fixture.settingsGroups.searchTanpaMatch |

## Test Steps

### TC-FA-GRP-678, 679, 680: Search per kolom Name, Asset ID, dan Status

1. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
2. Untuk setiap baris tabel "Kolom uji" (langkah 3 sampai 13)
3. Pastikan kolom pada baris tabel tampil
4. Ketik Search keyword huruf kecil baris tabel, tekan Enter
5. Verifikasi sedikitnya satu baris tampil
6. Verifikasi setiap baris yang tampil memiliki nilai kolom yang mengandung substring keyword
7. Verifikasi baris pembanding yang nilai kolomnya tidak mengandung substring (`Fixture.settingsGroups.searchBarisPembanding`) tidak tampil
8. Ganti isi kotak search dengan keyword huruf KAPITAL baris tabel, tekan Enter
9. Verifikasi sedikitnya satu baris tampil
10. Verifikasi himpunan baris yang tampil identik dengan hasil keyword huruf kecil pada langkah 5
11. Ganti isi kotak search dengan keyword tanpa match baris tabel, tekan Enter
12. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
13. Klik `(←)` pada kotak Search

## Notes

- Iterasi: langkah 3 sampai 13 diulang untuk 3 baris tabel "Kolom uji" (Name, Asset ID, Status); parameter tiap iterasi ada di tabel Prerequisites dan `Verifikasi` tetap satu per klausa (8b butir 7).
- Langkah penghubung (S-03): langkah 1 membuka Popup Detail Group Tab Assets; langkah 13 (klik `(←)`) mereset Search dan tabel sebelum iterasi berikutnya (S-09).
- Spec berisi satu kelas harness (fungsional) dan satu dataset Warehouse A; ekspansi iterasi 2 + 3 x 11 = 35 langkah, tidak melewati ambang.
- Temuan untuk QA:
  - TC-678, 679, 680: Tabel Data Uji dengan nilai konkret tidak ada; nilai keyword memakai fixture yang disediakan tim FE/BE.
  - TC-678 a: "potongan bagian Increment ikut dicocokkan" tidak menyebut nilai; keyword Name memuat potongan Increment dan hasil diasersi lewat nilai kolom Name teks lengkap.
