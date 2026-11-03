---
id: TC-AC-ACC-E2E-286-filter-status-produk-fams-sams-siem
title: "Filter Client List: Placeholder dan Opsi Status FAMS, SAMS, SIEM Mengikuti Data Sub-tab, serta Hasil Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-378
  - TC-AC-ACC-379
  - TC-AC-ACC-380
  - TC-AC-ACC-387
coverage:
  web: automated
---

# Filter Client List: Placeholder dan Opsi Status FAMS, SAMS, SIEM Mengikuti Data Sub-tab, serta Hasil Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 hanya dibaca: C-LST-1 `PT Sortir Alfa` (FAMS Grace, SAMS Active, SIEM Pending), C-LST-2 `PT Sortir Beta` (FAMS Pending, SAMS Grace, SIEM Active), C-LST-3 `PT Sortir Gamma` (FAMS Active, SAMS Pending, SIEM Grace); C-LIF-16 `PT Aktif Plus Menunggu` (SAMS Waiting for Approval); C-FX11-2 `PT Riwayat Opsi Status` (badge SAMS Active; riwayat term SAMS Renewed, Rejected, dan Canceled).
- Fixture Tabel A Pre-setup yang dipakai TC-AC-ACC-387: sub-tab Active `PT Sejahtera Abadi` FAMS Active, `PT Teknologi Maju` FAMS Grace, `PT Mulai Esok` FAMS Pending, `PT Cahaya Baru` FAMS Waiting for Approval; sub-tab Archived `PT Karya Abadi` FAMS Archive, `PT Lama Tak Berbayar` FAMS Purge.
- Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Opsi status mengikuti sub-tab (TC-AC-ACC-387)

1. Klik Filter, buka dropdown FAMS dan baca opsi (sub-tab Active)
2. Verifikasi opsi memuat `Active`, `Grace`, `Pending`, dan `Waiting for Approval`
3. Verifikasi opsi tidak memuat `Renewed`, `Rejected`, dan `Canceled`
4. Klik ikon Filter untuk menutup panel, lalu klik sub-tab Archived
5. Klik Filter, buka dropdown FAMS dan baca opsi
6. Verifikasi opsi memuat `Archive` dan `Purge`
7. Verifikasi opsi tidak memuat `Active`, `Grace`, `Pending`, dan `Waiting for Approval`
8. Klik ikon Filter untuk menutup panel, lalu klik sub-tab Active

### Filter FAMS (TC-AC-ACC-378)

9. Klik Filter dan lihat placeholder field FAMS
10. Verifikasi placeholder field FAMS `All statuses`
11. Buka dropdown FAMS dan baca opsi
12. Verifikasi opsi memuat `Active`, `Grace`, `Pending`, dan `Waiting for Approval`
13. Verifikasi opsi tidak memuat `Renewed`, `Rejected`, dan `Canceled`
14. Pilih opsi `Grace`, lalu klik [Apply]
15. Ketik Search `PT Sortir Alfa`, tekan Enter
16. Verifikasi baris `PT Sortir Alfa` tampil
17. Ganti isi kotak search dengan `PT Sortir Gamma`, tekan Enter
18. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
19. Klik `(←)` pada kotak Search, lalu klik Filter, klik [Clear Field], dan klik [Apply]

### Filter SAMS (TC-AC-ACC-379)

20. Klik Filter dan lihat placeholder field SAMS
21. Verifikasi placeholder field SAMS `All statuses`
22. Buka dropdown SAMS dan baca opsi
23. Verifikasi opsi memuat `Active`, `Grace`, `Pending`, dan `Waiting for Approval`
24. Verifikasi opsi tidak memuat `Renewed`, `Rejected`, dan `Canceled` walau `PT Riwayat Opsi Status` memiliki term SAMS berstatus itu pada riwayatnya
25. Pilih opsi `Grace`, lalu klik [Apply]
26. Ketik Search `PT Sortir Beta`, tekan Enter
27. Verifikasi baris `PT Sortir Beta` tampil
28. Ganti isi kotak search dengan `PT Sortir Alfa`, tekan Enter
29. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
30. Klik Filter, klik [Clear Field], lalu klik [Apply]
31. Ganti isi kotak search dengan `PT Riwayat Opsi Status`, tekan Enter
32. Verifikasi baris `PT Riwayat Opsi Status` tampil dengan sel SAMS `Active`
33. Klik `(←)` pada kotak Search

### Filter SIEM (TC-AC-ACC-380)

34. Klik Filter dan lihat placeholder field SIEM
35. Verifikasi placeholder field SIEM `All statuses`
36. Buka dropdown SIEM dan baca opsi
37. Verifikasi opsi memuat `Active`, `Grace`, dan `Pending`
38. Verifikasi opsi tidak memuat `Renewed`, `Rejected`, dan `Canceled`
39. Pilih opsi `Grace`, lalu klik [Apply]
40. Ketik Search `PT Sortir Gamma`, tekan Enter
41. Verifikasi baris `PT Sortir Gamma` tampil
42. Ganti isi kotak search dengan `PT Sortir Beta`, tekan Enter
43. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
44. Klik `(←)` pada kotak Search, lalu klik Filter, klik [Clear Field], dan klik [Apply]

## Notes

- Urutan blok: opsi (TC-AC-ACC-387) lebih dulu karena tanpa Search; tiga blok Filter berikutnya memakai Search yang dikosongkan di akhir tiap blok (S-09). Blok [Clear Field]/[Apply] dan `(←)` adalah langkah penghubung (S-03).
- Spec melewati sekitar 35 langkah; alasan: seluruh blok satu kelas harness dan satu dataset (Filter status produk List), blok berurutan tanpa state bersama, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA
  - TC-AC-ACC-379: precondition fixture C-FX11-2 menyebut `badge SAMS Active`, tetapi tidak menyebut apakah Search `PT Riwayat Opsi Status` dijalankan di sub-tab Active; spec mengasumsikan sub-tab Active tetap aktif.
