---
id: TC-FA-FASVC-E2E-045-notifikasi-event-dep-notification
title: "Notifikasi: Inactive Otomatis, Cakupan Dipersempit atau Melebar, dan Schedule Terdampak"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.8#p1", "§9.8#r1", "§9.8#r2", "§9.8#r3", "§9.8#r4", "§9.8#r5", FASVC-LOGIC-05d, MR-FASVC-02d, MR-FASVC-04d, MR-FASVC-06d, MR-FASVC-09c, MR-FASVC-10c, EC-FASVC-10e, EC-FASVC-14c, EC-FASVC-49c, EC-FASVC-39b, MR-FASVC-07d]
smoke: []
dependsOn: ["Notification: daftar Notifikasi", "Group: pohon Group dan master Group", "Category: pohon Category dan master Category", "Brand: master Brand", "Maintenance Routine: Schedule dan Task"]
trace:
  "§9.8#p1": 19
  "§9.8#r1": 5
  "§9.8#r2": [16, 44, 54]
  "§9.8#r3": [30, 33]
  "§9.8#r4": 19
  "§9.8#r5": 27
  FASVC-LOGIC-05d: 5
  MR-FASVC-02d: 19
  MR-FASVC-04d: 30
  MR-FASVC-06d: 33
  MR-FASVC-09c: [30, 33]
  MR-FASVC-10c: 33
  EC-FASVC-10e: 16
  EC-FASVC-14c: 30
  EC-FASVC-49c: 33
  EC-FASVC-39b: [19, 25, 27]
  MR-FASVC-07d: 22
anchor: []
coverage:
  web: automated
