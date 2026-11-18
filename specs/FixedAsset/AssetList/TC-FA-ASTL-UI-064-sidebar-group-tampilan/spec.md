---
id: TC-FA-ASTL-UI-064-sidebar-group-tampilan
title: "Perilaku Sidebar Group"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-14b", "ASTL-LOGIC-14c", "ASTL-LOGIC-14h", "ASTL-LOGIC-14i", "FI-25", "FI-26", "S-43", "S-44", "§4.1g#p1", "§7.1#p1", "EB-SRC-6@sidebar-group"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-14b": 6
  "ASTL-LOGIC-14c": [5, 8, 9]
  "ASTL-LOGIC-14h": 11
  "ASTL-LOGIC-14i": [13, 14]
  "FI-25": [19, 20]
  "FI-26": [11, 13, 14]
  "S-43": 37
  "S-44": [39, 40]
  "§4.1g#p1": [2, 3, 4, 5, 19, 23, 25, 26, 29, 31, 33, 35, 43, 45, 48, 50]
  "§7.1#p1": [39, 40]
  "EB-SRC-6@sidebar-group": [17, 19]
anchor: []
coverage:
  web: automated
---
# Perilaku Sidebar Group

## Prerequisites
- Aktor: Group Manager yang cakupannya hanya group `GA`, `Finance`, dan `Jakarta Selatan Distribution Center` (bukan Total Control).
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Sidebar Group
- Data:
  - DU-064-1: Hierarki group: node akar `All Groups`, leluhur `Kantor Pusat` yang berada di luar cakupan aktor dengan anak `GA` dan `Finance` yang berada dalam cakupan aktor, serta group `Jakarta Selatan Distribution Center` di bawah `All Groups` yang juga dalam cakupan aktor.
  - DU-064-2: Aset pada group GA: Name `Printer Laser - 1`, Asset ID `AST-0031`, Group `GA`, Status `Not Paired Yet`.
  - DU-064-3: Aset pada group Finance: Name `Laptop Dell - 1`, Asset ID `AST-0101`, Group `Finance`, Status `Available`.
- Kondisi:
  - K1: sidebar memuat DU-064-1 dengan hierarki `Kantor Pusat` awalnya terbuka, dan tabel memuat DU-064-2 dan DU-064-3.
  - K2: respons hierarki group belum selesai dimuat.
  - K3: memuat hierarki group gagal karena error server.

## Test Steps

### Struktur panel dan node aktif bawaan
1. Tampilkan Sidebar Group dengan kondisi K1
2. Verifikasi header panel `Groups` tampil
3. Verifikasi header panel tidak memuat tombol Close
4. Verifikasi kotak pencarian berplaceholder `Search group...` dan tombol Expand/Collapse All tampil
5. Verifikasi node akar `All Groups` tampil dan aktif
6. Verifikasi tidak ada aksi Create, Edit, maupun Delete pada sidebar
7. Klik node `GA`
8. Verifikasi tepat satu node aktif, yaitu `GA`
9. Verifikasi tabel memuat `Printer Laser - 1` dan tidak memuat `Laptop Dell - 1`

### Leluhur di luar cakupan
10. Tampilkan Sidebar Group dengan kondisi K1
11. Verifikasi node `Kantor Pusat` tampil greyed-out
12. Klik node `Kantor Pusat`
13. Verifikasi hierarki `Kantor Pusat` tertutup dan `GA` serta `Finance` tidak tampil
14. Verifikasi node aktif tetap `All Groups`

### Pencarian group berjalan saat Enter
15. Tampilkan Sidebar Group dengan kondisi K1
16. Ketik `GA` pada kotak `Search group...` tanpa menekan Enter
17. Verifikasi node `Finance` dan `Jakarta Selatan Distribution Center` masih tampil
18. Tekan Enter
19. Verifikasi node `GA` beserta leluhurnya `Kantor Pusat` tampil
20. Verifikasi node `Finance` dan `Jakarta Selatan Distribution Center` tidak tampil

### Pencarian tanpa hasil dan node aktif yang tersembunyi
21. Tampilkan Sidebar Group dengan kondisi K1
22. Klik node `GA`
23. Verifikasi tabel memuat `Printer Laser - 1`
24. Ketik `Tidak Ada` pada kotak `Search group...`, tekan Enter
25. Verifikasi panel menampilkan ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
26. Verifikasi node aktif tetap `GA` dan tabel tetap memuat `Printer Laser - 1`

### Nama group panjang dan tombol mengambang
27. Tampilkan Sidebar Group dengan kondisi K1
28. Arahkan pointer ke node `Jakarta Selatan Distribution Center`
29. Verifikasi tooltip `Jakarta Selatan Distribution Center` tampil
30. Arahkan pointer ke tombol mengambang di tepi kiri panel
31. Verifikasi tooltip `Collapse Group Tree` tampil
32. Klik tombol mengambang di tepi kiri panel
33. Verifikasi panel tertutup
34. Arahkan pointer ke tombol mengambang di tepi kanan layar
35. Verifikasi tooltip `Open Group Tree` tampil

### Sidebar memuat
36. Tampilkan Sidebar Group dengan kondisi K2
37. Verifikasi hierarki group belum tampil selama memuat, dan panel tidak menampilkan state error maupun `No results found`

### Sidebar gagal memuat
38. Tampilkan Sidebar Group dengan kondisi K3
39. Verifikasi panel menampilkan `Unable to load this data.` dan tombol `[Try Again]`
40. Verifikasi panel tidak menampilkan `No results found`

### Expand/Collapse All membuka dan menutup seluruh node
41. Tampilkan Sidebar Group dengan kondisi K1
42. Klik tombol Expand/Collapse All
43. Verifikasi seluruh node hierarki terbuka, termasuk `GA` dan `Finance` di bawah `Kantor Pusat`
44. Klik tombol Expand/Collapse All
45. Verifikasi seluruh node hierarki tertutup dan `GA` serta `Finance` tidak tampil

### Panel dibuka kembali lewat tombol mengambang
46. Tampilkan Sidebar Group dengan kondisi K1
47. Klik tombol mengambang di tepi kiri panel
48. Verifikasi panel tertutup
49. Klik tombol `Open Group Tree` di tepi kanan layar
50. Verifikasi panel Groups terbuka kembali dan node aktif tetap `All Groups`
