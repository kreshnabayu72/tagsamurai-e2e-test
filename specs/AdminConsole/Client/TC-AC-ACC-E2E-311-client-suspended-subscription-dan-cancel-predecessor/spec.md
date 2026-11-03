---
id: TC-AC-ACC-E2E-311-client-suspended-subscription-dan-cancel-predecessor
title: "Client Suspended dengan Perubahan Subscription dan Cancel Predecessor: Status Entitas Independen, Add Subscription, Renewal, dan Successor Ikut Canceled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-438
  - TC-AC-ACC-671
  - TC-AC-ACC-673
  - TC-AC-ACC-674
  - TC-AC-ACC-675
coverage:
  web: automated
---

# Client Suspended dengan Perubahan Subscription dan Cancel Predecessor: Status Entitas Independen, Add Subscription, Renewal, dan Successor Ikut Canceled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-438: C-ISO-11 -> `PT Dua Produk Uji {runId}-311` (Active; FAMS Active dan SAMS Active; Partner CV Mitra Sejati; Group Area Jakarta).
  - TC-AC-ACC-671: C-LIF-12 -> `PT Suspend Tanpa Produk {runId}-311` (Suspended; FAMS Active; SAMS dan SIEM tidak pernah berlangganan; Default User Activated).
  - TC-AC-ACC-673: C-LIF-13 -> `PT Suspend Kedaluwarsa {runId}-311` (Suspended; FAMS satu-satunya term Expired yang memenuhi syarat Renewal).
  - TC-AC-ACC-674: C-LIF-14 -> `PT Renewal Terjadwal {runId}-311` (Active; FAMS predecessor Active + Renewal Pending dengan tanggal mulai di masa depan, terotorisasi).
  - TC-AC-ACC-675: C-LIF-15 -> `PT Renewal Menunggu {runId}-311` (Active; FAMS predecessor Active + Renewal Waiting for Approval).
- Data Add Subscription TC-AC-ACC-671 (SIEM mode New, terotorisasi langsung) dan Renewal TC-AC-ACC-673 (terotorisasi langsung): Plan, Duration, dan Start Date disediakan tim FE karena Data Uji TC tidak menyebut nilai (lihat Temuan untuk QA).
- Kemampuan teknis: tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Status entitas dan status subscription independen (TC-AC-ACC-438)

1. Ketik Search `PT Dua Produk Uji {runId}-311`, tekan Enter, buka `⋯` baris itu → Suspend, lalu klik `[Suspend]`
2. Tunggu aksi selesai (Suspend)
3. Buka Admin Console > Client Subscription, ketik Search `PT Dua Produk Uji {runId}-311`, tekan Enter, buka `⋯` baris term SAMS Active → Cancel Subscription, lalu klik `[Cancel Subscription]` pada dialog
4. Tunggu aksi selesai (Cancel Subscription)
5. Muat ulang Admin Console > Client, klik sub-tab Suspended, ketik Search `PT Dua Produk Uji {runId}-311`, tekan Enter
6. Verifikasi baris `PT Dua Produk Uji {runId}-311` tetap di sub-tab Suspended
7. Verifikasi sel FAMS `Active`
8. Verifikasi sel SAMS `Archive`
9. Klik Company Name `PT Dua Produk Uji {runId}-311`
10. Verifikasi badge status entitas di Detail `Suspended`

### Add Subscription mode New pada Client Suspended (TC-AC-ACC-671)

11. Buka Admin Console > Client Subscription dan tambah subscription SIEM mode New yang terotorisasi langsung untuk `PT Suspend Tanpa Produk {runId}-311`
12. Tunggu aksi selesai (Add Subscription)
13. Kembali ke Admin Console > Client, klik sub-tab Suspended, ketik Search `PT Suspend Tanpa Produk {runId}-311`, tekan Enter
14. Verifikasi `PT Suspend Tanpa Produk {runId}-311` tetap tampil di sub-tab Suspended
15. Verifikasi sel SIEM `Active` (severity success)
16. Verifikasi sel FAMS tetap `Active`
17. Buka menu `⋯` pada baris `PT Suspend Tanpa Produk {runId}-311`
18. Verifikasi menu `⋯` memuat `Detail | Unsuspend`
19. Klik Company Name `PT Suspend Tanpa Produk {runId}-311`, Tab Subscription, sub-tab SIEM
20. Verifikasi badge status entitas Detail tetap `Suspended` (severity warning)
21. Verifikasi sub-tab SIEM menampilkan Status badge `Active`

