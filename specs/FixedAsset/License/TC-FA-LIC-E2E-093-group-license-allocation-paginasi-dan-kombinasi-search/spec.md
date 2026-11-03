---
id: TC-FA-LIC-E2E-093-group-license-allocation-paginasi-dan-kombinasi-search
title: "Group License Allocation: Kombinasi Search, Filter, Sort, dan Page Size serta Paginasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-323
  - TC-FA-LIC-324
  - TC-FA-LIC-325
  - TC-FA-LIC-326
coverage:
  web: automated
---

# Group License Allocation: Kombinasi Search, Filter, Sort, dan Page Size serta Paginasi

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup (identitas dan nilai dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki`, belum ada, disiapkan tim FE; nilai pada langkah adalah nilai fixture itu):
  - Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`; diperlukan TC-FA-LIC-326): client Paid Pre-setup #1 dengan `License allocation per group` ON; tabel Group License Allocation pada node All Groups menampilkan empat baris level 1: Produksi (Used 1450), Cabang Medan (Used 880), Cabang Surabaya (Used di atas 700), Kantor Pusat (Used 700); kode grup berawalan `GRP-`.
  - Variasi Pre-setup #12 dengan node Kantor Pusat memiliki 12 child (data uji, diperlukan TC-FA-LIC-323, 324, 325), kode grup berawalan `GRP-`; penerapan dan pemulihannya mengikuti pernyataan fixture BE pemulih Pre-setup #12 di `suite.md` dan dilakukan lewat langkah penghubung.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12.

## Test Steps

### TC-FA-LIC-326: Kombinasi Search, Filter, Sort, dan paginasi bekerja bersamaan dan lepas secara independen

1. Klik tab Allocation Quota di node All Groups
2. Ketik Search `GRP-`, tekan Enter
3. Buka Filter Panel, isi `Used by This Group` Min `700`, klik `[Apply]`
4. Klik header kolom `Allocated Quota` untuk sort, lalu ubah page size menjadi 25
5. Verifikasi semua kontrol berlaku bersamaan: tabel menampilkan Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat
6. Klik header kolom `Remaining Quota` untuk sort
7. Verifikasi mengganti kolom sort tidak mereset Search dan Filter: kotak Search tetap `GRP-`, filter `Used by This Group` Min `700` tetap, tabel menampilkan Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat
8. Klik `[Clear Field]`, lalu klik `[Apply]` pada Filter Panel
9. Verifikasi Clear Filter tidak mereset Search dan Sort: kotak Search tetap `GRP-` dan indikator sort kolom `Remaining Quota` tetap aktif
10. Isi `Used by This Group` Min `700`, klik `[Apply]`, lalu kosongkan isi kotak search, tekan Enter
11. Verifikasi mengosongkan Search tidak mereset Filter dan Sort: filter `Used by This Group` Min `700` tetap dan indikator sort kolom `Remaining Quota` tetap aktif
12. Ketik Search `medan`, tekan Enter
13. Ubah `Used by This Group` Min menjadi `1000`, klik `[Apply]`
14. Verifikasi hasil kosong dari Search dan Filter: tabel menampilkan empty state `No results found`
15. Klik `[Clear Field]`, lalu klik `[Apply]` pada Filter Panel
16. Verifikasi tabel pulih saat Filter dilepas: tabel menampilkan Cabang Medan
17. Kosongkan isi kotak search, tekan Enter, lalu klik header kolom `Remaining Quota` hingga sort netral

### Pindah ke variasi Pre-setup #12 dengan 12 child pada Kantor Pusat

18. Terapkan variasi Pre-setup #12 dengan 12 child pada node Kantor Pusat
19. Klik menu License pada sidebar, lalu tab Allocation Quota di node All Groups
20. Klik node `Kantor Pusat` pada Sidebar

### TC-FA-LIC-323: Paginasi default 10 per halaman, pilihan 10/25/50/100, input nomor halaman

