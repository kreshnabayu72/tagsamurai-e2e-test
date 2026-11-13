---
id: TC-FA-FAREG-E2E-096-mobile-registrasi-send
title: "Registrasi mobile: Scan, Photo, data aset, dan Send"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FAREG-11", "FAREG-LOGIC-20d", "FAREG-LOGIC-20j", "FAREG-LOGIC-20n", "FAREG-LOGIC-20o", "§4.6#p1", "§9.4.2#r59", "§9.6#r8", "§9.7#r3"]
smoke: []
dependsOn: []
trace:
  "F-FAREG-11": [3, 6]
  "FAREG-LOGIC-20d": [12, 34, 36, 38, 43]
  "FAREG-LOGIC-20j": [3, 34, 36, 38, 40]
  "FAREG-LOGIC-20n": [31]
  "FAREG-LOGIC-20o": [16]
  "§4.6#p1": [3, 6, 12, 16]
  "§9.4.2#r59": 16
  "§9.6#r8": 16
  "§9.7#r3": [16, 19]
coverage:
  android: manual
---

# Registrasi mobile: Scan, Photo, data aset, dan Send

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
- Layar awal: layar Scan pada Registrasi mobile.
- Data:
  - DU-096-1: Tag RFID `E28068940000500AB1C00961{runId}` berstatus `Available`.
  - DU-096-2: Tag NFC `04A2B9C3D45E80{runId}` berstatus `Available`.
  - DU-096-3: Asset Name `Laptop` dengan Brand `Dell`, Model `Latitude 5440`, dan TAG Type `RFID`.
  - DU-096-4: Group `Gudang 1 {runId}`, belum memiliki batch Draft.
  - DU-096-5: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
  - DU-096-6: Batch Draft hasil Send dengan Group `Gudang 1 {runId}`, Requested By `Rina W`, satu aset (Quantity `1`, Condition `Normal`).
  - DU-096-7: Tag RFID `E28068940000500AB1C00962{runId}` berstatus `To be Returned` dengan Return Group `Gudang 1 {runId}`.
  - DU-096-8: Tag RFID `E28068940000500AB1C00963{runId}` berstatus `Paired`. Pesan penolakan yang diharapkan `E28068940000500AB1C00963{runId} is not available (Paired)`, dari template `[TAG Code] is not available ([Status])` dengan TAG Code `E28068940000500AB1C00963{runId}` dan Status `Paired`.
  - DU-096-9: Tag RFID `E28068940000500AB1C00964{runId}` berstatus `Reserved`. Pesan penolakan yang diharapkan `E28068940000500AB1C00964{runId} is not available (Reserved)`, dari template `[TAG Code] is not available ([Status])` dengan TAG Code `E28068940000500AB1C00964{runId}` dan Status `Reserved`.
  - DU-096-10: Tag RFID `E28068940000500AB1C00965{runId}` berstatus `Retired`. Pesan penolakan yang diharapkan `E28068940000500AB1C00965{runId} is not available (Retired)`, dari template `[TAG Code] is not available ([Status])` dengan TAG Code `E28068940000500AB1C00965{runId}` dan Status `Retired`.
- Kondisi:
  - Perangkat tersambung ke server.

## Test Steps

### Send tanpa Group ditolak dengan error validasi inline
1. Buka layar Scan pada Registrasi mobile
2. Pindai Tag `E28068940000500AB1C00961{runId}` dengan perangkat
3. Verifikasi Tag `E28068940000500AB1C00961{runId}` tertahan di layar Scan
4. Lanjut ke layar Photo
5. Ambil satu Photo dengan kamera perangkat
6. Verifikasi satu Photo tampil di layar Photo
7. Lanjut ke layar `Asset Name, Brand, Model & Group`
8. Pilih Asset Name `Laptop`
9. Pilih Brand `Dell`
10. Pilih Model `Latitude 5440`
11. Klik `Send`
12. Verifikasi error inline `Group must not be empty` tampil pada layar `Asset Name, Brand, Model & Group`

### Send membentuk batch Draft satu aset
13. Pilih Group `Gudang 1 {runId}`
14. Klik `Send`
15. Buka sub tab `Draft`
16. Verifikasi tepat satu card Draft dengan Group `Gudang 1 {runId}` dan Requested By `Rina W` tampil
17. Klik `[⋯]` pada card `Gudang 1 {runId}`
18. Klik `Registration Log`
19. Verifikasi Registration Log memuat entri `Draft created by Rina W`
20. Tutup bottom sheet Registration Log

### Send dengan Tag bertipe tidak cocok ditolak
21. Buka layar Scan pada Registrasi mobile
22. Pindai Tag `04A2B9C3D45E80{runId}` dengan perangkat
23. Lanjut ke layar Photo
24. Ambil satu Photo dengan kamera perangkat
25. Lanjut ke layar `Asset Name, Brand, Model & Group`
26. Pilih Asset Name `Laptop`
27. Pilih Brand `Dell`
28. Pilih Model `Latitude 5440`
29. Pilih Group `Gudang 1 {runId}`
30. Klik `Send`
31. Verifikasi pesan `This slot needs a RFID TAG` tampil untuk Tag `04A2B9C3D45E80{runId}`

### Error inline pada layar Scan dan layar Photo
32. Buka layar Scan pada Registrasi mobile
33. Pindai Tag `E28068940000500AB1C00963{runId}` dengan perangkat
34. Verifikasi error inline `E28068940000500AB1C00963{runId} is not available (Paired)` tampil pada layar Scan
35. Pindai Tag `E28068940000500AB1C00964{runId}` dengan perangkat
36. Verifikasi error inline `E28068940000500AB1C00964{runId} is not available (Reserved)` tampil pada layar Scan
37. Pindai Tag `E28068940000500AB1C00965{runId}` dengan perangkat
38. Verifikasi error inline `E28068940000500AB1C00965{runId} is not available (Retired)` tampil pada layar Scan
39. Pindai Tag `E28068940000500AB1C00962{runId}` dengan perangkat
40. Verifikasi Tag `E28068940000500AB1C00962{runId}` tertahan di layar Scan
41. Lanjut ke layar Photo
42. Pilih berkas Photo `foto-laptop.gif` dari galeri perangkat
43. Verifikasi error inline `Unsupported format. Please upload JPG, PNG, or JPEG.` tampil pada layar Photo
