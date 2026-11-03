---
id: TC-GS-IMPORT-E2E-165-master-data-count-limit-user-login-dan-non-login-satu-pool-serta-create
title: "Master Data Count Limit: User Login dan Non Login satu pool, serta Create Missing Divisions dan Positions di slot terakhir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-332
  - TC-GS-IMPORT-408
  - TC-GS-IMPORT-409
  - TC-GS-IMPORT-719
coverage:
  web: automated
---

# Master Data Count Limit: User Login dan Non Login satu pool, serta Create Missing Divisions dan Positions di slot terakhir

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai kuota Master Data Count Limit Client Limit (seed 999 record per katalog) yang dibagikan dengan spec batas kuota lain, dan draft Client Limit dibagikan ke seluruh admin; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client Limit (Bima Saputra) `totalControl_automated_qaTeam7@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTLIMIT_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client Limit dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Skrip seed R7/D-46: Client Limit memakai Master Data Count Limit minimum 1000 per katalog; 999 record per katalog tersimpan (Division, Position, User; nama `Seed [Entity] nnnn`), sisa 1 slot; seed dan draft dibuat ulang sebelum tiap TC dan dipulihkan sesudahnya. User Login `rina.admin.limit@example.com` (aktif) termasuk dalam 999 user.
  - Division `Engineering` (dan produk `Global Settings` untuk Access) ada di Client Limit dan termasuk dalam 999 Division seed (sisa 1 slot dihitung sesudahnya); disediakan tim FE sampai TC menyatakannya (lihat Temuan untuk QA).
  - Mock layanan AI deterministik mode normal D-40 (tabel D-41 dan D-42) untuk TC-332.
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job commit latar belakang selesai (bukan menunggu jam).
- Data Dinamis (milik spec ini; nama sesuai Data Uji TC karena asersi Search mencocokkan nama persis; hook `before` membersihkan sisa nama itu dari run sebelumnya dan hook `after` menghapus yang dibuat spec):
  - D-45 `user-login-division-cap.csv` (TC-332): 2 baris Siti Rahmawati dan Budi Santoso; Division `Pengadaan` (#1) dan `Logistik` (#2); Position kosong; Division `Pengadaan` dan `Logistik` belum ada di Client Limit.
  - D-45 `user-login-position-cap.csv` (TC-719): 2 baris Siti Rahmawati dan Budi Santoso; Division `Engineering`; Position `Store Supervisor` (#1) dan `Shift Lead` (#2).
  - `user-login-cap-2.csv` (TC-408): kolom First Name; Last Name; Email; Division; Access; #1 Putu Aditya `putu.aditya@example.com` Engineering `Global Settings`; #2 Qori Ramadhan `qori.ramadhan@example.com` Engineering `Global Settings`.
  - `user-login-pool-1.csv` dan `user-non-login-pool-1.csv` (TC-409): User Login Putu Aditya `putu.aditya@example.com` Engineering `Global Settings`; User Non Login Qori Ramadhan `qori.ramadhan@example.com` Engineering, Represented By `rina.admin.limit@example.com`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): kembalikan seed Division, Position, dan User Client Limit ke 999 (hapus `Pengadaan`, `Store Supervisor`, `Putu Aditya` dan record hasil commit lain), hapus draft Client Limit, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-332: Create Missing Divisions saat Master Data Count Limit tercapai

1. Reset Client Limit lewat skrip fixture: tanpa draft User Login, Master Data Count Limit Division 1000 dengan 999 Division tersimpan (sisa 1 slot); pastikan mock AI mode normal
2. Muat ulang halaman Import > User Login
3. Klik `[Upload File]` di toolbar
4. Pilih berkas `user-login-division-cap.csv` di file picker
5. Biarkan seluruh dropdown File Column pada nilai auto-match
6. Klik `[Confirm Mapping]`
7. Tunggu aksi selesai (Modal Column Mapping tertutup)
8. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
9. Verifikasi toast sukses "Success, division has been created. Some items were skipped."
10. Verifikasi Error Summary Callout memuat pesan "You've reached the platform limit of 1000 divisions. Contact support if you need a higher limit." dengan badge "1 row"
11. Muat ulang halaman Import > User Login
12. Verifikasi baris #1 `Pengadaan` berstatus `pending`
13. Verifikasi baris #2 `Logistik` tetap berstatus `error`
14. Verifikasi Error Summary Callout tetap memuat pesan "You've reached the platform limit of 1000 divisions. Contact support if you need a higher limit." dengan badge "1 row" setelah muat ulang
15. Buka Global Settings > User > Division
16. Ketik Search `Pengadaan`, tekan Enter
17. Verifikasi pencarian `Pengadaan` menampilkan 1 baris `Pengadaan`
18. Ganti isi kotak search dengan `Logistik`, tekan Enter
19. Verifikasi pencarian `Logistik` tidak menampilkan baris

### TC-GS-IMPORT-719: Create Missing Positions saat Master Data Count Limit tercapai

20. Reset Client Limit lewat skrip fixture: tanpa draft User Login, Master Data Count Limit Position 1000 dengan 999 Position tersimpan (sisa 1 slot)
21. Buka Global Settings > Import, pilih Sub-Tab User Login
22. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-position-cap.csv`
23. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
24. Tunggu aksi selesai (Modal Column Mapping tertutup)
25. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
26. Verifikasi toast sukses "Success, position has been created. Some items were skipped."
27. Verifikasi Error Summary Callout memuat pesan "You've reached the platform limit of 1000 positions. Contact support if you need a higher limit." dengan badge "1 row"
28. Muat ulang halaman Import > User Login
29. Verifikasi baris #1 (`Store Supervisor`, kemunculan pertama menurut Row #) berstatus `pending`
30. Verifikasi baris #2 (`Shift Lead`) tetap berstatus `error`
31. Buka Global Settings > User > Position
32. Ketik Search `Store Supervisor`, tekan Enter
33. Verifikasi pencarian `Store Supervisor` menampilkan 1 baris `Store Supervisor`
34. Ganti isi kotak search dengan `Shift Lead`, tekan Enter
35. Verifikasi pencarian `Shift Lead` tidak menampilkan baris

