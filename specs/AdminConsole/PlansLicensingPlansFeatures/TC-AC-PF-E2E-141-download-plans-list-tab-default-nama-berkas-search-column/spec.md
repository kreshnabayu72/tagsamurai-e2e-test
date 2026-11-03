---
id: TC-AC-PF-E2E-141-download-plans-list-tab-default-nama-berkas-search-column
title: Download Plans List Tab Default Nama Berkas, Search, Column Visibility, dan Lintas Halaman
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-350
  - TC-AC-PF-353
  - TC-AC-PF-354
  - TC-AC-PF-355
  - TC-AC-PF-361
  - TC-AC-PF-688
coverage:
  web: automated
---

# Download Plans List Tab Default Nama Berkas, Search, Column Visibility, dan Lintas Halaman

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21; default aktif `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`; default archived `Growth Plus (old)`) dan Dataset Plan R (Pre-setup #30; archived `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`) untuk langkah 1 sampai 31. Dataset Plan Z (Pre-setup #38; 12 default aktif bernomor 01 sampai 12, nama literal Pre-setup dipakai di langkah) untuk langkah 32 sampai 35; Dataset Plan A dan Dataset Plan Z menempati slot Free dan Paid per Product yang sama sehingga tidak bersamaan.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal dan berpindah dari Dataset Plan A dan R ke Dataset Plan Z (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before`, `after`, dan pada langkah 32. Kemampuan membaca berkas CSV yang terunduh (jumlah baris dan header) disediakan tim FE/BE. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup selain berpindah dataset lewat fixture BE.
- State sementara: kolom `Version` disembunyikan lalu ditampilkan kembali (langkah 15 dan 20); preferensi kolom browser dihapus di hook `after` (kemampuan disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-350 Overlay dan nama berkas

1. Hover ikon Download.
2. Verifikasi tooltip ikon `Download` tampil.
3. Klik ikon Download.
4. Verifikasi overlay memuat `Download as CSV` dan `Download as XLSX`.
5. Pilih `Download as CSV`.
6. Verifikasi tidak ada toast sukses.
7. Verifikasi berkas CSV terunduh bernama `Plans-Features-Default.csv`.
8. Klik ikon Download lagi, pilih `Download as XLSX`.
9. Verifikasi berkas XLSX terunduh bernama `Plans-Features-Default.xlsx` (ekstensi mengikuti pilihan).

### TC-AC-PF-353 Download mengikuti Search

10. Ketik Search `grow`, tekan Enter.
11. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
12. Verifikasi berkas hanya memuat baris `Growth` hasil Search.
13. Kosongkan isi kotak search, tekan Enter.

### TC-AC-PF-354 Download mengikuti Column Visibility

14. Sembunyikan kolom `Version` lewat Overlay Column Visibility.
15. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
16. Verifikasi tidak ada toast atau dialog peringatan.
17. Verifikasi header berkas tidak memuat kolom `Version`.
18. Verifikasi kolom lain yang tampil ikut diekspor.
19. Tampilkan kembali kolom `Version` lewat Overlay Column Visibility.

### TC-AC-PF-355 Hasil kosong

20. Ketik Search `zzzzz`, tekan Enter.
21. Verifikasi tombol Download tetap aktif.
22. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
23. Verifikasi tidak ada toast sukses.
24. Verifikasi berkas hanya berisi baris header kolom yang tampil tanpa baris data.
25. Kosongkan isi kotak search, tekan Enter.

### TC-AC-PF-361 Download sub-tab Archive

26. Klik sub-tab Archive.
27. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas.
28. Verifikasi tidak ada toast sukses.
29. Verifikasi berkas bernama `Plans-Features-Default.csv`.
30. Verifikasi berkas memuat empat baris plan archived (`Growth Plus (old)`, `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`).
31. Verifikasi berkas tidak memuat plan aktif.

### TC-AC-PF-688 Download lintas halaman

32. Pindah ke Dataset Plan Z lewat fixture BE dan muat ulang halaman Default > Active.
33. Verifikasi footer menampilkan `Showing 1–10 of 12 entries`.
34. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
35. Verifikasi berkas memuat satu baris header dan 12 baris data `Rencana 01` sampai `Rencana 12`, bukan 10.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 13 dan 25 mengosongkan Search; langkah 14 dan 19 menyembunyikan serta menampilkan kembali kolom `Version`; langkah 32 berpindah dataset lewat fixture BE.
- Verifikasi "tidak ada toast sukses" ditempatkan segera setelah pemicu download dan sebelum asersi berkas (bagian 8b butir 11); pemicunya sendiri menjadi anchor positif yang buktinya menyusul pada asersi berkas.
- Langkah 6 tanpa pengulangan untuk XLSX: Expected TC-AC-PF-350 butir b menyebut "tidak ada toast sukses" satu kali untuk kedua unduhan.
- Isi sel berkas (nilai, BOM, tipe sel) diasersi di spec kelas f lain; spec ini hanya nama berkas, jumlah baris, dan header.
- Temuan untuk QA: Dataset Plan A dan Dataset Plan Z saling menggeser slot default plan per Product (1 Free dan 3 Paid), sehingga TC-AC-PF-688 (Dataset Plan Z) tidak dapat memakai Dataset Plan A yang sama dengan TC lain di spec ini.
- Jumlah langkah 35: sekitar ambang 35.
