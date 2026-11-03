---
id: TC-AC-PF-E2E-134-filter-tab-default-active-indikator-clients-tersembunyi
title: Filter Tab Default Active Indikator, Kolom Clients Tersembunyi, Tanpa Hasil, dan Alur Search dengan Filter
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-320
  - TC-AC-PF-321
  - TC-AC-PF-322
  - TC-AC-PF-323
  - TC-AC-PF-324
coverage:
  web: automated
---

# Filter Tab Default Active Indikator, Kolom Clients Tersembunyi, Tanpa Hasil, dan Alur Search-Filter

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif `Starter` (FAMS, Free, v2, Clients 12), `Growth` (FAMS, Paid, v5, 47), `Professional` (FAMS, Paid, v3, 23), `Enterprise` (FAMS, Paid, v1, 8), `SIEM` (SIEM, Paid, v1, 5).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: visibilitas kolom `Clients` disembunyikan lalu dipulihkan di dalam spec (langkah 8 dan 13); preferensi kolom browser dihapus di hook `after` (kemampuan disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-320 Indikator titik pada ikon Filter

1. Buka Filter Panel, pilih Product `SIEM`, klik `[Apply]`.
2. Verifikasi ikon Filter menampilkan titik indikator saat Filter Panel tertutup.
3. Buka Filter Panel.
4. Verifikasi ikon Filter menampilkan titik indikator saat Filter Panel terbuka.
5. Klik `[Clear Field]`, lalu klik `[Apply]`.
6. Verifikasi titik indikator pada ikon Filter hilang.
7. Verifikasi tabel menampilkan lima baris.

### TC-AC-PF-321 Filter saat kolom Clients disembunyikan

8. Sembunyikan kolom `Clients` lewat Overlay Column Visibility.
9. Buka Filter Panel.
10. Verifikasi field Clients tetap ada di Filter Panel walau kolomnya tersembunyi.
11. Isi Min `20` pada Clients, klik `[Apply]`.
12. Verifikasi tabel menampilkan `Growth` dan `Professional`.
13. Tampilkan kembali kolom `Clients` lewat Overlay Column Visibility.
14. Verifikasi filter tetap ter-Apply setelah kolom ditampilkan (tabel tetap menampilkan `Growth` dan `Professional`).
15. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-322 Filter tanpa hasil

16. Buka Filter Panel, pilih Pricing Type `Free` dan Min Clients `50`, klik `[Apply]`.
17. Verifikasi Illustration tampil pada tabel.
18. Verifikasi Title "No results found" tampil.
19. Verifikasi Description "Try adjusting your search or filter." tampil.
20. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.
21. Verifikasi lima baris tampil kembali.

### TC-AC-PF-323 Search lalu Filter

22. Ketik Search `r`, tekan Enter.
23. Verifikasi tabel menampilkan `Starter`, `Growth`, `Professional`, `Enterprise` (mengandung `r`).
24. Buka Filter Panel, pilih Product `FAMS` dan Pricing Type `Paid`, klik `[Apply]`.
25. Verifikasi tabel menampilkan `Growth`, `Professional`, `Enterprise`.
26. Verifikasi kotak Search tetap berisi `r`.
27. Klik `✕` pada Search, tekan Enter.
28. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-324 Filter lalu Search

29. Buka Filter Panel, pilih Product `FAMS` dan Pricing Type `Paid`, klik `[Apply]`.
30. Ketik Search `r`, tekan Enter.
31. Verifikasi hasil sama dengan alur Search lalu Filter: `Growth`, `Professional`, `Enterprise`.
32. Verifikasi filter Product `FAMS` dan Pricing Type `Paid` tetap aktif.
33. Klik `✕` pada Search, tekan Enter.
34. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 15, 20, 28, dan 34 mengosongkan Filter; langkah 27 dan 33 mengosongkan Search (`✕` lalu Enter, bagian 8b butir 9); langkah 8 dan 13 menyembunyikan serta menampilkan kembali kolom `Clients` sebagai bagian dari alur TC-AC-PF-321.
- TC-AC-PF-322 memecah Expected empty state per butir (Illustration, Title, Description); spec mengikuti pemecahan TC (S-01).
- Temuan untuk QA: TC-AC-PF-320 langkah 2 "Tutup panel dan amati ikon Filter" tidak menyatakan apakah `[Apply]` menutup panel otomatis; spec mengasumsikan Filter Panel tertutup sesudah `[Apply]` (selaras dengan TC lain yang selalu "Buka Filter Panel" sebelum Apply berikutnya) sehingga langkah 2 hanya mengamati ikon.
- Jumlah langkah 34: di bawah ambang sekitar 35.
