---
id: TC-FA-FAREG-BE-128-send-mobile
title: "Send dari mobile: validasi dan batch satu aset"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-20n, FAREG-LOGIC-20o, "§9.2#p8", "§9.6#r8"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-20n: [6, 9, 10]
  FAREG-LOGIC-20o: [3, 4, 5, 13, 15, 20, 21]
  "§9.2#p8": [13, 15]
  "§9.6#r8": [3, 7, 16, 18, 25, 27, 28, 29]
owner: BE
---
# Send dari mobile: validasi dan batch satu aset

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Mataram {runId}` dan `Gudang Kupang {runId}`, pengirim dari aplikasi mobile).
- Data:
  - DU-128-1: Group `Gudang Mataram {runId}`, Assignable, di entitas aktor.
  - DU-128-2: Group `Gudang Kupang {runId}`, Assignable, di entitas aktor.
  - DU-128-3: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`.
  - DU-128-4: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-128`, TAG Type `Non-TAG`.
  - DU-128-5: Asset Name `Printer Lama {runId}`, Category `IT Equipment`, Brand `HP`, Model `LaserJet Pro`, status `Inactive`.
  - DU-128-6: Tag RFID `E280-1280-0001 {runId}`, status `Available`.
  - DU-128-7: Tag QR `QR-1280-0002 {runId}`, status `Available`.
  - DU-128-8: Tag RFID `E280-1280-0003 {runId}`, status `Available`.
  - DU-128-9: Tag RFID `E280-1280-0004 {runId}`, status `Available`.
- Kondisi:
  - Sisa kuota Group `Gudang Kupang {runId}` bernilai `0`.
  - Kuota tenant dan kuota Group `Gudang Mataram {runId}` mencukupi.
  - Register Asset Bulk Limit bernilai `100`.

## Test Steps

### Send membentuk satu batch Draft berisi satu aset
1. Rina mencatat jumlah batch Draft miliknya
2. Rina mengirim Send dari mobile dengan Group `Gudang Mataram {runId}`, Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, dan Tag RFID `E280-1280-0001 {runId}`
3. Verifikasi Send berhasil dan jumlah batch Draft milik Rina bertambah satu
4. Verifikasi batch Draft hasil Send berisi tepat satu aset dengan Quantity `1` dan Condition `Normal`, sehingga tidak melampaui Register Asset Bulk Limit
5. Verifikasi Owner batch Draft hasil Send adalah `Rina`
6. Verifikasi slot RFID aset berstatus `Verified` dengan Tag `E280-1280-0001 {runId}`
7. Verifikasi Registration Log batch memuat node `Draft created by Rina` dengan Total Asset `1`

### Tag dipetakan ke slot bertipe sama
8. Rina mengirim Send dari mobile dengan Group `Gudang Mataram {runId}`, Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, dan Tag QR `QR-1280-0002 {runId}`
9. Verifikasi Tag ditolak dengan pesan `This slot needs a RFID TAG`
10. Verifikasi slot RFID aset berstatus `Unverified`

### Send diblokir oleh validasi form yang sama
11. Rina mencatat jumlah batch Draft miliknya
12. Rina mengirim Send dari mobile tanpa Group, dengan Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, dan Tag RFID `E280-1280-0003 {runId}`
13. Verifikasi Send ditolak server dengan pesan `Group must not be empty`
14. Rina mengirim Send dari mobile dengan Group `Gudang Mataram {runId}`, Asset Name nonaktif `Printer Lama {runId}`, Brand `HP`, Model `LaserJet Pro`, dan Tag RFID `E280-1280-0004 {runId}`
15. Verifikasi Send ditolak server dengan pesan yang menyatakan Asset Name `Printer Lama {runId}` tidak tersedia
16. Verifikasi jumlah batch Draft milik Rina sama dengan catatan sebelum kedua Send yang ditolak
17. Rina mengirim Send dari mobile dengan Group `Gudang Mataram {runId}`, Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, dan Tag RFID `E280-1280-0003 {runId}`
18. Verifikasi Send berhasil dan Tag `E280-1280-0003 {runId}` terpasang pada aset batch Draft baru

### Send tidak memeriksa kuota
19. Rina mengirim Send dari mobile dengan Group `Gudang Kupang {runId}`, Asset Name `Meja Kerja {runId}`, Brand `Olympic`, dan Model `OL-128`
20. Verifikasi Send berhasil dan batch Draft berisi satu aset terbentuk di `Gudang Kupang {runId}`
21. Verifikasi sisa kuota Group `Gudang Kupang {runId}` tetap `0`

### Send tidak idempotent dan menjaga Tag tetap unik
22. Rina mencatat jumlah batch Draft miliknya
23. Rina mengirim Send dari mobile dengan Group `Gudang Mataram {runId}`, Asset Name `Meja Kerja {runId}`, Brand `Olympic`, dan Model `OL-128`
24. Rina mengirim Send yang sama sekali lagi
25. Verifikasi jumlah batch Draft milik Rina bertambah dua dari catatan sebelum kedua Send
26. Rina mengirim Send dari mobile dengan Group `Gudang Mataram {runId}`, Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, dan Tag RFID `E280-1280-0001 {runId}` yang sudah dipakai batch Draft pertama
27. Verifikasi Send ditolak server dengan pesan yang memuat Tag `E280-1280-0001 {runId}` dan status `Reserved`
28. Verifikasi jumlah batch Draft milik Rina tidak bertambah akibat Send yang ditolak

### Send tercatat di Activity Log dengan Source Mobile
29. Verifikasi Activity Log memuat entri Action `Create` atas batch Draft hasil Send dari langkah 2 dengan Source `Mobile`
