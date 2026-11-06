---
id: TC-FA-FAAC-E2E-103-versi-scheduled-alert-dan-save-no-op
title: "Versi Scheduled: Alert Next Version, Save No-Op, dan Validasi Effective From Perubahan Lanjutan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-321
  - TC-FA-FAAC-322
  - TC-FA-FAAC-323
  - TC-FA-FAAC-324
  - TC-FA-FAAC-325
coverage:
  web: automated
---

# Versi Scheduled: Alert Next Version, Save No-Op, dan Validasi Effective From Perubahan Lanjutan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-SCHED` "Scheduled Fixture" dipakai aset dengan satu versi Scheduled sejak M+2 yang nilai Useful Life-nya berbeda dari nilai berlaku saat ini; Asset Class `B-SCHED2` dengan dua versi Scheduled M+2 dan M+4; Asset Class `B-ANCHOR` tanpa versi Scheduled. Spec ini hanya membaca dan membatalkan perubahan, tidak mengubah data.
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser sinkron dan tidak digeser spec ini. Bulan pada Alert dan caption ditulis MMM YYYY.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan versi itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-323: Alert versi Scheduled tampil di atas bar tab pada semua tab dan tidak dapat ditutup

1. Ketik Search `B-SCHED`, tekan Enter
2. Klik link Class Code `B-SCHED` di tabel
3. Klik tab `General`
4. Verifikasi Alert info `Next version starts [MMM YYYY].` dengan bulan = Effective From versi Scheduled (M+2) tampil di bawah header dan di atas bar tab
5. Klik tab `Depreciation`
6. Verifikasi Alert yang sama tampil di bawah header dan di atas bar tab
7. Klik tab `Accounts`
8. Verifikasi Alert yang sama tampil di bawah header dan di atas bar tab
9. Klik tab `Asset Names`
10. Verifikasi Alert yang sama tampil di bawah header dan di atas bar tab
11. Verifikasi Alert tidak memiliki tombol tutup

### TC-FA-FAAC-322: Save tanpa perubahan atas Asset Class dengan versi Scheduled adalah No-Op terhadap versi terakhir

12. Klik tab `Depreciation`
13. Verifikasi form terisi nilai versi Scheduled (versi terakhir)
14. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
15. Klik `Save` tanpa mengubah apa pun
16. Verifikasi toast info `No changes to save.`
17. Verifikasi tidak ada dialog `Apply Changes`
18. Verifikasi halaman kembali ke tabel Asset Class (Save tanpa perubahan adalah No-Op)
19. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
20. Klik link Class Code `B-SCHED` di tabel
21. Klik tab `Depreciation`

### TC-FA-FAAC-321: Perubahan lanjutan setelah versi Scheduled membentuk versi baru yang tunduk V-25

22. Verifikasi form Depreciation terisi dari versi terakhir (termasuk versi Scheduled)
23. Ubah Useful Life dari nilai versi Scheduled menjadi 36
24. Klik `Save`
25. Pilih Effective From bulan berjalan (lebih awal dari versi Scheduled)
26. Verifikasi caption `Effective from must not be earlier than [MMM YYYY]` dengan bulan = Effective From versi Scheduled (M+2)
27. Klik `Apply`
28. Verifikasi `Apply` tidak menyimpan (dialog `Apply Changes` tetap terbuka)
29. Klik `Cancel`
30. Klik breadcrumb `Asset Class`
31. Verifikasi dialog `Unsaved Changes` tampil
32. Klik `[Leave]`

### TC-FA-FAAC-324: Dengan beberapa versi Scheduled Alert memakai Effective From paling awal

33. Ganti isi kotak search dengan `B-SCHED2`, tekan Enter
34. Klik link Class Code `B-SCHED2` di tabel
35. Verifikasi Alert `Next version starts [MMM YYYY].` dengan bulan Effective From paling awal (M+2), bukan yang M+4
36. Klik breadcrumb `Asset Class`

### TC-FA-FAAC-325: Alert versi Scheduled tidak tampil pada mode Create dan pada Asset Class tanpa versi Scheduled

37. Ganti isi kotak search dengan `B-ANCHOR`, tekan Enter
38. Klik link Class Code `B-ANCHOR` di tabel
39. Verifikasi bar tab Detail `B-ANCHOR` tampil
40. Verifikasi tidak ada Alert di Detail `B-ANCHOR` (tanpa versi Scheduled)
41. Klik breadcrumb `Asset Class`
42. Klik `+ Asset Class`
43. Verifikasi bar tab Detail mode Create tampil
44. Verifikasi tidak ada Alert di Detail mode Create
45. Klik breadcrumb `Asset Class`
46. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: screening Alert (TC-323), Save tanpa perubahan (TC-322), dan validasi Effective From yang ditolak (TC-321) pada Detail `B-SCHED` yang sama, dibuka di langkah 2 dan dibuka ulang di langkah 20 dan 21 (Save tanpa perubahan mengembalikan halaman ke tabel, TC-322 c); lalu Alert pada `B-SCHED2` (TC-324) dan tanpa Alert (TC-325).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 33, dan 37 (Search untuk menemukan baris target, R-16), langkah 3, 5, 7, 9, 12, dan 21 (pindah tab sebagai bagian dari langkah TC), langkah 14 (baseline Changelog, S-12), langkah 20 dan 21 (membuka Detail `B-SCHED` kembali sesudah Save No-Op; hasil Search `B-SCHED` diasumsikan dipertahankan di tabel), langkah 29 (menutup dialog), langkah 36, 41, dan 45 (kembali ke tabel), dan langkah 46 (mengosongkan Search). Langkah 30 sampai 32 menutup form yang masih terisi lewat breadcrumb `Asset Class`, `Unsaved Changes`, dan `[Leave]` (S-08, S-09).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan versi Scheduled tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. S-05 dan P-1: Expected "tanpa log" pada TC-322 diasersi di spec ini (langkah 19) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class.
5. Alasan melebihi sekitar 35 langkah (46 langkah): spec berisi lima blok TC yang hanya membaca Detail Asset Class dengan versi Scheduled; setiap blok berdiri sendiri, tidak mengubah data, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
6. Temuan untuk QA: nilai Useful Life versi Scheduled pada TC-322 dan TC-321 tidak disebut di TC (hanya "nilai versi Scheduled"); spec mengasumsikan seed membedakannya dari nilai berlaku saat ini. TC-325 tidak menyebut Expected untuk anchor halaman; langkah 39 dan 43 adalah anchor positif absence (bagian 8b butir 2).
