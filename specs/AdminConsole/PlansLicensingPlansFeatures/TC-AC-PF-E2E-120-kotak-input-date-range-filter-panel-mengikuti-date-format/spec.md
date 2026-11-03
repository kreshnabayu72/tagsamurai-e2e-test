---
id: TC-AC-PF-E2E-120-kotak-input-date-range-filter-panel-mengikuti-date-format
title: "Kotak Input Date Range Filter Panel Mengikuti Date Format General Settings pada Enam Surface"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-771
  - TC-AC-PF-772
  - TC-AC-PF-773
  - TC-AC-PF-774
  - TC-AC-PF-775
  - TC-AC-PF-776
coverage:
  web: automated
---

# Kotak Input Date Range Filter Panel Mengikuti Date Format General Settings pada Enam Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data Pre-setup (hanya dibaca, tidak diubah): Dataset Plan A (Pre-setup #21), Dataset Plan C (Pre-setup #23), Dataset Plan D (Pre-setup #24: `Growth` v5 dengan 9 client), Dataset Log D, Dataset Log C, dan Dataset Log G (Pre-setup #40, #41, #42; dipulihkan lewat Fixture BE di hook `before`). Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix pada data Pre-setup, hanya dibaca).
- Mengubah General Settings (state global, Pre-setup #44 dan #61): Date Format diatur lewat Fixture BE (disediakan tim FE/BE) pada langkah 1, 15, 29, dan 36 dengan Time Format 24-hour dan Time Zone UTC, lalu dipulihkan ke baseline (Date Format `dd MMM yy`) pada langkah 45 dan di hook `after`. Suite serial (`parallel: false`).
- Tabel iterasi Date Format dan surface (rentang yang dipilih di kalender selalu 15 Jun 2026 sampai 22 Jun 2026):

  | Date Format | TC | Surface | Field Filter |
  |---|---|---|---|
  | `dd/MM/yy` | TC-AC-PF-771 | Filter Panel tab Default sub-tab Active | `Last Modified` |
  | `dd/MM/yy` | TC-AC-PF-775 | Filter Panel modal Changelog Custom | `Date` |
  | `M/d/yy` | TC-AC-PF-772 | Filter Panel tab Custom sub-tab Active | `Last Modified` |
  | `M/d/yy` | TC-AC-PF-774 | Filter Panel modal Changelog Default | `Date` |
  | `DDD, MMM dd, yy` | TC-AC-PF-773 | Filter Panel Tab Assigned Clients `Growth` | `Assigned Date` |
  | `DDD, MMM dd, yyyy` | TC-AC-PF-776 | Filter Panel modal Changelog Global Settings | `Date` |

- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk mengatur dan memulihkan General Settings serta memulihkan Dataset Log.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-771: Filter Panel tab Default sub-tab Active

1. Atur General Settings Date Format `dd/MM/yy` lewat Fixture BE, lalu muat ulang halaman Plans & Features
2. Klik ikon Filter
3. Pada field `Last Modified` pilih rentang 15 Jun 2026 sampai 22 Jun 2026 pada kalender
4. Verifikasi Kotak input `Last Modified` menampilkan tanggal awal `15/06/26` sesuai Date Format `dd/MM/yy` (bukan `15 Jun 26` dan bukan format kalender bawaan)
5. Verifikasi Kotak input `Last Modified` menampilkan tanggal akhir `22/06/26` sesuai Date Format `dd/MM/yy`
6. Tutup Filter Panel

### TC-AC-PF-775: Filter Panel modal Changelog Custom

7. Klik tab `Custom` sub-tab `Active`
8. Klik ikon Changelog pada toolbar tab Custom
9. Klik ikon Filter
10. Pada field `Date` pilih rentang 15 Jun 2026 sampai 22 Jun 2026 pada kalender
11. Verifikasi Kotak input `Date` menampilkan tanggal awal `15/06/26` sesuai Date Format `dd/MM/yy` (bukan `15 Jun 26` dan bukan format kalender bawaan)
12. Verifikasi Kotak input `Date` menampilkan tanggal akhir `22/06/26` sesuai Date Format `dd/MM/yy`
13. Tutup Filter Panel
14. Tutup modal Changelog

### TC-AC-PF-772: Filter Panel tab Custom sub-tab Active

15. Atur General Settings Date Format `M/d/yy` lewat Fixture BE, muat ulang halaman Plans & Features, lalu klik tab `Custom` sub-tab `Active`
16. Klik ikon Filter
17. Pada field `Last Modified` pilih rentang 15 Jun 2026 sampai 22 Jun 2026 pada kalender
18. Verifikasi Kotak input `Last Modified` menampilkan tanggal awal `6/15/26` sesuai Date Format `M/d/yy` (bukan `15 Jun 26` dan bukan format kalender bawaan)
19. Verifikasi Kotak input `Last Modified` menampilkan tanggal akhir `6/22/26` sesuai Date Format `M/d/yy`
20. Tutup Filter Panel

### TC-AC-PF-774: Filter Panel modal Changelog Default

21. Klik tab `Default` sub-tab `Active`
22. Klik ikon Changelog pada toolbar tab Default
23. Klik ikon Filter
24. Pada field `Date` pilih rentang 15 Jun 2026 sampai 22 Jun 2026 pada kalender
25. Verifikasi Kotak input `Date` menampilkan tanggal awal `6/15/26` sesuai Date Format `M/d/yy` (bukan `15 Jun 26` dan bukan format kalender bawaan)
26. Verifikasi Kotak input `Date` menampilkan tanggal akhir `6/22/26` sesuai Date Format `M/d/yy`
27. Tutup Filter Panel
28. Tutup modal Changelog

### TC-AC-PF-773: Filter Panel Tab Assigned Clients

29. Atur General Settings Date Format `DDD, MMM dd, yy` lewat Fixture BE, lalu muat ulang halaman Plans & Features
30. Buka Plan Detail `Growth`, lalu klik Tab Assigned Clients
31. Klik ikon Filter
32. Pada field `Assigned Date` pilih rentang 15 Jun 2026 sampai 22 Jun 2026 pada kalender
33. Verifikasi Kotak input `Assigned Date` menampilkan tanggal awal `Mon, Jun 15, 26` sesuai Date Format `DDD, MMM dd, yy` (bukan `15 Jun 26` dan bukan format kalender bawaan)
34. Verifikasi Kotak input `Assigned Date` menampilkan tanggal akhir `Mon, Jun 22, 26` sesuai Date Format `DDD, MMM dd, yy`
35. Tutup Filter Panel

### TC-AC-PF-776: Filter Panel modal Changelog Global Settings

36. Atur General Settings Date Format `DDD, MMM dd, yyyy` lewat Fixture BE, lalu muat ulang halaman Plans & Features
37. Klik tab `Global Settings`
38. Klik ikon Changelog di pojok kanan atas Card
39. Klik ikon Filter
40. Pada field `Date` pilih rentang 15 Jun 2026 sampai 22 Jun 2026 pada kalender
41. Verifikasi Kotak input `Date` menampilkan tanggal awal `Mon, Jun 15, 2026` sesuai Date Format `DDD, MMM dd, yyyy` (bukan `15 Jun 26` dan bukan format kalender bawaan)
42. Verifikasi Kotak input `Date` menampilkan tanggal akhir `Mon, Jun 22, 2026` sesuai Date Format `DDD, MMM dd, yyyy`
43. Tutup Filter Panel
44. Tutup modal Changelog
45. Pulihkan General Settings ke baseline (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) lewat Fixture BE

## Notes

- Urutan TC di dalam spec dikelompokkan menurut Date Format (771, 775, 772, 774, 773, 776) supaya pengaturan General Settings dan muat ulang halaman tidak diulang untuk format yang sama (S-09).
- Langkah penghubung (S-03): pengaturan dan pemulihan General Settings lewat Fixture BE disertai muat ulang halaman (langkah 1, 15, 29, 36, 45), pindah tab dan sub-tab (langkah 7, 15, 21, 37), buka Plan Detail dan Tab Assigned Clients (langkah 30), serta tutup Filter Panel dan modal Changelog (S-09). Filter tidak diterapkan; rentang hanya dipilih dan dibaca dari kotak input.
- Pembagian TC lintas spec: TC-AC-PF-549 dan TC-AC-PF-767 sampai TC-AC-PF-770 (Last Modified dan Date pada list serta Changelog) ada di spec 119.
- Alasan melewati sekitar 35 langkah (45 langkah): enam TC memakai enam surface berbeda dengan empat Date Format berbeda; tiap TC butuh pembukaan surface, pemilihan rentang, dan penutupan sendiri, dan S-01 memecah Expected menjadi `Verifikasi` tanggal awal dan tanggal akhir. Seluruh blok berkelas fungsional, satu pola, dan satu dataset. Setiap blok mengatur General Settings sendiri dan memulihkannya, sehingga blok tetap berdiri sendiri dalam satu spec.
- Temuan untuk QA:
  - TC-AC-PF-771 sampai TC-AC-PF-776 tidak menyatakan apakah rentang diterapkan lewat tombol Apply; spec hanya membaca kotak input sesuai Expected.
  - Tabel Pre-setup #61 mendaftarkan Date Format `dd/MM/yy`, `M/d/yy`, `DDD, MMM dd, yy`, dan `DDD, MMM dd, yyyy` tanpa memetakan format ke TC; spec memakai format yang tertulis di precondition tiap TC.
  - Post Condition "Tidak ada perubahan data" tidak diasersi (S-01).
