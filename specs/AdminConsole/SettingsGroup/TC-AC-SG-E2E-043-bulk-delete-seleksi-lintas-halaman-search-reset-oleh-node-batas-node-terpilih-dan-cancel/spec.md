---
id: TC-AC-SG-E2E-043-bulk-delete-seleksi-lintas-halaman-search-reset-oleh-node-batas-node-terpilih-dan-cancel
title: "Bulk Delete: Seleksi Lintas Halaman dan Search, Reset oleh Node, Batas Node Terpilih, dan Cancel"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-154
  - TC-AC-SG-155
  - TC-AC-SG-156
  - TC-AC-SG-167
coverage:
  web: automated
---

# Bulk Delete: Seleksi Lintas Halaman dan Search, Reset oleh Node, Batas Node Terpilih, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Hapus Utama (Pre-setup #21) `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #21 (entitas `Distributor Hapus Utama`, dibaca saja), nama literal karena TC mengasersi nama baris dan jumlah descendant:
  - `Hapus Bulk 1` sampai `Hapus Bulk 6` dan `Hapus Warn A`, `Hapus Warn B`, `Hapus Warn B1`, `Hapus Warn B2` (tanpa entitas), total 24 node entitas sehingga tabel All Groups memiliki tiga halaman (ukuran halaman default 10).
  - `Hapus Member B` dengan descendant `Hapus Member B1`, `Hapus Member B2`, dan `Hapus Member B3`: N = 3 untuk node `Hapus Member B` (diturunkan dari seeding Pre-setup #21, bagian 8b butir 10).
- Spec ini hanya memilih baris dan membatalkan dialog; tidak ada node yang dihapus atau diubah, Last Updated tidak berubah (S-06, aksi dibatalkan). Hook `before` dan `after` memastikan baseline Pre-setup #21 lewat Fixture BE.
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-154: Seleksi bertahan lintas halaman, Search, dan Filter

1. Ketik Search `Hapus Bulk 1`, tekan Enter
2. Centang kolom Checkbox pada baris `Hapus Bulk 1`
3. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
4. Pindah ke halaman 2
5. Centang baris pertama pada halaman 2
6. Verifikasi teks Bulk Actions Bar tetap menghitung seluruh baris terpilih ("2 Groups selected") setelah pindah halaman
7. Ketik Search `Hapus Warn`, tekan Enter
8. Verifikasi teks Bulk Actions Bar tetap "2 Groups selected" setelah Search diubah
9. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
10. Verifikasi teks Bulk Actions Bar tetap "2 Groups selected" setelah Search dibersihkan
11. Klik ikon Filter pada toolbar
12. Isi Total Member Min = 1
13. Klik `[Apply]`
14. Verifikasi teks Bulk Actions Bar tetap "2 Groups selected" setelah Filter Total Member dengan Min 1 diterapkan
15. Klik `[Clear Field]`
16. Klik `[Apply]`
17. Verifikasi teks Bulk Actions Bar tetap "2 Groups selected" setelah Filter dibersihkan
18. Klik ikon Filter pada toolbar untuk menutup Filter Panel
19. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-155: Mengganti atau toggle node sidebar mereset seleksi

20. Ketik Search `Hapus Bulk`, tekan Enter
21. Centang kolom Checkbox pada baris `Hapus Bulk 1` dan `Hapus Bulk 2`
22. Klik node `Hapus Warn B` di sidebar
23. Verifikasi seleksi kosong setelah mengganti node
24. Verifikasi Bulk Actions Bar hilang
25. Klik node `All Groups` di sidebar
26. Ganti isi kotak search dengan `Hapus Bulk`, tekan Enter
27. Verifikasi baris `Hapus Bulk 1` dan `Hapus Bulk 2` tidak otomatis terpilih lagi (checkbox tidak tercentang)
28. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-156: Bulk Delete tidak menjangkau baris yang tidak tampil pada node terpilih

29. Klik node `Hapus Member B` di sidebar
30. Klik "Select All (3 records)" pada Bulk Actions Bar
31. Verifikasi Select All hanya memilih descendant `Hapus Member B` (3 baris: `Hapus Member B1`, `Hapus Member B2`, `Hapus Member B3`)
32. Verifikasi Bulk Actions Bar menampilkan "3 Groups selected"
33. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
34. Verifikasi dialog tampil
35. Verifikasi bullet nama pada dialog hanya memuat baris terpilih (`Hapus Member B1`, `Hapus Member B2`, `Hapus Member B3`), bukan group di luar node `Hapus Member B`
36. Klik `[Cancel]` pada dialog
37. Verifikasi dialog tertutup
38. Verifikasi seluruh group tetap ada (`Hapus Member B1`, `Hapus Member B2`, `Hapus Member B3` masih tampil di tabel)
39. Verifikasi tidak ada toast
40. Klik ikon `×` pada Bulk Actions Bar
41. Klik node `All Groups` di sidebar

### TC-AC-SG-167: Cancel pada dialog bulk mempertahankan seleksi

42. Ketik Search `Hapus Bulk`, tekan Enter
43. Centang kolom Checkbox pada baris `Hapus Bulk 4` dan `Hapus Bulk 5`
44. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
45. Klik `[Cancel]`
46. Verifikasi dialog tertutup
47. Verifikasi seleksi dan Bulk Actions Bar ("2 Groups selected") dipertahankan
48. Verifikasi baris `Hapus Bulk 4` dan `Hapus Bulk 5` masih tampil dan tercentang (tidak ada group terhapus)
49. Klik ikon `×` pada Bulk Actions Bar

## Notes

- Langkah penghubung (S-03): langkah 1, 20, 26, dan 42 (Search untuk menemukan baris target, R-16); langkah 3, 9, 28 (reset Search); langkah 18 (menutup Filter Panel); langkah 19, 40, dan 49 (membersihkan seleksi, S-09); langkah 41 (kembali ke All Groups); langkah 45 (aksi TC `[Cancel]`).
- Langkah 26: Search tetap menyaring tabel `Hapus Bulk` pada langkah 20 atau sudah kosong setelah klik node sidebar; langkah ditulis "Ganti isi kotak search" supaya benar pada kedua keadaan. Perilaku Search setelah klik node sidebar (bertahan atau direset) perlu dikonfirmasi tim FE.
- Langkah 32 (`Verifikasi Bulk Actions Bar menampilkan "3 Groups selected"`) adalah asersi tambahan yang tidak ada di Expected TC-AC-SG-156: teks hitungan seleksi memperkuat bukti bahwa Select All hanya memilih tiga descendant `Hapus Member B` (selaras dengan teks "2 Groups selected" pada langkah 47 untuk TC-AC-SG-167), sehingga dipertahankan.
- Langkah 30 mengikuti TC; "Select All (3 records)" memakai N = 3 dari seeding.
- Langkah 15 dan 16 membersihkan Filter dengan `[Clear Field]` lalu `[Apply]`; Filter Panel tetap terbuka sesudah `[Apply]` dan ditutup di langkah 18.
- Alasan di atas sekitar 35 langkah: satu halaman, satu komponen (Bulk Actions Bar), dan seluruh blok memakai seed Pre-setup #21 yang sama tanpa mengubah data; tiap blok TC berdiri sendiri dan berakhir dengan seleksi bersih, sehingga penggabungan menghemat login dan pembukaan halaman.
- Temuan untuk QA:
  - TC-AC-SG-154 langkah 3 "centang satu baris" di halaman 2 tidak menyebut baris tertentu; spec memilih baris pertama halaman 2.
  - Perilaku `(←)` pada kotak Search terhadap pagination diasumsikan mereset tabel ke halaman 1 sesuai bagian 8b butir 9.
