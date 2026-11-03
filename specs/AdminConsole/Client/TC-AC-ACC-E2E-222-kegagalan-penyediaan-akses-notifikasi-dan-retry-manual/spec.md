---
id: TC-AC-ACC-E2E-222-kegagalan-penyediaan-akses-notifikasi-dan-retry-manual
title: "Kegagalan Penyediaan Akses Produk: Notifikasi setelah Percobaan Ketiga dan Retry Manual Berhasil atau Gagal Lagi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-244
  - TC-AC-ACC-992
  - TC-AC-ACC-1004
coverage:
  web: automated
---

# Kegagalan Penyediaan Akses Produk: Notifikasi setelah Percobaan Ketiga dan Retry Manual Berhasil atau Gagal Lagi

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dikonsumsi pada TC, ditiru bersuffix; di-seed hook `before` lewat Fixture BE yang disediakan tim FE/BE): (a) "PT Baru Daftar B {runId}-222" dengan atribut C-09 (Tabel A2): Active, Direct (tanpa relasi manager), Group Cabang Menteng, belum pernah memiliki subscription, Default User Not Yet Activated (TC-244); (b) "PT Retry Akses Manual {runId}-222" (atribut C-FX14-3: Active, Direct, Group Area Jakarta, belum pernah memiliki subscription, Default User Not Yet Activated) (TC-992); (c) "PT Retry Gagal Lagi {runId}-222" (atribut C-FX15-7: Active, Direct, Group Area Jakarta, belum pernah memiliki subscription, Default User Not Yet Activated) (TC-1004). Hook `after` menghapus ketiga Client lewat API.
- Kemampuan teknis (kelas d, harness eksternal): simulasi penyediaan instance produk FAMS (tertunda atau gagal pada setiap percobaan) untuk tenant uji; job scheduler antrean percobaan ulang; disediakan tim FE/BE tanpa endpoint karangan (S-13). Hook `after` membatalkan simulasi penyediaan dan memulihkan jam server.
- Manipulasi jam: jam server dimajukan absolut (1 menit, 5 menit, 15 menit) agar antrean percobaan ulang penyediaan akses berjalan; hanya jam server karena antrean dihitung di server dan tidak diamati lewat countdown UI; hook `after` memulihkan jam server ke waktu nyata (S-09, bagian 6).
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- Kemampuan baca jumlah notifikasi berstatus Unread pada dropdown notifikasi navbar dicatat sebagai baseline sebelum aksi (S-12). Notifikasi diamati pada akun aktor Total Control yang sama dengan penekan `[Retry]`; item notifikasi uji ditandai `[Mark as Read]` di hook `after`.
- Kemampuan teknis tambahan: halaman Settings > User > Detail akun aktor > Tab System Log dan Admin Console > Activity Log (kemampuan baca log) untuk TC-992 dan TC-1004; pencarian di modal Changelog List. Suite berjalan serial (`parallel: false`).
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).

## Test Steps

### TC-AC-ACC-244: Penyediaan akses gagal: notifikasi view-only "Product access setup failed" setelah percobaan ulang ketiga

1. Buka dropdown notifikasi pada navbar, catat jumlah notifikasi berstatus Unread (N1), lalu tutup dropdown
2. Paksa penyediaan instance produk FAMS gagal pada setiap percobaan
3. Aktifkan term pertama FAMS "PT Baru Daftar B {runId}-222" (mode New, terotorisasi langsung, Start Date hari ini) dari Admin Console > Client Subscription
4. Tunggu aksi selesai, lalu buka Admin Console > Client, klik sub-tab `Active`, ketik Search `PT Baru Daftar B {runId}-222`, tekan Enter, klik Company Name "PT Baru Daftar B {runId}-222", dan buka Tab `Subscription` sub-tab `FAMS`
5. Verifikasi sub-tab `FAMS` menampilkan badge term `Active`
6. Verifikasi sub-tab `FAMS` menampilkan indikator "Preparing access"
7. Majukan waktu sistem 1 menit, tunggu antrean percobaan ulang berjalan, buka dropdown notifikasi dan catat jumlah Unread (N2), lalu tutup dropdown
8. Verifikasi N2 = N1 (belum ada notifikasi baru)
9. Majukan waktu sistem 5 menit, tunggu antrean percobaan ulang berjalan, buka dropdown notifikasi dan catat jumlah Unread (N3), lalu tutup dropdown
10. Verifikasi N3 = N1 (belum ada notifikasi baru)
11. Majukan waktu sistem 15 menit, muat ulang halaman tiap 5 detik sampai notifikasi baru muncul di dropdown notifikasi (batas tunggu 2 menit), lalu buka dropdown notifikasi, catat jumlah Unread (N4), dan lihat item teratas
12. Verifikasi N4 = N1 + 1
13. Verifikasi item teratas berstatus Unread dengan Title "Product access setup failed" dan Body "PT Baru Daftar B {runId}-222: FAMS access could not be prepared after repeated attempts."
14. Verifikasi tombol aksi item teratas hanya `[Mark as Read]` (tidak ada `[Detail]` atau tombol navigasi lain)
15. Klik `[Mark as Read]` pada notifikasi uji, lalu tutup dropdown
16. Muat ulang Tab `Subscription` sub-tab `FAMS` "PT Baru Daftar B {runId}-222"
17. Verifikasi sub-tab `FAMS` tetap menampilkan badge term `Active`
18. Verifikasi indikator berganti "Access setup failed" dengan tombol `[Retry]` (penyediaan berstatus gagal final)
19. Batalkan simulasi kegagalan penyediaan instance FAMS dan pulihkan waktu sistem ke waktu nyata

