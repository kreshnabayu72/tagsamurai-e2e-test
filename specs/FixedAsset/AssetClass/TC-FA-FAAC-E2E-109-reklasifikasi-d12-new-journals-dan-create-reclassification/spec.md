---
id: TC-FA-FAAC-E2E-109-reklasifikasi-d12-new-journals-dan-create-reclassification
title: "Reklasifikasi D-12: Pilihan New Journals Only, Create Reclassification, dan Urutan D-11 Lalu D-12"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-345
  - TC-FA-FAAC-346
  - TC-FA-FAAC-350
coverage:
  web: automated
---

# Reklasifikasi D-12: Pilihan New Journals Only, Create Reclassification, dan Urutan D-11 Lalu D-12

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nilai literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-EXP` dengan Last Exported Period Aug 2026, akun lengkap, dan tanpa versi Scheduled: Asset Cost `11001 – Machinery Cost`, Accumulated Depreciation `12001 – Accumulated Depreciation Machinery`; Asset Class `B-EXPA` dipakai aset dan Last Exported Period terisi (seed Pre-setup sesuai NC-16). Akun pengganti `11002 – Machinery Cost Alt` tersedia di dropdown.
- Jam: bulan berjalan mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser sinkron dan tidak digeser spec ini. Nilai Useful Life baru yang diketik pada TC-350 adalah 48.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): membaca nilai tersimpan Useful Life dan akun `B-EXPA` serta ada tidaknya permintaan jurnal reklasifikasi ke Export Journal (Export Journal belum disusun, OI-06 TC) lewat fixture BE.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Asset Cost `B-EXP` kembali `11001 – Machinery Cost`. Pemulihan dilakukan juga sebagai langkah penghubung di antara TC-345 dan TC-346 (kedua TC mulai dari akun `11001`).
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nomor akun itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-345: Pilih New journals only pada D-12

1. Ketik Search `B-EXP`, tekan Enter
2. Klik link Class Code `B-EXP` di tabel
3. Klik tab `Accounts`
4. Ganti Asset Cost menjadi `11002 – Machinery Cost Alt`
5. Klik `Save`
6. Klik `New journals only`
7. Verifikasi halaman kembali ke tabel Asset Class (tidak ada versi Scheduled)
8. Verifikasi toast sukses `Success, asset class has been updated.` tampil di tabel
9. Buka Detail `B-EXP` dan klik tab `Accounts`
10. Verifikasi Asset Cost berubah menjadi `11002`
11. Verifikasi tidak ada permintaan jurnal reklasifikasi (dibaca lewat fixture BE)
12. Klik breadcrumb `Asset Class`
13. Pulihkan Asset Cost `B-EXP` ke `11001 – Machinery Cost` lewat fixture BE hingga tersimpan

### TC-FA-FAAC-346: Pilih Create reclassification pada D-12

14. Muat ulang halaman tabel Asset Class
15. Klik link Class Code `B-EXP` di tabel
16. Klik tab `Accounts`
17. Ganti Asset Cost menjadi `11002 – Machinery Cost Alt`
18. Klik `Save`
19. Klik `Create reclassification`
20. Verifikasi halaman kembali ke tabel Asset Class (tidak ada versi Scheduled)
21. Verifikasi toast sukses `Success, asset class has been updated.` tampil di tabel
22. Buka Detail `B-EXP` dan klik tab `Accounts`
23. Verifikasi Asset Cost berubah menjadi `11002`
24. Verifikasi penyimpanan berhasil tanpa dialog tambahan (permintaan jurnal reklasifikasi diteruskan ke Export Journal)
25. Klik breadcrumb `Asset Class`

### TC-FA-FAAC-350: Save yang memuat perubahan estimasi dan akun menampilkan D-11 lebih dulu lalu D-12

26. Ganti isi kotak search dengan `B-EXPA`, tekan Enter
27. Klik link Class Code `B-EXPA` di tabel
28. Klik tab `Depreciation` dan ubah Useful Life menjadi 48
29. Klik tab `Accounts` dan ganti Asset Cost menjadi `11002 – Machinery Cost Alt`
30. Klik `Save`
31. Verifikasi Dialog `Apply Changes` tampil lebih dulu
32. Klik `Apply`
33. Verifikasi Dialog `Reclassify Balances` tampil sesudah `Apply`
34. Klik `Cancel` pada dialog `Reclassify Balances`
35. Verifikasi belum ada data tersimpan: Useful Life dan Asset Cost tersimpan `B-EXPA` tidak berubah (dibaca lewat fixture BE)
36. Klik breadcrumb `Asset Class`
37. Verifikasi dialog `Unsaved Changes` tampil
38. Klik `[Leave]`
39. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: dua pilihan D-12 yang menyimpan akun (TC-345 lalu TC-346 setelah pemulihan akun) dan TC-350 yang berakhir dengan Cancel di akhir.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan 26 (Search untuk menemukan baris target, R-16), langkah 9 dan 22 (membuka Detail kembali untuk membaca akun di server), langkah 12 dan 25 (kembali ke tabel), langkah 13 dan 14 (memulihkan Asset Cost lewat fixture BE agar TC-346 mulai dari akun `11001`), langkah 36 sampai 38 (menutup form terisi lewat breadcrumb `Asset Class`, `Unsaved Changes`, dan `[Leave]`, S-08 dan S-09), dan langkah 39 (mengosongkan Search).
3. Alasan melebihi sekitar 35 langkah (39 langkah): spec berisi tiga blok TC pada dialog D-12 yang berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna dan tiap blok memulai dari akun yang dipulihkan fixture BE.
4. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan nomor akun tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
5. Temuan untuk QA: Expected TC-345 b ("tidak ada permintaan jurnal reklasifikasi") dan TC-346 b ("diteruskan ke Export Journal") tidak punya cara observasi di UI Asset Class; TC-346 sendiri membatasi pengamatan pada penyimpanan berhasil tanpa dialog tambahan, dan TC-345 diasersi lewat kemampuan baca BE yang disediakan tim FE/BE. TC-350 Expected c ("belum ada data tersimpan sampai kedua dialog diselesaikan") diasersi sesudah Cancel dengan pembacaan BE.