### Renewal pada Client Suspended (TC-AC-ACC-673)

22. Klik `(←)` pada kotak Search, klik sub-tab Suspended, ketik Search `PT Suspend Kedaluwarsa {runId}-311`, tekan Enter
23. Verifikasi sel FAMS `Expired` (severity danger)
24. Buka Admin Console > Client Subscription dan lakukan Renewal FAMS `PT Suspend Kedaluwarsa {runId}-311` yang terotorisasi langsung
25. Tunggu aksi selesai (Renewal)
26. Kembali ke Admin Console > Client, klik sub-tab Suspended, ketik Search `PT Suspend Kedaluwarsa {runId}-311`, tekan Enter
27. Verifikasi sel FAMS `Active` (severity success)
28. Verifikasi baris `PT Suspend Kedaluwarsa {runId}-311` tetap di sub-tab Suspended
29. Buka menu `⋯` pada baris `PT Suspend Kedaluwarsa {runId}-311`
30. Verifikasi menu `⋯` memuat `Detail | Unsuspend`

### Cancel predecessor saat Renewal Pending belum aktif (TC-AC-ACC-674)

31. Klik `(←)` pada kotak Search, klik sub-tab Active, ketik Search `PT Renewal Terjadwal {runId}-311`, tekan Enter
32. Verifikasi sel FAMS `Active` (term predecessor; Renewal Pending belum menggantikan)
33. Buka Admin Console > Client Subscription dan Cancel term FAMS predecessor `PT Renewal Terjadwal {runId}-311`
34. Tunggu aksi selesai (Cancel Subscription)
35. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Renewal Terjadwal {runId}-311`, tekan Enter
36. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (baris tidak tampil di sub-tab Active)
37. Klik sub-tab Archived, ketik Search `PT Renewal Terjadwal {runId}-311`, tekan Enter
38. Verifikasi `PT Renewal Terjadwal {runId}-311` tampil di sub-tab Archived
39. Verifikasi sel FAMS `Archive` (term predecessor)
40. Verifikasi successor `Canceled` tidak tampil sebagai badge
41. Klik `[Changelog]` di toolbar List, ketik Search `PT Renewal Terjadwal {runId}-311` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
42. Verifikasi hasil Search memuat baris Action `Auto-Archive` (Old Value `Active`, New Value `Archived`, Modified By `System`) untuk `PT Renewal Terjadwal {runId}-311`

### Cancel predecessor saat Renewal Waiting for Approval (TC-AC-ACC-675)

43. Tutup modal Changelog, klik sub-tab Active, ketik Search `PT Renewal Menunggu {runId}-311`, tekan Enter
44. Verifikasi sel FAMS `Active` (term predecessor; Renewal Waiting for Approval belum menggantikan)
45. Buka Admin Console > Client Subscription dan Cancel term FAMS predecessor `PT Renewal Menunggu {runId}-311`
46. Tunggu aksi selesai (Cancel Subscription)
47. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Renewal Menunggu {runId}-311`, tekan Enter
48. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (baris tidak tampil di sub-tab Active)
49. Klik sub-tab Archived, ketik Search `PT Renewal Menunggu {runId}-311`, tekan Enter
50. Verifikasi `PT Renewal Menunggu {runId}-311` tampil di sub-tab Archived
51. Verifikasi sel FAMS `Archive` (term predecessor)
52. Verifikasi successor `Canceled` tidak tampil sebagai badge
53. Klik `[Changelog]` di toolbar List, ketik Search `PT Renewal Menunggu {runId}-311` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
54. Verifikasi hasil Search memuat baris Action `Auto-Archive` (Old Value `Active`, New Value `Archived`, Modified By `System`) untuk `PT Renewal Menunggu {runId}-311`

## Notes

- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi.
- Pemulihan Post Condition TC (`Seed ulang`) dipenuhi hook `before`/`after`.
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (perubahan subscription Client) dan data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Langkah 2, 4, 12, 25, 34, 46 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-671, 673: Data Uji hanya menyebut `SIEM mode New`/`Renewal terotorisasi langsung` tanpa Plan, Duration, dan Start Date; nilai disediakan tim FE.
  - TC-AC-ACC-438: Langkah 1 `Suspend → [Suspend]` tidak menyebut dialog; spec memakai nama aksi dan tombol TC.
  - TC-AC-ACC-674, 675: Langkah `Cancel term FAMS predecessor` tidak menyebut dialog; spec mengikuti Langkah TC.