### TC-AC-ACC-992: Retry manual penyediaan akses produk oleh Total Control

20. Paksa penyediaan instance produk FAMS gagal pada setiap percobaan
21. Aktifkan term pertama FAMS "PT Retry Akses Manual {runId}-222" (mode New, terotorisasi langsung, Start Date hari ini) dari Admin Console > Client Subscription
22. Majukan waktu sistem 1 menit, 5 menit, lalu 15 menit secara berurutan
23. Buka Admin Console > Client, klik sub-tab `Active`, ketik Search `PT Retry Akses Manual {runId}-222`, tekan Enter, klik Company Name "PT Retry Akses Manual {runId}-222", buka Tab `Subscription` sub-tab `FAMS`, lalu muat ulang tiap 5 detik sampai indikator "Access setup failed" tampil (batas tunggu 2 menit)
24. Verifikasi sub-tab `FAMS` menampilkan badge term `Active`
25. Verifikasi sub-tab `FAMS` menampilkan indikator "Access setup failed" dengan tombol `[Retry]`
26. Verifikasi indikator "Preparing access" tidak tampil
27. Batalkan simulasi kegagalan penyediaan instance FAMS
28. Klik `[Retry]` pada indikator "Access setup failed"
29. Verifikasi toast sukses "Success, access setup retry has been started."
30. Verifikasi indikator kembali menjadi "Preparing access"
31. Verifikasi tombol `[Retry]` tidak tampil (rangkaian pengulangan baru dimulai)
32. Muat ulang Tab `Subscription` sub-tab `FAMS` tiap 5 detik sampai indikator "Preparing access" tidak tampil (batas tunggu 2 menit)
33. Verifikasi indikator "Preparing access" dan "Access setup failed" tidak tampil
34. Verifikasi badge term tetap `Active`
35. Kembali ke List, klik `[Changelog]` di toolbar, ketik Search modal `PT Retry Akses Manual {runId}-222`, tekan Enter
36. Verifikasi Modal Changelog memuat tepat satu baris Action `Retry Access Setup`, Client Name "PT Retry Akses Manual {runId}-222", Field `Product`, Old Value `—`, New Value `FAMS`, dan Modified By user Total Control yang menekan `[Retry]` (bukan `System`)
37. Tutup modal Changelog, lalu buka Settings > User > Detail akun aktor > Tab System Log, klik ikon Search, ketik `PT Retry Akses Manual {runId}-222`, tekan Enter
38. Verifikasi System Log akun aktor memuat tepat satu baris Action `Retry Access Setup`, Object `Client`, Name "PT Retry Akses Manual {runId}-222", Field `Product`, Old Value `—`, New Value `FAMS`
39. Pulihkan waktu sistem ke waktu nyata

### TC-AC-ACC-1004: Retry manual penyediaan akses produk yang gagal lagi

