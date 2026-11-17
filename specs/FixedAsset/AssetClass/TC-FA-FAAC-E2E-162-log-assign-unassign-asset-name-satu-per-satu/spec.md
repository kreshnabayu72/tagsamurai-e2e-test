---
id: TC-FA-FAAC-E2E-162-log-assign-unassign-asset-name-satu-per-satu
title: "Log Assign dan Unassign Asset Name Satu per Satu pada Tiga Surface"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-541
  - TC-FA-FAAC-542
  - TC-FA-FAAC-543
sourceRules: ["L-06", "§4.1.1#r26", "§4.1.1#r32", "§8.2#p1", "§8.2#r1", "§8.3#p1", "L-07"]
smoke: []
dependsOn: []
trace:
  "L-06": [12, 13, 29]
  "§4.1.1#r26": 14
  "§4.1.1#r32": [15, 46]
  "§8.2#p1": 28
  "§8.2#r1": 29
  "§8.3#p1": [31, 32]
  "L-07": [44, 45]
coverage:
  web: automated
---

# Log Assign dan Unassign Asset Name Satu per Satu pada Tiga Surface

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Light Vehicles` (`LT-VEH`) tanpa Asset Name; Asset Name tanpa Asset Class `Hand Truck` (0 aset aktif); `Roller Cart` (0 aset aktif) tersedia untuk di-assign ke `LT-VEH` pada TC-543.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Jam server dan jam browser sinkron dan tidak digeser spec ini; bulan berjalan M mengikuti zona waktu General Settings client (NC-11). Kolom Date entri log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: LT-VEH dikembalikan tanpa Asset Name; Hand Truck dan Roller Cart kembali tanpa Asset Class.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-541: Assign Asset Name tercatat di Changelog Asset Class (L-06)

1. Setel keadaan awal lewat fixture BE: `LT-VEH` tanpa Asset Name dan `Hand Truck` tanpa Asset Class (precondition TC-541, tidak diasersi)
2. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
3. Ketik Search `LT-VEH`, tekan Enter
4. Klik link Class Code `LT-VEH` di tabel
5. Klik tab `Asset Names`
6. Klik tombol `+ Assign Asset Names`
7. Centang `Hand Truck`
8. Klik `[Assign]`
9. Catat waktu aksi sesudah `[Assign]` selesai
10. Klik kembali ke tabel Asset Class
11. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
12. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
13. Verifikasi baris teratas Changelog: Action `Edit`, Class Code `LT-VEH`, Field `Asset Names`, Old Value `—`, New Value `Hand Truck`
14. Verifikasi kolom Date baris teratas berisi waktu aksi (format General Settings, toleransi satu menit)
15. Verifikasi kolom Modified By baris teratas `Rina W` (aktor)
16. Tutup modal Changelog

### TC-FA-FAAC-542: Assign Asset Name tercatat di System Log dan Activity Log (L-06)

17. Buka Fixed Asset > Settings > Accounting > tab Asset Class
18. Pulihkan lewat fixture BE: `LT-VEH` tanpa Asset Name dan `Hand Truck` tanpa Asset Class (precondition TC-542, tidak diasersi)
19. Catat jumlah entri System Log aktor (Ns) dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
20. Ketik Search `LT-VEH`, tekan Enter
21. Klik link Class Code `LT-VEH` di tabel
22. Klik tab `Asset Names`
23. Klik tombol `+ Assign Asset Names`
24. Centang `Hand Truck`
25. Klik `[Assign]`
26. Tunggu aksi selesai
27. Buka Global Settings > User > Detail User milik aktor > Tab System Log
28. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
29. Verifikasi baris teratas System Log (kolom Date, Action, Object, Name, Field, Old Value, New Value): Action `Edit`, Object `Asset Class`, Name `LT-VEH`, Field `Asset Names`, Old Value `—`, New Value `Hand Truck`
30. Buka Activity Log FAMS
31. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
32. Verifikasi baris teratas Activity Log (kolom Date, Action, Object, Name, Field, Old Value, New Value, Modified By): baris yang sama dengan Modified By `Rina W`

### TC-FA-FAAC-543: Unassign Asset Name tercatat di Changelog Asset Class (L-07)

33. Buka Fixed Asset > Settings > Accounting > tab Asset Class
34. Pulihkan lewat fixture BE: `LT-VEH` memiliki Asset Name `Roller Cart` (0 aset aktif) (precondition TC-543, tidak diasersi)
35. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
36. Ketik Search `LT-VEH`, tekan Enter
37. Klik link Class Code `LT-VEH` di tabel
38. Klik tab `Asset Names`
39. Klik ikon `⋯` pada baris `Roller Cart`, lalu pilih `Unassign`
40. Klik `[Unassign]`
41. Tunggu aksi selesai
42. Klik kembali ke tabel Asset Class
43. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
44. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
45. Verifikasi baris teratas Changelog: Action `Edit`, Class Code `LT-VEH`, Field `Asset Names`, Old Value `Roller Cart`, New Value `—`
46. Verifikasi kolom Modified By baris teratas `Rina W`
47. Tutup modal Changelog

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (fixture BE menyetel keadaan awal blok TC-541, tidak diasersi), baseline log di awal tiap blok TC, langkah "Catat waktu aksi" (S-12), langkah 18 dan 34 (pemulihan seed lewat fixture BE sebagai precondition TC, tidak diasersi), langkah 3, 20, dan 36 (Search kode `LT-VEH` untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris sehingga baris tidak dijangkau lewat posisi), langkah kembali ke layar awal, dan langkah "Tunggu aksi selesai" sesudah `[Assign]` dan `[Unassign]` yang hasilnya tidak diasersi langsung sebelum pindah surface.
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: (a) TC-541 menulis Date "waktu aksi (format General Settings)" tanpa toleransi; spec memakai toleransi satu menit karena kolom Date berketelitian menit. (b) TC-542 dan TC-544 menyebut "Detail User milik aktor" tanpa menyebut aktornya selain Total Control; spec memakai akun aktor spec ini.
6. Pembagian TC lintas spec: TC-542 dan TC-543 menyebut Asset Name yang sama dengan TC-541 (Hand Truck); tiap TC memulihkan seed-nya sendiri.
