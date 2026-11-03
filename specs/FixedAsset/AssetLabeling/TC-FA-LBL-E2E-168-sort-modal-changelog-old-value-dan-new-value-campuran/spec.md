---
id: TC-FA-LBL-E2E-168-sort-modal-changelog-old-value-dan-new-value-campuran
title: "Sort Modal Changelog: Old Value dan New Value Campuran Angka dan Teks"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-519
coverage:
  web: automated
---

# Sort Modal Changelog: Old Value dan New Value Campuran Angka dan Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Sort Changelog (Pre-setup #36; email dari `Fixture.assetLabeling.akun.totalControlSortChangelog`, pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_SORTCHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Sort Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlSortChangelog` (belum ada; disediakan tim FE, S-12), dengan env `Spectra.env.FA_TC_SORTCHANGELOG_PASSWORD` (belum terdaftar di `suite.md`; disediakan tim FE).
- Data Pre-setup #36 (Company Sort Changelog, hanya dibaca): log seed tujuh entri (entri TC lain boleh ada; Date seed belum ditetapkan, NC-17): Create `10`, Create `9`, Create `beta`, Create `Alpha`, Create `2`, Edit Label Name `2` ke `Zeta`, Edit Label Name `beta` ke `Gamma`. Kolom Old Value dan New Value memiliki lebih dari dua nilai distinct (S-11).
- State global yang diubah: tidak ada. Tidak ada data dinamis; spec tidak membuat atau mengubah data backend.

## Test Steps

### TC-FA-LBL-519: Sort Changelog Old Value dan New Value campuran angka dan teks: angka lebih dulu, teks A-Z tanpa beda huruf, kosong di akhir

1. Klik icon Changelog di Table Tools
2. Klik header kolom `New Value` satu kali
3. Verifikasi di antara tujuh baris seed, New Value klik 1 (Ascending): `2`, `9`, `10` (urut nilai numerik), lalu `Alpha`, `beta`, `Gamma`, `Zeta` (alfabetis tanpa membedakan huruf besar-kecil)
4. Klik header kolom `New Value` untuk kedua kali
5. Verifikasi di antara tujuh baris seed, New Value klik 2 (Descending): kebalikan penuh: `Zeta`, `Gamma`, `beta`, `Alpha`, `10`, `9`, `2`
6. Klik header kolom `New Value` untuk ketiga kali
7. Verifikasi di antara tujuh baris seed, New Value klik 3 (Netral): kembali ke default Date Newest First
8. Klik header kolom `Old Value` satu kali
9. Verifikasi di antara tujuh baris seed, Old Value klik 1 (Ascending): `2`, `beta`, lalu lima baris `—` di akhir
10. Klik header kolom `Old Value` untuk kedua kali
11. Verifikasi di antara tujuh baris seed, Old Value klik 2 (Descending): lima baris `—` di awal, lalu `beta`, `2`
12. Klik header kolom `Old Value` untuk ketiga kali
13. Verifikasi di antara tujuh baris seed, Old Value klik 3 (Netral): kembali ke default Date Newest First
14. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Klik ketiga pada tiap kolom mengembalikan tabel ke default Date Newest First (S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup Modal Changelog di akhir spec.
- TC-FA-LBL-305 sampai TC-FA-LBL-309 ada di spec 081, TC-FA-LBL-310, TC-FA-LBL-311, dan TC-FA-LBL-325 ada di spec 082.
- Spec ini memakai Company Sort Changelog sebagai akun aktor sejak hook `before` sehingga tidak memerlukan langkah ganti akun di tengah spec.
- Temuan untuk QA:
  - TC-FA-LBL-519 tidak menyebut email Company Sort Changelog (hanya Pre-setup #36) dan tidak menyebut urutan antar lima baris `—` pada kolom Old Value; spec mengasersi hanya yang tertulis.
  - Tanggal ketujuh entri seed Pre-setup #36 belum ditetapkan (NC-17, menunggu konfirmasi tim FE/BE), sehingga spec tidak memakai Filter Date dan tidak dapat menjamin ketujuh baris seed berada di halaman teramati bila entri TC lain bertanggal hari run bertambah (S-14); spec mengikuti TC dan menilai urutan di antara tujuh baris seed, entri TC lain bila ada diabaikan.
  - Email akun Total Control Company Sort Changelog tidak tertulis lengkap di Pre-setup #36 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
