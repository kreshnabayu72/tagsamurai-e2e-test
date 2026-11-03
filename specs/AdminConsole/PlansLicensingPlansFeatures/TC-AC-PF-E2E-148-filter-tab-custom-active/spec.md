---
id: TC-AC-PF-E2E-148-filter-tab-custom-active
title: Filter Tab Custom Active
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-373
  - TC-AC-PF-374
  - TC-AC-PF-375
  - TC-AC-PF-376
  - TC-AC-PF-377
  - TC-AC-PF-378
  - TC-AC-PF-379
coverage:
  web: automated
---

# Filter Tab Custom Active

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier` (FAMS, v2, Clients 12, 05 Jun 26 09:00), `Beta Pro` (SAMS, v10, 7, 18 Jun 26 14:30), `Growth Tier` (FAMS, v20, 1, 22 Jun 26 08:00), `Zeta Max` (SIEM, v3, 0, 28 Jun 26 16:00); semuanya Paid.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-373 Screening Filter Panel

2. Klik ikon Filter.
3. Verifikasi field `Product` (multi-select searchable) dengan placeholder `All products`.
4. Verifikasi field `Clients` (range) dengan placeholder `Min` dan `Max`.
5. Verifikasi field `Last Modified` (date range picker) dengan placeholder `Select date`.
6. Verifikasi tidak ada field Pricing Type.
7. Verifikasi tombol `[Clear Field]` dan `[Apply]`.

### TC-AC-PF-378 Opsi dropdown Product

8. Buka dropdown Product.
9. Verifikasi opsi `FAMS`, `SAMS`, `SIEM` (ketiga Product ada di data tabel).
10. Klik ikon Filter untuk menutup panel.

### TC-AC-PF-374 Filter Product

11. Buka Filter Panel, pilih Product `FAMS`, klik `[Apply]`.
12. Verifikasi tabel menampilkan `alpha Tier` dan `Growth Tier`.
13. Buka Filter Panel, tambahkan `SIEM`, klik `[Apply]`.
14. Verifikasi tabel menampilkan `alpha Tier`, `Growth Tier`, `Zeta Max`.
15. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-375 Filter Clients inklusif

16. Buka Filter Panel, isi Min `7` dan Max `12`, klik `[Apply]`.
17. Verifikasi tabel menampilkan `alpha Tier` (12) dan `Beta Pro` (7).
18. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-376 Filter Last Modified

19. Buka Filter Panel, pilih rentang `18 Jun 26` sampai `22 Jun 26`, klik `[Apply]`.
20. Verifikasi tabel menampilkan `Beta Pro` dan `Growth Tier` (batas awal dan akhir inklusif).
21. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-379 Filter tanpa hasil

22. Buka Filter Panel, isi Min Clients `100`, klik `[Apply]`.
23. Verifikasi Illustration tampil pada tabel.
24. Verifikasi Title "No results found" tampil.
25. Verifikasi Description "Try adjusting your search or filter." tampil.
26. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-377 Kombinasi Search dan Filter AND

27. Ketik Search `tier`, tekan Enter.
28. Buka Filter Panel, pilih Product `FAMS` dan Min Clients `5`, klik `[Apply]`.
29. Verifikasi tabel menampilkan `alpha Tier` saja (Search `tier`, Product `FAMS`, Clients ≥ 5).
30. Verifikasi kotak Search tetap berisi `tier`.
31. Klik `✕` pada Search, tekan Enter.
32. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

## Notes

- Urutan blok: TC-AC-PF-378 diletakkan sesudah screening karena panel masih terbuka; TC-AC-PF-379 dan TC-AC-PF-377 mendekati akhir karena memakai kombinasi kontrol (bagian 3 prinsip 1).
- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 10 menutup Filter Panel; langkah 15, 18, 21, 26, dan 32 mengosongkan Filter; langkah 31 mengosongkan Search (bagian 8b butir 9).
- TC-AC-PF-379 memecah Expected empty state per butir (Illustration, Title, Description); spec mengikuti pemecahan TC (S-01).
- Jumlah langkah 32: di bawah ambang sekitar 35.
