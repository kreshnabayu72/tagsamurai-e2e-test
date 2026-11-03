---
id: TC-AC-CS-E2E-153-changelog-pagination-dan-download
title: "Changelog: Pagination dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-428
  - TC-AC-CS-429
coverage:
  web: automated
---

# Changelog: Pagination dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #84 (Changelog Client Subscription berisi 24 entri contoh PRD §4.1.2 dengan Action Edit, Activate, Cancel, Renew, Add Subscription, Resubmit, Timeout Auto-Cancel, Cancel Request, Scheduled Flip Auto-Cancel, Convert, dan Schedule Renewal, Modified By `Fajar N`, `Dewi A`, `Rina P`, `Hendra W`, `Maya T`, `Budi S`, dan `System`) bersifat baca-saja; spec tidak menulis entri Changelog. Changelog adalah audit trail permanen: asersi posisi atau urutan memakai entri seed #84 pada keadaan yang dipulihkan baseline automation sebelum tiap spec (Catatan TC; S-14).
- Changelog, Activity Log, dan System Log adalah audit trail permanen: spec ini tidak menulis entri dan tidak mengasersi total entri sebagai angka absolut (S-12).
- Kemampuan membaca berkas unduhan (nama berkas, jumlah baris data) dan jumlah total entri Changelog Client Subscription (N) disediakan tim FE/BE; N dibaca di hook `before`.
- Jumlah entri minimum yang dibutuhkan run: N lebih dari 100 (sedikitnya 101), sesuai Precondition TC-AC-CS-428, agar page size 25, 50, dan 100 memberi baris per halaman sama dengan page size itu dan halaman `2` tersedia pada tiap iterasi langkah 3 sampai 5. Seed #84 hanya 24 entri; baseline automation menambah entri sampai N terpenuhi lewat kemampuan FE/BE, bila tidak run dihentikan di hook `before` dan dilaporkan (lihat Temuan untuk QA).
- Tabel "Page size" (TC-AC-CS-428): `25`, `50`, `100`.

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-AC-CS-428: Pagination Modal Changelog default 10 dengan pilihan 10, 25, 50, 100

2. Verifikasi Pagination Modal Changelog default 10 baris per halaman
3. Untuk setiap baris tabel "Page size" (langkah 3 sampai 5): pindah ke halaman `2`, buka Overlay page size, lalu pilih page size itu
4. Verifikasi jumlah baris per halaman berubah sesuai page size itu
5. Verifikasi tabel kembali ke halaman 1
6. Buka Overlay page size dan pilih `10`

### TC-AC-CS-429: Download Changelog mengikuti Search dan Filter dengan filename Changelog-Client-Subscription

7. Ketik Search `reject`, tekan Enter
8. Verifikasi tabel menampilkan sedikitnya satu entri
9. Klik ikon Download lalu pilih `Download as CSV`
10. Verifikasi tidak ada toast sukses
11. Verifikasi berkas bernama `Changelog-Client-Subscription.csv` terunduh
12. Verifikasi berkas memuat sedikitnya satu baris data
13. Verifikasi berkas hanya memuat entri yang cocok dengan keyword `reject`
14. Klik `(←)` pada kotak Search

## Notes

- TC-AC-CS-419 sampai 421 (sort Changelog) ada di spec 108.
- Langkah berulang per page size: langkah 3 sampai 5 (tiga iterasi); parameter iterasi ada di tabel `## Prerequisites`, tanpa langkah bersyarat.
- Asersi absence toast sukses (TC-AC-CS-429) mengikuti bagian 8b butir 11: pemicu klik Download dan `Verifikasi` berkas terunduh menjadi anchor positif; ini bukan absence log (S-05).
- Temuan untuk QA:
  - TC-AC-CS-428 Precondition menyebut lebih dari 100 entri (spec memakai N lebih dari 100 sebagai prasyarat, lihat `## Prerequisites`), sedangkan seed #84 hanya berisi 24 entri; dengan 24 entri pilihan page size 25, 50, dan 100 menampilkan semua entri pada satu halaman sehingga jumlah baris yang diasersi bergantung pada jumlah entri nyata.
  - TC-AC-CS-428 Expected b tidak memuat langkah pindah halaman sebelum mengganti page size; spec menambah langkah pindah ke halaman 2 agar "kembali ke halaman 1" teramati (S-14).
  - TC-AC-CS-429 Expected b hanya menyebut entri yang cocok dengan keyword tanpa menyebut Filter; Filter tidak dipakai di Langkah Uji.
