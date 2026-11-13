---
id: TC-FA-FAREG-BE-143-isi-activity-log-dep-activity-log
title: "Activity Log: entri per aksi registrasi"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-07f, FAREG-LOGIC-21b, "§8#r1", "§8#r3", "§8#b1", "§8.2#p2", "§8.2#p3", "§8.3#p4", "§9.6#r1", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§9.6#r5", "§9.6#r6", "§9.6#r7", "§9.6#r9", "§9.6#r11", "§9.6#r13", "§9.6#r14", "§9.6#r15"]
smoke: []
dependsOn:
  - "Activity Log: daftar entri"
owner: BE
trace:
  FAREG-LOGIC-07f: [21, 22]
  FAREG-LOGIC-21b: [51, 54, 57, 60]
  "§8#r1": 3
  "§8#r3": 6
  "§8#b1": [3, 21]
  "§8.2#p2": [14, 51, 54, 57, 60]
  "§8.2#p3": [3, 14, 21, 26, 29, 32]
  "§8.3#p4": 29
  "§9.6#r1": [3, 6]
  "§9.6#r2": [8, 11]
  "§9.6#r3": 14
  "§9.6#r4": 20
  "§9.6#r5": [24, 26]
  "§9.6#r6": 29
  "§9.6#r7": 32
  "§9.6#r9": [35, 38]
  "§9.6#r11": 18
  "§9.6#r13": 42
  "§9.6#r14": 45
  "§9.6#r15": 48
---

