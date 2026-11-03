---
id: TC-AC-ACC-E2E-310-auto-archive-varian-term-lama-trial-dan-convert
title: "Auto-Archive Setelah Cancel Term Active Terakhir: Term Lama Purge atau Deleted, Trial Active, dan Successor Pending Hasil Convert"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-971
  - TC-AC-ACC-972
  - TC-AC-ACC-1021
  - TC-AC-ACC-1028
coverage:
  web: automated
---

# Auto-Archive Setelah Cancel Term Active Terakhir: Term Lama Purge atau Deleted, Trial Active, dan Successor Pending Hasil Convert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-971: C-FX9-3 -> `PT Cancel Akhir Purge {runId}-310` (Active; FAMS term lama Purge + term baru Active plan owner Principal; SAMS dan SIEM tidak pernah berlangganan; Partner CV Mitra Sejati; Group Area Jakarta).
  - TC-AC-ACC-972: C-FX9-4 -> `PT Cancel Akhir Deleted {runId}-310` (sama dengan C-FX9-3 dengan term lama Deleted).
  - TC-AC-ACC-1021: C-FX17-3 -> `PT Trial Tidak Menahan {runId}-310` (Active; FAMS Active satu-satunya term paid; SAMS Trial Active).
  - TC-AC-ACC-1028: C-FX18-6 -> `PT Convert Pending Batal {runId}-310` (Active; SAMS: term paid Active predecessor, Trial Converted, dan term paid hasil Convert mode Renewal Pending; FAMS dan SIEM tidak berlangganan).
- Kemampuan teknis: tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Cancel term Active dengan term lama Purge (TC-AC-ACC-971)

1. Klik sub-tab Active, ketik Search `PT Cancel Akhir Purge {runId}-310`, tekan Enter
2. Verifikasi sel FAMS `Active`
3. Verifikasi sel SAMS dan SIEM `No Subscription`
4. Klik `[Changelog]` di toolbar List, ketik Search `PT Cancel Akhir Purge {runId}-310` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Auto-Archive` (N1), lalu tutup modal
5. Buka Admin Console > Client Subscription, ketik Search `PT Cancel Akhir Purge {runId}-310`, tekan Enter, buka `⋯` baris term FAMS Active → Cancel Subscription, lalu klik `[Cancel Subscription]` pada dialog
6. Tunggu aksi selesai (Cancel Subscription)
7. Kembali ke Admin Console > Client, klik sub-tab Archived, ketik Search `PT Cancel Akhir Purge {runId}-310`, tekan Enter
8. Verifikasi `PT Cancel Akhir Purge {runId}-310` tampil di sub-tab Archived tanpa aksi manual
9. Verifikasi sel FAMS `Archive` (term Active yang di-Cancel masuk `Archive` tanpa melewati `Grace`, bukan `Purge` dari term lama)
10. Verifikasi badge `Grace` dan `Canceled` tidak tampil
11. Klik `[Changelog]` di toolbar List, ketik Search `PT Cancel Akhir Purge {runId}-310` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Auto-Archive` (N2)
12. Verifikasi N2 = N1 + 1
13. Verifikasi baris terbaru Action `Auto-Archive`, Client Name `PT Cancel Akhir Purge {runId}-310`, Field `Status`, Old Value `Active`, New Value `Archived`, Modified By `System`

### Cancel term Active dengan term lama Deleted (TC-AC-ACC-972)

