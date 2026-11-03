---
id: TC-AC-ACC-E2E-312-auto-reactivate-client-archived
title: "Auto-Reactivate Client Archived: Add Subscription Mode New, Permintaan Di-Reject atau Di-Approve, dan Trial Tidak Memicu Reaktivasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-437
  - TC-AC-ACC-1018
  - TC-AC-ACC-1019
  - TC-AC-ACC-1029
coverage:
  web: automated
---

# Auto-Reactivate Client Archived: Add Subscription Mode New, Permintaan Di-Reject atau Di-Approve, dan Trial Tidak Memicu Reaktivasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-437: C-04 `PT Karya Abadi` -> `PT Karya Abadi Uji {runId}-312` (Archived; FAMS Archive; Partner CV Mitra Sejati; Group Area Jakarta).
  - TC-AC-ACC-1018: C-FX17-1 -> `PT Arsip Menunggu Tolak {runId}-312` (Archived; FAMS Archive sebagai term sebelumnya; permintaan FAMS baru mode New Waiting for Approval, requester bukan GM/TC).
  - TC-AC-ACC-1019: C-FX17-2 -> `PT Arsip Menunggu Setuju {runId}-312` (Archived; sama dengan C-FX17-1 dengan Start Date hari ini).
  - TC-AC-ACC-1029: C-FX18-7 -> `PT Arsip Aktifkan Trial {runId}-312` (Archived; FAMS Archive satu-satunya term; SAMS dan SIEM tidak pernah berlangganan).
- Data Activate Trial TC-AC-ACC-1029: SAMS; Plan Growth; Trial Duration 14 day(s); Trial Asset Quota 10; Trial Concurrent User Quota 5 (dalam ceiling Trial). Data Add Subscription TC-AC-ACC-437 (FAMS mode New terotorisasi langsung): Plan, Duration, dan Start Date disediakan tim FE.
- Kemampuan teknis: tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Add Subscription pada Client Archived (TC-AC-ACC-437)

1. Klik sub-tab Archived, ketik Search `PT Karya Abadi Uji {runId}-312`, tekan Enter, lalu buka `⋯` baris itu
2. Verifikasi menu `⋯` memuat `Detail | Edit | Delete`
3. Buka Admin Console > Client Subscription dan tambah term FAMS mode New yang terotorisasi langsung pada `PT Karya Abadi Uji {runId}-312`
4. Tunggu aksi selesai (Add Subscription)
5. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Karya Abadi Uji {runId}-312`, tekan Enter
6. Verifikasi `PT Karya Abadi Uji {runId}-312` tampil di sub-tab Active
7. Verifikasi sel FAMS `Active`
8. Buka `⋯` baris `PT Karya Abadi Uji {runId}-312`
9. Verifikasi menu `⋯` memuat `Detail | Edit | Change Partner | Suspend`
10. Verifikasi `Delete` tidak ada pada menu
11. Klik `[Changelog]` di toolbar List, ketik Search `PT Karya Abadi Uji {runId}-312` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
12. Verifikasi hasil Search memuat baris baru Action `Auto-Reactivate`, Client Name `PT Karya Abadi Uji {runId}-312`, Field `Status`, Old Value `Archived`, New Value `Active`, Modified By `System`

### Permintaan di-Reject, Client tetap Archived (TC-AC-ACC-1018)

13. Tutup modal Changelog, klik sub-tab Archived, ketik Search `PT Arsip Menunggu Tolak {runId}-312`, tekan Enter
14. Verifikasi baris `PT Arsip Menunggu Tolak {runId}-312` tampil di sub-tab Archived
15. Verifikasi sel FAMS `Waiting for Approval`
16. Klik sub-tab Active, ketik Search `PT Arsip Menunggu Tolak {runId}-312`, tekan Enter
17. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (term Waiting for Approval belum memicu Auto-Reactivate)
18. Klik `[Changelog]` di toolbar List, ketik Search `PT Arsip Menunggu Tolak {runId}-312` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Auto-Reactivate` (N1), lalu tutup modal
19. Buka Admin Console > Approvals > Client Subscription dan Reject permintaan FAMS `PT Arsip Menunggu Tolak {runId}-312`
20. Tunggu aksi selesai (Reject)
21. Kembali ke Admin Console > Client, klik sub-tab Archived, ketik Search `PT Arsip Menunggu Tolak {runId}-312`, tekan Enter
22. Verifikasi baris `PT Arsip Menunggu Tolak {runId}-312` tetap tampil di sub-tab Archived
23. Verifikasi sel FAMS `Archive` (status term sebelumnya; label `Rejected` tidak tampil)
24. Klik sub-tab Active, ketik Search `PT Arsip Menunggu Tolak {runId}-312`, tekan Enter
25. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
26. Klik `[Changelog]` di toolbar List, ketik Search `PT Arsip Menunggu Tolak {runId}-312` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
27. Hitung baris Action `Auto-Reactivate` untuk `PT Arsip Menunggu Tolak {runId}-312` pada hasil Search (N2)
28. Verifikasi N2 = N1 (tidak ada baris Action `Auto-Reactivate` baru)

