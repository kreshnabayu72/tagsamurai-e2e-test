---
id: TC-FA-FACO-E2E-018-form-kotor-muat-ulang-navigasi
title: "Form Add dan Edit Account yang kotor saat muat ulang atau pindah menu"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-FRM-2@form-add-account", "EB-FRM-2@form-edit-account"]
smoke: []
dependsOn: []
trace:
  "EB-FRM-2@form-add-account": [5, 7, 9, 11, 13, 17, 22, 27]
  "EB-FRM-2@form-edit-account": [32, 34, 36, 38, 41, 44, 48]
anchor: [20, 26, 47]
coverage:
  web: automated
---

# Form Add dan Edit Account yang kotor saat muat ulang atau pindah menu

## Prerequisites
- Aktor: pengguna Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-018-1: akun `FM1-{runId}`, Account Name `Form Awal {runId}`, Account Function `Asset Cost`, Status `Active`. Nilai Account Name yang diketik lalu tidak disimpan: `Form Ubah {runId}`.
  - DU-018-2: isian form Add Account yang diketik lalu tidak disimpan: Account Code `FM2-{runId}` dan Account Name `Form Kotor {runId}`. Tidak ada akun yang tersimpan dari isian ini.

## Test Steps
### Add Account kotor: muat ulang memunculkan konfirmasi bawaan browser
1. Klik `[+ Account]`
2. Isi Account Code `FM2-{runId}`
3. Isi Account Name `Form Kotor {runId}`
4. Muat ulang halaman
5. Verifikasi konfirmasi bawaan browser untuk meninggalkan halaman muncul karena form Add Account kotor
6. Pilih tetap di halaman pada konfirmasi bawaan browser
7. Verifikasi form Add Account masih terbuka dengan Account Code `FM2-{runId}` dan Account Name `Form Kotor {runId}`

### Add Account kotor: pindah menu atau Back memunculkan dialog Unsaved Changes
8. Klik menu lain di sidebar, di luar halaman Accounting
9. Verifikasi dialog dengan teks `You have unsaved changes. Are you sure you want to leave?` tampil dengan tombol `[Cancel]` dan `[Leave]` saat berpindah menu dari form Add Account yang kotor
10. Klik `[Cancel]`
11. Verifikasi form Add Account masih terbuka dengan Account Code `FM2-{runId}` dan Account Name `Form Kotor {runId}`
12. Klik tombol Back browser
13. Verifikasi dialog dengan teks `You have unsaved changes. Are you sure you want to leave?` tampil dengan tombol `[Cancel]` dan `[Leave]` saat Back browser ditekan dari form Add Account yang kotor
14. Klik `[Cancel]`
15. Klik menu lain di sidebar, di luar halaman Accounting
16. Klik `[Leave]`
17. Verifikasi form Add Account tertutup dan halaman menu tujuan tampil
18. Buka kembali Settings > Accounting > Chart of Accounts lewat menu sidebar
19. Ketik Search `FM1-{runId}`, tekan Enter
20. Verifikasi baris `FM1-{runId}` tampil di tabel
21. Ganti isi kotak Search dengan `FM2-{runId}`, tekan Enter
22. Verifikasi `No results found` tampil karena akun `FM2-{runId}` tidak tersimpan sesudah `[Leave]`

### Add Account bersih: muat ulang tanpa konfirmasi
23. Klik `(←)` pada kotak Search
24. Klik `[+ Account]`
25. Muat ulang halaman
26. Verifikasi header kolom `Account Code` tampil sesudah halaman termuat ulang
27. Verifikasi tidak ada konfirmasi bawaan browser yang muncul saat memuat ulang dengan form Add Account bersih

### Edit Account kotor: muat ulang dan pindah menu
28. Ketik Search `FM1-{runId}`, tekan Enter
29. Klik `⋯` pada baris `FM1-{runId}` > `Edit`
30. Ganti isi Account Name dengan `Form Ubah {runId}`
31. Muat ulang halaman
32. Verifikasi konfirmasi bawaan browser untuk meninggalkan halaman muncul karena form Edit Account kotor
33. Pilih tetap di halaman pada konfirmasi bawaan browser
34. Verifikasi form Edit Account masih terbuka dengan Account Name `Form Ubah {runId}`
35. Klik menu lain di sidebar, di luar halaman Accounting
36. Verifikasi dialog dengan teks `You have unsaved changes. Are you sure you want to leave?` tampil dengan tombol `[Cancel]` dan `[Leave]` saat berpindah menu dari form Edit Account yang kotor
37. Klik `[Cancel]`
38. Verifikasi form Edit Account masih terbuka dengan Account Name `Form Ubah {runId}`
39. Klik menu lain di sidebar, di luar halaman Accounting
40. Klik `[Leave]`
41. Verifikasi form Edit Account tertutup dan halaman menu tujuan tampil
42. Buka kembali Settings > Accounting > Chart of Accounts lewat menu sidebar
43. Ketik Search `FM1-{runId}`, tekan Enter
44. Verifikasi baris `FM1-{runId}` tampil dengan Account Name `Form Awal {runId}` karena perubahan tidak tersimpan sesudah `[Leave]`

### Edit Account bersih: muat ulang tanpa konfirmasi
45. Klik `⋯` pada baris `FM1-{runId}` > `Edit`
46. Muat ulang halaman
47. Verifikasi header kolom `Account Code` tampil sesudah halaman termuat ulang dari form Edit Account
48. Verifikasi tidak ada konfirmasi bawaan browser yang muncul saat memuat ulang dengan form Edit Account bersih
