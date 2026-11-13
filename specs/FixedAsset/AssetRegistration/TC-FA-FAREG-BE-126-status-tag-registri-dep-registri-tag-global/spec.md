---
id: TC-FA-FAREG-BE-126-status-tag-registri-dep-registri-tag-global
title: "Status Tag di registri Global per aksi registrasi"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-03p, FAREG-LOGIC-04e, FAREG-LOGIC-04h, FAREG-LOGIC-04n, FAREG-LOGIC-04p, "§9.4.2#r30", "§9.4.2#r31", "§9.4.2#r54", "§9.4.2#r55", "§9.6#r9"]
smoke: []
dependsOn: ["Registri Tag Global: status Tag"]
trace:
  FAREG-LOGIC-03p: [21, 22]
  FAREG-LOGIC-04e: [14]
  FAREG-LOGIC-04h: [5, 38, 39, 46]
  FAREG-LOGIC-04n: [3, 5, 10, 14, 15, 17, 19]
  FAREG-LOGIC-04p: [34, 35, 36, 41, 42, 43, 48, 50]
  "§9.4.2#r30": [2, 5]
  "§9.4.2#r31": [12, 14, 15]
  "§9.4.2#r54": [29, 30, 32]
  "§9.4.2#r55": [24, 25]
  "§9.6#r9": [7]
