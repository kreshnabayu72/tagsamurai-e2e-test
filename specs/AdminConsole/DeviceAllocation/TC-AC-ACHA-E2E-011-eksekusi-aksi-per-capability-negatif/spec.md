---
id: TC-AC-ACHA-E2E-011-eksekusi-aksi-per-capability-negatif
title: "Role Matrix Negatif: Aksi Tidak Tersedia untuk Hak Parsial, Non-Creator, dan Perubahan Hak di Tengah Sesi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-59
  - TC-AC-ACHA-63
  - TC-AC-ACHA-64
  - TC-AC-ACHA-65
  - TC-AC-ACHA-66
  - TC-AC-ACHA-67
  - TC-AC-ACHA-68
  - TC-AC-ACHA-69
coverage:
  web: automated
---

# Role Matrix Negatif: Aksi Tidak Tersedia untuk Hak Parsial, Non-Creator, dan Perubahan Hak di Tengah Sesi

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-59 | Create dan Read tanpa Update Distributor PT Global Distribusi (alias CO_DIST) | #35 | `createOnlyDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_CO_DIST_PASSWORD` |
| TC-63 | Update dan Read tanpa Create Distributor (alias UO_DIST) | #36 | `updateOnlyDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_UO_DIST_PASSWORD` |
| TC-64, TC-66 | Total Control Distributor (alias TC_DIST, bukan creator) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| TC-65 | Group Member Distributor toggle OFF (nama pengguna Citra Anggraini) | #33 | `memberOffDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_OFF_PASSWORD` |
| TC-69 | Additional Approver Distributor tanpa capability Manage allocation (Bambang Prasetyo) | #37 | `additionalApprover_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_ADD_APPROVER_PASSWORD` |
| TC-67, TC-68 | Group Member Distributor toggle ON (alias MB_ON, Budi Santoso), hak diturunkan menjadi Read Only | #32 | `memberOnDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_ON_PASSWORD` |

