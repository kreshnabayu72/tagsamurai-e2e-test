---
id: TC-FA-FAREG-BE-140-entitas-suspended-expired
title: "Entitas Suspended atau Expired: semua aksi tulis ditolak"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [F-FAREG-05.k3, FAREG-LOGIC-21d, "§9.4.2#r64", "§9.4.2#r65", "§9.4.2#r66", "§9.4.2#r67", "§9.4.2#r68", EB-AKS-7]
smoke: []
dependsOn: []
owner: BE
trace:
  F-FAREG-05.k3: [2, 6, 8, 10, 12, 14, 22, 26, 28, 30, 32, 34, 42]
  FAREG-LOGIC-21d: [22, 42, 56, 57]
  "§9.4.2#r64": [6, 26]
  "§9.4.2#r65": [8, 28]
  "§9.4.2#r66": [10, 30]
  "§9.4.2#r67": [12, 32]
  "§9.4.2#r68": [14, 34]
  EB-AKS-7: [22, 42]
---

# Entitas Suspended atau Expired: semua aksi tulis ditolak

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Pusat {runId}`) sebagai pengaju.
  - Lina (Manage asset & TAG, Group terkelola `Gudang Pusat {runId}`).
  - Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Pusat {runId}`) sebagai approver.
  - Operator Admin Console yang mengubah status entitas.
