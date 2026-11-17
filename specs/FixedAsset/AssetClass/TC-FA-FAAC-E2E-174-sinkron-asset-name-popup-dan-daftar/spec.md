---
id: TC-FA-FAAC-E2E-174-sinkron-asset-name-popup-dan-daftar
title: "Sinkronisasi Asset Name: Banner, Popup Used By, Daftar Asset Name, Register Asset, dan Dampak Aset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-579
  - TC-FA-FAAC-580
  - TC-FA-FAAC-581
  - TC-FA-FAAC-582
  - TC-FA-FAAC-585
sourceRules: ["S-13", "§4.1.1#p3", "S-07a", "S-15", "FAAC-LOGIC-14a", "FAAC-LOGIC-14b", "D-11", "FAAC-LOGIC-07f", "FAAC-LOGIC-07c"]
smoke: []
dependsOn: []
trace:
  "S-13": 9
  "§4.1.1#p3": 9
  "S-07a": 20
  "S-15": 23
  "FAAC-LOGIC-14a": 30
  "FAAC-LOGIC-14b": [33, 34]
  "D-11": 41
  "FAAC-LOGIC-07f": 41
  "FAAC-LOGIC-07c": 42
anchor: [28, 29]
coverage:
  web: automated
---

# Sinkronisasi Asset Name: Banner, Popup Used By, Daftar Asset Name, Register Asset, dan Dampak Aset

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Name `Old Pallet`, `Old Hand Truck`, `Tail Lift`, dan `Tail Lift Spare`; akun Asset Cost `1-2100 – Vehicles Cost` dipetakan ke `LT-VEH`; `LT-VEH` dengan Assets = 6 dan Useful Life 48 pada TC-585. Keadaan awal Asset Name tanpa Asset Class per TC dinyatakan di Keadaan awal dinamis.
- Keadaan awal dinamis: fixture BE menyetel keadaan awal tiap TC pada langkah pertama blok-nya karena banner Asset Name tanpa Asset Class menghitung seluruh Asset Name tanpa Asset Class: tepat 2 (`Old Pallet` dan `Old Hand Truck`) pada TC-579 (langkah 1); `Tail Lift` tanpa Asset Class dan `LT-VEH` memiliki 1 Asset Name pada TC-580 (langkah 10); `Tail Lift Spare` tanpa Asset Class pada TC-581 dan TC-582 (langkah 25 dan 31).
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Kemampuan teknis: modul Asset dengan alur Register Asset (field wajib mengikuti fixture; copy toast sukses mengikuti PRD Asset).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Old Pallet dibuat ulang; Tail Lift kembali tanpa Asset Class; aset yang didaftarkan TC-582 dihapus; LT-VEH kembali ke Useful Life 48. Banner Asset Name tanpa Asset Class bergantung pada data bersama client sehingga suite berjalan serial.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-579: Menghapus Asset Name tanpa Asset Class mengurangi banner

1. Setel keadaan awal lewat fixture BE: tepat 2 Asset Name tanpa Asset Class, `Old Pallet` dan `Old Hand Truck` (precondition TC-579)
2. Buka Fixed Asset > Settings > Accounting > tab Asset Class
3. Buka Settings > Asset Master > Asset Name
4. Ketik Search `Old Pallet`, tekan Enter
5. Hapus Asset Name `Old Pallet`
6. Klik `Delete` pada dialog konfirmasi
7. Tunggu aksi selesai
8. Buka Fixed Asset > Settings > Accounting > tab Asset Class
9. Verifikasi banner: `1 asset name has no asset class and will not be depreciated.`

### TC-FA-FAAC-580: Popup Used By Chart of Accounts mencerminkan jumlah Asset Name per Asset Class setelah Assign

