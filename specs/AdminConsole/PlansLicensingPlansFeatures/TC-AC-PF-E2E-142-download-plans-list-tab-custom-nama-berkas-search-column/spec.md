---
id: TC-AC-PF-E2E-142-download-plans-list-tab-custom-nama-berkas-search-column
title: Download Plans List Tab Custom Nama Berkas, Search, Column Visibility, dan Hasil Kosong
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-365
  - TC-AC-PF-401
  - TC-AC-PF-404
  - TC-AC-PF-405
  - TC-AC-PF-406
coverage:
  web: automated
---

# Download Plans List Tab Custom Nama Berkas, Search, Column Visibility, dan Hasil Kosong

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier` (FAMS, v2, Clients 12), `Beta Pro` (SAMS, v10, 7), `Growth Tier` (FAMS, v20, 1), `Zeta Max` (SIEM, v3, 0); archived `Arsip Custom Satu` dan `Arsip Custom Dua`; semuanya Paid.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Kemampuan membaca berkas CSV dan XLSX yang terunduh (jumlah baris dan header) disediakan tim FE/BE. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: kolom `Version` disembunyikan lalu ditampilkan kembali (langkah 15 dan 20); preferensi kolom browser dihapus di hook `after` (kemampuan disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-401 Overlay dan nama berkas

2. Hover ikon Download.
3. Verifikasi tooltip ikon `Download` tampil.
4. Klik ikon Download.
5. Verifikasi overlay memuat `Download as CSV` dan `Download as XLSX`.
6. Pilih `Download as CSV`.
7. Verifikasi tidak ada toast sukses.
8. Verifikasi berkas CSV terunduh bernama `Plans-Features-Custom.csv`.
9. Klik ikon Download lagi, pilih `Download as XLSX`.
10. Verifikasi berkas XLSX terunduh bernama `Plans-Features-Custom.xlsx` (ekstensi mengikuti pilihan).

### TC-AC-PF-404 Download mengikuti Search

11. Ketik Search `tier`, tekan Enter.
12. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
13. Verifikasi berkas hanya memuat `alpha Tier` dan `Growth Tier` hasil Search.
14. Kosongkan isi kotak search, tekan Enter.

### TC-AC-PF-405 Download mengikuti Column Visibility

15. Sembunyikan kolom `Version` lewat Overlay Column Visibility.
16. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
17. Verifikasi tidak ada toast atau dialog peringatan.
18. Verifikasi header berkas tidak memuat kolom `Version`.
19. Verifikasi kolom lain yang tampil ikut diekspor.
20. Tampilkan kembali kolom `Version` lewat Overlay Column Visibility.

### TC-AC-PF-406 Hasil kosong

21. Ketik Search `zzzzz`, tekan Enter.
22. Verifikasi tombol Download tetap aktif.
23. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
24. Verifikasi tidak ada toast sukses.
25. Verifikasi berkas hanya berisi baris header kolom yang tampil tanpa baris data.
26. Kosongkan isi kotak search, tekan Enter.

### TC-AC-PF-365 Download sub-tab Custom Archive

27. Klik sub-tab Archive.
28. Klik ikon Download, pilih `Download as XLSX`, lalu buka berkas.
29. Verifikasi tidak ada toast sukses.
30. Verifikasi berkas bernama `Plans-Features-Custom.xlsx`.
31. Verifikasi berkas memuat dua baris custom plan archived.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 14 dan 26 mengosongkan Search; langkah 15 dan 20 menyembunyikan serta menampilkan kembali kolom `Version`.
- Verifikasi "tidak ada toast sukses" ditempatkan segera setelah pemicu download dan sebelum asersi berkas (bagian 8b butir 11).
- Langkah 7 tanpa pengulangan untuk XLSX: Expected TC-AC-PF-401 butir b menyebut "tidak ada toast sukses" satu kali untuk kedua unduhan.
- Jumlah langkah 31: di bawah ambang sekitar 35.
