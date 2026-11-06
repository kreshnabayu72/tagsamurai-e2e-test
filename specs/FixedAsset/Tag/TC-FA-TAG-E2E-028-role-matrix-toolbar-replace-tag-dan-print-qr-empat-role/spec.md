---
id: TC-FA-TAG-E2E-028-role-matrix-toolbar-replace-tag-dan-print-qr-empat-role
title: "Role Matrix: Tombol Toolbar Replace TAG dan Print QR per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-144
  - TC-FA-TAG-145
  - TC-FA-TAG-146
  - TC-FA-TAG-147
coverage:
  web: automated
---

# Role Matrix: Tombol Toolbar Replace TAG dan Print QR per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 3 | Manage asset & TAG (Read) | MR | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |
| 4 | Manage asset & TAG (Read + Update) dengan Update pada Group Plant A | MU_UPA | `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_UPA_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00330` berstatus Paired; aset 'Excavator 20 Ton - 42' (AST-0042, Group Plant A, TAG Type Asset Name RFID) punya satu Tag QR `QR-00230` berstatus Paired (Non-standard); aset 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet); stok Global: Tag RFID `RF-00412` dan `RF-00415` serta Tag NFC `NF-00500` berstatus Available.
- Data: satu reader RFID/NFC tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- Kemampuan teknis (disediakan tim FE/BE): membaca tombol `Print QR` dan `Replace TAG` pada Table Tools dan state Enabled atau Disabled-nya.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### Total Control (TC-FA-TAG-144)

1. Verifikasi tombol `Print QR` tampil dan Enabled
2. Verifikasi tombol scan `Replace TAG` tampil dan Enabled
3. Verifikasi `Print QR` berada di sebelah kiri `Replace TAG`

### Read Only (TC-FA-TAG-145)

4. Ganti akun: logout dari akun Total Control [TC], login dengan akun Read Only [RO], lalu buka Fixed Asset > TAG tab Paired
5. Verifikasi tombol `Print QR` Hidden (tidak dirender)
6. Verifikasi tombol scan `Replace TAG` Hidden (tidak dirender)
7. Verifikasi tombol `Changelog` dan Download tetap tampil

### Manage asset & TAG (Read) (TC-FA-TAG-146)

8. Ganti akun: logout dari akun Read Only [RO], login dengan akun Manage asset & TAG (Read) [MR], lalu buka Fixed Asset > TAG tab Paired
9. Verifikasi tombol `Print QR` Hidden (tidak dirender)
10. Verifikasi tombol scan `Replace TAG` Hidden (tidak dirender)
11. Verifikasi tombol `Changelog` dan Download tetap tampil

### Manage asset & TAG (Read + Update) dengan Update pada Group Plant A (TC-FA-TAG-147)

12. Ganti akun: logout dari akun Manage asset & TAG (Read) [MR], login dengan akun Manage asset & TAG (Read + Update) dengan Update pada Group Plant A [MU_UPA], lalu buka Fixed Asset > TAG tab Paired
13. Verifikasi tombol `Print QR` tampil dan Enabled
14. Verifikasi tombol scan `Replace TAG` tampil dan Enabled

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 4, 8, 12.
- Tombol toolbar diamati tanpa memindai; reader tersambung hanya sebagai precondition TC dan tidak diasersi.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - Pre-setup tab Paired menyebut Non-standard 0 untuk grup Excavator 20 Ton / Plant A, sedangkan Precondition TC-144 sampai TC-162 menyebut AST-0042 (Tag QR, Non-standard) di Plant A; spec memakai dataset Precondition TC masing-masing (kebab grup Excavator 20 Ton / Plant A memuat `Replace non-standard TAGs`).
