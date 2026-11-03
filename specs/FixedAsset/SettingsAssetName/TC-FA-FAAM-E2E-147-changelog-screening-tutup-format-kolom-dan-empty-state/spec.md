---
id: TC-FA-FAAM-E2E-147-changelog-screening-tutup-format-kolom-dan-empty-state
title: "Modal Changelog: Screening, Tutup Hanya [✕] atau Esc, Format Kolom, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-462
  - TC-FA-FAAM-463
  - TC-FA-FAAM-464
  - TC-FA-FAAM-465
  - TC-FA-FAAM-467
coverage:
  web: automated
---

# Modal Changelog: Screening, Tutup Hanya [✕] atau Esc, Format Kolom, dan Empty State

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28) berisi entri Create, Edit, dan Delete oleh Sarah Johnson, David Kurniawan, dan Michael Wijaya, bertanggal berbeda-beda; rentang tanggal seed ada di `changelogSeed.dateRange`. Seed memuat sedikitnya satu entri Old Value atau New Value berupa daftar panjang. Jumlah total entri Changelog tidak diasersi sebagai angka absolut karena audit trail permanen (S-12); halaman pertama tanpa Filter memuat sedikitnya dua entri dengan Date (menit) berbeda.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: tidak ada yang diubah. Spec ini tidak menyimpan konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-462: Screening Modal Changelog: Asset Name

1. Klik icon Changelog
2. Verifikasi title `Changelog: Asset Name`
3. Verifikasi icon `[✕]` tampil di header modal
4. Verifikasi toolbar `Search | Filter | Download` tampil
5. Verifikasi kolom `Date (sortable) | Action (sortable) | Asset Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯)`
6. Verifikasi sedikitnya dua baris entri tampil pada tabel Changelog
7. Verifikasi default sort Date Newest First: baris halaman pertama urut Date dari terbaru ke terlama
8. Verifikasi format Modified By `[First Name] [Last Initial]` pada setiap baris halaman pertama
9. Verifikasi footer pagination default 10 data per halaman
10. Klik dropdown page size
11. Verifikasi pilihan page size `10`, `25`, `50`, `100`
12. Pilih `10`
13. Terapkan Filter Date rentang seed (`Fixture.faAssetName.changelogSeed.dateRange`): klik icon Filter, pilih rentang tanggal, klik `[Apply]`

### TC-FA-FAAM-464: Format kolom Changelog: Action plain text, Old/New Value plain text, Modified By singkat

14. Verifikasi Action `Create`, `Edit`, dan `Delete` tampil sebagai plain text tanpa badge
15. Verifikasi baris Create: Old Value `—`
16. Verifikasi baris Delete: New Value `—`
17. Verifikasi Old Value dan New Value tampil sebagai plain text
18. Verifikasi Modified By `Sarah J`
19. Arahkan kursor ke Modified By `Sarah J`
20. Verifikasi tooltip `Sarah Johnson`

### TC-FA-FAAM-465: Old Value dan New Value panjang wrap tanpa truncation dan tanpa tooltip

21. Verifikasi teks Old Value dan New Value pada entri berdaftar panjang wrap natural
22. Verifikasi teks Old Value dan New Value pada entri berdaftar panjang tidak dipotong dengan `..`
23. Arahkan kursor ke teks Old Value pada entri berdaftar panjang
24. Verifikasi tidak ada tooltip

### TC-FA-FAAM-467: Search atau Filter Changelog tanpa hasil menampilkan no results

25. Ketik Search `zzzz`, tekan Enter
26. Verifikasi empty state dengan title `No results found`, dan deskripsi `Try adjusting your search or filter.`
27. Klik `(←)` pada kotak Search

### TC-FA-FAAM-463: Modal Changelog ditutup hanya lewat [✕] atau Esc; klik backdrop diabaikan

28. Klik area gelap di luar modal Changelog
29. Verifikasi modal Changelog tetap tampil dengan title `Changelog: Asset Name`
30. Tekan Esc
31. Verifikasi Table Tools halaman Asset Name tampil
32. Verifikasi modal Changelog tertutup

## Notes

- Urutan di spec: modal dibuka sekali (langkah 1) dan TC-FA-FAAM-462, 464, 465, 467 dijalankan di modal yang sama; TC-FA-FAAM-463 paling akhir karena menutup modal (S-10). Urutan ini berbeda dari urutan nomor TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): memilih `10` menutup dropdown page size (langkah 12), Filter Date rentang seed supaya halaman teramati memuat entri seed bertanggal berbeda dan beragam Action (langkah 13, S-14), dan mengosongkan Search sebelum modal ditutup (langkah 27).
- Asersi absence pada langkah 24 (tidak ada tooltip) beranchor hover di langkah 23 sebagai pemicu; langkah 22 beranchor teks yang tampil di langkah 21. Asersi modal tertutup pada langkah 32 beranchor Table Tools halaman tampil (langkah 31).
- Pembagian TC lintas spec: TC-FA-FAAM-466 (Changelog kosong pada client lain) ada di spec 165; TC-FA-FAAM-469 di spec 157.
- Temuan untuk QA:
  - TC-FA-FAAM-465 butuh entri Old Value atau New Value berdaftar panjang, tetapi Pre-setup #28 tidak merinci nilainya; spec mengandalkan seed yang disediakan tim BE.
  - TC-FA-FAAM-462 Expected e (default sort) hanya dapat diasersi sebagai urutan antarbaris bila halaman pertama memuat dua nilai Date (menit) berbeda; TC tidak menjamin hal itu pada audit trail yang tumbuh (S-14).
  - TC-FA-FAAM-466 memuat ACC `#16`, sedangkan Precondition menyebut `#16b` (lihat spec 165).
