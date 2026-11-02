---
id: TC-GS-IMPORT-E2E-136-banner-hasil-commit-dapat-ditutup-tampil-tanpa-unsaved-banner-dan-batas
title: "Banner Hasil Commit: dapat ditutup, tampil tanpa Unsaved Banner, dan batas usia 23 jam 59 menit dan tepat 24 jam"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-360
  - TC-GS-IMPORT-573
  - TC-GS-IMPORT-824
coverage:
  web: automated
---

# Banner Hasil Commit: dapat ditutup, tampil tanpa Unsaved Banner, dan batas usia 23 jam 59 menit dan tepat 24 jam

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Akun kedua untuk ganti akun di TC-GS-IMPORT-824: Import data (Read Only) Client E (Indra Gunawan) `importRead_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_IMPORTRO_PASSWORD`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand (Client E).
- Data Dinamis (berkas dan draft disiapkan lewat fixture, `Fixture.import.commitBanner136`, fixture baru; nama literal dari Data Dinamis karena asersi bergantung pada nama dan jumlah): D-58 (brand-partial-15.csv: 15 baris, 10 `pending`, 3 `duplicate`, 2 `error`) untuk TC-360; D-50 (brand-12.csv: 12 baris `pending`) untuk TC-573 dan TC-824; D-76 varian 1 (umur draft 25 jam) untuk TC-360.
- Kemampuan teknis (disediakan tim FE/BE): skrip reset Client E sesuai D-47 (hapus Brand hasil commit, draft, hasil commit terakhir, dan penanda Banner Hasil Commit); hook umur draft D-76; fixture waktu commit selesai hasil commit terakhir (NC-08) yang mengatur waktu relatif terhadap waktu server.
- State global: waktu commit selesai hasil commit terakhir Client E diatur lewat fixture; dipulihkan oleh reset D-47 di hook `after`. Suite Import berjalan serial (`parallel: false`) karena Client E dipakai bersama spec commit lain.
- Margin waktu (bagian 8b butir 3): TC-GS-IMPORT-824 mengatur waktu commit selesai relatif terhadap waktu server saat fixture dijalankan (langkah 36), dan jam bergerak maju selama sesi berjalan. Usia 23 jam 59 menit berjarak 1 menit (60 detik) dari batas 24 jam; pembacaan Staging Table dan banner dilakukan lewat muat ulang segera (langkah 37, kurang dari 30 detik sesudah langkah 36, D-76 varian 2). Margin = 60 detik - kurang dari 30 detik = lebih dari 30 detik. Ganti akun dan buka Import > Brand (langkah 34 sampai 35) dilakukan sebelum pengaturan waktu sehingga tidak memakan margin.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 dan pulihkan sesi ke akun default.

## Test Steps

### TC-GS-IMPORT-360: Banner Hasil Commit dapat ditutup dan tidak persisten

1. Reset Client E ke tanpa draft (D-47), siapkan draft Brand D-58 lewat fixture, atur umur draft 25 jam (D-76 varian 1), lalu muat ulang halaman Import > Brand
2. Klik [Import (10)]
3. Tunggu aksi selesai (permintaan mendapat respons)
4. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
5. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 2 errors remain." tampil
6. Verifikasi Banner Hasil Commit tampil di atas Unsaved Banner
7. Klik `[×]` pada Banner Hasil Commit
8. Verifikasi Banner Hasil Commit hilang
9. Muat ulang halaman
10. Verifikasi Staging Table menampilkan baris `error` sisa commit
11. Verifikasi Banner Hasil Commit tidak tampil lagi
12. Klik Sub-Tab Measurement
13. Klik Sub-Tab Brand
14. Verifikasi Staging Table Sub-Tab Brand tampil
15. Verifikasi Banner Hasil Commit tidak tampil di Sub-Tab Brand

### TC-GS-IMPORT-573: Banner Hasil Commit tampil pada state belum ada draft setelah commit tuntas tanpa Unsaved Banner

16. Reset Client E ke tanpa draft (D-47), siapkan draft Brand D-50 lewat fixture, lalu muat ulang halaman Import > Brand
17. Klik [Import (12)]
18. Tunggu aksi selesai (permintaan mendapat respons)
19. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
20. Verifikasi Dropzone tampil
21. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil di atas halaman
22. Verifikasi Unsaved Banner tidak tampil
23. Klik `[×]` pada banner
24. Verifikasi banner hilang
25. Muat ulang halaman
26. Verifikasi Dropzone tampil
27. Verifikasi banner tidak muncul lagi bagi administrator yang sama

### TC-GS-IMPORT-824: Banner Hasil Commit tampil pada usia 23 jam 59 menit dan tidak tampil pada usia tepat 24 jam