### TC-GS-IMPORT-408: Commit Tab User Login melampaui kuota menjadi error

36. Reset Client Limit lewat skrip fixture: Master Data Count Limit User 1000 dengan 999 User tersimpan (sisa 1 slot); seed draft User Login 2 baris `pending` dari `user-login-cap-2.csv`
37. Buka Global Settings > Import, pilih Sub-Tab User Login
38. Klik `[Import (2)]`
39. Tunggu aksi selesai (permintaan mendapat respons)
40. Tunggu commit selesai: muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
41. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
42. Verifikasi Staging Table menampilkan 1 baris berstatus `error` yaitu `Qori Ramadhan`
43. Verifikasi kolom # baris itu bernilai 1
44. Verifikasi Error Summary Callout memuat "You've reached the platform limit of 1000 users. Contact support if you need a higher limit." dengan badge "1 row"
45. Buka halaman Global Settings > User > User List > Login User
46. Ketik Search `Putu Aditya`, tekan Enter
47. Verifikasi Search `Putu Aditya` menampilkan baris bernama persis `Putu Aditya`
48. Ganti isi kotak search dengan `Qori Ramadhan`, tekan Enter
49. Verifikasi Search `Qori Ramadhan` tidak menampilkan baris bernama persis `Qori Ramadhan`

### TC-GS-IMPORT-409: User Login dan User Non Login satu pool

