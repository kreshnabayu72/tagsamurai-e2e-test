---
id: TC-AC-PF-E2E-140-pagination-tab-default-active-dan-archive-baris-terakhir
title: Pagination Tab Default Active dan Archive Baris Terakhir di Halaman Terakhir
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-345
  - TC-AC-PF-346
  - TC-AC-PF-347
  - TC-AC-PF-348
  - TC-AC-PF-349
  - TC-AC-PF-641
coverage:
  web: automated
---

# Pagination Tab Default Active dan Archive Baris Terakhir di Halaman Terakhir

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan Z (Pre-setup #38), 12 default plan aktif bernomor 01 sampai 12, nama literal Pre-setup (FAMS: 01 Free, 02 sampai 04 Paid; SAMS: 05 Free, 06 sampai 08 Paid; SIEM: 09 Free, 10 sampai 12 Paid), tanpa subscription penahan. Dataset Plan Z menempati seluruh slot Free dan Paid per Product sehingga spec ini tidak bersama Dataset Plan A.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Plan Z ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Blok TC-AC-PF-641 meng-Archive dua default plan Dataset Plan Z (Last Updated dan entri Changelog Default berubah); dipulihkan fixture BE di hook `after`.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-345 Default pagination dan opsi page size

1. Verifikasi halaman 1 menampilkan 10 baris.
2. Verifikasi teks `Showing 1–10 of 12 entries`.
3. Verifikasi `Rows per page: 10`.
4. Klik Overlay Page Size.
5. Verifikasi Overlay Page Size memuat `10`, `25`, `50`, `100` tanpa opsi All.
6. Verifikasi tombol `Prev` Disabled pada halaman 1.
7. Tekan Esc untuk menutup overlay.

### TC-AC-PF-346 Navigasi halaman

8. Klik `Next`.
9. Verifikasi baris 11 sampai 12 tampil.
10. Verifikasi teks `Showing 11–12 of 12 entries`.
11. Klik `Prev`.
12. Verifikasi tabel kembali ke halaman 1.
13. Ketik `2` pada input nomor halaman, tekan Enter.
14. Verifikasi halaman 2 langsung terbuka.

### TC-AC-PF-347 Nomor halaman tidak valid

15. Ketik `0` pada input nomor halaman, tekan Enter.
16. Ketik `999` pada input nomor halaman, tekan Enter.
17. Ketik `abc` pada input nomor halaman, tekan Enter.
18. Verifikasi ketiga input diabaikan dan tabel tetap di halaman 2.

### TC-AC-PF-348 Ganti page size

19. Pilih `25` pada Overlay Page Size.
20. Verifikasi tabel kembali ke halaman 1 dengan page size 25.
21. Verifikasi teks `Showing 1–12 of 12 entries`.
22. Pilih `10` pada Overlay Page Size.

### TC-AC-PF-349 Search, Filter, dan Sort terhadap nomor halaman

23. Klik `Next` untuk pindah ke halaman 2.
24. Klik header kolom pertama satu kali (sort ascending).
25. Verifikasi tabel tetap di halaman 2 setelah ganti sort.
26. Ketik Search `Rencana`, tekan Enter.
27. Verifikasi tabel kembali ke halaman 1.
28. Verifikasi teks `Showing 1–10 of 12 entries`.
29. Klik `✕` pada Search, tekan Enter.
30. Klik header kolom pertama dua kali untuk mengembalikan sort ke netral.

### TC-AC-PF-641 Archive baris terakhir di halaman terakhir

31. Klik `Next` untuk pindah ke halaman 2.
32. Verifikasi teks `Showing 11–12 of 12 entries`.
33. Buka Overlay Row Action baris pertama di halaman 2, klik `Archive`, klik `[Archive]`.
34. Verifikasi tabel tetap di halaman 2.
35. Verifikasi teks `Showing 11–11 of 11 entries`.
36. Buka Overlay Row Action baris yang tersisa di halaman 2, klik `Archive`, klik `[Archive]`.
37. Verifikasi tabel pindah ke halaman terakhir yang masih ada (halaman 1).
38. Verifikasi teks `Showing 1–10 of 10 entries`.
39. Verifikasi tabel bukan empty state dan bukan halaman kosong.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 7 menutup overlay; langkah 22 mengembalikan page size ke 10; langkah 23 pindah ke halaman 2; langkah 29 dan 30 memulihkan Search dan sort.
- Urutan: TC-AC-PF-641 (aksi Archive yang mengubah data) berada di akhir spec (S-10, aksi mengubah data di akhir).
- Alasan di atas sekitar 35 langkah (39): seluruh blok memakai satu surface (footer pagination Default Active), satu dataset (Dataset Plan Z), dan tidak ada state yang dibangun antar-blok selain halaman aktif; TC-AC-PF-641 memerlukan Dataset Plan Z yang sama dan memang harus berakhir sebagai aksi mengubah data. Estimasi langkah semula lebih rendah karena S-01 memecah tiap butir Expected per klausa.
