---
id: TC-FA-DAMAGED-UI-113-dialog-mark-as-repaired-tampilan-awal
title: "Dialog Mark as Repaired: header record, bagian Scan TAG hanya untuk aset ber-TAG, label After photo wajib atau opsional menurut setting, Repair note, footer, dan aksesibilitas"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-02, "§4.2.4#p2", "§4.4#r7", FI-DMG-11, FI-DMG-12, S-DMG-07, "§9.2#b16", FLD-DMG-04, EB-FRM-7@mark-as-repaired]
smoke: []
dependsOn: []
trace:
  D-DMG-02: [2, 8, 9]
  "§4.2.4#p2": [2, 3, 4, 6, 7, 8, 9, 11, 12]
  "§4.4#r7": [2]
  FI-DMG-11: [15]
  FI-DMG-12: [7]
  S-DMG-07: [7, 15]
  "§9.2#b16": [5, 13]
  FLD-DMG-04: [15, 18]
  EB-FRM-7@mark-as-repaired: [20, 21, 22, 23, 25, 27, 29, 31, 33, 35, 38]
anchor: []
coverage:
  web: automated
---

# Dialog Mark as Repaired: header record, bagian Scan TAG hanya untuk aset ber-TAG, label After photo wajib atau opsional menurut setting, Repair note, footer, dan aksesibilitas

## Prerequisites
- Aktor: Aktor Damaged pada Group aset.
- Layar awal: Dialog Mark as Repaired belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Mark as Repaired (D-DMG-02)
- Data:
  - DU-113-1: record `Damaged` untuk aset `Laptop Dell Latitude 5420 - 6`, Asset ID `LPT-2026-0006`, Group `Head Office`, berstatus `Damaged`, memiliki TAG RFID.
  - DU-113-2: record `Damaged` untuk aset `Toyota Avanza - 2`, Asset ID `VEH-2026-0002`, Group `Head Office`, berstatus `Damaged`, tanpa TAG.
  - DU-113-3: setting After photo required bernilai `OFF`.
  - DU-113-4: setting After photo required bernilai `ON`.
  - DU-113-5: Repair note yang diketik `Layar diganti baru dan sudah diuji fungsi`.
- Kondisi:
  - K1: record DU-113-1 dengan setting DU-113-3; Scan TAG belum dipindai dan Repair note belum diisi.
  - K2: record DU-113-2 dengan setting DU-113-3.
  - K3: record DU-113-2 dengan setting DU-113-4; foto After photo belum dipilih.

## Test Steps

### Isi dialog aset ber-TAG dengan After photo opsional
1. Tampilkan Dialog Mark as Repaired dengan kondisi K1
2. Verifikasi judul dialog `Mark as Repaired`
3. Verifikasi header aset memuat `Laptop Dell Latitude 5420 - 6` dengan badge status `Damaged`
4. Verifikasi bagian `Scan TAG*` tampil dengan tombol `[Scan TAG]`
5. Verifikasi tautan `I Can't Scan the TAG` tampil pada bagian `Scan TAG*`
6. Verifikasi isian `Repair note*` tampil dengan placeholder `Enter repair note`
7. Verifikasi label `After photo` tampil tanpa tanda wajib
8. Verifikasi tombol `[Cancel]` tampil
9. Verifikasi tombol `[Mark as Repaired]` tampil

### Aset tanpa TAG tidak memuat bagian Scan TAG
10. Tampilkan Dialog Mark as Repaired dengan kondisi K2
11. Verifikasi isian `Repair note*` tampil
12. Verifikasi bagian `Scan TAG*` tidak dirender
13. Verifikasi tautan `I Can't Scan the TAG` tidak dirender

### After photo wajib saat setting After photo required ON
14. Tampilkan Dialog Mark as Repaired dengan kondisi K3
15. Verifikasi label `After photo*` tampil
16. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
17. Klik `[Mark as Repaired]`
18. Verifikasi caption `After photo must not be empty` tampil di bawah pemilih foto `After photo*`

### Aksesibilitas dialog
19. Tampilkan Dialog Mark as Repaired dengan kondisi K1
20. Verifikasi fokus berada pada elemen di dalam dialog Mark as Repaired
21. Verifikasi isian `Repair note*` pada dialog Mark as Repaired memiliki penanda wajib untuk teknologi bantu
22. Verifikasi tombol tutup dialog Mark as Repaired memiliki nama aksesibel `Close dialog`
23. Verifikasi tombol unggah foto pada dialog Mark as Repaired memiliki nama aksesibel `Upload image`
24. Tekan `Tab` sebanyak 12 kali
25. Verifikasi fokus tetap berada pada elemen di dalam dialog Mark as Repaired
26. Klik `[Mark as Repaired]`
27. Verifikasi pesan error di bawah isian `Repair note*` terhubung sebagai deskripsi aksesibel isian itu
28. Klik `[Cancel]`
29. Verifikasi fokus kembali ke elemen yang membuka dialog Mark as Repaired

### Aksesibilitas bagian Scan TAG wajib
30. Tampilkan Dialog Mark as Repaired dengan kondisi K1
31. Verifikasi bagian `Scan TAG*` pada dialog Mark as Repaired memiliki penanda wajib untuk teknologi bantu
32. Klik `[Mark as Repaired]`
33. Verifikasi caption `Scan TAG must not be empty` terhubung sebagai deskripsi aksesibel bagian `Scan TAG*`

### Aksesibilitas pemilih foto After photo wajib
34. Tampilkan Dialog Mark as Repaired dengan kondisi K3
35. Verifikasi pemilih foto `After photo*` pada dialog Mark as Repaired memiliki penanda wajib untuk teknologi bantu
36. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
37. Klik `[Mark as Repaired]`
38. Verifikasi caption `After photo must not be empty` terhubung sebagai deskripsi aksesibel pemilih foto `After photo*`
