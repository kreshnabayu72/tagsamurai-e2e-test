---

id: TC-AC-LA-E2E-071-edit-record-pending-toggle-off

title: "Edit Allocation Pending dengan Require Approval OFF: Tetap Pending atau Active dengan Capture"

priority: Critical

caseType: Positive

status: draft

sourceTc:

  - TC-AC-LA-213

  - TC-AC-LA-215

  - TC-AC-LA-216

coverage:

  web: automated

---



# Edit Allocation Pending dengan Require Approval OFF: Tetap Pending atau Active dengan Capture



## Prerequisites



- Mode: FE+BE

- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current).

- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).

- Data Pre-setup: Toko Serba Ada (Pre-setup #21; term Active `SUBS-20250201-J7K8L` End Date 31 Dec 2026 dan term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34).

- Konfigurasi: Require Approval for Allocation OFF pada group Client uji (Pre-setup #39), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.

- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #46 bersama): tiga alokasi `Completed` berstatus lisensi `Pending`, Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini, Cost $3,650.00 di-Reserve (10 × $365 × 365 hari ÷ 365): `{idP4}` (TC-AC-LA-213), `{idP5}` (TC-AC-LA-215), `{idP6}` (TC-AC-LA-216). Tanggal submit pertama `{idP4}` diatur 25 Dec 2026 lewat fixture waktu.

- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture toggle Require Approval, fixture waktu untuk tanggal submit pertama, kemampuan membaca saldo kantong (Balance, Reserved, Available), ledger term, dan notifikasi Plan Owner (baseline jumlah notifikasi `License allocated` sebelum aksi).

- Kemampuan teknis tambahan (disediakan tim FE/BE): seeding satu notifikasi Plan Owner PT Maju Bersama yang tidak terkait `{idP6}` sehingga daftar notifikasi Plan Owner memuat sedikitnya satu notifikasi lain sebagai anchor asersi absence notifikasi (langkah 36). Jendela tunggu 5 detik tanpa memuat ulang halaman (langkah 37) adalah pilihan spec, bukan nilai TC atau PRD (bagian 6).

- State global: toggle Require Approval OFF dipulihkan ke nilai awal di hook `after`; saldo kantong dikembalikan oleh pembersihan record seed. Pelaku Capture pada term Active mengubah Last Updated record seed saja, bukan baris Pre-setup.

- Suite berjalan serial (`parallel: false`).



## Test Steps



### Edit Pending (toggle OFF): Target ke term Active menjadi Active dengan Capture



1. Ketik Search `{idP4}`, tekan Enter

2. Klik row action `Edit` pada baris Pending

3. Ganti Target ke term Active `SUBS-20250201-J7K8L`

4. Pilih Type `Concurrent User`

5. Isi Additional Quantity `10`

6. Catat Balance kantong saat ini

7. Klik `[Save]`

8. Verifikasi toast sukses: "Success, license allocation has been updated."

9. Verifikasi tidak ada dialog D-04

10. Verifikasi Status menjadi `Active`

11. Verifikasi Reserve disesuaikan dari `$3,650.00` ke `$70.00` (10 × $365 × 7 hari ÷ 365 = 70.0000, hari dihitung dari 25 sampai 31 Dec 2026 dengan kedua tanggal dihitung)

12. Verifikasi Reserve di-Capture tepat `$70.00`

13. Verifikasi Balance kantong berkurang `$70.00` dari Balance yang dicatat sebelum `[Save]`

14. Verifikasi Reserved turun total `$3,650.00` sehingga `$3,580.00` kembali ke Available

15. Verifikasi entri ledger pindah ke term Active dalam transaksi yang sama

16. Verifikasi kolom Cost menampilkan `$70.00`

17. Buka modal Changelog dari ikon Changelog pada Table Tools

18. Verifikasi baris Status Old `Pending` New `Active` dicatat pada entri `Edit` yang sama dengan perubahan lain atas `{idP4}`

19. Tutup modal Changelog



### Edit Pending (toggle OFF): hanya Quantity



20. Ganti isi kotak search dengan `{idP5}`, tekan Enter

21. Klik row action `Edit` pada baris Pending

22. Ubah hanya Additional Quantity menjadi `12`

23. Catat Balance kantong saat ini

24. Klik `[Save]`

25. Verifikasi Status lisensi tetap `Pending` tanpa kembali ke `Waiting for Approval`

26. Verifikasi Reserve disesuaikan dari `$3,650.00` menjadi `$4,380.00` (12 × $365 × 365 hari ÷ 365)

27. Verifikasi Capture tidak terjadi: Balance kantong sama dengan Balance yang dicatat sebelum `[Save]`



### Edit Pending ke term yang sudah mulai: requester dari entitas Plan Owner



28. Ganti isi kotak search dengan `{idP6}`, tekan Enter

29. Klik row action `Edit` pada baris Pending

30. Ganti Target ke term Active `SUBS-20250201-J7K8L`

31. Catat jumlah notifikasi `License allocated` Plan Owner PT Maju Bersama

32. Klik `[Save]`

33. Verifikasi Status `Active`

34. Verifikasi Capture terjadi

35. Buka notifikasi Plan Owner PT Maju Bersama

36. Verifikasi daftar notifikasi Plan Owner memuat sedikitnya satu notifikasi lain (daftar termuat, anchor)

37. Tunggu 5 detik tanpa memuat ulang halaman

38. Verifikasi jumlah notifikasi `License allocated` Plan Owner sama dengan jumlah yang dicatat, tidak ada notifikasi baru, karena entitas requester (PT Maju Bersama) sama dengan entitas Plan Owner



## Notes



- Langkah penghubung (S-03, R-16): langkah 1, 20, dan 28 (Search untuk menemukan baris seed), langkah 17 dan 19 (membuka dan menutup modal Changelog), langkah 6, 23, dan 31 (Catat baseline Balance dan jumlah notifikasi).

- Urutan toast sebelum asersi ketiadaan dialog D-04 pada langkah 8 dan 9: toast menjadi anchor bahwa penyimpanan selesai (8b butir 2 dan 11); urutan butir Expected TC-AC-LA-213 (a sebelum b) berubah karena alasan itu. Pada langkah 33 dan 38, Status `Active` menjadi anchor positif sebelum asersi ketiadaan notifikasi, dengan baseline notifikasi `License allocated` Plan Owner dicatat pada langkah 31.

- Langkah 35 (membuka notifikasi Plan Owner) dan 37 (jendela tunggu 5 detik tanpa Verifikasi, bagian 6) adalah langkah penghubung; langkah 36 adalah anchor positif asersi absence notifikasi pada langkah 38 (daftar notifikasi Plan Owner termuat dan memuat notifikasi lain; teks notifikasi lain itu tidak ada di katalog PRD sehingga tidak ditulis).

- Edit Pending dengan toggle ON (D-04) ada di spec 058.

- Spec melewati sekitar 35 langkah (38 langkah). Alasan pertahanan: ketiga blok satu kelas (edit alokasi Pending dengan Require Approval OFF) pada seed milik spec yang sama, tiap blok berdiri sendiri, dan tambahan langkah adalah langkah Catat baseline (S-12) serta anchor notifikasi (bagian 6).

- Temuan untuk QA:

  - TC-AC-LA-213 menyebut tanggal submit pertama diatur 25 Dec 2026 tetapi tidak menyatakan apakah jam server juga diatur; spec hanya mengatur tanggal submit pertama record `{idP4}` (fixture waktu) karena faktor hari dihitung dari tanggal itu.

  - TC-AC-LA-213 butir c dan e, TC-AC-LA-215 butir b, serta TC-AC-LA-216 butir a menyebut Reserve, Balance, dan ledger tanpa menyebut halaman atau cara membacanya; langkah 11 sampai 15, 26, 27, dan 33 memakai kemampuan baca state BE yang disediakan tim FE/BE.

  - TC-AC-LA-215 menyebut "tanpa D-04" pada judul tetapi Expected hanya memuat butir a dan b; spec mengikuti Expected dan tidak mengasersi ketiadaan D-04 pada blok ini.

  - TC-AC-LA-216 butir b: akun penerima notifikasi Plan Owner tidak disebut; langkah 38 memakai kemampuan baca notifikasi Plan Owner yang disediakan tim FE.

  - TC-AC-LA-213 langkah 2 menyebut Target `SUBS-20250201-J7K8L` dengan End Date 31 Dec 2026 dan alokasi baru tetap masuk akal hanya bila tanggal acuan berada dalam masa term Active; TC tidak menyebut tanggal acuan server selain tanggal submit pertama.

