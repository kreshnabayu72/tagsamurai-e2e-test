---
id: TC-AC-PF-E2E-130-search-tab-default-active-siklus-trim-tanpa-hasil
title: Search Tab Default Active Siklus Input, Trim, dan Tanpa Hasil
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-301
  - TC-AC-PF-302
  - TC-AC-PF-303
coverage:
  web: automated
---

# Search Tab Default Active Siklus Input, Trim, dan Tanpa Hasil

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif berurutan `Starter` (FAMS, Free, v2, Clients 12), `Growth` (FAMS, Paid, v5, 47), `Professional` (FAMS, Paid, v3, 23), `Enterprise` (FAMS, Paid, v1, 8), `SIEM` (SIEM, Paid, v1, 5).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-301 Siklus interaksi Search

1. Hover ikon Search.
2. Verifikasi tooltip `Search` tampil.
3. Klik ikon Search.
4. Verifikasi input Search muncul dan langsung berfokus.
5. Verifikasi placeholder input Search adalah `Search plan name, product...`.
6. Ketik `grow` pada input Search tanpa menekan Enter.
7. Verifikasi ikon `x` muncul di dalam input Search.
8. Verifikasi tabel belum tersaring (baris `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM` masih tampil).
9. Tekan Enter.
10. Verifikasi tabel tersaring: hanya baris `Growth` yang tampil.
11. Klik ikon `x` di dalam input Search.
12. Verifikasi input Search kosong.
13. Verifikasi tabel tetap menampilkan hasil Search terakhir (hanya baris `Growth`).
14. Tekan Enter pada input Search yang kosong.
15. Verifikasi tabel kembali menampilkan seluruh data (lima baris).
16. Ketik Search `grow`, tekan Enter.
17. Klik ikon panah collapse di kiri toolbar.
18. Verifikasi input Search tertutup.
19. Verifikasi tabel langsung kembali menampilkan seluruh data (lima baris).
20. Klik ikon Search.
21. Verifikasi input Search kosong (kata kunci dikosongkan).

### TC-AC-PF-302 Search di-trim

22. Ketik Search `  grow  ` (spasi, `grow`, spasi), tekan Enter.
23. Verifikasi hasil pencarian sama dengan pencarian `grow` tanpa spasi: hanya baris `Growth` yang tampil.
24. Verifikasi isi kotak Search tetap seperti diketik (`  grow  `).
25. Ganti isi kotak search dengan tiga spasi, tekan Enter.
26. Verifikasi tabel kembali menampilkan seluruh data (lima baris).

### TC-AC-PF-303 Search tanpa hasil

27. Ganti isi kotak search dengan `zzzzz`, tekan Enter.
28. Verifikasi empty state tampil: Illustration, Title "No results found", dan Description "Try adjusting your search or filter.".
29. Kosongkan isi kotak search, tekan Enter.
30. Verifikasi seluruh baris tampil kembali (lima baris).

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 20 membuka kembali input Search agar langkah 21 dapat mengamati kata kunci yang dikosongkan oleh tombol collapse (kotak Search tertutup tidak dapat diamati).
- Search dijalankan hanya dengan Enter (bagian 8b butir 9); langkah 16 membuka input sekaligus mengetik karena input sudah terbuka dari langkah sebelumnya.
- Temuan untuk QA: TC-AC-PF-301 butir f menyebut "mengosongkan kata kunci" saat collapse tanpa langkah observasi; spec mengamatinya lewat langkah 20 dan 21 (membuka kembali input).
