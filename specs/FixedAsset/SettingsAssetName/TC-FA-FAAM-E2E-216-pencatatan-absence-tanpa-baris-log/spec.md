---
id: TC-FA-FAAM-E2E-216-pencatatan-absence-tanpa-baris-log
title: "Pencatatan Absence: Tanpa Baris Log untuk Delete Tidak Ada, Record Lain, dan Delete Label Diblokir"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-575
  - TC-FA-FAAM-588
  - TC-FA-FAAM-593
coverage:
  web: automated
---

# Pencatatan Absence: Tanpa Baris Log untuk Delete Tidak Ada, Record Lain, dan Delete Label Diblokir

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 22 (Category `IT Equipment`), No. 25 (Label), No. 25d (fixture `Guard Label Item 593`).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-216`, Code literal Tabel Dinamis (batas panjang Code; hook `before` menghapus sisa Code yang sama dari run lama):
  - `Edit Target Item 588 {runId}-216` (Code `ETI588`): salinan fixture 13d (Tabel Dinamis No. 56), Total Asset 0, Category `IT Equipment`, TAG `QR`, Brand `Dell` model `5420`, UoM `Unit`.
  - `Guard Label Item 593 {runId}-216` (Code `GLI593`): salinan fixture 25d, Total Asset 0, Default Label `Delete Guard Label 593 {runId}-216`; label itu tidak menempel pada aset mana pun. Label tersebut juga menjadi data Tab Labels.
  - `Warehouse Pallet 575 {runId}-216` (Code `PLT-WH575`): salinan fixture 13 (Tabel Dinamis No. 62), Total Asset 0.
- Kemampuan teknis: membuka Modal Changelog dan memakai Search di dalamnya; membaca jumlah baris hasil Search Changelog sebelum aksi (baseline); pelaku kedua lewat sesi API aktor untuk menghapus Asset Name hingga tersimpan (TC-FA-FAAM-575). Changelog adalah audit trail permanen sehingga total entri tidak diasersi, hanya selisih terhadap baseline.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini dan label `Delete Guard Label 593 {runId}-216` lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-575, 588, 593: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan

1. Ketik Search `{runId}-216`, tekan Enter

### TC-FA-FAAM-588: Aksi pada satu record tidak menulis entri ke record lain

2. Klik icon Changelog
3. Ketik Search `Guard Label Item 593 {runId}-216`, tekan Enter
4. Catat jumlah baris Changelog `Guard Label Item 593 {runId}-216` sebagai baseline G
5. Tutup Modal Changelog
6. Klik `⋯` baris `Edit Target Item 588 {runId}-216` lalu `Edit`
7. Ubah Code menjadi `NEG1`
8. Klik `[Save]`
9. Klik icon Changelog
10. Ketik Search `Edit Target Item 588 {runId}-216`, tekan Enter
11. Verifikasi satu baris Field `Code`, Old `ETI588`, New `NEG1`
12. Ganti isi kotak search dengan `Guard Label Item 593 {runId}-216`, tekan Enter
13. Verifikasi jumlah baris Changelog `Guard Label Item 593 {runId}-216` sama dengan baseline G pada langkah 4 (tidak ada entri baru untuk Asset Name lain)
14. Tutup Modal Changelog

### TC-FA-FAAM-593: Delete label yang dijadikan Default Label diblokir

15. Catat Last Updated baris `Guard Label Item 593 {runId}-216`
16. Klik icon Changelog
17. Ketik Search `Guard Label Item 593 {runId}-216`, tekan Enter
18. Catat jumlah baris Changelog `Guard Label Item 593 {runId}-216` sebagai baseline H
19. Tutup Modal Changelog
20. Buka tab Labels
21. Klik `⋯` baris label `Delete Guard Label 593 {runId}-216` lalu `Delete`
22. Verifikasi dialog `Cannot Delete Label` memuat bullet `Delete Guard Label 593 {runId}-216`, teks `This label is used as Default Label by 1 asset name.`, dan teks `Remove it from those assets and Default Label lists before deleting it.`
23. Verifikasi tidak ada teks `This label is assigned to`
24. Verifikasi tombol `[OK]`
25. Klik `[OK]`
26. Buka tab Asset Name
27. Verifikasi label `Delete Guard Label 593 {runId}-216` tetap ada di Default Label `Guard Label Item 593 {runId}-216`
28. Verifikasi Last Updated `Guard Label Item 593 {runId}-216` sama dengan nilai pada langkah 15
29. Klik icon Changelog
30. Ketik Search `Guard Label Item 593 {runId}-216`, tekan Enter
31. Verifikasi jumlah baris Changelog `Guard Label Item 593 {runId}-216` sama dengan baseline H pada langkah 18 (tidak ada baris Changelog Asset Name baru)
32. Tutup Modal Changelog

### TC-FA-FAAM-575: Delete record yang sudah tidak ada tidak menulis baris log

33. Klik `⋯` baris `Warehouse Pallet 575 {runId}-216` lalu `Delete` sehingga dialog konfirmasi tampil
34. Pelaku kedua (sesi API Total Control) menghapus `Warehouse Pallet 575 {runId}-216` hingga tersimpan
35. Klik `[Delete]` pada dialog konfirmasi
36. Klik icon Changelog
37. Ketik Search `Warehouse Pallet 575 {runId}-216`, tekan Enter
38. Verifikasi tepat satu baris Action `Delete` untuk `Warehouse Pallet 575 {runId}-216` (dari penghapusan pertama)
39. Verifikasi tidak ada baris Action `Delete` kedua untuk `Warehouse Pallet 575 {runId}-216`
40. Tutup Modal Changelog

## Notes

- P-5(a): spec ini kelas g; pemicu kelas lain (Delete label diblokir pada TC-FA-FAAM-593, dua sesi pada TC-FA-FAAM-575) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji. Tiap TC memakai seed dan baseline sendiri.
- Di atas smell 35 langkah. Spec berisi 40 langkah, di atas ~35. Alasan: seluruh blok kelas g, tiap blok punya seed dan baseline sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search tabel utama), langkah 2, 3, 9, 10, 12, 16, 17, 29, 30, 36, 37 (membuka dan mencari di Modal Changelog; S-12, S-14), langkah 5, 14, 19, 32, 40 (menutup Modal Changelog), langkah 20 dan 26 (pindah tab), dan langkah 4, 15, 18 (mencatat baseline).
- Anchor positif absence: langkah 11 (baris Edit target tampil) untuk langkah 13; langkah 22 dan 24 (dialog blok tampil) untuk langkah 23; langkah 27 dan 28 untuk langkah 31; langkah 38 (baris Delete pertama) untuk langkah 39.
- Urutan TC: TC-FA-FAAM-588, TC-FA-FAAM-593, lalu TC-FA-FAAM-575 (aksi menghapus data di akhir; S-10).
- Rujukan lintas spec: absence log atas tiga permukaan pada TC-FA-FAAM-576 dan TC-FA-FAAM-577 ada di spec 240 (TC-FA-FAAM-576 dan 577 tidak ada di `sourceTc` spec ini).
- Temuan untuk QA:
  - TC-FA-FAAM-575 menulis "Hapus lewat dua sesi" tanpa urutan; spec mengikuti pola dialog dibuka, pihak lain menghapus, lalu konfirmasi (S-04). Hasil UI sesi pertama pada record yang sudah hilang (toast atau dialog) tidak ada di Expected sehingga tidak diasersi.
  - Label `Delete Guard Label 593` tidak punya baris Pre-setup selain 25d; Tab Labels diasumsikan menampilkan label bersuffix spec ini dengan Search.