40. Buka dropdown notifikasi, catat jumlah notifikasi berstatus Unread (N1), lalu tutup dropdown
41. Paksa penyediaan instance produk FAMS gagal pada setiap percobaan
42. Aktifkan term pertama FAMS "PT Retry Gagal Lagi {runId}-222" (mode New, terotorisasi langsung, Start Date hari ini) dari Admin Console > Client Subscription
43. Majukan waktu sistem 1 menit, 5 menit, lalu 15 menit secara berurutan
44. Buka Admin Console > Client, klik sub-tab `Active`, ketik Search `PT Retry Gagal Lagi {runId}-222`, tekan Enter, klik Company Name "PT Retry Gagal Lagi {runId}-222", buka Tab `Subscription` sub-tab `FAMS`, lalu muat ulang tiap 5 detik sampai indikator "Access setup failed" tampil (batas tunggu 2 menit)
45. Verifikasi sub-tab `FAMS` menampilkan badge term `Active`
46. Verifikasi sub-tab `FAMS` menampilkan indikator "Access setup failed" dengan tombol `[Retry]`
47. Klik `[Retry]` pada indikator "Access setup failed" lalu lihat toast dan indikator
48. Verifikasi toast sukses "Success, access setup retry has been started."
49. Verifikasi indikator kembali menjadi "Preparing access" tanpa tombol `[Retry]`
50. Majukan waktu sistem 1 menit, 5 menit, lalu 15 menit secara berurutan
51. Muat ulang halaman tiap 5 detik sampai notifikasi kedua dari rangkaian Retry muncul di dropdown notifikasi (batas tunggu 2 menit), lalu buka dropdown notifikasi, catat jumlah Unread (N2), dan lihat item teratas
52. Verifikasi N2 = N1 + 2 (satu notifikasi dari rangkaian awal dan satu dari rangkaian Retry)
53. Verifikasi item teratas berstatus Unread dengan Title "Product access setup failed" dan Body "PT Retry Gagal Lagi {runId}-222: FAMS access could not be prepared after repeated attempts."
54. Verifikasi tombol aksi item teratas hanya `[Mark as Read]`
55. Muat ulang Tab `Subscription` sub-tab `FAMS`
56. Verifikasi indikator berganti "Access setup failed" dengan tombol `[Retry]`
57. Verifikasi badge term tetap `Active`
58. Kembali ke List, klik `[Changelog]` di toolbar, ketik Search modal `PT Retry Gagal Lagi {runId}-222`, tekan Enter
59. Verifikasi Modal Changelog memuat tepat satu baris Action `Retry Access Setup`, Client Name "PT Retry Gagal Lagi {runId}-222", Field `Product`, Old Value `—`, New Value `FAMS`, dan Modified By user Total Control yang menekan `[Retry]` (bukan `System`)
60. Tutup modal Changelog, lalu buka Admin Console > Activity Log dan cari baris Action `Retry Access Setup`
61. Verifikasi Activity Log memuat baris Action `Retry Access Setup` dengan Object `Client`, Name "PT Retry Gagal Lagi {runId}-222", Field `Product`, Old Value `—`, New Value `FAMS`, dan Modified By user Total Control yang menekan `[Retry]`
62. Buka Settings > User > Detail akun aktor > Tab System Log, klik ikon Search, ketik `PT Retry Gagal Lagi {runId}-222`, tekan Enter
63. Verifikasi System Log akun aktor memuat tepat satu baris Action `Retry Access Setup`, Object `Client`, Name "PT Retry Gagal Lagi {runId}-222", Field `Product`, Old Value `—`, New Value `FAMS`
64. Klik `[Mark as Read]` pada notifikasi uji, lalu pulihkan waktu sistem ke waktu nyata

## Notes

- Spec ini melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas harness (kegagalan penyediaan akses dengan pemajuan jam server), tiap blok memakai Client sendiri dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): polling "muat ulang tiap 5 detik, batas tunggu 2 menit" (idiom bagian 6) pada langkah 11, 23, 32, 44, dan 51. Langkah 7 dan 9 (N2 = N1, N3 = N1 setelah pemajuan 1 dan 5 menit) tidak memiliki anchor teramati bahwa antrean sudah berjalan sehingga masih menunggu keputusan QA.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Baris "tepat satu baris" pada Changelog dan System Log memakai nama Client bersuffix unik sehingga baseline nol (S-12). Jam server dipulihkan di antara blok dan di hook `after` sebelum akun aktor membuka Activity Log atau System Log (S-09). N1 dan N2 pada TC-244 dan TC-1004 dicatat sebagai baseline hitungan notifikasi (S-12).
- Temuan untuk QA (S-15): TC-244 Langkah 6 dan 7 menyebut Modified By "user Total Control yang menekan [Retry]" tanpa nama user; spec memakai akun aktor Total Control. TC-244, TC-992, dan TC-1004 bergantung simulasi kegagalan penyediaan dan pemajuan jam (alasan Manual Only (b)) yang disediakan tim FE/BE. Jeda percobaan ulang 1, 5, 15 menit berasal dari data uji TC (PRD menyebut "satu menit/lima menit/lima belas menit"). Post Condition seluruh TC dipenuhi hook `after`.
