---
id: TC-FA-TAG-E2E-379-screening-halaman-tag-tab-paired-tanpa-tombol-create-atau-delete-data-tag
title: "Halaman TAG Tanpa Tombol Create atau Delete Data Tag"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-13
coverage:
  web: automated
---

# Halaman TAG Tanpa Tombol Create atau Delete Data Tag

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab Paired (dipakai TC-FA-TAG-13; hanya dibaca, tidak diubah):

  | Asset Name | Group | TAG Type | Total Assets | Reported | Non-standard | Not Paired Yet |
  |---|---|---|---|---|---|---|
  | Excavator 20 Ton | Plant A | RFID | 20 | 0 | 0 | 2 |
  | Excavator 20 Ton | Plant B | RFID | 20 | 2 | 5 | 0 |
  | Laptop Pro 14 | HQ | NFC, QR | 25 | 1 | 0 | 2 |
  | Forklift Manual | Plant A | Non TAG | 10 | 0 | 3 | 0 |

- Tab To Be Returned memuat Tag `RF-00071`, `RF-00088`, dan `NF-00092` (dipakai TC-FA-TAG-13 sebagai baris yang dibuka kebab aksinya).
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.

## Test Steps

### TC-FA-TAG-13: Halaman TAG tidak memiliki tombol Create atau Delete data Tag

1. Periksa Table Tools tab Paired
2. Verifikasi Table Tools tab Paired memuat `Search`, `Filter`, `Download`, `Changelog`, `Print QR`, `Replace TAG`
3. Verifikasi tidak ada tombol Create dan tidak ada aksi Delete pada Table Tools tab Paired
4. Klik kebab di ujung baris pertama tabel grup
5. Verifikasi kebab aksi grup memuat aksi `Detail`
6. Verifikasi kebab aksi grup tidak memuat aksi Delete
7. Tekan Esc untuk menutup kebab
8. Klik Asset Name pada baris pertama tabel grup untuk membuka Popup Detail
9. Verifikasi Popup Detail tampil dengan judul `Assets`
10. Klik kebab row action pada baris pertama tabel T-TAG-02
11. Verifikasi row action memuat sedikitnya satu aksi
12. Verifikasi row action tidak memuat aksi Delete
13. Tekan Esc untuk menutup menu row action
14. Centang checkbox baris pertama tabel T-TAG-02
15. Verifikasi Bulk Action Bar tampil
16. Verifikasi Bulk Action Bar tidak memuat aksi Delete
17. Klik `Unselect All` pada Bulk Action Bar
18. Klik ikon close pada Popup Detail
19. Klik Tab `To Be Returned`
20. Verifikasi Table Tools tab To Be Returned memuat `Search`, `Filter`, `Download`, `Event Log`, `Receive TAG`
21. Verifikasi tidak ada tombol Create dan tidak ada aksi Delete pada Table Tools tab To Be Returned
22. Klik kebab row action pada baris pertama tabel To Be Returned
23. Verifikasi row action memuat sedikitnya satu aksi
24. Verifikasi row action tidak memuat aksi Delete
25. Tekan Esc untuk menutup menu row action
26. Centang checkbox baris pertama tabel To Be Returned
27. Verifikasi Bulk Action Bar tampil
28. Verifikasi Bulk Action Bar tidak memuat aksi Delete
29. Klik `Unselect All` pada Bulk Action Bar

## Notes

- Langkah 7, 13, 17, 18, 25, dan 29 adalah langkah penghubung (menutup menu, melepas seleksi, menutup Popup Detail), tanpa asersi (S-03). Langkah 1 dan 4 mengikuti langkah 1 TC-FA-TAG-13 per permukaan yang diperiksa.
- Langkah 3, 6, 12, 16, 21, 24, dan 28 adalah asersi absence atas elemen UI; anchor positif adalah Verifikasi elemen lain pada permukaan yang sama tepat sebelumnya (langkah 2, 5, 9 dan 11, 15, 20, 23, 27) (bagian 8b butir 2).
- TC-FA-TAG-1 sampai 3 ada di spec 001, TC-FA-TAG-4 sampai 7 ada di spec 018, dan TC-FA-TAG-8 sampai 12 ada di spec 002.
- Temuan untuk QA:
  - TC-FA-TAG-13 menyebut "Bulk Action" tetapi Bulk Action Bar baru tampil setelah baris dicentang; spec mencentang baris pertama untuk memunculkannya. Isi aksi row action Popup Detail dan tab To Be Returned tidak disebut di TC ini, sehingga spec hanya mengasersi "sedikitnya satu aksi" sebagai anchor.
  - Nama dan kode literal Pre-setup tidak diberi suffix karena TC menuntut asersi nama, urutan, dan jumlah, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
