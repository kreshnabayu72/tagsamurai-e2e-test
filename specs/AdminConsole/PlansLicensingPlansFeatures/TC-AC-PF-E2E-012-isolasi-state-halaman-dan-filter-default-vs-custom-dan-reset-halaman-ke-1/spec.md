---
id: TC-AC-PF-E2E-012-isolasi-state-halaman-dan-filter-default-vs-custom-dan-reset-halaman-ke-1
title: "Isolasi State Halaman dan Filter Tab Default vs Custom serta Reset Halaman ke 1 (Volume 120 Plan)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-710
  - TC-AC-PF-711
  - TC-AC-PF-712
  - TC-AC-PF-713
coverage:
  web: automated
---

# Isolasi State Halaman dan Filter Tab Default vs Custom serta Reset Halaman ke 1 (Volume 120 Plan)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data (hook `before`, volume 100 baris atau lebih sehingga kelas e): Dataset Plan Z (Pre-setup #38: 12 default plan aktif bernomor urut 01 sampai 12 dengan nama lengkap seperti pada langkah, 3 di antaranya Free (nomor 01, 05, dan 09); total Default Active N = 12) dan Dataset Plan B (Pre-setup #22: 120 custom plan Principal `Paket 001` sampai `Paket 120`, FAMS, Paid, v1, Clients 0; total Custom Active N = 120) untuk TC-AC-PF-710 dan TC-AC-PF-711; langkah penghubung mengganti Dataset Plan B dengan Dataset Plan B2 (Pre-setup #56: `Paket 001` sampai `Paket 060` Product FAMS dan `Paket 061` sampai `Paket 120` Product SAMS) untuk TC-AC-PF-712 dan TC-AC-PF-713. Dataset Plan Z menggantikan default plan Dataset Plan A karena slot Free dan Paid per Product terbatas. Fixture BE yang idempoten (disediakan tim FE/BE) menyiapkan dan memulihkan semua Dataset di hook `before` dan `after`. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (nama plan Dataset Plan Z pada langkah dan `Paket 001` sampai `Paket 120`) dipakai karena menentukan asersi urutan, jumlah, dan teks; spec hanya membaca data itu dan tidak mengubahnya. Suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (seeding 120 plan, penggantian Dataset, pemulihan) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-710: State halaman tidak dibagi antar tab Default dan tab Custom

1. Pindah ke halaman 2 pada tab Default
2. Klik tab Custom
3. Verifikasi tab Custom berada di halaman 1 dengan teks `Showing 1–10 of 120 entries`
4. Klik tab Default
5. Verifikasi halaman 2 masih aktif di tab Default dengan teks `Showing 11–12 of 12 entries`

### TC-AC-PF-711: Filter yang di-Apply tidak dibagi antar tab Default dan tab Custom

6. Klik menu Plans & Licensing > Plans & Features di sidebar
7. Buka Filter Panel, pilih Pricing Type `Free`, klik `[Apply]`
8. Verifikasi tab Default menampilkan tiga baris: `Rencana 01`, `Rencana 05`, `Rencana 09`
9. Klik tab Custom
10. Verifikasi tab Custom tidak tersaring dengan teks `Showing 1–10 of 120 entries`
11. Verifikasi ikon Filter tab Custom tanpa badge titik
12. Klik tab Default
13. Verifikasi filter Pricing Type `Free` masih ter-Apply di tab Default dengan tiga baris yang sama: `Rencana 01`, `Rencana 05`, `Rencana 09`
14. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`

### Penghubung: ganti Dataset Plan B dengan Dataset Plan B2

15. Ganti Dataset Plan B dengan Dataset Plan B2 lewat fixture BE hingga tersimpan
16. Klik menu Plans & Licensing > Plans & Features di sidebar
17. Klik tab Custom

### TC-AC-PF-712: Mengosongkan Search yang mengubah hasil mereset halaman ke 1

18. Ketik Search `Paket 1`, tekan Enter
19. Verifikasi hasil Search 21 baris (`Paket 100` sampai `Paket 120`) dengan teks `Showing 1–10 of 21 entries`
20. Pindah ke halaman 2
21. Verifikasi halaman 2 menampilkan teks `Showing 11–20 of 21 entries`
22. Klik ikon `x` di dalam input Search, lalu tekan Enter pada input kosong
23. Verifikasi tabel kembali ke halaman 1 dengan teks `Showing 1–10 of 120 entries`

### TC-AC-PF-713: Clear Field Filter yang mengubah hasil mereset halaman ke 1

24. Klik menu Plans & Licensing > Plans & Features di sidebar
25. Klik tab Custom
26. Buka Filter Panel, pilih Product `SAMS`, klik `[Apply]`
27. Verifikasi hasil Filter 60 baris dengan teks `Showing 1–10 of 60 entries`
28. Pindah ke halaman 2
29. Verifikasi halaman 2 menampilkan teks `Showing 11–20 of 60 entries`
30. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`
31. Verifikasi tabel kembali ke halaman 1 dengan teks `Showing 1–10 of 120 entries`

## Notes

- Langkah penghubung (S-03): langkah 6, 16, dan 24 (klik menu sidebar) mereset state list sebelum TC berikutnya (S-09); langkah 14 mengosongkan Filter Pricing Type `Free`; langkah 15 sampai 17 mengganti Dataset Plan B dengan Dataset Plan B2 yang dibutuhkan precondition TC-AC-PF-712 dan TC-AC-PF-713 (kedua dataset memakai nama `Paket 001` sampai `Paket 120` sehingga tidak dapat ada bersamaan); klik tab Custom pada langkah 17 dan 25 mengarahkan layar ke tab yang disyaratkan precondition TC.
- Temuan untuk QA:
  - Dataset Plan B dan Dataset Plan B2 memakai nama plan yang sama dengan Product berbeda sehingga tidak dapat hadir bersamaan; TC tidak menyebut urutan penggantian.
