---
id: TC-FA-ASSIGN-E2E-010-tab-drafts-tampilan
title: "Tab Drafts: kolom, urutan awal, dan Draft hasil timeout"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-20, "§4.1#r4", "§9.5#r2", EC-ASG-78]
smoke: []
dependsOn: []
trace:
  T-ASG-20: [2, 3, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 21, 23, 25, 27, 29, 31, 33, 52, 53, 55, 56, 57]
  "§4.1#r4": 6
  "§9.5#r2": 7
  EC-ASG-78: [37, 40, 44, 48]
anchor: [5]
coverage:
  web: automated
---

# Tab Drafts: kolom, urutan awal, dan Draft hasil timeout

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-010-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-010-2: Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`.
  - DU-010-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}` dan `Branch Surabaya {runId}`; ia pembuat Draft DU-010-6, DU-010-7, DU-010-12, dan DU-010-13 dan tampil sebagai `Agus P`, dari `Agus Prasetyo {runId}`.
  - DU-010-4: User `Budi Santoso {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-010-5: User `Sari Dewi {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Sari D`, dari `Sari Dewi {runId}`.
  - DU-010-6: Draft `New` untuk Assignee DU-010-4 di Group `Head Office {runId}`, aset `Laptop Dell Latitude 5440 {runId}` dan `Monitor Dell P2422H {runId}`, Total Asset `2`, dibuat `Agus Prasetyo {runId}`; dibuat pertama.
  - DU-010-7: Draft `Restored` hasil Cancel dengan `Save as Draft to edit` untuk Assignee DU-010-5 di Group `Branch Surabaya {runId}`, aset `Mesin Fotokopi Ricoh {runId}` yang tidak layak karena sedang berada di ASG aktif DU-010-9, Total Asset `1 ⚠`, diubah `Agus Prasetyo {runId}`; dibuat kedua.
  - DU-010-8: Draft `Restored by system` hasil penutupan otomatis ASG karena tidak diserahkan dalam Transaction timeout, untuk Assignee Division `Finance {runId}` dengan aset `Kursi Ergotec A {runId}` di Group `Head Office {runId}` dan `Kursi Ergotec B {runId}` di Group `Branch Surabaya {runId}`, Total Asset `2`, diubah `System`; dibuat ketiga.
  - DU-010-9: ASG berstatus `Waiting for Approval` untuk Assignee DU-010-4 dengan aset `Mesin Fotokopi Ricoh {runId}`, Group `Branch Surabaya {runId}`, Total Asset `1`; ia yang membuat aset Draft DU-010-7 tidak layak.
  - DU-010-10: User `Rina Wijaya {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Rina W`, dari `Rina Wijaya {runId}`.
  - DU-010-11: User `Wulan Hartati {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Wulan H`, dari `Wulan Hartati {runId}`.
  - DU-010-12: Draft `New` untuk Assignee DU-010-10 di Group `Head Office {runId}`, aset `Printer Epson L3250 {runId}`, Total Asset `1`, dibuat `Agus Prasetyo {runId}`; terakhir diubah T0 − 1 hari; dibuat keempat.
  - DU-010-13: Draft `New` untuk Assignee DU-010-11 di Group `Head Office {runId}`, aset `Scanner Fujitsu fi-7160 {runId}`, Total Asset `1`, dibuat `Agus Prasetyo {runId}`; terakhir diubah T0 − 5 hari; dibuat kelima.
  - DU-010-14: Acuan waktu T0 adalah tanggal dan waktu saat spec dijalankan; Draft DU-010-6 sampai DU-010-8 terakhir diubah pada T0.

## Test Steps

### Tab Drafts dan isi kolom
1. Klik tab `Drafts`
2. Verifikasi URL memuat `?tab=drafts` dan tab `Drafts` menjadi tab yang aktif
3. Verifikasi teks bantu `Drafts don't reserve assets. Submit to lock them.` tampil di atas tabel
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi tabel memuat tepat 5 Draft, yaitu Draft untuk Assignee `Budi S`, `Sari D`, `Finance {runId}`, `Rina W`, dan `Wulan H`
6. Verifikasi header kolom tampil berurutan dari kiri ke kanan setelah kolom checkbox: `Assignee`, `Assignee Type`, `Group`, `Total Asset`, `Origin`, `Modified By`, `Last Updated`
7. Verifikasi urutan awal baris dari atas ke bawah menurut Last Updated terbaru: `Finance {runId}`, `Sari D`, `Budi S`, `Rina W`, `Wulan H`
8. Arahkan kursor ke kolom `Last Updated` baris `Budi S`
9. Verifikasi teks hover `Today` tampil karena Draft terakhir diubah hari ini
10. Verifikasi Draft tidak punya nomor ASG sehingga tidak ada kolom `Transaction ID`
11. Verifikasi kolom `Assignee Type` menampilkan `Employee` pada baris `Budi S` dan `Sari D`, dan `Division` pada baris `Finance {runId}`
12. Verifikasi kolom `Group` baris `Finance {runId}` menampilkan satu badge Group diikuti `+1`
13. Verifikasi kolom `Total Asset` menampilkan `2` pada baris `Budi S`, `1 ⚠` pada baris `Sari D`, dan `2` pada baris `Finance {runId}`
14. Verifikasi kolom `Origin` menampilkan `New` pada baris `Budi S`, `Restored` pada baris `Sari D`, dan `Restored by system` pada baris `Finance {runId}`
15. Verifikasi baris `Sari D` dan baris `Finance {runId}` memuat baris kedua `Restored from` diikuti Transaction ID asalnya pada kolom `Assignee`
16. Verifikasi kolom `Modified By` menampilkan `Agus P` pada baris `Budi S` dan `Sari D`, dan `System` pada baris `Finance {runId}`
17. Klik `⋯` pada baris `Budi S`
18. Verifikasi menu aksi baris memuat `Edit` dan `Delete`
19. Tutup menu aksi baris

### Hover kolom dan pembukaan Draft
20. Arahkan kursor ke kolom `Last Updated` baris `Rina W`
21. Verifikasi teks hover `1 day ago` tampil
22. Arahkan kursor ke kolom `Last Updated` baris `Wulan H`
23. Verifikasi teks hover `5 days ago` tampil
24. Arahkan kursor ke kolom `Assignee` baris `Budi S`
25. Verifikasi `Budi Santoso {runId}` tampil sebagai nama lengkap Assignee pada hover tab `Drafts`
26. Arahkan kursor ke kolom `Group` baris `Finance {runId}`
27. Verifikasi daftar Group `Head Office {runId}` dan `Branch Surabaya {runId}` tampil pada hover baris `Finance {runId}`
28. Arahkan kursor ke kolom `Total Asset` baris `Sari D`
29. Verifikasi daftar aset memuat `Mesin Fotokopi Ricoh {runId}` dengan keterangan tidak layak karena sedang berada di ASG aktif
30. Arahkan kursor ke kolom `Origin` baris `Sari D`
31. Verifikasi Transaction ID ASG asal Draft DU-010-7 tampil
32. Klik nama Assignee `Budi S`
33. Verifikasi form Edit draft terbuka dengan Assignee `Budi S`
34. Tutup form Edit draft yang belum diubah

### Filter Origin memisahkan Draft hasil sistem
35. Klik `Filter`
36. Klik field `Origin`
37. Verifikasi opsi `Restored by system`, `Restored`, dan `New` tampil
38. Pilih opsi `Restored by system` pada field `Origin`
39. Klik `[Apply]`
40. Verifikasi baris `Finance {runId}` tampil dan baris `Budi S` dan `Sari D` tidak tampil
41. Hapus pilihan `Restored by system` pada field `Origin`
42. Pilih opsi `Restored` pada field `Origin`
43. Klik `[Apply]`
44. Verifikasi baris `Sari D` tampil dan baris `Budi S` dan `Finance {runId}` tidak tampil
45. Hapus pilihan `Restored` pada field `Origin`
46. Pilih opsi `New` pada field `Origin`
47. Klik `[Apply]`
48. Verifikasi baris `Budi S`, `Rina W`, dan `Wulan H` tampil dan baris `Sari D` dan `Finance {runId}` tidak tampil

### Filter Assignee Type memisahkan Draft Employee dan Division
49. Klik `[Clear Field]`
50. Pilih opsi `Division` pada field `Assignee Type`
51. Klik `[Apply]`
52. Verifikasi baris `Finance {runId}` tampil karena Assignee Type `Division`
53. Verifikasi baris `Budi S`, `Sari D`, `Rina W`, dan `Wulan H` tidak tampil karena Assignee Type `Employee`

### Field filter dan placeholder tab Drafts
54. Klik `[Clear Field]`
55. Verifikasi field filter `Assignee`, `Assignee Type`, `Group`, `Total Asset`, `Origin`, `Modified By`, dan `Last Updated` tampil
56. Verifikasi placeholder `All assignees`, `All types`, `All groups`, `All origins`, dan `All users` tampil pada field dropdown masing-masing
57. Verifikasi field `Total Asset` memuat input `Min` dan `Max`, serta field `Last Updated` memuat placeholder `Select date`
