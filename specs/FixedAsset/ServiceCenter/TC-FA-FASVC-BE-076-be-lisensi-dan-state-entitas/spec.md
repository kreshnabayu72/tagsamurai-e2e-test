---
id: TC-FA-FASVC-BE-076-be-lisensi-dan-state-entitas
title: "Server: Tanpa Lisensi Addon atau Entitas Suspended atau Expired, Aksi Tulis Ditolak"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["FASVC-LOGIC-10e", "§9.11#r1", "EB-AKS-7"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-10e": [2, 4, 6, 8, 10, 12, 15]
  "§9.11#r1": [2, 4, 6, 8, 10, 12, 15]
  "EB-AKS-7": [18, 20, 22, 24, 26, 28, 30, 32, 35, 37, 39, 41, 43, 45, 47, 50]
anchor: []
---

# Server: Tanpa Lisensi Addon atau Entitas Suspended atau Expired, Aksi Tulis Ditolak

## Prerequisites
- Aktor: Total Control `Dewi Anggraini {runId}` pada entitas khusus `Klien Status Khusus {runId}`.
- Data:
  - DU-076-1: Entitas khusus `Klien Status Khusus {runId}` berstatus `Active` dengan lisensi addon Maintenance tidak aktif, tidak dipakai spec lain.
  - DU-076-2: User `Dewi Anggraini {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group pada `Klien Status Khusus {runId}`.
  - DU-076-3: Service Center `PT Sejuk Abadi Teknik {runId}` pada `Klien Status Khusus {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `kontak@entitas076.co.id`, Status `Active`.
  - DU-076-4: Service Center `CV Genset Prima {runId}` pada `Klien Status Khusus {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@entitas076.co.id`, Status `Active`.
  - DU-076-5: Service Center `UD Cahaya Servis {runId}` pada `Klien Status Khusus {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Malang`, Company email `kontak@entitas076.co.id`, Status `Inactive`.
  - DU-076-6: Service Center `Bengkel Maju Motor {runId}` pada `Klien Status Khusus {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Bandung`, Company email `kontak@entitas076.co.id`, Status `Active`.
- Kondisi:
  - Spec ini memakai entitas khusus DU-076-1 yang tidak dipakai spec lain; entitas itu berstatus `Active` dan lisensi addon Maintenance tidak aktif pada awal spec.
  - Aksi yang mengubah lisensi atau status entitas dilakukan oleh pemilik entitas di luar modul ini.
## Test Steps
### Tanpa lisensi addon, semua aksi ditolak
1. `Dewi Anggraini {runId}` mengirim Create dengan Name `Mitra Teknik Baru {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `kontak@entitas076.co.id`
2. Verifikasi permintaan ditolak karena lisensi addon tidak aktif
3. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
4. Verifikasi permintaan ditolak karena lisensi addon tidak aktif
5. `Dewi Anggraini {runId}` mengirim Inactivate atas `CV Genset Prima {runId}`
6. Verifikasi permintaan ditolak karena lisensi addon tidak aktif
7. `Dewi Anggraini {runId}` mengirim Activate atas `UD Cahaya Servis {runId}`
8. Verifikasi permintaan ditolak karena lisensi addon tidak aktif
9. `Dewi Anggraini {runId}` mengirim Delete atas `Bengkel Maju Motor {runId}`
10. Verifikasi permintaan ditolak karena lisensi addon tidak aktif
11. `Dewi Anggraini {runId}` membaca daftar Service Center dengan pencarian `{runId}`
12. Verifikasi permintaan baca ditolak karena lisensi addon tidak aktif
13. Lisensi addon Maintenance diaktifkan pada `Klien Status Khusus {runId}`
14. `Dewi Anggraini {runId}` membaca daftar Service Center dengan pencarian `{runId}`
15. Verifikasi `PT Sejuk Abadi Teknik {runId}` bernilai City `Jakarta Selatan`, `CV Genset Prima {runId}` dan `Bengkel Maju Motor {runId}` berstatus `Active`, `UD Cahaya Servis {runId}` berstatus `Inactive`, dan `Mitra Teknik Baru {runId}` tidak ada, sehingga semua aksi yang ditolak tidak mengubah data

### Entitas Suspended: data terbaca dan setiap aksi tulis ditolak
16. Status `Klien Status Khusus {runId}` diubah menjadi `Suspended`
17. `Dewi Anggraini {runId}` membaca daftar Service Center dengan pencarian `{runId}`
18. Verifikasi daftar terbaca dan memuat `PT Sejuk Abadi Teknik {runId}`, `CV Genset Prima {runId}`, `UD Cahaya Servis {runId}`, dan `Bengkel Maju Motor {runId}`
19. `Dewi Anggraini {runId}` mengirim Create dengan Name `Sentral Servis Tambahan {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `kontak@entitas076.co.id`
20. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
21. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
22. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
23. `Dewi Anggraini {runId}` mengirim Inactivate atas `CV Genset Prima {runId}`
24. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
25. `Dewi Anggraini {runId}` mengirim Activate atas `UD Cahaya Servis {runId}`
26. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
27. `Dewi Anggraini {runId}` mengirim Delete atas `Bengkel Maju Motor {runId}`
28. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
29. `Dewi Anggraini {runId}` mengunggah berkas `izin-usaha-sejuk.pdf` (PDF, 500 KB) sebagai lampiran `PT Sejuk Abadi Teknik {runId}`
30. Verifikasi unggahan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
31. `Dewi Anggraini {runId}` membaca ulang daftar Service Center dengan pencarian `{runId}`
32. Verifikasi `PT Sejuk Abadi Teknik {runId}` bernilai City `Jakarta Selatan`, `CV Genset Prima {runId}` dan `Bengkel Maju Motor {runId}` berstatus `Active`, `UD Cahaya Servis {runId}` berstatus `Inactive`, dan `Sentral Servis Tambahan {runId}` tidak ada, sehingga data tidak berubah

### Entitas Expired: data terbaca dan setiap aksi tulis ditolak
33. Status `Klien Status Khusus {runId}` diubah menjadi `Expired`
34. `Dewi Anggraini {runId}` membaca daftar Service Center dengan pencarian `{runId}`
35. Verifikasi daftar terbaca dan memuat `PT Sejuk Abadi Teknik {runId}`, `CV Genset Prima {runId}`, `UD Cahaya Servis {runId}`, dan `Bengkel Maju Motor {runId}`
36. `Dewi Anggraini {runId}` mengirim Create dengan Name `Karya Mesin Perkasa {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `kontak@entitas076.co.id`
37. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
38. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
39. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
40. `Dewi Anggraini {runId}` mengirim Inactivate atas `CV Genset Prima {runId}`
41. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
42. `Dewi Anggraini {runId}` mengirim Activate atas `UD Cahaya Servis {runId}`
43. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
44. `Dewi Anggraini {runId}` mengirim Delete atas `Bengkel Maju Motor {runId}`
45. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
46. `Dewi Anggraini {runId}` membaca ulang daftar Service Center dengan pencarian `{runId}`
47. Verifikasi `PT Sejuk Abadi Teknik {runId}` bernilai City `Jakarta Selatan`, `CV Genset Prima {runId}` dan `Bengkel Maju Motor {runId}` berstatus `Active`, `UD Cahaya Servis {runId}` berstatus `Inactive`, dan `Karya Mesin Perkasa {runId}` tidak ada, sehingga data tidak berubah

### Entitas pada masa Grace memakai penolakan yang sama
48. Status `Klien Status Khusus {runId}` diubah menjadi masa `Grace`
49. `Dewi Anggraini {runId}` mengirim Create dengan Name `Prima Servis Terpadu {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `kontak@entitas076.co.id`
50. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`, sama dengan Suspended dan Expired
