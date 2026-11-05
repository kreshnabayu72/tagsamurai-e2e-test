---
id: TC-FA-TAG-E2E-034-scope-group-grup-popup-detail-kartu-dan-search-bagian-2
title: "Scope Group: Search Tidak Menampilkan Grup di Luar Scope"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-138
coverage:
  web: automated
---

# Scope Group: Search Tidak Menampilkan Grup di Luar Scope

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) (Update: Plant A) | MU_PA | `manageAssetTagReadUpdateUpdatePlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PA_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Ketik Search `Laptop`, tekan Enter
2. Verifikasi `No results found` tampil karena Laptop Pro 14 / HQ di luar scope
3. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 3.
- Pembagian TC lintas spec: TC-FA-TAG-30 dan TC-FA-TAG-131 sampai 137 ada di spec `TC-FA-TAG-E2E-033-scope-group-grup-popup-detail-kartu-dan-search-bagian-1`.
- Langkah 1 menggabungkan `Klik ikon Search` dan `Ketik ... lalu tekan Enter` pada TC menjadi satu langkah atomik (bagian 8b butir 9).
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-138 bertipe Security dengan Expected `No results found`; asersi hanya pada tampilan, bukan pada respons server.
