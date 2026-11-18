---
id: TC-FA-ASTL-BE-081-otorisasi-aksi-tulis
title: "Otorisasi aksi tulis per role"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-17r, ASTL-LOGIC-19f, ASTL-LOGIC-20o, "§9.3#r1", "§9.3#r2", "§9.3#r4", "§9.3#r5", "§9.3#r6", "§9.3#p1", "EB-AKS-3@add-label", "EB-AKS-3@remove-label", "EB-AKS-3@manage-asset", "EB-AKS-3@delete-asset-data", "EB-AKS-3@edit-purchase"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-17r: [30, 32, 34, 36, 38]
  ASTL-LOGIC-19f: [40, 41, 55]
  ASTL-LOGIC-20o: [43, 45, 47, 58, 60]
  "§9.3#r1": [2, 4, 6]
  "§9.3#r2": [8, 10, 12, 14, 16]
  "§9.3#r4": [18, 20, 49, 51, 53]
  "§9.3#r5": [24, 28]
  "§9.3#r6": [30, 32, 34, 36, 38]
  "§9.3#p1": [6, 12, 14, 20, 22, 26, 36]
  "EB-AKS-3@add-label": [12, 16]
  "EB-AKS-3@remove-label": 14
  "EB-AKS-3@manage-asset": [22, 62]
  "EB-AKS-3@delete-asset-data": [36, 38]
  "EB-AKS-3@edit-purchase": 26
anchor: []
---

# Otorisasi aksi tulis per role