28. Reset Client E ke tanpa draft (D-47), siapkan draft Brand D-50 lewat fixture, lalu muat ulang halaman Import > Brand
29. Total Control Client E: klik [Import (12)]
30. Total Control Client E: Tunggu aksi selesai (permintaan mendapat respons)
31. Total Control Client E: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
32. Verifikasi Dropzone tampil bagi Total Control Client E
33. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil bagi Total Control Client E
34. Ganti akun: Logout, lalu login sebagai Import data (Read Only) Client E dengan `Spectra.env.GS_CLIENTE_IMPORTRO_PASSWORD`
35. Buka Global Settings > Import > Brand
36. Atur waktu commit selesai hasil commit terakhir Brand Client E menjadi 23 jam 59 menit sebelum waktu server saat ini (fixture waktu commit selesai)
37. Muat ulang halaman Import > Brand segera (kurang dari 30 detik sesudah langkah 36)
38. Verifikasi Dropzone tampil bagi Import data (Read Only) Client E
39. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil bagi Import data (Read Only) Client E
40. Atur waktu commit selesai hasil commit terakhir Brand Client E menjadi tepat 24 jam sebelum waktu server saat ini (fixture waktu commit selesai)
41. Muat ulang halaman Import > Brand
42. Verifikasi Dropzone tampil bagi Import data (Read Only) Client E
43. Verifikasi Banner Hasil Commit tidak tampil bagi Import data (Read Only) Client E

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (360, 573, 824) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 16, dan 28 (reset Client E dan penyiapan draft lewat fixture, karena tiap TC mensyaratkan Client E direset sebelum TC); langkah 3, 4, 18, 19, 30, dan 31 (menunggu aksi selesai sesudah klik [Import (N)] dan menunggu commit selesai); langkah 12 dan 13 (pindah Sub-Tab untuk TC-360); langkah 36 dan 40 (pengaturan waktu commit selesai), langkah 34 sampai 35 (ganti akun dan buka layar), dan langkah 37 (muat ulang segera sesudah pengaturan waktu, D-76 varian 2).
- Anchor positif untuk absence banner: langkah 10 (Staging Table baris `error` tampil sebelum asersi langkah 11), langkah 14 (Staging Table Sub-Tab Brand tampil sebelum langkah 15), langkah 26 (Dropzone sebelum langkah 27), dan langkah 42 (Dropzone sebelum langkah 43). Langkah 22 (Unsaved Banner tidak tampil) didahului langkah 20 dan 21.
- Spec melewati sekitar 35 langkah (43 langkah, dihitung tanpa ekspansi). Alasan: tiga blok TC berdiri sendiri, masing-masing mereset Client E; kegagalan satu blok tidak membuat blok lain kehilangan makna; ketiganya satu objek uji (Banner Hasil Commit) dan satu akun kecuali ganti akun eksplisit di blok terakhir (langkah 34) yang tetap bermakna walau blok sebelumnya gagal.
- Aktor kedua: Import data (Read Only) Client E dipakai sebagai pengamat lewat UI dengan Step ganti akun eksplisit (langkah 34), bukan pemicu; tidak butuh butir P-2.
- Temuan untuk QA:
  - TC-GS-IMPORT-824: batas usia banner (23 jam 59 menit dan tepat 24 jam) tidak merujuk D-76 maupun hook jam di Precondition; spec memakai fixture waktu commit selesai (NC-08) yang disebut di Precondition TC d. Nilai "23 jam 59 menit sebelum waktu server saat ini" bergeser tiap detik sejak fixture dijalankan; margin 1 menit (60 detik) antara langkah 36 dan batas 24 jam cukup karena langkah 37 memuat ulang kurang dari 30 detik sesudahnya (D-76 varian 2), tetapi acuan T0 dari waktu commit selesai sebenarnya (dibaca lewat API seeding) tidak dinyatakan TC (bagian 8b butir 3).
  - TC-GS-IMPORT-360 dan TC-GS-IMPORT-573: Post Condition tidak punya langkah observasi di TC (draft Brand berisi 2 baris `error` dan penanda Banner Hasil Commit sudah ditampilkan; 12 record Brand baru di Master Reference > Brand) sehingga tidak diasersi sebagai butir tersendiri. Langkah 10 (baris `error` tampil) dan langkah 20 serta 26 (Dropzone) hanya menjadi anchor.
  - TC-GS-IMPORT-824: Post Condition c (hasil commit Client E direset) dipenuhi lewat reset D-47 di hook `after`, tanpa asersi.
  - Data Dinamis commit (nama Brand literal `Acme Corp`, `Lenovo`, dan seterusnya) tidak bersuffix per run karena asersi bergantung pada nama; pengecualian S-12 untuk data ini belum dinyatakan di konvensi, dipertahankan dengan reset D-47 dan suite serial.
