---
id: TC-FA-FAREG-BE-132-kunci-sesi-edit
title: "Kunci sesi edit batch Draft"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-19a, FAREG-LOGIC-19c, FAREG-LOGIC-19e, FAREG-LOGIC-19f, "§9.2#p21", "§9.6#r12", EB-EDG-3]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-19a: [3, 7, 14]
  FAREG-LOGIC-19c: [14, 27, 29, 32, 33, 41, 45]
  FAREG-LOGIC-19e: [7, 11, 14, 51, 53, 61, 64, 66, 69, 72]
  FAREG-LOGIC-19f: [17, 20, 22, 24, 48]
  "§9.2#p21": [33, 34, 36, 40, 41, 44, 45, 46]
  "§9.6#r12": [17, 18, 20, 22, 24, 25, 56, 57]
  EB-EDG-3: [44, 45, 46, 48]
owner: BE
---
# Kunci sesi edit batch Draft

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Blitar {runId}`, pembuat dan Owner batch Draft di bawah); Budi (Manage asset & TAG, Group terkelola `Gudang Blitar {runId}`); Citra dan Hadi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Blitar {runId}`, approver); Agus (Manage asset & TAG tanpa akses ke `Gudang Blitar {runId}`).
- Data:
  - DU-132-1: Group `Gudang Blitar {runId}`, Assignable, toggle `Require Approval for Registration` ON, di entitas aktor.
  - DU-132-2: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-132`, TAG Type `Non-TAG`.
  - DU-132-3: batch Draft milik Rina, Group `Gudang Blitar {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-132-4: batch Draft milik Rina, Group `Gudang Blitar {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-132-5: batch Draft milik Rina, Group `Gudang Blitar {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-132-6: batch Draft milik Rina, Group `Gudang Blitar {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-132-7: batch Draft milik Rina, Group `Gudang Blitar {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-132-8: batch Draft milik Rina, Group `Gudang Blitar {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-132-10: batch Draft milik Rina, Group `Gudang Blitar {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-132-11: batch Draft milik Rina, Group `Gudang Blitar {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-132-9: batch Draft baru yang dibuat Rina lewat Save draft pertama: Group `Gudang Blitar {runId}`, Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-132`, Quantity `1`.
- Kondisi:
  - Approval Workflow aktif untuk `Gudang Blitar {runId}` dengan Citra dan Hadi sebagai approver.
  - Kuota tenant dan kuota Group `Gudang Blitar {runId}` mencukupi untuk seluruh aset yang diajukan spec ini.
  - TTL kunci sesi edit bernilai 10 menit tanpa aktivitas.

## Test Steps

### Kunci sesi eksklusif per batch
1. Rina membuka batch DU-132-3 dalam mode Edit hingga memegang kunci sesinya
2. Budi membuka batch DU-132-3 dalam mode Edit
3. Verifikasi Budi tidak memperoleh kunci dan kunci sesi batch DU-132-3 tetap dipegang Rina

### Kunci diperpanjang oleh aktivitas dan kedaluwarsa setelah 10 menit penuh tanpa aktivitas
4. Rina membuka batch DU-132-4 dalam mode Edit hingga memegang kunci sesinya
5. Enam menit berlalu tanpa interaksi baru dari Rina
6. Budi membuka batch DU-132-4 dalam mode Edit
7. Verifikasi kunci sesi batch DU-132-4 tetap dipegang Rina karena belum 10 menit tanpa aktivitas
8. Rina berinteraksi dengan form batch DU-132-4 dengan mengubah Alias Name menjadi `Meja Rapat {runId}` tanpa menyimpan
9. Enam menit berlalu tanpa interaksi baru dari Rina
10. Budi membuka batch DU-132-4 dalam mode Edit
11. Verifikasi kunci sesi batch DU-132-4 tetap dipegang Rina karena interaksi Rina memperpanjang kunci dan batas 10 menit dihitung dari aktivitas terakhir
12. Lima menit berlalu tanpa interaksi baru dari Rina, sehingga 11 menit penuh sejak interaksi terakhir
13. Budi membuka batch DU-132-4 dalam mode Edit
14. Verifikasi kunci sesi Rina sudah kedaluwarsa dan kunci sesi batch DU-132-4 dipegang Budi

### Take over memindahkan kunci dan menolak sesi pemegang lama tanpa mutasi
15. Rina membuka batch DU-132-5 dalam mode Edit hingga memegang kunci sesinya
16. Budi membuka batch DU-132-5 dan meminta Take over kunci sesinya
17. Verifikasi kunci sesi batch DU-132-5 berpindah ke Budi dan tidak lagi dipegang Rina
18. Verifikasi Registration Log batch DU-132-5 tidak memuat entri untuk Take over
19. Rina mengirim Save draft atas batch DU-132-5 dari sesinya dengan Alias Name `Meja Lama {runId}`
20. Verifikasi Save draft dari Rina ditolak server tanpa mutasi dan Alias Name batch DU-132-5 tetap kosong
21. Rina mengirim autosave atas batch DU-132-5 dari sesinya dengan Alias Name `Meja Lama {runId}`
22. Verifikasi autosave dari Rina ditolak server tanpa mutasi
23. Rina mengirim Submit atas batch DU-132-5 dari sesinya
24. Verifikasi Submit dari Rina ditolak server tanpa mutasi dan batch DU-132-5 tetap Draft
25. Verifikasi kunci sesi batch DU-132-5 tetap dipegang Budi

### Kunci dilepas saat keluar form
26. Budi keluar dari form batch DU-132-5 tanpa Submit
27. Verifikasi tidak ada pemegang kunci sesi batch DU-132-5
28. Rina membuka batch DU-132-5 dalam mode Edit
29. Verifikasi kunci sesi batch DU-132-5 dipegang Rina tanpa Take over

### Kunci dilepas saat Submit dan notifikasi approver lain otomatis Read
30. Rina membuka batch DU-132-6 dalam mode Edit hingga memegang kunci sesinya
31. Rina mengirim Submit atas batch DU-132-6
32. Verifikasi Submit berhasil dan aset batch DU-132-6 berstatus Waiting for Approval
33. Verifikasi tidak ada pemegang kunci sesi batch DU-132-6
34. Verifikasi notifikasi actionable `registration_waiting_approval` milik Citra dan milik Hadi untuk pengajuan batch DU-132-6 berstatus belum dibaca
35. Citra mengirim keputusan `Approve` untuk seluruh aset pengajuan batch DU-132-6
36. Verifikasi notifikasi `registration_waiting_approval` milik Hadi untuk pengajuan itu otomatis berstatus Read

### Kunci dilepas saat batch di-Submit pihak lain
37. Rina membuka batch DU-132-7 dalam mode Edit hingga memegang kunci sesinya
38. Budi membuka batch DU-132-7 dan meminta Take over kunci sesinya
39. Budi mengirim Submit atas batch DU-132-7
40. Verifikasi Submit dari Budi berhasil dan aset batch DU-132-7 berstatus Waiting for Approval
41. Verifikasi tidak ada pemegang kunci sesi batch DU-132-7, baik Rina maupun Budi

### Batch yang dihapus melepas kunci dan Registration Log tidak dipertahankan
42. Rina membuka batch DU-132-8 dalam mode Edit hingga memegang kunci sesinya
43. Rina mengirim Delete atas batch DU-132-8
44. Verifikasi Delete berhasil dan batch DU-132-8 tidak lagi tampil di daftar Draft
45. Verifikasi tidak ada pemegang kunci sesi batch DU-132-8
46. Verifikasi Registration Log batch DU-132-8 tidak dipertahankan dan tidak memuat entri apa pun
47. Budi membuka batch DU-132-8 dalam mode Edit
48. Verifikasi pembukaan ditolak server dengan pesan `This draft is no longer available.` dan bukan dengan pesan sesi diambil alih

### Autosave berjalan setelah Draft tercipta oleh Save pertama
49. Rina mencatat jumlah batch Draft miliknya
50. Rina mengirim Save draft pertama dari form baru dengan Group `Gudang Blitar {runId}`, Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-132`, dan Quantity `1`
51. Verifikasi jumlah batch Draft milik Rina bertambah satu
52. Rina mengirim autosave atas batch Draft baru itu dengan Alias Name `Meja Tamu {runId}`
53. Verifikasi autosave diterima dan Alias Name `Meja Tamu {runId}` tersimpan pada batch Draft baru

### Take over oleh user tanpa hak ditolak
54. Rina membuka batch DU-132-10 dalam mode Edit hingga memegang kunci sesinya
55. Agus meminta Take over kunci sesi batch DU-132-10
56. Verifikasi Take over dari Agus ditolak server tanpa mutasi
57. Verifikasi kunci sesi batch DU-132-10 tetap dipegang Rina

### Save draft dan autosave memperpanjang kunci dan tidak melepasnya
58. Rina membuka batch DU-132-11 dalam mode Edit hingga memegang kunci sesinya
59. Enam menit berlalu tanpa interaksi baru dari Rina
60. Rina mengirim Save draft atas batch DU-132-11 dengan Alias Name `Meja Direksi {runId}`
61. Verifikasi kunci sesi batch DU-132-11 tetap dipegang Rina sesudah Save draft
62. Enam menit berlalu tanpa interaksi baru dari Rina, sehingga 12 menit penuh sejak kunci diperoleh
63. Budi membuka batch DU-132-11 dalam mode Edit
64. Verifikasi kunci sesi batch DU-132-11 tetap dipegang Rina karena Save draft memperpanjang kunci
65. Rina mengirim autosave atas batch DU-132-11 dengan Alias Name `Meja Pimpinan {runId}`
66. Verifikasi kunci sesi batch DU-132-11 tetap dipegang Rina sesudah autosave
67. Enam menit berlalu tanpa interaksi baru dari Rina, sehingga 12 menit penuh sejak Save draft dan 6 menit sejak autosave
68. Budi membuka batch DU-132-11 dalam mode Edit
69. Verifikasi kunci sesi batch DU-132-11 tetap dipegang Rina karena autosave memperpanjang kunci

### Autosave tidak berjalan sebelum Save draft pertama
70. Rina mencatat jumlah batch Draft miliknya
71. Rina mengirim autosave dari form baru dengan Group `Gudang Blitar {runId}`, Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-132`, dan Quantity `1` sebelum Save draft pertama
72. Verifikasi autosave tidak membuat batch Draft dan jumlah batch Draft milik Rina sama dengan catatan langkah 70
