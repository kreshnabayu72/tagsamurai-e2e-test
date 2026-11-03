---
id: TC-AC-ACC-E2E-079-edit-retry-activation-email-gagal-notifikasi-dan-dihentikan-tcp
title: "Edit Email Default User: Retry Activation Email Gagal, Notifikasi Setelah Percobaan Ketiga, dan Pengulangan Dihentikan (Total Control)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-959
  - TC-AC-ACC-976
  - TC-AC-ACC-984
coverage:
  web: automated
---

# Edit Email Default User: Retry Activation Email Gagal, Notifikasi Setelah Percobaan Ketiga, dan Pengulangan Dihentikan (Total Control)

## Prerequisites

- Mode: FE+BE. Kelas harness eksternal (majukan waktu sistem, antrean percobaan ulang, mail-catcher) untuk ketiga TC.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Kemampuan teknis: memajukan waktu sistem (jam server) dan memicu antrean percobaan ulang berjalan; jam browser tidak diubah karena antrean percobaan ulang dihitung di server dan tidak diamati lewat countdown UI (bagian 6 konvensi); jam server dipulihkan ke waktu nyata di hook `after` dan sebelum membuka Activity Log atau Changelog (S-09). Memaksa email service gagal (5xx) pada setiap percobaan kirim (disediakan tim FE/BE; endpoint tidak dikarang). Membaca jumlah notifikasi berstatus Unread dan item teratas pada dropdown notifikasi navbar.
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- Dataset seed (nama bersuffix, Default User Not Yet Activated): `PT Berakhir Belum Aktivasi {runId}-079` (replika C-LIF-5: Active, FAMS Expired, Email awal `berakhir.awal+{runId}-079@qwertysystem.net`); `PT Retry Henti Suspend {runId}-079` (replika C-FX12-8: Active, FAMS Active, Email awal `retryhenti.awal+{runId}-079@qwertysystem.net`); `PT Retry Henti Arsip {runId}-079` (replika C-FX13-1: Active, FAMS Active satu-satunya term, Email awal `retryarsip.awal+{runId}-079@qwertysystem.net`). Mail-catcher dengan baseline jumlah email per alamat sebelum aksi (S-12). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Jeda percobaan ulang otomatis: 1 menit, 5 menit, 15 menit.
- Cleanup: hook `after` membatalkan simulasi kegagalan email service, menandai notifikasi uji `[Mark as Read]`, men-seed ulang Client dengan Email awal, dan memulihkan waktu sistem ke waktu nyata.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-959: Notifikasi baru muncul setelah percobaan ulang ketiga

1. Buka dropdown notifikasi pada navbar, catat jumlah notifikasi Unread (N1), lalu tutup dropdown
2. Paksa email service gagal pada setiap percobaan kirim (5xx)
3. Klik sub-tab Active
4. Ketik Search `PT Berakhir Belum Aktivasi {runId}-079`, tekan Enter
5. Buka `⋯` baris `PT Berakhir Belum Aktivasi {runId}-079` lalu klik `Edit`
6. Ubah Email Default User menjadi `retry.edit+{runId}-079@qwertysystem.net`
7. Klik `[Save]`
8. Verifikasi toast sukses "Success, client has been updated."
9. Majukan waktu sistem 1 menit dan tunggu antrean percobaan ulang berjalan
10. Buka dropdown notifikasi, catat jumlah Unread (N2), lalu tutup dropdown
11. Verifikasi N2 sama dengan N1
12. Majukan waktu sistem 5 menit dan tunggu antrean percobaan ulang berjalan
13. Buka dropdown notifikasi, catat jumlah Unread (N3), lalu tutup dropdown
14. Verifikasi N3 sama dengan N1
15. Majukan waktu sistem 15 menit dan tunggu antrean percobaan ulang berjalan
16. Buka dropdown notifikasi, catat jumlah Unread (N4), dan lihat item teratas
17. Verifikasi N4 sama dengan N1 + 1
18. Verifikasi item teratas berstatus Unread dengan Title "Activation email not delivered" dan Body "PT Berakhir Belum Aktivasi {runId}-079: the activation email could not be sent after repeated attempts."
19. Verifikasi tombol aksi item teratas hanya `[Mark as Read]` (tidak ada `[Detail]`)
20. Klik Company Name `PT Berakhir Belum Aktivasi {runId}-079` untuk membuka Detail
21. Verifikasi section Default User menampilkan email "retry.edit+{runId}-079@qwertysystem.net"
22. Verifikasi `[Resend Activation Email]` tersedia
23. Klik `[Mark as Read]` pada notifikasi uji lalu pulihkan waktu sistem ke waktu nyata

### TC-976: Pengulangan dihentikan saat Client di-Suspend

