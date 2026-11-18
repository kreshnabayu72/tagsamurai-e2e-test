---
id: TC-FA-ASTL-BE-083-label-bulk-idempoten
title: "Aturan server Add Label dan Remove Label"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-04b, ASTL-LOGIC-04e, ASTL-LOGIC-07c, ASTL-LOGIC-20f, EC-03, F-ASTL-10.k2, F-ASTL-11.k2, "§9.4.3#p2", "§9.6#r1", "§9.6#r2"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-04b: 4
  ASTL-LOGIC-04e: [12, 13]
  ASTL-LOGIC-07c: 8
  ASTL-LOGIC-20f: 4
  EC-03: [4, 5]
  F-ASTL-10.k2: [6, 22, 23]
  F-ASTL-11.k2: [13, 25, 26]
  "§9.4.3#p2": [15, 17, 19]
  "§9.6#r1": [4, 6]
  "§9.6#r2": [12, 13, 15]
anchor: []
---

# Aturan server Add Label dan Remove Label

## Prerequisites
- Aktor: Group Manager (Dewi).
- Data:
  - DU-083-1: User `Dewi Lestari {runId}`, role Group Manager untuk group `IT {runId}`.
  - DU-083-2: Group `IT {runId}` dan Group `Cabang Bandung {runId}` (tanpa induk).
  - DU-083-3: Aset `Laptop Pro 16 - 1 {runId}` ber-Lifecycle `Active` di `IT {runId}`, berlabel manual `Prioritas {runId}` (Label manual 1) dan `Inventaris Kantor {runId}` (Label manual 2).
  - DU-083-4: Aset `Laptop Pro 16 - 2 {runId}` ber-Lifecycle `Active` di `IT {runId}`, tanpa label manual, dengan label bawaan template Asset Name `Perangkat IT {runId}`.
  - DU-083-5: Aset `Monitor Dell - 1 {runId}` ber-Lifecycle `Disposed` di `IT {runId}`, berlabel manual `Prioritas {runId}`.
  - DU-083-6: Aset `Proyektor X2 - 1 {runId}` ber-Lifecycle `Active` di `Cabang Bandung {runId}`, di luar cakupan Dewi.
  - DU-083-7: Aset `Meja Rapat - 1 {runId}` ber-Lifecycle `Active` di `IT {runId}`, berlabel manual `Prioritas {runId}`.

## Test Steps

### Add Label melewati pasangan aset-label yang sudah ada
1. Catat jumlah entri Changelog aset `Laptop Pro 16 - 1 {runId}`
2. Catat jumlah entri Changelog aset `Laptop Pro 16 - 2 {runId}`
3. Dewi menambahkan label `Prioritas {runId}` pada aset `Laptop Pro 16 - 1 {runId}` dan `Laptop Pro 16 - 2 {runId}` sekaligus
4. Verifikasi permintaan berhasil tanpa error walau `Laptop Pro 16 - 1 {runId}` sudah berlabel `Prioritas {runId}`
5. Verifikasi `Laptop Pro 16 - 2 {runId}` kini berlabel `Prioritas {runId}` dan `Laptop Pro 16 - 1 {runId}` tetap berlabel `Prioritas {runId}` tepat satu kali
6. Verifikasi Changelog `Laptop Pro 16 - 2 {runId}` bertambah satu entri dan Changelog `Laptop Pro 16 - 1 {runId}` tidak bertambah
7. Dewi menambahkan label `Prioritas {runId}` pada aset `Laptop Pro 16 - 1 {runId}` saja
8. Verifikasi permintaan itu diproses sebagai idempotensi, bukan sebagai Edit No-Op, dan label `Prioritas {runId}` tetap terpasang

### Remove Label hanya mengubah aset yang memilikinya
9. Catat jumlah entri Changelog aset `Laptop Pro 16 - 1 {runId}`
10. Catat jumlah entri Changelog aset `Laptop Pro 16 - 2 {runId}`
11. Dewi mencabut label `Inventaris Kantor {runId}` dari `Laptop Pro 16 - 1 {runId}` dan `Laptop Pro 16 - 2 {runId}` sekaligus
12. Verifikasi permintaan berhasil tanpa error walau `Laptop Pro 16 - 2 {runId}` tidak memiliki label itu
13. Verifikasi `Laptop Pro 16 - 1 {runId}` tidak lagi berlabel `Inventaris Kantor {runId}`, Changelog-nya bertambah satu entri, dan Changelog `Laptop Pro 16 - 2 {runId}` tidak bertambah

### Label bawaan template tidak bisa dicabut
14. Dewi mencabut label bawaan `Perangkat IT {runId}` dari `Laptop Pro 16 - 2 {runId}`
15. Verifikasi label bawaan `Perangkat IT {runId}` tetap terpasang pada `Laptop Pro 16 - 2 {runId}`

### Aset Disposed tidak menerima mutasi label
16. Dewi menambahkan label `Inventaris Kantor {runId}` pada aset Disposed `Monitor Dell - 1 {runId}`
17. Verifikasi `Monitor Dell - 1 {runId}` tidak berlabel `Inventaris Kantor {runId}`
18. Dewi mencabut label `Prioritas {runId}` dari `Monitor Dell - 1 {runId}`
19. Verifikasi `Monitor Dell - 1 {runId}` tetap berlabel `Prioritas {runId}`

### Bulk Add Label dan Remove Label atomik atas seluruh seleksi
20. Catat jumlah entri Changelog aset `Meja Rapat - 1 {runId}`
21. Dewi menambahkan label `Inventaris Kantor {runId}` pada `Meja Rapat - 1 {runId}` dan `Proyektor X2 - 1 {runId}` sekaligus
22. Verifikasi seluruh permintaan ditolak karena `Proyektor X2 - 1 {runId}` berada di luar cakupan group Dewi
23. Verifikasi `Meja Rapat - 1 {runId}` tidak berlabel `Inventaris Kantor {runId}` dan jumlah entri Changelog-nya tidak berubah
24. Dewi mencabut label `Prioritas {runId}` dari `Meja Rapat - 1 {runId}` dan `Proyektor X2 - 1 {runId}` sekaligus
25. Verifikasi seluruh permintaan ditolak karena `Proyektor X2 - 1 {runId}` berada di luar cakupan group Dewi
26. Verifikasi `Meja Rapat - 1 {runId}` tetap berlabel `Prioritas {runId}`
