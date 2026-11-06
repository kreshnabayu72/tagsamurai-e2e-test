---
id: TC-FA-TAG-E2E-025-role-matrix-negatif-aksi-tulis-read-only-bagian-1
title: "Role Matrix Negatif: Aksi Tulis pada Halaman TAG untuk Read Only (Bagian 1)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-103
  - TC-FA-TAG-104
  - TC-FA-TAG-105
  - TC-FA-TAG-106
  - TC-FA-TAG-107
  - TC-FA-TAG-108
coverage:
  web: automated
---

# Role Matrix Negatif: Aksi Tulis pada Halaman TAG untuk Read Only (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Data: Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan AST-0011 (Excavator 20 Ton - 11), AST-0020 (Excavator 20 Ton - 20), AST-0021 (Excavator 20 Ton - 21), AST-0043 (Excavator 20 Ton - 43), AST-0044 (Excavator 20 Ton - 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011.
- Data: Pre-setup Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.); kebab AST-0020 memakai aset dengan laporan terbuka (Reported 2 pada grup Plant B).
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

1. Verifikasi tombol `Replace TAG` tidak ada (Hidden)
2. Verifikasi tombol `Print QR` tidak ada (Hidden)
3. Verifikasi Table Tools hanya memuat `Search | Filter | Download | Changelog`
4. Klik kebab baris Excavator 20 Ton / Plant B (Non-standard 5)
5. Verifikasi hanya aksi `Detail` yang tampil
6. Verifikasi aksi `Replace non-standard TAGs` tidak ada (Hidden)
7. Tutup menu kebab (Esc)
8. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
9. Klik kebab baris aset ber-Tag AST-0011
10. Verifikasi kebab AST-0011 tidak memuat `Replace TAG` (Hidden)
11. Tutup menu kebab (Esc)
12. Klik kebab baris aset dengan laporan terbuka AST-0020
13. Verifikasi kebab aset dengan laporan terbuka tidak memuat `Decline Report` (Hidden)
14. Tutup menu kebab (Esc)
15. Centang dua aset ber-Tag normal (AST-0011 dan AST-0021)
16. Verifikasi tidak ada aksi `Batch Replace TAG` maupun `Pair TAG` pada Bulk Action Bar (Hidden)
17. Tutup Popup Detail
18. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
19. Klik `Show` di samping `Not Paired Yet`
20. Klik kebab baris aset Not Paired Yet
21. Verifikasi kebab aset Not Paired Yet tidak memuat `Pair TAG` (Hidden)
22. Tutup Popup Detail
23. Klik Tab `To Be Returned`
24. Verifikasi tombol `Event Log` tampil (Show)
25. Verifikasi tombol `Receive TAG` tidak ada (Hidden)
26. Klik kebab baris RF-00071
27. Verifikasi kebab baris tidak memuat `Receive Manually` (Hidden)
28. Tutup menu kebab (Esc)
29. Centang baris RF-00071
30. Verifikasi Bulk Action Bar tidak memuat `Receive Manually` (Hidden)
31. Klik tombol `Event Log`
32. Verifikasi modal `Event Log: To Be Returned` terbuka

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 7, 11, 14, 17, 19, 22, 28.
- Urutan TC-FA-TAG-105 dan TC-FA-TAG-106 disusun ulang (kebab di Popup Detail Plant B, lalu Bulk Action Bar Plant B, lalu Popup Detail Plant A) supaya popup tidak dibuka dua kali; Expected tiap TC tetap diasersi.
- Langkah `Verifikasi` tombol `Event Log` tampil (TC-FA-TAG-108 butir a) diletakkan sebelum asersi Hidden tab To Be Returned sebagai anchor permukaan; klik `Event Log` dan modalnya (TC-FA-TAG-108 butir b) sesudahnya.
- Row action Pair TAG diamati pada baris Not Paired Yet di Popup Detail Plant A, sehingga `Show` di samping `Not Paired Yet` diklik lebih dulu.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-105 butir c ("Kebab pada aset dengan laporan terbuka tidak memuat Decline Report") tidak punya langkah yang membuka kebab aset itu; spec menambah langkah membuka kebab AST-0020 (aset dengan laporan terbuka pada data TC-174).
  - TC-105 (langkah TC ke-3) membuka kebab aset Not Paired Yet tanpa menyebut filter `Show` di samping `Not Paired Yet`; spec menambah langkah penghubung itu.
