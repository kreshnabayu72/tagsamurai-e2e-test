---
id: TC-AC-ACC-E2E-314-activation-email-dan-penyediaan-akses-gagal
title: "Kegagalan Activation Email Otomatis dan Penyediaan Akses Produk: Toast Error, Notifikasi Setelah Percobaan Ketiga, dan Pengulangan Dihentikan Saat Suspend"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-464
  - TC-AC-ACC-963
  - TC-AC-ACC-983
coverage:
  web: automated
---

# Kegagalan Activation Email Otomatis dan Penyediaan Akses Produk: Toast Error, Notifikasi Setelah Percobaan Ketiga, dan Pengulangan Dihentikan Saat Suspend

## Prerequisites

- Mode: FE+BE (kegagalan email service dan penyediaan instance produk dipicu di sisi server).
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- State global: jam server (job scheduler lifecycle berjalan di server) diatur absolut lewat kemampuan manipulasi jam (disediakan tim FE/BE) dan jam browser/klien diatur bersama; keduanya dipulihkan ke waktu nyata setelah tiap blok TC dan di hook `after` (R-10, S-09). Tidak ada langkah "Tunggu N menit"; menunggu job memakai polling worker (muat ulang halaman tiap 5 detik sampai perubahan terlihat, batas 2 menit). Suite berjalan serial.
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-464: C-09 `PT Baru Daftar` -> `PT Baru Daftar Email {runId}-314` (Active; belum pernah memiliki subscription; Default User Not Yet Activated).
  - TC-AC-ACC-963: C-W3LIF-6 -> `PT Retry Email Satu {runId}-314` (Active; belum pernah memiliki subscription; Default User Not Yet Activated).
  - TC-AC-ACC-983: C-FX12-9 -> `PT Penyediaan Henti Suspend {runId}-314` (Active; belum pernah memiliki subscription; Default User Not Yet Activated; Group Area Jakarta; Direct).
- Kemampuan teknis: memaksa email service gagal pada setiap percobaan kirim (mock 5xx di sisi server) dan memaksa penyediaan instance produk FAMS gagal pada setiap percobaan, serta membatalkannya (disediakan tim FE/BE; tidak ada endpoint yang dikarang); memajukan jam server 1 menit, 5 menit, 15 menit, dan 30 menit (jeda percobaan ulang `ACC-LOGIC-10.1`/`10.2` ditulis PRD dengan kata); membaca jumlah notifikasi Unread di dropdown notifikasi navbar. Data Add Subscription TC-AC-ACC-983: Plan Professional, Duration 1 year(s), Start Date hari ini; TC-AC-ACC-464 dan TC-AC-ACC-963 aktivasi term pertama FAMS: Plan, Duration, dan Start Date disediakan tim FE.
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)

## Test Steps

### Activation Email otomatis gagal (TC-AC-ACC-464)

1. Buka dropdown notifikasi pada navbar, catat jumlah notifikasi Unread (N1), lalu tutup dropdown
2. Paksa email service gagal (mock 5xx di sisi server)
3. Aktifkan term pertama FAMS `PT Baru Daftar Email {runId}-314` dari Client Subscription
4. Verifikasi toast error `Error, failed to send activation email.` ke aktor pemicu
5. Buka dropdown notifikasi pada navbar, catat jumlah Unread (N2), lalu tutup dropdown
6. Verifikasi N2 = N1 (belum ada notifikasi baru setelah percobaan pertama gagal)
7. Buka Admin Console > Client, klik sub-tab Active, ketik Search `PT Baru Daftar Email {runId}-314`, tekan Enter
8. Verifikasi sel FAMS `Active` (Client dan term tetap Active)
9. Klik Company Name `PT Baru Daftar Email {runId}-314` dan lihat section Default User
10. Verifikasi `[Resend Activation Email]` tersedia pada section Default User
11. Batalkan simulasi kegagalan email service

### Activation Email gagal berulang sampai notifikasi (TC-AC-ACC-963)

12. Buka dropdown notifikasi pada navbar, catat jumlah Unread (N1), lalu tutup dropdown
13. Paksa email service gagal pada setiap percobaan kirim (mock 5xx)
14. Aktifkan term pertama FAMS `PT Retry Email Satu {runId}-314` dari Admin Console > Client Subscription
15. Majukan jam server dan jam browser 1 menit, tunggu antrean percobaan ulang berjalan lewat polling, buka dropdown notifikasi, catat jumlah Unread (N2), lalu tutup dropdown
16. Verifikasi N2 = N1
17. Majukan jam server dan jam browser 5 menit, tunggu antrean percobaan ulang berjalan lewat polling, buka dropdown notifikasi, catat jumlah Unread (N3), lalu tutup dropdown
18. Verifikasi N3 = N1 (belum ada notifikasi baru)
19. Majukan jam server dan jam browser 15 menit, tunggu antrean percobaan ulang berjalan lewat polling, buka dropdown notifikasi, catat jumlah Unread (N4), dan lihat item teratas
20. Verifikasi N4 = N1 + 1
21. Verifikasi item teratas berstatus Unread dengan Title `Activation email not delivered` dan Body `PT Retry Email Satu {runId}-314: the activation email could not be sent after repeated attempts.`
22. Verifikasi tombol aksi item teratas hanya `[Mark as Read]` (tidak ada `[Detail]`)
23. Pulihkan jam server dan jam browser, buka Admin Console > Client, klik sub-tab Active, ketik Search `PT Retry Email Satu {runId}-314`, tekan Enter
24. Verifikasi sel FAMS `Active` (Client dan term tetap Active)
25. Klik Company Name `PT Retry Email Satu {runId}-314` dan lihat section Default User
26. Verifikasi `[Resend Activation Email]` tersedia pada section Default User
27. Klik `[Mark as Read]` pada notifikasi uji dan batalkan simulasi kegagalan email service

