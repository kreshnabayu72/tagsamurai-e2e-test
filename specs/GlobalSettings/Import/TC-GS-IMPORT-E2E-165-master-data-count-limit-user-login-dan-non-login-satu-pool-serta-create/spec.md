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
2. Buka Global Settings > Import, pilih Sub-Tab User Login
3. Klik `[Upload File]` di toolbar
4. Pilih berkas `user-login-division-cap.csv` di file picker
5. Biarkan seluruh dropdown File Column pada nilai auto-match
6. Klik `[Confirm Mapping]`
7. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
8. Verifikasi toast sukses "Success, division has been created. Some items were skipped."
9. Verifikasi Error Summary Callout memuat pesan "You've reached the platform limit of 1000 divisions. Contact support if you need a higher limit." dengan badge "1 row"
10. Muat ulang halaman Import > User Login
11. Verifikasi baris #1 `Pengadaan` berstatus `pending`
12. Verifikasi baris #2 `Logistik` tetap berstatus `error`
13. Verifikasi Error Summary Callout tetap memuat pesan "You've reached the platform limit of 1000 divisions. Contact support if you need a higher limit." dengan badge "1 row" setelah muat ulang
14. Buka Global Settings > User > Division
15. Ketik Search `Pengadaan`, tekan Enter
16. Verifikasi pencarian `Pengadaan` menampilkan 1 baris `Pengadaan`
17. Ganti isi kotak search dengan `Logistik`, tekan Enter
18. Verifikasi pencarian `Logistik` tidak menampilkan baris

### TC-GS-IMPORT-719: Create Missing Positions saat Master Data Count Limit tercapai

