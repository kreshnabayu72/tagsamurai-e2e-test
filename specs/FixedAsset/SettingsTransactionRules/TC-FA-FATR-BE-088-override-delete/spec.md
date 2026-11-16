---
id: TC-FA-FATR-BE-088-override-delete
title: "Delete override baris dan bulk"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§Aturan Logika Modul#r45", "§4.1#r348", FI-01sampaiFI-14, "§9.2#b116", "§9.2#b117", "§9.2#b126", "§9.2#b162", "§9.2#b163", "§9.2#b180", "§9.2#b189", "§9.2#b190", "§9.4.1#r19", "§9.4.2#r78", "§9.4.2#r79", "§9.4.2#r80", "§9.4.2#r117", "§9.4.2#r118", "§9.4.4#r26", "§9.6#r3", "§9.6#r26", "§9.6#r29", "§9.10.4#b3"]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#r45": [16, 18]
  "§4.1#r348": [3, 5]
  FI-01sampaiFI-14: [9, 29, 31, 33]
  "§9.2#b116": 13
  "§9.2#b117": 10
  "§9.2#b126": 22
  "§9.2#b162": 7
  "§9.2#b163": 8
  "§9.2#b180": 27
  "§9.2#b189": 13
  "§9.2#b190": 12
  "§9.4.1#r19": 8
  "§9.4.2#r78": 13
  "§9.4.2#r79": 12
  "§9.4.2#r80": [3, 4]
  "§9.4.2#r117": 7
  "§9.4.2#r118": 8
  "§9.4.4#r26": 10
  "§9.6#r3": [5, 27]
  "§9.6#r26": [7, 15, 18, 20]
  "§9.6#r29": 8
  "§9.10.4#b3": [24, 35]
---
# Delete override baris dan bulk

