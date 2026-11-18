---
id: TC-FA-ASTL-UI-063-kartu-status-tampilan
title: "Tampilan kartu status"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-13d", "S-40", "S-42", "§4.1a#r1", "§4.1a#r3", "§4.1a#r4", "§4.1a#b2"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-13d": [2, 3, 7, 8]
  "S-40": [23, 24]
  "S-42": [26, 27, 29, 31, 32, 33, 35, 37]
  "§4.1a#r1": [2, 5]
  "§4.1a#r3": 11
  "§4.1a#r4": [13, 16]
  "§4.1a#b2": [11, 13, 18, 21]
anchor: []
coverage:
  web: automated
---
# Tampilan kartu status

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Kartu Status
- Data:
  - DU-063-1: Angka kartu normal: All `320`, Available `200`, In Transaction `189` dengan rincian `Borrowed 64 · Assigned 120 · In Disposal Process 5`, Issues `22` dengan rincian `Damaged 7 · Missing 3 · Not Paired Yet 12`, Disposed `20`.
  - DU-063-2: Angka kartu In Transaction nol: All `10`, In Transaction `0`, Issues `3` dengan rincian `Damaged 3`.
  - DU-063-3: Satu aset dihitung pada dua nilai: All `10`, In Transaction `1` dengan rincian `Borrowed 1 · In Disposal Process 1`.
  - DU-063-4: Aset pembanding pada tabel: Name `Printer Laser - 1`, Asset ID `AST-0031`, Status `Not Paired Yet`.
- Kondisi:
  - K1: kartu status memuat DU-063-1 dan tabel memuat DU-063-4.
  - K2: kartu status memuat DU-063-2.
  - K3: kartu status memuat DU-063-3.
  - K4: kartu status belum selesai dimuat, sedangkan tabel sudah memuat DU-063-4.
  - K5: memuat kartu status gagal karena error server, sedangkan tabel berhasil memuat DU-063-4, dan permintaan ulang kartu berhasil memuat DU-063-1.
  - K6: memuat kartu status dan memuat tabel sama-sama gagal karena error server, permintaan ulang kartu berhasil memuat DU-063-1, dan permintaan ulang tabel berhasil memuat DU-063-4.

## Test Steps

### Kartu aktif dan tooltip kartu All
1. Tampilkan Kartu Status dengan kondisi K1
2. Verifikasi kartu `All` aktif dengan angka `320`
3. Verifikasi kartu `Available`, `In Transaction`, `Issues`, dan `Disposed` tidak aktif
4. Arahkan pointer ke kartu `All`
5. Verifikasi tooltip `Active assets only. Disposed assets are in the Disposed card.` tampil
6. Klik kartu `Issues`
7. Verifikasi hanya kartu `Issues` yang aktif
8. Verifikasi kartu `All` tidak aktif

### Rincian hover kartu In Transaction dan Issues
9. Tampilkan Kartu Status dengan kondisi K1
10. Arahkan pointer ke kartu `In Transaction`
11. Verifikasi rincian `Borrowed 64 · Assigned 120 · In Disposal Process 5` tampil
12. Arahkan pointer ke kartu `Issues`
13. Verifikasi rincian `Damaged 7 · Missing 3 · Not Paired Yet 12` tampil

### Kartu berjumlah nol tidak menampilkan hover
14. Tampilkan Kartu Status dengan kondisi K2
15. Arahkan pointer ke kartu `Issues`
16. Verifikasi rincian `Damaged 3` tampil
17. Arahkan pointer ke kartu `In Transaction`
18. Verifikasi kartu `In Transaction` berangka `0` tidak menampilkan hover

### Jumlah rincian dapat melebihi angka kartu
19. Tampilkan Kartu Status dengan kondisi K3
20. Arahkan pointer ke kartu `In Transaction`
21. Verifikasi angka kartu `1` dan rincian `Borrowed 1 · In Disposal Process 1` yang berjumlah lebih besar dari angka kartu

### Kartu memuat terpisah dari tabel
22. Tampilkan Kartu Status dengan kondisi K4
23. Verifikasi tabel menampilkan baris `Printer Laser - 1` sementara kartu belum selesai dimuat
24. Verifikasi angka kartu belum tampil selama memuat, sementara tabel sudah memuat `Printer Laser - 1`, tanpa pesan error pada kartu

### Gagal memuat kartu saja
25. Tampilkan Kartu Status dengan kondisi K5
26. Verifikasi baris kartu menampilkan `Unable to load this data.` dan tombol `[Try Again]`
27. Verifikasi tabel tetap menampilkan baris `Printer Laser - 1` tanpa state error
28. Klik `[Try Again]` pada baris kartu
29. Verifikasi kartu `All` menampilkan angka `320`

### Gagal memuat kartu dan tabel sekaligus
30. Tampilkan Kartu Status dengan kondisi K6
31. Verifikasi baris kartu menampilkan `Unable to load this data.` dan `[Try Again]`
32. Verifikasi area tabel juga menampilkan `Unable to load this data.` dan `[Try Again]`

### Kartu dan tabel dimuat ulang terpisah
33. Verifikasi error baris kartu tampil pada baris kartu dan bukan sebagai toast
34. Klik `[Try Again]` pada baris kartu
35. Verifikasi kartu `All` menampilkan angka `320` sementara area tabel masih menampilkan `Unable to load this data.` dan tidak dimuat ulang
36. Klik `[Try Again]` pada area tabel
37. Verifikasi tabel menampilkan baris `Printer Laser - 1` dan angka kartu tidak dimuat ulang
