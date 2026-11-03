---
id: TC-FA-TAG-E2E-035-scope-group-modal-changelog-dan-event-log
title: "Scope Group: Modal Changelog dan Event Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-139
  - TC-FA-TAG-140
  - TC-FA-TAG-141
coverage:
  web: automated
---

# Scope Group: Modal Changelog dan Event Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) (Update: Plant A) | MU_PA | `manageAssetTagReadUpdateUpdatePlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PA_PASSWORD` |
| 2 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 3 | Manage asset & TAG (Read + Update) (Update: Disposal Center) | MU_DC | `manageAssetTagReadUpdateUpdateDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_DC_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Entri Changelog (Replace) untuk Excavator 20 Ton - 50 (Plant A) dan Excavator 20 Ton - 20 (Plant B) dibuat sebagai entri terbaru sehingga berada di halaman pertama Modal Changelog.
- Data: Event Log To Be Returned memuat entri RF-00071 (Return Group Disposal Center) dan NF-00092 (Return Group HQ Warehouse) sebagai entri terbaru.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Manage asset & TAG (Read + Update) (Update: Plant A) (TC-FA-TAG-139)

1. Klik tombol `Changelog`
2. Verifikasi entri Excavator 20 Ton - 50 tampil
3. Verifikasi entri Excavator 20 Ton - 20 tidak tampil
4. Tutup modal Changelog

### Read Only (TC-FA-TAG-140)

5. Ganti akun: logout dari akun Manage asset & TAG (Read + Update) (Update: Plant A) [MU_PA], login dengan akun Read Only [RO], lalu buka Fixed Asset > TAG tab Paired
6. Klik tombol `Changelog`
7. Verifikasi kedua entri (Excavator 20 Ton - 50 dan Excavator 20 Ton - 20) tampil
8. Tutup modal Changelog

### Manage asset & TAG (Read + Update) (Update: Disposal Center) (TC-FA-TAG-141)

9. Ganti akun: logout dari akun Read Only [RO], login dengan akun Manage asset & TAG (Read + Update) (Update: Disposal Center) [MU_DC], lalu buka Fixed Asset > TAG tab Paired
10. Klik Tab `To Be Returned`
11. Klik tombol `Event Log`
12. Verifikasi entri RF-00071 tampil
13. Verifikasi entri NF-00092 tidak tampil
14. Tutup modal Event Log

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 4, 5, 8, 9, 14.
- Entri Changelog dan Event Log diamati pada halaman pertama modal karena entri seeding menjadi entri terbaru (S-14); tidak ada asersi jumlah total entri.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-139 dan TC-140 tidak menyebut cara menemukan entri di Modal Changelog; spec mengasumsikan entri seeding berada di halaman pertama.
  - TC-141 menyebut entri NF-00092 di Event Log sedangkan TC-169 dan TC-170 memakai NF-00093; spec mengikuti masing-masing TC.
