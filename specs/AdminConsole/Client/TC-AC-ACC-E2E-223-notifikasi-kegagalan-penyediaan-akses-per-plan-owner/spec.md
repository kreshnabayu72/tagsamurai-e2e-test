---
id: TC-AC-ACC-E2E-223-notifikasi-kegagalan-penyediaan-akses-per-plan-owner
title: "Notifikasi Kegagalan Penyediaan Akses per Plan Owner: Distributor Pemilik Plan Menerima, Read Only dan Distributor Luar Jaringan Tidak"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-1006
  - TC-AC-ACC-1032
coverage:
  web: automated
---

# Notifikasi Kegagalan Penyediaan Akses per Plan Owner: Distributor Pemilik Plan Menerima, Read Only dan Distributor Luar Jaringan Tidak

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| Distributor Total Control (PT Distribusi Nusantara), A-13 | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` |
| Read Only (Principal), A-02 | `readOnlyPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_RO_PASSWORD` |

- Env var `AC_CLIENT_DIST_TC_PASSWORD`, `AC_CLIENT_RO_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`. `AC_TC_PASSWORD` sudah terdaftar.
- Sesi Distributor A-13 dan Read Only A-02 adalah konteks browser terpisah dari sesi Total Control (Principal) hook `before`; keduanya login lewat langkah 1 dan 2 di `## Test Steps` dan tetap terbuka selama spec (bukan ganti akun pada satu sesi); hook `after` menutup kedua konteks browser itu.
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dikonsumsi pada TC, ditiru bersuffix; di-seed hook `before` lewat Fixture BE yang disediakan tim FE/BE): (a) "PT Notif Total Control Distributor {runId}-223" (atribut C-FX15-5: Active, relasi Distributor-langsung PT Distribusi Nusantara tanpa Partner, Group Area Jakarta, belum pernah memiliki subscription, Default User Not Yet Activated); (b) "PT Notif Plan Owner Principal {runId}-223" (atribut C-FX15-9: sama dengan (a)). Hook `after` menghapus kedua Client lewat API.
- Kemampuan teknis (kelas d, harness eksternal): simulasi penyediaan instance produk FAMS (tertunda atau gagal pada setiap percobaan) untuk tenant uji; job scheduler antrean percobaan ulang; disediakan tim FE/BE tanpa endpoint karangan (S-13). Hook `after` membatalkan simulasi penyediaan dan memulihkan jam server.
- Manipulasi jam: jam server dimajukan absolut (1 menit, 5 menit, 15 menit) agar antrean percobaan ulang penyediaan akses berjalan; hanya jam server karena antrean dihitung di server dan tidak diamati lewat countdown UI; hook `after` memulihkan jam server ke waktu nyata (S-09, bagian 6).
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- Kemampuan baca jumlah notifikasi berstatus Unread pada dropdown notifikasi navbar dicatat sebagai baseline sebelum aksi (S-12).
- Kelas campuran c dan d: tiap TC memakai beberapa sesi UI sekaligus (Total Control, Distributor Total Control, dan Read Only) dan pemajuan jam server dalam satu alur yang tidak dapat dipisah; sesi kedua dan ketiga menjadi objek asersi (notifikasi dan Detail) sehingga bukan pemicu `P-2`. Suite berjalan serial (`parallel: false`). Perangkat dan browser terpisah per sesi disediakan tim FE.

## Test Steps

### TC-AC-ACC-1006: Notifikasi diterima Total Control Distributor pemilik plan; tidak diterima Read Only; [Retry] tampil untuk Distributor pemilik plan

1. [Sesi Distributor A-13] Login sebagai Distributor Total Control (PT Distribusi Nusantara) (A-13) pada konteks browser terpisah dan biarkan sesi terbuka
2. [Sesi Read Only A-02] Login sebagai Read Only (Principal) (A-02) pada konteks browser terpisah dan biarkan sesi terbuka
3. [Sesi Distributor A-13] Buka dropdown notifikasi, catat jumlah Unread (N1D), lalu tutup dropdown
4. [Sesi Read Only A-02] Buka dropdown notifikasi, catat jumlah Unread (N1R), lalu tutup dropdown
5. [Sesi Total Control (Principal)] Paksa penyediaan instance produk FAMS gagal pada setiap percobaan
6. [Sesi Distributor A-13] Aktifkan term pertama FAMS "PT Notif Total Control Distributor {runId}-223" (mode New, terotorisasi langsung, Start Date hari ini) dari Admin Console > Client Subscription sehingga plan owner term = PT Distribusi Nusantara
7. [Sesi Total Control (Principal)] Majukan waktu sistem 1 menit, 5 menit, lalu 15 menit secara berurutan
8. [Sesi Distributor A-13] Muat ulang halaman tiap 5 detik sampai notifikasi baru muncul di dropdown notifikasi (batas tunggu 2 menit), lalu buka dropdown notifikasi, catat jumlah Unread (N2D), dan lihat item teratas
9. Verifikasi N2D = N1D + 1
10. Verifikasi item teratas berstatus Unread dengan Title "Product access setup failed" dan Body "PT Notif Total Control Distributor {runId}-223: FAMS access could not be prepared after repeated attempts."
11. Verifikasi tombol aksi item teratas hanya `[Mark as Read]`
12. [Sesi Distributor A-13] Buka Admin Console > Client, ketik Search `PT Notif Total Control Distributor {runId}-223`, tekan Enter, klik Company Name, dan buka Tab `Subscription` sub-tab `FAMS`
13. Verifikasi sub-tab `FAMS` menampilkan indikator "Access setup failed" dengan tombol `[Retry]`
14. [Sesi Read Only A-02] Buka dropdown notifikasi dan catat jumlah Unread (N2R)
15. Verifikasi N2R = N1R (Read Only tidak menerima notifikasi)
16. [Sesi Distributor A-13] Klik `[Mark as Read]` pada notifikasi uji; [Sesi Total Control (Principal)] pulihkan waktu sistem ke waktu nyata

