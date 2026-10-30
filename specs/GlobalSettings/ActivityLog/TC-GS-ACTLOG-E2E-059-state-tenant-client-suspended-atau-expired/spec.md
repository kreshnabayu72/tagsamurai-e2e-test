---
id: TC-GS-ACTLOG-E2E-059-state-tenant-client-suspended-atau-expired
title: "State Tenant: Client Suspended atau Expired"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-222
  - TC-GS-ACTLOG-223
coverage:
  web: automated
---

# State Tenant: Client Suspended atau Expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control dari Client uji khusus spec ini (`Fixture.activityLog.clientUji059`, awalnya berstatus Active; fixture baru, email dan kredensial disediakan tim FE). Fixture `GS_CLIENTSUSP_TC_PASSWORD` tidak dipakai karena suite lain menganggapnya selalu Suspended. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control `Fixture.activityLog.clientUji059` dan halaman Activity Log (kemampuan disediakan tim FE/BE).
- Data Pre-setup: Client uji `Fixture.activityLog.clientUji059` berstatus Active dan akun Total Control-nya (data environment tetap, disediakan tim FE). Status Client diubah ke Suspended oleh spec ini dan dipulihkan ke Active di hook `after`.
- Data Dinamis (bersuffix per run, dibersihkan di hook `after` tanpa berasumsi seeding berhasil penuh): Brand `Brand Seed {runId}-059` dan berkas `Berkas Sistem {runId}-059.png` (di Recycle Bin, melewati batas auto-purge) di-seed lewat API di hook `before` pada Client uji selagi berstatus Active, sehingga Tab Session dan Tab User Action memiliki baris sebelum Client di-suspend. Seed dua aksi sumber dengan Action berbeda agar Tab User Action memuat sedikitnya dua nilai Action distinct: Create Brand `Brand Seed {runId}-059` (Action `Create`) lalu Edit Brand yang sama dengan mengganti Brand Name (satu-satunya field Brand) menjadi `Brand Seed {runId}-059 Ubah` (Action `Edit`). Seed berkas juga menghasilkan entri log bernama `Berkas Sistem {runId}-059.png` oleh aktor seed (Modified By bukan `System`); entri log tidak dapat dihapus, nama bersuffix run mencegah bentrok dengan run lain. Brand dihapus di hook `after` dengan nama terakhir (`Brand Seed {runId}-059 Ubah`); berkas dihapus permanen di hook `after` bila masih ada di Recycle Bin.
- Urutan hook `before`: (1) seed Brand dan berkas selagi Client Active, (2) setel flag Guided Tooltip `seen` untuk akun aktor, (3) login akun aktor, (4) Total Control Principal men-suspend Client uji lewat API. Hook `after` memulihkan status Client ke Active, lalu memulihkan flag Guided Tooltip, lalu menghapus data seed.
- Kemampuan teknis (disediakan tim FE/BE, tanpa mengarang endpoint): (1) Total Control Principal (`Spectra.env.GS_PRINCIPAL_TC_PASSWORD`) mengubah status Client uji menjadi Suspended lewat API di hook `before` dan memulihkannya ke Active di hook `after`; (2) memicu proses sistem di modul Global Settings lain pada Client yang sedang Suspended (auto-purge berkas `Berkas Sistem {runId}-059.png`, seed BE); (3) mengamati unduhan berkas dari icon Download; (4) sesi API akun Total Control Client uji (dan Principal) sebagai pelaku seed dan cleanup, tanpa mengarang endpoint.
- State global yang diubah: status tenant Client uji (Active menjadi Suspended; pemulihan ke Active di hook `after`). Suite serial (`parallel: false`) mengikuti `suite.md`.

## Test Steps

### TC-GS-ACTLOG-222: Log tetap dapat dilihat saat Client suspended

