---
id: TC-FA-FASVC-E2E-046-hak-dicabut-saat-dialog-dep-role-permission
title: "Hak Kelola Dicabut Saat Dialog Terbuka: Toast Error, Isian Terjaga, Tree Dimuat Ulang"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [V-FASVC-39, EC-FASVC-16, F-FASVC-02.k7, EB-AKS-6]
smoke: []
dependsOn: ["Role Permission: pengaturan role dan cakupan", "Group: pohon Group dan master Group"]
trace:
  V-FASVC-39: [8, 9, 10, 13, 24, 25, 30, 31, 36, 37]
  EC-FASVC-16: [8, 9]
  F-FASVC-02.k7: [8, 9, 13]
  EB-AKS-6: [8, 19, 24, 30, 36]
anchor: [3, 12, 17]
coverage:
  web: automated
---
# Hak Kelola Dicabut Saat Dialog Terbuka: Toast Error, Isian Terjaga, Tree Dimuat Ulang

## Prerequisites
- Aktor: Asset Admin `Fajar Hak {runId}` (Role Transaksi Maintenance Routine, cakupan Group `Cabang Tegal {runId}`, `Cabang Brebes {runId}`, `Cabang Slawi {runId}`, `Cabang Pekalongan {runId}`, dan `Cabang Batang {runId}`) menguji layarnya; akunnya aktif dan kredensialnya disediakan fase 2. Admin `Dimas Pratama {runId}` (Total Control, cakupan seluruh Group) mengubah cakupan Group Asset Admin dari sesinya sendiri.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-046-1: Group `Cabang Tegal {runId}`, parent root pohon Group entitas aktor, dilepas dari cakupan Asset Admin saat dialog Edit terbuka, tanpa aset dan user lain.
  - DU-046-2: Group `Cabang Brebes {runId}`, parent root pohon Group entitas aktor, dilepas dari cakupan Asset Admin saat dialog Inactivate terbuka, tanpa aset dan user lain.
  - DU-046-3: Group `Cabang Slawi {runId}`, parent root pohon Group entitas aktor, dilepas dari cakupan Asset Admin saat dialog Activate terbuka, tanpa aset dan user lain.
  - DU-046-4: Group `Cabang Pekalongan {runId}`, parent root pohon Group entitas aktor, dilepas dari cakupan Asset Admin saat dialog Delete terbuka, tanpa aset dan user lain.
  - DU-046-5: Group `Cabang Batang {runId}`, parent root pohon Group entitas aktor, tetap dalam cakupan Asset Admin, tanpa aset dan user lain.
  - DU-046-6: Service Center `Servis Pompa Tegal {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Tegal {runId}` dan `Cabang Batang {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Tegal`, Company phone nomor `81234500461`, Company email `servis@pompategal.example`, Notes `Teknisi tersedia hari kerja {runId}`, Usage `0`, Status `Active`.
  - DU-046-7: Service Center `Servis Pompa Brebes {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Brebes {runId}` dan `Cabang Batang {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Brebes`, Company phone nomor `81234500462`, Company email `servis@pompabrebes.example`, Notes `Teknisi tersedia hari kerja {runId}`, Usage `0`, Status `Active`.
  - DU-046-8: Service Center `Servis Pompa Slawi {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Slawi {runId}` dan `Cabang Batang {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Slawi`, Company phone nomor `81234500463`, Company email `servis@pompaslawi.example`, Notes `Teknisi tersedia hari kerja {runId}`, Usage `0`, Status `Inactive`.
  - DU-046-9: Service Center `Servis Pompa Pekalongan {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Pekalongan {runId}` dan `Cabang Batang {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Pekalongan`, Company phone nomor `81234500464`, Company email `servis@pompapekalongan.example`, Notes `Teknisi tersedia hari kerja {runId}`, Usage `0`, Status `Active`.
  - DU-046-10: Notes `Teknisi tersedia akhir pekan {runId}`, nilai yang diketik pada dialog Edit `Servis Pompa Tegal {runId}` lalu ditolak saat `[Save]`.
  - DU-046-11: User Asset Admin `Fajar Hak {runId}`, Role Transaksi Maintenance Routine, cakupan Group `Cabang Tegal {runId}`, `Cabang Brebes {runId}`, `Cabang Slawi {runId}`, `Cabang Pekalongan {runId}`, dan `Cabang Batang {runId}`.
  - DU-046-12: User Admin `Dimas Pratama {runId}`, role Total Control, cakupan seluruh Group.