### TC-AC-ACC-1032: Total Control Distributor tidak menerima notifikasi dan tidak melihat [Retry] untuk term dengan plan owner Principal

17. [Sesi Distributor A-13] Buka dropdown notifikasi, catat jumlah Unread (N1D), lalu tutup dropdown
18. [Sesi Total Control (Principal)] Paksa penyediaan instance produk FAMS gagal pada setiap percobaan
19. [Sesi Total Control (Principal)] Aktifkan term pertama FAMS "PT Notif Plan Owner Principal {runId}-223" (mode New, terotorisasi langsung, Start Date hari ini) dari Admin Console > Client Subscription sehingga plan owner term = Principal
20. [Sesi Total Control (Principal)] Majukan waktu sistem 1 menit, 5 menit, lalu 15 menit secara berurutan
21. [Sesi Total Control (Principal)] Buka Admin Console > Client, ketik Search `PT Notif Plan Owner Principal {runId}-223`, tekan Enter, klik Company Name, buka Tab `Subscription` sub-tab `FAMS`, lalu muat ulang tiap 5 detik sampai indikator "Access setup failed" tampil (batas tunggu 2 menit)
22. Verifikasi sub-tab `FAMS` menampilkan indikator "Access setup failed" dengan tombol `[Retry]`
23. [Sesi Distributor A-13] Buka dropdown notifikasi dan catat jumlah Unread (N2D)
24. Verifikasi N2D = N1D (Total Control Distributor di luar jaringan plan owner term tidak menerima notifikasi)
25. [Sesi Distributor A-13] Buka Admin Console > Client, ketik Search `PT Notif Plan Owner Principal {runId}-223`, tekan Enter, klik Company Name, dan buka Tab `Subscription`
26. Verifikasi Tab `Subscription` menampilkan teks "You don't have access to this client's subscriptions."
27. Verifikasi sub-tab `FAMS`, indikator penyediaan akses, dan tombol `[Retry]` tidak ada
28. [Sesi Total Control (Principal)] Batalkan simulasi kegagalan penyediaan instance FAMS dan pulihkan waktu sistem ke waktu nyata

## Notes

- Pembagian TC lintas spec: penyediaan akses gagal dengan satu sesi (TC-244, TC-992, TC-1004) ada di spec 222; Retry manual dari tampilan basi (TC-1035) ada di spec 224. Id TC masing-masing tetap satu spec.
- Langkah penghubung (S-03, R-16): langkah 1 dan 2 (login sesi Distributor A-13 dan Read Only A-02); polling "muat ulang tiap 5 detik, batas tunggu 2 menit" (idiom bagian 6) pada langkah 8 dan 21; anchor bahwa antrean sudah berjalan sebelum asersi absence langkah 15 dan 24 adalah Verifikasi langkah 9 dan 22.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Anchor absence TC-1032: Verifikasi N1D/N2D (hitungan Unread) dan teks akses pada Tab `Subscription` mendahului asersi sub-tab dan `[Retry]` tidak ada (bagian 8b butir 2). Baris "sesi" ditulis dengan label [Sesi ...] pada tiap langkah karena aktor berganti di dalam satu langkah alur; sesi tetap terbuka bersamaan (bukan Step ganti akun).
- Temuan untuk QA (S-15): TC-1006 dan TC-1032 menyebut akun A-13 dan A-02 yang ada di Tabel A1; sesi kedua dan ketiga adalah sesi UI karena notifikasi dan Detail diamati di sesi itu. Post Condition seluruh TC dipenuhi hook `after` karena Client milik spec dihapus.
