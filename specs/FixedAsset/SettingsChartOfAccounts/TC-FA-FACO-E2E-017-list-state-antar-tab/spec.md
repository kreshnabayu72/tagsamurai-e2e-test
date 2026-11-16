---
id: TC-FA-FACO-E2E-017-list-state-antar-tab
title: "State tabel Account List pulih saat pindah tab dan muat ulang halaman"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#b12"]
smoke: []
dependsOn: []
trace:
  "§5#b12": [12, 14, 15, 16, 18, 19, 20, 23, 25]
anchor: [9]
coverage:
  web: automated
---

# State tabel Account List pulih saat pindah tab dan muat ulang halaman

## Prerequisites
- Aktor: pengguna Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-017-1: 9 akun, Account Code `LS{n}-{runId}`, Account Name `0{n} Keadaan {runId}`, Account Function `Asset Cost`, Status `Active`, untuk n 1 sampai 9.
  - DU-017-2: akun `LS10-{runId}`, Account Name `10 Keadaan {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-017-3: akun `LS11-{runId}`, Account Name `11 Keadaan {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-017-4: akun `LS12-{runId}`, Account Name `12 Keadaan {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-017-5: akun `LS13-{runId}`, Account Name `13 Keadaan {runId}`, Account Function `Gain on Disposal`, Status `Active`.
  - Search `Keadaan {runId}` hanya mencocokkan kelima entri di atas (13 akun). Dengan Filter Function `Asset Cost`, hasilnya 12 akun, sehingga tabel berisi 2 halaman pada ukuran halaman 10.
- Kondisi:
  - Ukuran halaman tabel adalah 10 baris (nilai bawaan).

## Test Steps
### Menyetel Search, Filter, Sort, dan paginasi
1. Ketik Search `Keadaan {runId}`, tekan Enter
2. Klik ikon Filter
3. Pilih `Asset Cost` pada field Function
4. Klik `[Apply]`
5. Klik ikon Filter untuk menutup Filter Panel
6. Klik header kolom Account Name (klik pertama)
7. Klik header kolom Account Name (klik kedua)
8. Klik halaman 2 pada Paginator
9. Verifikasi halaman 2 memuat baris `LS2-{runId}` lalu `LS1-{runId}`, urut menurun menurut Account Name, dan tidak memuat baris `LS13-{runId}`

### Pindah ke tab lain lalu kembali memulihkan state tabel
10. Klik tab `Asset Class`
11. Klik tab `Chart of Accounts`
12. Verifikasi kotak Search berisi `Keadaan {runId}`
13. Klik ikon Filter
14. Verifikasi nilai `Asset Cost` pada field Function di Filter Panel masih terpilih sesudah kembali dari tab lain
15. Verifikasi halaman 2 menjadi halaman aktif pada Paginator
16. Verifikasi halaman 2 memuat baris `LS2-{runId}` lalu `LS1-{runId}`, urut menurun menurut Account Name

### Muat ulang halaman mempertahankan tab aktif dan state tabel
17. Muat ulang halaman
18. Verifikasi tab `Chart of Accounts` tetap menjadi tab aktif
19. Verifikasi kotak Search berisi `Keadaan {runId}` dan halaman 2 menjadi halaman aktif
20. Verifikasi halaman 2 memuat tepat dua baris, yaitu `LS2-{runId}` lalu `LS1-{runId}`, urut menurun menurut Account Name, karena Filter Function `Asset Cost` masih berlaku dan `LS13-{runId}` tidak ikut tampil

### Meninggalkan halaman mereset state tabel
21. Klik menu lain di sidebar, di luar halaman Accounting
22. Buka kembali Settings > Accounting > Chart of Accounts lewat menu sidebar
23. Verifikasi kotak Search kosong dan halaman 1 menjadi halaman aktif
24. Ketik Search `Keadaan {runId}`, tekan Enter
25. Verifikasi baris `LS13-{runId}` tampil di halaman 1 karena Filter Function dan Sort Account Name sudah direset, dengan urutan default Account Code
