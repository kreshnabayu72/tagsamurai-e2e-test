---
id: TC-FA-FAAC-E2E-104-versi-scheduled-cancel-dialog-d24
title: "Versi Scheduled: Dialog Cancel Scheduled Version (D-24), Konfirmasi, Back, dan Penolakan Server"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-330
  - TC-FA-FAAC-331
  - TC-FA-FAAC-332
  - TC-FA-FAAC-333
  - TC-FA-FAAC-334
sourceRules: ["§4.1#r12", "§3.11#p1", "E-FAAC-115", "F-FAAC-17.k2", "T-15", "F-FAAC-17.k3", "L-13", "F-FAAC-17.k4", "E-FAAC-117", "FAAC-LOGIC-07b"]
smoke: []
dependsOn: []
trace:
  "§4.1#r12": 4
  "§3.11#p1": 4
  "E-FAAC-115": [7, 10]
  "F-FAAC-17.k2": [8, 9]
  "T-15": [14, 26]
  "F-FAAC-17.k3": [15, 17, 37, 39]
  "L-13": [19, 20, 42]
  "F-FAAC-17.k4": [26, 27, 28]
  "E-FAAC-117": 29
  "FAAC-LOGIC-07b": 40
coverage:
  web: automated
---

# Versi Scheduled: Dialog Cancel Scheduled Version (D-24), Konfirmasi, Back, dan Penolakan Server

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`; memiliki hak Update). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-SCHED` "Scheduled Fixture" dengan satu versi Scheduled sejak M+2 (M = bulan berjalan menurut zona waktu General Settings, NC-11); Asset Class `B-SCHED2` dengan dua versi Scheduled M+2 dan M+4. Bulan pada dialog, Alert, dan Changelog ditulis MMM YYYY.
- Jam: TC-334 memajukan jam server dan jam browser bersama ke bulan Effective From (M+2) (bagian 6 konvensi); keduanya dipulihkan segera sesudah diasersi (langkah penghubung) dan oleh hook `after`. Spec ini membutuhkan sesi UI dan sesi API aktor yang tetap valid selama jam digeser (kemampuan suite, lihat suite.md).
- Changelog dibaca lewat kemampuan baca Changelog yang disediakan tim FE/BE: jumlah entri dicatat sebelum aksi dan asersi memakai selisih (audit trail permanen, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: versi Scheduled `B-SCHED` dan `B-SCHED2` dibuat ulang (M+2 pada `B-SCHED`; M+2 dan M+4 pada `B-SCHED2`). Pemulihan `B-SCHED` juga dilakukan sebagai langkah penghubung sebelum TC-334.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan versi itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-SCHED`, tekan Enter
2. Klik link Class Code `B-SCHED` di tabel

### TC-FA-FAAC-330: Screening dialog Cancel Scheduled Version

3. Klik tombol `Cancel scheduled version` pada Alert
4. Verifikasi Dialog `Cancel Scheduled Version` (MD, tanpa field) memuat tiga baris `B-SCHED – Scheduled Fixture`, `Effective From [MMM YYYY]` (bulan M+2), dan `Are you sure you want to cancel this scheduled version?` dengan tombol `Back` dan `Cancel version` (merah)
5. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log

### TC-FA-FAAC-332: Back pada D-24 tidak membatalkan versi

6. Klik `Back`
7. Verifikasi tidak ada toast yang tampil
8. Verifikasi dialog menutup
9. Verifikasi Alert versi Scheduled tetap tampil
10. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-331: Cancel Scheduled Version dikonfirmasi

11. Catat jumlah entri Changelog sebagai baseline N
12. Klik `Cancel scheduled version`
13. Klik `Cancel version`
14. Verifikasi toast sukses `Success, scheduled version has been cancelled.`
15. Verifikasi Alert versi Scheduled hilang
16. Klik tab `Depreciation`
17. Verifikasi nilai berlaku tidak berubah (sama dengan nilai berlaku pada seed)
18. Buka Changelog
19. Verifikasi jumlah entri Changelog bertambah 1 dari N
20. Verifikasi entri teratas adalah Edit Field `Scheduled Version` Old `[MMM YYYY]` (M+2) New `—`
21. Tutup modal Changelog

### TC-FA-FAAC-334: Cancel Scheduled Version ditolak bila bulan Effective From sudah dimulai saat Confirm

22. Pulihkan versi Scheduled `B-SCHED` sejak M+2 lewat fixture BE hingga tersimpan, lalu muat ulang halaman
23. Klik `Cancel scheduled version`
24. Majukan jam server dan jam browser ke bulan Effective From (M+2)
25. Klik `Cancel version`
26. Verifikasi toast error `Error, failed to cancel scheduled version.`
27. Verifikasi dialog D-24 menutup
28. Verifikasi Alert versi Scheduled disegarkan sesuai data terbaru
29. Verifikasi server menolak tanpa mengubah data (versi Scheduled `B-SCHED` tetap ada, dibaca lewat fixture BE)
30. Pulihkan jam server dan jam browser ke waktu semula

### TC-FA-FAAC-333: Pembatalan mengenai versi Scheduled paling awal dan versi terakhir tidak berubah

31. Klik breadcrumb `Asset Class`
32. Ganti isi kotak search dengan `B-SCHED2`, tekan Enter
33. Klik link Class Code `B-SCHED2` di tabel
34. Catat jumlah entri Changelog sebagai baseline N
35. Klik `Cancel scheduled version`
36. Klik `Cancel version`
37. Verifikasi Alert kini menampilkan `Next version starts [MMM YYYY].` untuk versi M+4
38. Klik tab `Depreciation`
39. Verifikasi nilai berlaku tidak berubah (sama dengan nilai berlaku pada seed)
40. Verifikasi Effective From versi terakhir yang dipakai V-25 tetap versi M+4
41. Buka Changelog
42. Verifikasi jumlah entri Changelog bertambah 1 dari N, yaitu satu entri L-13 untuk Effective From M+2
43. Tutup modal Changelog
44. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: dialog dan Back (TC-330, TC-332) lebih dulu, lalu konfirmasi yang membatalkan versi (TC-331), penolakan server pada jam yang dimajukan (TC-334) sesudah versi dipulihkan, dan TC-333 pada Asset Class lain di akhir.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan 32 (Search untuk menemukan baris target, R-16), langkah 5, 11, 34 (baseline Changelog, S-12), langkah 16 dan 38 (pindah ke tab Depreciation untuk membaca nilai berlaku), langkah 21 dan 43 (menutup modal Changelog), langkah 22 (memulihkan versi Scheduled), langkah 30 (memulihkan jam, S-09), langkah 31 (kembali ke tabel), dan langkah 44 (mengosongkan Search).
3. Entri Changelog baru dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (S-14).
4. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan versi Scheduled tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
5. Alasan melebihi sekitar 35 langkah (44 langkah): spec berisi lima blok TC yang berdiri sendiri pada dialog D-24 yang sama; tiap blok memakai versi Scheduled yang dipulihkan fixture BE sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna dan blok jam (TC-334) terisolasi.
6. S-05 (prinsip 13g): Expected "tidak ada log" pada TC-332 diasersi di spec ini (langkah 10) dengan `Verifikasi` selisih jumlah entri Changelog terhadap baseline (langkah 5); aksinya bukan request langsung (kelas a). TC tidak menyebut surface log selain "log"; yang diasersi Changelog.
7. Id P/K: pergeseran jam server dan jam browser pada TC-334 adalah langkah rutin spec fungsional (bagian 4 kelas d, keputusan 2026-10-13) dan jam dipulihkan sesudahnya (S-09), bukan objek uji harness; tidak ada id P/K dari daftar pengecualian yang berlaku untuk TC-334.
8. Temuan untuk QA: TC-333 Expected b ("Effective From versi terakhir yang dipakai V-25 tetap versi M+4") tidak menyebut cara observasi; spec mengasersi klausa itu apa adanya dan Alert langkah 37 menjadi penanda versi M+4 yang tersisa. TC-334 tidak menyebut keadaan Alert sesudah penolakan selain "disegarkan sesuai data terbaru". TC-331 dan TC-333 tidak menyebut nilai Useful Life berlaku; spec membandingkannya dengan nilai seed.
