---
id: TC-FA-ASTL-BE-089-konflik-versi-aset
title: "Konflik versi aset dan penolakan 409"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-20a, ASTL-LOGIC-20d, ASTL-LOGIC-20e, ASTL-LOGIC-20b, EC-32, EC-33, EC-34, F-ASTL-10.k1, F-ASTL-11.k1, F-ASTL-16.k3, F-ASTL-17.k1, F-ASTL-18.k2, "409", EB-ERR-4, EB-CON-1, EB-CON-3]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-20a: 5
  ASTL-LOGIC-20d: 6
  ASTL-LOGIC-20e: [16, 17]
  ASTL-LOGIC-20b: [10, 11, 42, 43]
  EC-32: [3, 5, 6]
  EC-33: [10, 11]
  EC-34: [16, 17, 21, 22, 26, 27, 31, 32]
  F-ASTL-10.k1: [16, 17]
  F-ASTL-11.k1: [21, 22]
  F-ASTL-16.k3: [26, 27]
  F-ASTL-17.k1: [11, 31, 32]
  F-ASTL-18.k2: 5
  "409": [5, 10, 16, 21, 26, 31, 42]
  EB-ERR-4: [6, 11]
  EB-CON-1: 5
  EB-CON-3: [36, 38]
anchor: []
---

# Konflik versi aset dan penolakan 409

