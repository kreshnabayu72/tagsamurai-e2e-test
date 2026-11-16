---
id: TC-FA-TDC-E2E-060-edit-kapitalisasi-no-op-class-code-sendiri-bukan-duplikat-dan-versi-baru-class-terkunci
title: "Edit: Kapitalisasi Class Code, Edit No-Op, Class Code Sendiri Bukan Duplikat, dan Versi Baru Class Terkunci"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-193
  - TC-FA-TDC-194
  - TC-FA-TDC-195
  - TC-FA-TDC-196
  - TC-FA-TDC-218
sourceRules: ["T-03", "E-FATDC-11", "F-FATDC-02.k2a", "V-04", "DO-01", "T-02a", "FATDC-LOGIC-04c", "§4.1.1#r2", "T-02c", "FATDC-LOGIC-04ad", "FATDC-LOGIC-04ac", "FATDC-LOGIC-04h", "ST-06", "FATDC-LOGIC-07a"]
smoke: []
dependsOn: []
trace:
  "T-03": [5, 10, 11]
  "E-FATDC-11": [6, 12]
  "F-FATDC-02.k2a": 7
  "V-04": [13, 19, 24]
  "DO-01": 14
  "T-02a": [18, 23]
  "FATDC-LOGIC-04c": 23
  "§4.1.1#r2": 26
  "T-02c": 33
  "FATDC-LOGIC-04ad": 36
  "FATDC-LOGIC-04ac": 36
  "FATDC-LOGIC-04h": 36
  "ST-06": 38
  "FATDC-LOGIC-07a": 38
coverage:
  web: automated
---

# Edit: Kapitalisasi Class Code, Edit No-Op, Class Code Sendiri Bukan Duplikat, dan Versi Baru Class Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk class berkunci), kendali jam sistem, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- State global yang diubah: jam server dan jam browser diatur bersama ke `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta) untuk blok TC-FA-TDC-218; dipulihkan dengan langkah eksplisit (langkah 41) dan di hook `after` sebagai cadangan.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |
| `khsLck` | `KHS-LCK` | Non-building, Useful Life `10`, Straight Line dan Declining Balance, Active, Used By 0, Last Posted Tax Year `2026` (Class Code terkunci) |

