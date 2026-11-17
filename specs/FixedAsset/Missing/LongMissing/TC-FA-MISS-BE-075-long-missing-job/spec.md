---
id: TC-FA-MISS-BE-075-long-missing-job
title: "Server: job harian Long missing, penanda dihitung ulang, notifikasi sekali, Days Missing dan Duration sebagai selisih kalender"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [§1.2#r110, §1.2#r111, §1.2#r112, §1.2#r113, §9.2#b48, §9.2#b49, §9.2#b50, §9.2#b51, §9.2#b52, §9.2#b53, §9.2#b54, §9.2#b55, §9.2#b56, §9.2#b57, §9.2#b58, §9.4.2#r19, §9.4.4#r23, §9.6#r11, §9.7#r7, §9.8#r6, §8#r9, §8.1#r13, §9.5#r5, §4.1a#r15, §4.1b#r14, §4.3#r2, §9.1#r8, §3#p6, §9.4.1#r11, §9.4.2#r16]
smoke: []
dependsOn: []
trace:
  §1.2#r110: [2, 11, 21, 39, 41, 44]
  §1.2#r111: [4, 11, 40, 44]
  §1.2#r112: 23
  §1.2#r113: [14, 33]
  §9.2#b48: 2
  §9.2#b49: [2, 11, 39]
  §9.2#b50: [11, 27, 32, 39, 41]
  §9.2#b51: [12, 13, 28, 42]
  §9.2#b52: [3, 7, 8, 19, 20, 26, 31, 38, 43]
  §9.2#b53: [2, 7, 11, 39, 44]
  §9.2#b54: 2
  §9.2#b55: [9, 17, 27, 32, 34]
  §9.2#b56: [17, 18]
  §9.2#b57: [13, 18, 28, 42, 47, 48]
  §9.2#b58: [12, 13, 18, 28, 42]
  §9.4.2#r19: [12, 13, 27, 42]
  §9.4.4#r23: [4, 12]
  §9.6#r11: [6, 12, 42]
  §9.7#r7: 4
  §9.8#r6: 4
  §8#r9: 5
  §8.1#r13: [3, 5]
  §9.5#r5: [2, 46]
  §4.1a#r15: [3, 7, 8, 26, 31, 38, 43]
  §4.1b#r14: [19, 20]
  §4.3#r2: 2
  §9.1#r8: 2
  §3#p6: 23
  §9.4.1#r11: [11, 27, 39]
  §9.4.2#r16: 21
---

# Server: job harian Long missing, penanda dihitung ulang, notifikasi sekali, Days Missing dan Duration sebagai selisih kalender

## Prerequisites
- Aktor: Rina W, Total Control pada Client `Klien Long Missing {runId}` (DU-075-2); `Sari Dewi {runId}` (DU-075-1), pemegang tanpa hak Aktor Missing yang sudah dinonaktifkan; job Long missing harian berjalan sebagai `System`.
- Data:
  - DU-075-1: User Name `Sari Dewi {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Status `dinonaktifkan`.
  - DU-075-2: Client Name `Klien Long Missing {runId}`, Setting Long missing after `30 hari`; entitas khusus yang tidak dipakai spec lain, dan seluruh aset di bawah ada di Client ini.
  - DU-075-3: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA075-001`, Group aset `Finance Room`, Record berjalan `Missing`, Reported Date `T0 − 29 hari, pukul 09:00`.
  - DU-075-4: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA075-002`, Group aset `Finance Room`, Record berjalan `Missing`, Reported Date `T0 − 30 hari, pukul 09:00`.
  - DU-075-5: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA075-003`, Group aset `Finance Room`, Record berjalan `Missing`, Reported Date `T0 − 45 hari, pukul 09:00`, Node Long missing `sudah ada dengan Days missing 31`, missing_long `sudah terkirim satu kali`.
  - DU-075-6: Asset Name `Toyota Innova {runId}`, Asset ID `FA075-004`, Group aset `Finance Room`, Record berjalan `Reported Disposal`, Reported Date `T0 − 40 hari, pukul 09:00`, Node Long missing `sudah ada dengan Days missing 35`, missing_long `sudah terkirim satu kali`.
  - DU-075-7: Asset Name `Camera Canon EOS {runId}`, Asset ID `FA075-005`, Group aset `Finance Room`, Record berjalan `Missing`, Reported Date `T0 − 1 hari, pukul 23:50`.
  - DU-075-8: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA075-006`, Group aset `Finance Room`, Record berjalan `Found`, Reported Date `T0 − 10 hari, pukul 09:00`, Resolved Date `T0 − 3 hari, pukul 14:00`.
  - DU-075-9: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA075-007`, Group aset `Finance Room`, Record berjalan `Found`, Reported Date `T0 − 5 hari, pukul 23:50`, Resolved Date `T0 − 4 hari, pukul 00:10`.
  - DU-075-10: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA075-008`, Group aset `Finance Room`, Record berjalan `Missing`, Reported Date `T0 − 31 hari, pukul 09:00`, Last holder `Sari Dewi {runId}`.
  - DU-075-15: Asset Name `Dispenser Air Galon {runId}`, Asset ID `FA075-009`, Group aset `Finance Room`, Record berjalan `tidak ada`.
  - Days Missing yang diharapkan `33 days` untuk `Hand Pallet Truck {runId}` pada evaluasi hari T0 + 3, dari selisih tanggal kalender dengan Reported Date T0 − 30 hari.
  - Days Missing yang diharapkan `35 days` untuk `Kursi Ergonomis {runId}` pada evaluasi hari T0 + 4, dari Reported Date T0 − 31 hari.
  - Days Missing yang diharapkan `2 days` untuk `Dispenser Air Galon {runId}` dan `7 days` untuk `Camera Canon EOS {runId}` pada evaluasi hari T0 + 6, dari Reported Date T0 + 4 hari dan T0 − 1 hari.
- Kondisi:
  - Long missing after bernilai `30`
  - Job Long missing harian berjalan pukul 00:00 zona waktu Company
  - Hari evaluasi pertama disebut T0

## Test Steps
### Evaluasi harian pertama menandai record yang mencapai batas
1. Job Long missing harian berjalan pada pukul 00:00 zona waktu Company di hari T0
2. Verifikasi record `Hand Pallet Truck {runId}` yang dilaporkan T0 − 30 hari mendapat penanda `Long missing` pada evaluasi itu, karena selisih tanggal kalender mencapai nilai Long missing after `30`
3. Verifikasi Days Missing record `Hand Pallet Truck {runId}` bernilai `30 days` dan node `Long missing` pada record itu memuat Days missing `30`
4. Verifikasi record `Hand Pallet Truck {runId}` menerima tepat satu notifikasi `missing_long` dan satu node `Long missing`
5. Verifikasi node `Long missing` itu dicatat oleh `System` dengan Activity Log Modified By `System` dan tanpa entri System Log
6. Verifikasi penanda `Long missing`, node `Long missing`, dan notifikasi `missing_long` atas record `Hand Pallet Truck {runId}` tercatat bersama pada evaluasi itu, tanpa salah satunya saja
7. Verifikasi record `Laptop Dell Latitude 5420 {runId}` yang dilaporkan T0 − 29 hari bernilai Days Missing `29 days` dan belum mendapat penanda `Long missing`, node `Long missing`, maupun notifikasi `missing_long`
8. Verifikasi record `Camera Canon EOS {runId}` yang dilaporkan T0 − 1 hari pukul 23:50 bernilai Days Missing `1 day`, karena selisih dihitung dari tanggal kalender dan bukan dari waktu yang berlalu
9. Verifikasi record `Toyota Innova {runId}` yang berstatus `Reported Disposal` tidak lagi memuat penanda `Long missing` pada evaluasi itu karena penanda dihitung ulang tiap evaluasi

### Evaluasi berikutnya menghitung ulang penanda dan tidak mengirim ulang
10. Satu hari kalender berlalu dan job Long missing harian berjalan lagi
11. Verifikasi record `Laptop Dell Latitude 5420 {runId}` kini bernilai Days Missing `30 days` dan mendapat penanda `Long missing`, satu node `Long missing`, dan satu notifikasi `missing_long` pada evaluasi itu
12. Verifikasi record `Hand Pallet Truck {runId}` bernilai Days Missing 31 hari dalam format `[N] days`, tetap memuat satu node `Long missing`, dan tidak menerima notifikasi `missing_long` lagi
13. Verifikasi record `Projector Epson EB-X06 {runId}` yang sudah memiliki node `Long missing` dan sudah menerima `missing_long` tetap memiliki node itu, tidak mendapat node baru, dan tidak menerima notifikasi `missing_long` lagi
14. Verifikasi record `Projector Epson EB-X06 {runId}` tetap berstatus `Missing` dan tidak ditutup otomatis walau sudah melewati batas

### Penanda muncul kembali bila record kembali ke Missing dari Reported Disposal
15. Rina W menjalankan Cancel Disposal Report atas record `Toyota Innova {runId}`
16. Satu hari kalender berlalu dan job Long missing harian berjalan lagi
17. Verifikasi record `Toyota Innova {runId}` berstatus `Missing` dan memuat penanda `Long missing` lagi karena selisih tanggal kalender sudah melewati batas
18. Verifikasi record `Toyota Innova {runId}` tetap memiliki node `Long missing` yang lama dan tidak menerima notifikasi `missing_long` lagi

### Duration record History dihitung sebagai selisih tanggal kalender
19. Verifikasi Duration record `Monitor LG 27UL500 {runId}` bernilai `7 days`, yaitu selisih tanggal kalender antara tanggal selesai dan Reported Date
20. Verifikasi Duration record `Printer HP LaserJet M404 {runId}` bernilai `1 day` walau waktu yang berlalu hanya sepuluh menit, karena tanggal kalendernya berbeda

### Last holder yang dinonaktifkan tidak menghalangi evaluasi
21. Verifikasi record `Kursi Ergonomis {runId}` tetap ada, tetap mencatat `Sari Dewi {runId}` sebagai Last holder, dan mendapat penanda `Long missing` pada evaluasi harian

### Saran tindak lanjut Report Disposal tersedia pada record bertanda Long missing
22. Rina W mengirim Report Disposal atas record `Laptop Dell Latitude 5420 {runId}` yang bertanda `Long missing` dengan Reason `Aset tidak ditemukan setelah pencarian lebih dari 30 hari`
23. Verifikasi permintaan itu diterima dan record `Laptop Dell Latitude 5420 {runId}` berstatus `Reported Disposal`, sehingga aksi Report Disposal tersedia pada record `Missing` yang bertanda `Long missing`

### Nilai dinaikkan menghilangkan penanda pada record yang sudah ada
24. Rina W mengubah Long missing after menjadi `60`
25. Satu hari kalender berlalu dan job Long missing harian berjalan lagi
26. Verifikasi Days Missing record `Hand Pallet Truck {runId}` bernilai `33 days`
27. Verifikasi record `Hand Pallet Truck {runId}` berstatus `Missing` dan tidak lagi memuat penanda `Long missing`, karena selisih tanggal kalender `33` belum mencapai nilai Long missing after `60`
28. Verifikasi record `Hand Pallet Truck {runId}` tetap memiliki satu node `Long missing` yang sudah ada dan tidak menerima notifikasi `missing_long` baru

### Nilai 0 menonaktifkan penanda tanpa menutup record
29. Rina W mengubah Long missing after menjadi `0`
30. Satu hari kalender berlalu dan job Long missing harian berjalan lagi
31. Verifikasi Days Missing record `Kursi Ergonomis {runId}` bernilai `35 days`
32. Verifikasi record `Kursi Ergonomis {runId}` berstatus `Missing` dan tidak memuat penanda `Long missing`, karena nilai `0` menonaktifkan penanda
33. Verifikasi record `Projector Epson EB-X06 {runId}` tetap berstatus `Missing` dan tidak ditutup otomatis
34. Verifikasi record `Projector Epson EB-X06 {runId}` tidak memuat penanda `Long missing`, karena nilai `0` menonaktifkan penanda

### Nilai diturunkan menilai record yang dilaporkan sesudah perubahan dan menghitung ulang record lama
35. Rina W mengubah Long missing after menjadi `2`
36. Rina W mengirim Report Missing atas aset `Dispenser Air Galon {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
37. Dua hari kalender berlalu dan job Long missing harian berjalan pada hari kedua
38. Verifikasi Days Missing record `Dispenser Air Galon {runId}` bernilai `2 days`
39. Verifikasi record `Dispenser Air Galon {runId}` mendapat penanda `Long missing` karena selisih tanggal kalender mencapai nilai Long missing after `2`
40. Verifikasi record `Dispenser Air Galon {runId}` menerima tepat satu notifikasi `missing_long` dan satu node `Long missing`
41. Verifikasi record `Hand Pallet Truck {runId}` memuat penanda `Long missing` lagi karena nilai diturunkan
42. Verifikasi record `Hand Pallet Truck {runId}` tetap memiliki satu node `Long missing` yang lama dan tidak menerima notifikasi `missing_long` lagi
43. Verifikasi Days Missing record `Camera Canon EOS {runId}` bernilai `7 days`
44. Verifikasi record `Camera Canon EOS {runId}` mendapat penanda `Long missing` dan menerima tepat satu notifikasi `missing_long`

### Nilai Long missing after dikembalikan
45. Rina W mengubah Long missing after kembali menjadi `30`
46. Verifikasi Long missing after tersimpan bernilai `30`

### Notifikasi missing_long yang sudah terkirim tidak dihapus
47. Verifikasi notifikasi `missing_long` atas record `Projector Epson EB-X06 {runId}` yang sudah terkirim sebelum evaluasi pertama masih ada dan jumlahnya tetap satu, sesudah nilai Long missing after dinaikkan, diubah menjadi `0`, diturunkan, dan dikembalikan
48. Verifikasi notifikasi `missing_long` atas record `Hand Pallet Truck {runId}` yang terkirim pada evaluasi pertama masih ada dan jumlahnya tetap satu, bersama satu node `Long missing`, sesudah nilai Long missing after dinaikkan, diubah menjadi `0`, diturunkan, dan dikembalikan
