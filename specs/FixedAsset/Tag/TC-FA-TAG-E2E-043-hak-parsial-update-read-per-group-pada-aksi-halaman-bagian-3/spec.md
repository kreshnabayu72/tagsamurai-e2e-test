---
id: TC-FA-TAG-E2E-043-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-3
title: "Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 3)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-157
  - TC-FA-TAG-158
  - TC-FA-TAG-159
  - TC-FA-TAG-160
  - TC-FA-TAG-161
coverage:
  web: automated
---

# Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B | UP_PA_ROPB | `manageAssetTagDenganUpdatePadaGroupPlantADanHanyaReadPadaGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PA_ROPB_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Aset 'Excavator 20 Ton - 13' (AST-0013, Group Plant B, TAG Type RFID) punya Tag RFID `RF-00103` Paired; aset 'Excavator 20 Ton - 14' (AST-0014, Group Plant B) punya Tag QR `QR-00235` Paired (Non-standard); aset 'Excavator 20 Ton - 55' (AST-0055, Group Plant B, TAG Type RFID) Not Paired Yet; aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired; satu reader RFID/NFC tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

1. Klik Asset Name `Excavator 20 Ton` pada baris grup Plant B untuk membuka Popup Detail
2. Klik kebab baris 'Excavator 20 Ton - 13'
3. Verifikasi baris 'Excavator 20 Ton - 13' (Plant B) tidak memuat row action `Replace TAG` (Hidden)
4. Verifikasi baris tetap tampil dan `TAG Code` terbaca
5. Tutup Popup Detail
6. Klik kebab di ujung baris grup Excavator 20 Ton Plant B
7. Verifikasi kebab grup Plant B hanya memuat `Detail`
8. Verifikasi `Replace non-standard TAGs` Hidden
9. Klik Asset Name `Excavator 20 Ton` pada baris grup Plant B untuk membuka Popup Detail
10. Klik `Show` di samping `Not Paired Yet`
11. Klik kebab baris 'Excavator 20 Ton - 55'
12. Verifikasi baris tidak memuat row action `Pair TAG`
13. Centang baris 'Excavator 20 Ton - 55'
14. Verifikasi Bulk Action Bar tidak memuat `Pair TAG`
15. Tutup Popup Detail
16. Klik Asset Name `Excavator 20 Ton` pada baris grup Plant A untuk membuka Popup Detail
17. Klik kebab baris 'Excavator 20 Ton - 220'
18. Verifikasi baris 'Excavator 20 Ton - 220' (Plant A) memuat row action `Replace TAG`
19. Klik kebab di ujung baris grup Excavator 20 Ton Plant A
20. Verifikasi kebab grup Plant A memuat `Detail` dan `Replace non-standard TAGs`
21. Tutup Popup Detail
22. Verifikasi tombol `Print QR` dan `Replace TAG` tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 5, 10, 15, 21.
- Pembagian TC lintas spec: TC-FA-TAG-130 dan TC-FA-TAG-162 ada di spec `TC-FA-TAG-E2E-032-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-2`.
- Kebab baris dibuka sebagai langkah penghubung pada TC-FA-TAG-157, 159, dan 160 karena aksi baris hanya teramati lewat kebab baris.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-160 butir b bersyarat ("bila Non-standard > 0, Replace non-standard TAGs") dan tidak menyebut Non-standard grup Plant A, sedangkan Pre-setup tab Paired menyebut Non-standard 0 untuk Excavator 20 Ton / Plant A. Spec mengasersi tanpa syarat dengan dataset Precondition TC-148 (AST-0042 Non-standard di Plant A).
  - TC-157, TC-159, dan TC-160 tidak punya langkah yang membuka kebab baris; spec menambahnya sebagai langkah penghubung.
