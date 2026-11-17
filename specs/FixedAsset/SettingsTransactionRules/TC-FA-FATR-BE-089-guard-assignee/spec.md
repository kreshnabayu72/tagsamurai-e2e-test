---
id: TC-FA-FATR-BE-089-guard-assignee
title: "Guard Allowed assignee OFF/OFF"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§4.1#r121", "§4.1#r122", "§4.1#r123", "§4.1#r124", "§4.1#r125", "§4.1#r126", "§4.1#r129", "§4.1#r130", "§4.1#r131", "§4.1#r133", "§6#r35", "§6#r36", "§6#r37", "§6#r40", "§6#r41", "§9.2#b32", "§9.2#b44", "§9.2#b47", "§9.2#b106", "§9.2#b110", "§9.2#b111", "§9.2#b114", "§9.2#b115", "§9.2#b116", "§9.2#b118", "§9.2#b119", "§9.2#b185", "§9.2#b187", "§9.2#b188", "§9.2#b189", "§9.2#b191", "§9.4.2#r73", "§9.4.2#r74", "§9.4.2#r76", "§9.4.2#r77", "§9.4.2#r78", "§9.4.2#r79", "§9.4.2#r80", "§9.4.2#r81", "§9.4.2#r82", "§9.4.2#r85", "§9.4.4#r34", "§9.6#r31", "§9.6#r32", "§9.6#r33", "§9.9#r12", "§9.9#r17", "§9.9#r22", EB-ERR-4, D-07, "§6#r3"]
smoke: []
dependsOn: []
trace:
  "§4.1#r121": [3, 5, 7, 42, 43]
  "§4.1#r122": 15
  "§4.1#r123": 17
  "§4.1#r124": 19
  "§4.1#r125": 2
  "§4.1#r126": [9, 10, 13]
  "§4.1#r129": 24
  "§4.1#r130": 22
  "§4.1#r131": [26, 28]
  "§4.1#r133": 2
  "§6#r35": [22, 24]
  "§6#r36": 15
  "§6#r37": 26
  "§6#r40": 31
  "§6#r41": 40
  "§9.2#b32": 19
  "§9.2#b44": 15
  "§9.2#b47": 19
  "§9.2#b106": [26, 28]
  "§9.2#b110": 31
  "§9.2#b111": 40
  "§9.2#b114": 32
  "§9.2#b115": [31, 32]
  "§9.2#b116": 38
  "§9.2#b118": 35
  "§9.2#b119": 36
  "§9.2#b185": 31
  "§9.2#b187": 40
  "§9.2#b188": 32
  "§9.2#b189": 38
  "§9.2#b191": 35
  "§9.4.2#r73": 7
  "§9.4.2#r74": [9, 12]
  "§9.4.2#r76": 15
  "§9.4.2#r77": 17
  "§9.4.2#r78": 19
  "§9.4.2#r79": 22
  "§9.4.2#r80": [26, 28]
  "§9.4.2#r81": 19
  "§9.4.2#r82": 31
  "§9.4.2#r85": 32
  "§9.4.4#r34": 33
  "§9.6#r31": 32
  "§9.6#r32": 38
  "§9.6#r33": 35
  "§9.9#r12": [2, 20]
  "§9.9#r17": [22, 24]
  "§9.9#r22": 31
  EB-ERR-4: [3, 10, 20]
  D-07: 40
  "§6#r3": [31, 40]
---
# Guard Allowed assignee OFF/OFF

