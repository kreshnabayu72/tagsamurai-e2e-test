---
id: TC-FA-FACO-E2E-005-seluruh-daftar-paginasi-select-all
title: "Paginasi, Select All, dan opsi filter atas seluruh daftar akun"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["N-11", "§5#b7", "§9.5#r11", "EB-TBL-7@tabel-account-list", "EB-BLK-2@tabel-account-list", "EB-FLT-1@tabel-account-list"]
smoke: []
dependsOn: []
trace:
  "N-11": [5, 9]
  "§5#b7": [18, 26]
  "§9.5#r11": [3, 8, 62]
  "EB-TBL-7@tabel-account-list": [53, 54]
  "EB-BLK-2@tabel-account-list": [14, 16, 21, 24]
  "EB-FLT-1@tabel-account-list": [3, 4, 36, 46, 62]
anchor: [45, 50, 61]
coverage:
  web: automated
---

# Paginasi, Select All, dan opsi filter atas seluruh daftar akun

## Prerequisites
- Aktor: pengguna Total Control di entitas khusus spec ini.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-005-1: entitas khusus `Entitas Uji Daftar {runId}`, hanya dipakai spec ini, dan tidak berisi akun selain DU-005-2 sampai DU-005-5.
  - DU-005-2: 18 akun, Account Code `P{n}-{runId}`, Account Name `Kas Pusat {n} {runId}`, Account Function `Asset Cost`, Status `Active`, untuk n 1 sampai 18.
  - DU-005-3: akun `PA-{runId}`, Account Name `Penyusutan Gedung {runId}`, Account Function `Accumulated Depreciation`, Status `Inactive`. Satu-satunya akun Inactive di entitas ini; Status-nya diubah menjadi `Active` pada kelompok langkah terakhir.
  - DU-005-4: akun `PB-{runId}`, Account Name `Beban Penyusutan Kantor {runId}`, Account Function `Depreciation Expense`, Status `Active`.
  - DU-005-5: akun `PC-{runId}`, Account Name `Hasil Pelepasan Aset {runId}`, Account Function `Disposal Proceeds`, Status `Active`. Satu-satunya akun ber-Function `Disposal Proceeds` di entitas ini.
  - Jumlah akun di entitas ini 21, sehingga tabel berisi 3 halaman pada ukuran halaman 10.
- Kondisi:
  - Ukuran halaman tabel adalah 10 baris (nilai bawaan).

## Test Steps
### Opsi filter berisi nilai yang ada di tabel
1. Klik ikon Filter
2. Buka dropdown field Function
3. Verifikasi opsi field Function adalah `Accumulated Depreciation`, `Asset Cost`, `Depreciation Expense`, dan `Disposal Proceeds`
4. Verifikasi opsi `Capitalization Offset`, `Gain on Disposal`, dan `Loss on Disposal` tidak tampil karena tidak dipakai akun mana pun
5. Verifikasi opsi `None` tidak tampil di field Function
6. Tutup dropdown field Function
7. Buka dropdown field Active
8. Verifikasi opsi field Active adalah `Active` dan `Inactive`
9. Verifikasi opsi `None` tidak tampil di field Active
10. Tutup dropdown field Active

### Select All dengan Filter aktif memilih seluruh baris yang cocok lintas halaman
11. Pilih `Asset Cost` pada field Function
12. Klik `[Apply]`
13. Centang baris `P1-{runId}`
14. Verifikasi tombol `Select All (18 records)` tampil
15. Klik `Select All (18 records)`
16. Verifikasi tombol berubah menjadi `Unselect All`
17. Klik halaman 2 pada Paginator
18. Verifikasi 8 baris di halaman 2 seluruhnya tercentang
19. Klik halaman 1 pada Paginator
20. Hapus centang baris `P1-{runId}`
21. Verifikasi tombol kembali menjadi `Select All (18 records)`

### N pada Select All mengikuti seluruh baris yang cocok saat Filter dilepas
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Verifikasi tombol `Select All (21 records)` tampil
25. Klik `Select All (21 records)`
26. Verifikasi counter Bulk Action Bar menampilkan `21 Accounts selected`
27. Klik `Unselect All`
28. Klik ikon Filter untuk menutup Filter Panel

### Akun baru menambah opsi filter tanpa muat ulang
29. Klik `[+ Account]`
30. Isi Account Code `PZ-{runId}`
31. Isi Account Name `Laba Pelepasan Aset {runId}`
32. Pilih `Gain on Disposal` pada field Account Function
33. Klik `[Submit]`
34. Klik ikon Filter
35. Buka dropdown field Function
36. Verifikasi opsi `Gain on Disposal` tampil di field Function tanpa memuat ulang halaman
37. Tutup dropdown field Function
38. Klik ikon Filter untuk menutup Filter Panel

### Opsi filter hilang saat akun terakhir pembawa nilainya dihapus
39. Ketik Search `PC-{runId}`, tekan Enter
40. Klik `⋯` pada baris `PC-{runId}` > `Delete`
41. Klik `[Delete]` pada dialog `Delete Account`
42. Klik `(←)` pada kotak Search
43. Klik ikon Filter
44. Buka dropdown field Function
45. Verifikasi opsi `Asset Cost` tampil di field Function
46. Verifikasi opsi `Disposal Proceeds` tidak tampil karena akun terakhir ber-Function itu sudah dihapus
47. Tutup dropdown field Function
48. Klik ikon Filter untuk menutup Filter Panel

### Menghapus baris terakhir di halaman terakhir pindah ke halaman terakhir yang masih ada
49. Klik halaman 3 pada Paginator
50. Verifikasi halaman 3 memuat satu baris, yaitu `PZ-{runId}`
51. Klik `⋯` pada baris `PZ-{runId}` > `Delete`
52. Klik `[Delete]` pada dialog `Delete Account`
53. Verifikasi halaman 2 menjadi halaman aktif karena halaman 3 sudah tidak ada
54. Verifikasi halaman 2 memuat 10 baris

### Opsi filter Active hanya memuat nilai yang ada di tabel
55. Ketik Search `PA-{runId}`, tekan Enter
56. Klik Switch Status pada baris `PA-{runId}`
57. Klik `[Activate]` pada dialog konfirmasi
58. Klik `(←)` pada kotak Search
59. Klik ikon Filter
60. Buka dropdown field Active
61. Verifikasi opsi `Active` tampil di field Active
62. Verifikasi opsi `Inactive` tidak tampil di field Active karena tidak ada lagi akun Inactive di entitas ini
63. Tutup dropdown field Active
64. Klik ikon Filter untuk menutup Filter Panel
