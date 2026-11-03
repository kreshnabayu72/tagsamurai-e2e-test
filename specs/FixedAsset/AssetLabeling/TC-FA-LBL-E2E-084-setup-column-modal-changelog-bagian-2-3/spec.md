---
id: TC-FA-LBL-E2E-084-setup-column-modal-changelog-bagian-2-3
title: "Setup Column Modal Changelog (bagian 2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-315
  - TC-FA-LBL-316
coverage:
  web: automated
---

# Setup Column Modal Changelog (bagian 2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): tujuh kolom Modal Changelog pada konfigurasi default.
- State global yang diubah: konfigurasi kolom Setup Column Modal Changelog (urutan dan pin, disimpan lewat `[Save]`). Dipulihkan dengan `[Reset to Default]` lalu `[Save]` di antara TC dan oleh hook `after` suite (hapus preferensi kolom di browser; kemampuan disediakan tim FE). Spec tidak membuat atau mengubah data backend.
- Kemampuan teknis: muat ulang halaman dengan F5; scroll horizontal tabel modal; drag and drop pada daftar Setup Column.

## Test Steps

### TC-FA-LBL-315: Setup Column Changelog: drag reorder

1. Klik icon Changelog di Table Tools
2. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`
3. Seret `Action` ke posisi paling atas daftar
4. Verifikasi urutan Live Preview: `Action`, `Date`, `Label Name`, `Field`, `Old Value`, `New Value`, `Modified By`
5. Seret `Label Name` ke posisi paling atas daftar
6. Verifikasi urutan Live Preview: `Label Name`, `Action`, `Date`, `Field`, `Old Value`, `New Value`, `Modified By`
7. Seret `Field` ke posisi paling atas daftar
8. Verifikasi urutan Live Preview: `Field`, `Label Name`, `Action`, `Date`, `Old Value`, `New Value`, `Modified By`
9. Seret `Old Value` ke posisi paling atas daftar
10. Verifikasi urutan Live Preview: `Old Value`, `Field`, `Label Name`, `Action`, `Date`, `New Value`, `Modified By`
11. Seret `New Value` ke posisi paling atas daftar
12. Verifikasi urutan Live Preview: `New Value`, `Old Value`, `Field`, `Label Name`, `Action`, `Date`, `Modified By`
13. Seret `Modified By` ke posisi paling atas daftar
14. Verifikasi urutan Live Preview: `Modified By`, `New Value`, `Old Value`, `Field`, `Label Name`, `Action`, `Date`
15. Seret `Date` ke posisi paling atas daftar
16. Verifikasi urutan Live Preview: `Date`, `Modified By`, `New Value`, `Old Value`, `Field`, `Label Name`, `Action`
17. Klik `[Save]`, tekan F5, lalu klik icon Changelog di Table Tools
18. Verifikasi urutan header tabel sama dengan urutan Live Preview terakhir (`Date`, `Modified By`, `New Value`, `Old Value`, `Field`, `Label Name`, `Action`) dan bertahan setelah reload
19. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-FA-LBL-316: Setup Column Changelog: pin dan batas pin ketiga

20. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`
21. Klik icon Pin `Date`, `Action`, dan `Label Name` satu per satu, lalu hover icon Pin `Field`
22. Verifikasi icon Pin `Field` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
23. Klik `[Save]` lalu scroll tabel horizontal
24. Verifikasi `Date`, `Action`, dan `Label Name` membeku di kiri saat scroll
25. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`, lepas pin ketiga kolom itu satu per satu, lalu klik icon Pin `Field`, `Old Value`, dan `New Value` satu per satu
26. Klik `[Save]` lalu scroll tabel horizontal
27. Verifikasi `Field`, `Old Value`, dan `New Value` membeku
28. Verifikasi `Date`, `Action`, dan `Label Name` ikut bergeser saat scroll
29. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`, lepas pin ketiga kolom itu, lalu klik icon Pin `Modified By`
30. Klik `[Save]` lalu scroll tabel horizontal
31. Verifikasi hanya `Modified By` yang membeku
32. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`, lepas pin `Modified By`, klik `[Reset to Default]`, lalu klik `[Save]`
33. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan `Verifikasi`): `[Reset to Default]` lalu `[Save]` sesudah TC-FA-LBL-315 supaya TC-FA-LBL-316 dimulai dari urutan default; pelepasan pin dan `[Reset to Default]` pada akhir TC-FA-LBL-316; menutup Modal Changelog di akhir spec. `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (bagian 8b butir 8).
- TC-FA-LBL-312 dan TC-FA-LBL-313 ada di spec 083, TC-FA-LBL-314 ada di spec 167, TC-FA-LBL-317 dan TC-FA-LBL-318 ada di spec 085.
- Temuan untuk QA:
  - TC-FA-LBL-316 butir c mengasersi `Date`, `Action`, dan `Label Name` "ikut bergeser" saat scroll tanpa menyebut posisi awal; spec mengasersi hanya yang tertulis.
  - TC-FA-LBL-315 butir h menyebut urutan header sama dengan butir g dan bertahan setelah reload; spec menutup dan membuka modal lagi setelah F5 sebagai bagian langkah TC.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