## Prerequisites
- Aktor: Total Control (Rina), Total Control (Budi).
- Data:
  - DU-089-1: User, admin pertama: Name `Rina Maharani {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-089-2: User, admin kedua: Name `Budi Santoso {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-089-3: Group, group kantor pusat dan cabang dengan Available license dua: Name `Kantor Pusat {runId}`, Group lain `Cabang Medan K {runId}`, Available license Cabang Medan K `2`.
  - DU-089-4: Asset, aset untuk simpan Edit Purchase berebut: Name `Laptop Pro 16 - K1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Date `T0 - 30 hari`, Purchase Cost `18500000.00`.
  - DU-089-5: Asset, aset Unmanaged yang statusnya berubah setelah dialog dibuka: Name `Pompa Air - D1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Status `Unmanaged`, Custody `Available`, Jejak finansial `tidak ada`.
  - DU-089-6: Asset, aset pertama untuk Add Label yang basi: Name `Monitor Dell - L1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Cost `4000000.00`.
  - DU-089-7: Asset, aset kedua untuk Add Label yang basi: Name `Monitor Dell - L2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Cost `4000000.00`.
  - DU-089-8: Asset, aset segar untuk Add Label: Name `Monitor Dell - L3 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Cost `4000000.00`.
  - DU-089-9: Asset, aset berlabel yang akan basi: Name `Printer Laser - R1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Label manual `Prioritas {runId}`, Purchase Cost `6000000.00`.
  - DU-089-10: Asset, aset berlabel yang segar: Name `Printer Laser - R2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Label manual `Prioritas {runId}`, Purchase Cost `6000000.00`.
  - DU-089-11: Asset, aset Unmanaged yang akan basi: Name `Tablet Inventaris - M1 {runId}`, Lifecycle `Active`, Group `Cabang Medan K {runId}`, Status `Unmanaged`, Purchase Cost `2000000.00`.
  - DU-089-12: Asset, aset Unmanaged yang segar: Name `Tablet Inventaris - M2 {runId}`, Lifecycle `Active`, Group `Cabang Medan K {runId}`, Status `Unmanaged`, Purchase Cost `2000000.00`.
  - DU-089-13: Asset, aset Unmanaged yang akan basi untuk Delete: Name `Forklift - X1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Status `Unmanaged`, Custody `Available`, Purchase Cost `8000000.00`.
  - DU-089-14: Asset, aset Unmanaged yang segar untuk Delete: Name `Forklift - X2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Status `Unmanaged`, Custody `Available`, Purchase Cost `8000000.00`.
  - DU-089-15: Asset, aset Unmanaged yang dihapus saat diedit: Name `Meja Rapat - K2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Status `Unmanaged`, Custody `Available`, Purchase Cost `3500000.00`.
  - DU-089-16: Asset, aset Unmanaged yang dihapus dua aktor serentak: Name `Genset Diesel - Z1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Status `Unmanaged`, Custody `Available`.
  - DU-089-17: Input, nilai Purchase Cost yang disimpan pada Edit Purchase: K1 Rina `20000000.00`, K1 Budi `21000000.00`, K1 Rina kedua `22000000.00`, L1 `5000000.00`, L2 `6000000.00`, R1 `7000000.00`, M1 `3000000.00`, X1 `9000000.00`, K2 `4000000.00`.

## Test Steps

### Simpan Edit Purchase kedua atas versi lama ditolak
1. Rina dan Budi masing-masing menyiapkan Edit Purchase atas `Laptop Pro 16 - K1 {runId}` dengan versi data aset yang sama
2. Rina menyimpan Edit Purchase pada `Laptop Pro 16 - K1 {runId}` dengan Purchase Cost `20000000.00`
3. Verifikasi simpan Rina berhasil dan Purchase Cost `Laptop Pro 16 - K1 {runId}` menjadi `20000000.00`
4. Budi menyimpan Edit Purchase pada `Laptop Pro 16 - K1 {runId}` dengan Purchase Cost `21000000.00` memakai versi data aset yang lama
5. Verifikasi simpan Budi ditolak karena data aset berubah sejak dialog dibuka
6. Verifikasi Purchase Cost `Laptop Pro 16 - K1 {runId}` tetap `20000000.00` dan nilai Rina tidak ditimpa

### Status berubah sejak dialog dibuka ditolak sebagai konflik, didahulukan atas syarat Delete
7. Budi menyiapkan Delete Asset Data atas `Pompa Air - D1 {runId}` dengan versi dan status aset saat itu
8. Activity Lock `In Audit` dipasang pada `Pompa Air - D1 {runId}`
9. Budi mengirim Delete Asset Data atas `Pompa Air - D1 {runId}`
10. Verifikasi permintaan ditolak karena versi dan status aset berubah sejak dialog dibuka, bukan karena syarat Delete Asset Data tidak terpenuhi, walau perubahan itu membuat aset terblokir
11. Verifikasi `Pompa Air - D1 {runId}` tetap ada tanpa perubahan apa pun

### Bulk Add Label dengan aset basi ditolak seluruhnya
12. Budi menyiapkan Add Label `Prioritas {runId}` atas `Monitor Dell - L1 {runId}`, `Monitor Dell - L2 {runId}`, dan `Monitor Dell - L3 {runId}` dengan versi data aset saat itu
13. Rina menyimpan Edit Purchase pada `Monitor Dell - L1 {runId}` dengan Purchase Cost `5000000.00`
14. Rina menyimpan Edit Purchase pada `Monitor Dell - L2 {runId}` dengan Purchase Cost `6000000.00`
15. Budi mengirim Add Label `Prioritas {runId}`
16. Verifikasi seluruh seleksi ditolak karena data aset berubah, dan alasan penolakan menyebut `Monitor Dell - L1 {runId}` dan `Monitor Dell - L2 {runId}` sebagai aset penyebab
17. Verifikasi `Monitor Dell - L3 {runId}` tidak berlabel `Prioritas {runId}` sehingga tidak ada aset yang berubah

### Bulk Remove Label dengan aset basi ditolak seluruhnya
18. Budi menyiapkan Remove Label `Prioritas {runId}` atas `Printer Laser - R1 {runId}` dan `Printer Laser - R2 {runId}` dengan versi data aset saat itu
19. Rina menyimpan Edit Purchase pada `Printer Laser - R1 {runId}` dengan Purchase Cost `7000000.00`
20. Budi mengirim Remove Label `Prioritas {runId}`
21. Verifikasi seluruh seleksi ditolak karena data aset berubah, dan alasan penolakan menyebut `Printer Laser - R1 {runId}`
22. Verifikasi `Printer Laser - R2 {runId}` tetap berlabel `Prioritas {runId}` sehingga tidak ada aset yang berubah

### Bulk Manage dengan aset basi ditolak seluruhnya
23. Budi menyiapkan Manage atas `Tablet Inventaris - M1 {runId}` dan `Tablet Inventaris - M2 {runId}` dengan sumber `Available quota` dan versi data aset saat itu
24. Rina menyimpan Edit Purchase pada `Tablet Inventaris - M1 {runId}` dengan Purchase Cost `3000000.00`
25. Budi mengirim Manage atas kedua aset
26. Verifikasi seluruh seleksi ditolak karena data aset berubah, dan alasan penolakan menyebut `Tablet Inventaris - M1 {runId}`
27. Verifikasi `Tablet Inventaris - M2 {runId}` tetap `Unmanaged` dan Available group `Cabang Medan K {runId}` tetap `2` sehingga tidak ada aset yang berubah

### Bulk Delete dengan aset basi ditolak seluruhnya
28. Budi menyiapkan Delete Asset Data atas `Forklift - X1 {runId}` dan `Forklift - X2 {runId}` dengan versi data aset saat itu
29. Rina menyimpan Edit Purchase pada `Forklift - X1 {runId}` dengan Purchase Cost `9000000.00`
30. Budi mengirim Delete Asset Data atas kedua aset
31. Verifikasi seluruh seleksi ditolak karena data aset berubah, dan alasan penolakan menyebut `Forklift - X1 {runId}`
32. Verifikasi `Forklift - X2 {runId}` tetap ada sehingga tidak ada aset yang berubah

### Edit atas aset yang sudah dihapus pihak lain
33. Budi menyiapkan Edit Purchase atas `Meja Rapat - K2 {runId}`
34. Rina menjalankan Delete Asset Data pada `Meja Rapat - K2 {runId}`
35. Budi menyimpan Edit Purchase pada `Meja Rapat - K2 {runId}` dengan Purchase Cost `4000000.00`
36. Verifikasi simpan Budi ditolak karena aset sudah tidak tersedia, dengan pesan `This asset is no longer available.`

### Dua Delete serentak atas aset yang sama
37. Rina dan Budi menjalankan Delete Asset Data pada `Genset Diesel - Z1 {runId}` secara serentak
38. Verifikasi paling banyak satu permintaan berhasil, permintaan lainnya ditolak, dan `Genset Diesel - Z1 {runId}` terhapus tepat satu kali

### Konflik versi didahulukan atas penolakan validasi pada Edit Purchase
39. Budi menyiapkan Edit Purchase atas `Laptop Pro 16 - K1 {runId}` dengan versi data aset saat itu
40. Rina menyimpan Edit Purchase pada `Laptop Pro 16 - K1 {runId}` dengan Purchase Cost `22000000.00`
41. Budi mengirim Edit Purchase pada `Laptop Pro 16 - K1 {runId}` dengan Purchase Date `T0 + 1 hari` memakai versi data aset yang lama
42. Verifikasi permintaan ditolak karena versi data aset berubah sejak dialog dibuka, didahulukan atas penolakan validasi Purchase Date setelah hari ini
43. Verifikasi Purchase Cost `Laptop Pro 16 - K1 {runId}` tetap `22000000.00` dan Purchase Date tetap `T0 - 30 hari` tanpa perubahan apa pun
