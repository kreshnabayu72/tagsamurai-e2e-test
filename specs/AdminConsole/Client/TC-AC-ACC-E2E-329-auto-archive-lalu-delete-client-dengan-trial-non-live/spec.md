---
id: TC-AC-ACC-E2E-329-auto-archive-lalu-delete-client-dengan-trial-non-live
title: "Auto-Archive Setelah Cancel Term Paid Terakhir dengan Trial Expired atau Waiting for Approval, Lalu Client Dihapus dari Sub-tab Archived"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-1036
  - TC-AC-ACC-1038
coverage:
  web: automated
---

# Auto-Archive Setelah Cancel Term Paid Terakhir dengan Trial Expired atau Waiting for Approval, Lalu Client Dihapus dari Sub-tab Archived

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-1036: C-FX18-9 -> `PT Paid Aktif Trial Expired {runId}-329` (Active; FAMS paid Active; SAMS Trial Expired; SIEM tidak pernah berlangganan; Group Area Jakarta).
  - TC-AC-ACC-1038: C-FX18-10 -> `PT Paid Aktif Trial Menunggu {runId}-329` (Active; FAMS paid Active; SAMS Trial Waiting for Approval dengan toggle Require Approval for Trial Activation ON; SIEM tidak pernah berlangganan; Group Area Jakarta).
- Aksi Delete menghabisi Client milik spec; Client tidak dipakai TC lain (aksi Delete di akhir spec, prinsip 5). Tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Trial Expired tidak memblokir Delete (TC-AC-ACC-1036)

1. Klik sub-tab Active, ketik Search `PT Paid Aktif Trial Expired {runId}-329`, tekan Enter
2. Verifikasi baris `PT Paid Aktif Trial Expired {runId}-329` tampil di sub-tab Active
3. Verifikasi sel FAMS `Active`
4. Verifikasi sel SAMS `Expired`
5. Buka Admin Console > Client Subscription, cari term FAMS `PT Paid Aktif Trial Expired {runId}-329` berstatus Active, lalu lakukan Cancel Subscription
6. Tunggu aksi selesai (Cancel Subscription)
7. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Paid Aktif Trial Expired {runId}-329`, tekan Enter
8. Verifikasi baris `PT Paid Aktif Trial Expired {runId}-329` tampil di sub-tab Archived (term yang dihitung, FAMS Archive dan Trial Expired, seluruhnya terminal)
9. Verifikasi sel FAMS `Archive`
10. Verifikasi sel SAMS `Expired`
11. Klik sub-tab Active, ketik Search `PT Paid Aktif Trial Expired {runId}-329`, tekan Enter
12. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`

### Trial Waiting for Approval tidak dihitung (TC-AC-ACC-1038)

13. Klik sub-tab Active, ketik Search `PT Paid Aktif Trial Menunggu {runId}-329`, tekan Enter
14. Verifikasi baris `PT Paid Aktif Trial Menunggu {runId}-329` tampil di sub-tab Active
15. Verifikasi sel FAMS `Active`
16. Verifikasi sel SAMS `Waiting for Approval`
17. Buka Admin Console > Client Subscription, cari term FAMS `PT Paid Aktif Trial Menunggu {runId}-329` berstatus Active, lalu lakukan Cancel Subscription
18. Tunggu aksi selesai (Cancel Subscription)
19. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Paid Aktif Trial Menunggu {runId}-329`, tekan Enter
20. Verifikasi baris `PT Paid Aktif Trial Menunggu {runId}-329` tampil di sub-tab Archived (Trial Waiting for Approval tidak dihitung dan tidak menahan Client di Active)
21. Verifikasi sel FAMS `Archive`
22. Verifikasi sel SAMS `Waiting for Approval`
23. Klik sub-tab Active, ketik Search `PT Paid Aktif Trial Menunggu {runId}-329`, tekan Enter
24. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`

### Delete dari sub-tab Archived (TC-AC-ACC-1036 dan TC-AC-ACC-1038)

25. Klik sub-tab Archived, ketik Search `PT Paid Aktif Trial Expired {runId}-329`, tekan Enter, buka `⋯` baris `PT Paid Aktif Trial Expired {runId}-329` → Delete, ketik nama persis `PT Paid Aktif Trial Expired {runId}-329`, centang checkbox, lalu klik `[Delete]`
26. Verifikasi tidak ada dialog blok (Trial Expired tidak memblokir Delete)
27. Verifikasi toast sukses `Success, client has been deleted.`
28. Ganti isi kotak search dengan `PT Paid Aktif Trial Expired {runId}-329`, tekan Enter
29. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
30. Ganti isi kotak search dengan `PT Paid Aktif Trial Menunggu {runId}-329`, tekan Enter, buka `⋯` baris `PT Paid Aktif Trial Menunggu {runId}-329` → Delete, ketik nama persis `PT Paid Aktif Trial Menunggu {runId}-329`, centang checkbox, lalu klik `[Delete]`
31. Verifikasi tidak ada dialog blok (Trial Waiting for Approval tidak memblokir Delete)
32. Verifikasi toast sukses `Success, client has been deleted.`
33. Ganti isi kotak search dengan `PT Paid Aktif Trial Menunggu {runId}-329`, tekan Enter
34. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`

## Notes

- Urutan TC disusun ulang (S-05 perubahan urutan dicatat): aksi Delete kedua TC ditaruh di blok terakhir karena aksi menghabisi data selalu di akhir (prinsip 3 butir 5), walau Langkah 5 TC-AC-ACC-1036 dan TC-AC-ACC-1038 menyebut Delete sesudah langkah lainnya di TC yang sama.
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (Auto-Archive via Cancel lalu Delete) dan data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi.
- Langkah penghubung (S-03, R-16): Langkah 6, 18 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-1036 dan TC-AC-ACC-1038: Langkah 2 `cari term FAMS ... lakukan Cancel Subscription` tidak menyebut dialog; spec mengikuti Langkah TC apa adanya. `Verifikasi` `tidak ada dialog blok` memakai baris menu Delete yang terbuka sebagai anchor (Delete dapat dijalankan).
