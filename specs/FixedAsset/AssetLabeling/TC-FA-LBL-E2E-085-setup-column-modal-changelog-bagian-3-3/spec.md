---
id: TC-FA-LBL-E2E-085-setup-column-modal-changelog-bagian-3-3
title: "Setup Column Modal Changelog (bagian 3/3)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-317
  - TC-FA-LBL-318
coverage:
  web: automated
---

# Setup Column Modal Changelog (bagian 3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): tujuh kolom Modal Changelog pada konfigurasi default.
- State global yang diubah: konfigurasi kolom Setup Column Modal Changelog (`[Save]` pada TC-FA-LBL-317 menyimpan konfigurasi default). Konfigurasi akhir adalah default; hook `after` suite menghapus preferensi kolom di browser (kemampuan disediakan tim FE). Spec tidak membuat atau mengubah data backend.

## Test Steps

### TC-FA-LBL-317: Setup Column Changelog: Reset to Default dan discard

1. Klik icon Changelog di Table Tools
2. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`
3. Sembunyikan `Field`
4. Klik `[Reset to Default]` lalu klik `[Save]`
5. Verifikasi ketujuh kolom default tampil di modal
6. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`
7. Sembunyikan `Action`
8. Klik `[✕]`
9. Verifikasi perubahan `Action` dibuang
10. Verifikasi ketujuh kolom tetap tampil

### TC-FA-LBL-318: Setup Column Changelog: guard satu kolom tersisa

11. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`
12. Hapus centang enam kolom sehingga hanya `Date` tersisa
13. Hover checkbox `Date`
14. Verifikasi checkbox `Date` disabled dengan tooltip `At least one column must remain visible.`
15. Klik `[✕]`
16. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan `Verifikasi`): `[✕]` pada popup Setup Column yang berisi perubahan yang tidak disimpan (membuang perubahan; popup Setup Column tidak memakai dialog `Unsaved Changes`), dan menutup Modal Changelog di akhir spec. Pemulihan state kolom TC-FA-LBL-318 dilakukan oleh `[✕]` tanpa `[Save]`.
- TC-FA-LBL-312 dan TC-FA-LBL-313 ada di spec 083, TC-FA-LBL-314 ada di spec 167, TC-FA-LBL-315 dan TC-FA-LBL-316 ada di spec 084.
- Temuan untuk QA:
  - TC-FA-LBL-317 tidak menyatakan apakah `[Save]` menutup popup Setup Column; asersi ketujuh kolom dibaca dari tabel modal sesudah `[Save]`.
  - TC-FA-LBL-318 tidak menyatakan keadaan popup sesudah `[✕]` dengan perubahan belum disimpan (dialog `Unsaved Changes` tidak disebut); spec mengikuti TC-FA-LBL-317 yang membuang perubahan tanpa dialog.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
