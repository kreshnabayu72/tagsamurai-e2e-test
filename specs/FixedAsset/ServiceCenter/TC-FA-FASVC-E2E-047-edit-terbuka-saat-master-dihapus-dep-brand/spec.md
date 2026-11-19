---
id: TC-FA-FASVC-E2E-047-edit-terbuka-saat-master-dihapus-dep-brand
title: "Master Dihapus atau Di-merge Saat Dialog Edit Terbuka: Save Ditolak, Service Center Changed, Form Terbaru"
layer: ui-e2e
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: [MR-FASVC-10c, EC-FASVC-58a, EC-FASVC-58b, DO-FASVC-09, F-FASVC-08.k10]
smoke: []
dependsOn: ["Brand: master Brand"]
trace:
  MR-FASVC-10c: [7, 24]
  EC-FASVC-58a: [7, 11, 24, 28]
  EC-FASVC-58b: [9, 10, 26, 27]
  DO-FASVC-09: [7, 24]
  F-FASVC-08.k10: [7, 16, 24, 33]
anchor: [3, 15, 20, 32]
coverage:
  web: automated
---
# Master Dihapus atau Di-merge Saat Dialog Edit Terbuka: Save Ditolak, Service Center Changed, Form Terbaru

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` (cakupan seluruh Group) menguji layar Edit-nya. Admin Brand `Dimas Pratama {runId}` (Total Control, cakupan seluruh Group) mengubah master Brand dari sesinya sendiri.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-047-1: Brand `Bosch {runId}`, Status `Active`, ada di entitas aktor, dihapus dari master oleh Admin Brand.
  - DU-047-2: Brand `Makita {runId}`, Status `Active`.
  - DU-047-3: Brand `Krisbow {runId}`, Status `Active`, di-merge ke `Ingco {runId}` oleh Admin Brand.
  - DU-047-4: Brand `Ingco {runId}`, Status `Active`, Brand tujuan merge.
  - DU-047-5: Service Center `Servis Kipas Cilacap {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands `Bosch {runId}` dan `Makita {runId}`, Country `Indonesia`, City `Cilacap`, Company phone nomor `81234500471`, Company email `servis@kipascilacap.example`, Notes `Teknisi tersedia hari kerja {runId}`, Usage `0`, Status `Active`.
  - DU-047-6: Service Center `Servis Kipas Purwokerto {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands `Krisbow {runId}`, Country `Indonesia`, City `Purwokerto`, Company phone nomor `81234500472`, Company email `servis@kipaspurwokerto.example`, Notes `Teknisi tersedia hari kerja {runId}`, Usage `0`, Status `Active`.
  - DU-047-7: Notes `Jadwal servis dipercepat {runId}`, nilai yang diketik pada dialog Edit `Servis Kipas Cilacap {runId}` lalu ditolak saat `[Save]`.
  - DU-047-8: Notes `Jadwal servis ditunda {runId}`, nilai yang diketik pada dialog Edit `Servis Kipas Purwokerto {runId}` lalu ditolak saat `[Save]`.
  - DU-047-9: User Total Control `Rina Wulandari {runId}`, cakupan seluruh Group.
  - DU-047-10: User Admin Brand `Dimas Pratama {runId}`, role Total Control, cakupan seluruh Group.

## Test Steps

### Brand dihapus saat dialog Edit terbuka: Save ditolak dan form diisi ulang dengan cakupan terbaru
1. Ketik Search `Servis Kipas Cilacap {runId}`, tekan Enter
2. Klik `⋯` pada baris `Servis Kipas Cilacap {runId}`, lalu klik `Edit`
3. Verifikasi dialog `Edit Service Center` terbuka dengan field Brands berisi `Bosch {runId}` dan `Makita {runId}`
4. Admin Brand menghapus Brand `Bosch {runId}` dari master Brand
5. Ganti isi field Notes dengan `Jadwal servis dipercepat {runId}`
6. Klik `[Save]`
7. Verifikasi dialog `Service Center Changed` tampil karena versi data dinaikkan oleh perubahan master yang menghapus Brand
8. Klik `[OK]`
9. Verifikasi dialog `Edit Service Center` tetap terbuka dan diisi ulang dengan data terbaru
10. Verifikasi field Brands berisi `Makita {runId}`
11. Verifikasi field Notes berisi `Teknisi tersedia hari kerja {runId}`, bukan `Jadwal servis dipercepat {runId}`
12. Klik `✕` pada form yang belum diubah sejak diisi ulang
13. Klik `Changelog` pada toolbar
14. Ketik Search `Servis Kipas Cilacap {runId}` pada modal `Changelog: Service Center`, tekan Enter
15. Verifikasi entri dengan Action `Updated`, Field `Brands`, Old Value `Bosch {runId}, Makita {runId}`, New Value `Makita {runId}`, dan Modified By `System` tampil
16. Verifikasi tidak ada entri dengan Field `Notes` untuk Service Center ini karena `[Save]` ditolak
17. Tutup modal `Changelog: Service Center` lewat icon close

### Brand di-merge saat dialog Edit terbuka: Save ditolak dan form diisi ulang dengan Brand hasil merge
18. Ganti isi kotak Search dengan `Servis Kipas Purwokerto {runId}`, tekan Enter
19. Klik `⋯` pada baris `Servis Kipas Purwokerto {runId}`, lalu klik `Edit`
20. Verifikasi dialog `Edit Service Center` terbuka dengan field Brands berisi `Krisbow {runId}`
21. Admin Brand me-merge Brand `Krisbow {runId}` ke Brand `Ingco {runId}` di master Brand
22. Ganti isi field Notes dengan `Jadwal servis ditunda {runId}`
23. Klik `[Save]`
24. Verifikasi dialog `Service Center Changed` tampil karena versi data dinaikkan oleh perubahan master yang me-merge Brand
25. Klik `[OK]`
26. Verifikasi dialog `Edit Service Center` tetap terbuka dan diisi ulang dengan data terbaru
27. Verifikasi field Brands berisi `Ingco {runId}`
28. Verifikasi field Notes berisi `Teknisi tersedia hari kerja {runId}`, bukan `Jadwal servis ditunda {runId}`
29. Klik `✕` pada form yang belum diubah sejak diisi ulang
30. Klik `Changelog` pada toolbar
31. Ketik Search `Servis Kipas Purwokerto {runId}` pada modal `Changelog: Service Center`, tekan Enter
32. Verifikasi entri dengan Action `Updated`, Field `Brands`, Old Value `Krisbow {runId}`, New Value `Ingco {runId}`, dan Modified By `System` tampil
33. Verifikasi tidak ada entri dengan Field `Notes` untuk Service Center ini karena `[Save]` ditolak
34. Tutup modal `Changelog: Service Center` lewat icon close