## Prerequisites
- Aktor: Maya Pengelola (DU-089-2) dan pemanggil terotorisasi Rudi Integrasi (DU-089-3), keduanya Total Control dengan cakupan seluruh Group.
- Data:
  - DU-089-1: Entitas, entitas khusus spec ini: Name `Entitas Guard {runId}`.
  - DU-089-2: User, pengelola yang menyimpan setting dan mengelola override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-089-3: User, pemanggil terotorisasi yang mengirim request langsung: Name `Rudi Integrasi {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-089-4: Category, Category dengan satu override Employee OFF yang sudah ada: Name `Guard Override Ada {runId}`.
  - DU-089-5: Category, Category tanpa override untuk Save langsung: Name `Guard Save Bersih {runId}`.
  - DU-089-6: Category, Category dengan Allow Assign nilai sendiri Deny untuk Save Allowed assignee OFF/OFF: Name `Guard Deny Tersimpan {runId}`.
  - DU-089-7: Category, Category dengan Allow Assign nilai sendiri Deny yang asetnya dibuka override Allow: Name `Guard Deny Dibuka {runId}`.
  - DU-089-8: Category, Category dengan Allowed assignee: Division nilai sendiri OFF untuk Add override: Name `Guard Add {runId}`.
  - DU-089-9: Category, Category dengan Allowed assignee: Division nilai sendiri OFF untuk Delete ditolak: Name `Guard Hapus {runId}`.
  - DU-089-10: Category, Category dengan Allowed assignee: Division nilai sendiri OFF untuk bulk Delete: Name `Guard Hapus Bulk {runId}`.
  - DU-089-11: Category, Category dengan Allow Assign Deny dan Division OFF untuk Delete yang lolos: Name `Guard Deny Setelah Hapus {runId}`.
  - DU-089-12: Category, Category tanpa override untuk Add override dengan Deny dari override sendiri: Name `Guard Add Deny Sendiri {runId}`.
  - DU-089-13: Group, Group target override guard: Name `Tim Guard Ada {runId}`.
  - DU-089-14: Group, Group target override guard: Name `Tim Guard Deny {runId}`.
  - DU-089-15: Group, Group target override guard: Name `Tim Guard Dibuka {runId}`.
  - DU-089-16: Group, Group target override guard: Name `Tim Guard Add {runId}`.
  - DU-089-17: Group, Group target override guard: Name `Tim Guard Hapus {runId}`.
  - DU-089-18: Group, Group target override guard: Name `Tim Guard Hapus Bulk {runId}`.
  - DU-089-19: Group, Group target override guard: Name `Tim Guard Plain {runId}`.
  - DU-089-20: Group, Group target override guard: Name `Tim Guard Deny Hapus {runId}`.
  - DU-089-21: Group, Group target override guard: Name `Tim Guard Add Deny {runId}`.
  - DU-089-22: Asset, aset target guard: Name `Perangkat Guard Ada {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Override Ada {runId}`; Group `Tim Guard Ada {runId}`.
  - DU-089-23: Asset, aset target guard: Name `Mesin Terkunci Satu {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Deny Tersimpan {runId}`; Group `Tim Guard Deny {runId}`.
  - DU-089-24: Asset, aset target guard: Name `Mesin Terkunci Dua {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Deny Tersimpan {runId}`; Group `Tim Guard Deny {runId}`.
  - DU-089-25: Asset, aset target guard: Name `Mesin Dibuka {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Deny Dibuka {runId}`; Group `Tim Guard Dibuka {runId}`.
  - DU-089-26: Asset, aset target guard: Name `Perangkat Guard Add {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Add {runId}`; Group `Tim Guard Add {runId}`.
  - DU-089-27: Asset, aset target guard: Name `Perangkat Guard Hapus {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Hapus {runId}`; Group `Tim Guard Hapus {runId}`.
  - DU-089-28: Asset, aset target guard: Name `Perangkat Guard Hapus Bulk {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Hapus Bulk {runId}`; Group `Tim Guard Hapus Bulk {runId}`.
  - DU-089-29: Asset, aset target guard: Name `Mesin Deny Hapus {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Deny Setelah Hapus {runId}`; Group `Tim Guard Deny Hapus {runId}`.
  - DU-089-30: Asset, aset target guard: Name `Perangkat Guard Add Deny {runId}`; Asset Name `Perangkat Guard Umum {runId}`; Category `Guard Add Deny Sendiri {runId}`; Group `Tim Guard Add Deny {runId}`.
  - DU-089-31: Override, override Employee OFF yang sudah ada pada Group: Scope `Group`; Target `Tim Guard Ada {runId}`; Category `Guard Override Ada {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Employee`; Value `OFF`.
  - DU-089-32: Override, override Allow yang membuka aset di bawah Category Deny: Scope `aset`; Target `Mesin Dibuka {runId}`; Category `Guard Deny Dibuka {runId}`; Transaksi `penugasan`; Field `Allow Assign`; Value `Allow`.
  - DU-089-33: Override, override Group Division ON yang jadi satu-satunya penyebab kombinasi override aset tidak OFF/OFF: Scope `Group`; Target `Tim Guard Hapus {runId}`; Category `Guard Hapus {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Division`; Value `ON`.
  - DU-089-34: Override, override aset Employee OFF yang tersisa: Scope `aset`; Target `Perangkat Guard Hapus {runId}`; Category `Guard Hapus {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Employee`; Value `OFF`.
  - DU-089-35: Override, override Group Division ON pada bulk Delete: Scope `Group`; Target `Tim Guard Hapus Bulk {runId}`; Category `Guard Hapus Bulk {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Division`; Value `ON`.
  - DU-089-36: Override, override aset Employee OFF yang tersisa pada bulk Delete: Scope `aset`; Target `Perangkat Guard Hapus Bulk {runId}`; Category `Guard Hapus Bulk {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Employee`; Value `OFF`.
  - DU-089-37: Override, override biasa pada bulk Delete yang boleh terhapus: Scope `Group`; Target `Tim Guard Plain {runId}`; Category `Guard Hapus Bulk {runId}`; Transaksi `penugasan`; Field `Max assets per assignee (concurrent)`; Value `2`.
  - DU-089-38: Override, override Group Division ON pada Category Deny yang aman dihapus: Scope `Group`; Target `Tim Guard Deny Hapus {runId}`; Category `Guard Deny Setelah Hapus {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Division`; Value `ON`.
  - DU-089-39: Override, override aset Employee OFF pada Category Deny: Scope `aset`; Target `Mesin Deny Hapus {runId}`; Category `Guard Deny Setelah Hapus {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Employee`; Value `OFF`.
  - DU-089-40 sampai DU-089-47 adalah nilai input Save dan Add override yang ditolak atau diterima di blok masing-masing, bukan record yang sudah ada.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Guard {runId}` (DU-089-1) yang tidak dipakai spec lain, karena yang diasersi adalah nilai Company default dan nilai Category.
  - Allowed assignee: Employee `ON` dan Allowed assignee: Division `ON` pada Company default, dan Allow Assign `Allow` pada Company default.
  - Category `Guard Deny Tersimpan {runId}`, `Guard Deny Dibuka {runId}`, dan `Guard Deny Setelah Hapus {runId}` memiliki Allow Assign nilai sendiri `Deny`; Category `Guard Add {runId}`, `Guard Hapus {runId}`, `Guard Hapus Bulk {runId}`, dan `Guard Deny Setelah Hapus {runId}` memiliki Allowed assignee: Division nilai sendiri `OFF`.
  - Seluruh nilai Category lainnya Inherit.
  - Transaksi Assign disebut «transaksi penugasan» dan transaksi Borrow disebut «transaksi peminjaman» di langkah.

## Test Steps

### Save dengan draft keduanya OFF ditolak server walau lolos dari tampilan
1. Rudi Integrasi mengirim langsung Save Category `Guard Save Bersih {runId}` dengan Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`
2. Verifikasi Save ditolak server dengan pesan `At least one assignee type must be enabled`
3. Verifikasi tidak ada perubahan tersimpan: Allowed assignee: Employee dan Allowed assignee: Division Category `Guard Save Bersih {runId}` tetap Inherit

### Salah satu jenis OFF diterima, tetapi mematikan jenis terakhir ditolak
4. Maya Pengelola menyimpan Category `Guard Save Bersih {runId}` dengan Allowed assignee: Employee nilai sendiri `OFF` dan Allowed assignee: Division tetap Inherit
5. Verifikasi Save diterima dan Allowed assignee: Employee `OFF` tersimpan, karena minimal satu jenis ON sudah cukup
6. Maya Pengelola menyimpan Category `Guard Save Bersih {runId}` dengan Allowed assignee: Division nilai sendiri `OFF`, jenis terakhir yang masih ON
7. Verifikasi Save ditolak karena nilai yang berlaku keduanya OFF, dan Allowed assignee: Division tetap Inherit

### Save yang membuat override yang sudah ada menjadi OFF/OFF ditolak secara atomik
8. Maya Pengelola menyimpan Category `Guard Override Ada {runId}` dengan Allowed assignee: Division nilai sendiri `OFF` dan Max extensions nilai sendiri `2` dalam satu Save
9. Verifikasi Save ditolak karena override Group `Tim Guard Ada {runId}` yang sudah ada akan memiliki kombinasi efektif OFF/OFF
10. Verifikasi tidak ada perubahan yang tersimpan: Allowed assignee: Division dan Max extensions Category `Guard Override Ada {runId}` tetap Inherit
11. Maya Pengelola menyimpan Company default dengan Allowed assignee: Division `OFF`
12. Verifikasi Save ditolak karena perubahan Company default membuat kombinasi efektif override Group `Tim Guard Ada {runId}` menjadi OFF/OFF
13. Verifikasi Allowed assignee: Division Company default tetap `ON` dan tidak ada perubahan yang tersimpan di Company default

### Nilai Category tidak dievaluasi selama Allow Assign Deny dan dievaluasi saat menjadi Allow
14. Maya Pengelola menyimpan Category `Guard Deny Tersimpan {runId}` dengan Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`
15. Verifikasi Save diterima dan kedua nilai `OFF` tersimpan, karena nilai Category tidak dievaluasi selama Allow Assign bernilai Deny
16. Maya Pengelola menyimpan Category `Guard Deny Tersimpan {runId}` dengan Allow Assign `Allow`
17. Verifikasi Save ditolak karena Save yang membuat Allow Assign bernilai Allow mengevaluasi nilai Category yang kini keduanya OFF

### Aset yang dibuka override Allow di bawah Category Deny tetap dievaluasi
18. Maya Pengelola menyimpan Category `Guard Deny Dibuka {runId}` dengan Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`
19. Verifikasi Save ditolak karena aset `Mesin Dibuka {runId}`, yang dibuka override Allow, akan memiliki kombinasi efektif OFF/OFF
20. Verifikasi Allowed assignee: Employee dan Allowed assignee: Division Category `Guard Deny Dibuka {runId}` tetap Inherit, karena kombinasi aset yang dibuka override Allow menolak Save
21. Maya Pengelola menambahkan override aset `Mesin Terkunci Satu {runId}` pada Category `Guard Deny Tersimpan {runId}` untuk transaksi penugasan dengan Allow Assign `Allow`
22. Verifikasi Add override ditolak dengan pesan `At least one assignee type must be enabled` karena membuka aset yang kombinasi efektif Allowed assignee-nya OFF/OFF di bawah Category Deny, dan tidak ada override terbuat

### Add override yang membuat kombinasi efektif OFF/OFF ditolak
23. Maya Pengelola menambahkan override Group `Tim Guard Add {runId}` pada Category `Guard Add {runId}` untuk transaksi penugasan dengan Allowed assignee: Employee `OFF`
24. Verifikasi Add override ditolak karena kombinasi efektif pada aset target keduanya OFF, dan tidak ada override terbuat

### Guard tidak dievaluasi untuk aset target yang Allow Assign-nya Deny
25. Maya Pengelola menambahkan override aset `Mesin Terkunci Dua {runId}` pada Category `Guard Deny Tersimpan {runId}` untuk transaksi penugasan dengan Allowed assignee: Employee `OFF`
26. Verifikasi Add override diterima walau nilai efektif keduanya OFF, karena nilai efektif Allow Assign aset itu Deny
27. Maya Pengelola menambahkan override Group `Tim Guard Add Deny {runId}` pada Category `Guard Add Deny Sendiri {runId}` untuk transaksi penugasan dengan Allow Assign `Deny` dan Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`
28. Verifikasi Add override diterima, karena Deny dari override yang sedang dibuat membuat guard tidak dievaluasi

### Delete override yang membuat override yang tersisa OFF/OFF ditolak
29. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log serta versi setting
30. Maya Pengelola menghapus override Group `Tim Guard Hapus {runId}`, yang akan membuat kombinasi efektif override aset `Perangkat Guard Hapus {runId}` yang tersisa keduanya OFF
31. Verifikasi Delete ditolak server dengan pesan `At least one assignee type must be enabled`
32. Verifikasi override Group `Tim Guard Hapus {runId}` masih ada
33. Verifikasi Changelog dan Activity Log tidak bertambah entri dan versi setting tidak naik

### Bulk Delete: baris yang ditolak guard dilewati dan bila tidak ada yang terhapus tidak ada perubahan
34. Maya Pengelola menghapus bulk override Group `Tim Guard Hapus {runId}` dan override Group `Tim Guard Hapus Bulk {runId}`, keduanya akan ditolak guard
35. Verifikasi tidak ada override yang terhapus, dan kedua override masih ada
36. Verifikasi hasil Delete menyebut hanya kedua override itu sebagai ditolak guard
37. Maya Pengelola menghapus bulk override Group `Tim Guard Hapus Bulk {runId}`, yang akan ditolak guard, dan override Group `Tim Guard Plain {runId}`
38. Verifikasi override Group `Tim Guard Plain {runId}` terhapus dan override Group `Tim Guard Hapus Bulk {runId}` dilewati seperti baris di luar cakupan

### Guard tidak dievaluasi bila aset target Allow Assign-nya Deny sesudah penghapusan
39. Maya Pengelola menghapus override Group `Tim Guard Deny Hapus {runId}`, yang bila dievaluasi akan membuat kombinasi override aset `Mesin Deny Hapus {runId}` keduanya OFF
40. Verifikasi Delete diterima dan override itu terhapus, karena nilai efektif Allow Assign aset itu Deny sesudah penghapusan

### Save Company default dengan keduanya OFF ditolak
41. Maya Pengelola menyimpan Company default dengan Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`
42. Verifikasi Save ditolak server dengan pesan `At least one assignee type must be enabled`
43. Verifikasi Allowed assignee: Employee dan Allowed assignee: Division Company default tetap `ON`, tidak ada perubahan yang tersimpan
