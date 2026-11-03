---
id: TC-FA-TAG-E2E-011-popup-detail-tombol-show-reported-non-standard-dan-not-paired-bagian-2
title: "Popup Detail: Interaksi Show Reported dengan Not Paired Yet, Reset Saat Ditutup, dan Terpisah dari Search dan Filter"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-56
  - TC-FA-TAG-57
  - TC-FA-TAG-58
  - TC-FA-TAG-1450
coverage:
  web: automated
---

# Popup Detail: Interaksi Show Reported dengan Not Paired Yet, Reset Saat Ditutup, dan Terpisah dari Search dan Filter

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

- Data grup Laptop Pro 14 / HQ: Reported 1 (satu aset dengan laporan terbuka), Not Paired Yet 2 (TAG Code `—`, Asset Status `Not Paired Yet`, row action `Pair TAG`).
- Data grup Excavator 20 Ton / Plant B (20 aset): lima aset acuan `AST-0011`, `AST-0020`, `AST-0021`, `AST-0043`, `AST-0044`; Non-standard 5 aset.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.

## Test Steps

### TC-FA-TAG-56: Show Reported atau Non-standard aktif menyembunyikan aset Not Paired Yet

1. Klik Asset Name `Laptop Pro 14` pada baris HQ
2. Klik `Show` di samping `Reported`
3. Verifikasi tabel hanya memuat satu aset dengan laporan terbuka
4. Verifikasi dua aset Not Paired Yet tidak tampil

### TC-FA-TAG-1450: Tombol Show Not Paired Yet dan Reported hanya satu yang aktif pada satu waktu

5. Amati kedua tombol dan tabel
6. Verifikasi tombol `Reported` berlabel `Close`
7. Verifikasi tombol `Not Paired Yet` tetap berlabel `Show`
8. Verifikasi aset Not Paired Yet tidak tampil di tabel
9. Klik `Show` di samping `Not Paired Yet`
10. Amati kedua tombol dan tabel
11. Verifikasi tombol `Reported` kembali berlabel `Show`
12. Verifikasi tombol `Not Paired Yet` berlabel `Close`
13. Verifikasi tabel hanya menampilkan aset Not Paired Yet dengan kolom TAG Code `—`, Asset Status `Not Paired Yet`, dan row action `Pair TAG`

### TC-FA-TAG-57: Menutup Popup Detail mereset penyaringan Show

14. Tutup popup dengan ikon close, lalu klik Asset Name `Excavator 20 Ton` pada baris Plant B
15. Klik `Show` di samping `Reported`
16. Tutup popup dengan ikon close
17. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
18. Verifikasi tombol `Reported` berlabel `Show`
19. Verifikasi tabel memuat 20 aset

### TC-FA-TAG-58: Penyaringan Show terpisah dari Search dan Filter Panel

20. Klik `Show` di samping `Non-standard`
21. Periksa Search dan Filter Panel pada Table Tools popup
22. Verifikasi Search tidak terisi
23. Verifikasi Filter Panel tidak menampilkan indikator filter aktif
24. Verifikasi tabel popup tetap terfilter oleh Show
25. Tutup popup dengan ikon close

## Notes

- Langkah 5, 10, 14 (bagian menutup popup), 16, 21, dan 25 adalah langkah penghubung atau pengamatan tanpa asersi (S-03, S-09).
- Pembagian aksi antar TC (urutan TC diubah: TC-FA-TAG-1450 diletakkan tepat sesudah TC-FA-TAG-56 karena memakai popup Laptop Pro 14 / HQ dengan `Show` `Reported` yang sama): langkah 1 dan 2 TC-FA-TAG-1450 (buka popup dan klik `Show` `Reported`) identik dengan langkah 1 dan 2 TC-FA-TAG-56 dan dijalankan sekali pada langkah 1 dan 2.
- Langkah 4 dan 8 adalah asersi absence atas baris tabel; anchor positif adalah Verifikasi satu aset Reported tampil (langkah 3) dan Verifikasi label tombol (langkah 6) pada popup yang sama (bagian 8b butir 2).
- Langkah 22 dan 23 adalah asersi absence atas isi Search dan indikator Filter; anchor positif adalah Verifikasi tabel popup tetap terfilter (langkah 24) dan Popup Detail yang sudah termuat.
- TC-FA-TAG-50 sampai 55 ada di spec 010.
- Temuan untuk QA:
  - TC-FA-TAG-58 Langkah 3 ("Search dan Filter Panel pada Table Tools halaman") ambigu: popup Detail menutupi Table Tools halaman dan tabel T-TAG-02 punya Table Tools sendiri. Spec memeriksa Table Tools popup; mohon QA mengonfirmasi.
  - TC-FA-TAG-57 tidak menyebut jumlah baris yang tampil per halaman saat "20 aset"; spec mengasersi jumlah total aset 20 dan menyerahkan cara pengamatan ke tahap script.
  - Nama dan kode literal Pre-setup tidak diberi suffix karena TC menuntut asersi nama, urutan, dan jumlah, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