50. Reset Client Limit lewat skrip fixture: Master Data Count Limit User 1000 dengan 999 user (Login dan Non Login, termasuk `rina.admin.limit@example.com`) tersimpan (sisa 1 slot); seed draft User Login 1 baris `pending` (`user-login-pool-1.csv`) dan draft User Non Login 1 baris `pending` (`user-non-login-pool-1.csv`)
51. Buka Global Settings > Import, pilih Sub-Tab User Login
52. Klik `[Import (1)]` di Tab User Login
53. Tunggu aksi selesai (permintaan mendapat respons)
54. Tunggu commit selesai: muat ulang halaman Import > User Login setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
55. Verifikasi Dropzone tampil di Tab User Login
56. Buka halaman Global Settings > User > User List > Login User
57. Ketik Search `Putu Aditya`, tekan Enter
58. Verifikasi Search `Putu Aditya` menampilkan baris bernama `Putu Aditya` (user ke-1000)
59. Buka halaman Global Settings > Import, pilih Sub-Tab User Non Login
60. Klik `[Import (1)]` di Tab User Non Login
61. Tunggu aksi selesai (permintaan mendapat respons)
62. Tunggu commit selesai: muat ulang halaman Import > User Non Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
63. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
64. Verifikasi Staging Table Tab User Non Login menampilkan 1 baris berstatus `error` yaitu Qori Ramadhan
65. Verifikasi Error Summary Callout memuat "You've reached the platform limit of 1000 users. Contact support if you need a higher limit." dengan badge "1 row"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data (e); objek uji adalah batas Master Data Count Limit pada Create Missing dan commit User, dengan seed 999 record per katalog sebagai volume.
- Alasan melewati sekitar 35 langkah (65 langkah nominal): empat blok homogen (batas kuota di slot terakhir per katalog), semua satu kelas dan berdiri sendiri dengan reset Client Limit di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok Create Missing (TC-332, 719) mendahului blok commit (TC-408, 409).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 20, 36, 50), muat ulang halaman Import > User Login (langkah 2), pembukaan halaman dan Sub-Tab, "Tunggu aksi selesai (permintaan mendapat respons)" persis sesudah klik `[Import (N)]` dan sebelum polling (langkah 39, 53, 61; bagian 8b butir 8), "Tunggu aksi selesai (Modal Column Mapping tertutup)" persis sesudah klik `[Confirm Mapping]` dan sebelum klik tombol Callout (langkah 7, 24; bagian 8b butir 8), polling job (langkah 40, 54, 62), dan Search atomik (butir 9 bagian 8b). Pencarian yang menampilkan baris (langkah 17, 33, 47, 58) menjadi anchor positif sebelum asersi absence berikutnya (langkah 19, 35, 49).
- Temuan untuk QA:
  - Penanda selesai untuk klik `[Import (N)]` (langkah 39, 53, 61) tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
  - Penanda selesai untuk klik `[Confirm Mapping]` sebelum klik tombol Callout (langkah 7, 24) tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "Modal Column Mapping tertutup" sampai QA menetapkan penanda yang teramati.
  - TC-GS-IMPORT-332, 408, 409, 719 memakai nama literal (`Pengadaan`, `Store Supervisor`, `Putu Aditya`, dan seterusnya) tanpa suffix per run karena asersi Search mencocokkan nama persis; spec menjaga isolasi lewat reset seed dan cleanup di `after`.
  - TC-GS-IMPORT-332 dan 719 menulis langkah pencarian "Hapus isi Search, ketik ..." tanpa menyebut Enter pada langkah hapus; spec memakai "ganti isi kotak search" yang atomik.
  - TC-GS-IMPORT-409 menyebut `rina.admin.limit@example.com` sebagai User Login aktif Client Limit yang termasuk dalam 999 user (Pre-setup Client Limit); spec memakainya sebagai Represented By tanpa mengubahnya.
  - Post Condition TC-GS-IMPORT-332, 408, 409, 719 (record tersimpan, total 1000, draft berisi baris `error` atau `pending`) dikonfirmasi oleh Expected tiap TC dan tidak diasersi tambahan (S-01).
  - TC-GS-IMPORT-332, 408, 409, 719 memakai Division `Engineering` (dan produk `Global Settings`) tanpa menyatakan bahwa keduanya ada di Client Limit dan termasuk dalam 999 Division seed; spec menuliskannya di Prerequisites sebagai kemampuan seed yang disediakan tim FE sampai TC menyatakannya. Bila `Engineering` tidak ada, baris `Qori Ramadhan` dan `Putu Aditya` menjadi `error` "Division not found" dan asersi "1 error remains" dan "user ke-1000" tidak lagi menguji batas kuota.
  - Pola kuota pada Division di TC-GS-IMPORT-410 dan 720 (race dua sesi) ada di spec 151.
