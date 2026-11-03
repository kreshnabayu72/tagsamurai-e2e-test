---
id: TC-FA-LBL-E2E-077-search-modal-changelog-bagian-1-2
title: "Search Modal Changelog (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-290
  - TC-FA-LBL-291
  - TC-FA-LBL-292
  - TC-FA-LBL-293
  - TC-FA-LBL-294
coverage:
  web: automated
---

# Search Modal Changelog (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): log Changelog Labels memuat tujuh baris seed (Date 08 sampai 15 Sep 2026): Create `High Priority` (15 Sep 2026 14:20, Sarah J), Edit `High Priority` Color `#DC2626` ke `#EF4444` (15 Sep 2026 14:25, Sarah J), Create `Finance Department` (14 Sep 2026 11:15, David K), Edit `Finance Department` Label Name `Finance Dept` ke `Finance Department` (14 Sep 2026 11:30, David K), Create `Audit Ready` (12 Sep 2026 09:40, Sarah J), Create `Executive Asset` (10 Sep 2026 16:30, Michael W), Delete `Old Tag` (08 Sep 2026 13:00, David K). Entri TC lain (mis. Delete bertanggal hari run dari TC-FA-LBL-325) menambah entri permanen bertanggal hari run sehingga ketujuh baris seed dapat bergeser ke luar halaman pertama (pagination default 10 per halaman). Karena itu spec menerapkan Filter Date `08 Sep 2026` sampai `15 Sep 2026` (rentang inklusif) di Filter Panel Modal Changelog sebelum mengamati baris seed, dan asersi dinilai atas hasil filter itu: tepat tujuh baris seed (entri TC lain berada di luar rentang) (S-12, S-14).
- State global yang diubah: tidak ada. Tidak ada data dinamis; spec tidak membuat atau mengubah data backend. State Search dibersihkan di akhir spec.

## Test Steps

### Membuka Modal Changelog

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di toolbar modal
3. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`

### TC-FA-LBL-290: Search Changelog kelas Action, Label Name, Field: substring

4. Klik icon Search di toolbar modal
5. Verifikasi placeholder kotak Search `Search label name, action...`
6. Ketik Search `Color`, tekan Enter
7. Verifikasi pada hasil Filter Date, tabel memuat hanya satu baris: `Edit High Priority`
8. Ganti isi kotak search dengan `Finance`, tekan Enter
9. Verifikasi pada hasil Filter Date, tabel memuat dua baris seed `Finance Department`
10. Ganti isi kotak search dengan `Delet`, tekan Enter
11. Verifikasi pada hasil Filter Date, tabel memuat hanya satu baris: `Delete Old Tag`

### TC-FA-LBL-291: Search Changelog kelas Action, Label Name, Field: tidak membedakan huruf besar-kecil

12. Ganti isi kotak search dengan `COLOR`, tekan Enter
13. Verifikasi pada hasil Filter Date, tabel memuat `Edit High Priority`
14. Ganti isi kotak search dengan `finance`, tekan Enter
15. Verifikasi pada hasil Filter Date, tabel memuat dua baris seed `Finance Department`
16. Ganti isi kotak search dengan `EDIT`, tekan Enter
17. Verifikasi pada hasil Filter Date, tabel memuat dua baris seed Edit: `High Priority` dan `Finance Department`

### TC-FA-LBL-292: Search Changelog: kata kunci tidak ditemukan

18. Ganti isi kotak search dengan `zzzz`, tekan Enter
19. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-FA-LBL-293: Search Changelog kelas Old Value dan New Value

20. Ganti isi kotak search dengan `Finance Dept`, tekan Enter
21. Verifikasi pada hasil Filter Date, tabel memuat hanya satu baris: `Edit Finance Department` (cocok pada Old Value)
22. Ganti isi kotak search dengan `#EF4444`, tekan Enter
23. Verifikasi pada hasil Filter Date, tabel memuat hanya satu baris: `Edit High Priority` (cocok pada New Value)

### TC-FA-LBL-294: Search Changelog kolom Modified By

24. Ganti isi kotak search dengan `david`, tekan Enter
25. Verifikasi pada hasil Filter Date, tabel memuat tiga baris seed `David K`: `Edit Finance Department`, `Create Finance Department`, `Delete Old Tag`
26. Klik `(←)` pada kotak Search
27. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal dibuka sekali di awal dan dipakai kelima TC; Filter Date rentang seed di-Apply sekali di awal (langkah 2 dan 3, sama dengan langkah Filter tiap TC) dan tetap berlaku untuk kelima TC; tiap TC berikutnya mengganti isi kotak search sehingga state Search TC sebelumnya tidak terbawa.
- Langkah penghubung (tanpa awalan `Verifikasi`): `(←)` pada kotak Search (menutup input dan mereset tabel) dan menutup Modal Changelog di akhir spec.
- Search hanya menyaring saat Enter (bagian 8b butir 9). Asersi "hanya" dinilai atas hasil Filter Date (tujuh baris seed) sesuai Expected TC; entri TC lain di Company Changelog berada di luar rentang sehingga baris yang tampil menjadi pembanding sekaligus.
- Pasangan TC pencarian bagian 2 (TC-FA-LBL-295, TC-FA-LBL-492, TC-FA-LBL-508) ada di spec 078.
- Temuan untuk QA:
  - TC-FA-LBL-294 menyebut keyword `david` cocok dengan `David K`; TC tidak menyebut nama lengkap David K, sehingga tidak jelas apakah pencocokan memakai nama lengkap (lihat TC-FA-LBL-508).
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