### Permintaan di-Approve menjadi Active (TC-AC-ACC-1019)

29. Tutup modal Changelog, klik sub-tab Archived, ketik Search `PT Arsip Menunggu Setuju {runId}-312`, tekan Enter
30. Verifikasi baris `PT Arsip Menunggu Setuju {runId}-312` tampil di sub-tab Archived
31. Verifikasi sel FAMS `Waiting for Approval`
32. Klik sub-tab Active, ketik Search `PT Arsip Menunggu Setuju {runId}-312`, tekan Enter
33. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (baris tidak tampil di sub-tab Active)
34. Buka Admin Console > Approvals > Client Subscription dan Approve permintaan FAMS `PT Arsip Menunggu Setuju {runId}-312`
35. Tunggu aksi selesai (Approve)
36. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Arsip Menunggu Setuju {runId}-312`, tekan Enter
37. Verifikasi baris `PT Arsip Menunggu Setuju {runId}-312` tampil di sub-tab Active
38. Verifikasi sel FAMS `Active`
39. Klik `[Changelog]` di toolbar List, ketik Search `PT Arsip Menunggu Setuju {runId}-312` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
40. Verifikasi hasil Search memuat baris Action `Auto-Reactivate` (Field `Status`, Old Value `Archived`, New Value `Active`, Modified By `System`)

### Trial Active tidak memicu Auto-Reactivate (TC-AC-ACC-1029)

41. Tutup modal Changelog, klik sub-tab Archived, ketik Search `PT Arsip Aktifkan Trial {runId}-312`, tekan Enter
42. Verifikasi sel SAMS berisi teks `No Subscription` (teks sel, bukan badge)
43. Buka Admin Console > Client Subscription, klik `[+ Activate Trial]`, pilih Client `PT Arsip Aktifkan Trial {runId}-312`, Product SAMS, isi Trial Duration, Trial Asset Quota, dan Trial Concurrent User Quota sesuai Data Uji, lalu klik Submit
44. Tunggu aksi selesai (Activate Trial)
45. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Arsip Aktifkan Trial {runId}-312`, tekan Enter
46. Verifikasi baris `PT Arsip Aktifkan Trial {runId}-312` tetap tampil di sub-tab Archived
47. Verifikasi sel SAMS `Active` (baris Trial)
48. Klik sub-tab Active, ketik Search `PT Arsip Aktifkan Trial {runId}-312`, tekan Enter
49. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (tidak ada Auto-Reactivate)

## Notes

- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi.
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (Auto-Reactivate) dan data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Absence `Auto-Reactivate` pada TC-AC-ACC-1018 (kelas g) berada di spec ini dengan P-1 (state berat: permintaan Reject dibangun di spec ini); anchor positif memakai baris `PT Arsip Menunggu Tolak {runId}-312` yang tampil di sub-tab Archived dan baseline hitungan N1 sebelum aksi (S-12).
- Langkah penghubung (S-03, R-16): Langkah 4, 20, 35, 44 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-437: Data Uji TC kosong (Plan, Duration, Start Date term baru).
  - TC-AC-ACC-1018: Expected butir (e) `hasil Search tidak memuat baris Action Auto-Reactivate` tanpa baseline; spec mencatat jumlah baris sebelum Reject (N1) dan membandingkannya dengan sesudah Reject (N2).
