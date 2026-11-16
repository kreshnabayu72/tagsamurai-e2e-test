---
id: TC-FA-FATR-UI-062-area-disposal-dm
title: "Area utama: field tab Disposal dan tab Damaged & Missing"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r55
  - §4.1#r143
  - §4.1#r144
  - §4.1#r145
  - §4.1#r156
  - §4.1#r162
  - §4.1#r179
  - §4.1#r184
  - §4.1#r200
  - §4.1#r212
  - §9.2#b71
  - §9.2#b85
  - §9.2#b425
  - §9.2#b426
  - §9.4.2#r9
  - §9.4.4#r19
smoke: []
dependsOn: []
trace:
  §4.1#r55: [2, 4]
  §4.1#r143: [6, 33, 36, 41]
  §4.1#r144: [7, 37, 42]
  §4.1#r145: [8, 38, 43]
  §4.1#r156: 28
  §4.1#r162: 29
  §4.1#r179: [19, 46, 48]
  §4.1#r184: [20, 22, 50, 52]
  §4.1#r200: 25
  §4.1#r212: [26, 39, 44]
  §9.2#b71: [15, 16]
  §9.2#b85: 30
  §9.2#b425: [10, 11]
  §9.2#b426: 29
  §9.4.2#r9: [15, 16]
  §9.4.4#r19: 17
anchor: [13]
coverage:
  web: automated
---

# Area utama: field tab Disposal dan tab Damaged & Missing

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-062-1: Pengaturan Company default tab Disposal pada All categories: Allow Disposal `Allow`, Allowed disposal types `Sell`, `Scrap`, `Lost`, `Donate`, `Trade-in`, `Write-off`, Min asset age warning `12`, Max deviation from book value `30`, Require approval `ON`, Approval type `Any one approver`, Transaction timeout `7`, Send email notifications `OFF`.
  - DU-062-2: Pengaturan Company default tab Damaged & Missing pada All categories: Long missing after `30`, After photo required `OFF`.
  - DU-062-3: Pengaturan Company default tab Disposal dengan Allowed disposal types hanya `Sell`.
  - DU-062-4: Pengaturan Company default tab Disposal pada All categories yang berbeda dari nilai awal: Allowed disposal types hanya `Sell`, Min asset age warning `24`, Max deviation from book value `50`, Send email notifications `ON`.
  - DU-062-5: Pengaturan Company default tab Disposal pada All categories yang berbeda dari nilai awal: Require approval `OFF`.
  - DU-062-6: Pengaturan Company default tab Disposal pada All categories yang berbeda dari nilai awal: Require approval `ON`, Approval type `All approvers (AND)`.
- Kondisi:
  - K1: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-062-1.
  - K2: node All categories terpilih, tab Damaged & Missing aktif, nilai Company default memakai DU-062-2.
  - K3: node All categories terpilih, tab Disposal aktif, Allowed disposal types hanya `Sell` memakai DU-062-3.
  - K4: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-062-4.
  - K5: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-062-5.
  - K6: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-062-6.

## Test Steps

### Eligibility dan Limits Disposal
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi `Allow Disposal` bernilai `Allow`
3. Buka daftar pilihan `Allow Disposal`
4. Verifikasi pilihan `Allow Disposal` adalah `Allow` dan `Deny`
5. Tutup daftar pilihan dengan Escape
6. Verifikasi `Allowed disposal types` terpilih `Sell`, `Scrap`, `Lost`, `Donate`, `Trade-in`, dan `Write-off`
7. Verifikasi `Min asset age warning` bernilai `12`
8. Verifikasi `Max deviation from book value` bernilai `30`

### Evidence tidak ada di Disposal
9. Tampilkan Area utama dengan kondisi K1
10. Verifikasi tab `Disposal` memuat bagian `Limits` dan `Approval`
11. Verifikasi tab `Disposal` tidak memuat setting `Photo at start`, `Photo at end`, dan `After photo required`

### Pilihan terakhir Allowed disposal types tidak dapat dihapus
12. Tampilkan Area utama dengan kondisi K3
13. Verifikasi `Allowed disposal types` terpilih `Sell`
14. Hapus pilihan `Sell` pada `Allowed disposal types`
15. Verifikasi `Sell` tetap terpilih pada `Allowed disposal types`
16. Verifikasi pesan `At least one disposal type must be selected` tampil di bawah kontrol `Allowed disposal types`
17. Verifikasi tidak ada permintaan Save yang terkirim akibat penghapusan itu

### Approval Disposal
18. Tampilkan Area utama dengan kondisi K1
19. Verifikasi `Require approval` bernilai `ON`
20. Verifikasi `Approval type` bernilai `Any one approver`
21. Buka daftar pilihan `Approval type`
22. Verifikasi pilihan `Approval type` adalah `Any one approver` dan `All approvers (AND)`
23. Tutup daftar pilihan dengan Escape

### Reminders dan Notifications Disposal
24. Tampilkan Area utama dengan kondisi K1
25. Verifikasi `Transaction timeout` bernilai `7`
26. Verifikasi `Send email notifications` bernilai `OFF`

### Tab Damaged & Missing
27. Tampilkan Area utama dengan kondisi K2
28. Verifikasi `Long missing after` bernilai `30`
29. Verifikasi `After photo required` bernilai `OFF`
30. Verifikasi tab `Damaged & Missing` tidak memuat bagian `Overrides`

### Daftar pilihan Allowed disposal types
31. Tampilkan Area utama dengan kondisi K1
32. Buka daftar pilihan `Allowed disposal types`
33. Verifikasi pilihan `Allowed disposal types` adalah `Sell`, `Scrap`, `Lost`, `Donate`, `Trade-in`, dan `Write-off`
34. Tutup daftar pilihan dengan Escape

### Reset to Default mengembalikan Limits dan Notifications Disposal ke nilai awal
35. Tampilkan Area utama dengan kondisi K4
36. Verifikasi `Allowed disposal types` tampil dengan pilihan `Sell` saja sebelum Reset to Default
37. Verifikasi `Min asset age warning` bernilai `24`
38. Verifikasi `Max deviation from book value` bernilai `50`
39. Verifikasi `Send email notifications` bernilai `ON`
40. Klik `Reset to Default`
41. Verifikasi `Allowed disposal types` kembali ke nilai awal terpilih `Sell`, `Scrap`, `Lost`, `Donate`, `Trade-in`, dan `Write-off`
42. Verifikasi `Min asset age warning` kembali ke nilai awal `12`
43. Verifikasi `Max deviation from book value` kembali ke nilai awal `30`
44. Verifikasi `Send email notifications` kembali ke nilai awal `OFF`

### Reset to Default mengembalikan Require approval Disposal ke nilai awal
45. Tampilkan Area utama dengan kondisi K5
46. Verifikasi `Require approval` bernilai `OFF`
47. Klik `Reset to Default`
48. Verifikasi `Require approval` kembali ke nilai awal `ON`

### Reset to Default mengembalikan Approval type Disposal ke nilai awal
49. Tampilkan Area utama dengan kondisi K6
50. Verifikasi `Approval type` bernilai `All approvers (AND)`
51. Klik `Reset to Default`
52. Verifikasi `Approval type` kembali ke nilai awal `Any one approver`