owner: BE
---
# Status Tag di registri Global per aksi registrasi

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Pontianak {runId}` dan `Gudang Singkawang {runId}`, pengaju); Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Pontianak {runId}`, bukan pengaju, approver); Admin Tag (pengelola registri Tag Global, mengubah status Tag di luar modul registrasi).
- Data:
  - DU-126-1: Group `Gudang Pontianak {runId}`, Assignable, di entitas aktor.
  - DU-126-2: Group `Gudang Singkawang {runId}`, Assignable, di entitas aktor.
  - DU-126-3: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID` (satu slot Tag).
  - DU-126-4: Tag RFID `E280-1260-0001 {runId}`, status `Available`.
  - DU-126-5: Tag RFID `E280-1260-0002 {runId}`, status `Available`.
  - DU-126-6: Tag RFID `E280-1260-0003 {runId}`, status `Available`.
  - DU-126-7: Tag RFID `E280-1260-0004 {runId}`, status `To be Returned`, Return Group `Gudang Pontianak {runId}`.
  - DU-126-8: batch Draft milik Rina, Group `Gudang Pontianak {runId}`, satu Item `Laptop {runId}` Quantity `2`, slot Tag kedua aset kosong.
  - DU-126-9: batch Draft milik Rina, Group `Gudang Pontianak {runId}`, satu Item `Laptop {runId}` Quantity `1`, aset ber-Tag RFID `E280-1260-0005 {runId}`.
  - DU-126-10: Tag RFID `E280-1260-0005 {runId}`, status `Reserved` atas aset batch DU-126-9.
  - DU-126-11: batch Draft milik Rina, Group `Gudang Pontianak {runId}`, satu Item `Laptop {runId}` Quantity `2` dengan Tingkat 2 lengkap; aset pertama ber-Tag RFID `E280-1260-0006 {runId}` dan aset kedua ber-Tag RFID `E280-1260-0007 {runId}`.
  - DU-126-12: Tag RFID `E280-1260-0006 {runId}`, status `Reserved` atas aset pertama batch DU-126-11.
  - DU-126-13: Tag RFID `E280-1260-0007 {runId}`, status `Reserved` atas aset kedua batch DU-126-11.
  - DU-126-14: batch Draft milik Rina, Group `Gudang Singkawang {runId}`, satu Item `Laptop {runId}` Quantity `2` dengan Tingkat 2 lengkap; aset pertama ber-Tag RFID `E280-1260-0008 {runId}` dan aset kedua tanpa Tag.
  - DU-126-15: Tag RFID `E280-1260-0008 {runId}`, status `Reserved` atas aset pertama batch DU-126-14.
  - DU-126-16: batch Draft milik Rina, Group `Gudang Pontianak {runId}`, satu Item `Laptop {runId}` Quantity `3` dengan Tingkat 2 lengkap; aset pertama ber-Tag RFID `E280-1260-0010 {runId}`, aset kedua `E280-1260-0011 {runId}`, aset ketiga `E280-1260-0012 {runId}`.
  - DU-126-17: Tag RFID `E280-1260-0010 {runId}`, status `Reserved` atas aset pertama batch DU-126-16.
  - DU-126-18: Tag RFID `E280-1260-0011 {runId}`, status `Reserved` atas aset kedua batch DU-126-16.
  - DU-126-19: Tag RFID `E280-1260-0012 {runId}`, status `Reserved` atas aset ketiga batch DU-126-16.
  - DU-126-20: batch Draft milik Rina, Group `Gudang Pontianak {runId}`, satu Item `Laptop {runId}` Quantity `1` dengan Tingkat 2 lengkap, aset ber-Tag RFID `E280-1260-0013 {runId}`.
  - DU-126-21: Tag RFID `E280-1260-0013 {runId}`, status `Reserved` atas aset batch DU-126-20.
  - DU-126-22: batch Draft milik Rina, Group `Gudang Pontianak {runId}`, satu Item `Laptop {runId}` Quantity `1` dengan Tingkat 2 lengkap, aset ber-Tag RFID `E280-1260-0014 {runId}`.
  - DU-126-23: Tag RFID `E280-1260-0014 {runId}`, status `Reserved` atas aset batch DU-126-22.
- Kondisi:
  - Approval Workflow aktif untuk `Gudang Pontianak {runId}` dengan toggle `Require Approval for Registration` ON; untuk `Gudang Singkawang {runId}` toggle itu OFF.
  - Kuota tenant dan kuota Group `Gudang Pontianak {runId}` dan `Gudang Singkawang {runId}` mencukupi untuk seluruh aset yang diajukan spec ini.

## Test Steps

### Scan hanya memvalidasi dan Save draft menjadikan Tag Reserved
1. Rina memindai Tag RFID `E280-1260-0001 {runId}` pada slot RFID aset pertama batch DU-126-8
2. Verifikasi slot RFID aset pertama berstatus `Verified`
3. Verifikasi status Tag `E280-1260-0001 {runId}` di registri Global tetap `Available`
4. Rina mengirim Save draft atas batch DU-126-8
5. Verifikasi status Tag `E280-1260-0001 {runId}` di registri Global menjadi `Reserved` atas aset pertama batch DU-126-8
6. Rina memindai ulang Tag RFID `E280-1260-0001 {runId}` pada slot RFID aset pertama batch DU-126-8
7. Verifikasi status Tag `E280-1260-0001 {runId}` tetap `Reserved` atas aset yang sama dan hanya satu Tag terpasang pada aset itu
8. Rina memindai Tag RFID `E280-1260-0002 {runId}` pada slot RFID aset kedua batch DU-126-8 tanpa mengirim Save draft
9. Rina menutup sesi edit batch DU-126-8 tanpa mengirim Save draft
10. Verifikasi status Tag `E280-1260-0002 {runId}` di registri Global tetap `Available`

### Rescan melepas Tag lama dalam transaksi Save draft
11. Rina membuka batch DU-126-8 dan memindai Tag RFID `E280-1260-0003 {runId}` pada slot RFID aset pertama
12. Verifikasi slot RFID aset pertama berstatus `Verified` dengan Tag `E280-1260-0003 {runId}`
13. Rina mengirim Save draft atas batch DU-126-8
14. Verifikasi status Tag `E280-1260-0001 {runId}` di registri Global kembali `Available`
15. Verifikasi status Tag `E280-1260-0003 {runId}` di registri Global menjadi `Reserved` atas aset pertama batch DU-126-8

### Tag To be Returned keluar dari status itu saat Save draft
16. Rina memindai Tag RFID `E280-1260-0004 {runId}` pada slot RFID aset kedua batch DU-126-8
17. Verifikasi status Tag `E280-1260-0004 {runId}` di registri Global tetap `To be Returned`
18. Rina mengirim Save draft atas batch DU-126-8
19. Verifikasi status Tag `E280-1260-0004 {runId}` di registri Global menjadi `Reserved` atas aset kedua batch DU-126-8

### Quantity turun melepas Tag aset yang dihapus
20. Rina mengirim Save draft atas batch DU-126-8 dengan Quantity Item `Laptop {runId}` diturunkan dari `2` menjadi `1`
21. Verifikasi status Tag `E280-1260-0004 {runId}` di registri Global menjadi `Available`
22. Verifikasi status Tag `E280-1260-0003 {runId}` di registri Global tetap `Reserved` atas aset pertama batch DU-126-8

### Delete draft melepas Tag aset
23. Rina menghapus batch DU-126-9
24. Verifikasi status Tag `E280-1260-0005 {runId}` di registri Global menjadi `Available`
25. Verifikasi Tag `E280-1260-0005 {runId}` tidak terpasang pada aset mana pun

### Tag terpasang yang berubah di registri Global membuat slot Unverified saat draft dibuka
26. Admin Tag mengubah status Tag `E280-1260-0006 {runId}` di registri Global menjadi `Retired`
27. Admin Tag menghapus Tag `E280-1260-0007 {runId}` dari registri Global
28. Rina membuka batch DU-126-11
29. Verifikasi slot RFID aset pertama berstatus `Unverified` dengan peringatan untuk Tag `E280-1260-0006 {runId}`
30. Verifikasi slot RFID aset kedua berstatus `Unverified` dengan peringatan untuk Tag `E280-1260-0007 {runId}`
31. Rina mengirim Submit atas batch DU-126-11 tanpa mencentang Skip pairing
32. Verifikasi Submit ditolak server dengan pesan `Choose to submit without pairing, or pair the TAGs first.`

### Activate tanpa pairing mengubah Tag terpasang menjadi Paired
33. Rina mengirim Submit atas batch DU-126-14 dengan Skip pairing dicentang dan Reason `TAG not yet available`
34. Verifikasi slot Tag aset kedua berstatus `Skipped`
35. Verifikasi slot Tag aset pertama tetap `Verified` dengan Tag `E280-1260-0008 {runId}`
36. Verifikasi status Tag `E280-1260-0008 {runId}` di registri Global menjadi `Paired`

### Status Tag mengikuti keputusan approval
37. Rina mengirim Submit atas batch DU-126-16
38. Verifikasi ketiga aset batch DU-126-16 berstatus Waiting for Approval
39. Verifikasi status Tag `E280-1260-0010 {runId}`, `E280-1260-0011 {runId}`, dan `E280-1260-0012 {runId}` di registri Global sama-sama `Reserved`
40. Budi mengirim keputusan: aset pertama `Approve`; aset kedua `Return to Draft` dengan Reason `Warna casing tidak cocok`; aset ketiga `Reject` dengan Reason `Unit rusak saat pengiriman`
41. Verifikasi status Tag `E280-1260-0010 {runId}` di registri Global menjadi `Paired`
42. Verifikasi status Tag `E280-1260-0011 {runId}` di registri Global tetap `Reserved` atas aset kedua pada batch Draft baru
43. Verifikasi status Tag `E280-1260-0012 {runId}` di registri Global menjadi `Available`

### Status Tag mengikuti pembatalan pengajuan
44. Rina mengirim Submit atas batch DU-126-20
45. Rina mengirim Submit atas batch DU-126-22
46. Verifikasi status Tag `E280-1260-0013 {runId}` dan `E280-1260-0014 {runId}` di registri Global sama-sama `Reserved`
47. Rina membatalkan pengajuan batch DU-126-20 dengan `Save as Draft to edit` dicentang
48. Verifikasi status Tag `E280-1260-0013 {runId}` di registri Global tetap `Reserved` atas aset pada batch Draft baru
49. Rina membatalkan pengajuan batch DU-126-22 dengan `Save as Draft to edit` tidak dicentang
50. Verifikasi status Tag `E280-1260-0014 {runId}` di registri Global menjadi `Available`
