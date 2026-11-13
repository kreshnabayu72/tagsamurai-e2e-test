---
id: TC-FA-FAREG-BE-145-isi-system-log-dep-system-log
title: "System Log: peristiwa yang dipicu aktor"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-07f, "§8.1#p1", "§8.3#p4"]
smoke: []
dependsOn:
  - "System Log: daftar entri"
owner: BE
trace:
  FAREG-LOGIC-07f: 8
  "§8.1#p1": [3, 7, 11, 14, 17, 20, 23, 27, 30, 34, 37]
  "§8.3#p4": [11, 14]
---

# System Log: peristiwa yang dipicu aktor

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Solo {runId}`) sebagai pengaju.
  - Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Solo {runId}`) sebagai approver.
  - Hana T (Total Control, termasuk akses mengubah master Asset Name).
- Data:
  - DU-145-1: Group `Gudang Solo {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-145-2: Asset Name `Meja Kerja {runId}` dengan Brand `Olympic` Model `OL-145` dan Brand `Chitose` Model `Orion`, TAG Type `Non-TAG`, Status `Active`.
  - DU-145-3: batch Draft milik Rina W di Group `Gudang Solo {runId}`, Item `Meja Kerja {runId}` Quantity `2`, memenuhi Tingkat 2, Asset Code belum dialokasikan.
  - DU-145-4: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Solo {runId}` berisi `2` aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-145`.
  - DU-145-5: batch Draft milik Rina W di Group `Gudang Solo {runId}`, Item `Meja Kerja {runId}` Quantity `2`, Asset Code sudah dialokasikan.
  - DU-145-6: batch Draft milik Rina W di Group `Gudang Solo {runId}`, Item `Meja Kerja {runId}` Quantity `1`, Asset Code belum dialokasikan.
  - DU-145-7: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Solo {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-145-8: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Solo {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-145-9: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Solo {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-145-10: batch Draft milik Rina W di Group `Gudang Solo {runId}` dengan Item 1 `Meja Kerja {runId}` Quantity `3` dan Item 2 `Meja Kerja {runId}` Quantity `2`, Asset Code seluruh aset sudah dialokasikan.
  - DU-145-11: batch Draft milik Rina W di Group `Gudang Solo {runId}`, Item `Meja Kerja {runId}` Quantity `1`, memenuhi Tingkat 2.
  - DU-145-12: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Solo {runId}` berisi `1` aset `Meja Kerja {runId}`.
- Kondisi:
  - kuota Group `Gudang Solo {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.

## Test Steps

### Submit for Approval mencatat alokasi Asset Code dan kuota Reserved
1. Catat jumlah entri System Log milik aktor
2. Rina W mengirim Submit for Approval atas batch DU-145-3
3. Verifikasi System Log memuat entri alokasi Asset Code dan increment untuk kedua aset serta entri kuota Reserved

### Approve mencatat kuota Used dan koreksi approver
4. Catat jumlah entri System Log milik aktor
5. Budi menyimpan koreksi Brand aset pertama pengajuan DU-145-4 menjadi `Chitose` dengan Model `Orion`
6. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-145-4
7. Verifikasi System Log memuat entri kuota Used dengan perpindahan Reserved menjadi Used untuk kedua aset
8. Verifikasi System Log approver memuat entri koreksi Brand yang diterapkan pada aset pertama dengan Modified By `Budi`

### Delete draft mencatat Voided hanya bila Asset Code sudah beralokasi
9. Catat jumlah entri System Log milik aktor
10. Rina W menghapus batch DU-145-5 yang Asset Code-nya sudah dialokasikan
11. Verifikasi System Log memuat entri Asset Code `Voided` untuk kedua aset
12. Catat jumlah entri System Log milik aktor
13. Rina W menghapus batch DU-145-6 yang Asset Code-nya belum dialokasikan
14. Verifikasi jumlah entri System Log tidak bertambah dibanding catatan

### Reject dan Cancel registration mencatat Voided dan kuota Released
15. Catat jumlah entri System Log milik aktor
16. Budi mengirim keputusan `Reject` dengan Reason `Aset duplikat dengan pengajuan lain` untuk aset pengajuan DU-145-7
17. Verifikasi System Log memuat entri Asset Code `Voided` dan entri kuota Released untuk aset itu
18. Catat jumlah entri System Log milik aktor
19. Rina W membatalkan pengajuan DU-145-8 dengan `Save as Draft to edit` tidak tercentang
20. Verifikasi System Log memuat entri Asset Code `Voided` dan entri kuota Released untuk aset yang dibuang
21. Catat jumlah entri System Log milik aktor
22. Rina W membatalkan pengajuan DU-145-9 dengan `Save as Draft to edit` tercentang
23. Verifikasi System Log memuat entri kuota Released dan tidak memuat entri Asset Code `Voided` karena aset kembali ke Draft

### Quantity turun dan Remove Item mencatat Voided
24. Catat jumlah entri System Log milik aktor
25. Rina W menurunkan Quantity Item 1 batch DU-145-10 dari `3` menjadi `1`
26. Rina W menyimpan batch DU-145-10
27. Verifikasi System Log memuat dua entri Asset Code `Voided`, satu per aset yang dihapus
28. Catat jumlah entri System Log milik aktor
29. Rina W menghapus Item 2 batch DU-145-10 lewat Remove Item
30. Verifikasi System Log memuat dua entri Asset Code `Voided`, satu per aset pada Item yang dihapus

### Validasi ulang karena master diarsipkan dan auto-cancel tidak dicatat
31. Catat jumlah entri System Log milik aktor
32. Asset Name `Meja Kerja {runId}` diarsipkan oleh Hana T
33. Rina W menyimpan batch DU-145-11
34. Verifikasi jumlah entri System Log tidak bertambah dibanding catatan walau draft divalidasi ulang karena master diarsipkan
35. Catat jumlah entri System Log milik aktor
36. Waktu berlalu sampai Approval Timeout platform terlampaui sejak pengajuan DU-145-12 diajukan
37. Verifikasi jumlah entri System Log tidak bertambah dibanding catatan karena auto-cancel sistem tanpa aktor
