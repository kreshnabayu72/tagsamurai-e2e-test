---
id: TC-FA-ASTL-E2E-013-warranty-expiry
title: "Kolom Warranty Expiry dan hover garansi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ASTL-LOGIC-11b, ASTL-LOGIC-11c, ASTL-LOGIC-11e, ASTL-LOGIC-11l]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-11b: [6, 7, 8, 9]
  ASTL-LOGIC-11c: [11, 12, 13]
  ASTL-LOGIC-11e: [17, 18]
  ASTL-LOGIC-11l: [22, 24, 26]
anchor: []
coverage:
  web: automated
---

# Kolom Warranty Expiry dan hover garansi

## Prerequisites
- Aktor: Total Control `Dimas Prasetyo {runId}`.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-013-1: User `Dimas Prasetyo {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan (kolom `Warranty Expiry` belum tampil).
  - DU-013-2: Aset `Genset - 1 {runId}` dengan tiga garansi: `Garansi Mesin` berakhir `T0 - 40 hari`, `Garansi Baterai` berakhir `T0 + 15 hari`, dan `Garansi Servis` berakhir `T0 + 200 hari`.
  - DU-013-3: Aset `Dispenser - 1 {runId}` dengan dua garansi yang keduanya sudah lewat: `Garansi Unit` berakhir `T0 - 90 hari` dan `Garansi Kompresor` berakhir `T0 - 20 hari`.
  - DU-013-4: Aset `Kulkas - 1 {runId}` dengan satu garansi `Garansi Pintu` berakhir `T0 + 100 hari`.
  - DU-013-5: Aset `Kipas - 1 {runId}` tanpa garansi.
  - Nilai yang diharapkan di kolom `Warranty Expiry`, dari garansi di atas: `Genset - 1 {runId}` menampilkan `T0 + 15 hari`; `Dispenser - 1 {runId}` menampilkan `T0 - 20 hari`; `Kulkas - 1 {runId}` menampilkan `T0 + 100 hari`; `Kipas - 1 {runId}` menampilkan `—`. Semua tanggal ditulis menurut Date Format.
  - Rentang Filter untuk `Warranty Expiry`: `T0 + 190 hari` sampai `T0 + 210 hari`.
- Kondisi:
  - Akun `Dimas Prasetyo {runId}` aktif dan kredensialnya tersedia.
  - Date Format bernilai `dd/MM/yy`.

## Test Steps

### Kolom Warranty Expiry menampilkan garansi terdekat yang belum lewat
1. Masuk sebagai `Dimas Prasetyo {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Ketik Search `{runId}`, tekan Enter
4. Klik header kolom `Actions`
5. Centang kolom `Warranty Expiry` pada panel Column Visibility
6. Verifikasi sel `Warranty Expiry` pada baris `Genset - 1 {runId}` menampilkan tanggal `Garansi Baterai` (`T0 + 15 hari`), yaitu garansi terdekat yang belum lewat
7. Verifikasi sel `Warranty Expiry` pada baris `Dispenser - 1 {runId}` menampilkan tanggal `Garansi Kompresor` (`T0 - 20 hari`), yaitu tanggal terakhir karena semua garansi sudah lewat
8. Verifikasi sel `Warranty Expiry` pada baris `Kulkas - 1 {runId}` menampilkan tanggal `Garansi Pintu` (`T0 + 100 hari`)
9. Verifikasi sel `Warranty Expiry` pada baris `Kipas - 1 {runId}` menampilkan `—`

### Hover menampilkan seluruh garansi beserta penandanya
10. Arahkan kursor ke sel `Warranty Expiry` pada baris `Genset - 1 {runId}`
11. Verifikasi hover memuat `Garansi Mesin`, `Garansi Baterai`, dan `Garansi Servis`, masing-masing dalam bentuk `[Warranty Name] — [Date]` dengan tanggal sesuai garansinya
12. Verifikasi `Garansi Mesin` bertanda `Warranty expired` dan `Garansi Baterai` bertanda `Warranty expires soon`
13. Verifikasi `Garansi Servis` tidak bertanda

### Filter rentang tanggal cocok bila salah satu garansi cocok
14. Klik ikon Filter
15. Isi field Warranty Expiry dengan rentang `T0 + 190 hari` sampai `T0 + 210 hari`
16. Klik `[Apply]`
17. Verifikasi tabel memuat `Genset - 1 {runId}` yang salah satu garansinya (`Garansi Servis`) berada dalam rentang, walau sel `Warranty Expiry` menampilkan `Garansi Baterai`
18. Verifikasi tabel tidak memuat `Kulkas - 1 {runId}`, `Dispenser - 1 {runId}`, dan `Kipas - 1 {runId}`

### Penanda masa garansi tidak memengaruhi Sort dan Search
19. Klik `[Clear Field]`
20. Klik `[Apply]`
21. Klik ikon Filter
22. Verifikasi tabel memuat `Genset - 1 {runId}`, `Dispenser - 1 {runId}`, `Kulkas - 1 {runId}`, dan `Kipas - 1 {runId}`
23. Klik header kolom `Warranty Expiry`
24. Verifikasi urutan baris `Dispenser - 1 {runId}`, `Genset - 1 {runId}`, `Kulkas - 1 {runId}`, lalu `Kipas - 1 {runId}` mengikuti tanggal yang tampil di sel, tanpa dipengaruhi penanda garansi
25. Ganti isi kotak search dengan `Warranty expired`, tekan Enter
26. Verifikasi baris `Genset - 1 {runId}` dan `Dispenser - 1 {runId}` yang garansinya bertanda `Warranty expired` tidak tampil karena teks penanda tidak ikut dicari
