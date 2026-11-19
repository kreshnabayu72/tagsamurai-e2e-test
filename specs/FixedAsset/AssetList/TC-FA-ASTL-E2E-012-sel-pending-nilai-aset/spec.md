---
id: TC-FA-ASTL-E2E-012-sel-pending-nilai-aset
title: "Sel Pending dan nilai kosong pada kolom bergerbang"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ASTL-LOGIC-10h, ASTL-LOGIC-10i, ASTL-LOGIC-10j, ASTL-LOGIC-12i, ASTL-LOGIC-12j, ASTL-LOGIC-12k, ASTL-LOGIC-12l, EC-14, EC-25]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-10h: [6, 7, 8]
  ASTL-LOGIC-10i: [10, 12]
  ASTL-LOGIC-10j: [16, 21, 32]
  ASTL-LOGIC-12i: 9
  ASTL-LOGIC-12j: [13, 15]
  ASTL-LOGIC-12k: [18, 20, 23]
  ASTL-LOGIC-12l: 25
  EC-14: [16, 17, 18, 20]
  EC-25: [10, 12, 15, 22, 25]
anchor: []
coverage:
  web: automated
---

# Sel Pending dan nilai kosong pada kolom bergerbang

## Prerequisites
- Aktor: Total Control `Maya Anggraini {runId}`, dan Group Manager `Hendra Wijaya {runId}`.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-012-1: User `Maya Anggraini {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan.
  - DU-012-2: Aset `Lemari Arsip - 1 {runId}` dengan Asset Class `Peralatan Kantor`, Purchase Date `T0 - 30 hari`, dan Purchase Cost `15000000`, tampil `Rp 15.000.000,00`.
  - DU-012-3: Aset `Kabel Roll - 1 {runId}` dengan Asset Class `Peralatan Kantor` dan Purchase Cost `0`, tampil `Rp 0,00`.
  - DU-012-4: Aset `Printer Laser - 1 {runId}` dengan Asset Class `Peralatan Kantor`, tanpa Purchase Date dan Purchase Cost.
  - DU-012-5: Aset `Kursi Kerja - 1 {runId}` yang Asset Name-nya tanpa Asset Class, dengan Purchase Date `T0 - 60 hari` dan Purchase Cost `2500000`, tampil `Rp 2.500.000,00`, di group `Ruang Kerja {runId}`.
  - DU-012-6: Aset `Meja Rapat - 1 {runId}` yang Asset Name-nya tanpa Asset Class, tanpa Purchase Date dan Purchase Cost.
  - DU-012-7: Group `Ruang Kerja {runId}`.
  - DU-012-8: User `Hendra Wijaya {runId}`, role Group Manager, cakupan group `Ruang Kerja {runId}` dan descendant-nya, memakai konfigurasi kolom bawaan.
- Kondisi:
  - Akun `Maya Anggraini {runId}` dan `Hendra Wijaya {runId}` aktif dan kredensialnya tersedia.
  - Date Format bernilai `dd/MM/yy`.

## Test Steps

### Sel bernilai tampil sebagai nilai, termasuk nilai nol
1. Masuk sebagai `Maya Anggraini {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Ketik Search `{runId}`, tekan Enter
4. Klik header kolom `Actions`
5. Centang kolom `Asset Class`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Purchase Date`, dan `Purchase Cost` pada panel Column Visibility
6. Verifikasi sel `Purchase Cost` pada baris `Lemari Arsip - 1 {runId}` menampilkan `Rp 15.000.000,00`
7. Verifikasi sel `Purchase Date` pada baris `Lemari Arsip - 1 {runId}` menampilkan `T0 - 30 hari` menurut Date Format
8. Verifikasi sel `Purchase Cost` pada baris `Kabel Roll - 1 {runId}` menampilkan `Rp 0,00`
9. Verifikasi sel `Asset Value (Commercial)` dan `Asset Value (Fiscal)` pada baris `Lemari Arsip - 1 {runId}` berisi nilai currency, bukan `Pending`, karena kedua data sumbernya sudah ada

### Purchase Cost belum diisi membuat Purchase Date, Purchase Cost, dan Asset Value Pending
10. Verifikasi sel `Purchase Date` dan `Purchase Cost` pada baris `Printer Laser - 1 {runId}` menampilkan `Pending`
11. Arahkan kursor ke sel `Purchase Cost` pada baris `Printer Laser - 1 {runId}`
12. Verifikasi alasan `Purchase data has not been set.` tersampaikan pada sel
13. Verifikasi sel `Asset Value (Commercial)` dan `Asset Value (Fiscal)` pada baris `Printer Laser - 1 {runId}` menampilkan `Pending`
14. Arahkan kursor ke sel `Asset Value (Commercial)` pada baris `Printer Laser - 1 {runId}`
15. Verifikasi alasan `Purchase cost has not been set.` tersampaikan pada sel

### Asset Name tanpa Asset Class membuat Asset Class kosong dan Asset Value Pending
16. Verifikasi sel `Asset Class` pada baris `Kursi Kerja - 1 {runId}` menampilkan `—`
17. Verifikasi sel `Purchase Cost` pada baris `Kursi Kerja - 1 {runId}` menampilkan `Rp 2.500.000,00`
18. Verifikasi sel `Asset Value (Commercial)` pada baris `Kursi Kerja - 1 {runId}` menampilkan `Pending`
19. Arahkan kursor ke sel `Asset Value (Commercial)` pada baris `Kursi Kerja - 1 {runId}`
20. Verifikasi alasan `Asset class has not been set.` tersampaikan pada sel

### Alasan Purchase didahulukan bila Purchase Cost dan Asset Class sama-sama belum ada
21. Verifikasi sel `Asset Class` pada baris `Meja Rapat - 1 {runId}` menampilkan `—`
22. Verifikasi sel `Purchase Date` dan `Purchase Cost` pada baris `Meja Rapat - 1 {runId}` menampilkan `Pending`
23. Verifikasi sel `Asset Value (Commercial)` pada baris `Meja Rapat - 1 {runId}` menampilkan `Pending`
24. Arahkan kursor ke sel `Asset Value (Commercial)` pada baris `Meja Rapat - 1 {runId}`
25. Verifikasi alasan `Purchase cost has not been set.` tersampaikan pada sel, bukan alasan `Asset class has not been set.`

### Keadaan tidak berlaku tetap `—` bagi aktor tanpa hak Asset Class
26. Keluar dari akun
27. Masuk sebagai `Hendra Wijaya {runId}`
28. Klik menu `Fixed Asset > Assets` pada sidebar
29. Ketik Search `{runId}`, tekan Enter
30. Klik header kolom `Actions`
31. Centang kolom `Asset Class` pada panel Column Visibility
32. Verifikasi sel `Asset Class` pada baris `Kursi Kerja - 1 {runId}` menampilkan `—`, bukan `No access`, karena field itu tidak berlaku bagi Asset Name aset
