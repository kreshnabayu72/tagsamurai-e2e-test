---
id: TC-AC-DS-E2E-109-download-list-cakupan-baris-kolom-dan-sidebar
title: "Download List: Seluruh Baris, Mengikuti Search dan Filter, Kolom Tampil, dan Sidebar Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-370
  - TC-AC-DS-371
  - TC-AC-DS-372
  - TC-AC-DS-602
coverage:
  web: automated
---

# Download List: Seluruh Baris, Mengikuti Search dan Filter, Kolom Tampil, dan Sidebar Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti; `HHR-ARC-100` dan `HHR-ARC-200` berkategori `UHF Handheld` dan Brand `Arcturus`, Hardware Type `Handheld Reader`) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`. Pohon Category (#25) dibaca untuk Sidebar Category.
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Kemampuan teknis: pembaca berkas unduhan CSV dan XLSX (nama berkas, header kolom, dan jumlah serta kode SKU baris data) disediakan tim FE. Isi sel (nilai, BOM, tipe sel) tidak diasersi di spec ini.
- Preferensi kolom List: langkah 14 dan 19 mengubah visibilitas kolom (tersimpan di cache browser). Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global lain yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-370: Download tanpa Search dan Filter

1. Klik ikon Download
2. Klik `Download as CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi file `Device-SKU.csv` terunduh berisi header dan 129 baris data (bukan hanya 10 baris halaman 1)

### TC-AC-DS-371: Download dengan Search dan Filter aktif

5. Ketik Search `Arcturus`, tekan Enter
6. Klik ikon Filter
7. Pada field Hardware Type pilih `Handheld Reader`
8. Klik `[Apply]`
9. Klik ikon Download
10. Klik `Download as XLSX`
11. Verifikasi file `Device-SKU.xlsx` terunduh berisi header dan 2 baris data: `HHR-ARC-100` dan `HHR-ARC-200`
12. Verifikasi baris di luar kondisi Search dan Filter tidak ikut di file
13. Klik `[Clear Field]`, lalu `[Apply]`, lalu klik `(←)` pada kotak Search

### TC-AC-DS-372: Download mengikuti kolom yang tampil

14. Klik header kolom Actions (⋯), lalu hilangkan centang `Brand` dan `Model/Type` pada Overlay Column Visibility
15. Klik ikon Download
16. Klik `Download as CSV`
17. Verifikasi tidak ada toast atau peringatan tentang kolom yang tidak ikut
18. Verifikasi file pertama tidak memuat kolom Brand dan Model/Type
19. Klik header kolom Actions (⋯), lalu centang kembali `Brand` dan `Model/Type`
20. Klik ikon Download
21. Klik `Download as CSV`
22. Verifikasi file kedua memuat kembali kolom Brand dan Model/Type

### TC-AC-DS-602: Download mengikuti node Sidebar Category

23. Klik node `UHF Handheld` pada Sidebar Category
24. Klik ikon Download
25. Klik `Download as CSV`
26. Verifikasi tidak ada toast sukses
27. Verifikasi file `Device-SKU.csv` terunduh berisi header dan 2 baris data: `HHR-ARC-100` dan `HHR-ARC-200`
28. Verifikasi SKU berkategori lain tidak ikut di file

## Notes

- Langkah penghubung (S-03): langkah 13 melepas Filter dan Search; tanpa asersi.
- Asersi absence toast pada langkah 3, 17, dan 26 diletakkan segera setelah pemicu dan sebelum asersi berkas terunduh (8b butir 11); berkas terunduh menjadi anchor positifnya.
- Langkah 12 dan 28 adalah asersi atas berkas yang sama dengan langkah 11 dan 27 (anchor positif: baris yang seharusnya ada sudah teramati).
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 dan total 129 baris. Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - TC-AC-DS-372 tidak menyebut cara membaca isi kolom berkas; spec memakai pembaca berkas yang disediakan tim FE (S-13).
  - TC-AC-DS-602 tidak menyebut cara memilih node "semua" sesudahnya; keadaan Sidebar direset oleh hook `beforeEach` suite pada spec berikutnya.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
