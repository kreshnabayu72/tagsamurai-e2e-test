---
id: TC-FA-TAG-E2E-031-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-1
title: "Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-122
  - TC-FA-TAG-124
  - TC-FA-TAG-125
  - TC-FA-TAG-126
  - TC-FA-TAG-127
coverage:
  web: automated
---

# Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Manage asset & TAG (Read + Update) (Update: Plant A; Read: Plant B) | MU | `manageAssetTagReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Data: Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan AST-0011 (Excavator 20 Ton - 11), AST-0020 (Excavator 20 Ton - 20), AST-0021 (Excavator 20 Ton - 21), AST-0043 (Excavator 20 Ton - 43), AST-0044 (Excavator 20 Ton - 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011.
- Data: Group Plant A dan Plant B; blok 2 memegang Update pada Plant A dan Read pada Plant B (capability diatur lewat fixture backend sebelum blok).
- Data: Tab To Be Returned memuat RF-00071 (Return Group Disposal Center).
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Total Control (TC-FA-TAG-122)

1. Klik kebab grup Excavator 20 Ton pada baris Plant B
2. Tutup menu kebab (Esc)
3. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
4. Klik kebab baris aset dengan laporan terbuka AST-0020
5. Verifikasi row action tab Paired hanya terdiri atas `Replace TAG`, `Pair TAG`, dan `Decline Report`
6. Tutup menu kebab (Esc)
7. Centang dua aset ber-Tag normal (AST-0011 dan AST-0021)
8. Tutup Popup Detail
9. Klik Tab `To Be Returned`
10. Klik kebab baris RF-00071
11. Verifikasi tidak ada tombol atau aksi `Report TAG` maupun `Cancel Report` di halaman TAG

### Manage asset & TAG (Read + Update) (Update: Plant A; Read: Plant B) (TC-FA-TAG-124 sampai TC-FA-TAG-127)

12. Ganti akun: logout dari akun Total Control [TC], login dengan akun Manage asset & TAG (Read + Update) (Update: Plant A; Read: Plant B) [MU], lalu buka Fixed Asset > TAG tab Paired
13. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
14. Klik kebab baris aset ber-Tag AST-0220
15. Verifikasi Popup Plant A: kebab aset ber-Tag memuat `Replace TAG`
16. Tutup Popup Detail
17. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
18. Klik kebab baris aset ber-Tag AST-0011
19. Verifikasi Popup Plant B: kebab aset tidak memuat `Replace TAG`, `Pair TAG`, maupun `Decline Report` (Hidden)
20. Tutup Popup Detail
21. Klik kebab baris Forklift Manual / Plant A (Non-standard 3)
22. Verifikasi baris Plant A memuat `Detail` dan `Replace non-standard TAGs`
23. Klik kebab baris Excavator 20 Ton / Plant B (Non-standard 5)
24. Verifikasi baris Plant B hanya memuat `Detail`
25. Verifikasi tombol `Print QR` dan `Replace TAG` tampil
26. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
27. Centang dua aset ber-Tag normal (AST-0011 dan AST-0021)
28. Verifikasi tidak ada aksi `Batch Replace TAG` pada Bulk Action Bar (Hidden karena group Plant B hanya Read)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 2, 6, 8, 12, 16, 20.
- Pembagian TC lintas spec: TC-FA-TAG-128 dan 129 ada di spec `TC-FA-TAG-E2E-380-hak-parsial-update-read-per-group-pada-aksi-halaman-return-group-dan-descendant`; TC-FA-TAG-130 dan TC-FA-TAG-162 ada di spec `TC-FA-TAG-E2E-032-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-2`; TC-FA-TAG-157 sampai 161 ada di spec `TC-FA-TAG-E2E-043-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-3`.
- Kebab baris dibuka sebagai langkah penghubung pada TC-FA-TAG-122, 124, dan 127 karena aksi baris hanya teramati lewat kebab baris.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-124 sampai TC-127 memakai Role `Manage asset & TAG (Read + Update) (Update: Plant A; Read: Plant B)`; kunci akun tidak tertulis di Pre-setup TC. Spec memakai akun `Manage asset & TAG (Read + Update)` dengan capability group yang diatur fixture backend; Pre-setup juga memuat akun terdekat `Manage asset & TAG dengan Update di group Plant A dan Read di group Plant B`.
  - TC-122 butir b ("Row action tab Paired hanya Replace TAG, Pair TAG, dan Decline Report") tidak menyebut baris yang diperiksa; spec memeriksa kebab baris AST-0020 (aset dengan laporan terbuka).
  - TC-124 butir a memakai kebab aset ber-Tag di Popup Plant A tanpa menyebut aset; spec memakai AST-0220 (data TC-148).
  - Pre-setup tab Paired menyebut Non-standard 0 untuk grup Excavator 20 Ton / Plant A, sedangkan Precondition TC-144 sampai TC-162 menyebut AST-0042 (Tag QR, Non-standard) di Plant A; spec memakai dataset Precondition TC masing-masing (kebab grup Excavator 20 Ton / Plant A memuat `Replace non-standard TAGs`).
