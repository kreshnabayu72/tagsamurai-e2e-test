---
id: TC-FA-TAG-E2E-042-role-matrix-row-action-batch-replace-dan-aksi-grup-replace-non-standard-update-parsial
title: "Role Matrix: Aksi Replace TAG bagi Pemegang Update pada Group Plant A dan Descendant"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-151
  - TC-FA-TAG-152
coverage:
  web: automated
---

# Role Matrix: Aksi Replace TAG bagi Pemegang Update pada Group Plant A dan Descendant

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) dengan Update pada Group Plant A | MU_UPA | `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_UPA_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00330` berstatus Paired; aset 'Excavator 20 Ton - 42' (AST-0042, Group Plant A, TAG Type Asset Name RFID) punya satu Tag QR `QR-00230` berstatus Paired (Non-standard); aset 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet); stok Global: Tag RFID `RF-00412` dan `RF-00415` serta Tag NFC `NF-00500` berstatus Available; aset 'Excavator 20 Ton - 24' (AST-0024, Group 'Line 1' anak dari Plant A, TAG Type RFID) punya satu Tag RFID `RF-00143` Paired.
- Data: satu reader RFID/NFC tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik kebab di ujung baris grup Excavator 20 Ton Plant A
2. Verifikasi kebab grup memuat aksi `Replace non-standard TAGs` selain `Detail`
3. Tutup menu kebab (Esc)
4. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
5. Klik kebab baris 'Excavator 20 Ton - 220'
6. Verifikasi baris 'Excavator 20 Ton - 220' memuat row action `Replace TAG`
7. Tutup menu kebab (Esc)
8. Centang baris 'Excavator 20 Ton - 220' pada Popup Detail
9. Verifikasi Bulk Action Bar memuat `Batch Replace TAG`
10. Tutup Popup Detail
11. Klik Asset Name `Excavator 20 Ton` pada baris grup Line 1 untuk membuka Popup Detail
12. Klik kebab baris 'Excavator 20 Ton - 24'
13. Verifikasi baris 'Excavator 20 Ton - 24' memuat row action `Replace TAG`

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 3, 7, 10.
- Pembagian TC lintas spec: TC-FA-TAG-148 sampai 150 (Total Control, Read Only, Manage asset & TAG (Read)) ada di spec `TC-FA-TAG-E2E-029-role-matrix-row-action-batch-replace-dan-aksi-grup-replace-non-standard`.
- Kebab baris 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 24' dibuka sebagai langkah penghubung karena row action `Replace TAG` hanya teramati lewat kebab baris.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - Pre-setup tab Paired menyebut Non-standard 0 untuk grup Excavator 20 Ton / Plant A, sedangkan Precondition TC-144 sampai TC-162 menyebut AST-0042 (Tag QR, Non-standard) di Plant A; spec memakai dataset Precondition TC masing-masing (kebab grup Excavator 20 Ton / Plant A memuat `Replace non-standard TAGs`).
  - TC-151 dan TC-152 tidak punya langkah yang membuka kebab baris; spec menambahnya sebagai langkah penghubung.