### Pengulangan penyediaan akses dihentikan saat Suspend (TC-AC-ACC-983)

28. Buka dropdown notifikasi pada navbar, catat jumlah Unread (N1), lalu tutup dropdown
29. Paksa penyediaan instance produk FAMS gagal pada setiap percobaan
30. Aktifkan term pertama FAMS `PT Penyediaan Henti Suspend {runId}-314` (mode New, terotorisasi langsung, Start Date hari ini) dari Admin Console > Client Subscription
31. Tunggu aksi selesai (Aktivasi term pertama FAMS)
32. Buka Admin Console > Client, klik sub-tab Active, ketik Search `PT Penyediaan Henti Suspend {runId}-314`, tekan Enter, klik Company Name `PT Penyediaan Henti Suspend {runId}-314`, dan buka Tab Subscription sub-tab FAMS
33. Verifikasi sub-tab FAMS menampilkan badge term `Active`
34. Verifikasi indikator `Preparing access`
35. Klik breadcrumb `Client` untuk kembali ke List, ketik Search `PT Penyediaan Henti Suspend {runId}-314`, tekan Enter, buka `⋯` baris `PT Penyediaan Henti Suspend {runId}-314` → Suspend, lalu klik `[Suspend]` pada dialog `Suspend Client`
36. Verifikasi toast `Success, client has been suspended.`
37. Muat ulang Admin Console > Client tanpa memajukan jam server, buka dropdown notifikasi, catat jumlah Unread (N2), lihat item teratas, lalu tutup dropdown
38. Verifikasi N2 = N1 + 1 (notifikasi dikirim segera saat pengulangan dihentikan oleh Suspend)
39. Verifikasi item teratas berstatus Unread dengan Title `Product access setup failed` dan Body `PT Penyediaan Henti Suspend {runId}-314: FAMS access could not be prepared after repeated attempts.`
40. Verifikasi tombol aksi item teratas hanya `[Mark as Read]` (tidak ada `[Detail]` atau tombol navigasi lain)
41. Batalkan simulasi kegagalan penyediaan instance FAMS (penyediaan berikutnya berhasil)
42. Majukan jam server dan jam browser 30 menit, tunggu antrean percobaan ulang berjalan lewat polling, lalu pulihkan jam; buka dropdown notifikasi, catat jumlah Unread (N3), lalu tutup dropdown
43. Verifikasi N3 = N2 (tidak ada notifikasi tambahan)
44. Klik sub-tab Suspended, ketik Search `PT Penyediaan Henti Suspend {runId}-314`, tekan Enter, klik Company Name `PT Penyediaan Henti Suspend {runId}-314`, dan buka Tab Subscription sub-tab FAMS
45. Verifikasi sub-tab FAMS tetap menampilkan badge term `Active`
46. Verifikasi indikator `Access setup failed`
47. Verifikasi tombol `[Retry]` tidak ada (Hidden karena Client Suspended)
48. Klik `[Mark as Read]` pada notifikasi uji

## Notes

- Kelas b+d: kegagalan yang dipaksa di server (email service, penyediaan instance) bersama jam server; ketiga TC memakai harness yang sama (kegagalan terkelola di server + jam server) sehingga digabung. Jam dipulihkan sebelum langkah yang membuka Detail atau halaman lain (S-09). Absence `Verifikasi` memakai N1 sebagai baseline hitungan notifikasi Unread (S-12).
- Teks Title dan Body notifikasi mengandung nama Client bersuffix; nama pada Expected TC (`PT Retry Email Satu`, `PT Penyediaan Henti Suspend`) ditambah suffix `{runId}-314` mengikuti S-12.
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (kegagalan email/penyediaan + jam) dan data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Langkah 31 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-464: Langkah 2 `Paksa email service gagal (mock 5xx)` tidak menyebut mekanisme; Expected hanya menyebut toast ke aktor pemicu.
  - TC-AC-ACC-963 dan TC-AC-ACC-983: jeda percobaan ulang (1, 5, 15 menit) berasal dari ACC-LOGIC-10 yang ditulis PRD dengan kata; Data Uji TC memuat angka.
  - TC-AC-ACC-983: Expected butir (e) menyebut `[Retry]` Hidden karena ACC-LOGIC-04.7; `Verifikasi` ini memakai Detail sub-tab FAMS sebagai anchor positif (badge Active tampil).
