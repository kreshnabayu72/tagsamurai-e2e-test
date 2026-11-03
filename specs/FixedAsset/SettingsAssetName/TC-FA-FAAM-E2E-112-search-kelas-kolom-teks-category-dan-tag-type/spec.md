---
id: TC-FA-FAAM-E2E-112-search-kelas-kolom-teks-category-dan-tag-type
title: "Search: Kelas Kolom Asset Name, Code, UoM, Category, dan TAG Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-343
  - TC-FA-FAAM-344
  - TC-FA-FAAM-345
coverage:
  web: automated
---

# Search: Kelas Kolom Asset Name, Code, UoM, Category, dan TAG Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10), `Ergonomic Chair` (Pre-setup #11), `Warehouse Pallet` (Pre-setup #13), `Service Vehicle` (Pre-setup #14).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-343: Search kelas kolom Asset Name, Code, UoM
1. Ketik Search `LATITUDE`, tekan Enter
2. Verifikasi keyword `LATITUDE` pada kolom Asset Name menampilkan baris `Dell Latitude`
3. Ganti isi kotak search dengan `dlat`, tekan Enter
4. Verifikasi keyword `dlat` pada kolom Code menampilkan baris `Dell Latitude`
5. Ganti isi kotak search dengan `pcs`, tekan Enter
6. Verifikasi keyword `pcs` pada kolom UoM menampilkan baris dengan UoM `Pcs` (`Ergonomic Chair`)
### TC-FA-FAAM-344: Search kelas kolom Category
7. Ganti isi kotak search dengan `equip`, tekan Enter
8. Verifikasi keyword `equip` menampilkan baris dengan Category memuat `Equip`, termasuk `Dell Latitude` (`IT Equipment`)
9. Verifikasi baris `Ergonomic Chair` (`Office Furniture`) dan `Warehouse Pallet` (`Logistics`) tidak tampil
### TC-FA-FAAM-345: Search kelas kolom TAG Type
10. Ganti isi kotak search dengan `rfid`, tekan Enter
11. Verifikasi keyword `rfid` menampilkan baris ber-icon RFID (`Dell Latitude`, `Service Vehicle`)
12. Ganti isi kotak search dengan `non-tag`, tekan Enter
13. Verifikasi keyword `non-tag` menampilkan baris `Warehouse Pallet`
14. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): klik `(←)` terakhir yang menutup Search dan mereset tabel.
- Asersi absence pada TC-FA-FAAM-344 beranchor Verifikasi baris `Dell Latitude` tampil pada Search yang sama (bagian 8b butir 2).
