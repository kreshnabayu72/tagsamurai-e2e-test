---
id: TC-AC-ACC-E2E-313-job-scheduler-lifecycle-jam-server
title: "Job Lifecycle Otomatis dengan Jam Server Dimajukan: Auto-Archive Grace, Purge ke Deleted, Renewal Pending Menjadi Live, dan Trial Expired Lalu Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-669
  - TC-AC-ACC-670
  - TC-AC-ACC-964
  - TC-AC-ACC-1033
coverage:
  web: automated
---

# Job Lifecycle Otomatis dengan Jam Server Dimajukan: Auto-Archive Grace, Purge ke Deleted, Renewal Pending Menjadi Live, dan Trial Expired Lalu Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- State global: jam server (job scheduler lifecycle berjalan di server) diatur absolut lewat kemampuan manipulasi jam (disediakan tim FE/BE) dan jam browser/klien diatur bersama; keduanya dipulihkan ke waktu nyata setelah tiap blok TC dan di hook `after` (R-10, S-09). Tidak ada langkah "Tunggu N menit"; menunggu job memakai polling worker (muat ulang halaman tiap 5 detik sampai perubahan terlihat, batas 2 menit). Suite berjalan serial.
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-669: C-LIF-8 -> `PT Grace Tenggat {runId}-313` (Active; FAMS satu-satunya term Grace dengan Grace End 7 hari setelah tanggal seed; SAMS dan SIEM tidak pernah berlangganan).
  - TC-AC-ACC-670: C-LIF-9 -> `PT Purge Tenggat {runId}-313` (Archived; FAMS satu-satunya term Purge; tanggal akhir masa retensi post-purge R = tanggal seed + 7 hari, tercatat di keluaran skrip seed; tanggal ini tidak tampil di UI Client).
  - TC-AC-ACC-964: C-W3LIF-3 -> `PT Renewal Berjadwal Dua {runId}-313` (Active; FAMS predecessor Active `SUBS-20260101-W3L04` + Renewal Pending `SUBS-20260901-W3L05` dengan tanggal mulai di masa depan = End predecessor + 1 hari).
  - TC-AC-ACC-1033: C-FX18-4 -> `PT Trial Arsip Saja {runId}-313` (Active; SAMS Trial Active satu-satunya term dengan End Date jatuh pada hari uji; Group Area Jakarta).
- Zona waktu: Time Zone General Settings tenant uji. Kadens job tidak disebut PRD Client (asumsi lingkungan uji: waktu uji pukul 01:00 pada hari setelah tenggat); eksekusi job berikutnya dipicu dengan memajukan jam server satu interval job (nilai interval disediakan tim FE/BE).

## Test Steps

### Auto-Archive saat Grace melewati batas (TC-AC-ACC-669)

1. Klik `[Changelog]` di toolbar List, ketik Search `PT Grace Tenggat {runId}-313` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Auto-Archive` (N1), lalu tutup modal
2. Klik sub-tab Active, ketik Search `PT Grace Tenggat {runId}-313`, tekan Enter
3. Verifikasi sel FAMS `Grace`
4. Klik Company Name `PT Grace Tenggat {runId}-313`, buka Tab Subscription sub-tab FAMS, dan catat Grace End pada Subscription Details sebagai G
5. Verifikasi Subscription Details menampilkan Status badge `Grace`
6. Verifikasi Grace End terisi tanggal (G)
7. Atur jam server dan jam browser ke pukul 01:00 pada hari setelah G (absolut, zona waktu General Settings)
8. Muat ulang Admin Console > Client tiap 5 detik (batas 2 menit) sampai job lifecycle berjalan, klik sub-tab Archived, ketik Search `PT Grace Tenggat {runId}-313`, tekan Enter
9. Verifikasi `PT Grace Tenggat {runId}-313` tampil di sub-tab Archived tanpa aksi manual
10. Verifikasi sel FAMS `Archive`
11. Pulihkan jam server dan jam browser ke waktu nyata
12. Klik `[Changelog]` di toolbar List, ketik Search `PT Grace Tenggat {runId}-313` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Auto-Archive` (N2), dan lihat baris terbaru
13. Verifikasi N2 = N1 + 1
14. Verifikasi baris terbaru Action `Auto-Archive`, Client Name `PT Grace Tenggat {runId}-313`, Field `Status`, Old Value `Active`, New Value `Archived`, Modified By `System`
15. Tutup modal Changelog, picu eksekusi job lifecycle berikutnya (jam server dan jam browser dimajukan satu interval job), lalu pulihkan jam; klik sub-tab Archived, ketik Search `PT Grace Tenggat {runId}-313`, tekan Enter
16. Verifikasi `PT Grace Tenggat {runId}-313` tetap tampil di sub-tab Archived
17. Klik `[Changelog]` di toolbar List, ketik Search `PT Grace Tenggat {runId}-313` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Auto-Archive` (N3)
18. Verifikasi N3 = N2 (evaluasi berikutnya tidak menambah log)

### Transisi Purge ke Deleted otomatis (TC-AC-ACC-670)

19. Tutup modal Changelog, klik sub-tab Archived, ketik Search `PT Purge Tenggat {runId}-313`, tekan Enter
20. Verifikasi sel FAMS `Purge` (severity dark)
21. Atur jam server dan jam browser ke pukul 01:00 pada hari setelah R (absolut, zona waktu General Settings)
22. Muat ulang List tiap 5 detik (batas 2 menit), klik sub-tab Archived, ketik Search `PT Purge Tenggat {runId}-313`, tekan Enter, sampai sel FAMS berubah
23. Verifikasi sel FAMS `Deleted` (severity dark)
24. Verifikasi `PT Purge Tenggat {runId}-313` tetap di sub-tab Archived tanpa aksi manual
25. Pulihkan jam server dan jam browser ke waktu nyata, lalu klik Company Name `PT Purge Tenggat {runId}-313`, Tab Subscription, sub-tab FAMS
26. Verifikasi Section Subscription Details menampilkan Status badge `Deleted`
27. Verifikasi tidak ada tombol aksi dan tidak ada elipsis aksi (Delete/Purge manual tidak tersedia)

### Renewal Pending menjadi term live pada tanggal mulai (TC-AC-ACC-964)

28. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Renewal Berjadwal Dua {runId}-313`, tekan Enter
29. Verifikasi sel FAMS `Active`
30. Klik Company Name `PT Renewal Berjadwal Dua {runId}-313`, buka Tab Subscription sub-tab FAMS, dan catat End predecessor sebagai E
31. Verifikasi Subscription Details menampilkan Subscription ID `SUBS-20260101-W3L04` dengan Status badge `Active` (term Renewal Pending tidak menggantikannya)
32. Atur jam server dan jam browser ke pukul 23:59 pada E (hari sebelum tanggal mulai Renewal, E + 1 hari), tunggu job terjadwal berjalan lewat polling, lalu pulihkan jam
33. Muat ulang Tab Subscription sub-tab FAMS
34. Verifikasi Subscription Details tetap menampilkan Subscription ID `SUBS-20260101-W3L04` dengan Status badge `Active`
35. Atur jam server dan jam browser ke pukul 01:00 pada E + 1 hari (tanggal mulai Renewal), tunggu job terjadwal berjalan lewat polling, lalu pulihkan jam
36. Muat ulang Tab Subscription sub-tab FAMS
37. Verifikasi Subscription Details menampilkan Subscription ID `SUBS-20260901-W3L05` dengan Status badge `Active`
38. Verifikasi Start sama dengan E + 1 hari (tanggal mulai term Renewal)
39. Kembali ke Admin Console > Client, klik sub-tab Active, ketik Search `PT Renewal Berjadwal Dua {runId}-313`, tekan Enter
40. Verifikasi sel FAMS `Active`