---
# Notifikasi: Inactive Otomatis, Cakupan Dipersempit atau Melebar, dan Schedule Terdampak

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` (cakupan seluruh Group) menguji layarnya dan meng-inactivate serta mengedit Service Center. Admin `Dimas Pratama {runId}` (Total Control, cakupan seluruh Group) memicu perubahan master dari sesinya sendiri. Penerima notifikasi adalah pembuat Service Center (Total Control) dan Asset Admin Schedule (Role Transaksi Maintenance Routine), masing-masing akun milik spec ini dengan akun aktif dan kredensial yang disediakan fase 2.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-045-1: Group `Cabang Kediri {runId}`, parent root pohon Group entitas aktor, dihapus oleh Admin, Available to Service Center habis, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-2: Group `Cabang Blitar {runId}`, parent root pohon Group entitas aktor, di-Inactivate oleh Admin, Available to Service Center habis, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-3: Group `Cabang Jember {runId}`, parent root pohon Group entitas aktor, dihapus oleh Admin, Available to Service Center habis, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-4: Group `Cabang Probolinggo {runId}`, parent root pohon Group entitas aktor, tempat Service Center yang di-Inactivate Total Control, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-5: Group `Cabang Banyuwangi {runId}`, parent root pohon Group entitas aktor, tempat Service Center ber-Specialization satu Category, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-6: Group `Cabang Situbondo {runId}`, parent root pohon Group entitas aktor, tempat Service Center ber-Brands satu Brand, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-7: Group `Cabang Lumajang {runId}`, parent root pohon Group entitas aktor, Group yang tetap ada di Available to, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-8: Group `Cabang Bondowoso {runId}`, parent root pohon Group entitas aktor, Group yang dilepas lewat Edit saat dipakai Schedule, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-9: Category `Spesialis Genset {runId}`, parent root pohon Category entitas aktor, satu-satunya Category di Specialization `Servis Genset Banyuwangi {runId}`.
  - DU-045-10: Brand `Yanmar {runId}`, Status `Active`, satu-satunya Brand di Brands `Servis Genset Situbondo {runId}`.
  - DU-045-11: Service Center `Servis Genset Kediri {runId}`, dibuat oleh `Citra Kediri {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Kediri {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Kediri`, Company phone nomor `81234500451`, Company email `servis@gensetkediri.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-12: Service Center `Servis Genset Blitar {runId}`, dibuat oleh `Citra Blitar {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Blitar {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Blitar`, Company phone nomor `81234500452`, Company email `servis@gensetblitar.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-13: Service Center `Servis Genset Jember {runId}`, dibuat oleh `Citra Jember {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Jember {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Jember`, Company phone nomor `81234500453`, Company email `servis@gensetjember.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-14: Service Center `Servis Genset Probolinggo {runId}`, dibuat oleh `Rina Wulandari {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Probolinggo {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Probolinggo`, Company phone nomor `81234500454`, Company email `servis@gensetprobolinggo.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-15: Service Center `Servis Genset Banyuwangi {runId}`, dibuat oleh `Rina Wulandari {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Banyuwangi {runId}`, Specialization `Spesialis Genset {runId}`, Brands kosong (`All brands`), Country `Indonesia`, City `Banyuwangi`, Company phone nomor `81234500455`, Company email `servis@gensetbanyuwangi.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-16: Service Center `Servis Genset Situbondo {runId}`, dibuat oleh `Rina Wulandari {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Situbondo {runId}`, Specialization kosong (`All categories`), Brands `Yanmar {runId}`, Country `Indonesia`, City `Situbondo`, Company phone nomor `81234500456`, Company email `servis@gensetsitubondo.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-17: Service Center `Servis Genset Lumajang {runId}`, dibuat oleh `Rina Wulandari {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Bondowoso {runId}` dan `Cabang Lumajang {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Lumajang`, Company phone nomor `81234500457`, Company email `servis@gensetlumajang.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-18: Aset `Genset Jember {runId}`, Group `Cabang Jember {runId}`, tanpa Brand, Category `Genset`.
  - DU-045-19: Aset `Genset Probolinggo {runId}`, Group `Cabang Probolinggo {runId}`, tanpa Brand, Category `Genset`.
  - DU-045-20: Aset `Genset Bondowoso {runId}`, Group `Cabang Bondowoso {runId}`, tanpa Brand, Category `Genset`.
  - DU-045-21: Schedule `Servis Berkala Jember {runId}`, Status `Active`, mode aset terpilih `Genset Jember {runId}`, pelaksana default `Servis Genset Jember {runId}`, Asset Admin Schedule `Fajar Jember {runId}`.
  - DU-045-22: Schedule `Servis Berkala Probolinggo {runId}`, Status `Active`, mode aset terpilih `Genset Probolinggo {runId}`, pelaksana default `Servis Genset Probolinggo {runId}`, Asset Admin Schedule `Fajar Probolinggo {runId}`.
  - DU-045-23: Schedule `Servis Berkala Lumajang {runId}`, Status `Active`, mode aset terpilih `Genset Bondowoso {runId}`, pelaksana default `Servis Genset Lumajang {runId}`, Asset Admin Schedule `Fajar Lumajang {runId}`.
  - DU-045-24: User `Rina Wulandari {runId}`, role Total Control, cakupan seluruh Group, aktor penguji, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-25: User `Dimas Pratama {runId}`, role Total Control, cakupan seluruh Group, Admin pemicu perubahan master, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-26: User `Citra Kediri {runId}`, role Total Control, cakupan seluruh Group, pembuat `Servis Genset Kediri {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-27: User `Citra Blitar {runId}`, role Total Control, cakupan seluruh Group, pembuat `Servis Genset Blitar {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-28: User `Citra Jember {runId}`, role Total Control, cakupan seluruh Group, pembuat `Servis Genset Jember {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-29: User `Fajar Jember {runId}`, role Asset Admin (Role Transaksi Maintenance Routine), cakupan Cabang Jember {runId}, Asset Admin Schedule `Servis Berkala Jember {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-30: User `Fajar Probolinggo {runId}`, role Asset Admin (Role Transaksi Maintenance Routine), cakupan Cabang Probolinggo {runId}, Asset Admin Schedule `Servis Berkala Probolinggo {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-31: User `Fajar Banyuwangi {runId}`, role Asset Admin (Role Transaksi Maintenance Routine), cakupan Cabang Banyuwangi {runId}, Asset Admin dalam Available to `Servis Genset Banyuwangi {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-32: User `Fajar Situbondo {runId}`, role Asset Admin (Role Transaksi Maintenance Routine), cakupan Cabang Situbondo {runId}, Asset Admin dalam Available to `Servis Genset Situbondo {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-33: User `Fajar Lumajang {runId}`, role Asset Admin (Role Transaksi Maintenance Routine), cakupan Cabang Bondowoso {runId} dan Cabang Lumajang {runId}, Asset Admin Schedule `Servis Berkala Lumajang {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-34: Group `Cabang Pamekasan {runId}`, parent root pohon Group entitas aktor, tempat Service Center yang Specialization-nya dipersempit, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-35: Group `Cabang Sampang {runId}`, parent root pohon Group entitas aktor, tempat Service Center yang Brands-nya dipersempit, tanpa aset dan user kecuali dinyatakan di entri lain.
  - DU-045-36: Category `Spesialis Pompa {runId}`, parent root pohon Category entitas aktor, dilepas dari Specialization `Servis Pompa Pamekasan {runId}` lewat Edit.
  - DU-045-37: Category `Spesialis Kompresor {runId}`, parent root pohon Category entitas aktor, tetap di Specialization `Servis Pompa Pamekasan {runId}`.
  - DU-045-38: Brand `Grundfos {runId}`, Status `Active`, dilepas dari Brands `Servis Pompa Sampang {runId}` lewat Edit.
  - DU-045-39: Brand `Ebara {runId}`, Status `Active`, tetap di Brands `Servis Pompa Sampang {runId}`.
  - DU-045-40: Service Center `Servis Pompa Pamekasan {runId}`, dibuat oleh `Rina Wulandari {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Pamekasan {runId}`, Specialization `Spesialis Kompresor {runId}` dan `Spesialis Pompa {runId}`, Brands kosong (`All brands`), Country `Indonesia`, City `Pamekasan`, Company phone nomor `81234500458`, Company email `servis@pompapamekasan.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-41: Service Center `Servis Pompa Sampang {runId}`, dibuat oleh `Rina Wulandari {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Sampang {runId}`, Specialization kosong (`All categories`), Brands `Ebara {runId}` dan `Grundfos {runId}`, Country `Indonesia`, City `Sampang`, Company phone nomor `81234500459`, Company email `servis@pompasampang.example`, Usage sesuai Schedule di bawah, Status `Active`.
  - DU-045-42: Aset `Pompa Pamekasan {runId}`, Group `Cabang Pamekasan {runId}`, tanpa Brand, Category `Spesialis Pompa {runId}`.
  - DU-045-43: Aset `Pompa Sampang {runId}`, Group `Cabang Sampang {runId}`, Brand `Grundfos {runId}`, Category `Genset`.
  - DU-045-44: Schedule `Servis Berkala Pamekasan {runId}`, Status `Active`, mode aset terpilih `Pompa Pamekasan {runId}`, pelaksana default `Servis Pompa Pamekasan {runId}`, Asset Admin Schedule `Fajar Pamekasan {runId}`.
  - DU-045-45: Schedule `Servis Berkala Sampang {runId}`, Status `Active`, mode aset terpilih `Pompa Sampang {runId}`, pelaksana default `Servis Pompa Sampang {runId}`, Asset Admin Schedule `Fajar Sampang {runId}`.
  - DU-045-46: User `Fajar Pamekasan {runId}`, role Asset Admin (Role Transaksi Maintenance Routine), cakupan Cabang Pamekasan {runId}, Asset Admin Schedule `Servis Berkala Pamekasan {runId}` dan Asset Admin dalam Available to `Servis Pompa Pamekasan {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).
  - DU-045-47: User `Fajar Sampang {runId}`, role Asset Admin (Role Transaksi Maintenance Routine), cakupan Cabang Sampang {runId}, Asset Admin Schedule `Servis Berkala Sampang {runId}` dan Asset Admin dalam Available to `Servis Pompa Sampang {runId}`, notifikasi Unread `0` (badge notifikasi tidak tampil).

## Test Steps

### Service Center di-Inactivate saat dipakai Schedule aktif: Asset Admin Schedule diberi notifikasi
1. Ketik Search `Servis Genset Probolinggo {runId}`, tekan Enter
2. Klik `⋯` pada baris `Servis Genset Probolinggo {runId}`, lalu klik `Inactivate`
3. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
4. Ganti akun ke Asset Admin `Fajar Probolinggo {runId}`
5. Verifikasi angka badge notifikasi pada ikon bell adalah `1`

### Available to dipersempit saat dipakai Schedule aktif: Asset Admin dalam Available to diberi notifikasi
6. Ganti akun ke Total Control `Rina Wulandari {runId}`
7. Buka Add-ons > Service Center lewat sidebar
8. Ketik Search `Servis Genset Lumajang {runId}`, tekan Enter
9. Klik `⋯` pada baris `Servis Genset Lumajang {runId}`, lalu klik `Edit`
10. Klik field Available to untuk membuka tree
11. Hapus centang `Cabang Bondowoso {runId}` pada tree Available to
12. Klik `[Select]` pada dialog pilihan Available to
13. Klik `[Save]`
14. Klik `[Save]` pada dialog `Narrow Coverage`
15. Ganti akun ke Asset Admin `Fajar Lumajang {runId}`
16. Verifikasi angka badge notifikasi pada ikon bell adalah `1`

### Available to habis karena Group dihapus: pembuat diberi notifikasi
17. Admin `Dimas Pratama {runId}` menghapus Group `Cabang Kediri {runId}` dari master Group
18. Ganti akun ke Total Control `Citra Kediri {runId}`
19. Verifikasi angka badge notifikasi pada ikon bell adalah `1`

### Available to habis karena Group di-Inactivate: pembuat diberi notifikasi
20. Admin `Dimas Pratama {runId}` meng-inactivate Group `Cabang Blitar {runId}` di master Group
21. Ganti akun ke Total Control `Citra Blitar {runId}`
22. Verifikasi angka badge notifikasi pada ikon bell adalah `1`

### Available to habis saat dipakai Schedule aktif: pembuat dan Asset Admin Schedule diberi notifikasi
23. Admin `Dimas Pratama {runId}` menghapus Group `Cabang Jember {runId}` dari master Group
24. Ganti akun ke Total Control `Citra Jember {runId}`
25. Verifikasi angka badge notifikasi pada ikon bell adalah `1`
26. Ganti akun ke Asset Admin `Fajar Jember {runId}`
27. Verifikasi angka badge notifikasi pada ikon bell adalah `1`

### Category satu-satunya di Specialization dihapus: Asset Admin dalam Available to diberi notifikasi
28. Admin `Dimas Pratama {runId}` menghapus Category `Spesialis Genset {runId}` dari master Category
29. Ganti akun ke Asset Admin `Fajar Banyuwangi {runId}`
30. Verifikasi angka badge notifikasi pada ikon bell adalah `1`

### Brand satu-satunya di Brands dihapus: Asset Admin dalam Available to diberi notifikasi
31. Admin `Dimas Pratama {runId}` menghapus Brand `Yanmar {runId}` dari master Brand
32. Ganti akun ke Asset Admin `Fajar Situbondo {runId}`
33. Verifikasi angka badge notifikasi pada ikon bell adalah `1`

### Specialization dipersempit saat dipakai Schedule aktif: Asset Admin dalam Available to diberi notifikasi
34. Ganti akun ke Total Control `Rina Wulandari {runId}`
35. Buka Add-ons > Service Center lewat sidebar
36. Ketik Search `Servis Pompa Pamekasan {runId}`, tekan Enter
37. Klik `⋯` pada baris `Servis Pompa Pamekasan {runId}`, lalu klik `Edit`
38. Klik field Specialization untuk membuka tree
39. Hapus centang `Spesialis Pompa {runId}` pada tree Specialization
40. Klik `[Select]` pada dialog pilihan Specialization
41. Klik `[Save]`
42. Klik `[Save]` pada dialog `Narrow Coverage`
43. Ganti akun ke Asset Admin `Fajar Pamekasan {runId}`
44. Verifikasi angka badge notifikasi pada ikon bell adalah `1`

### Brands dipersempit saat dipakai Schedule aktif: Asset Admin dalam Available to diberi notifikasi
45. Ganti akun ke Total Control `Rina Wulandari {runId}`
46. Buka Add-ons > Service Center lewat sidebar
47. Ketik Search `Servis Pompa Sampang {runId}`, tekan Enter
48. Klik `⋯` pada baris `Servis Pompa Sampang {runId}`, lalu klik `Edit`
49. Klik field Brands untuk membuka daftar pilihan
50. Hapus centang `Grundfos {runId}` pada daftar pilihan Brands
51. Klik `[Save]`
52. Klik `[Save]` pada dialog `Narrow Coverage`
53. Ganti akun ke Asset Admin `Fajar Sampang {runId}`
54. Verifikasi angka badge notifikasi pada ikon bell adalah `1`
