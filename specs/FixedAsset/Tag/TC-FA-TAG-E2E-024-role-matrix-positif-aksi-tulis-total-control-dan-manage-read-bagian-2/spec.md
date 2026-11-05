---
id: TC-FA-TAG-E2E-024-role-matrix-positif-aksi-tulis-total-control-dan-manage-read-bagian-2
title: "Role Matrix Positif: Aksi Tulis Total Control dan Manage asset & TAG (Read + Update) (Bagian 2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-117
  - TC-FA-TAG-118
  - TC-FA-TAG-119
  - TC-FA-TAG-120
coverage:
  web: automated
---

# Role Matrix Positif: Aksi Tulis Total Control dan Manage asset & TAG (Read + Update) (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) | MU | `manageAssetTagReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Data: Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan AST-0011 (Excavator 20 Ton - 11), AST-0020 (Excavator 20 Ton - 20), AST-0021 (Excavator 20 Ton - 21), AST-0043 (Excavator 20 Ton - 43), AST-0044 (Excavator 20 Ton - 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011.
- Data: Pre-setup Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.); akun memegang Update pada Disposal Center.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
2. Klik kebab baris aset ber-Tag AST-0011
3. Verifikasi kebab AST-0011 memuat `Replace TAG`
4. Tutup menu kebab (Esc)
5. Centang dua aset ber-Tag normal (AST-0011 dan AST-0021)
6. Verifikasi Bulk Action Bar tampil dengan aksi `Batch Replace TAG` (ikon `ReplaceTag`, dark)
7. Tutup Popup Detail
8. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
9. Klik `Show` di samping `Not Paired Yet`
10. Klik kebab baris aset Not Paired Yet
11. Verifikasi kebab aset Not Paired Yet memuat `Pair TAG`
12. Tutup Popup Detail
13. Klik Tab `To Be Returned`
14. Verifikasi tombol scan `Receive TAG` tampil di ujung kanan setelah `Event Log`
15. Klik kebab baris RF-00071
16. Verifikasi kebab baris RF-00071 memuat `Receive Manually`
17. Tutup menu kebab (Esc)
18. Centang baris RF-00071
19. Verifikasi Bulk Action Bar memuat `Receive Manually`
20. Verifikasi tombol `Event Log` tampil (Show)
21. Klik tombol `Event Log`
22. Verifikasi modal `Event Log: To Be Returned` terbuka

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 4, 7, 9, 12, 17.
- Pembagian TC lintas spec: TC-FA-TAG-97 sampai 102, 115, dan 116 ada di spec `TC-FA-TAG-E2E-023-role-matrix-positif-aksi-tulis-total-control-dan-manage-read-bagian-1`.
- Urutan TC-FA-TAG-117 dan TC-FA-TAG-118 disusun ulang (Popup Detail Plant B dahulu, lalu Plant A) supaya popup tidak dibuka dua kali; Expected tiap TC tetap diasersi.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-117 sampai TC-120 memakai Role `Manage asset & TAG (Read + Update)` tanpa menyebut group Update, sedangkan TC-119 mensyaratkan akses Update pada Disposal Center; spec menganggap akun itu memegang Update pada Plant A, Plant B, dan Disposal Center.
  - TC-117 (langkah TC ke-3) membuka kebab aset Not Paired Yet tanpa menyebut filter `Show` di samping `Not Paired Yet`; spec menambah langkah penghubung itu.