### Trial Expired otomatis Archived lalu Delete (TC-AC-ACC-1033)

41. Klik sub-tab Active, ketik Search `PT Trial Arsip Saja {runId}-313`, tekan Enter
42. Verifikasi baris `PT Trial Arsip Saja {runId}-313` tampil di sub-tab Active
43. Verifikasi sel SAMS `Active` (Trial Active tidak dihitung untuk Auto-Archive)
44. Atur jam server dan jam browser melewati End Date Trial, tunggu job auto-expire trial berjalan lewat polling, lalu pulihkan jam
45. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Trial Arsip Saja {runId}-313`, tekan Enter
46. Verifikasi baris `PT Trial Arsip Saja {runId}-313` tampil di sub-tab Archived (Trial `Expired` dihitung sebagai term terminal)
47. Verifikasi sel SAMS `Expired`
48. Klik sub-tab Active, ketik Search `PT Trial Arsip Saja {runId}-313`, tekan Enter
49. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
50. Klik sub-tab Archived, ketik Search `PT Trial Arsip Saja {runId}-313`, tekan Enter, buka `⋯` baris `PT Trial Arsip Saja {runId}-313` → Delete, ketik nama persis `PT Trial Arsip Saja {runId}-313`, centang checkbox, lalu klik `[Delete]`
51. Verifikasi toast `Success, client has been deleted.`
52. Ganti isi kotak search dengan `PT Trial Arsip Saja {runId}-313`, tekan Enter
53. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`

## Notes

- Kelas d (harness eksternal: job scheduler dan jam server); keempat TC memakai harness yang sama (P-4 tidak dipakai karena jam dipulihkan antar blok dan Prerequisites menyatakan keadaan awal tiap blok). TC-AC-ACC-1033 (Delete) paling akhir (prinsip 5).
- Log yang dibuat saat jam digeser diasersi dengan selisih jumlah baris terhadap baseline (N1, N2, N3) dan mencari baris dengan Client Name bersuffix, bukan posisi teratas (S-12). Jam dipulihkan sebelum Changelog dibuka (S-09). Batas eksak: Prerequisites menyatakan jam diset absolut ke `G + 1 hari pukul 01:00`, `E pukul 23:59`, dan `E + 1 hari pukul 01:00` (bagian 6).
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (job lifecycle dengan jam server) dan data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi.
- Temuan untuk QA
  - F-10: Asersi langkah 34 (sesudah langkah 32, "tunggu job terjadwal berjalan lewat polling") dan langkah 18 (sesudah langkah 15, "picu eksekusi job lifecycle berikutnya") bergantung pada job latar yang tidak punya sinyal selesai; menunggu kemampuan "kueri fixture status job" (bagian 6 konvensi) dari tim BE/FE; diterima user 2026-11-03 (laporan e2e-audit F-10).
  - TC-AC-ACC-669: kadens job `bukan spesifikasi PRD Client`; langkah `Tunggu eksekusi job lifecycle berikutnya` tidak punya interval; spec memakai pemicu eksekusi berikutnya disediakan tim FE/BE.
  - TC-AC-ACC-670: nilai R hanya tersedia di keluaran skrip seed; spec membaca R dari keluaran itu (disediakan tim FE).
  - TC-AC-ACC-964: End predecessor (E) dibaca dari Subscription Details; batas waktu `pukul 23:59` dan `pukul 01:00` mengikuti Langkah TC.