14. Tutup modal Changelog, klik sub-tab Active, ketik Search `PT Cancel Akhir Deleted {runId}-310`, tekan Enter
15. Verifikasi sel FAMS `Active`
16. Verifikasi sel SAMS dan SIEM `No Subscription`
17. Klik `[Changelog]` di toolbar List, ketik Search `PT Cancel Akhir Deleted {runId}-310` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Auto-Archive` (N1), lalu tutup modal
18. Buka Admin Console > Client Subscription, ketik Search `PT Cancel Akhir Deleted {runId}-310`, tekan Enter, buka `⋯` baris term FAMS Active → Cancel Subscription, lalu klik `[Cancel Subscription]` pada dialog
19. Tunggu aksi selesai (Cancel Subscription)
20. Kembali ke Admin Console > Client, klik sub-tab Archived, ketik Search `PT Cancel Akhir Deleted {runId}-310`, tekan Enter
21. Verifikasi `PT Cancel Akhir Deleted {runId}-310` tampil di sub-tab Archived tanpa aksi manual
22. Verifikasi sel FAMS `Archive` (bukan `Deleted` dari term lama)
23. Verifikasi badge `Grace` dan `Canceled` tidak tampil
24. Klik `[Changelog]` di toolbar List, ketik Search `PT Cancel Akhir Deleted {runId}-310` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Auto-Archive` (N2)
25. Verifikasi N2 = N1 + 1
26. Verifikasi baris terbaru Action `Auto-Archive`, Client Name `PT Cancel Akhir Deleted {runId}-310`, Field `Status`, Old Value `Active`, New Value `Archived`, Modified By `System`

### Trial Active tidak mencegah Auto-Archive (TC-AC-ACC-1021)

27. Tutup modal Changelog, klik sub-tab Active, ketik Search `PT Trial Tidak Menahan {runId}-310`, tekan Enter
28. Verifikasi sel FAMS `Active`
29. Verifikasi sel SAMS `Active`
30. Buka Admin Console > Client Subscription, ketik Search `PT Trial Tidak Menahan {runId}-310`, tekan Enter, buka `⋯` baris term FAMS Active → Cancel Subscription, lalu klik `[Cancel Subscription]` pada dialog
31. Tunggu aksi selesai (Cancel Subscription)
32. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Trial Tidak Menahan {runId}-310`, tekan Enter
33. Verifikasi `PT Trial Tidak Menahan {runId}-310` tampil di sub-tab Archived (Trial Active tidak dihitung sebagai term yang mencegah Archive)
34. Verifikasi sel FAMS `Archive`
35. Verifikasi sel SAMS `Active`
36. Klik sub-tab Active, ketik Search `PT Trial Tidak Menahan {runId}-310`, tekan Enter
37. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`

### Predecessor Active dengan successor Pending hasil Convert (TC-AC-ACC-1028)

38. Klik `(←)` pada kotak Search, klik sub-tab Active, ketik Search `PT Convert Pending Batal {runId}-310`, tekan Enter
39. Verifikasi baris `PT Convert Pending Batal {runId}-310` tampil di sub-tab Active
40. Buka Admin Console > Client Subscription, cari term paid SAMS `PT Convert Pending Batal {runId}-310` berstatus Active (predecessor), lakukan Cancel Subscription, lalu konfirmasi pada dialog
41. Tunggu aksi selesai (Cancel Subscription)
42. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Convert Pending Batal {runId}-310`, tekan Enter
43. Verifikasi baris `PT Convert Pending Batal {runId}-310` tampil di sub-tab Archived (term yang dihitung, predecessor Archive dan Trial Converted, seluruhnya terminal; successor Canceled tidak dihitung)
44. Verifikasi sel SAMS `Converted`
45. Klik sub-tab Active, ketik Search `PT Convert Pending Batal {runId}-310`, tekan Enter
46. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
47. Klik sub-tab Archived, ketik Search `PT Convert Pending Batal {runId}-310`, tekan Enter, klik Company Name, buka Tab Subscription sub-tab SAMS, lalu lihat Section Subscription Details dan tabel License Quota
48. Verifikasi Status badge `Converted`
49. Verifikasi tabel License Quota memuat baris Asset dengan Total 0, Used 0, Available 0 (kuota Trial pindah ke term paid)

## Notes

- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi.
- N1 dan N2 pada TC-AC-ACC-971 dan TC-AC-ACC-972 adalah hitungan baris Action `Auto-Archive` pada Search nama Client bersuffix; nama unik membuat baseline N1 deterministik (S-12).
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (Auto-Archive via Cancel) dan data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Langkah 6, 19, 31, 41 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-1028: Langkah 2 menyebut `cari term paid SAMS ... lakukan Cancel Subscription` tanpa detail dialog; spec mengikuti Langkah TC apa adanya. Expected butir (b) menyebut sel SAMS `Converted` sebagai `term terakhir yang bukan terminal riwayat`; wording ambigu.
