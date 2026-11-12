---
id: TC-FA-TAG-E2E-030-role-matrix-pair-tag-row-action-dan-bulk
title: "Role Matrix: Pair TAG pada Row Action dan Bulk Action Bar"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-153
  - TC-FA-TAG-154
  - TC-FA-TAG-155
  - TC-FA-TAG-156
coverage:
  web: automated
---

# Role Matrix: Pair TAG pada Row Action dan Bulk Action Bar

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
- Data: Aset 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja) dan 'Excavator 20 Ton - 52' (AST-0052, Group Plant A, TAG Type RFID) belum punya Tag Paired (Not Paired Yet); stok Global: Tag RFID `RF-00412` dan `RF-00415` serta Tag NFC `NF-00500` berstatus Available.
- Data: satu reader RFID/NFC tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### Total Control (TC-FA-TAG-153)

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
2. Klik `Show` di samping `Not Paired Yet`
3. Klik kebab baris 'Excavator 20 Ton - 51'
4. Verifikasi baris 'Excavator 20 Ton - 51' memuat row action `Pair TAG`
5. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 52'
6. Verifikasi Bulk Action Bar memuat `Pair TAG`
7. Tutup Popup Detail

### Read Only (TC-FA-TAG-154)

8. Ganti akun: logout dari akun Total Control [TC], login dengan akun Read Only [RO], lalu buka Fixed Asset > TAG tab Paired
9. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
10. Klik `Show` di samping `Not Paired Yet`
11. Klik kebab baris 'Excavator 20 Ton - 51'
12. Verifikasi baris tidak memuat row action `Pair TAG` (Hidden)
13. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 52'
14. Verifikasi Bulk Action Bar tidak memuat `Pair TAG` (Hidden)
15. Tutup Popup Detail

### Manage asset & TAG (Read) (TC-FA-TAG-155)

16. Ganti akun: logout dari akun Read Only [RO], login dengan akun Manage asset & TAG (Read) [MR], lalu buka Fixed Asset > TAG tab Paired
17. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
18. Klik `Show` di samping `Not Paired Yet`
19. Klik kebab baris 'Excavator 20 Ton - 51'
20. Verifikasi baris tidak memuat row action `Pair TAG` (Hidden)
21. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 52'
22. Verifikasi Bulk Action Bar tidak memuat `Pair TAG` (Hidden)
23. Tutup Popup Detail

### Manage asset & TAG (Read + Update) dengan Update pada Group Plant A (TC-FA-TAG-156)

24. Ganti akun: logout dari akun Manage asset & TAG (Read) [MR], login dengan akun Manage asset & TAG (Read + Update) dengan Update pada Group Plant A [MU_UPA], lalu buka Fixed Asset > TAG tab Paired
25. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
26. Klik `Show` di samping `Not Paired Yet`
27. Klik kebab baris 'Excavator 20 Ton - 51'
28. Verifikasi baris 'Excavator 20 Ton - 51' memuat row action `Pair TAG`
29. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 52'
30. Verifikasi Bulk Action Bar memuat `Pair TAG`
31. Tutup Popup Detail

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 2, 7, 8, 10, 15, 16, 18, 23, 24, 26, 31.
- TC-FA-TAG-153 sampai 156 hanya menyebut centang baris; kebab baris 'Excavator 20 Ton - 51' dibuka sebagai langkah penghubung karena row action `Pair TAG` hanya teramati lewat kebab baris.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-153 sampai TC-156 butir a ("Baris ... memuat row action Pair TAG") tidak punya langkah yang membuka kebab baris; spec menambahnya sebagai langkah penghubung.
