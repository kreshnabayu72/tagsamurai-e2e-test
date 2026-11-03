---
id: TC-FA-TAG-E2E-001-screening-halaman-tag-tab-paired-breadcrumb-dan-tooltip-toolbar-bagian-1
title: "Screening Halaman TAG Tab Paired: Header, Kartu, Table Tools, Tabel Grup, Breadcrumb, dan Tab Awal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1
  - TC-FA-TAG-2
  - TC-FA-TAG-3
coverage:
  web: automated
---

# Screening Halaman TAG Tab Paired: Header, Kartu, Table Tools, Tabel Grup, Breadcrumb, dan Tab Awal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab Paired (dipakai TC-FA-TAG-1 dan TC-FA-TAG-3; hanya dibaca, tidak diubah):

  | Asset Name | Group | TAG Type | Total Assets | Reported | Non-standard | Not Paired Yet |
  |---|---|---|---|---|---|---|
  | Excavator 20 Ton | Plant A | RFID | 20 | 0 | 0 | 2 |
  | Excavator 20 Ton | Plant B | RFID | 20 | 2 | 5 | 0 |
  | Laptop Pro 14 | HQ | NFC, QR | 25 | 1 | 0 | 2 |
  | Forklift Manual | Plant A | Non TAG | 10 | 0 | 3 | 0 |

- Tab To Be Returned memuat Tag RF-00071, RF-00088, dan NF-00092 (dipakai hanya sebagai latar; spec ini tidak mengasersi isinya).
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Kemampuan teknis: tidak ada selain fixture seeding di atas. Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.

## Test Steps

### TC-FA-TAG-1: Screening halaman TAG tab Paired (Total Control)

1. Amati halaman Fixed Asset > TAG dari atas ke bawah tanpa berinteraksi
2. Verifikasi Breadcrumb `Fixed Asset > TAG > Paired` tampil
3. Verifikasi segmen terakhir Breadcrumb `Paired` bukan link
4. Verifikasi tidak ada Page Title
5. Verifikasi Tab `Paired` (aktif) dan Tab `To Be Returned` tampil
6. Verifikasi Tab `To Be Returned` memuat Badge jumlah Tag
7. Verifikasi kartu filter `Reported`, `Non-standard`, `Not Paired Yet` tampil
8. Verifikasi Table Tools `Search`, `Filter`, `Download`, `Changelog`, `Print QR`, `Replace TAG` tampil
9. Verifikasi `Print QR` berada di kiri `Replace TAG` dan `Replace TAG` berada di ujung kanan
10. Verifikasi tidak ada tombol Create
11. Verifikasi kolom tabel grup berurutan `Asset Name (sortable)`, `Group (sortable)`, `TAG Type (sortable)`, `Total Assets (sortable)`, `Reported (sortable)`, `Non-standard (sortable)`, `Not Paired Yet (sortable)`, `Column Visibility (⋯)`
12. Arahkan pointer ke header kolom terakhir `⋯`
13. Verifikasi tooltip `Column Visibility` tampil
14. Verifikasi body kolom `⋯` pada tiap baris berupa kebab aksi grup
15. Verifikasi empat baris grup tampil sesuai Data Uji
16. Verifikasi Asset Name berupa link
17. Verifikasi Group berupa badge Primary
18. Verifikasi TAG Type berupa ikon per tipe dan badge `Non TAG` untuk Forklift Manual
19. Verifikasi urutan awal Asset Name A-Z: Excavator 20 Ton (dua baris), Forklift Manual, Laptop Pro 14
20. Verifikasi Pagination page size default 10
21. Verifikasi pilihan page size 10 / 25 / 50 / 100

### TC-FA-TAG-2: Breadcrumb halaman TAG pada tab Paired tanpa Page Title

22. Amati area atas halaman
23. Verifikasi Breadcrumb `Fixed Asset > TAG > Paired` tampil
24. Klik segmen terakhir Breadcrumb `Paired`
25. Verifikasi klik tidak berpindah halaman
26. Verifikasi Tab `Paired` tetap aktif
27. Verifikasi tidak ada Page Title Header di halaman

### TC-FA-TAG-3: Tab Paired aktif saat pertama kali masuk halaman TAG

28. Buka menu Fixed Asset > TAG lewat sidebar
29. Verifikasi Tab `Paired` aktif
30. Verifikasi tabel grup T-TAG-01 dan tiga kartu tampil
31. Verifikasi Tab `To Be Returned` tidak aktif

## Notes

- Langkah 22 dan 28 adalah langkah penghubung (mengamati area atas; membuka menu dari sidebar), tanpa asersi (S-03). Halaman TAG sudah dibuka hook `beforeEach` suite untuk TC-FA-TAG-1 dan TC-FA-TAG-2, sehingga langkah "Buka menu Fixed Asset > TAG" pada TC-FA-TAG-1 dan TC-FA-TAG-2 dipenuhi hook; TC-FA-TAG-3 membuka menu lewat sidebar karena objek ujinya adalah tab awal saat masuk.
- Langkah 12 sampai 13 memenuhi klausa "header ⋯ bertooltip `Column Visibility`" dari Expected TC-FA-TAG-1 butir b.i dengan hover; tooltip yang sama diuji sebagai TC sendiri di spec 002.
- TC-FA-TAG-4 sampai 7 ada di spec 018 dan TC-FA-TAG-8 sampai 13 ada di spec 002.
- Temuan untuk QA:
  - TC-FA-TAG-3 Precondition b ("akun belum membuka halaman TAG pada sesi browser ini") tidak dapat dipenuhi bersama hook suite `beforeEach` yang sudah membuka halaman TAG; spec membuka menu dari sidebar dan tidak mengasersi "kunjungan pertama". Mohon QA mengonfirmasi apakah syarat itu relevan bagi Total Control (pembeda dari kunjungan dengan Guided Tooltip).
  - Nama dan kode literal Pre-setup (Excavator 20 Ton, Laptop Pro 14, Forklift Manual) tidak diberi suffix karena TC menuntut asersi nama, urutan, dan jumlah, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
  - TC-FA-TAG-1 Expected b.i menyebut "Column Visibility (⋯)" dengan header bertooltip, sedangkan body kolom itu berupa kebab aksi grup; spec mengikuti TC apa adanya.
