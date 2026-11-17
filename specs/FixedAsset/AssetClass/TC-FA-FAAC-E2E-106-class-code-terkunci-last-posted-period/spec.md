---
id: TC-FA-FAAC-E2E-106-class-code-terkunci-last-posted-period
title: "Class Code Terkunci oleh Last Posted Period: Tooltip, Kunci Berubah Setelah Halaman Dibuka, dan Edit Class Name"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-336
  - TC-FA-FAAC-337
  - TC-FA-FAAC-338
  - TC-FA-FAAC-339
sourceRules: ["ST-07", "§4.3#r21", "§4.1.2#r4", "D-19", "F-FAAC-02.k1", "§7.2#b1", "T-02", "FAAC-LOGIC-10b", "FAAC-LOGIC-10a"]
smoke: []
dependsOn: []
trace:
  "ST-07": [3, 17]
  "§4.3#r21": [5, 17]
  "§4.1.2#r4": 6
  "D-19": 13
  "F-FAAC-02.k1": 15
  "§7.2#b1": 15
  "T-02": [24, 30]
  "FAAC-LOGIC-10b": [25, 31]
  "FAAC-LOGIC-10a": 32
coverage:
  web: automated
---

# Class Code Terkunci oleh Last Posted Period: Tooltip, Kunci Berubah Setelah Halaman Dibuka, dan Edit Class Name

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-LOCK` dengan Last Posted Period Mar 2026 dan belum punya Last Exported Period (seed Pre-setup sesuai NC-16); `B-LOCKR` "Lock Race Fixture" belum pernah diposting; `B-LOCKR2` belum pernah diposting.
- Pelaku kedua: sesi API aktor (kemampuan suite, lihat suite.md): mengisi Last Posted Period Mar 2026 pada `B-LOCKR` dan `B-LOCKR2` lewat fixture BE, bukan sesi UI kedua.
- Nilai uji yang diketik: Class Code `B-LOCKR9` (TC-338), Class Name `Lock Race Renamed` (TC-339), dan Class Name `Locked Renamed` (TC-337).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Last Posted Period `B-LOCKR` dan `B-LOCKR2` dikosongkan kembali, Class Name `B-LOCKR2` dan `B-LOCK` kembali ke nilai seed.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan periode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-336: Class Code Disabled dengan tooltip bila Last Posted Period terisi

1. Ketik Search `B-LOCK`, tekan Enter
2. Klik link Class Code `B-LOCK` di tabel
3. Verifikasi field Class Code Disabled
4. Arahkan kursor ke field Class Code
5. Verifikasi tooltip `Class code can't be changed because this asset class was used in depreciation for Mar 2026.`
6. Verifikasi Last Posted Period menampilkan `Mar 2026`
7. Klik breadcrumb `Asset Class`

### TC-FA-FAAC-338: Kunci Class Code berubah setelah halaman dibuka dan Save mengubah Class Code

8. Ganti isi kotak search dengan `B-LOCKR`, tekan Enter
9. Klik link Class Code `B-LOCKR` di tabel
10. Ubah Class Code menjadi `B-LOCKR9` (`B-LOCKR` belum terkunci)
11. Lewat sesi API aktor, isi Last Posted Period Mar 2026 untuk `B-LOCKR` hingga nilainya tersimpan
12. Klik `Save`
13. Verifikasi Save ditolak server dengan Dialog Blok `Cannot Save Asset Class` berisi `• B-LOCKR – Lock Race Fixture` dan `The class code has been locked by another action. The page has been reloaded with the latest lock status.` dengan tombol `OK`
14. Klik `OK`
15. Verifikasi tidak ada yang tersimpan: Class Code pada halaman yang dimuat ulang tetap `B-LOCKR`
16. Arahkan kursor ke field Class Code
17. Verifikasi field Class Code Disabled dengan tooltip kunci `Class code can't be changed because this asset class was used in depreciation for Mar 2026.`
18. Klik breadcrumb `Asset Class`

### TC-FA-FAAC-339: Kunci berubah setelah halaman dibuka tetapi Save tidak mengubah Class Code

19. Ganti isi kotak search dengan `B-LOCKR2`, tekan Enter
20. Klik link Class Code `B-LOCKR2` di tabel
21. Ubah Class Name saja menjadi `Lock Race Renamed` (`B-LOCKR2` belum terkunci)
22. Lewat sesi API aktor, isi Last Posted Period Mar 2026 untuk `B-LOCKR2` hingga nilainya tersimpan
23. Klik `Save`
24. Verifikasi toast sukses `Success, asset class has been updated.`
25. Verifikasi tidak ada Dialog D-19 `Cannot Save Asset Class`

### TC-FA-FAAC-337: Class Name dan Description tetap dapat diubah saat Class Code terkunci

26. Ganti isi kotak search dengan `B-LOCK`, tekan Enter
27. Klik link Class Code `B-LOCK` di tabel
28. Ubah Class Name menjadi `Locked Renamed`
29. Klik `Save`
30. Verifikasi toast sukses `Success, asset class has been updated.`
31. Verifikasi Class Name berubah menjadi `Locked Renamed`
32. Verifikasi Class Code tetap `B-LOCK`
33. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: screening kunci (TC-336) lebih dulu, lalu kasus kunci berubah (TC-338 ditolak, TC-339 berhasil), dan TC-337 yang menyimpan Class Name `B-LOCK` di akhir.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 8, 19, dan 26 (Search untuk menemukan baris target, R-16), langkah 7 dan 18 (kembali ke tabel), dan langkah 33 (mengosongkan Search). Langkah 11 dan 22 adalah pemicu pelaku kedua lewat sesi API (bukan kelas c; tidak memakai P-2). Langkah 4 dan 16 (hover) mendahului asersi tooltip (bagian 8b butir 5).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan Last Posted Period tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Temuan untuk QA: TC-337 dan TC-339 tidak menyebut keadaan halaman setelah Save berhasil (tabel atau Detail), sehingga asersi memakai nilai Class Name dan Class Code tanpa menyebut lokasi. TC-338 menyebut Class Code `B-LOCKR9` dan TC-339 tidak menyebut nilai Class Name baru; spec memakai nilai uji yang diketik pada Prerequisites. Teks tooltip kunci pada TC-338 Expected c mengikuti Expected TC-336 (TC-338 hanya menyebut "tooltip kunci").
