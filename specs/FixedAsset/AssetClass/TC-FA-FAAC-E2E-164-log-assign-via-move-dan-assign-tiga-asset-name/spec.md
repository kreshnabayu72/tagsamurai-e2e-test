---
id: TC-FA-FAAC-E2E-164-log-assign-via-move-dan-assign-tiga-asset-name
title: "Log Assign sebagai Move dan Assign Tiga Asset Name pada Changelog"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-547
  - TC-FA-FAAC-548
sourceRules: ["FAAC-LOGIC-13c", "F-FAAC-08.k1", "L-08", "§8.4#r7", "L-06", "§8.4#r6"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-13c": 12
  "F-FAAC-08.k1": 12
  "L-08": [12, 13, 14]
  "§8.4#r7": 12
  "L-06": [27, 28, 29, 30]
  "§8.4#r6": 27
coverage:
  web: automated
---

# Log Assign sebagai Move dan Assign Tiga Asset Name pada Changelog

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Light Vehicles` (`LT-VEH`) tanpa Asset Name; Asset Name `Box Truck` (0 aset aktif) ter-assign ke `Machinery` (`MACHINERY`); Asset Name tanpa Asset Class `Hand Cart`, `Pallet Truck`, dan `Drum Dolly` (masing-masing 0 aset aktif).
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Box Truck kembali ke MACHINERY; Hand Cart, Pallet Truck, Drum Dolly, dan Box Truck dilepas dari LT-VEH.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-547: Move lewat dialog Assign dicatat sebagai L-08 dengan dua entri

1. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
2. Ketik Search `LT-VEH`, tekan Enter
3. Klik link Class Code `LT-VEH` di tabel
4. Klik tab `Asset Names`
5. Klik tombol `+ Assign Asset Names`
6. Hilangkan centang `Without asset class only`
7. Centang `Box Truck`
8. Klik `[Assign]`
9. Tunggu aksi selesai
10. Klik kembali ke tabel Asset Class
11. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
12. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc (tepat dua entri L-08, tanpa entri L-06 tunggal tambahan)
13. Verifikasi entri Asset Names Class Code `MACHINERY`: Old Value `Box Truck`, New Value `—`
14. Verifikasi entri Asset Names Class Code `LT-VEH`: Old Value `—`, New Value `Box Truck`
15. Tutup modal Changelog

### TC-FA-FAAC-548: Assign tiga Asset Name menulis satu entri L-06 per Asset Name

16. Buka Fixed Asset > Settings > Accounting > tab Asset Class
17. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
18. Ketik Search `LT-VEH`, tekan Enter
19. Klik link Class Code `LT-VEH` di tabel
20. Klik tab `Asset Names`
21. Klik tombol `+ Assign Asset Names`
22. Centang `Hand Cart`, `Pallet Truck`, dan `Drum Dolly`
23. Klik `[Assign]`
24. Tunggu aksi selesai
25. Klik kembali ke tabel Asset Class
26. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
27. Verifikasi jumlah entri Changelog bertambah tepat 3 dari Nc
28. Verifikasi entri Edit Field `Asset Names` Class Code `LT-VEH`: Old Value `—`, New Value `Hand Cart`
29. Verifikasi entri Edit Field `Asset Names` Class Code `LT-VEH`: Old Value `—`, New Value `Pallet Truck`
30. Verifikasi entri Edit Field `Asset Names` Class Code `LT-VEH`: Old Value `—`, New Value `Drum Dolly`
31. Tutup modal Changelog

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan awal tiap blok TC (baseline log), langkah 2 dan 18 (Search kode `LT-VEH` untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris), dan langkah kembali ke layar awal. Langkah "Tunggu aksi selesai" (9, 24) sesudah aksi tulis yang hasilnya tidak diasersi langsung, sebelum membuka log (8b butir 8).
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Temuan untuk QA: (a) Expected b TC-547 "Tidak ada entri L-06 tunggal untuk Box Truck" diasersi sebagai selisih tepat dua entri pada baseline yang dicatat; ini asersi jumlah, bukan asersi absence kelas g (bagian 3 prinsip 13g). (b) TC-548 menulis "Perhatikan baris paling atas" tetapi Expected menyebut tiga entri; spec membaca tiga baris teratas sebanyak selisih. (c) TC-547 tidak menyebut dialog Effective From atau pratinjau dampak pada Assign yang menjadi Move; Box Truck tanpa aset aktif sehingga dialog tersebut tidak ditulis.
