---
id: TC-FA-LBL-E2E-083-setup-column-modal-changelog-bagian-1-3
title: "Setup Column Modal Changelog (bagian 1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-312
  - TC-FA-LBL-313
coverage:
  web: automated
---

# Setup Column Modal Changelog (bagian 1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): tujuh kolom Modal Changelog (`Date`, `Action`, `Label Name`, `Field`, `Old Value`, `New Value`, `Modified By`) pada konfigurasi default.
- State global yang diubah: tidak ada (spec ini tidak menekan `[Save]`). Konfigurasi kolom Setup Column yang tersimpan spec lain dihapus oleh hook `after` suite (preferensi kolom di browser; kemampuan disediakan tim FE). Spec tidak membuat atau mengubah data backend.

## Test Steps

### Membuka Modal Changelog

1. Klik icon Changelog di Table Tools

### TC-FA-LBL-312: Screening overlay Column Visibility Changelog

2. Klik header kolom Actions (⋯) di modal
3. Verifikasi overlay memuat tujuh kolom `Date`, `Action`, `Label Name`, `Field`, `Old Value`, `New Value`, `Modified By` tercentang (Hideable)
4. Verifikasi overlay memuat drag handle
5. Verifikasi overlay memuat item `Setup Column...`

### TC-FA-LBL-313: Screening Popup Setup Column Changelog (3 zona)

6. Klik `Setup Column...`
7. Verifikasi Zona Header memuat Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan `[✕]`
8. Verifikasi Zona Body memuat tujuh kolom tercentang
9. Verifikasi Zona Body memuat drag handle pada tiap kolom
10. Verifikasi Zona Body memuat icon Pin pada tiap kolom
11. Verifikasi Zona Body memuat Live Preview
12. Verifikasi Zona Footer memuat `[Reset to Default]` dan `[Save]`
13. Verifikasi Zona Footer tidak memuat `[Cancel]`
14. Klik `[✕]`
15. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Overlay Column Visibility dari TC-FA-LBL-312 dipakai langsung oleh TC-FA-LBL-313 (klik `Setup Column...`).
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup popup Setup Column dengan `[✕]` (tanpa perubahan) dan menutup Modal Changelog di akhir spec.
- TC-FA-LBL-314 ada di spec 167. TC-FA-LBL-315 dan TC-FA-LBL-316 ada di spec 084; TC-FA-LBL-317 dan TC-FA-LBL-318 ada di spec 085.
- Temuan untuk QA:
  - TC-FA-LBL-284 menyebut overlay Column Visibility memiliki CTA `[Setup Column]`, sedangkan TC-FA-LBL-312 menyebut item `Setup Column...`. Spec ini memakai `Setup Column...` sesuai TC-FA-LBL-312.
  - Popup Setup Column pada TC-FA-LBL-313 menyebut "Live Preview" tanpa isi; spec hanya mengasersi keberadaannya.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
