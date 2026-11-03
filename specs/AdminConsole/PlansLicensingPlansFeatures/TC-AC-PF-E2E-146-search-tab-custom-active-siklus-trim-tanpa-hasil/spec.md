---
id: TC-AC-PF-E2E-146-search-tab-custom-active-siklus-trim-tanpa-hasil
title: Search Tab Custom Active Siklus Input, Trim, dan Tanpa Hasil
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-366
  - TC-AC-PF-367
  - TC-AC-PF-368
coverage:
  web: automated
---

# Search Tab Custom Active Siklus Input, Trim, dan Tanpa Hasil

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier` (FAMS, v2, Clients 12), `Beta Pro` (SAMS, v10, 7), `Growth Tier` (FAMS, v20, 1), `Zeta Max` (SIEM, v3, 0); semuanya Paid.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-366 Siklus interaksi Search

2. Hover ikon Search.
3. Verifikasi tooltip `Search` tampil.
4. Klik ikon Search.
5. Verifikasi input Search muncul dan langsung berfokus.
6. Verifikasi placeholder input Search adalah `Search plan name, product...`.
7. Ketik `tier` pada input Search tanpa menekan Enter.
8. Verifikasi ikon `x` muncul di dalam input Search.
9. Verifikasi tabel belum tersaring (keempat baris `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max` masih tampil).
10. Tekan Enter.
11. Verifikasi tabel tersaring: baris `alpha Tier` dan `Growth Tier`.
12. Klik ikon `x` di dalam input Search.
13. Verifikasi input Search kosong.
14. Verifikasi tabel tetap menampilkan hasil Search terakhir (`alpha Tier` dan `Growth Tier`).
15. Tekan Enter pada input Search yang kosong.
16. Verifikasi tabel kembali menampilkan seluruh data (empat baris).
17. Ketik Search `tier`, tekan Enter.
18. Klik ikon panah collapse di kiri toolbar.
19. Verifikasi input Search tertutup.
20. Verifikasi tabel langsung kembali menampilkan seluruh data (empat baris).
21. Klik ikon Search.
22. Verifikasi input Search kosong (kata kunci dikosongkan).

### TC-AC-PF-367 Search di-trim

23. Ketik Search `  tier  ` (spasi, `tier`, spasi), tekan Enter.
24. Verifikasi hasil pencarian sama dengan pencarian `tier` tanpa spasi: baris `alpha Tier` dan `Growth Tier`.
25. Verifikasi isi kotak Search tetap seperti diketik (`  tier  `).
26. Ganti isi kotak search dengan tiga spasi, tekan Enter.
27. Verifikasi tabel kembali menampilkan seluruh data (empat baris).

### TC-AC-PF-368 Search tanpa hasil

28. Ganti isi kotak search dengan `zzzzz`, tekan Enter.
29. Verifikasi empty state tampil: Illustration, Title "No results found", dan Description "Try adjusting your search or filter.".
30. Kosongkan isi kotak search, tekan Enter.
31. Verifikasi seluruh baris tampil kembali (empat baris).

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 21 membuka kembali input Search agar langkah 22 dapat mengamati kata kunci yang dikosongkan oleh tombol collapse.
- Search dijalankan hanya dengan Enter (bagian 8b butir 9).
- Temuan untuk QA: TC-AC-PF-366 butir f menyebut "mengosongkan kata kunci" saat collapse tanpa langkah observasi; spec mengamatinya lewat langkah 21 dan 22.
- Jumlah langkah 31: di bawah ambang sekitar 35.
