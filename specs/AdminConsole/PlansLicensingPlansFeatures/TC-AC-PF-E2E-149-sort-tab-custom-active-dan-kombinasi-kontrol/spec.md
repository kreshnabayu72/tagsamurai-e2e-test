---
id: TC-AC-PF-E2E-149-sort-tab-custom-active-dan-kombinasi-kontrol
title: Sort Tab Custom Active per Kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-380
  - TC-AC-PF-381
  - TC-AC-PF-382
  - TC-AC-PF-383
coverage:
  web: automated
---

# Sort Tab Custom Active per Kolom

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier` (FAMS, v2, Clients 12, 05 Jun 26 09:00, Created By Andi Wijaya), `Beta Pro` (SAMS, v10, 7, 18 Jun 26 14:30, Rina Kusuma), `Growth Tier` (FAMS, v20, 1, 22 Jun 26 08:00, Andi Wijaya), `Zeta Max` (SIEM, v3, 0, 28 Jun 26 16:00, Budi Aditya); semuanya Paid. Urutan default Plan Name A-Z.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: kolom `Created By` ditampilkan lewat Popup Setup Column (langkah 24); preferensi kolom browser dihapus di hook `after` (kemampuan disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-380 Plan Name, Product, Pricing Type

2. Klik header `Plan Name` satu kali.
3. Verifikasi ascending berurutan `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`.
4. Klik header `Plan Name` kali kedua.
5. Verifikasi descending berupa kebalikan urutan ascending.
6. Klik header `Plan Name` kali ketiga.
7. Verifikasi tabel kembali ke urutan default.
8. Klik header `Product` satu kali.
9. Verifikasi Product ascending berurutan `alpha Tier`, `Growth Tier` (FAMS), `Beta Pro` (SAMS), `Zeta Max` (SIEM).
10. Klik header `Pricing Type` satu kali.
11. Verifikasi Pricing Type ascending: urutan tetap `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`.
12. Klik header `Pricing Type` kali kedua.
13. Verifikasi Pricing Type descending: urutan tetap `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`.

### TC-AC-PF-381 Version dan Clients natural

14. Klik header `Version` satu kali.
15. Verifikasi Version ascending: `alpha Tier` (v2), `Zeta Max` (v3), `Beta Pro` (v10), `Growth Tier` (v20).
16. Klik header `Clients` satu kali.
17. Verifikasi Clients ascending: `Zeta Max` (0), `Growth Tier` (1), `Beta Pro` (7), `alpha Tier` (12).

### TC-AC-PF-382 Last Modified

18. Klik header `Last Modified` satu kali.
19. Verifikasi ascending: `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`.
20. Klik header `Last Modified` kali kedua.
21. Verifikasi descending: `Zeta Max`, `Growth Tier`, `Beta Pro`, `alpha Tier`.

### TC-AC-PF-383 Created By memakai nama lengkap

22. Klik header `Last Modified` kali ketiga untuk mengembalikan sort ke netral.
23. Tampilkan kolom `Created By` lewat Popup Setup Column, klik `[Save]`.
24. Klik header `Created By` satu kali.
25. Verifikasi ascending berdasarkan nama lengkap: `Andi Wijaya` (`alpha Tier`, `Growth Tier`), `Budi Aditya` (`Zeta Max`), `Rina Kusuma` (`Beta Pro`).
26. Verifikasi sel Created By tampil sebagai `Andi W`, `Budi A`, dan `Rina K`.
27. Hover sel `Andi W`.
28. Verifikasi tooltip menampilkan `Andi Wijaya`.
29. Hover sel `Budi A`.
30. Verifikasi tooltip menampilkan `Budi Aditya`.
31. Hover sel `Rina K`.
32. Verifikasi tooltip menampilkan `Rina Kusuma`.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 22 menyelesaikan siklus klik `Last Modified`; langkah 23 menampilkan kolom curated `Created By` yang tersembunyi secara default.
- Pindah kolom sort mereset sort kolom sebelumnya, sehingga langkah 8, 10, 14, 16, 18, dan 24 tidak didahului pemulihan sort.
- Jumlah langkah 32: di bawah ambang sekitar 35.