## Prerequisites
- Aktor: Total Control (Hendra), Group Manager (Dewi), pemegang Manage asset & TAG (Sari, Budi, Tono), pemegang Manage purchase (Rina), Read Only (Wulan).
- Data:
  - DU-081-1: User, total Control: Name `Hendra Saputra {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-081-2: User, group Manager: Name `Dewi Lestari {runId}`, Role `Group Manager`, Cakupan `IT {runId}`.
  - DU-081-3: User, manage asset & TAG (Read + Update): Name `Sari Wulandari {runId}`, Role `Manage asset & TAG (Read + Update)`, Cakupan `Update pada IT {runId}, Read pada GA {runId}`.
  - DU-081-4: User, manage asset & TAG (Read): Name `Budi Santoso {runId}`, Role `Manage asset & TAG (Read)`, Cakupan `Read pada IT {runId}`.
  - DU-081-5: User, manage asset & TAG (Read + Delete): Name `Tono Hartono {runId}`, Role `Manage asset & TAG (Read + Delete)`, Cakupan `IT {runId}`.
  - DU-081-6: User, manage purchase (Update): Name `Rina Maharani {runId}`, Role `Manage purchase (Update)`, Cakupan `IT {runId}`.
  - DU-081-7: User, read Only: Name `Wulan Anggraini {runId}`, Role `Read Only`, Cakupan `Seluruh client`.
  - DU-081-8: Group, tiga group tanpa induk: Name `IT {runId}`, Group kedua `GA {runId}`, Group ketiga `Cabang Bandung {runId}`.
  - DU-081-9: Asset, aset IT tanpa label: Name `Laptop Pro 16 - 1 {runId}`, Lifecycle `Active`, Group `IT {runId}`.
  - DU-081-10: Asset, aset IT berlabel manual: Name `Laptop Pro 16 - 2 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Label manual `Prioritas {runId}`.
  - DU-081-11: Asset, aset di GA yang hanya dapat dibaca Sari: Name `Meja Rapat - 1 {runId}`, Lifecycle `Active`, Group `GA {runId}`.
  - DU-081-12: Asset, aset di luar cakupan Sari: Name `Proyektor X2 - 1 {runId}`, Lifecycle `Active`, Group `Cabang Bandung {runId}`.
  - DU-081-13: Asset, aset Unmanaged untuk Manage: Name `Tablet Inventaris - M1 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Status `Unmanaged`; Available license group `IT {runId}` cukup (DU-081-26).
  - DU-081-14: Asset, aset untuk Edit Purchase: Name `Forklift - E1 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Purchase Cost `8000000.00`.
  - DU-081-15: Asset, aset berjejak Posted: Name `Pompa Air - P1 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Purchase Cost `18500000.00`, Jejak finansial `Penyusutan Posted`.
  - DU-081-16: Asset, aset Unmanaged yang dihapus Tono: Name `Kamera CCTV - D1 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Status `Unmanaged`, Custody `Available`.
  - DU-081-17: Asset, aset Unmanaged yang dihapus Dewi: Name `Kamera CCTV - D2 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Status `Unmanaged`, Custody `Available`.
  - DU-081-18: Asset, aset Unmanaged yang dihapus Hendra: Name `Kamera CCTV - D3 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Status `Unmanaged`, Custody `Available`.
  - DU-081-19: Asset, aset Unmanaged yang tidak boleh dihapus aktor tanpa hak: Name `Kamera CCTV - D5 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Status `Unmanaged`, Custody `Available`.
  - DU-081-21: Asset, aset Disposed: Name `Genset Lama - X1 {runId}`, Lifecycle `Disposed`, Group `IT {runId}`.
  - DU-081-22: Group, anak dari `IT {runId}`: Name `IT Support {runId}`.
  - DU-081-23: Asset, aset di group anak: Name `Headset - C1 {runId}`, Lifecycle `Active`, Group `IT Support {runId}`.
  - DU-081-24: Asset, aset kedua di group anak: Name `Headset - C2 {runId}`, Lifecycle `Active`, Group `IT Support {runId}`.
  - DU-081-25: Asset, aset Unmanaged untuk kontrol positif Manage: Name `Tablet Inventaris - M2 {runId}`, Lifecycle `Active`, Group `IT {runId}`, Status `Unmanaged`.
  - DU-081-26: Input, label kedua `Cadangan {runId}`; Available license group `IT {runId}` cukup (minimal 2 slot) sehingga penolakan Manage hanya bisa karena hak, bukan kuota.

## Test Steps

### Melihat daftar dan Download hanya untuk aset dalam cakupan
1. Sari meminta daftar aset
2. Verifikasi daftar memuat `Laptop Pro 16 - 1 {runId}` di `IT {runId}` dan `Meja Rapat - 1 {runId}` di `GA {runId}` karena Sari berhak membaca kedua group, dan tidak memuat `Proyektor X2 - 1 {runId}`
3. Sari mengunduh daftar aset
4. Verifikasi berkas Download tidak memuat `Proyektor X2 - 1 {runId}`
5. Sari meminta akses langsung ke aset `Proyektor X2 - 1 {runId}`
6. Verifikasi akses ditolak karena aset di luar cakupan dan tidak ada data aset yang dikirim

### Bulk Add Label dan Remove Label hanya untuk pemegang Update
7. Sari menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - 1 {runId}`
8. Verifikasi permintaan diterima dan `Laptop Pro 16 - 1 {runId}` berlabel `Prioritas {runId}`
9. Sari mencabut label `Prioritas {runId}` dari `Laptop Pro 16 - 2 {runId}`
10. Verifikasi permintaan diterima dan `Laptop Pro 16 - 2 {runId}` tidak lagi berlabel `Prioritas {runId}`
11. Budi menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - 2 {runId}`
12. Verifikasi permintaan ditolak karena tidak berhak, walau permintaan dikirim langsung tanpa lewat UI, dan `Laptop Pro 16 - 2 {runId}` tidak berubah
13. Wulan mencabut label `Prioritas {runId}` dari `Laptop Pro 16 - 1 {runId}`
14. Verifikasi permintaan ditolak karena tidak berhak, walau permintaan dikirim langsung tanpa lewat UI, dan `Laptop Pro 16 - 1 {runId}` tetap berlabel `Prioritas {runId}`
15. Tono menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - 2 {runId}`
16. Verifikasi permintaan ditolak karena tidak berhak, walau permintaan dikirim langsung tanpa lewat UI karena Tono hanya memegang Delete, dan `Laptop Pro 16 - 2 {runId}` tidak berubah

