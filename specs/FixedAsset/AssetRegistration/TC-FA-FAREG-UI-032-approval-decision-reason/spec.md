---
id: TC-FA-FAREG-UI-032-approval-decision-reason
title: "Halaman Approval: Decision per aset dan validasi Reason"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06e, FI-REG-15, S-REG-23, V-REG-16, V-REG-18, §4.1#r7, §4.2.4#b4, §4.2.4#b5, §9.9#r19, §9.9#r20, EB-FRM-4@reason]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-06e: [8, 10, 13, 31, 33, 39]
  FI-REG-15: [18, 20]
  S-REG-23: [28, 29]
  V-REG-16: [29, 30, 31, 32, 33, 34, 40, 64]
  V-REG-18: [45, 49, 53, 57, 61]
  §4.1#r7: [26, 28, 30, 32]
  §4.2.4#b4: [2, 4]
  §4.2.4#b5: [8, 10, 11, 13]
  §9.9#r19: [31, 33, 39, 45, 49, 53, 57, 64]
  §9.9#r20: [6, 8, 10, 13]
  EB-FRM-4@reason: [45, 49, 53, 57]
anchor: [38, 63]
coverage:
  web: automated
---
# Halaman Approval: Decision per aset dan validasi Reason

## Prerequisites
- Aktor: Dewi A (approver, role Group Manager, cakupan Group binaan + sub-group termasuk Gudang 1, bukan pengaju pengajuan).
- Layar awal: Halaman Approval pengajuan yang dibuka dari antrean Approvals tab Active.
- Komponen: Halaman Approval
- Data:
  - DU-032-1: pengajuan Registration ID `REG-20261109-00003`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `4`.
  - DU-032-2: aset Name `Laptop - 128`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-032-3: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Corrections `1`, Decision `Approve`, tanpa Reason.
  - DU-032-4: aset Name `Laptop - 130`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-032-5: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
- Kondisi:
  - K1: pengajuan DU-032-1 berisi aset DU-032-2 sampai DU-032-4 dalam grup Accordion `Laptop` dan DU-032-5 dalam grup Accordion `Office Desk`, dengan Decision awal `Approve` dan tanpa Reason, dan approver berhak memutuskan.

## Test Steps

### Placeholder Reason dan Reason dapat diisi pada Decision Approve
1. Tampilkan Halaman Approval dengan kondisi K1
2. Verifikasi sel Reason pada baris `Laptop - 128` memiliki placeholder `Enter reason`
3. Isi Reason pada baris `Laptop - 128` dengan `Scratch on the casing is minor`
4. Verifikasi Reason pada baris `Laptop - 128` menampilkan `Scratch on the casing is minor`

### Decision diubah per aset
5. Tampilkan Halaman Approval dengan kondisi K1
6. Verifikasi Decision pada baris `Laptop - 130` bernilai `Approve` sebelum diubah
7. Pilih Decision `Return to Draft` pada baris `Laptop - 130`
8. Verifikasi Decision pada baris `Laptop - 130` menampilkan `Return to Draft`
9. Pilih Decision `Reject` pada baris `Office Desk - 12`
10. Verifikasi Decision pada baris `Office Desk - 12` menampilkan `Reject`
11. Verifikasi Decision pada baris `Laptop - 128` tetap `Approve`
12. Pilih Decision `Approve` pada baris `Laptop - 130`
13. Verifikasi Decision pada baris `Laptop - 130` menampilkan `Approve`

### Reason yang sudah diketik tidak dikosongkan saat Decision diubah
14. Tampilkan Halaman Approval dengan kondisi K1
15. Pilih Decision `Reject` pada baris `Office Desk - 12`
16. Isi Reason pada baris `Office Desk - 12` dengan `Duplicate entry`
17. Pilih Decision `Return to Draft` pada baris `Office Desk - 12`
18. Verifikasi Reason pada baris `Office Desk - 12` tetap `Duplicate entry`
19. Pilih Decision `Approve` pada baris `Office Desk - 12`
20. Verifikasi Reason pada baris `Office Desk - 12` tetap `Duplicate entry`

