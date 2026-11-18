---
id: TC-FA-ASSIGN-E2E-007-transactions-setup-column-tersimpan
title: "Konfigurasi kolom tab Transactions tersimpan di akun"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r9", "EB-KOL-2@tabel-transactions", "EB-SRC-5@tabel-transactions"]
smoke: []
dependsOn: []
trace:
  "§5#r9": 31
  "EB-KOL-2@tabel-transactions": [4, 6, 10, 13, 15, 16, 17, 19, 21]
  "EB-SRC-5@tabel-transactions": [24, 28]
anchor: [1]
coverage:
  web: automated
---

# Konfigurasi kolom tab Transactions tersimpan di akun

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`; akun `Agus Prasetyo {runId}` dipakai sebagai pengguna lain.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-007-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-007-2: Group `Head Office {runId}`.
  - DU-007-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pengaju ASG DU-007-6 dan DU-007-7, tidak pernah mengubah konfigurasi kolom, dan akunnya aktif dengan kredensial yang disediakan fase 2.
  - DU-007-4: User `Budi Santoso {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-007-5: Division `Gudang Pusat {runId}` dengan PIC aktif `Dewi Anggraini {runId}`, karyawan aktif ber-akun login tanpa akses menu Assignment.
  - DU-007-6: ASG berstatus `Waiting for Approval` untuk Assignee DU-007-4, aset `Proyektor BenQ MH550 {runId}`, Total Asset `1`.
  - DU-007-7: ASG berstatus `Assigned` untuk Assignee Division `Gudang Pusat {runId}`, aset `Rak Besi Lion {runId}`, Total Asset `1`.

## Test Steps

### Ubah konfigurasi kolom
1. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Transaction ID`, `Status`, `Group`, `Assignee`, `Assignee Type`, `Total Asset`, `Requested By`, `Request Date`, `Last Updated`
2. Klik header kolom `Actions`
3. Hilangkan centang kolom `Requested By` pada panel Column Visibility
4. Verifikasi kolom `Requested By` tidak tampil di tabel
5. Pindahkan kolom `Assignee Type` ke posisi tepat sebelum kolom `Status` pada panel Column Visibility
6. Verifikasi kolom `Assignee Type` tampil tepat sebelum kolom `Status`
7. Klik `Setup Column...` pada panel Column Visibility
8. Klik ikon pin pada kolom `Transaction ID` di modal Setup Column
9. Klik `[Save]`
10. Verifikasi kolom `Transaction ID` tetap tampil di kiri saat tabel digulir ke kanan
11. Ketik Search `Agus Prasetyo {runId}`, tekan Enter

### Konfigurasi bertahan sesudah muat ulang dan login ulang
12. Muat ulang halaman
13. Verifikasi kolom `Requested By` tetap tidak tampil dan `Assignee Type` tetap tepat sebelum `Status` sesudah muat ulang
14. Keluar dari akun lalu masuk lagi sebagai `Hendra Kusuma {runId}`
15. Verifikasi kolom `Requested By` tetap tidak tampil dan `Assignee Type` tetap tepat sebelum `Status` sesudah masuk lagi
16. Verifikasi kolom `Transaction ID` masih terpin sesudah masuk lagi
17. Verifikasi kotak Search kosong sesudah masuk lagi karena Search tidak tersimpan di akun
18. Masuk sebagai `Hendra Kusuma {runId}` di browser lain
19. Verifikasi kolom `Requested By` tidak tampil dan `Assignee Type` tepat sebelum `Status` di browser lain
20. Masuk sebagai `Agus Prasetyo {runId}`
21. Verifikasi header kolom tampil berurutan dengan konfigurasi bawaan: `Transaction ID`, `Status`, `Group`, `Assignee`, `Assignee Type`, `Total Asset`, `Requested By`, `Request Date`, `Last Updated`

### Kolom yang disembunyikan tidak dicari
22. Masuk sebagai `Hendra Kusuma {runId}`
23. Ganti isi kotak search dengan `Agus Prasetyo {runId}`, tekan Enter
24. Verifikasi pesan `No results found` tampil karena kolom `Requested By` yang disembunyikan tidak ikut dicari
25. Klik header kolom `Actions`
26. Centang kolom `Requested By` pada panel Column Visibility
27. Ganti isi kotak search dengan `Agus Prasetyo {runId}`, tekan Enter
28. Verifikasi baris `Budi S` dan `Gudang Pusat {runId}` tampil karena kolom `Requested By` ditampilkan kembali

### Setidaknya satu kolom tetap tampil
29. Klik header kolom `Actions`
30. Hilangkan centang semua kolom kecuali `Status` pada panel Column Visibility
31. Verifikasi centang kolom `Status` dinonaktifkan dengan tooltip `At least one column must remain visible.`