### Print Label hanya untuk pemegang Update
17. Sari mencetak label untuk `Laptop Pro 16 - 1 {runId}`
18. Verifikasi permintaan Print Label diterima karena Sari pemegang Update dan aset dalam cakupan
19. Budi mencetak label untuk `Laptop Pro 16 - 1 {runId}`
20. Verifikasi permintaan Print Label ditolak karena tidak berhak, walau permintaan dikirim langsung tanpa lewat UI karena Budi bukan pemegang Update

### Manage hanya untuk pemegang Update
21. Budi meng-Manage aset `Tablet Inventaris - M1 {runId}` dengan sumber `Available quota`
22. Verifikasi permintaan ditolak karena tidak berhak, walau permintaan dikirim langsung tanpa lewat UI, dan `Tablet Inventaris - M1 {runId}` tetap `Unmanaged`

### Edit Purchase hanya untuk pemegang Manage purchase dengan Update
23. Rina menyimpan Edit Purchase pada `Forklift - E1 {runId}` dengan Purchase Cost `12500000.00`
24. Verifikasi permintaan diterima dan Purchase Cost `Forklift - E1 {runId}` menjadi `12500000.00`
25. Sari menyimpan Edit Purchase pada `Forklift - E1 {runId}` dengan Purchase Cost `14000000.00`
26. Verifikasi permintaan ditolak karena tidak berhak, walau permintaan dikirim langsung tanpa lewat UI karena Sari tidak memegang Manage purchase, dan Purchase Cost `Forklift - E1 {runId}` tetap `12500000.00`
27. Rina menyimpan Edit Purchase pada `Pompa Air - P1 {runId}` dengan Purchase Cost `13000000.00`
28. Verifikasi Edit Purchase oleh pemegang Manage purchase tetap ditolak karena `Pompa Air - P1 {runId}` berjejak Posted, dan Purchase Cost tetap `18500000.00`

### Delete Asset Data hanya untuk Total Control, Group Manager, dan pemegang Delete
29. Hendra menjalankan Delete Asset Data pada `Kamera CCTV - D3 {runId}`
30. Verifikasi penghapusan diterima karena Hendra Total Control
31. Dewi menjalankan Delete Asset Data pada `Kamera CCTV - D2 {runId}`
32. Verifikasi penghapusan diterima karena Dewi Group Manager untuk `IT {runId}`
33. Tono menjalankan Delete Asset Data pada `Kamera CCTV - D1 {runId}`
34. Verifikasi penghapusan diterima karena Tono memegang Delete pada Manage asset & TAG
35. Sari menjalankan Delete Asset Data pada `Kamera CCTV - D5 {runId}`
36. Verifikasi permintaan ditolak karena tidak berhak, walau permintaan dikirim langsung tanpa lewat UI karena Sari hanya pemegang Update, dan `Kamera CCTV - D5 {runId}` tetap ada
37. Wulan menjalankan Delete Asset Data pada `Kamera CCTV - D5 {runId}`
38. Verifikasi permintaan ditolak karena tidak berhak, walau permintaan dikirim langsung tanpa lewat UI karena Wulan hanya Read Only, dan `Kamera CCTV - D5 {runId}` tetap ada

