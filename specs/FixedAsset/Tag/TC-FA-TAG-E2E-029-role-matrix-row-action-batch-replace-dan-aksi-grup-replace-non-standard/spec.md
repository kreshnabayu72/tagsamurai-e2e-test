---
id: TC-FA-TAG-E2E-029-role-matrix-row-action-batch-replace-dan-aksi-grup-replace-non-standard
title: "Role Matrix: Row Action Replace TAG, Batch Replace TAG, dan Aksi Grup Replace non-standard TAGs"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-148
  - TC-FA-TAG-149
  - TC-FA-TAG-150
coverage:
  web: automated
---

# Role Matrix: Row Action Replace TAG, Batch Replace TAG, dan Aksi Grup Replace non-standard TAGs

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 3 | Manage asset & TAG (Read) | MR | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00330` berstatus Paired; aset 'Excavator 20 Ton - 42' (AST-0042, Group Plant A, TAG Type Asset Name RFID) punya satu Tag QR `QR-00230` berstatus Paired (Non-standard); aset 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet); stok Global: Tag RFID `RF-00412` dan `RF-00415` serta Tag NFC `NF-00500` berstatus Available.
- Data: satu reader RFID/NFC tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### Total Control (TC-FA-TAG-148)

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

### Read Only (TC-FA-TAG-149)

11. Ganti akun: logout dari akun Total Control [TC], login dengan akun Read Only [RO], lalu buka Fixed Asset > TAG tab Paired
12. Klik kebab di ujung baris grup Excavator 20 Ton Plant A
13. Verifikasi kebab grup hanya memuat `Detail`; `Replace non-standard TAGs` Hidden
14. Tutup menu kebab (Esc)
15. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
16. Klik kebab baris 'Excavator 20 Ton - 220'
17. Verifikasi baris tidak memuat row action `Replace TAG`
18. Tutup menu kebab (Esc)
19. Centang baris 'Excavator 20 Ton - 220' pada Popup Detail
20. Verifikasi Bulk Action Bar tidak memuat `Batch Replace TAG`
21. Verifikasi checkbox seleksi dan `Detail` tetap tampil
22. Tutup Popup Detail

### Manage asset & TAG (Read) (TC-FA-TAG-150)

23. Ganti akun: logout dari akun Read Only [RO], login dengan akun Manage asset & TAG (Read) [MR], lalu buka Fixed Asset > TAG tab Paired
24. Klik kebab di ujung baris grup Excavator 20 Ton Plant A
25. Verifikasi kebab grup hanya memuat `Detail`; `Replace non-standard TAGs` Hidden
26. Tutup menu kebab (Esc)
27. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
28. Klik kebab baris 'Excavator 20 Ton - 220'
29. Verifikasi baris tidak memuat row action `Replace TAG`
30. Tutup menu kebab (Esc)
31. Centang baris 'Excavator 20 Ton - 220' pada Popup Detail
32. Verifikasi Bulk Action Bar tidak memuat `Batch Replace TAG`
33. Verifikasi checkbox seleksi dan `Detail` tetap tampil
34. Tutup Popup Detail

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 3, 7, 10, 11, 14, 18, 22, 23, 26, 30, 34.
- Pembagian TC lintas spec: TC-FA-TAG-151 dan TC-FA-TAG-152 (pemegang Update pada Group Plant A) ada di spec `TC-FA-TAG-E2E-042-role-matrix-row-action-batch-replace-dan-aksi-grup-replace-non-standard-update-parsial`.
- TC-FA-TAG-148 sampai 150 hanya menyebut kebab grup, Popup Detail, dan centang baris; kebab baris 'Excavator 20 Ton - 220' dibuka sebagai langkah penghubung karena row action `Replace TAG` hanya teramati lewat kebab baris.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - Pre-setup tab Paired menyebut Non-standard 0 untuk grup Excavator 20 Ton / Plant A, sedangkan Precondition TC-144 sampai TC-162 menyebut AST-0042 (Tag QR, Non-standard) di Plant A; spec memakai dataset Precondition TC masing-masing (kebab grup Excavator 20 Ton / Plant A memuat `Replace non-standard TAGs`).
  - TC-148 butir b ("Baris ... memuat row action Replace TAG") tidak punya langkah yang membuka kebab baris; spec menambahnya sebagai langkah penghubung.
