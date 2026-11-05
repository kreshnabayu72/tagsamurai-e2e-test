---
id: TC-FA-FAAC-E2E-161-log-status-delete-dan-penjadwalan-versi
title: "Log Activate, Deactivate, Delete, dan Penjadwalan Versi Scheduled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-534
  - TC-FA-FAAC-535
  - TC-FA-FAAC-536
coverage:
  web: automated
---

# Log Activate, Deactivate, Delete, dan Penjadwalan Versi Scheduled

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-LOG4` Active tanpa Asset Name; `B-LOG5` tanpa Asset Name, belum pernah diposting, dengan entri Create lama di Changelog; `B-ASSETS3` dipakai aset.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Jam server dan jam browser sinkron dan tidak digeser spec ini; bulan berjalan M mengikuti zona waktu General Settings client (NC-11). Kolom Date entri log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: B-LOG4 kembali Active; B-LOG5 dibuat ulang beserta entri Create lamanya; B-ASSETS3 kembali tanpa versi Scheduled.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-534: Log Activate dan Deactivate satu baris Status

1. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
2. Nonaktifkan `B-LOG4` lewat toggle Active pada baris, lalu klik `Deactivate` pada dialog `Deactivate Asset Class`
3. Aktifkan kembali `B-LOG4` lewat toggle Active, lalu klik `Activate` pada dialog
4. Tunggu aksi selesai
5. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
6. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
7. Verifikasi dua baris teratas Changelog: Action `Edit`, Field `Status`, Old Value `Active` New Value `Inactive`, lalu Old Value `Inactive` New Value `Active`
8. Verifikasi nilai Status pada kedua baris Changelog ditulis polos tanpa badge
9. Tutup modal Changelog
10. Buka Global Settings > User > Detail User milik aktor > Tab System Log
11. Verifikasi jumlah entri System Log bertambah tepat 2 dari Ns
12. Verifikasi dua baris teratas System Log memuat dua kejadian Status yang sama untuk `B-LOG4`
13. Buka Activity Log FAMS
14. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
15. Verifikasi dua baris teratas Activity Log memuat dua kejadian Status yang sama untuk `B-LOG4`

### TC-FA-FAAC-535: Log Delete memakai satu baris dan data tetap di log

16. Buka Fixed Asset > Settings > Accounting > tab Asset Class
17. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
18. Klik ikon `⋯` pada baris `B-LOG5`, lalu pilih `Delete`
19. Klik `Delete` pada dialog konfirmasi
20. Tunggu aksi selesai
21. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
22. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
23. Verifikasi baris teratas Changelog: Action `Delete`, Class Code `B-LOG5`, Field `Class Code`, Old Value `B-LOG5`, New Value `—`
24. Verifikasi entri Changelog yang sudah ada untuk `B-LOG5` (Create dari seed) tetap tampil sesudah Asset Class terhapus
25. Tutup modal Changelog
26. Buka Global Settings > User > Detail User milik aktor > Tab System Log
27. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
28. Verifikasi baris teratas System Log memuat kejadian Delete atas `B-LOG5`
29. Buka Activity Log FAMS
30. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
31. Verifikasi baris teratas Activity Log memuat kejadian Delete atas `B-LOG5`

### TC-FA-FAAC-536: Log penjadwalan versi satu baris Scheduled Version

32. Buka Fixed Asset > Settings > Accounting > tab Asset Class
33. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
34. Klik link Class Code `B-ASSETS3` di tabel
35. Klik tab `Depreciation`
36. Ubah Useful Life menjadi nilai berbeda dari seed (`72`)
37. Klik `Save`
38. Pada dialog `Apply Changes` pilih Effective From dua bulan sesudah bulan berjalan (M+2), lalu klik `Apply`
39. Tunggu aksi selesai
40. Kembali ke tabel Asset Class lewat Breadcrumb
41. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
42. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc (satu baris, bukan per field)
43. Verifikasi baris teratas Changelog: Action `Edit`, Field `Scheduled Version`, Old Value `—`, New Value `[MMM YYYY]` bulan M+2 (contoh `Dec 2026` bila M = Oct 2026)
44. Tutup modal Changelog

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): baseline log di awal tiap TC (langkah 1 dan langkah serupa di awal tiap blok TC), langkah kembali ke layar awal sebelum TC berikutnya, serta langkah "Tunggu aksi selesai" dan kembali ke tabel lewat Breadcrumb sesudah `Apply` versi Scheduled (hasil `Apply` tidak diasersi langsung; versi Scheduled tetap di Detail). Langkah "Tunggu aksi selesai" (4, 20) sesudah aksi tulis yang hasilnya tidak diasersi langsung, sebelum membuka log (8b butir 8).
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Pembagian TC lintas spec: TC-537 dan TC-538 ada di spec 175; Expected TC-538 butir b (System Log tidak memuat entri L-10 dan L-11) diasersi di spec 166 (S-05).
6. Temuan untuk QA: (a) TC-534 tidak menyebut dialog konfirmasi Deactivate dan Activate sedangkan Deactivate pada Asset Class lain memakai dialog; spec menulis dialog `Deactivate Asset Class` dan `Activate`. (b) TC-535 tidak menyebut dialog konfirmasi `Delete` dan entri Create lama `B-LOG5` pada Precondition; spec menambahkannya di Prerequisites. (c) TC-536 tidak menyebut nilai Useful Life baru; spec memakai 72.
