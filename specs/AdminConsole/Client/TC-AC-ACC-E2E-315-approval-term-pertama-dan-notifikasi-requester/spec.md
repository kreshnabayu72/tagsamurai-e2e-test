---
id: TC-AC-ACC-E2E-315-approval-term-pertama-dan-notifikasi-requester
title: "Approvals Term Pertama Mode New: Approve Menjadi Active dengan Activation Email, Reject Kembali ke No Subscription, dan Notifikasi ke Requester"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-667
  - TC-AC-ACC-668
  - TC-AC-ACC-449
coverage:
  web: automated
---

# Approvals Term Pertama Mode New: Approve Menjadi Active dengan Activation Email, Reject Kembali ke No Subscription, dan Notifikasi ke Requester

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-667: C-LIF-10 -> `PT Menunggu Setuju A {runId}-315` (Active; FAMS satu-satunya term Waiting for Approval mode New, requester bukan GM/TC; Default User Not Yet Activated, email inbox dapat dibaca mail-catcher).
  - TC-AC-ACC-668: C-LIF-11 -> `PT Menunggu Setuju B {runId}-315` (sama dengan C-LIF-10 untuk Reject).
  - TC-AC-ACC-449: dua Client bersuffix `PT Notif Approve {runId}-315` dan `PT Notif Reject {runId}-315` dengan masing-masing satu term FAMS Waiting for Approval (requester akun non-GM/TC `disediakan tim FE`, TC tidak menyebut akunnya).
- Kemampuan teknis: mail-catcher untuk membaca inbox Default User dengan baseline jumlah email sebelum aksi (R-11); membaca jumlah notifikasi Unread requester (akun requester disediakan tim FE). Aksi Approve dan Reject dilakukan Total Control di Admin Console > Approvals > Client Subscription.

## Test Steps

### Approve term pertama (TC-AC-ACC-667)

1. Catat jumlah email di inbox Default User `PT Menunggu Setuju A {runId}-315` lewat mail-catcher (baseline)
2. Klik sub-tab Active, ketik Search `PT Menunggu Setuju A {runId}-315`, tekan Enter
3. Verifikasi sel FAMS `Waiting for Approval` (severity warning)
4. Buka Admin Console > Approvals > Client Subscription dan Approve permintaan FAMS `PT Menunggu Setuju A {runId}-315`
5. Tunggu aksi selesai
6. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Menunggu Setuju A {runId}-315`, tekan Enter
7. Verifikasi sel FAMS `Active` (severity success)
8. Klik Company Name `PT Menunggu Setuju A {runId}-315`, Tab Subscription, sub-tab FAMS
9. Verifikasi Status badge `Active` pada Section Subscription Details
10. Periksa inbox email Default User lewat mail-catcher
11. Verifikasi satu Activation Email baru diterima Default User dibandingkan baseline (term pertama Client)

### Reject term pertama (TC-AC-ACC-668)

12. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Menunggu Setuju B {runId}-315`, tekan Enter
13. Verifikasi sel FAMS `Waiting for Approval` (severity warning)
14. Buka Admin Console > Approvals > Client Subscription dan Reject permintaan FAMS `PT Menunggu Setuju B {runId}-315`
15. Tunggu aksi selesai
16. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Menunggu Setuju B {runId}-315`, tekan Enter
17. Verifikasi sel FAMS berisi teks `No Subscription` (teks sel, bukan badge)
18. Verifikasi label `Rejected` tidak tampil
19. Klik Company Name `PT Menunggu Setuju B {runId}-315` dan lihat section Default User
20. Verifikasi badge `Not Yet Activated` pada section Default User
21. Verifikasi `[Resend Activation Email]` Hidden

### Notifikasi ke requester pada Approve dan Reject (TC-AC-ACC-449)

22. Ganti akun: login sebagai requester non-GM/TC (disediakan tim FE), buka dropdown notifikasi, catat jumlah Unread (N1), lalu logout
23. Ganti akun: login sebagai Total Control (A-01), buka Admin Console > Approvals > Client Subscription, lalu Approve term FAMS `PT Notif Approve {runId}-315`
24. Tunggu aksi selesai
25. Ganti akun: login sebagai requester, buka dropdown notifikasi, dan catat jumlah Unread (N2)
26. Verifikasi N2 = N1 + 1 (requester menerima notifikasi hasil Approve)
27. Logout, login sebagai Total Control (A-01), buka Admin Console > Approvals > Client Subscription, lalu Reject term FAMS `PT Notif Reject {runId}-315`
28. Tunggu aksi selesai
29. Ganti akun: login sebagai requester, buka dropdown notifikasi, dan catat jumlah Unread (N3)
30. Verifikasi N3 = N2 + 1 (requester menerima notifikasi hasil Reject)
31. Logout, login sebagai Total Control (A-01)

## Notes

- Spec berisi ganti akun eksplisit di blok ketiga (TC-AC-ACC-449); blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal (prinsip 3, pengecualian butir b). Akun requester dan password-nya disediakan tim FE (`Spectra.env` ditentukan tim FE; tidak ada nama env yang dikarang di spec ini).
- Langkah penghubung (S-03): ganti akun dan logout adalah pemulihan sesi (S-07) tanpa asersi; hook `after` mengembalikan sesi ke akun default suite.
- Lintas modul: Approvals berada di modul lain; TC-AC-ACC-667, 668, dan 449 sama-sama menguji dampak Approve/Reject pada Client dan dicatat di spec modul Approvals sebagai rujukan silang bila ada.
- Temuan untuk QA
  - TC-AC-ACC-449: Langkah `Approve dan Reject term dari Approvals` tanpa Client, requester, atau isi notifikasi; Expected hanya `Requester menerima notifikasi pada kedua hasil`. Spec mengasersi penambahan satu notifikasi Unread per hasil; judul dan isi notifikasi tidak diasersi karena tidak disebut TC.
  - TC-AC-ACC-667: Expected (d) `Satu Activation Email diterima Default User` mengandalkan inbox email asli (label `Manual Only (c)`); spec memakai mail-catcher dengan baseline jumlah email.
