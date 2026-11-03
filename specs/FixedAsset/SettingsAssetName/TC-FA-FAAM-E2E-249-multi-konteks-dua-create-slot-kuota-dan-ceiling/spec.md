---
id: TC-FA-FAAM-E2E-249-multi-konteks-dua-create-slot-kuota-dan-ceiling
title: "Multi-Konteks: Dua Create Bersamaan pada Slot Kuota Terakhir dan Slot Ceiling Terakhir"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-635
  - TC-FA-FAAM-636
coverage:
  web: automated
---

# Multi-Konteks: Dua Create Bersamaan pada Slot Kuota Terakhir dan Slot Ceiling Terakhir

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor sesi A TC-FA-FAAM-635: Total Control pada client Starter `AutoStarter9b` (Tabel Data Uji Pre-setup No. 16f, plan Starter, 9 Asset Name, kuota 10, dua sesi); email tidak tertulis di Pre-setup TC dan disediakan tim FE, `Spectra.env.FA_STARTER9B_TC_PASSWORD` (nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor sesi A TC-FA-FAAM-636: Total Control pada client dengan katalog satu di bawah ceiling Master Data Count Limit (Pre-setup No. 19i, dua sesi; client khusus TC ini); email disediakan tim FE, `Spectra.env.FA_CEILING_TC_PASSWORD` (nama baru, didaftarkan oleh pemilik repo). Login dilakukan lewat langkah ganti client eksplisit (langkah 15).
- Sesi B adalah konteks UI kedua dengan akun yang sama pada client yang sama; sesi B menjadi objek asersi. Akun harus mengizinkan dua sesi web paralel (kemampuan disediakan tim FE/BE). Password tidak ditulis di spec atau fixture.
- Env var: `FA_STARTER9B_TC_PASSWORD`, `FA_CEILING_TC_PASSWORD`.
- Data Pre-setup (client dedicated, nama literal karena client dipakai satu TC saja): No. 16f (9 Asset Name, kuota Starter 10) dan No. 19i (katalog Asset Name satu di bawah ceiling).
- Data Dinamis (dibuat lewat UI, nama bersuffix `{runId}-249`): `Quota Race A {runId}-249` dan `Quota Race B {runId}-249` (TC-FA-FAAM-635); `Ceiling Race A {runId}-249` dan `Ceiling Race B {runId}-249` (TC-FA-FAAM-636). Field wajib lain: Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`; TC tidak menyebut nilai ini (lihat Temuan untuk QA).
- Kemampuan teknis: dua konteks UI paralel untuk akun yang sama; submit berurutan tanpa jeda dari dua sesi; Master Data Count Limit diturunkan ke minimum lewat seed API pada client No. 19i (disediakan tim BE/FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tutup konteks UI kedua, hapus Asset Name bersuffix `-249` lewat API, dan pulihkan Master Data Count Limit serta jumlah Asset Name client No. 16f dan 19i ke keadaan awal.
- State global yang diubah: Master Data Count Limit client No. 19i (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-635 dan 636: login sebagai Total Control pada client yang bersangkutan dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-635: Dua Create bersamaan pada slot kuota terakhir

1. Sesi B: buka konteks UI kedua, login sebagai Total Control pada client Starter `AutoStarter9b`, dan buka Fixed Asset > Settings > Asset Master > Asset Name
2. Sesi A: klik `[+ Asset Name]`
3. Sesi A: isi Asset Name `Quota Race A {runId}-249` dengan field wajib lain
4. Sesi B: klik `[+ Asset Name]`
5. Sesi B: isi Asset Name `Quota Race B {runId}-249` dengan field wajib lain
6. Sesi A: klik `[Submit]`
7. Sesi B: klik `[Submit]` tanpa jeda
8. Verifikasi satu sesi (A) sukses dan jumlah Asset Name client menjadi 10
9. Verifikasi sesi B mendapat dialog kuota `Asset Name Limit Reached`
10. Sesi B: klik `[OK]` pada dialog kuota
11. Sesi B: klik `✕` pada Modal Create
12. Verifikasi dialog `Unsaved Changes` di sesi B
13. Sesi B: klik `[Leave]`
14. Tutup konteks UI kedua dan hapus sesi login browser terkait

### TC-FA-FAAM-636: Dua Create bersamaan pada slot ceiling terakhir

15. Sesi A: logout lalu login sebagai Total Control pada client katalog satu di bawah ceiling (Pre-setup No. 19i)
16. Sesi B: buka konteks UI kedua, login sebagai Total Control pada client yang sama, dan buka Fixed Asset > Settings > Asset Master > Asset Name
17. Sesi A: buka Fixed Asset > Settings > Asset Master > Asset Name
18. Sesi A: klik `[+ Asset Name]`
19. Sesi A: isi Asset Name `Ceiling Race A {runId}-249` dengan field wajib lain
20. Sesi B: klik `[+ Asset Name]`
21. Sesi B: isi Asset Name `Ceiling Race B {runId}-249` dengan field wajib lain
22. Sesi A: klik `[Submit]`
23. Sesi B: klik `[Submit]` tanpa jeda
24. Verifikasi satu sesi (A) sukses
25. Verifikasi sesi B mendapat dialog D-07
26. Sesi B: klik tombol penutup dialog D-07
27. Sesi B: klik `✕` pada Modal Create
28. Verifikasi dialog `Unsaved Changes` di sesi B
29. Sesi B: klik `[Leave]`
30. Tutup konteks UI kedua dan hapus sesi login browser terkait

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 16 (membuka sesi B), langkah 10, 11, 13, 26, 27, 29 (menutup dialog dan form dirty secara deterministik; S-08), langkah 14 dan 30 (menutup konteks kedua; S-09), dan langkah 15 serta 17 (ganti client eksplisit; S-07).
- Pemenang race ditetapkan oleh urutan Submit (sesi A lebih dulu) agar deterministik.
- Pembagian TC lintas spec: TC-FA-FAAM-633 dan 634 ada di spec 235.
- Temuan untuk QA:
  - TC-FA-FAAM-635 dan 636 menyebut "hampir bersamaan" tanpa mekanisme submit paralel; spec menulis Submit berurutan tanpa jeda.
  - TC-FA-FAAM-636 menyebut "dialog D-07" tanpa judul dan teksnya (rujukan PRD); spec mengasersi dialog D-07 tampil tanpa teks dan memakai "tombol penutup" tanpa label.
  - Pre-setup No. 16f dan 19i tidak memuat email akun Total Control; jumlah Asset Name pasca-sukses (10) berasal dari seeding 9 ditambah 1.
