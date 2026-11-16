---
id: TC-FA-FACO-UI-104-form-add-respons-server
title: "Form Add Account: toast dan reaksi atas respons server"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [D-13, FACO-LOGIC-10d, R-01, T-01, §7.2#p2, §7.2#b2, §7.2#b3, §7.3#b1, §[F-FACO-01] Create Account#r6, §9.4.2#r39, EB-FB-1@create-account, EB-FB-4, EB-ERR-1@create-account]
smoke: []
dependsOn: []
trace:
  D-13: [47, 48, 49, 50]
  FACO-LOGIC-10d: 47
  R-01: [14, 16, 28, 29, 31]
  T-01: [6, 14]
  §7.2#p2: [16, 17, 31, 32, 59, 60]
  §7.2#b2: [15, 30]
  §7.2#b3: [28, 29, 31, 32, 58]
  §7.3#b1: [16, 17, 31, 32, 59, 60]
  §[F-FACO-01] Create Account#r6: 52
  §9.4.2#r39: 52
  EB-FB-1@create-account: [6, 14]
  EB-FB-4: [8, 20, 22]
  EB-ERR-1@create-account: [16, 17, 18, 28, 31, 32, 33, 39, 41, 58, 59, 60]
anchor: []
coverage:
  web: automated
---

# Form Add Account: toast dan reaksi atas respons server

## Prerequisites
- Aktor: Total Control.
- Layar awal: Modal Add Account pada Settings > Accounting > Chart of Accounts.
- Komponen: Modal Add Account.
- Kondisi:
  - K1: penyimpanan akun berhasil.
  - K2: penyimpanan akun gagal karena error server.
  - K3: penyimpanan akun gagal karena timeout.
  - K4: Master Data Count Limit bernilai `1000`; saat modal dibuka jumlah akun masih di bawah batas, dan saat Submit dikirim jumlah akun sudah mencapai `1000`.
  - K5: penyimpanan akun gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K6: penyimpanan akun gagal karena koneksi terputus.

## Test Steps

### Submit berhasil menampilkan toast sukses yang hilang sendiri
1. Tampilkan Modal Add Account dengan kondisi K1
2. Ketik Account Code `6-4001-PR`
3. Ketik Account Name `Biaya Penyusutan Peralatan Produksi {runId}`
4. Pilih Account Function `Loss on Disposal`
5. Klik `[Submit]`
6. Verifikasi toast `Success, account has been created.` tampil sesudah `[Submit]` pada form Add
7. Waktu berlalu sampai 4 detik sejak toast sukses tampil
8. Verifikasi toast `Success, account has been created.` hilang sendiri

### Error server menampilkan toast gagal tanpa menutup form
9. Tampilkan Modal Add Account dengan kondisi K2
10. Ketik Account Code `6-4002-PR`
11. Ketik Account Name `Biaya Penyusutan Kendaraan Operasional {runId}`
12. Pilih Account Function `Accumulated Depreciation`
13. Klik `[Submit]`
14. Verifikasi toast `Error, failed to create account.` tampil
15. Verifikasi toast `Error, failed to create account.` tidak memiliki tombol aksi `[Try Again]` maupun `[Retry]`
16. Verifikasi modal Add Account tetap terbuka sesudah toast gagal tampil
17. Verifikasi input Account Code `6-4002-PR`, Account Name `Biaya Penyusutan Kendaraan Operasional {runId}`, dan Account Function `Accumulated Depreciation` dipertahankan
18. Verifikasi tombol `[Submit]` dapat diklik lagi sesudah toast gagal tampil
19. Waktu berlalu sampai 10 detik sejak toast gagal tampil
20. Verifikasi toast `Error, failed to create account.` masih tampil
21. Klik tombol tutup pada toast gagal
22. Verifikasi toast `Error, failed to create account.` tertutup sesudah tombol tutup diklik

### Timeout menampilkan toast koneksi tanpa menutup form
23. Tampilkan Modal Add Account dengan kondisi K3
24. Ketik Account Code `6-4003-PR`
25. Ketik Account Name `Biaya Penyusutan Mesin Cetak {runId}`
26. Pilih Account Function `Accumulated Depreciation`
27. Klik `[Submit]`
28. Verifikasi toast `Connection problem. Please try again.` tampil sesudah `[Submit]` pada form Add timeout
29. Verifikasi toast `Error, failed to create account.` tidak tampil sesudah timeout
30. Verifikasi toast koneksi `Connection problem. Please try again.` tidak menyediakan tombol aksi `[Try Again]` maupun `[Retry]`
31. Verifikasi modal Add Account tetap terbuka sesudah timeout
32. Verifikasi input Account Code `6-4003-PR`, Account Name `Biaya Penyusutan Mesin Cetak {runId}`, dan Account Function `Accumulated Depreciation` dipertahankan sesudah timeout
33. Verifikasi tombol `[Submit]` dapat diklik lagi sesudah timeout

### Submit ulang sesudah penyimpanan pulih berhasil
34. Tampilkan Modal Add Account dengan kondisi K5
35. Ketik Account Code `6-4005-PR`
36. Ketik Account Name `Biaya Penyusutan Komputer Kantor {runId}`
37. Pilih Account Function `Accumulated Depreciation`
38. Klik `[Submit]`
39. Verifikasi toast `Error, failed to create account.` tampil sesudah percobaan pertama
40. Klik `[Submit]` sekali lagi
41. Verifikasi toast `Success, account has been created.` tampil sesudah Submit ulang

### Batas jumlah akun tercapai saat Submit
42. Tampilkan Modal Add Account dengan kondisi K4
43. Ketik Account Code `6-4004-PR`
44. Ketik Account Name `Biaya Penyusutan Bangunan Pabrik {runId}`
45. Pilih Account Function `Accumulated Depreciation`
46. Klik `[Submit]`
47. Verifikasi dialog `Cannot Add Account` tampil
48. Verifikasi dialog memuat `You've reached the platform limit of 1000 records. Contact support if you need a higher limit.`
49. Verifikasi dialog memiliki tombol `[OK]`
50. Verifikasi tidak ada toast yang tampil bersama dialog `Cannot Add Account`
51. Klik `[OK]` pada dialog `Cannot Add Account`
52. Verifikasi modal Add Account tetap terbuka dengan Account Code `6-4004-PR` dipertahankan sesudah dialog ditutup

### Koneksi terputus menampilkan toast koneksi tanpa menutup form
53. Tampilkan Modal Add Account dengan kondisi K6
54. Ketik Account Code `6-4006-PR`
55. Ketik Account Name `Biaya Penyusutan Alat Berat {runId}`
56. Pilih Account Function `Accumulated Depreciation`
57. Klik `[Submit]`
58. Verifikasi toast `Connection problem. Please try again.` tampil sesudah `[Submit]` pada form Add saat koneksi terputus
59. Verifikasi modal Add Account tetap terbuka sesudah koneksi terputus
60. Verifikasi input Account Code `6-4006-PR`, Account Name `Biaya Penyusutan Alat Berat {runId}`, dan Account Function `Accumulated Depreciation` dipertahankan sesudah koneksi terputus
