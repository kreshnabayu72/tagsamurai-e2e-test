---
id: TC-FA-TAG-E2E-009-popup-detail-assets-screening-buka-dan-tutup
title: "Screening Popup Detail Assets: Cara Buka dan Tutup serta Blok Info Reported, Non-standard, dan Not Paired Yet"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-42
  - TC-FA-TAG-43
  - TC-FA-TAG-44
  - TC-FA-TAG-45
  - TC-FA-TAG-46
  - TC-FA-TAG-47
  - TC-FA-TAG-48
  - TC-FA-TAG-49
coverage:
  web: automated
---

# Screening Popup Detail Assets: Cara Buka dan Tutup serta Blok Info Reported, Non-standard, dan Not Paired Yet

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab Paired (hanya dibaca, tidak diubah):

  | Asset Name | Group | TAG Type | Total Assets | Reported | Non-standard | Not Paired Yet |
  |---|---|---|---|---|---|---|
  | Excavator 20 Ton | Plant A | RFID | 20 | 0 | 0 | 2 |
  | Excavator 20 Ton | Plant B | RFID | 20 | 2 | 5 | 0 |
  | Laptop Pro 14 | HQ | NFC, QR | 25 | 1 | 0 | 2 |
  | Forklift Manual | Plant A | Non TAG | 10 | 0 | 3 | 0 |

- Data grup Excavator 20 Ton / Plant B (20 aset): lima aset acuan `AST-0011` (Excavator 20 Ton - 11), `AST-0020` (- 20), `AST-0021` (- 21), `AST-0043` (- 43), `AST-0044` (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.

## Test Steps

### TC-FA-TAG-42: Screening Popup Detail grup Excavator 20 Ton / Plant B

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Amati popup dari atas ke bawah
3. Verifikasi judul `Assets` (flat, tanpa nama record)
4. Verifikasi ikon close di pojok kanan atas dan tidak ada tombol teks `Close` di footer
5. Verifikasi blok info grid `Label: Value` 3 kolom berurutan: `Asset Name: Excavator 20 Ton`, `TAG Type: RFID`, `Total Assets: 20`
6. Verifikasi `Reported: 2` berupa badge danger dengan tombol `Show`
7. Verifikasi `Non-standard: 5` berupa badge warning dengan tombol `Show`
8. Verifikasi `Not Paired Yet: 0` berupa teks tanpa tombol
9. Verifikasi tabel T-TAG-02 dengan kolom default berurutan `Name (sortable)`, `Asset ID (sortable)`, `TAG Code (sortable)`, `Brand (sortable)`, `Model/Type (sortable)`, `Group (sortable)`, `Status (sortable)`, `Last Updated (sortable)`, `Column Visibility (⋯)`
10. Verifikasi satu baris per aset: 20 baris total, pagination menampilkan 10 baris pertama
11. Verifikasi Bulk Action Bar belum tampil
12. Verifikasi checkbox seleksi per baris tersedia
13. Verifikasi Pagination page size 10 / 25 / 50 / 100
14. Verifikasi urutan awal Last Updated terbaru di atas

### TC-FA-TAG-46: Klik backdrop tidak menutup Popup Detail

15. Klik area gelap di luar popup
16. Verifikasi popup tetap terbuka
17. Tekan Esc
18. Verifikasi popup tertutup

### TC-FA-TAG-43: Klik Asset Name membuka Popup Detail

19. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
20. Verifikasi Popup Detail terbuka di atas tab Paired tanpa pindah halaman
21. Verifikasi Breadcrumb `Fixed Asset > TAG > Paired` tidak berubah

### TC-FA-TAG-45: Menutup Popup Detail lewat ikon close

22. Klik ikon close pada popup
23. Verifikasi popup tertutup
24. Verifikasi tab Paired tampil kembali dengan empat baris grup

### TC-FA-TAG-44: Aksi grup Detail membuka Popup Detail

25. Klik kebab di ujung baris Excavator 20 Ton / Plant B
26. Verifikasi kebab memuat aksi `Detail` dengan ikon `FileInfoLine`
27. Klik aksi `Detail`
28. Verifikasi Popup Detail terbuka dengan judul `Assets` dan Asset Name `Excavator 20 Ton`

### TC-FA-TAG-47: Blok info Popup Detail menampilkan tombol Show hanya pada angka lebih dari nol

29. Tutup popup dengan ikon close, lalu klik Asset Name `Excavator 20 Ton` pada baris Plant B
30. Verifikasi `Reported: 2` dan `Non-standard: 5` diikuti tombol teks `Show` (severity primary, size sm)
31. Verifikasi `Not Paired Yet: 0` tampil sebagai teks tanpa tombol

### TC-FA-TAG-48: Blok info Popup Detail grup tanpa Reported dan Non-standard menampilkan angka nol tanpa tombol

32. Tutup popup dengan ikon close, lalu klik Asset Name `Laptop Pro 14` pada baris HQ
33. Verifikasi `Non-standard: 0` tampil sebagai teks tanpa tombol `Show` dan tanpa badge warning
34. Verifikasi `Reported: 1` dan `Not Paired Yet: 2` masing-masing diikuti tombol `Show`
35. Verifikasi `TAG Type` berisi badge atau ikon NFC dan QR

### TC-FA-TAG-49: Popup Detail Asset Name Non-TAG menampilkan TAG Type berupa badge Non TAG

36. Tutup popup dengan ikon close, lalu klik Asset Name `Forklift Manual` pada baris Plant A
37. Verifikasi field `TAG Type` pada blok info berupa badge `Non TAG`
38. Verifikasi `Non-standard: 3` diikuti tombol `Show`
39. Tutup popup dengan ikon close

## Notes

- Langkah 2 adalah langkah penghubung (mengamati popup), tanpa asersi (S-03). Langkah 29, 32, 36, dan 39 menutup popup sebelum TC berikutnya (S-09); penutupan pada langkah 29, 32, dan 36 digabung dalam langkah pembuka TC berikutnya.
- Urutan TC pada spec: TC-FA-TAG-42, 46, 43, 45, 44, 47, 48, 49. TC-FA-TAG-46 diletakkan tepat sesudah TC-FA-TAG-42 agar popup yang sudah terbuka dipakai, dan TC-FA-TAG-45 sesudah TC-FA-TAG-43 agar popup yang dibuka langkah 19 langsung ditutup; keduanya tidak mengubah isi TC.
- Langkah 8 dan 31 memuat klausa "tanpa tombol" sebagai asersi absence atas elemen UI; anchor positif adalah Verifikasi `Reported` dan `Non-standard` dengan tombol `Show` pada popup yang sama (langkah 6, 7, 30) (bagian 8b butir 2). Langkah 33 memakai Verifikasi `Reported` dan `Not Paired Yet` pada langkah 34 sebagai pembanding pada popup yang sama.
- Spec ini melewati sekitar 35 langkah (39). Alasan: seluruh blok screening Popup Detail berkelas sama (fungsional, hanya membaca data Pre-setup yang sama) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan blok TC-FA-TAG-42 sendiri memuat 12 Verifikasi dari Expected TC yang tidak dapat diringkas tanpa menggabungkan klausa.
- TC-FA-TAG-50 sampai 55 ada di spec 010.
- Temuan untuk QA:
  - TC-FA-TAG-42 Expected b menyebut "Bulk Action Bar belum tampil" sebagai satu klausa tanpa langkah yang memicunya; spec hanya mengasersi bahwa bar belum tampil sebelum ada seleksi.
  - Nama dan kode literal Pre-setup tidak diberi suffix karena TC menuntut asersi nama, urutan, dan jumlah, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
