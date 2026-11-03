---
id: TC-AC-PF-E2E-132-filter-tab-default-active-screening-product-pricing-type
title: Filter Tab Default Active Screening, Product, Pricing Type, Clients, dan Last Modified
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-309
  - TC-AC-PF-310
  - TC-AC-PF-311
  - TC-AC-PF-312
  - TC-AC-PF-313
  - TC-AC-PF-314
coverage:
  web: automated
---

# Filter Tab Default Active Screening, Product, Pricing Type, Clients, dan Last Modified

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif `Starter` (FAMS, Free, v2, Clients 12, Last Modified 15 Jun 26), `Growth` (FAMS, Paid, v5, 47, 15 Jun 26), `Professional` (FAMS, Paid, v3, 23, 15 Jun 26), `Enterprise` (FAMS, Paid, v1, 8, 12 Aug 26), `SIEM` (SIEM, Paid, v1, 5, 09 Jul 26).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-309 dan TC-AC-PF-314 Screening Filter Panel

1. Hover ikon Filter.
2. Verifikasi tooltip `Filter` tampil.
3. Klik ikon Filter.
4. Verifikasi ikon Filter menjadi gelap saat panel terbuka.
5. Verifikasi field `Product` (multi-select searchable) dengan placeholder `All products`.
6. Verifikasi field `Pricing Type` (multi-select searchable) dengan placeholder `All pricing types`.
7. Verifikasi field `Clients` (range Min–Max) dengan placeholder `Min` dan `Max`.
8. Verifikasi field `Last Modified` (date range picker) dengan placeholder `Select date`.
9. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan.
10. Verifikasi maksimal empat field dalam satu baris.
11. Klik ikon Filter untuk menutup panel.

### TC-AC-PF-310 Filter Product

12. Buka Filter Panel, buka dropdown Product dan pilih `FAMS`, klik `[Apply]`.
13. Verifikasi tabel menampilkan empat baris (`Starter`, `Growth`, `Professional`, `Enterprise`).
14. Buka Filter Panel dan tambahkan `SIEM` pada Product, klik `[Apply]`.
15. Verifikasi tabel menampilkan lima baris.
16. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-311 Filter Pricing Type

17. Buka Filter Panel dan pilih Pricing Type `Free`, klik `[Apply]`.
18. Verifikasi tabel menampilkan baris `Starter` saja.
19. Buka Filter Panel dan ganti pilihan Pricing Type menjadi `Paid`, klik `[Apply]`.
20. Verifikasi tabel menampilkan baris `Growth`, `Professional`, `Enterprise`, `SIEM`.
21. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-312 Filter Clients

22. Buka Filter Panel, isi Min `10`, Max kosong, klik `[Apply]`.
23. Verifikasi tabel menampilkan `Starter` (12), `Growth` (47), `Professional` (23).
24. Buka Filter Panel, kosongkan Min, isi Max `10`, klik `[Apply]`.
25. Verifikasi tabel menampilkan `Enterprise` (8) dan `SIEM` (5).
26. Buka Filter Panel, isi Min `8` dan Max `12`, klik `[Apply]`.
27. Verifikasi tabel menampilkan `Starter` (12) dan `Enterprise` (8).
28. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-313 Filter Last Modified

29. Buka Filter Panel, pilih rentang `15 Jun 26` sampai `15 Jun 26`, klik `[Apply]`.
30. Verifikasi tabel menampilkan `Starter`, `Growth`, `Professional`.
31. Buka Filter Panel, pilih rentang `01 Jul 26` sampai `31 Aug 26`, klik `[Apply]`.
32. Verifikasi tabel menampilkan `SIEM` (09 Jul 26) dan `Enterprise` (12 Aug 26).
33. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 11 menutup Filter Panel; langkah 16, 21, 28, dan 33 mengosongkan Filter (`[Clear Field]` lalu `[Apply]`) agar tiap TC berikutnya mulai dari tabel penuh.
- Verifikasi placeholder `Select date` pada langkah 8 memenuhi TC-AC-PF-309 butir b dan sekaligus TC-AC-PF-314 (Expected-nya sama: placeholder Last Modified `Select date`); TC-AC-PF-314 ditempatkan di blok screening karena panel sudah terbuka.
- Jumlah langkah 33: di bawah ambang sekitar 35.
