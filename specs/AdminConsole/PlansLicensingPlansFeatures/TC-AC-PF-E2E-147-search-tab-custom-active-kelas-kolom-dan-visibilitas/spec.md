---
id: TC-AC-PF-E2E-147-search-tab-custom-active-kelas-kolom-dan-visibilitas
title: Search Tab Custom Active Kelas Kolom dan Visibilitas Kolom Created By
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-369
  - TC-AC-PF-370
  - TC-AC-PF-371
  - TC-AC-PF-372
coverage:
  web: automated
---

# Search Tab Custom Active Kelas Kolom dan Visibilitas Kolom Created By

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier` (FAMS, v2, Clients 12, 05 Jun 26 09:00, Created By Andi Wijaya), `Beta Pro` (SAMS, v10, 7, 18 Jun 26 14:30, Rina Kusuma), `Growth Tier` (FAMS, v20, 1, 22 Jun 26 08:00, Andi Wijaya), `Zeta Max` (SIEM, v3, 0, 28 Jun 26 16:00, Budi Aditya); semuanya Paid. Kolom curated `Created By` tersembunyi secara default.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: kolom `Created By` ditampilkan dan disembunyikan lewat Popup Setup Column (langkah 2, 20, 23); preferensi kolom browser dihapus di hook `after` (kemampuan disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-369 Kelas teks Plan Name dan Created By

2. Tampilkan kolom `Created By` lewat Popup Setup Column, klik `[Save]`.
3. Ketik Search `beta`, tekan Enter.
4. Verifikasi tabel menampilkan `Beta Pro` (Plan Name).
5. Ganti isi kotak search dengan `rina`, tekan Enter.
6. Verifikasi tabel menampilkan `Beta Pro` (Created By `Rina K`, pencarian memakai nama lengkap).

### TC-AC-PF-370 Kelas badge dan angka

7. Ganti isi kotak search dengan `sams`, tekan Enter.
8. Verifikasi tabel menampilkan `Beta Pro`.
9. Ganti isi kotak search dengan `10`, tekan Enter.
10. Verifikasi tabel menampilkan `Beta Pro` (Version `v10`).
11. Ganti isi kotak search dengan `paid`, tekan Enter.
12. Verifikasi tabel menampilkan keempat baris (Pricing Type semua baris Paid).
13. Ganti isi kotak search dengan `12`, tekan Enter.
14. Verifikasi tabel menampilkan `alpha Tier` (Clients `12`).

### TC-AC-PF-371 Kolom tanggal tidak dicocokkan

15. Kosongkan isi kotak search, tekan Enter.
16. Verifikasi keempat baris tampil dengan Last Modified bulan Jun.
17. Ganti isi kotak search dengan `Jun`, tekan Enter.
18. Verifikasi tabel menampilkan "No results found" walau semua baris memiliki Last Modified bulan Jun.
19. Kosongkan isi kotak search, tekan Enter.

### TC-AC-PF-372 Search terikat visibilitas Created By

20. Buka Popup Setup Column, klik `[Reset to Default]`, klik `[Save]` (kolom `Created By` kembali tersembunyi).
21. Ketik Search `rina`, tekan Enter.
22. Verifikasi Search `rina` menampilkan "No results found" saat kolom `Created By` tersembunyi.
23. Tampilkan kolom `Created By` lewat Popup Setup Column, klik `[Save]`.
24. Tekan Enter pada kotak Search yang masih berisi `rina`.
25. Verifikasi tabel menampilkan `Beta Pro`.
26. Kosongkan isi kotak search, tekan Enter.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 15, 19, 26 mengosongkan Search; langkah 20 mengembalikan kolom `Created By` ke keadaan tersembunyi (kondisi awal TC-AC-PF-372); langkah 24 menjalankan ulang Search `rina` ("Jalankan Search `rina` lagi").
- Anchor absence (bagian 8b butir 2): "No results found" pada langkah 18 didahului langkah 16, dan pada langkah 22 didahului langkah 16 serta langkah 12 (baris tabel yang sama tampil).
- Jumlah langkah 26: di bawah ambang sekitar 35.