- Data:
  - DU-140-1: entitas khusus `Entitas Registrasi Status {runId}` berstatus `Active`, tidak dipakai spec lain.
  - DU-140-5: Group `Gudang Pusat {runId}` di entitas `Entitas Registrasi Status {runId}`, ber-toggle `Require Approval for Registration` ON.
  - DU-140-6: Asset Name `Meja Kerja {runId}` dengan Brand `Olympic` Model `OL-140` dan Brand `Chitose` Model `Orion`, TAG Type `Non-TAG`, Status `Active`.
  - DU-140-22: Asset Name `Kursi Lipat {runId}` dengan Brand `Olympic` Model `KL-140`, TAG Type `RFID`, Status `Active`.
  - DU-140-7: batch Draft milik Rina W di Group `Gudang Pusat {runId}`, Item `Meja Kerja {runId}` Quantity `2`, memenuhi Tingkat 2.
  - DU-140-8: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Pusat {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-140-9: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Pusat {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-140-10: batch Draft milik Rina W di Group `Gudang Pusat {runId}`, Item `Meja Kerja {runId}` Quantity `1`.
  - DU-140-11: aset `Active` `Meja Kerja {runId}` dengan Alias Name `Meja Rapat {runId}`.
  - DU-140-12: batch Draft milik Rina W di Group `Gudang Pusat {runId}`, Item `Kursi Lipat {runId}` Quantity `1`, slot Tag aset pertama kosong.
  - DU-140-18: Tag RFID `E280-1400-0001 {runId}`, status `Available` di registri Global, belum terpasang pada aset mana pun.
  - DU-140-13: batch Draft milik Rina W di Group `Gudang Pusat {runId}`, Item `Meja Kerja {runId}` Quantity `1`, kunci sesi edit dipegang Rina W.
  - DU-140-14: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Pusat {runId}` berisi `1` aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-140`.
  - DU-140-15: batch Draft milik Rina W di Group `Gudang Pusat {runId}`, Item `Meja Kerja {runId}` Quantity `2`.
- Kondisi:
  - spec ini memakai entitas khusus `Entitas Registrasi Status {runId}` yang tidak dipakai spec lain, dengan status awal `Active`.
  - kuota Group `Gudang Pusat {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.
  - pada langkah Grace Period, entitas berada di masa Grace Period.

## Test Steps

### Entitas Active menerima aksi tulis
1. Rina W menyimpan batch DU-140-7 dengan Quantity `3`
2. Verifikasi Save diterima server saat entitas `Active` dan Quantity batch menjadi `3`

### Entitas Suspended: semua aksi tulis ditolak
3. Operator Admin Console mengubah status entitas `Entitas Registrasi Status {runId}` menjadi `Suspended`
4. Catat jumlah batch Draft Rina W
5. Rina W menyimpan batch DU-140-7 dengan Quantity `4`
6. Verifikasi Save draft ditolak server dengan copy `Changes can't be saved while this workspace is suspended or expired.` dan Quantity batch tetap `3`
7. Rina W mengirim Activate atas batch DU-140-7
8. Verifikasi Activate ditolak server dengan copy yang sama dan batch tetap Draft tanpa pengajuan baru
9. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-140-8
10. Verifikasi keputusan ditolak server dengan copy yang sama dan pengajuan DU-140-8 tetap `Waiting for Approval`
11. Rina W menghapus batch DU-140-10
12. Verifikasi Delete draft ditolak server dengan copy yang sama dan batch DU-140-10 tetap ada
13. Rina W mengirim Send dari aplikasi mobile untuk batch Draft baru di Group `Gudang Pusat {runId}`
14. Verifikasi Send ditolak server dengan copy yang sama dan jumlah batch Draft Rina W sama dengan catatan
15. Rina W mengirim autosave atas batch DU-140-7 dengan Quantity `4`
16. Rina W membatalkan pengajuan DU-140-9
17. Rina W mengubah Alias Name aset DU-140-11 menjadi `Meja Tamu {runId}`
18. Rina W memindai Tag `E280-1400-0001 {runId}` pada aset pertama batch DU-140-12
19. Lina mengambil alih sesi edit batch DU-140-13 dengan Take over
20. Budi menyimpan koreksi Brand aset pertama pengajuan DU-140-14 menjadi `Chitose` dengan Model `Orion`
21. Rina W menerapkan Apply to all pada batch DU-140-15
22. Verifikasi autosave, Cancel registration, Edit Active, Scan Tag, Take over, Simpan koreksi, dan Apply to all ditolak server dengan copy `Changes can't be saved while this workspace is suspended or expired.` tanpa mutasi

### Entitas Expired: semua aksi tulis ditolak
23. Operator Admin Console mengubah status entitas `Entitas Registrasi Status {runId}` menjadi `Expired`
24. Catat jumlah batch Draft Rina W
25. Rina W menyimpan batch DU-140-7 dengan Quantity `4`
26. Verifikasi Save draft ditolak server dengan copy `Changes can't be saved while this workspace is suspended or expired.` dan Quantity batch tetap `3`
27. Rina W mengirim Activate atas batch DU-140-7
28. Verifikasi Activate ditolak server dengan copy yang sama dan batch tetap Draft tanpa pengajuan baru
29. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-140-8
30. Verifikasi keputusan ditolak server dengan copy yang sama dan pengajuan DU-140-8 tetap `Waiting for Approval`
31. Rina W menghapus batch DU-140-10
32. Verifikasi Delete draft ditolak server dengan copy yang sama dan batch DU-140-10 tetap ada
33. Rina W mengirim Send dari aplikasi mobile untuk batch Draft baru di Group `Gudang Pusat {runId}`
34. Verifikasi Send ditolak server dengan copy yang sama dan jumlah batch Draft Rina W sama dengan catatan
35. Rina W mengirim autosave atas batch DU-140-7 dengan Quantity `4`
36. Rina W membatalkan pengajuan DU-140-9
37. Rina W mengubah Alias Name aset DU-140-11 menjadi `Meja Tamu {runId}`
38. Rina W memindai Tag `E280-1400-0001 {runId}` pada aset pertama batch DU-140-12
39. Lina mengambil alih sesi edit batch DU-140-13 dengan Take over
40. Budi menyimpan koreksi Brand aset pertama pengajuan DU-140-14 menjadi `Chitose` dengan Model `Orion`
41. Rina W menerapkan Apply to all pada batch DU-140-15
42. Verifikasi autosave, Cancel registration, Edit Active, Scan Tag, Take over, Simpan koreksi, dan Apply to all ditolak server dengan copy `Changes can't be saved while this workspace is suspended or expired.` tanpa mutasi

### Entitas di masa Grace Period tidak memblokir aksi apa pun
43. Operator Admin Console mengubah status entitas `Entitas Registrasi Status {runId}` menjadi masa Grace Period
44. Rina W menyimpan batch DU-140-7 dengan Quantity `5`
45. Rina W mengirim autosave atas batch DU-140-7 dengan Quantity `5`
46. Rina W mengirim Activate atas batch DU-140-7
47. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-140-8
48. Rina W membatalkan pengajuan DU-140-9
49. Rina W menghapus batch DU-140-10
50. Rina W mengubah Alias Name aset DU-140-11 menjadi `Meja Tamu {runId}`
51. Rina W memindai Tag `E280-1400-0001 {runId}` pada aset pertama batch DU-140-12
52. Lina mengambil alih sesi edit batch DU-140-13 dengan Take over
53. Budi menyimpan koreksi Brand aset pertama pengajuan DU-140-14 menjadi `Chitose` dengan Model `Orion`
54. Rina W menerapkan Apply to all pada batch DU-140-15
55. Rina W mengirim Send dari aplikasi mobile untuk batch Draft baru di Group `Gudang Pusat {runId}`
56. Verifikasi seluruh aksi tulis di atas diterima server tanpa penolakan karena status entitas
57. Verifikasi batch Draft baru dari Send tampil pada daftar batch Draft Rina W
