---
id: TC-FA-SU-E2E-241-modal-combined-changelog-user-download
title: "Modal Combined Changelog: User: Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-730
coverage:
  web: automated
---

# Modal Combined Changelog: User: Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Modal Combined Changelog dibuka dari icon Changelog di Table Tools halaman User List dan memuat riwayat seluruh pengguna Client `FaUserMain`. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Combined Changelog (Pre-setup #27, 6 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | User Name | Field; Modified By dalam format `[First Name] [Last Initial]`):
  - C-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`; Modified By `Ahmad D`
  - C-2: `Deactivate` | `Doni Prasetyo` | `Status`; Modified By `Budi S`
  - C-3: `Edit Home Group` | `Budi Santoso` | `Home Group`; Modified By `Lina M`
  - C-4: `Edit` | `Gita Permata` | `Manage group — Finance & Accounting — Update`; Modified By `Ahmad D`
  - C-5: `Assign` | `Budi Santoso` | `Manage accounting`; Modified By `Ahmad D`
  - C-6: `Activate` | `Eka Wulandari` | `Status`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Combined Changelog dan tidak menambah entri.
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nilai sel, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-730: Cakupan baris dan kolom Download: Search, Filter, Sort, dan Column Visibility

1. Klik icon Changelog di Table Tools halaman User List
2. Klik icon Download, pilih `Download as CSV`
3. Verifikasi berkas memuat seluruh baris (bukan hanya halaman aktif)
4. Verifikasi urutan baris pada berkas mengikuti sort aktif
5. Ketik Search `Edit`, tekan Enter
6. Klik icon Filter
7. Buka dropdown Modified By, centang `Ahmad D`
8. Klik `[Apply]`
9. Klik icon Download, pilih `Download as CSV`
10. Verifikasi berkas hanya memuat baris yang cocok dengan Search dan Filter (irisan Search `Edit` dan Filter Modified By `Ahmad D`: C-4 (1 baris))
11. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
12. Klik header Column Visibility (⋯), hilangkan centang Old Value
13. Klik icon Download, pilih `Download as CSV`
14. Verifikasi tidak ada toast peringatan
15. Verifikasi kolom Old Value tidak ikut berkas
16. Klik header Column Visibility (⋯), centang kembali Old Value
17. Klik icon Download, pilih `Download as CSV`
18. Verifikasi kolom Old Value ikut kembali pada berkas
19. Ketik Search `zzzz` (tidak ada hasil), tekan Enter
20. Klik icon Download, pilih `Download as CSV`
21. Verifikasi tidak ada toast
22. Verifikasi berkas terunduh
23. Verifikasi berkas hanya memuat baris header kolom yang visible
24. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- TC-FA-SU-729 ada di spec 240, TC-FA-SU-731 di spec 373, dan TC-FA-SU-732 di spec 368.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) TC-FA-SU-730 langkah 3 tidak menyebut kata kunci Search dan opsi Filter; spec memakai Search `Edit` dan Filter Modified By `Ahmad D` (irisan C-4) serta `zzzz` untuk hasil 0 baris sebagai pilihan sendiri. Hide kolom memakai Old Value.
