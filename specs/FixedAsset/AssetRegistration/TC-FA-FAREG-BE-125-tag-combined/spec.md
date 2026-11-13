---
id: TC-FA-FAREG-BE-125-tag-combined
title: "Tag combined: pengisian dan penolakan slot"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-04f, FAREG-LOGIC-04g, "§9.4.2#r42", "§9.4.2#r43", "§9.4.2#r44", "§9.4.2#r45", "§9.4.2#r46", "§9.4.2#r47", "§9.4.2#r48"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-04f: [2, 4]
  FAREG-LOGIC-04g: [9, 10]
  "§9.4.2#r42": [2, 4]
  "§9.4.2#r43": [12, 13]
  "§9.4.2#r44": [15, 17, 18, 19]
  "§9.4.2#r45": [21, 22]
  "§9.4.2#r46": [24, 26, 27]
  "§9.4.2#r47": [9, 10]
  "§9.4.2#r48": [6, 7]
owner: BE
---

# Tag combined: pengisian dan penolakan slot

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Palembang {runId}`).
- Data:
  - DU-125-1: Group `Gudang Palembang {runId}`, Assignable, di entitas aktor.
  - DU-125-2: Asset Name `Perangkat Ukur {runId}`, Category `Peralatan Lapangan`, Brand `Leica`, Model `TS16`, TAG Type `RFID` dan `NFC` (dua slot Tag).
  - DU-125-3: Asset Name `Perangkat Survei {runId}`, Category `Peralatan Lapangan`, Brand `Trimble`, Model `R12i`, TAG Type `RFID`, `QR`, dan `NFC` (tiga slot Tag).
  - DU-125-4: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID` (satu slot Tag).
  - DU-125-5: batch Draft milik Rina, Group `Gudang Palembang {runId}`, satu Item `Perangkat Ukur {runId}` Quantity `1`, kedua slot Tag kosong.
  - DU-125-6: batch Draft milik Rina, Group `Gudang Palembang {runId}`, satu Item `Perangkat Survei {runId}` Quantity `3`, seluruh slot Tag ketiga aset kosong.
  - DU-125-7: batch Draft milik Rina, Group `Gudang Palembang {runId}`, satu Item `Laptop {runId}` Quantity `1`, slot Tag RFID kosong.
  - DU-125-8: Tag combined `CMB-1250-0001 {runId}` berkomponen RFID dan NFC, status `Available`.
  - DU-125-9: Tag combined `CMB-1250-0002 {runId}` berkomponen RFID dan QR, status `Available`.
  - DU-125-10: Tag combined `CMB-1250-0003 {runId}` berkomponen RFID `E280-1250-0103 {runId}` berstatus `Available` dan QR `QR-1250-0003 {runId}` berstatus `Retired`.
  - DU-125-11: Tag combined `CMB-1250-0004 {runId}` berkomponen RFID `E280-1250-0104 {runId}` berstatus `Available` dan QR `QR-1250-0004 {runId}` yang tidak terdaftar di registri Global.
  - DU-125-12: Tag RFID tunggal `E280-1250-0001 {runId}`, status `Available`.
  - DU-125-13: Tag RFID tunggal `E280-1250-0002 {runId}`, status `Available`.
- Kondisi:
  - Approval Workflow tidak aktif untuk `Gudang Palembang {runId}`.

## Test Steps

### Tag combined mengisi seluruh slot terbuka
1. Rina memindai Tag combined `CMB-1250-0001 {runId}` pada slot RFID aset batch DU-125-5
2. Verifikasi slot RFID dan slot NFC aset batch DU-125-5 sama-sama berstatus `Verified`
3. Rina mengirim Save draft atas batch DU-125-5
4. Verifikasi slot RFID dan slot NFC aset tetap `Verified` sesudah Save draft

### Tag combined yang sudah terpasang tidak diterima lagi
5. Rina memindai ulang Tag combined `CMB-1250-0001 {runId}` pada slot NFC aset batch DU-125-5
6. Verifikasi pemindaian ditolak dengan pesan `This TAG is the same as the current TAG`
7. Verifikasi slot RFID dan slot NFC aset tetap berstatus `Verified`

### Rescan satu slot hasil combined mengosongkan slot pasangannya
8. Rina memindai Tag RFID `E280-1250-0002 {runId}` pada slot RFID aset batch DU-125-5
9. Verifikasi slot RFID aset berstatus `Verified` dengan Tag `E280-1250-0002 {runId}`
10. Verifikasi slot NFC aset kembali berstatus `Unverified`

### Tag combined yang hanya mencakup sebagian slot terbuka
11. Rina memindai Tag combined `CMB-1250-0002 {runId}` pada slot QR aset pertama batch DU-125-6
12. Verifikasi slot RFID dan slot QR aset pertama berstatus `Verified`
13. Verifikasi slot NFC aset pertama tetap berstatus `Unverified`

### Tag combined yang mencakup slot terisi Tag tunggal ditolak
14. Rina memindai Tag RFID `E280-1250-0001 {runId}` pada slot RFID aset kedua batch DU-125-6
15. Verifikasi pemindaian diterima dan slot RFID aset kedua berstatus `Verified`
16. Rina memindai Tag combined `CMB-1250-0002 {runId}` pada slot QR aset kedua batch DU-125-6
17. Verifikasi pemindaian ditolak dengan pesan `This combined TAG doesn't match the open slots`
18. Verifikasi slot RFID aset kedua tetap berstatus `Verified` dengan Tag `E280-1250-0001 {runId}`
19. Verifikasi slot QR aset kedua tetap berstatus `Unverified`

### Tag combined pada aset dengan satu slot ditolak
20. Rina memindai Tag combined `CMB-1250-0001 {runId}` pada slot RFID aset batch DU-125-7
21. Verifikasi pemindaian ditolak dengan pesan `This TAG is combined. It can only fill multiple slots.`
22. Verifikasi slot RFID aset batch DU-125-7 tetap berstatus `Unverified`

### Komponen yang gagal validasi menolak seluruh pemindaian
23. Rina memindai Tag combined `CMB-1250-0003 {runId}` pada slot RFID aset ketiga batch DU-125-6
24. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `QR-1250-0003 {runId}` dan status `Retired`
25. Rina memindai Tag combined `CMB-1250-0004 {runId}` pada slot RFID aset ketiga batch DU-125-6
26. Verifikasi pemindaian ditolak dengan pesan `Error, can't recognize TAG.`
27. Verifikasi slot RFID, slot QR, dan slot NFC aset ketiga sama-sama berstatus `Unverified`