21. Verifikasi footer menampilkan default 10 baris per halaman
22. Buka pilihan page size
23. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
24. Tutup pilihan page size tanpa mengubah, lalu ketik nomor halaman 2 pada input dan tekan Enter
25. Verifikasi input nomor halaman 2 langsung membuka halaman 2
26. Buka pilihan page size, lalu pilih 25
27. Verifikasi seluruh 12 baris child tampil dalam satu halaman
28. Verifikasi tabel kembali ke halaman 1

### TC-FA-LIC-324: Nomor halaman tidak valid diabaikan; ganti sort tetap di halaman sekarang; ganti page size ke halaman 1

29. Buka pilihan page size, pilih 10, lalu pindah ke halaman 2
30. Ketik `0` pada input nomor halaman, tekan Enter
31. Verifikasi input `0` diabaikan dan tabel tetap di halaman 2
32. Ketik `99` pada input nomor halaman, tekan Enter
33. Verifikasi input `99` diabaikan dan tabel tetap di halaman 2
34. Ketik `abc` pada input nomor halaman, tekan Enter
35. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 2
36. Klik header kolom `Allocated Quota` untuk sort
37. Verifikasi mengganti sort tetap di halaman 2
38. Ganti page size menjadi 25
39. Verifikasi mengganti page size kembali ke halaman 1
40. Klik header kolom `Allocated Quota` hingga sort netral

### TC-FA-LIC-325: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

41. Buka pilihan page size, pilih 10, lalu pindah ke halaman 2
42. Ketik Search `GRP-`, tekan Enter
43. Verifikasi setelah Search tabel kembali ke halaman 1
44. Pindah ke halaman 2
45. Buka Filter Panel, isi `Used by This Group` Min `0`, klik `[Apply]`
46. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
47. Klik `[Clear Field]`, lalu klik `[Apply]`, dan kosongkan isi kotak search, tekan Enter

## Notes

- Langkah penghubung tanpa `Verifikasi`: menutup pilihan page size, memilih page size 10 dan pindah ke halaman 2 sebagai awal TC-FA-LIC-324 dan TC-FA-LIC-325, membersihkan Search, Filter, dan Sort di akhir blok (S-09), membuka node `Kantor Pusat`, dan blok "Pindah ke variasi Pre-setup #12 dengan 12 child pada Kantor Pusat" (menerapkan variasi lalu membuka ulang tab lewat sidebar yang mereset Search, Sort, dan Filter).
- Spec berada di atas sekitar 35 langkah. Alasan: seluruh blok adalah paginasi dan kombinasi kontrol satu tabel, kegagalan satu blok tidak membuat blok lain kehilangan makna, dan dua kumpulan data (Pre-setup #12 dan variasinya) dipakai berurutan dengan penerapan variasi eksplisit.
- Temuan untuk QA: (1) TC-FA-LIC-323 sampai 325 menulis "Buka License > Allocation Quota (node All Groups)" tetapi Precondition menyebut tabel berisi 12 child pada satu node (fixture); node All Groups hanya berisi empat baris, sehingga spec memakai node Kantor Pusat dengan 12 child. (2) TC-FA-LIC-323 butir c menyebut "seluruh 25 baris" padahal fixture 12 child; spec mengasersi seluruh 12 baris. (3) TC-FA-LIC-323 butir d menyebut "halaman 2 (bila tersedia)" sesudah page size 25, ketika seluruh baris sudah muat satu halaman; spec mengasersi halaman 2 pada page size 10 sebelum memilih 25. (4) TC-FA-LIC-324 dan TC-FA-LIC-325 tidak menyebut kolom sort dan nilai Filter; spec memakai `Allocated Quota` dan `Used by This Group` Min `0`. (5) TC-FA-LIC-326 langkah 5 mengosongkan filter lalu Search, sehingga Expected b ("mengosongkan Search tidak mereset Filter"), c ("mengganti kolom sort"), dan d ("hasil kosong dari Search dan Filter pulih") tidak dapat diamati dengan urutan itu; spec mengatur ulang urutan aksi dan menambah Search `medan` dengan Filter Min `1000` untuk hasil kosong (oracle: Cabang Medan Used 880, TC-FA-LIC-301).
