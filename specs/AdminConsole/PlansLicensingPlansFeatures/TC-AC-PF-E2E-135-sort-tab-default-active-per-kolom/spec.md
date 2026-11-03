---
id: TC-AC-PF-E2E-135-sort-tab-default-active-per-kolom
title: Sort Tab Default Active per Kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-325
  - TC-AC-PF-326
  - TC-AC-PF-327
  - TC-AC-PF-328
  - TC-AC-PF-330
coverage:
  web: automated
---

# Sort Tab Default Active per Kolom

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), urutan default `Starter` (FAMS, Free, v2, Clients 12, 15 Jun 26 10:00), `Growth` (FAMS, Paid, v5, 47, 15 Jun 26 10:00), `Professional` (FAMS, Paid, v3, 23, 15 Jun 26 10:00), `Enterprise` (FAMS, Paid, v1, 8, 12 Aug 26 09:00), `SIEM` (SIEM, Paid, v1, 5, 09 Jul 26 11:00).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-325 Plan Name dan Product

1. Klik header `Plan Name` satu kali.
2. Verifikasi ascending berurutan `Enterprise`, `Growth`, `Professional`, `SIEM`, `Starter`.
3. Klik header `Plan Name` kali kedua.
4. Verifikasi descending berurutan `Starter`, `SIEM`, `Professional`, `Growth`, `Enterprise`.
5. Klik header `Plan Name` kali ketiga.
6. Verifikasi tabel kembali ke urutan default (`Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`).
7. Verifikasi tidak ada panah sort aktif pada header kolom.
8. Klik header `Product` satu kali.
9. Verifikasi Product ascending: empat baris FAMS (urutan default `Starter`, `Growth`, `Professional`, `Enterprise`) lalu `SIEM`.
10. Klik header `Product` kali kedua.
11. Verifikasi Product descending: `SIEM` lalu empat baris FAMS dengan urutan default.

### TC-AC-PF-326 Pricing Type mengikuti urutan tier

12. Klik header `Pricing Type` satu kali.
13. Verifikasi ascending: `Starter` (Free) lalu `Growth`, `Professional`, `Enterprise`, `SIEM` (Paid, urutan default).
14. Klik header `Pricing Type` kali kedua.
15. Verifikasi descending: baris Paid (urutan default) lalu `Starter`.
16. Klik header `Pricing Type` kali ketiga.
17. Verifikasi tabel kembali ke urutan default.

### TC-AC-PF-327 Version dan Clients numerik

18. Klik header `Version` satu kali.
19. Verifikasi Version ascending: `Enterprise` (v1), `SIEM` (v1) (urutan default sebagai tie-breaker), `Starter` (v2), `Professional` (v3), `Growth` (v5).
20. Klik header `Version` kali kedua.
21. Verifikasi Version descending berupa kebalikan nilai.
22. Klik header `Clients` satu kali.
23. Verifikasi Clients ascending: `SIEM` (5), `Enterprise` (8), `Starter` (12), `Professional` (23), `Growth` (47).
24. Klik header `Clients` kali kedua.
25. Verifikasi Clients descending berupa kebalikan nilai.

### TC-AC-PF-328 Last Modified

26. Klik header `Last Modified` satu kali.
27. Verifikasi ascending (Oldest First): `Starter`, `Growth`, `Professional` (15 Jun 26, urutan default), `SIEM` (09 Jul 26), `Enterprise` (12 Aug 26).
28. Klik header `Last Modified` kali kedua.
29. Verifikasi descending (Newest First): `Enterprise`, `SIEM`, lalu `Starter`, `Growth`, `Professional`.
30. Klik header `Last Modified` kali ketiga.

### TC-AC-PF-330 Header Actions

31. Verifikasi header kolom paling kanan (Actions, `⋯`) tidak memiliki ikon sort.
32. Klik header kolom Actions (`⋯`).
33. Verifikasi Overlay Column Visibility terbuka.
34. Tekan Esc untuk menutup overlay.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 30 menyelesaikan siklus tiga klik `Last Modified` agar sort kembali netral; langkah 34 menutup overlay.
- Pindah kolom sort mereset kolom sebelumnya (bagian 3 TC-AC-PF-329 diuji di spec lain); karena itu langkah 8, 12, 18, 22, dan 26 tidak didahului pemulihan sort kolom sebelumnya.
- Jumlah langkah 34: di bawah ambang sekitar 35.