24. Buka dropdown notifikasi pada navbar, catat jumlah notifikasi Unread (N5), lalu tutup dropdown
25. Paksa email service gagal pada setiap percobaan kirim (5xx)
26. Klik breadcrumb "Client" untuk kembali ke List, klik sub-tab Active
27. Ketik Search `PT Retry Henti Suspend {runId}-079`, tekan Enter
28. Buka `⋯` baris `PT Retry Henti Suspend {runId}-079` lalu klik `Edit`
29. Ubah Email Default User menjadi `retryhenti.baru+{runId}-079@qwertysystem.net`
30. Klik `[Save]`
31. Verifikasi toast sukses "Success, client has been updated."
32. Buka `⋯` baris "PT Retry Henti Suspend {runId}-079" lalu klik `Suspend`
33. Klik `[Suspend]` pada dialog "Suspend Client"
34. Verifikasi toast sukses "Success, client has been suspended."
35. Muat ulang Admin Console > Client tanpa memajukan waktu sistem
36. Buka dropdown notifikasi, catat jumlah Unread (N6), lihat item teratas, lalu tutup dropdown
37. Verifikasi N6 sama dengan N5 + 1 (notifikasi dikirim segera saat pengulangan dihentikan)
38. Verifikasi item teratas berstatus Unread dengan Title "Activation email not delivered" dan Body "PT Retry Henti Suspend {runId}-079: the activation email could not be sent after repeated attempts."
39. Verifikasi tombol aksi item teratas hanya `[Mark as Read]` (tidak ada `[Detail]`)
40. Batalkan simulasi kegagalan email service (pengiriman berikutnya berhasil)
41. Catat baseline jumlah email di mail-catcher untuk `retryhenti.baru+{runId}-079@qwertysystem.net` (E0)
42. Majukan waktu sistem 30 menit dan tunggu antrean percobaan ulang berjalan
43. Buka dropdown notifikasi, catat jumlah Unread (N7), lalu tutup dropdown
44. Verifikasi N7 sama dengan N6
45. Verifikasi jumlah Activation Email di inbox `retryhenti.baru+{runId}-079@qwertysystem.net` tetap E0 (tidak ada pengiriman meskipun email service sudah pulih)
46. Klik sub-tab Suspended
47. Ketik Search `PT Retry Henti Suspend {runId}-079`, tekan Enter
48. Klik Company Name `PT Retry Henti Suspend {runId}-079` untuk membuka Detail
49. Verifikasi "PT Retry Henti Suspend {runId}-079" tampil di sub-tab Suspended
50. Verifikasi badge Default User "Not Yet Activated"
51. Verifikasi `[Resend Activation Email]` Hidden
52. Klik `[Mark as Read]` pada notifikasi uji lalu pulihkan waktu sistem ke waktu nyata

### TC-984: Pengulangan dihentikan saat Client menjadi Archived

53. Buka dropdown notifikasi pada navbar, catat jumlah notifikasi Unread (N8), lalu tutup dropdown
54. Paksa email service gagal pada setiap percobaan kirim (5xx)
55. Klik breadcrumb "Client" untuk kembali ke List, klik sub-tab Active
56. Ketik Search `PT Retry Henti Arsip {runId}-079`, tekan Enter
57. Buka `⋯` baris `PT Retry Henti Arsip {runId}-079` lalu klik `Edit`
58. Ubah Email Default User menjadi `retryarsip.baru+{runId}-079@qwertysystem.net`
59. Klik `[Save]`
60. Verifikasi toast sukses "Success, client has been updated."
61. Buka Admin Console > Client Subscription dan Cancel term FAMS yang Active milik "PT Retry Henti Arsip {runId}-079"
62. Kembali ke Admin Console > Client, klik sub-tab Archived
63. Ketik Search `PT Retry Henti Arsip {runId}-079`, tekan Enter
64. Verifikasi "PT Retry Henti Arsip {runId}-079" tampil di sub-tab Archived tanpa aksi manual
65. Verifikasi sel FAMS "PT Retry Henti Arsip {runId}-079" menampilkan `Archive`
66. Muat ulang Admin Console > Client tanpa memajukan waktu sistem
67. Buka dropdown notifikasi, catat jumlah Unread (N9), lihat item teratas, lalu tutup dropdown
68. Verifikasi N9 sama dengan N8 + 1 (Client Archived diperlakukan sama seperti Suspended)
69. Verifikasi item teratas berstatus Unread dengan Title "Activation email not delivered" dan Body "PT Retry Henti Arsip {runId}-079: the activation email could not be sent after repeated attempts."
70. Verifikasi tombol aksi item teratas hanya `[Mark as Read]` (tidak ada `[Detail]`)
71. Batalkan simulasi kegagalan email service (pengiriman berikutnya berhasil)
72. Catat baseline jumlah email di mail-catcher untuk `retryarsip.baru+{runId}-079@qwertysystem.net` (E1)
73. Majukan waktu sistem 30 menit dan tunggu antrean percobaan ulang berjalan
74. Buka dropdown notifikasi, catat jumlah Unread (N10), lalu tutup dropdown
75. Verifikasi N10 sama dengan N9
76. Verifikasi jumlah Activation Email di inbox `retryarsip.baru+{runId}-079@qwertysystem.net` tetap E1
77. Klik `[Mark as Read]` pada notifikasi uji lalu pulihkan waktu sistem ke waktu nyata

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 80 langkah): satu role, satu kelas (majukan waktu sistem, antrean percobaan ulang, dan kegagalan email service); tiap blok memakai Client seed milik sendiri dan berdiri sendiri. Waktu sistem dipulihkan ke waktu nyata di akhir tiap blok sebelum blok berikutnya (S-09).
- Langkah penghubung (S-03): pencatatan N dan E, Search nama unik, sub-tab, penutupan notifikasi, pemulihan waktu dan `[Mark as Read]`.
- Temuan untuk QA:
  - TC-959, TC-976, dan TC-984 bertanda Manual Only (memajukan waktu sistem); spec memakai kemampuan majukan jam server yang disediakan tim FE/BE.
  - TC-959, TC-976, dan TC-984 menulis "Majukan waktu sistem 1 menit ... 5 menit ... 15 menit" secara relatif; batas eksak jadwal retry (bagian 6 konvensi menyarankan waktu absolut) tidak dinyatakan TC.