## Prerequisites
- Aktor: Maya Pengelola (DU-088-1), Total Control dengan cakupan seluruh Group; Sari Penata (DU-088-2), Group Role Manage asset & TAG (Read, Update) pada Group `Tim Hapus Lingkup {runId}` beserta turunannya; dan Budi Penyunting (DU-088-3), Total Control dengan cakupan seluruh Group.
- Data:
  - DU-088-1: User, pengelola yang menghapus override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-088-2: User, pengelola Group yang hanya berhak pada satu Group beserta turunannya: Name `Sari Penata {runId}`; Group Role `Manage asset & TAG (Read, Update)`; Cakupan `Group Tim Hapus Lingkup {runId} beserta turunannya`.
  - DU-088-3: User, pengelola kedua yang menghapus override lebih dulu: Name `Budi Penyunting {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-088-4: Category, Category leaf dengan Allowed assignee: Division nilai sendiri OFF: Name `Penghapusan Guard {runId}`.
  - DU-088-5: Category, Category leaf untuk override biasa: Name `Penghapusan Biasa {runId}`.
  - DU-088-6: Group, Group dalam cakupan Sari Penata: Name `Tim Hapus Lingkup {runId}`.
  - DU-088-7: Group, Group turunan dalam cakupan Sari Penata: Name `Seksi Hapus Lingkup {runId}`; Parent `Tim Hapus Lingkup {runId}`.
  - DU-088-8: Group, Group di luar cakupan Sari Penata: Name `Tim Hapus Luar {runId}`.
  - DU-088-9: Group, Group di luar cakupan Sari Penata yang overridenya akan ditolak guard bila dievaluasi: Name `Tim Hapus Luar Guard {runId}`.
  - DU-088-10: Group, Group target override biasa milik Maya Pengelola: Name `Tim Hapus Plain {runId}`.
  - DU-088-11: Asset, aset di Group dalam cakupan Sari Penata: Name `Perangkat Hapus Lingkup {runId}`; Asset Name `Perangkat Hapus {runId}`; Category `Penghapusan Guard {runId}`; Group `Tim Hapus Lingkup {runId}`.
  - DU-088-12: Asset, aset di Group di luar cakupan: Name `Perangkat Luar Guard {runId}`; Asset Name `Perangkat Hapus {runId}`; Category `Penghapusan Guard {runId}`; Group `Tim Hapus Luar Guard {runId}`.
  - DU-088-13: Override, override Group dalam cakupan yang akan ditolak guard bila dihapus: Scope `Group`; Target `Tim Hapus Lingkup {runId}`; Category `Penghapusan Guard {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Division`; Value `ON`.
  - DU-088-14: Override, override aset yang membuat kombinasi OFF/OFF bila override Group dihapus: Scope `aset`; Target `Perangkat Hapus Lingkup {runId}`; Category `Penghapusan Guard {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Employee`; Value `OFF`.
  - DU-088-15: Override, override Group di luar cakupan Sari Penata: Scope `Group`; Target `Tim Hapus Luar {runId}`; Category `Penghapusan Guard {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-16: Override, override Group turunan dalam cakupan yang boleh dihapus: Scope `Group`; Target `Seksi Hapus Lingkup {runId}`; Category `Penghapusan Guard {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-17: Override, override Group di luar cakupan yang juga akan ditolak guard bila dievaluasi: Scope `Group`; Target `Tim Hapus Luar Guard {runId}`; Category `Penghapusan Guard {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Division`; Value `ON`.
  - DU-088-18: Override, override aset di luar cakupan yang membuat kombinasi OFF/OFF bila override Group dihapus: Scope `aset`; Target `Perangkat Luar Guard {runId}`; Category `Penghapusan Guard {runId}`; Transaksi `penugasan`; Field `Allowed assignee: Employee`; Value `OFF`.
  - DU-088-19: Override, override Group biasa milik Maya Pengelola yang boleh dihapus: Scope `Group`; Target `Tim Hapus Plain {runId}`; Category `Penghapusan Guard {runId}`; Transaksi `penugasan`; Field `Max assets per assignee (concurrent)`; Value `2`.
  - DU-088-20: Group, Group target override yang dihapus bersama lima Group lain (5 record): Name `Tim Hapus Banyak {n} {runId}`.
  - DU-088-21: Override, override Group untuk bulk Delete banyak baris yang seluruhnya boleh dihapus (5 record): Scope `Group`; Target `Tim Hapus Banyak {n} {runId}`; Category `Penghapusan Biasa {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-22: Group, Group target Delete satu baris: Name `Tim Hapus Satu {runId}`.
  - DU-088-23: Override, override Group untuk Delete satu baris: Scope `Group`; Target `Tim Hapus Satu {runId}`; Category `Penghapusan Biasa {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-24: Group, Group target bulk Delete satu baris: Name `Tim Hapus Dua {runId}`.
  - DU-088-25: Override, override Group untuk bulk Delete tepat satu baris: Scope `Group`; Target `Tim Hapus Dua {runId}`; Category `Penghapusan Biasa {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-26: Group, Group excess pada masa Grace: Name `Tim Excess Hapus {runId}`.
  - DU-088-27: Override, override Group excess yang boleh dihapus: Scope `Group`; Target `Tim Excess Hapus {runId}`; Category `Penghapusan Biasa {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-28: Group, Group yang sudah dihapus dengan override yang tertinggal: Name `Tim Dihapus Lama {runId}`.
  - DU-088-29: Override, override pada Group yang sudah dihapus, tampil tidak berlaku: Scope `Group`; Target `Tim Dihapus Lama {runId}`; Category `Penghapusan Biasa {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-30: Group, Group target override yang dihapus dua kali: Name `Tim Dihapus Dua Kali {runId}`.
  - DU-088-31: Override, override yang dihapus Budi Penyunting lalu dihapus lagi oleh Maya Pengelola: Scope `Group`; Target `Tim Dihapus Dua Kali {runId}`; Category `Penghapusan Biasa {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-32: Override, override pembanding pada Group yang sama dengan Category lain yang harus tetap ada: Scope `Group`; Target `Tim Dihapus Dua Kali {runId}`; Category `Penghapusan Guard {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-33: Group, Group target Add override yang dievaluasi ulang guard: Name `Tim Kirim Ulang {runId}`.
  - DU-088-34: Asset, aset di Group target Add override: Name `Perangkat Kirim Ulang {runId}`; Asset Name `Perangkat Hapus {runId}`; Category `Penghapusan Biasa {runId}`; Group `Tim Kirim Ulang {runId}`.
  - DU-088-35 dan DU-088-36 adalah nilai input Add override yang dikirim di blok guard Submit ulang.
  - DU-088-37: Asset Name, Asset Name excess pada masa Grace: Name `Nama Excess Hapus {runId}`; Category `Penghapusan Biasa {runId}`.
  - DU-088-38: Override, override Asset Name excess yang boleh dihapus: Scope `Asset Name`; Target `Nama Excess Hapus {runId}`; Category `Penghapusan Biasa {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-088-39: Asset, aset di Group target Delete satu baris: Name `Perangkat Hapus Satu {runId}`; Asset Name `Perangkat Hapus {runId}`; Category `Penghapusan Biasa {runId}`; Group `Tim Hapus Satu {runId}`.
- Kondisi:
  - Category `Penghapusan Guard {runId}` memiliki Allowed assignee: Division nilai sendiri `OFF` dan Allowed assignee: Employee `ON`; override pada Category itu yang memuat Allowed assignee: Division `ON` adalah satu-satunya penyebab kombinasi override aset tetap tidak OFF/OFF.
  - Transaksi Borrow disebut «transaksi peminjaman» dan transaksi Assign disebut «transaksi penugasan» di langkah.
  - Seluruh override di Data sudah aktif sebelum langkah pertama dan hanya berhubungan dengan targetnya masing-masing.
  - Group `Tim Excess Hapus {runId}` dan Asset Name `Nama Excess Hapus {runId}` berstatus excess pada masa Grace, dan Group `Tim Dihapus Lama {runId}` sudah dihapus sehingga overridenya tampil sebagai tidak berlaku.
  - Allow Assign bernilai `Allow` pada Company default dan Inherit pada Category `Penghapusan Guard {runId}`; spec ini tidak mengubahnya, sehingga penolakan guard Allowed assignee berlaku untuk aset yang nilai efektif Allow Assign-nya bukan Deny.
  - Category `Penghapusan Biasa {runId}` pada transaksi Borrow: Max duration nilai sendiri `9`; field lainnya Inherit.

## Test Steps

### Bulk Delete yang seluruh barisnya dilewati tidak menghapus apa pun dan tidak menulis log
1. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log untuk Category `Penghapusan Guard {runId}`
2. Sari Penata menghapus bulk override Group `Tim Hapus Lingkup {runId}`, yang akan ditolak guard Allowed assignee, dan override Group `Tim Hapus Luar {runId}`, yang di luar cakupannya
3. Verifikasi tidak ada override yang terhapus: override Group `Tim Hapus Lingkup {runId}` dan override Group `Tim Hapus Luar {runId}` masih ada
4. Verifikasi hasil Delete menyebut hanya override Group `Tim Hapus Lingkup {runId}` sebagai ditolak guard, dan tidak menyebut override Group `Tim Hapus Luar {runId}` yang di luar cakupan
5. Verifikasi Changelog dan Activity Log untuk Category `Penghapusan Guard {runId}` tidak bertambah entri

### Bulk Delete campuran: baris dalam cakupan diproses dan baris di luar cakupan dilewati tanpa evaluasi guard
6. Sari Penata menghapus bulk override Group `Tim Hapus Luar Guard {runId}`, yang di luar cakupannya, dan override Group `Seksi Hapus Lingkup {runId}`, yang dalam cakupannya
7. Verifikasi override Group `Seksi Hapus Lingkup {runId}` terhapus, karena baris yang boleh dihapus diproses
8. Verifikasi override Group `Tim Hapus Luar Guard {runId}` masih ada, karena baris di luar cakupan dilewati
9. Verifikasi override Group `Tim Hapus Luar Guard {runId}` dilaporkan dilewati karena di luar cakupan dan bukan sebagai ditolak guard, karena guard hanya dievaluasi pada baris yang boleh dihapus role
10. Verifikasi hasil Delete adalah hasil sebagian: satu override terhapus dan satu dilewati

### Bulk Delete: baris yang ditolak guard dilewati seperti baris di luar cakupan
11. Maya Pengelola menghapus bulk override Group `Tim Hapus Lingkup {runId}`, yang akan ditolak guard Allowed assignee, dan override Group `Tim Hapus Plain {runId}`
12. Verifikasi override Group `Tim Hapus Plain {runId}` terhapus
13. Verifikasi override Group `Tim Hapus Lingkup {runId}` masih ada karena baris yang ditolak guard dilewati seperti baris di luar cakupan

### Bulk Delete banyak baris yang seluruhnya boleh dihapus
14. Maya Pengelola menghapus bulk override untuk lima Group `Tim Hapus Banyak {n} {runId}` pada Category `Penghapusan Biasa {runId}`
15. Verifikasi kelima override terhapus dan tidak ada yang dilewati

### Delete satu baris dan bulk satu baris menghapus override yang dipilih
16. Verifikasi nilai efektif Max duration untuk aset `Perangkat Hapus Satu {runId}` adalah `5`, dari override Group `Tim Hapus Satu {runId}` pada Category `Penghapusan Biasa {runId}` yang masih aktif tanpa batas waktu
17. Maya Pengelola menghapus override Group `Tim Hapus Satu {runId}`
18. Verifikasi override itu terhapus dan nilai efektif Max duration untuk aset `Perangkat Hapus Satu {runId}` kembali `9`, mengikuti Category `Penghapusan Biasa {runId}`, karena override berlaku sampai dihapus
19. Maya Pengelola menghapus bulk override Group `Tim Hapus Dua {runId}`, tepat satu baris
20. Verifikasi override Group `Tim Hapus Dua {runId}` terhapus

### Override yang target atau Category-nya sudah dihapus tetap dapat dihapus
21. Maya Pengelola menghapus override Group `Tim Dihapus Lama {runId}`, yang tampil tidak berlaku karena Group-nya sudah dihapus
22. Verifikasi override itu terhapus dengan aturan Delete yang sama seperti baris lain

### Delete override pada target excess diterima seperti biasa
23. Maya Pengelola menghapus override Group `Tim Excess Hapus {runId}`, Group yang berstatus excess
24. Verifikasi override itu terhapus, karena Delete tidak memeriksa status excess

### Delete atas override yang sudah dihapus pengguna lain tidak menimbulkan efek ganda
25. Budi Penyunting menghapus override Group `Tim Dihapus Dua Kali {runId}` pada Category `Penghapusan Biasa {runId}`
26. Maya Pengelola menghapus override Group `Tim Dihapus Dua Kali {runId}` yang sama, yang sudah hilang
27. Verifikasi tidak ada efek ganda: override pembanding Group `Tim Dihapus Dua Kali {runId}` pada Category `Penghapusan Guard {runId}` tetap ada

### Submit Add override berikutnya mengevaluasi ulang guard Allowed assignee
28. Maya Pengelola menambahkan override Group `Tim Kirim Ulang {runId}` pada Category `Penghapusan Biasa {runId}` untuk transaksi penugasan dengan Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`
29. Verifikasi Add override ditolak dengan pesan `At least one assignee type must be enabled`, dan tidak ada override untuk Group `Tim Kirim Ulang {runId}`
30. Maya Pengelola mengirim ulang Add override yang sama tanpa mengubah isinya
31. Verifikasi Submit berikutnya mengevaluasi ulang kombinasi itu dan menolaknya lagi dengan pesan `At least one assignee type must be enabled`
32. Maya Pengelola menambahkan override Group `Tim Kirim Ulang {runId}` pada Category `Penghapusan Biasa {runId}` untuk transaksi penugasan dengan Allowed assignee: Employee `OFF` dan Allowed assignee: Division `ON`
33. Verifikasi Add override diterima setelah kombinasi diperbaiki

### Delete override pada target Asset Name excess diterima seperti biasa
34. Maya Pengelola menghapus override Asset Name `Nama Excess Hapus {runId}`, Asset Name yang berstatus excess
35. Verifikasi override itu terhapus, karena Delete tidak memeriksa status excess
