---
id: TC-FA-FAAC-E2E-096-aksi-form-dan-status-pada-asset-class-dihapus-pengguna-lain
title: "Aksi Duplicate, Save Edit, Delete, Bulk, dan Toggle Status pada Asset Class yang Dihapus Pengguna Lain"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-181
  - TC-FA-FAAC-225
  - TC-FA-FAAC-253
  - TC-FA-FAAC-268
  - TC-FA-FAAC-305
  - TC-FA-FAAC-306
sourceRules: ["T-14", "F-FAAC-02.k14", "F-FAAC-05.k4", "F-FAAC-03.k2", "§7.3#b6"]
smoke: []
dependsOn: []
trace:
  "T-14": [4, 5, 32, 33, 39]
  "F-FAAC-02.k14": [11, 12, 13]
  "F-FAAC-05.k4": [18, 19, 20]
  "F-FAAC-03.k2": [25, 26, 27]
  "§7.3#b6": [32, 33, 34, 39, 40, 41, 42]
anchor: [6]
coverage:
  web: automated
---

# Aksi Duplicate, Save Edit, Delete, Bulk, dan Toggle Status pada Asset Class yang Dihapus Pengguna Lain

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Asset Class (kode literal TC, disediakan tim FE/BE lewat fixture BE): `B-GONE`, `B-GONE2`, `B-GONE3`, `B-GONE4`, `B-GONE5`, dan `B-GONE7` Active tanpa Asset Name dan belum pernah diposting; `B-GONE6` Inactive.
- Pelaku kedua: sesi API aktor (kemampuan suite, lihat suite.md): menghapus Asset Class target lewat fixture BE, bukan sesi UI kedua.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: ketujuh Asset Class `B-GONE*` yang terhapus dibuat ulang.
- Nilai Class Name pengganti untuk TC-181: `Gone Renamed` (nilai uji yang diketik, tidak bentrok dengan seed).
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-GONE`, tekan Enter

### TC-FA-FAAC-268: Duplicate Asset Class sumber yang sudah dihapus user lain

2. Lewat sesi API aktor, hapus `B-GONE5` hingga penghapusan tersimpan (tabel sudah termuat dengan baris `B-GONE5`)
3. Klik ikon `⋯` pada baris `B-GONE5`, lalu pilih `Duplicate`
4. Verifikasi toast info `This asset class is no longer available.`
5. Verifikasi tabel disegarkan tanpa `B-GONE5`
6. Verifikasi halaman Detail tidak dibuka

### TC-FA-FAAC-181: Save Edit atas Asset Class yang sudah dihapus user lain

7. Klik link Class Code `B-GONE` di tabel
8. Lewat sesi API aktor, hapus `B-GONE` hingga penghapusan tersimpan
9. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
10. Ubah Class Name menjadi `Gone Renamed`, lalu klik `Save`
11. Verifikasi toast info `This asset class is no longer available.`
12. Verifikasi halaman kembali ke tabel dan tabel disegarkan tanpa `B-GONE`; tidak ada perubahan data
13. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-225: Delete Asset Class yang sudah dihapus user lain

14. Klik ikon `⋯` pada baris `B-GONE2`, lalu pilih `Delete`
15. Lewat sesi API aktor, hapus `B-GONE2` hingga penghapusan tersimpan
16. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
17. Klik `Delete` pada dialog
18. Verifikasi toast info `This asset class is no longer available.`
19. Verifikasi tabel disegarkan tanpa `B-GONE2`
20. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-305: Activate Asset Class yang sudah dihapus user lain

21. Klik toggle kolom Active pada baris `B-GONE6` (Off)
22. Lewat sesi API aktor, hapus `B-GONE6` hingga penghapusan tersimpan
23. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
24. Klik `Activate` pada dialog
25. Verifikasi toast info `This asset class is no longer available.`
26. Verifikasi tabel disegarkan tanpa `B-GONE6`
27. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-306: Deactivate Asset Class yang sudah dihapus user lain

28. Klik toggle kolom Active pada baris `B-GONE7` (On)
29. Lewat sesi API aktor, hapus `B-GONE7` hingga penghapusan tersimpan
30. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
31. Klik `Deactivate` pada dialog
32. Verifikasi toast info `This asset class is no longer available.`
33. Verifikasi tabel disegarkan tanpa `B-GONE7`
34. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-253: Bulk dengan seluruh Asset Class terpilih sudah dihapus user lain

35. Centang baris `B-GONE3` dan `B-GONE4` di tabel
36. Lewat sesi API aktor, hapus `B-GONE3` dan `B-GONE4` hingga penghapusan tersimpan
37. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
38. Klik Bulk Action `Deactivate`, lalu klik `Deactivate` pada dialog
39. Verifikasi toast info `This asset class is no longer available.`
40. Verifikasi tidak ada toast sukses yang tampil
41. Verifikasi tabel disegarkan tanpa `B-GONE3` dan `B-GONE4`
42. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
43. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: semua TC berakhir dengan penolakan "no longer available" dan menghapus data seed milik spec, sehingga dikelompokkan dalam satu rangkaian yang diawali Duplicate dan diakhiri Bulk dengan dua baris.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16; hasil Search dipertahankan untuk TC berikutnya karena tabel hanya disegarkan), langkah 9, 16, 23, 30, dan 37 (baseline Changelog, S-12), dan langkah 43 (mengosongkan Search). Langkah 2, 8, 15, 22, 29, dan 36 adalah pemicu pelaku kedua lewat sesi API (bukan kelas c; tidak memakai P-2).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal yang dihapus oleh aksi TC; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini). Target adalah baris seed milik spec ini yang dibuat ulang fixture BE.
4. S-05 dan P-1: Expected "tanpa log" pada TC-181, TC-225, TC-305, TC-306, dan TC-253 diasersi di spec ini (langkah 13, 20, 27, 34, dan 42) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class. Baseline dicatat sesudah penghapusan oleh sesi API aktor, sehingga entri Delete milik aktor tidak terhitung.
5. Alasan melebihi sekitar 35 langkah (43 langkah): spec berisi enam blok TC yang berdiri sendiri pada baris seed `B-GONE*` berbeda dan satu topik aksi (aksi atas Asset Class yang dihapus pengguna lain); tiap blok memakai seed sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna dan pemecahan hanya menggandakan Search awal.
6. Temuan untuk QA: TC-268 mensyaratkan `B-GONE5` dihapus sebelum klik tetapi tidak menyebut pelaku dan caranya; TC-181 tidak menyebut keadaan kotak Search sesudah halaman kembali ke tabel, sehingga langkah Search berikutnya dihilangkan dan hasil Search diasumsikan dipertahankan. Spec mengikuti TC.
