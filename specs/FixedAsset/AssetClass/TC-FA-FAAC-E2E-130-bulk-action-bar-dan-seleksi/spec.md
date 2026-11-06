---
id: TC-FA-FAAC-E2E-130-bulk-action-bar-dan-seleksi
title: "Bulk Action Bar Tabel Asset Class: Tampil, Aksi Menurut Status Baris, Seleksi Halaman dan Lintas Halaman, serta Seleksi Dipertahankan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-435
  - TC-FA-FAAC-436
  - TC-FA-FAAC-437
  - TC-FA-FAAC-438
  - TC-FA-FAAC-439
  - TC-FA-FAAC-440
coverage:
  web: automated
---

# Bulk Action Bar Tabel Asset Class: Tampil, Aksi Menurut Status Baris, Seleksi Halaman dan Lintas Halaman, serta Seleksi Dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive).
- Data Pre-setup tambahan (hanya dibaca): jumlah Asset Class total [n] lebih dari 10 dan kurang dari Selection Limit (seed tambahan di luar sembilan kelas contoh); [n] diturunkan dari seeding dan tidak dibaca dari satu halaman tabel (8b butir 10). Seed disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data Asset Class (hanya seleksi sisi klien) dan tidak menjalankan aksi Activate atau Deactivate.

## Test Steps

### TC-FA-FAAC-435: Bulk Action Bar muncul saat satu baris dicentang

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Centang checkbox baris HEAVY-EQ
3. Verifikasi Bulk Action Bar tampil dengan jumlah terpilih 1
4. Klik icon `×` pada Bulk Action Bar
5. Verifikasi seleksi dibatalkan
6. Verifikasi Bulk Action Bar hilang

### TC-FA-FAAC-436: Aksi Bulk Action Bar mengikuti komposisi status baris terpilih

7. Ganti isi kotak search dengan `BLDG`, tekan Enter
8. Centang baris BLDG saja
9. Verifikasi Bulk Action Bar hanya menampilkan aksi `Deactivate`
10. Hilangkan centang BLDG
11. Ganti isi kotak search dengan `OFFICE-OLD`, tekan Enter
12. Centang baris OFFICE-OLD saja
13. Verifikasi Bulk Action Bar hanya menampilkan aksi `Activate`
14. Ganti isi kotak search dengan `BLDG`, tekan Enter
15. Centang baris BLDG sehingga BLDG dan OFFICE-OLD terpilih bersama
16. Verifikasi Bulk Action Bar menampilkan aksi `Activate` dan `Deactivate`
17. Klik icon `×` pada Bulk Action Bar
18. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-FAAC-437: Checkbox header hanya memilih baris di halaman aktif

19. Centang checkbox di header kolom Checkbox
20. Verifikasi hanya 10 baris di halaman 1 yang tercentang
21. Verifikasi checkbox header berstatus checked
22. Pindah ke halaman 2
23. Verifikasi di halaman 2 tidak ada baris yang tercentang
24. Pindah kembali ke halaman 1

### TC-FA-FAAC-438: Select All memilih semua baris lintas halaman lalu berubah menjadi Unselect All

25. Klik tombol `Select All ([n] records)`
26. Verifikasi seluruh [n] baris pada semua halaman terpilih
27. Verifikasi tombol berubah menjadi `Unselect All`
28. Klik tombol `Unselect All`
29. Verifikasi seluruh seleksi dibatalkan
30. Verifikasi Bulk Action Bar tertutup

### TC-FA-FAAC-439: Seleksi dipertahankan saat Search dan Filter diubah

31. Ketik Search `HEAVY-EQ`, tekan Enter
32. Centang baris HEAVY-EQ
33. Ganti isi kotak search dengan `IT-EQ`, tekan Enter
34. Centang baris IT-EQ
35. Ganti isi kotak search dengan `vehicles`, tekan Enter
36. Verifikasi selama Search aktif Bulk Action Bar tetap menunjukkan 2 baris terpilih walaupun baris itu tidak tampil
37. Klik `(←)` pada kotak Search
38. Ubah ukuran halaman tabel menjadi 100 supaya HEAVY-EQ dan IT-EQ terjangkau di halaman aktif
39. Verifikasi HEAVY-EQ dan IT-EQ masih tercentang
40. Klik icon `×` pada Bulk Action Bar

### TC-FA-FAAC-440: Seleksi dipertahankan saat pindah halaman

41. Kembalikan ukuran halaman tabel menjadi 10
42. Centang baris pertama di halaman 1
43. Pindah ke halaman 2 lalu kembali ke halaman 1
44. Verifikasi baris yang dicentang tetap tercentang
45. Verifikasi Bulk Action Bar tetap menunjukkan 1 baris terpilih

## Notes

- Langkah penghubung (S-03): langkah 17 dan 40 (membatalkan seleksi lewat `×`, S-09), langkah 18 (menutup input Search dan mereset tabel sebelum TC-FA-FAAC-437, S-09; R-16), langkah 24 (kembali ke halaman 1 sebelum TC-FA-FAAC-438; seleksi halaman dari langkah 19 dilanjutkan karena tombol Select All muncul pada Bulk Action Bar yang aktif), langkah 35 (Search `vehicles` ditulis sebagai bagian TC-FA-FAAC-439). Judul TC-FA-FAAC-439 menyebut Filter tetapi Langkah Uji hanya memuat Search; spec mengikuti Langkah Uji (lihat Temuan untuk QA).
- Baris contoh dijangkau lewat Search kode Class Code sebelum dicentang (precondition butir d TC-FA-FAAC-435, 436, dan 439): langkah 1, 7, 11, 14, 31, dan 33 (R-16). Seleksi dipertahankan antar Search (TC-FA-FAAC-439), sehingga OFFICE-OLD tetap tercentang saat BLDG dicentang pada langkah 15.
- Seleksi tidak dibatalkan pada akhir spec (langkah 42 sampai 45); seleksi hanya sisi klien dan hilang saat layar awal spec berikutnya dibuka oleh hook `beforeEach` suite.
- Alasan melebihi sekitar 35 langkah (45 langkah): semua blok satu topik (Bulk Action Bar tabel Asset Class) pada dataset yang sama, tiap blok berdiri sendiri, dan Search kode untuk menjangkau baris contoh menambah langkah tanpa mengubah topik.
- Aksi `Activate` dan `Deactivate` hanya diamati (tampil), tidak diklik; eksekusinya ada di spec lain.
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan status persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: TC-FA-FAAC-439 berjudul "Search dan Filter diubah" tetapi Langkah Uji dan Expected hanya memuat Search.
- Ukuran halaman (S-14, R-16): tabel memuat lebih dari 25 baris dengan ukuran halaman 10, sehingga HEAVY-EQ dan IT-EQ belum tentu tampil di halaman 1 setelah Search dikosongkan; langkah 38 menaikkan ukuran halaman menjadi 100 sebelum `Verifikasi` langkah 39, dan langkah 41 mengembalikannya ke 10 sebelum TC-FA-FAAC-440 yang membutuhkan halaman 2 (langkah penghubung, tanpa `Verifikasi`). Asumsi: seleksi dipertahankan saat ukuran halaman berubah (bagian dari perilaku seleksi dipertahankan TC-FA-FAAC-439).