## Test Steps

### Edit ditolak saat hak kelola dicabut: toast error, isian terjaga, dan tree Available to dimuat ulang
1. Ketik Search `Servis Pompa Tegal {runId}`, tekan Enter
2. Klik `⋯` pada baris `Servis Pompa Tegal {runId}`
3. Verifikasi menu `⋯` memuat `Edit`
4. Klik `Edit`
5. Ganti isi field Notes dengan `Teknisi tersedia akhir pekan {runId}`
6. Admin `Dimas Pratama {runId}` mengubah cakupan `Fajar Hak {runId}` dengan melepas Group `Cabang Tegal {runId}` dari cakupan tersebut
7. Klik `[Save]`
8. Verifikasi toast error memuat pesan `You don't have permission to do this.`
9. Verifikasi dialog `Edit Service Center` tetap terbuka setelah `[Save]` ditolak karena hak dicabut
10. Verifikasi field Notes tetap berisi `Teknisi tersedia akhir pekan {runId}`
11. Klik field Available to untuk membuka tree
12. Verifikasi tree Available to menampilkan `Cabang Batang {runId}`
13. Verifikasi tree Available to tidak menampilkan `Cabang Tegal {runId}`
14. Klik `✕` pada form
15. Klik `[Leave]` pada dialog `Unsaved Changes`
16. Ganti isi kotak Search dengan `Servis Pompa Tegal {runId}`, tekan Enter
17. Verifikasi baris `Servis Pompa Tegal {runId}` tampil
18. Klik `⋯` pada baris `Servis Pompa Tegal {runId}`
19. Verifikasi menu `⋯` hanya memuat `Detail`

### Inactivate ditolak saat hak kelola dicabut: toast error dan status tidak berubah
20. Ganti isi kotak Search dengan `Servis Pompa Brebes {runId}`, tekan Enter
21. Klik `⋯` pada baris `Servis Pompa Brebes {runId}`, lalu klik `Inactivate`
22. Admin `Dimas Pratama {runId}` mengubah cakupan `Fajar Hak {runId}` dengan melepas Group `Cabang Brebes {runId}` dari cakupan tersebut
23. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
24. Verifikasi toast error memuat pesan `You don't have permission to do this.`
25. Verifikasi Status baris `Servis Pompa Brebes {runId}` tetap `Active`

### Activate ditolak saat hak kelola dicabut: toast error dan status tidak berubah
26. Ganti isi kotak Search dengan `Servis Pompa Slawi {runId}`, tekan Enter
27. Klik `⋯` pada baris `Servis Pompa Slawi {runId}`, lalu klik `Activate`
28. Admin `Dimas Pratama {runId}` mengubah cakupan `Fajar Hak {runId}` dengan melepas Group `Cabang Slawi {runId}` dari cakupan tersebut
29. Klik `[Activate]` pada dialog `Activate Service Center`
30. Verifikasi toast error memuat pesan `You don't have permission to do this.`
31. Verifikasi Status baris `Servis Pompa Slawi {runId}` tetap `Inactive`

### Delete ditolak saat hak kelola dicabut: toast error dan Service Center tidak terhapus
32. Ganti isi kotak Search dengan `Servis Pompa Pekalongan {runId}`, tekan Enter
33. Klik `⋯` pada baris `Servis Pompa Pekalongan {runId}`, lalu klik `Delete`
34. Admin `Dimas Pratama {runId}` mengubah cakupan `Fajar Hak {runId}` dengan melepas Group `Cabang Pekalongan {runId}` dari cakupan tersebut
35. Klik `[Delete]` pada dialog `Delete Service Center`
36. Verifikasi toast error memuat pesan `You don't have permission to do this.`
37. Verifikasi baris `Servis Pompa Pekalongan {runId}` tetap tampil di tabel
