---
id: TC-AC-PF-E2E-156-pagination-tab-custom-active-volume-120-plan
title: Pagination Tab Custom Active Volume 120 Plan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-395
  - TC-AC-PF-396
  - TC-AC-PF-397
  - TC-AC-PF-398
  - TC-AC-PF-399
  - TC-AC-PF-400
coverage:
  web: automated
---

# Pagination Tab Custom Active Volume 120 Plan

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan B (Pre-setup #22): 120 custom plan Principal `Paket 001` sampai `Paket 120` (FAMS, Paid, v1, Clients 0). Kelas e (volume data 100 baris atau lebih); seeding 120 plan lewat fixture BE.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal dan seeding 120 plan (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-395 Default pagination dan opsi page size

2. Verifikasi halaman 1 menampilkan 10 baris.
3. Verifikasi teks `Showing 1–10 of 120 entries`.
4. Verifikasi `Rows per page: 10`.
5. Klik Overlay Page Size.
6. Verifikasi Overlay Page Size memuat `10`, `25`, `50`, `100` tanpa opsi All.
7. Verifikasi tombol `Prev` Disabled pada halaman 1.
8. Tekan Esc untuk menutup overlay.

### TC-AC-PF-396 Navigasi halaman

9. Klik `Next`.
10. Verifikasi baris 11 sampai 20 tampil.
11. Verifikasi teks `Showing 11–20 of 120 entries`.
12. Klik `Prev`.
13. Verifikasi tabel kembali ke halaman 1.
14. Ketik `2` pada input nomor halaman, tekan Enter.
15. Verifikasi halaman 2 langsung terbuka.

### TC-AC-PF-397 Nomor halaman tidak valid

16. Ketik `0` pada input nomor halaman, tekan Enter.
17. Ketik `999` pada input nomor halaman, tekan Enter.
18. Ketik `abc` pada input nomor halaman, tekan Enter.
19. Verifikasi ketiga input diabaikan dan tabel tetap di halaman 2.

### TC-AC-PF-398 Ganti page size

20. Pilih `25` pada Overlay Page Size.
21. Verifikasi tabel kembali ke halaman 1 dengan page size 25.
22. Verifikasi teks `Showing 1–25 of 120 entries`.
23. Pilih `10` pada Overlay Page Size.

### TC-AC-PF-399 Search dan Sort terhadap nomor halaman

24. Klik `Next` untuk pindah ke halaman 2.
25. Klik header kolom pertama satu kali (sort ascending).
26. Verifikasi tabel tetap di halaman 2 setelah ganti sort.
27. Ketik Search `Paket`, tekan Enter.
28. Verifikasi tabel kembali ke halaman 1.
29. Verifikasi teks `Showing 1–10 of 120 entries`.
30. Klik `✕` pada Search, tekan Enter.
31. Klik header kolom pertama dua kali untuk mengembalikan sort ke netral.

### TC-AC-PF-400 Rows per page 100

32. Pilih `100` pada Overlay Page Size.
33. Verifikasi teks `Showing 1–100 of 120 entries`.
34. Klik `Next`.
35. Verifikasi teks `Showing 101–120 of 120 entries`.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 8 menutup overlay; langkah 23 mengembalikan page size ke 10; langkah 24 pindah ke halaman 2; langkah 30 dan 31 memulihkan Search dan sort.
- Temuan untuk QA: TC-AC-PF-400 tidak mencantumkan precondition General Settings (tidak memengaruhi asersi).
- Jumlah langkah 35: sekitar ambang 35.