### Reason kosong pada Return to Draft dan Reject ditolak saat Submit
21. Tampilkan Halaman Approval dengan kondisi K1
22. Pilih Decision `Return to Draft` pada baris `Laptop - 130`
23. Kosongkan Reason pada baris `Laptop - 130`
24. Pilih Decision `Reject` pada baris `Office Desk - 12`
25. Kosongkan Reason pada baris `Office Desk - 12`
26. Verifikasi Alert Danger Reason belum tampil sebelum `[Submit]` ditekan
27. Klik `[Submit]`
28. Verifikasi Alert Danger tampil
29. Verifikasi Alert memuat `Reason for returned or rejected assets must not be empty`
30. Verifikasi sel Reason pada baris `Laptop - 130` ber-outline danger
31. Verifikasi pesan `Reason must not be empty` tampil di bawah sel Reason pada baris `Laptop - 130`
32. Verifikasi sel Reason pada baris `Office Desk - 12` ber-outline danger
33. Verifikasi pesan `Reason must not be empty` tampil di bawah sel Reason pada baris `Office Desk - 12`
34. Verifikasi halaman menggulir ke baris `Laptop - 130` sebagai baris pertama yang Reason-nya kosong

### Reason kosong pada Approve diterima saat Submit
35. Tampilkan Halaman Approval dengan kondisi K1
36. Kosongkan Reason pada baris `Laptop - 128`
37. Klik `[Submit]`
38. Verifikasi dialog `Submit Approval` tampil
39. Verifikasi Alert Danger Reason tidak tampil
40. Verifikasi sel Reason pada baris `Laptop - 128` tidak ber-outline danger
41. Klik `[Cancel]` pada dialog `Submit Approval`

### Reason tepat di batas panjang
42. Tampilkan Halaman Approval dengan kondisi K1
43. Pilih Decision `Return to Draft` pada baris `Laptop - 130`
44. Isi Reason pada baris `Laptop - 130` dengan `perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkap` (360 karakter)
45. Verifikasi tidak ada pesan `Max. 360 characters` pada Reason baris `Laptop - 130`

### Reason satu karakter di atas batas panjang
46. Tampilkan Halaman Approval dengan kondisi K1
47. Pilih Decision `Return to Draft` pada baris `Laptop - 130`
48. Isi Reason pada baris `Laptop - 130` dengan `perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapy` (361 karakter)
49. Verifikasi pesan `Max. 360 characters` tampil di bawah Reason baris `Laptop - 130`

### Reason di batas panjang dengan spasi di tengah
50. Tampilkan Halaman Approval dengan kondisi K1
51. Pilih Decision `Return to Draft` pada baris `Laptop - 130`
52. Isi Reason pada baris `Laptop - 130` dengan `Foto aset kurang jelas dan data fisik tidak lengkap di lapangan Foto aset kurang jelas dan data fisik tidak lengkap di lapangan Foto aset kurang jelas dan data fisik tidak lengkap di lapangan Foto aset kurang jelas dan data fisik tidak lengkap di lapangan Foto aset kurang jelas dan data fisik tidak lengkap di lapangan Foto aset kurang jelas dan data fisik ti` (360 karakter)
53. Verifikasi tidak ada pesan `Max. 360 characters` pada Reason baris `Laptop - 130`

### Reason di batas panjang dengan karakter beraksen dan non-BMP
54. Tampilkan Halaman Approval dengan kondisi K1
55. Pilih Decision `Return to Draft` pada baris `Laptop - 130`
56. Isi Reason pada baris `Laptop - 130` dengan `Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan Élan Şişli Çağrı Pemeriksaan𝒜` (360 karakter)
57. Verifikasi tidak ada pesan `Max. 360 characters` pada Reason baris `Laptop - 130`

### Reason satu karakter diterima saat Submit
58. Tampilkan Halaman Approval dengan kondisi K1
59. Pilih Decision `Return to Draft` pada baris `Laptop - 130`
60. Isi Reason pada baris `Laptop - 130` dengan `X` (1 karakter)
61. Verifikasi tidak ada pesan `Max. 360 characters` pada Reason baris `Laptop - 130`
62. Klik `[Submit]`
63. Verifikasi dialog `Submit Approval` tampil
64. Verifikasi pesan `Reason must not be empty` tidak tampil pada baris `Laptop - 130`
65. Klik `[Cancel]` pada dialog `Submit Approval`
