---
id: TC-FA-TDC-E2E-039-batas-selection-limit-select-all-dan-live-block-checkbox
title: "Batas Selection Limit: Select All Melebihi Batas Memotong Seleksi dan Live-Block Checkbox Baris"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-423
  - TC-FA-TDC-424
sourceRules: ["§3.6#p1", "FATDC-LOGIC-14k"]
smoke: []
dependsOn: []
trace:
  "§3.6#p1": 3
  "FATDC-LOGIC-14k": [4, 17]
anchor: [5, 6, 8, 15, 16]
coverage:
  web: automated
---

# Batas Selection Limit: Select All Melebihi Batas Memotong Seleksi dan Live-Block Checkbox Baris

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; nilainya disediakan tim FE).
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (kelas e, volume data; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): Selection Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits bernilai 100 (nilai minimum); tabel memuat 150 class, yaitu 7 class seed bawaan ditambah 143 class tambahan yang dibuat lewat API pre-setup di hook `before`. Total 150 berasal dari seeding (8b.10).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): mengatur Selection Limit dan membuat 143 class tambahan lewat fixture BE.
- Ukuran halaman: Pagination menyediakan 10 / 25 / 50 / 100 per halaman (PRD, default tabel; FATDC-LOGIC-14l), sehingga 101 baris tidak muat dalam satu halaman. TC-FA-TDC-424 memakai ukuran halaman 100: 100 baris pertama dicentang di halaman 1, baris ke-101 adalah baris pertama halaman 2 dari 150 class. Ukuran halaman awal 10 dipulihkan pada langkah 19.
- Jeda nyata pendek: langkah 7 menunggu 10 detik (di bawah 30 detik) untuk membuktikan toast tidak hilang otomatis; durasi 10 detik adalah pilihan spec karena TC tidak menyebut durasi.
- State global: Selection Limit dan 143 class tambahan. Hook `after` menghapus 143 class tambahan dan memulihkan Selection Limit ke nilai awal.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-423: Select All melebihi Selection Limit

1. Centang checkbox satu baris agar Bulk Action Bar tampil
2. Klik `Select All (150 records)` pada Bulk Action Bar
3. Verifikasi Bulk Action Bar tetap tampil
4. Verifikasi counter Bulk Action Bar bernilai 100
5. Verifikasi seleksi dipotong ke 100 baris pertama
6. Verifikasi toast error "Error, only the first 100 of 150 rows were selected. Narrow your filter to include the rest." tampil
7. Tunggu 10 detik tanpa memuat ulang halaman
8. Verifikasi toast error tidak hilang otomatis
9. Tutup toast error
10. Klik `Unselect All` pada Bulk Action Bar

### TC-FA-TDC-424: Live-block seleksi manual

11. Atur ukuran halaman Pagination ke 100
12. Centang checkbox baris satu per satu sampai 100 baris pada halaman 1 terpilih
13. Pindah ke halaman 2 lewat Pagination
14. Arahkan kursor ke checkbox baris pertama pada halaman 2, yaitu baris ke-101 secara keseluruhan
15. Verifikasi checkbox baris ke-101 Disabled
16. Verifikasi tooltip `You've reached the maximum selection of 100 rows.` tampil saat kursor di atas checkbox
17. Verifikasi counter Bulk Action Bar tetap bernilai 100
18. Klik `Unselect All` pada Bulk Action Bar
19. Kembalikan ukuran halaman Pagination ke 10

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 memunculkan Bulk Action Bar; langkah 9 menutup toast; langkah 10 dan 18 membersihkan seleksi; langkah 11 mengatur ukuran halaman 100, langkah 13 pindah ke halaman 2, dan langkah 19 mengembalikan ukuran halaman ke 10. Langkah 7 adalah jeda pendek 10 detik yang dinyatakan di Prerequisites.
- Langkah 15 dan 16 diasersi sebelum langkah lain mengubah state hover (8b.5).
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control.
  - TC-FA-TDC-423 mengklik `Select All (150 records)` pada Bulk Action Bar tanpa langkah yang memunculkan bar itu; spec menambah langkah penghubung mencentang satu baris (langkah 1).
  - TC-FA-TDC-423 butir b ("tidak hilang otomatis") tidak menyebut durasi toast standar; spec menunggu 10 detik.
  - TC-FA-TDC-424 mencentang 100 baris satu per satu tanpa menyebut ukuran halaman tabel atau cara menjangkau baris ke-101; spec memakai ukuran halaman 100 lalu halaman 2 (langkah 11 sampai 14) dan mengandaikan seleksi manual dipertahankan lintas halaman (PRD hanya menyebut seleksi lintas halaman lewat `Select All`, FATDC-LOGIC-14l). Perlu konfirmasi QA.