10. Setel keadaan awal lewat fixture BE: `Tail Lift` tanpa Asset Class dan `LT-VEH` memiliki 1 Asset Name (precondition TC-580)
11. Buka Fixed Asset > Settings > Accounting > tab Asset Class
12. Ketik Search `LT-VEH`, tekan Enter
13. Klik link Class Code `LT-VEH` di tabel
14. Klik tab `Asset Names`
15. Klik tombol `+ Assign Asset Names`
16. Centang `Tail Lift`
17. Klik `[Assign]`
18. Tunggu aksi selesai
19. Kembali ke tabel Asset Class lewat Breadcrumb
20. Verifikasi baris `LT-VEH` menampilkan Asset Names = 2
21. Klik tab `Chart of Accounts`
22. Buka popup Used By akun `1-2100 – Vehicles Cost`
23. Verifikasi popup Used By mencantumkan Asset Class `LT-VEH` dengan jumlah Asset Name 2, sama dengan kolom Asset Names tabel Asset Class
24. Tutup popup Used By

### TC-FA-FAAC-581: Asset Name tanpa Asset Class tidak diberi tanda di daftar Asset Name

25. Setel keadaan awal lewat fixture BE: `Tail Lift Spare` tanpa Asset Class (precondition TC-581)
26. Buka Settings > Asset Master > Asset Name
27. Ketik Search `Tail Lift Spare`, tekan Enter
28. Verifikasi baris `Tail Lift Spare` tampil
29. Verifikasi sedikitnya satu kolom Asset Name lain tampil pada daftar
30. Verifikasi baris `Tail Lift Spare` tampil seperti Asset Name lain tanpa tanda, ikon, atau kolom Asset Class

### TC-FA-FAAC-582: Aset di bawah Asset Name tanpa Asset Class tetap dapat dibuat

31. Setel keadaan awal lewat fixture BE: `Tail Lift Spare` tanpa Asset Class (precondition TC-582)
32. Buka modul Asset dan daftarkan aset baru dengan Asset Name `Tail Lift Spare` mengikuti alur Register Asset
33. Verifikasi aset berhasil dibuat sesuai alur Register Asset (copy toast sesuai PRD Asset)
34. Verifikasi tidak ada penolakan atau peringatan terkait Asset Class

### TC-FA-FAAC-585: Mengubah aturan penyusutan pada Asset Class yang dipakai aset menampilkan dampak jumlah aset

35. Buka Fixed Asset > Settings > Accounting > tab Asset Class
36. Ketik Search `LT-VEH`, tekan Enter
37. Klik link Class Code `LT-VEH` di tabel
38. Klik tab `Depreciation`
39. Ubah Useful Life dari `48` menjadi `60`
40. Klik `[Save]`
41. Verifikasi dialog `Apply Changes` tampil dengan blok pratinjau `Assets affected` bernilai 6
42. Verifikasi checkbox `Apply to existing assets` tercentang
43. Klik `Cancel` pada dialog `Apply Changes`
44. Kembalikan Useful Life ke `48`

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 10, 25, dan 31 (Setel keadaan awal lewat fixture BE, S-11), langkah 12 dan 36 (Search kode `LT-VEH` di tabel untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris), langkah 4 dan 27 (Search di daftar Asset Name untuk menemukan baris target sebelum `Hapus`, R-16), langkah "Tunggu aksi selesai" sesudah `Delete` dan `[Assign]` yang hasilnya tidak diasersi langsung sebelum pindah modul atau surface, menutup popup Used By, mengembalikan Useful Life `LT-VEH` pada TC-585 (S-09, form tidak dibiarkan dirty), dan kembali ke layar awal.
2. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
3. Alasan jumlah langkah: jumlah nominal 44 langkah melampaui sekitar 35 langkah karena lima TC sinkronisasi Asset Name yang tiap bloknya berstate sendiri dan dua langkah penghubung "Tunggu aksi selesai" (8b butir 8); semua TC satu topik dan tiap blok berdiri sendiri dengan seed sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
4. Temuan untuk QA: (a) TC-582 tidak menyebut field wajib Register Asset dan teks toast sukses (merujuk PRD Asset); spec mengasersi toast tanpa teks (S-02). (b) TC-579 tidak menyebut dialog konfirmasi Delete Asset Name; spec menulis `Delete` pada dialog. (c) TC-581 tidak menyebut Search; spec mencari baris target lewat Search. (d) TC-585 menulis dialog `Apply Changes` tanpa tombol; spec menutupnya dengan `Cancel`.