### Seleksi Bulk yang sebagian di luar hak ditolak seluruhnya
39. Sari menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - 2 {runId}` dan `Meja Rapat - 1 {runId}` sekaligus
40. Verifikasi seluruh seleksi ditolak tanpa penyaringan karena Sari tidak memegang Update pada group `GA {runId}` tempat `Meja Rapat - 1 {runId}` berada
41. Verifikasi `Laptop Pro 16 - 2 {runId}` tidak berlabel `Prioritas {runId}` sehingga tidak ada aset yang berubah

### Seleksi Bulk dengan aset di luar cakupan atau terhapus ditolak seluruhnya
42. Sari menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - 2 {runId}` dan `Proyektor X2 - 1 {runId}` sekaligus
43. Verifikasi seluruh seleksi ditolak dengan pesan `You don't have permission to do this.` karena `Proyektor X2 - 1 {runId}` di luar cakupan, dan `Laptop Pro 16 - 2 {runId}` tidak berubah
44. Sari menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - 2 {runId}` dan aset `Kamera CCTV - D3 {runId}` yang sudah dihapus permanen
45. Verifikasi seluruh seleksi ditolak dengan pesan `This asset is no longer available.` dan `Laptop Pro 16 - 2 {runId}` tidak berubah
46. Sari menambahkan label `Prioritas {runId}` pada `Proyektor X2 - 1 {runId}` dan aset `Kamera CCTV - D3 {runId}` yang sudah dihapus permanen
47. Verifikasi seluruh seleksi ditolak dengan pesan `You don't have permission to do this.`, karena penyebab di luar cakupan didahulukan atas aset terhapus

### Print Label ditolak untuk aset di luar cakupan, Disposed, dan Unmanaged
48. Sari mencetak label untuk `Proyektor X2 - 1 {runId}`
49. Verifikasi permintaan Print Label ditolak karena aset di luar cakupan group tempat Sari memegang Update, dan tidak ada data aset yang dikirim
50. Sari mencetak label untuk `Genset Lama - X1 {runId}`
51. Verifikasi permintaan Print Label ditolak karena aset Disposed
52. Sari mencetak label untuk `Tablet Inventaris - M1 {runId}`
53. Verifikasi permintaan Print Label ditolak karena aset Unmanaged, dan `Tablet Inventaris - M1 {runId}` tetap `Unmanaged`

### Hak Update berlaku pada group beserta descendant untuk seleksi Bulk
54. Sari menambahkan label `Prioritas {runId}` pada `Headset - C1 {runId}` dan `Headset - C2 {runId}` sekaligus
55. Verifikasi seluruh seleksi diterima karena kedua aset berada di `IT Support {runId}`, descendant dari `IT {runId}` tempat Sari memegang Update, dan keduanya berlabel `Prioritas {runId}`

### Urutan penolakan 403 atas 409 dan 404 atas 409
56. Hendra menambahkan label `Cadangan {runId}` pada `Laptop Pro 16 - 2 {runId}` sehingga versi data aset berubah
57. Sari menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - 2 {runId}` dan `Proyektor X2 - 1 {runId}` sekaligus, memakai versi data `Laptop Pro 16 - 2 {runId}` sebelum perubahan Hendra
58. Verifikasi seluruh seleksi ditolak dengan pesan `You don't have permission to do this.` karena `Proyektor X2 - 1 {runId}` di luar cakupan didahulukan atas konflik versi, dan `Laptop Pro 16 - 2 {runId}` tidak berlabel `Prioritas {runId}`
59. Sari menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - 2 {runId}` dan `Kamera CCTV - D3 {runId}` sekaligus, memakai versi data `Laptop Pro 16 - 2 {runId}` sebelum perubahan Hendra
60. Verifikasi seluruh seleksi ditolak dengan pesan `This asset is no longer available.` karena `Kamera CCTV - D3 {runId}` sudah dihapus permanen didahulukan atas konflik versi, dan `Laptop Pro 16 - 2 {runId}` tidak berlabel `Prioritas {runId}`

### Manage oleh pemegang Update diterima
61. Sari meng-Manage aset `Tablet Inventaris - M2 {runId}` dengan sumber `Available quota` saat Available license group `IT {runId}` cukup
62. Verifikasi permintaan diterima karena Sari memegang Update pada `IT {runId}`, dan `Tablet Inventaris - M2 {runId}` tidak lagi `Unmanaged`