- Login akun aktor pertama (CO_DIST) di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`) dan memulihkan hak MB_ON serta seed lewat fixture Pre-setup #20 (Lampiran A butir A-6). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit dan langkah tiap role berbeda.
- Hook suite: sesi API aktor, flag Guided Tooltip, pemulihan preferensi Setup Column, seed 30 baris idempotent (Lampiran A butir A-6), dan fixture Pre-setup #20 dinyatakan di `suite.md` (endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca kecuali disebut): Seed 30 alokasi (Pre-setup #48); transaksi Waiting for Approval milik CO_DIST (Pre-setup #68, TC-59: satu transaksi Waiting for Approval milik sendiri dan satu Canceled; yang dipakai adalah yang Waiting for Approval); transaksi Canceled milik UO_DIST untuk TC-63 (Pre-setup #48 tidak memuatnya; TC-63 membaca "transaksi Canceled milik sendiri" tanpa menyebut Pre-setup, lihat Temuan untuk QA); transaksi Waiting for Approval milik MB_ON (Pre-setup #49, TC-64, TC-65, TC-67, TC-68); transaksi Canceled milik MB_ON (Pre-setup #52, TC-66, TC-67). Allocation ID dibaca lewat fixture seed (disediakan tim FE/BE), tidak di-hardcode.
- Kemampuan teknis: fixture API Pre-setup #20 menurunkan hak MB_ON menjadi Read Only dan memulihkannya (hak Manage allocation Create, Read, Update di Group Jakarta toggle ON) tanpa memuat ulang sesi UI (TC-67, TC-68); pemulihan hak dijalankan sebagai langkah penghubung sesudah TC-67 dan di hook `after`. Pelaku kedua penurun hak memakai sesi API (bukan sesi UI), dan langkah pemicunya ditulis "... hingga tersimpan" (R-20).
- State global: hak role MB_ON diubah dan dipulihkan; suite berjalan serial. Status transaksi Pre-setup #49 tidak diubah (aksi Cancel pada TC-68 ditolak server).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var lain pada tabel "Role yang diuji" belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-59: Hak Create saja tidak dapat Edit atau Cancel transaksi sendiri

1. Ketik Search `Allocation ID` transaksi Waiting for Approval milik CO_DIST (Pre-setup #68), tekan Enter
2. Klik `[⋯]` pada baris hasil
3. Verifikasi menu hanya memuat `Allocation Log`
4. Verifikasi `Edit` Hidden
5. Verifikasi `Cancel Allocation` Hidden
6. Tekan Esc untuk menutup menu
7. Klik `(←)` pada kotak Search

### Ganti akun ke Update saja

8. Logout dari akun CO_DIST
9. Login sebagai UO_DIST (`updateOnlyDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_UO_DIST_PASSWORD`)
10. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-63: Hak Update saja tidak dapat membuat atau Resubmit

11. Amati Table Tools dan menu row action transaksi Canceled milik UO_DIST
12. Verifikasi sedikitnya satu ikon Table Tools (Search, Filter, atau Download) tampil
13. Verifikasi tombol `[+ Allocation]` Hidden
14. Ketik Search `Allocation ID` transaksi Canceled milik UO_DIST, tekan Enter
15. Klik `[⋯]` pada baris hasil
16. Verifikasi aksi `Allocation Log` Show pada menu
17. Verifikasi `Resubmit` Hidden pada transaksi Canceled milik sendiri (Resubmit membutuhkan Create)
18. Tekan Esc untuk menutup menu
19. Klik `(←)` pada kotak Search

### Ganti akun ke Total Control Distributor

20. Logout dari akun UO_DIST
21. Login sebagai TC_DIST (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)
22. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-64: Non-creator Total Control tidak melihat Edit dan Cancel transaksi orang lain

23. Ketik Search `Allocation ID` transaksi Waiting for Approval milik MB_ON (Pre-setup #49), tekan Enter
24. Klik `[⋯]` pada baris hasil
25. Verifikasi menu hanya memuat `Allocation Log`
26. Verifikasi `Edit` Hidden total (tidak dirender)
27. Verifikasi `Cancel Allocation` Hidden total (tidak dirender)
28. Tekan Esc untuk menutup menu

### TC-AC-ACHA-66: Non-creator tidak melihat Resubmit

29. Ganti isi kotak search dengan `Allocation ID` transaksi Canceled milik MB_ON (Pre-setup #52), tekan Enter
30. Klik `[⋯]` pada baris hasil
31. Verifikasi aksi `Allocation Log` Show pada menu
32. Verifikasi `Resubmit` Hidden total walau aktor Total Control punya izin Create alokasi secara umum
33. Tekan Esc untuk menutup menu
34. Klik `(←)` pada kotak Search

### Ganti akun ke Group Member toggle OFF

35. Logout dari akun TC_DIST
36. Login sebagai Citra Anggraini (`memberOffDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_MB_OFF_PASSWORD`)
37. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-65: Sesama role bukan creator tidak melihat Edit dan Cancel

38. Ketik Search `Allocation ID` transaksi Waiting for Approval milik MB_ON (Pre-setup #49), tekan Enter
39. Klik `[⋯]` pada baris hasil
40. Verifikasi aksi `Allocation Log` Show pada menu
41. Verifikasi `Edit` Hidden
42. Verifikasi `Cancel Allocation` Hidden (pengguna lain, meskipun sesama role, tidak dapat membatalkan transaksi creator lain)
43. Tekan Esc untuk menutup menu
44. Klik `(←)` pada kotak Search

### Ganti akun ke Additional Approver

45. Logout dari akun Citra Anggraini
46. Login sebagai Additional Approver (`additionalApprover_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_ADD_APPROVER_PASSWORD`)

### TC-AC-ACHA-69: Additional Approver tanpa hak ekstra di menu Device Allocation

47. Amati sidebar menu Allocation (akun berada di Dashboard Admin Console setelah login)
48. Verifikasi item menu Dashboard tampil di sidebar
49. Verifikasi item `Allocation > Device Allocation` Hidden (Additional Approver tidak mendapat hak ekstra di menu ini)
50. Buka menu Approvals > Device Allocation
51. Verifikasi menu Approvals > Device Allocation tersedia dan halaman terbuka untuk bertindak sebagai approver

### Ganti akun ke MB_ON

52. Logout dari akun Additional Approver
53. Login sebagai MB_ON (`memberOnDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_MB_ON_PASSWORD`)
54. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-67: Creator yang kehilangan Create dan Update tidak melihat aksi transaksinya

55. Turunkan hak MB_ON menjadi Read Only lewat fixture Pre-setup #20 (di tengah sesi) hingga tersimpan
56. Muat ulang halaman Allocation > Device Allocation (F5)
57. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil
58. Verifikasi tombol `[+ Allocation]` Hidden
59. Ketik Search `Allocation ID` transaksi Waiting for Approval milik MB_ON (Pre-setup #49), tekan Enter
60. Klik `[⋯]` pada baris hasil
61. Verifikasi menu hanya memuat `Allocation Log`
62. Verifikasi `Edit` Hidden
63. Verifikasi `Cancel Allocation` Hidden
64. Tekan Esc untuk menutup menu
65. Ganti isi kotak search dengan `Allocation ID` transaksi Canceled milik MB_ON (Pre-setup #52), tekan Enter
66. Klik `[⋯]` pada baris hasil
67. Verifikasi aksi `Allocation Log` Show pada menu
68. Verifikasi `Resubmit` Hidden (otorisasi dievaluasi saat aksi)
69. Tekan Esc untuk menutup menu
70. Klik `(←)` pada kotak Search
71. Pulihkan hak MB_ON ke Manage allocation (Create, Read, Update, Group Jakarta, toggle ON) lewat fixture Pre-setup #20 hingga tersimpan
72. Muat ulang halaman Allocation > Device Allocation (F5)

### TC-AC-ACHA-68: Aksi dari UI basi setelah hak diturunkan ditolak server

73. Ketik Search `Allocation ID` transaksi Waiting for Approval milik MB_ON (Pre-setup #49), tekan Enter
74. Klik `[⋯]` pada baris hasil, biarkan halaman tetap terbuka
75. Verifikasi `Cancel Allocation` Show pada menu
76. Turunkan hak MB_ON menjadi Read Only lewat fixture Pre-setup #20 hingga tersimpan, tanpa memuat ulang halaman
77. Klik `Cancel Allocation` pada baris yang sudah terbuka
78. Klik `[Cancel Allocation]` pada dialog
79. Verifikasi toast error "You don't have permission to do this."
80. Verifikasi status transaksi tetap `Waiting for Approval`
81. Verifikasi UI di-refresh sehingga tombol `[+ Allocation]` Hidden
82. Klik `[⋯]` pada baris hasil
83. Verifikasi aksi `Allocation Log` Show pada menu
84. Verifikasi `Cancel Allocation` Hidden pada menu baris
85. Pulihkan hak MB_ON ke Manage allocation (Create, Read, Update, Group Jakarta, toggle ON) lewat fixture Pre-setup #20 hingga tersimpan
86. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec Role Matrix negatif (bagian 3a): aksi tidak tersedia (Hidden) atau ditolak server untuk role dengan hak parsial, non-creator, dan perubahan hak di tengah sesi. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit dan langkah tiap role berbeda.
- Urutan TC di spec: TC-59, TC-63, TC-64, TC-66, TC-65, TC-69, TC-67, TC-68 (penyimpangan dari urutan nomor, S-05): dikelompokkan per akun agar jumlah ganti akun minimal; TC-67 dan TC-68 terakhir karena menurunkan hak MB_ON (pemulihan hak dijalankan sebagai langkah penghubung sesudah masing-masing TC, langkah terakhir TC-67 dan TC-68).
- Langkah penghubung (S-03): langkah Search untuk menemukan transaksi target, `(←)` yang mereset Search, `Esc` yang menutup menu, langkah ganti akun (subjudul "Ganti akun ..."), muat ulang halaman, dan langkah pemulihan hak MB_ON. Anchor absence (bagian 8b butir 2): asersi `Edit`, `Cancel Allocation`, dan `Resubmit` Hidden didahului `Verifikasi` aksi `Allocation Log` Show pada menu row action yang sama (atau "menu hanya memuat `Allocation Log`"); asersi menu `Allocation > Device Allocation` Hidden pada TC-69 didahului `Verifikasi` item Dashboard tampil. Pada TC-68, menu baris dibuka ulang sesudah penolakan server dan `Cancel Allocation` Hidden didahului `Verifikasi` aksi `Allocation Log` Show.
- Anchor positif (S-02, bagian 8b butir 2): `Verifikasi` ikon Table Tools tampil (langkah 12 dan 57) membuktikan toolbar List termuat sebelum asersi `[+ Allocation]` Hidden (langkah 13 dan 58); keduanya adalah asersi tambahan atas TC dengan alasan anchor absence.
- P-1 tidak dipakai. Pelaku kedua penurun hak (TC-67, TC-68) memakai sesi API melalui fixture, bukan konteks kedua UI (tidak butuh P-2).
- Pembagian TC lintas spec: kasus positif untuk capability yang sama (TC-58, TC-60, TC-61, TC-62) ada di spec 010; TC-70 (Group Manager group lain) ada di spec 020; kasus pembatalan Cancel dan Edit sukses di spec 026 dan 029.
- Ukuran spec (di atas sekitar 35 langkah): satu topik (negatif per capability) dengan tiap Expected menjadi `Verifikasi` sendiri (S-01) dan enam akun berbeda dengan ganti akun eksplisit; bagian sesudah ganti akun tetap bermakna bila bagian sebelumnya gagal keras karena tiap blok mencari transaksinya sendiri (bagian 3, pemisah (b)).
- Temuan untuk QA:
  - TC-63 Langkah Uji "menu row action transaksi Canceled milik sendiri" tidak menyebut Pre-setup transaksi Canceled milik UO_DIST (#60 adalah Waiting for Approval; #68 milik CO_DIST). Spec membaca transaksi Canceled milik UO_DIST lewat fixture seed (disediakan tim FE/BE, tidak dikarang).
  - TC-59 Precondition menyebut Pre-setup #68 "Transaksi Waiting for Approval milik akun ini" sedangkan #68 di tabel Pre-setup berbunyi "satu transaksi Waiting for Approval milik sendiri dan satu transaksi Canceled milik sendiri" (dipakai TC-60 untuk Canceled); spec memakai yang Waiting for Approval.
  - TC-67 Expected b menyebut "otorisasi dievaluasi saat aksi" sebagai alasan; diasersi hanya sebagai Hidden aksi.
  - TC-68 Expected b memuat dua klausa (status tetap, UI di-refresh); dipisah menjadi dua `Verifikasi`. Klausa "UI di-refresh sehingga aksi yang tidak berhak tersembunyi" diasersi lewat `[+ Allocation]` Hidden dan `Cancel Allocation` Hidden pada menu baris yang dibuka ulang; TC tidak menyebut elemen mana yang diamati.
  - TC-68 Langkah Uji 3 menulis "klik `Cancel Allocation` pada baris yang sudah terbuka" dan TC-67 Dependensi menunjuk TC-68 bergantung pada TC-67; spec memulihkan hak di antaranya sehingga TC-68 berdiri sendiri.
  - TC-69 Expected b ("menu Approvals > Device Allocation tersedia") tidak punya Data Uji akun; spec memakai Pre-setup #37.
  - TC-64 dan TC-66 Data Uji menyebut Total Control Distributor bukan creator; transaksi MB_ON (Pre-setup #49, #52) tidak mencantumkan nama Allocated By untuk asersi tambahan; tidak diasersi.
  - Post Condition TC-59, TC-63 sampai TC-69 bernilai `-`.