- Blok berjalan berurutan pada class `KHS-E1` yang sama: Class Name dan Class Code berubah antar blok (dipakai sebagai precondition, perubahan tiap blok dijelaskan di Notes).
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal dan jam sistem diubah (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-194: Class Name hanya kapitalisasi dan spasi tepi adalah Edit No-Op

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`
3. Ganti Class Name dari `Kelompok edit uji` menjadi `KELOMPOK EDIT UJI ` (huruf kapital semua dan satu spasi di akhir)
4. Klik `[Save]`
5. Verifikasi muncul toast info: `No changes to save.`
6. Verifikasi Drawer tertutup normal
7. Verifikasi baris `KHS-E1` menampilkan Class Name `Kelompok edit uji`

### TC-FA-TDC-195: Edit No-Op, Save tanpa perubahan nilai

8. Klik link Class Code `KHS-E1`
9. Klik `[Save]` tanpa mengubah field apa pun
10. Verifikasi muncul toast info: `No changes to save.`
11. Verifikasi tidak ada toast sukses
12. Verifikasi Drawer tertutup normal
13. Verifikasi tidak ada error duplikat terhadap Class Code sendiri
14. Verifikasi dialog Save Changes (D-09) tidak muncul

### TC-FA-TDC-196: Class Code sendiri tidak dianggap duplikat

15. Klik link Class Code `KHS-E1`
16. Ganti Class Name menjadi `Kelompok edit uji S` tanpa mengubah Class Code `KHS-E1`
17. Klik `[Save]`
18. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
19. Verifikasi caption `Class code already exists` tidak muncul

### TC-FA-TDC-193: Class Code hanya berubah kapitalisasi disimpan

20. Klik link Class Code `KHS-E1`
21. Ganti Class Code dari `KHS-E1` menjadi `Khs-E1`
22. Klik `[Save]`
23. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
24. Verifikasi caption `Class code already exists` tidak muncul
25. Ganti isi kotak search dengan `Khs-E1`, tekan Enter
26. Verifikasi baris tabel menampilkan Class Code `Khs-E1`

### TC-FA-TDC-218: Class Code terkunci tetap membentuk versi baru

27. Atur jam server dan jam browser ke `15 Okt 2026 10:00 WIB`
28. Ganti isi kotak search dengan `KHS-LCK`, tekan Enter
29. Klik link Class Code `KHS-LCK`
30. Ganti Useful Life dari `10` menjadi `12`
31. Klik `[Save]`
32. Pilih Effective From `Jan 2027` pada dialog Save Changes (D-09), lalu klik `[Apply]`
33. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
34. Klik link Class Code `KHS-LCK`
35. Klik tautan `View versions`
36. Verifikasi modal Versions memuat versi Scheduled dengan Effective From `Jan 2027`
37. Tutup modal Versions
38. Verifikasi Class Code tetap Disabled dengan ikon gembok
39. Klik ikon ✕
40. Ganti isi kotak search dengan `KHS-LCK`, tekan Enter
41. Pulihkan jam server dan jam browser ke waktu semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 25, 28, dan 40 Search agar baris target ada di halaman teramati (R-16, 8b.13); langkah 27 dan 41 mengatur dan memulihkan jam; langkah 37 dan 39 menutup modal Versions dan Drawer yang bersih. Langkah 40 membuat kotak Search menyaring `KHS-LCK` lagi sebelum jam dipulihkan.
- Urutan TC: TC-FA-TDC-194 dan TC-FA-TDC-195 (Edit No-Op) lebih dulu, lalu TC-FA-TDC-196, TC-FA-TDC-193 (Class Code berubah), dan terakhir TC-FA-TDC-218 (butuh jam sistem) (S-10). Langkah 16 mengubah Class Name dari `Kelompok edit uji` menjadi `Kelompok edit uji S`; langkah 21 mengubah Class Code dari `KHS-E1` menjadi `Khs-E1`, sehingga Search `KHS-E1` dari langkah 1 masih menampilkan baris target sampai langkah 20.
- Langkah 19 dan 24 (caption tidak muncul): toast sukses langkah 18 dan 23 menjadi anchor positif bahwa respons server sudah diproses; Drawer sudah tertutup sehingga asersi memastikan tidak ada error duplikat yang menahan Save (8b.2). Langkah 11, 13, dan 14 memakai toast info langkah 10 sebagai anchor.
- Langkah 32 menyebut dialog `Save Changes (D-09)` seperti penyebutan dialog itu pada TC lain; label tombol `[Apply]` mengikuti TC.
- Langkah 34 sampai 38 adalah observasi tambahan agar Expected b TC-FA-TDC-218 ("versi Scheduled `Jan 2027` terbentuk; Class Code tetap Disabled dengan ikon gembok") dapat diasersi; TC tidak memberi langkah observasinya (S-03, S-15).
- Alasan spec melewati sekitar 35 langkah: seluruh blok adalah Edit langsung satu class (`KHS-E1`, lalu `KHS-LCK`) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah langkah dibentuk `Verifikasi` per klausa (S-01) dan langkah pembuka berulang per blok.
- Edit No-Op (TC-FA-TDC-194, TC-FA-TDC-195): ketiadaan entri log dan versi baru adalah Post Condition tanpa langkah observasi di TC; tidak diasersi di spec ini. Anchor positif dan asersi absence log ada di spec pencatatan log (kelas g).
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-*` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-194 Post Condition a dan b, TC-FA-TDC-195 Post Condition a dan b, TC-FA-TDC-193 Post Condition (entri log L-02), dan TC-FA-TDC-196 tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini (S-01, S-05).
  - TC-FA-TDC-193 dan TC-FA-TDC-196 mempunyai precondition class `KHS-E1` asli; spec menjalankannya berurutan setelah blok lain pada class yang sama; asersi masing-masing TC tidak terpengaruh.
  - TC-FA-TDC-218 langkah 3 menyebut `[Apply]` tanpa menyebut dialog; spec menyebutnya dialog Save Changes (D-09) berdasarkan nama dialog di TC lain.