1. Buka Global Settings > Activity Log > Session
2. Verifikasi tabel Tab Session tampil
3. Verifikasi toolbar Tab Session tampil
4. Ketik Search `Login`, tekan Enter
5. Verifikasi tabel Tab Session menampilkan baris yang cocok dengan `Login`
6. Klik `(←)` pada kotak Search Tab Session
7. Klik icon Filter, pilih Activity `Login`, klik [Apply]
8. Verifikasi tabel Tab Session hanya menampilkan baris dengan Activity `Login`
9. Klik icon Filter, klik [Clear Field] pada field Activity, klik [Apply]
10. Klik icon Download, lalu klik `Download as CSV` pada Tab Session
11. Verifikasi berkas unduhan Tab Session terunduh
12. Klik tab "User Action"
13. Verifikasi tabel Tab User Action tampil
14. Verifikasi toolbar Tab User Action tampil
15. Ketik Search `Brand Seed {runId}-059`, tekan Enter
16. Verifikasi tabel Tab User Action menampilkan baris yang cocok dengan `Brand Seed {runId}-059`
17. Klik `(←)` pada kotak Search Tab User Action
18. Klik icon Filter, pilih Action `Create`, klik [Apply]
19. Verifikasi tabel Tab User Action hanya menampilkan baris dengan Action `Create`
20. Klik icon Filter, klik [Clear Field] pada field Action, klik [Apply]
21. Klik icon Download, lalu klik `Download as CSV` pada Tab User Action
22. Verifikasi berkas unduhan Tab User Action terunduh

### TC-GS-ACTLOG-223: Aksi saat Client suspended tetap tercatat

23. Di Tab User Action, ketik Search `Berkas Sistem {runId}-059.png`, tekan Enter, atur ukuran halaman 100, catat jumlah baris yang tampil sebagai baseline (hanya entri seed), lalu picu auto-purge berkas `Berkas Sistem {runId}-059.png` sebagai proses sistem di modul File Manager pada Client uji yang sedang Suspended dan tunggu job selesai
24. Muat ulang Tab User Action
25. Ketik Search `Berkas Sistem {runId}-059.png`, tekan Enter
26. Verifikasi jumlah baris hasil Search bertambah satu dari baseline langkah 23 dan baris baru untuk `Berkas Sistem {runId}-059.png` ber-Modified By `System` (entri aksi proses sistem, berbeda dari entri aksi seed) tampil di Tab User Action

### Pemulihan state akhir spec

27. Klik `(←)` pada kotak Search Tab User Action

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 6, 9, 17, 20, dan 27 (membersihkan Search dan Filter lewat `(←)` dan [Clear Field]); menunggu job selesai pada langkah 23 mendahului muat ulang (S-03). Subjudul "Pemulihan state" bukan TC sumber.
- Baseline TC-GS-ACTLOG-223 bukan nol: seed berkas lewat API sudah menghasilkan entri bernama sama. Baseline diambil sesudah seed dan sebelum proses sistem (langkah 23, jumlah baris yang tampil; PRD tidak punya indikator total), dan langkah 26 membedakan entri proses sistem lewat Modified By `System` (S-12). Langkah 23 menggabungkan pencatatan baseline dan pemicu karena keduanya satu keadaan awal.
- P-2: pemicu job latar (auto-purge File Manager) pada TC-GS-ACTLOG-223 hanya membentuk kondisi yang diuji (aksi proses sistem saat Client Suspended tercatat) dan bukan objek uji; proses sistem atau job latar yang hanya menjadi pemicu boleh berada di spec kelas h (keputusan 2026-10-21).
- Kelas harness h (state tenant); satu spec dengan dua TC karena keduanya memakai Client uji dan status yang sama.
- Pembagian TC lintas spec: TC-GS-ACTLOG-224 (tier plan) ada di spec 060; TC-GS-ACTLOG-225 (log lama) di spec 061.
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 9 dan 20 mengikuti TC-GS-ACTLOG-222.
  - Judul TC-GS-ACTLOG-222 menyebut "suspended atau expired", sedangkan Precondition dan Langkah Uji hanya memuat Client suspended; kondisi Expired tidak diuji. Fixture Client uji Expired (`GS_CLIENTEXP_TC_PASSWORD`) sudah ada bila QA menambah TC-nya.
  - TC-GS-ACTLOG-222 tidak menyebut keyword Search, nilai Filter, dan format Download yang dipakai; spec memakai `Login` (Tab Session) dan `Brand Seed {runId}-059` (Tab User Action) untuk Search, Activity `Login` dan Action `Create` untuk Filter, serta `Download as CSV`.
  - TC-GS-ACTLOG-223 tidak menyebut proses sistem yang dimaksud, Action, atau Name entri; spec memakai auto-purge File Manager dan mencari entri lewat nama berkas seed. Pemicu proses sistem pada Client Suspended disediakan tim FE/BE.
  - Mekanisme mengubah status Client menjadi Suspended tidak didefinisikan di TC maupun PRD Activity Log (Client Lifecycle di modul lain); disediakan tim FE/BE.
