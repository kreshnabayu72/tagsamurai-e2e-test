---
id: TC-FA-TAG-E2E-023-role-matrix-positif-aksi-tulis-total-control-dan-manage-read-bagian-1
title: "Role Matrix Positif: Aksi Tulis Total Control dan Manage asset & TAG (Read + Update) (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-97
  - TC-FA-TAG-98
  - TC-FA-TAG-99
  - TC-FA-TAG-100
  - TC-FA-TAG-101
  - TC-FA-TAG-102
  - TC-FA-TAG-115
  - TC-FA-TAG-116
coverage:
  web: automated
---

# Role Matrix Positif: Aksi Tulis Total Control dan Manage asset & TAG (Read + Update) (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Manage asset & TAG (Read + Update) | MU | `manageAssetTagReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Data: Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan AST-0011 (Excavator 20 Ton - 11), AST-0020 (Excavator 20 Ton - 20), AST-0021 (Excavator 20 Ton - 21), AST-0043 (Excavator 20 Ton - 43), AST-0044 (Excavator 20 Ton - 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011.
- Data: Pre-setup Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.).
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Total Control (TC-FA-TAG-97 sampai TC-FA-TAG-102)

1. Verifikasi tombol `Print QR` dan tombol scan `Replace TAG` tampil (Show) pada Table Tools tab Paired
2. Verifikasi `Print QR` berada di kiri `Replace TAG`
3. Klik kebab baris Excavator 20 Ton / Plant B (Non-standard 5)
4. Verifikasi aksi `Detail` dan `Replace non-standard TAGs` (ikon `ReplaceTag`, dark) tampil
5. Tutup menu kebab (Esc)
6. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
7. Klik kebab baris aset ber-Tag AST-0011
8. Verifikasi kebab AST-0011 memuat `Replace TAG`
9. Tutup menu kebab (Esc)
10. Centang dua aset ber-Tag normal (AST-0011 dan AST-0021)
11. Verifikasi Bulk Action Bar tampil dengan aksi `Batch Replace TAG` (ikon `ReplaceTag`, dark)
12. Tutup Popup Detail
13. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
14. Klik `Show` di samping `Not Paired Yet`
15. Klik kebab baris aset Not Paired Yet
16. Verifikasi kebab aset Not Paired Yet memuat `Pair TAG`
17. Tutup Popup Detail
18. Klik Tab `To Be Returned`
19. Verifikasi tombol scan `Receive TAG` tampil di ujung kanan setelah `Event Log`
20. Klik kebab baris RF-00071
21. Verifikasi kebab baris RF-00071 memuat `Receive Manually`
22. Tutup menu kebab (Esc)
23. Centang baris RF-00071
24. Verifikasi Bulk Action Bar memuat `Receive Manually`
25. Verifikasi tombol `Event Log` tampil (Show)
26. Klik tombol `Event Log`
27. Verifikasi modal `Event Log: To Be Returned` terbuka
28. Tutup modal Event Log

### Manage asset & TAG (Read + Update) (TC-FA-TAG-115 dan TC-FA-TAG-116)

29. Ganti akun: logout dari akun Total Control [TC], login dengan akun Manage asset & TAG (Read + Update) [MU], lalu buka Fixed Asset > TAG tab Paired
30. Verifikasi tombol `Print QR` dan tombol scan `Replace TAG` tampil (Show)
31. Verifikasi `Print QR` berada di kiri `Replace TAG`
32. Klik kebab baris Excavator 20 Ton / Plant B (Non-standard 5)
33. Verifikasi aksi `Detail` dan `Replace non-standard TAGs` (ikon `ReplaceTag`, dark) tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 5, 9, 12, 14, 17, 22, 28, 29.
- Urutan TC-FA-TAG-99 dan TC-FA-TAG-100 disusun ulang (kebab AST-0011 dan Bulk Batch Replace TAG di Popup Detail Plant B dahulu, baru Popup Detail Plant A) supaya popup tidak dibuka dua kali; Expected tiap TC tetap diasersi.
- Row action Pair TAG diamati pada baris Not Paired Yet di Popup Detail Plant A, sehingga `Show` di samping `Not Paired Yet` diklik lebih dulu (dipakai TC-FA-TAG-153).
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-99 (langkah TC ke-3) membuka kebab baris aset Not Paired Yet tanpa menyebut filter `Show` di samping `Not Paired Yet`; TC-153 menyebutnya. Spec menambah langkah penghubung itu.
  - TC-115 dan TC-116 memakai Role `Manage asset & TAG (Read + Update)` tanpa menyebut group Update; spec menganggap akun itu memegang Update pada group data uji.
