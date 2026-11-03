---
id: TC-FA-TAG-E2E-032-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-2
title: "Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-130
  - TC-FA-TAG-162
coverage:
  web: automated
---

# Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read) (Read: Plant A dan Plant B) | MR_PAPB | `manageAssetTagReadReadPlantADanPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PAPB_PASSWORD` |
| 2 | Manage asset & TAG (Read + Update) dengan Update pada Group Plant A | MU_UPA | `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_UPA_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Data: Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan AST-0011 (Excavator 20 Ton - 11), AST-0020 (Excavator 20 Ton - 20), AST-0021 (Excavator 20 Ton - 21), AST-0043 (Excavator 20 Ton - 43), AST-0044 (Excavator 20 Ton - 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011.
- Data: Pre-setup Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.).
- Data: Aset 'Label Printer - 72' (AST-0172, Group Plant A, TAG Type Asset Name QR) punya satu Tag QR `QR-00290` berstatus Paired; kode QR `QR-00700` berstatus Available (dibuat backend saat Start Print sebelumnya, belum Paired); satu reader RFID/NFC tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Manage asset & TAG (Read) (Read: Plant A dan Plant B) (TC-FA-TAG-130)

1. Verifikasi tombol `Print QR` dan `Replace TAG` tidak ada (Hidden) pada Table Tools tab Paired
2. Klik kebab baris Excavator 20 Ton / Plant B (Non-standard 5)
3. Verifikasi aksi `Replace non-standard TAGs` tidak ada (Hidden)
4. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
5. Klik kebab baris aset dengan laporan terbuka AST-0020
6. Verifikasi aksi `Replace TAG` dan `Decline Report` tidak ada (Hidden)
7. Centang dua aset ber-Tag normal (AST-0011 dan AST-0021)
8. Verifikasi aksi `Batch Replace TAG` tidak ada pada Bulk Action Bar (Hidden)
9. Tutup Popup Detail
10. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
11. Klik `Show` di samping `Not Paired Yet`
12. Klik kebab baris aset Not Paired Yet
13. Verifikasi aksi `Pair TAG` tidak ada (Hidden)
14. Tutup Popup Detail
15. Klik Tab `To Be Returned`
16. Verifikasi tombol `Receive TAG` tidak ada (Hidden)
17. Klik kebab baris RF-00071
18. Verifikasi aksi `Receive Manually` tidak ada pada kebab baris (Hidden)
19. Centang baris RF-00071
20. Verifikasi aksi `Receive Manually` tidak ada pada Bulk Action Bar (Hidden)
21. Verifikasi aksi baca `Detail`, `Changelog`, `Event Log`, Download, dan TAG Log tetap tampil

### Manage asset & TAG (Read + Update) dengan Update pada Group Plant A (TC-FA-TAG-162)

22. Ganti akun: logout dari akun Manage asset & TAG (Read) (Read: Plant A dan Plant B) [MR_PAPB], login dengan akun Manage asset & TAG (Read + Update) dengan Update pada Group Plant A [MU_UPA], lalu buka Fixed Asset > TAG tab Paired
23. Klik Asset Name 'Label Printer' pada baris grup Plant A untuk membuka Popup Detail
24. Klik kebab baris 'Label Printer - 72'
25. Klik row action `Replace TAG` pada baris 'Label Printer - 72'
26. Verifikasi slot `QR TAG` memuat tombol `Print QR`

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 9, 11, 14, 22.
- Pembagian TC lintas spec: TC-FA-TAG-122 dan TC-FA-TAG-124 sampai 129 ada di spec `TC-FA-TAG-E2E-031-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-1`; TC-FA-TAG-157 sampai 161 ada di spec `TC-FA-TAG-E2E-043-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-3`.
- Aksi baca `Detail`, `Changelog`, `Event Log`, Download, dan TAG Log pada `Verifikasi` terakhir blok pertama diamati dari permukaan yang sudah dibuka pada langkah sebelumnya.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-130 butir a menyebut delapan aksi tulis Hidden dalam satu butir; spec memecahnya per permukaan tempat aksi itu teramati (Table Tools, kebab grup, kebab baris, Bulk Action Bar, tab To Be Returned).
  - TC-162 hanya menyebut membuka dialog `Replace TAG` dan slot `QR TAG`; kebab baris dibuka sebagai langkah penghubung.