# Activity Log: entri per aksi registrasi

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Jakarta {runId}` dan `Gudang Bandung {runId}`) sebagai pengaju dan pelaku aksi draft.
  - Lina (Manage asset & TAG, Group terkelola `Gudang Jakarta {runId}`).
  - Agus P (Group Manager Group `Gudang Jakarta {runId}`) sebagai approver.
- Data:
  - DU-143-1: Group `Gudang Jakarta {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-143-2: Group `Gudang Bandung {runId}`, ber-toggle `Require Approval for Registration` OFF, ada di entitas aktor.
  - DU-143-3: Asset Name `Meja Kerja {runId}` dengan Brand `Olympic` Model `OL-143` dan Brand `Chitose` Model `Orion`, TAG Type `Non-TAG`, Status `Active`.
  - DU-143-4: Asset Name `Kursi Kantor {runId}`, Brand `Chitose`, Model `Orion K`, TAG Type `Non-TAG`, Status `Active`.
  - DU-143-5: Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, Status `Active`.
  - DU-143-7: batch Draft milik Rina W di Group `Gudang Bandung {runId}`, Item `Kursi Kantor {runId}` Quantity `12`, memenuhi Tingkat 2.
  - DU-143-8: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Jakarta {runId}` berisi `2` aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-143`.
  - DU-143-9: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Jakarta {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-143-10: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Jakarta {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-143-11: batch Draft milik Rina W di Group `Gudang Jakarta {runId}`, Item `Kursi Kantor {runId}` Quantity `2`.
  - DU-143-12: batch Draft milik Rina W di Group `Gudang Jakarta {runId}`, Item `Kursi Kantor {runId}` Quantity `1`.
  - DU-143-13: batch Draft milik Lina di Group `Gudang Jakarta {runId}`, Item `Kursi Kantor {runId}` Quantity `1`, kunci sesi edit dipegang Lina.
  - DU-143-14: batch Draft milik Rina W di Group `Gudang Jakarta {runId}`, Item `Laptop {runId}` Quantity `1`.
  - DU-143-15: batch Draft milik Rina W di Group `Gudang Jakarta {runId}` dengan Item 1 `Meja Kerja {runId}` Quantity `4`, Item 2 `Kursi Kantor {runId}` Quantity `2`, dan Item 3 `Laptop {runId}` Quantity `3`.
- Kondisi:
  - kuota Group `Gudang Jakarta {runId}` dan `Gudang Bandung {runId}` serta kuota tenant cukup untuk seluruh pengajuan di atas.
  - tabel di sub tab Draft, Waiting for Approval, History, dan antrean Approvals memuat baris data uji.

## Test Steps

### Save draft mencatat satu entri per aset
1. Catat jumlah entri Activity Log milik Rina W
2. Rina W menyimpan batch Draft baru DU-143-6 di Group `Gudang Jakarta {runId}` berisi `3` aset `Meja Kerja {runId}`
3. Verifikasi Activity Log memuat tiga entri baru, satu per aset, dengan Action `Create`, Object `Registration`, Source `Manual`, dan Modified By `Rina W`
4. Rina W mengubah Brand aset pertama batch DU-143-6 dari `Olympic` menjadi `Chitose` dengan Model `Orion`
5. Rina W menyimpan batch DU-143-6
6. Verifikasi Activity Log memuat entri baru dengan Action `Edit`, Field `Brand`, Old Value `Olympic`, New Value `Chitose`, dan Source `Manual`

### Autosave mencatat entri hanya bila ada perubahan
7. Rina W mengirim autosave atas batch DU-143-6 dengan Alias Name aset pertama `Meja Rapat {runId}`
8. Verifikasi Activity Log memuat satu entri baru dengan Field `Alias Name` dan New Value `Meja Rapat {runId}`
9. Catat jumlah entri Activity Log milik Rina W
10. Rina W mengirim autosave atas batch DU-143-6 tanpa perubahan apa pun
11. Verifikasi jumlah entri Activity Log tidak bertambah dibanding catatan

### Activate banyak aset mencatat satu entri per aset
12. Catat jumlah entri Activity Log milik Rina W
13. Rina W mengirim Activate atas batch DU-143-7 berisi `12` aset
14. Verifikasi Activity Log memuat dua belas entri baru, satu per aset, dengan Action `Activate`, Field `Status`, Old Value `Draft`, New Value `Active`, Source `Manual`, dan Modified By `Rina W`

### Keputusan approval dan koreksi approver dicatat saat Approve
15. Catat jumlah entri Activity Log milik Agus P
16. Agus P menyimpan koreksi Brand aset pertama pengajuan DU-143-8 menjadi `Chitose` dengan Model `Orion`
17. Agus P menyimpan koreksi Brand aset kedua pengajuan DU-143-8 menjadi `Chitose` dengan Model `Orion`
18. Verifikasi jumlah entri Activity Log tidak bertambah dibanding catatan setelah kedua koreksi disimpan
19. Agus P mengirim satu keputusan atas pengajuan DU-143-8: aset pertama `Approve`, aset kedua `Return to Draft` dengan Reason `Foto aset belum jelas`
20. Verifikasi Activity Log memuat entri Action `Approve`, Field `Status`, Old Value `Waiting for Approval`, New Value `Active`, dan Modified By `Agus P` untuk aset pertama serta entri Action `Return` untuk aset kedua
21. Verifikasi Activity Log memuat tepat satu entri Action `Correct`, Field `Brand`, Old Value `Olympic`, New Value `Chitose`, Source `Approver correction`, dan Modified By `Agus P` untuk aset pertama
22. Verifikasi Activity Log tidak memuat entri koreksi untuk aset kedua karena aset itu tidak disetujui

### Cancel registration dan auto-cancel sistem dicatat
23. Rina W membatalkan pengajuan DU-143-9
24. Verifikasi Activity Log memuat entri pembatalan dengan Action `Cancel` dan Modified By `Rina W`
25. Waktu berlalu sampai Approval Timeout platform terlampaui sejak pengajuan DU-143-10 diajukan
26. Verifikasi Activity Log memuat entri pembatalan pengajuan itu dengan Modified By `System`

### Delete draft dan Bulk Delete mencatat satu entri per aset terdampak
27. Catat jumlah entri Activity Log milik Rina W
28. Rina W menghapus batch DU-143-11 berisi `2` aset
29. Verifikasi Activity Log memuat dua entri baru dengan Action `Delete`, satu per aset, dan batch yang dihapus tidak lagi memiliki Registration Log yang dapat dibuka
30. Catat jumlah entri Activity Log milik Rina W
31. Rina W menjalankan Bulk Delete atas batch DU-143-12 dan batch DU-143-13
32. Verifikasi Activity Log memuat satu entri `Delete` baru untuk aset batch DU-143-12 dan tidak memuat entri untuk batch DU-143-13 yang dilewati karena kuncinya dipegang Lina

### Scan dan Rescan Tag dicatat
33. Rina W memindai Tag `E280-1430-0001 {runId}` pada aset pertama batch DU-143-14
34. Rina W menyimpan batch DU-143-14
35. Verifikasi Activity Log memuat entri dengan Action `Scan Tag`, Field `Tag`, Old Value `—`, dan New Value `E280-1430-0001 {runId}`
36. Rina W memindai ulang aset pertama batch DU-143-14 dengan Tag `E280-1430-0002 {runId}`
37. Rina W menyimpan batch DU-143-14
38. Verifikasi Activity Log memuat entri dengan Field `Tag`, Old Value `E280-1430-0001 {runId}`, dan New Value `E280-1430-0002 {runId}`

### Quantity turun, Remove Item, dan Apply to all dicatat per aset
39. Catat jumlah entri Activity Log milik Rina W
40. Rina W menurunkan Quantity Item 1 batch DU-143-15 dari `4` menjadi `2`
41. Rina W menyimpan batch DU-143-15
42. Verifikasi Activity Log memuat dua entri baru, satu per aset increment terakhir yang dihapus
43. Catat jumlah entri Activity Log milik Rina W
44. Rina W menghapus Item 2 batch DU-143-15 yang berisi `2` aset lewat Remove Item
45. Verifikasi Activity Log memuat dua entri baru, satu per aset pada Item yang dihapus
46. Catat jumlah entri Activity Log milik Rina W
47. Rina W menerapkan Apply to all dengan Alias Name `Meja Direksi {runId}` pada Item 3 batch DU-143-15 yang berisi `3` aset
48. Verifikasi Activity Log memuat tiga entri baru, satu per aset pada Item 3

### Download mencatat satu entri Activity Log
49. Catat jumlah entri Activity Log milik Rina W
50. Rina W mengunduh data dari sub tab Draft
51. Verifikasi Activity Log memuat satu entri baru `[User] exported [Filename]` dengan User `Rina W` dan Filename sama dengan nama berkas yang diunduh dari sub tab Draft
52. Catat jumlah entri Activity Log milik Rina W
53. Rina W mengunduh data dari sub tab Waiting for Approval
54. Verifikasi Activity Log memuat satu entri baru `[User] exported [Filename]` dengan User `Rina W` dan Filename sama dengan nama berkas yang diunduh dari sub tab Waiting for Approval
55. Catat jumlah entri Activity Log milik Rina W
56. Rina W mengunduh data dari sub tab History
57. Verifikasi Activity Log memuat satu entri baru `[User] exported [Filename]` dengan User `Rina W` dan Filename sama dengan nama berkas yang diunduh dari sub tab History
58. Catat jumlah entri Activity Log milik Rina W
59. Rina W mengunduh data dari antrean Approvals
60. Verifikasi Activity Log memuat satu entri baru `[User] exported [Filename]` dengan User `Rina W` dan Filename sama dengan nama berkas yang diunduh dari antrean Approvals
