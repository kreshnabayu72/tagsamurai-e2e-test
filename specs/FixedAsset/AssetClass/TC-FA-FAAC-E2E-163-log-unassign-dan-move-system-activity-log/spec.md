---
id: TC-FA-FAAC-E2E-163-log-unassign-dan-move-system-activity-log
title: "Log Unassign dan Move Asset Name pada System Log, Activity Log, dan Changelog"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-544
  - TC-FA-FAAC-545
  - TC-FA-FAAC-546
sourceRules: ["L-07", "§8.2#p1", "§8.2#r1", "§8.3#p1", "L-08", "§8.4#r7", "§4.1.1#r32"]
smoke: []
dependsOn: []
trace:
  "L-07": [9, 10, 12, 13]
  "§8.2#p1": [9, 38]
  "§8.2#r1": [10, 39]
  "§8.3#p1": [12, 13, 41, 42]
  "L-08": [24, 25, 26, 39, 42]
  "§8.4#r7": [24, 38, 41]
  "§4.1.1#r32": 27
coverage:
  web: automated
---

# Log Unassign dan Move Asset Name pada System Log, Activity Log, dan Changelog

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Light Vehicles` (`LT-VEH`) memiliki Asset Name `Dock Leveler`, `Utility Cart`, dan `Tool Trolley` (masing-masing 0 aset aktif); Asset Class Active `Machinery` (`MACHINERY`).
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Dock Leveler kembali ke LT-VEH, Utility Cart dan Tool Trolley kembali ke LT-VEH dari MACHINERY.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-544: Unassign Asset Name tercatat di System Log dan Activity Log (L-07)

1. Catat jumlah entri System Log aktor (Ns) dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
2. Ketik Search `LT-VEH`, tekan Enter
3. Klik link Class Code `LT-VEH` di tabel
4. Klik tab `Asset Names`
5. Klik ikon `⋯` pada baris `Dock Leveler`, lalu pilih `Unassign`
6. Klik `[Unassign]`
7. Tunggu aksi selesai
8. Buka Global Settings > User > Detail User milik aktor > Tab System Log
9. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
10. Verifikasi baris teratas System Log: Action `Edit`, Object `Asset Class`, Name `LT-VEH`, Field `Asset Names`, Old Value `Dock Leveler`, New Value `—`
11. Buka Activity Log FAMS
12. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
13. Verifikasi baris teratas Activity Log: baris yang sama dengan Modified By `Rina W`

### TC-FA-FAAC-545: Move Asset Name menghasilkan dua entri Changelog (L-08)

14. Buka Fixed Asset > Settings > Accounting > tab Asset Class
15. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
16. Ketik Search `LT-VEH`, tekan Enter
17. Klik link Class Code `LT-VEH` di tabel
18. Klik tab `Asset Names`
19. Klik ikon `⋯` pada baris `Utility Cart`, lalu pilih `Move`
20. Pilih `Destination Asset Class` = `MACHINERY – Machinery`, lalu klik `[Move]`
21. Tunggu aksi selesai
22. Klik kembali ke tabel Asset Class
23. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
24. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
25. Verifikasi entri Asset Class asal: Action `Edit`, Class Code `LT-VEH`, Field `Asset Names`, Old Value `Utility Cart`, New Value `—`
26. Verifikasi entri Asset Class tujuan: Action `Edit`, Class Code `MACHINERY`, Field `Asset Names`, Old Value `—`, New Value `Utility Cart`
27. Verifikasi kolom Modified By kedua entri `Rina W`
28. Tutup modal Changelog

### TC-FA-FAAC-546: Move Asset Name tercatat dua entri di System Log dan Activity Log (L-08)

29. Buka Fixed Asset > Settings > Accounting > tab Asset Class
30. Catat jumlah entri System Log aktor (Ns) dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
31. Ketik Search `LT-VEH`, tekan Enter
32. Klik link Class Code `LT-VEH` di tabel
33. Klik tab `Asset Names`
34. Klik ikon `⋯` pada baris `Tool Trolley`, lalu pilih `Move`
35. Pilih `Destination Asset Class` = `MACHINERY – Machinery`, lalu klik `[Move]`
36. Tunggu aksi selesai
37. Buka Global Settings > User > Detail User milik aktor > Tab System Log
38. Verifikasi jumlah entri System Log bertambah tepat 2 dari Ns
39. Verifikasi dua baris teratas System Log: Action `Edit`, Object `Asset Class`, Field `Asset Names`, yaitu Name `LT-VEH` (Old Value `Tool Trolley`, New Value `—`) dan Name `MACHINERY` (Old Value `—`, New Value `Tool Trolley`)
40. Buka Activity Log FAMS
41. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
42. Verifikasi dua baris teratas Activity Log: dua baris yang sama dengan Modified By `Rina W`

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan awal tiap blok TC (baseline log), langkah 2, 16, dan 31 (Search kode `LT-VEH` untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris), langkah kembali ke layar awal sebelum TC berikutnya, dan langkah "Tunggu aksi selesai" sesudah `[Unassign]` dan `[Move]` yang hasilnya tidak diasersi langsung sebelum pindah surface.
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: TC-544 dan TC-546 menyebut Detail User aktor dan Activity Log tanpa kolom Date yang diasersi; spec mengasersi Action, Object, Name, Field, Old Value, New Value, dan Modified By.
