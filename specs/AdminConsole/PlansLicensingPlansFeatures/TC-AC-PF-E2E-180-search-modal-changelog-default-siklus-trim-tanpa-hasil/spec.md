---
id: TC-AC-PF-E2E-180-search-modal-changelog-default-siklus-trim-tanpa-hasil
title: Search modal Changelog Default siklus interaksi, trim spasi, dan empty state tanpa hasil
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-457
  - TC-AC-PF-458
  - TC-AC-PF-459
coverage:
  web: automated
---

# Search modal Changelog Default siklus interaksi, trim spasi, dan empty state tanpa hasil

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Siklus interaksi Search (TC-AC-PF-457)

1. Klik ikon Changelog pada toolbar tab Default
2. Hover ikon Search
3. Verifikasi tooltip `Search`
4. Klik ikon Search
5. Verifikasi input Search muncul dengan placeholder `Search action, field, or value...`
6. Verifikasi input Search langsung berfokus
7. Ketik `growth` tanpa menekan Enter
8. Verifikasi ikon `x` muncul di dalam input
9. Verifikasi tabel belum tersaring (kelima baris masih tampil)
10. Tekan Enter
11. Verifikasi tabel tersaring: baris `Archive Growth Plus (old)` dan `Edit Growth`
12. Klik ikon `x` di dalam input
13. Verifikasi input Search kosong
14. Verifikasi tabel tetap menampilkan hasil Search terakhir (baris `Archive Growth Plus (old)` dan `Edit Growth`)
15. Tekan Enter pada input kosong
16. Verifikasi tabel kembali menampilkan seluruh data (kelima baris)
17. Ketik Search `growth`, tekan Enter
18. Klik ikon panah collapse di kiri toolbar
19. Verifikasi input Search tertutup
20. Verifikasi kata kunci dikosongkan
21. Verifikasi tabel langsung kembali menampilkan seluruh data (kelima baris)

### Trim spasi (TC-AC-PF-458)

22. Klik ikon Search, ketik `  growth  ` (spasi, `growth`, spasi), tekan Enter
23. Verifikasi hasil pencarian sama dengan pencarian `growth` tanpa spasi: baris `Archive Growth Plus (old)` dan `Edit Growth`
24. Verifikasi isi kotak Search tetap `  growth  ` seperti diketik
25. Hapus teks, ketik tiga spasi, tekan Enter
26. Verifikasi tabel kembali menampilkan seluruh data (kelima baris)

### Tanpa hasil (TC-AC-PF-459)

27. Ganti isi kotak search dengan `zzzzz`, tekan Enter
28. Verifikasi empty state: Illustration, Title "No results found", dan Description "Try adjusting your search or filter."
29. Kosongkan isi kotak search, tekan Enter
30. Verifikasi seluruh baris tampil kembali (kelima baris)

## Notes

- Tidak ada langkah penghubung: blok TC-AC-PF-458 dan TC-AC-PF-459 melanjutkan input Search yang terbuka dari blok sebelumnya (langkah 22 membuka input kembali setelah collapse pada langkah 18).
- Temuan untuk QA: TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi jumlah baris bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
