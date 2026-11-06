---

id: TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination

title: "Kombinasi Search, Filter, Sort, dan Pagination pada List serta Mutasi Saat Terfilter"

priority: High

caseType: Positive

status: draft

sourceTc:

  - TC-AC-LA-312

  - TC-AC-LA-313

  - TC-AC-LA-314

  - TC-AC-LA-315

  - TC-AC-LA-316

  - TC-AC-LA-317

  - TC-AC-LA-319

  - TC-AC-LA-318

coverage:

  web: automated

---



# Kombinasi Search, Filter, Sort, dan Pagination pada List serta Mutasi Saat Terfilter



## Prerequisites



- Mode: FE+BE.

- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.

- Akun ganti akun (langkah 55 sampai 56): Distributor Create+Read+Update (Pre-setup #4) `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, PT Maju Bersama), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (S-07).

- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.

- Data Pre-setup: seed #54 (minimal 30 alokasi lintas enam status, lebih dari 25 baris di tab Current; Product `FAMS` pada lebih dari 10 baris tab Current; Client `PT Sejahtera` dan `Klinik Medika Jaya`; License Type `Concurrent User` dan `Log Source`), Client PT Sejahtera (#19), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation OFF pada group Client uji (#39). Seed #54 bersifat baca-saja untuk langkah 1 sampai 54.

- Data Dinamis TC-AC-LA-318: satu alokasi Concurrent User ke PT Sejahtera yang dibuat Dewi pada langkah 59, dan satu alokasi berstatus `Waiting for Approval` milik spec dengan Dewi sebagai requester sebagai target Cancel (S-06; Allocation ID dibaca dari hasil seeding), di-seed lewat kemampuan "disediakan tim FE/BE" di hook `before` (seeding backend tidak tunduk pada toggle #39 OFF; Submit lewat API pada toggle OFF akan langsung Completed). Pemulihan kedua alokasi dilakukan baseline automation sebelum tiap spec (Catatan TC).

- Kemampuan teknis: seeding record `Waiting for Approval` milik spec dengan Dewi sebagai requester, disediakan tim FE/BE (bukan Submit lewat sesi API, karena toggle OFF menghasilkan Completed).

- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.



## Test Steps



### TC-AC-LA-312: Kombinasi penuh Search, Filter, Sort, dan Pagination



1. Ketik Search `Sejahtera`, tekan Enter

2. Terapkan filter License Type `Concurrent User`

3. Klik header Quantity

4. Verifikasi sedikitnya satu baris tampil

5. Verifikasi hasil adalah irisan Search dan Filter

6. Verifikasi hasil terurut Quantity ascending

7. Ubah page size ke 25

8. Verifikasi Search `Sejahtera` tidak ter-reset

9. Verifikasi Filter License Type `Concurrent User` tidak ter-reset

10. Verifikasi Sort Quantity ascending tidak ter-reset



### TC-AC-LA-313: Urutan Search dan Filter



11. Klik menu `License Allocation` di sidebar

12. Ketik Search `Sejahtera`, tekan Enter

13. Terapkan filter Product `FAMS`

14. Catat baris yang tampil

15. Klik menu `License Allocation` di sidebar

16. Terapkan filter Product `FAMS`

17. Ketik Search `Sejahtera`, tekan Enter

18. Catat baris yang tampil

19. Verifikasi baris yang dicatat pada langkah 14 dan langkah 18 adalah himpunan yang sama



### TC-AC-LA-314: Clear Filter mempertahankan Search dan Sort



20. Klik menu `License Allocation` di sidebar

21. Ketik Search `Sejahtera`, tekan Enter

22. Terapkan filter Product `FAMS`

23. Klik header Client

24. Klik ikon Filter

25. Klik `[Clear Field]` lalu `[Apply]`

26. Verifikasi ikon Filter tanpa titik indikator (kriteria filter hilang)

27. Verifikasi Search `Sejahtera` tetap aktif

28. Verifikasi Sort Client ascending tetap aktif



### TC-AC-LA-315: Clear Search mempertahankan Filter dan Sort



29. Terapkan filter Product `FAMS`

30. Klik ikon `(✕)` pada kotak Search

31. Tekan Enter pada input kosong

32. Verifikasi Search kosong

33. Verifikasi filter Product `FAMS` tetap aktif

34. Verifikasi Sort Client ascending tetap aktif



### TC-AC-LA-316: Ganti kolom sort mempertahankan Search dan Filter



35. Ketik Search `Sejahtera`, tekan Enter

36. Klik header Quantity

37. Verifikasi Search `Sejahtera` tetap aktif

38. Verifikasi filter Product `FAMS` tetap aktif

39. Verifikasi sort berpindah ke Quantity



### TC-AC-LA-317: Pemulihan dari empty state



40. Klik menu `License Allocation` di sidebar

41. Ketik Search `Sejahtera`, tekan Enter

42. Terapkan filter Client `Klinik Medika Jaya`

43. Verifikasi `No results found` tampil

44. Klik ikon Filter

45. Klik `[Clear Field]` lalu `[Apply]`

46. Verifikasi sedikitnya satu baris tampil

47. Verifikasi tabel pulih menampilkan baris yang cocok kriteria tersisa (Search `Sejahtera`)



### TC-AC-LA-319: Filter dipertahankan saat berpindah halaman



48. Klik menu `License Allocation` di sidebar

49. Catat jumlah total baris tab Current tanpa filter

50. Terapkan filter Product `FAMS` dengan 10 data per halaman

51. Pindah ke halaman 2

52. Pindah ke halaman 1

53. Verifikasi filter Product `FAMS` tetap aktif lintas halaman

54. Verifikasi jumlah total mengikuti hasil filter (berbeda dari jumlah total pada langkah 49)



### TC-AC-LA-318: Mutasi saat tabel terfilter (ganti akun ke Dewi A)



55. Logout

56. Login sebagai Distributor Create+Read+Update (Pre-setup #4) `dewiFullLic_automated_{namaCompany}@qwertysystem.net`

57. Klik menu `License Allocation` di sidebar

58. Terapkan filter License Type `Log Source`

59. Buat alokasi Concurrent User ke PT Sejahtera lewat form Allocate License (Payment Wallet) hingga alokasi tersimpan

60. Verifikasi sedikitnya satu baris License Type `Log Source` tampil

61. Verifikasi alokasi Concurrent User baru tidak muncul di tabel terfilter Log Source

62. Klik menu `License Allocation` di sidebar

63. Terapkan filter Status `Waiting for Approval`

64. Ketik Search Allocation ID seed `Waiting for Approval` milik spec, tekan Enter

65. Cancel baris seed itu lewat row action `Cancel Allocation`, lalu klik `[Cancel Request]` pada dialog konfirmasi

66. Kosongkan kotak search: klik `✕` pada Search, tekan Enter

67. Verifikasi baris `Waiting for Approval` lain tetap tampil

68. Verifikasi baris dengan Allocation ID seed yang di-Cancel hilang dari hasil filter Status `Waiting for Approval`

69. Klik tab `History`

70. Verifikasi baris yang di-Cancel tampil di tab History



## Notes



- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-AC-LA-312, TC-AC-LA-313, TC-AC-LA-314, TC-AC-LA-315, TC-AC-LA-316, TC-AC-LA-317, TC-AC-LA-319, lalu TC-AC-LA-318 (satu-satunya TC menulis data, S-10).

- Langkah `Terapkan filter <Field> <opsi>` berarti: klik ikon Filter, buka dropdown Field, centang opsi, klik `[Apply]`.

- Langkah penghubung (S-03): langkah 11, 15, 20, 40, 48, 57, 62 (klik menu sidebar mereset Search, Sort, Filter, dan paginasi), langkah 14, 18, 49 (mencatat baris dan jumlah), langkah 64 (Search Allocation ID seed untuk menemukan baris target Cancel, R-16) dan langkah 66 (mengosongkan Search dengan klik `✕` lalu Enter supaya filter Status tetap aktif dan baris `Waiting for Approval` lain kembali tampil).

- TC-AC-LA-315 dan TC-AC-LA-316 melanjutkan state TC sebelumnya (Search, Sort, dan Filter yang masih aktif) sebagai precondition mereka.

- Alasan spec melewati sekitar 35 langkah: semua blok satu topik (kombinasi kontrol List) dan satu dataset baca-saja (#54) kecuali blok terakhir yang memakai data milik spec; blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal (bagian 3, ganti akun eksplisit).

- Temuan untuk QA:

  - TC-AC-LA-318 mensyaratkan toggle Require Approval OFF (#39) sekaligus meng-Cancel baris `Waiting for Approval`, yang hanya terbentuk bila approval ON; spec memakai record `Waiting for Approval` yang di-seed lewat kemampuan "disediakan tim FE/BE" di hook `before` (tidak tunduk toggle) dan tidak mengubah toggle. Butuh keputusan QA.

  - TC-AC-LA-318 langkah 2 ("Buat alokasi Concurrent User") tidak merinci field form (Target, Type, Quantity, Pay From) dan langkah 3 tidak menyebut baris mana yang di-Cancel; spec mengikuti alur form Allocate License TC sumber alokasi Concurrent User dan target Cancel milik spec.

  - TC-AC-LA-318 tidak menyebut apakah filter License Type `Log Source` bertahan sesudah Submit; spec mengasersi tabel terfilter pada langkah 60 dan 61 sesudah alokasi tersimpan.

  - TC-AC-LA-319 membutuhkan halaman 2 pada hasil filter Product `FAMS` (lebih dari 10 baris); dipenuhi asumsi seed #54.

  - TC-AC-LA-313 Expected ("himpunan baris yang sama") tidak menyebut jumlah baris; spec membandingkan baris yang dicatat dari halaman pertama kedua urutan.