19. Reset Client Limit lewat skrip fixture: tanpa draft User Login, Master Data Count Limit Position 1000 dengan 999 Position tersimpan (sisa 1 slot)
20. Buka Global Settings > Import, pilih Sub-Tab User Login
21. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-position-cap.csv`
22. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
23. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
24. Verifikasi toast sukses "Success, position has been created. Some items were skipped."
25. Verifikasi Error Summary Callout memuat pesan "You've reached the platform limit of 1000 positions. Contact support if you need a higher limit." dengan badge "1 row"
26. Muat ulang halaman Import > User Login
27. Verifikasi baris #1 (`Store Supervisor`, kemunculan pertama menurut Row #) berstatus `pending`
28. Verifikasi baris #2 (`Shift Lead`) tetap berstatus `error`
29. Buka Global Settings > User > Position
30. Ketik Search `Store Supervisor`, tekan Enter
31. Verifikasi pencarian `Store Supervisor` menampilkan 1 baris `Store Supervisor`
32. Ganti isi kotak search dengan `Shift Lead`, tekan Enter
33. Verifikasi pencarian `Shift Lead` tidak menampilkan baris

### TC-GS-IMPORT-408: Commit Tab User Login melampaui kuota menjadi error

34. Reset Client Limit lewat skrip fixture: Master Data Count Limit User 1000 dengan 999 User tersimpan (sisa 1 slot); seed draft User Login 2 baris `pending` dari `user-login-cap-2.csv`
35. Buka Global Settings > Import, pilih Sub-Tab User Login
36. Klik `[Import (2)]`
37. Tunggu commit selesai: muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
38. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
39. Verifikasi Staging Table menampilkan 1 baris berstatus `error` yaitu `Qori Ramadhan`
40. Verifikasi kolom # baris itu bernilai 1
41. Verifikasi Error Summary Callout memuat "You've reached the platform limit of 1000 users. Contact support if you need a higher limit." dengan badge "1 row"
42. Buka halaman Global Settings > User > User List > Login User
43. Ketik Search `Putu Aditya`, tekan Enter
44. Verifikasi Search `Putu Aditya` menampilkan baris bernama persis `Putu Aditya`
45. Ganti isi kotak search dengan `Qori Ramadhan`, tekan Enter
46. Verifikasi Search `Qori Ramadhan` tidak menampilkan baris bernama persis `Qori Ramadhan`

### TC-GS-IMPORT-409: User Login dan User Non Login satu pool

47. Reset Client Limit lewat skrip fixture: Master Data Count Limit User 1000 dengan 999 user (Login dan Non Login, termasuk `rina.admin.limit@example.com`) tersimpan (sisa 1 slot); seed draft User Login 1 baris `pending` (`user-login-pool-1.csv`) dan draft User Non Login 1 baris `pending` (`user-non-login-pool-1.csv`)
48. Buka Global Settings > Import, pilih Sub-Tab User Login
49. Klik `[Import (1)]` di Tab User Login
50. Tunggu commit selesai: muat ulang halaman Import > User Login setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
51. Verifikasi Dropzone tampil di Tab User Login
52. Buka halaman Global Settings > User > User List > Login User
53. Ketik Search `Putu Aditya`, tekan Enter
54. Verifikasi Search `Putu Aditya` menampilkan baris bernama `Putu Aditya` (user ke-1000)
55. Buka halaman Global Settings > Import, pilih Sub-Tab User Non Login
56. Klik `[Import (1)]` di Tab User Non Login
57. Tunggu commit selesai: muat ulang halaman Import > User Non Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
58. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
59. Verifikasi Staging Table Tab User Non Login menampilkan 1 baris berstatus `error` yaitu Qori Ramadhan
60. Verifikasi Error Summary Callout memuat "You've reached the platform limit of 1000 users. Contact support if you need a higher limit." dengan badge "1 row"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data (e); objek uji adalah batas Master Data Count Limit pada Create Missing dan commit User, dengan seed 999 record per katalog sebagai volume.
- Alasan melewati sekitar 35 langkah (60 langkah nominal): empat blok homogen (batas kuota di slot terakhir per katalog), semua satu kelas dan berdiri sendiri dengan reset Client Limit di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok Create Missing (TC-332, 719) mendahului blok commit (TC-408, 409).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 19, 34, 47), pembukaan halaman dan Sub-Tab, polling job (langkah 37, 50, 57), dan Search atomik (butir 9 bagian 8b). Pencarian yang menampilkan baris (langkah 16, 31, 44, 54) menjadi anchor positif sebelum asersi absence berikutnya (langkah 18, 33, 46).
- Temuan untuk QA:
  - TC-GS-IMPORT-332, 408, 409, 719 memakai nama literal (`Pengadaan`, `Store Supervisor`, `Putu Aditya`, dan seterusnya) tanpa suffix per run karena asersi Search mencocokkan nama persis; spec menjaga isolasi lewat reset seed dan cleanup di `after`.
  - TC-GS-IMPORT-332 dan 719 menulis langkah pencarian "Hapus isi Search, ketik ..." tanpa menyebut Enter pada langkah hapus; spec memakai "ganti isi kotak search" yang atomik.
  - TC-GS-IMPORT-409 menyebut `rina.admin.limit@example.com` sebagai User Login aktif Client Limit yang termasuk dalam 999 user (Pre-setup Client Limit); spec memakainya sebagai Represented By tanpa mengubahnya.
  - Post Condition TC-GS-IMPORT-332, 408, 409, 719 (record tersimpan, total 1000, draft berisi baris `error` atau `pending`) dikonfirmasi oleh Expected tiap TC dan tidak diasersi tambahan (S-01).
  - TC-GS-IMPORT-332, 408, 409, 719 memakai Division `Engineering` (dan produk `Global Settings`) tanpa menyatakan bahwa keduanya ada di Client Limit dan termasuk dalam 999 Division seed; spec menuliskannya di Prerequisites sebagai kemampuan seed yang disediakan tim FE sampai TC menyatakannya. Bila `Engineering` tidak ada, baris `Qori Ramadhan` dan `Putu Aditya` menjadi `error` "Division not found" dan asersi "1 error remains" dan "user ke-1000" tidak lagi menguji batas kuota.
  - Pola kuota pada Division di TC-GS-IMPORT-410 dan 720 (race dua sesi) ada di spec 151.
