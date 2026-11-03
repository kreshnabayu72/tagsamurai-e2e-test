---
id: TC-FA-TAG-E2E-380-hak-parsial-update-read-per-group-pada-aksi-halaman-return-group-dan-descendant
title: "Hak Parsial Update dan Read per Group pada Aksi Halaman TAG: Return Group dan Descendant"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-128
  - TC-FA-TAG-129
coverage:
  web: automated
---

# Hak Parsial Update dan Read per Group pada Aksi Halaman TAG: Return Group dan Descendant

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) (Update: Disposal Center; Read: HQ Warehouse) | MU | `manageAssetTagReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PASSWORD` |
| 2 | Manage asset & TAG (Read + Update) (Update: Plant A; Plant A > Line 1 > Zone 1 adalah descendant) | MU | `manageAssetTagReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Data: blok 1 memegang Update pada Disposal Center dan Read pada HQ Warehouse, blok 2 memegang Update pada Plant A dengan descendant tiga tingkat (capability diatur lewat fixture backend sebelum tiap blok).
- Data: Tab To Be Returned memuat RF-00071 (Return Group Disposal Center) dan NF-00092 (Return Group HQ Warehouse).
- Data: Grup Excavator 20 Ton ada di Plant A, Plant A > Line 1, dan Plant A > Line 1 > Zone 1.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Update pada Disposal Center, Read pada HQ Warehouse (TC-FA-TAG-128)

1. Klik Tab `To Be Returned`
2. Klik kebab baris RF-00071
3. Verifikasi kebab RF-00071 memuat `Receive Manually`
4. Klik kebab baris NF-00092
5. Verifikasi baris NF-00092 tetap tampil
6. Verifikasi kebab NF-00092 tidak memuat `Receive Manually` (Hidden)

### Update pada Plant A dengan descendant tiga tingkat (TC-FA-TAG-129)

7. Ganti akun: logout dari akun Manage asset & TAG (Read + Update) (Update: Disposal Center; Read: HQ Warehouse) [MU], login dengan akun Manage asset & TAG (Read + Update) (Update: Plant A; Plant A > Line 1 > Zone 1 adalah descendant) [MU], lalu buka Fixed Asset > TAG tab Paired
8. Verifikasi tiga baris grup Excavator 20 Ton (Plant A, Line 1, Zone 1) tampil
9. Klik kebab baris grup Zone 1
10. Verifikasi kebab baris Zone 1 memuat aksi tulis (Show) karena Zone 1 descendant dari group Update
11. Klik Asset Name `Excavator 20 Ton` pada baris grup Zone 1 untuk membuka Popup Detail
12. Klik kebab baris aset pertama di Popup Detail Zone 1
13. Verifikasi row action aset di Popup Detail Zone 1 memuat aksi tulis (Show) karena Zone 1 descendant dari group Update

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 7.
- Pembagian TC lintas spec: TC-FA-TAG-122 dan 124 sampai 127 ada di spec `TC-FA-TAG-E2E-031-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-1`; TC-FA-TAG-130 dan TC-FA-TAG-162 ada di spec `TC-FA-TAG-E2E-032-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-2`; TC-FA-TAG-157 sampai 161 ada di spec `TC-FA-TAG-E2E-043-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-3`.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-128 dan TC-129 memakai Role `Manage asset & TAG (Read + Update)` dengan catatan group dalam kurung; kunci akun tidak tertulis di Pre-setup TC. Spec memakai akun `Manage asset & TAG (Read + Update)` dengan capability group yang diatur fixture backend; Pre-setup juga memuat akun terdekat `Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse` dan `Manage asset & TAG (Read + Update) (Update: Plant A)`.
  - TC-129 butir b menyebut "aksi tulis" tanpa nama aksi; spec mengasersi bahwa aksi tulis tampil (Show) tanpa menyebut nama aksi. TC-129 (langkah TC ke-2) membuka Popup Detail Zone 1 tanpa menyebut aset; spec membuka kebab baris aset pertama sebagai langkah penghubung.
