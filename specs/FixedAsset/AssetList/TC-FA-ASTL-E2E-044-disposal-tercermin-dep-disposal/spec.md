---
id: TC-FA-ASTL-E2E-044-disposal-tercermin-dep-disposal
title: "Disposal tercermin di daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-16h", "ASTL-LOGIC-17l", "§9.7#r2", "§9.7#r3"]
smoke: []
dependsOn: ["Disposal: Report Disposal dan Execute Disposal"]
trace:
  "ASTL-LOGIC-16h": 3
  "ASTL-LOGIC-17l": [11, 27]
  "§9.7#r2": [7, 8, 14, 18, 19, 30, 32, 35, 37, 40, 42, 43]
  "§9.7#r3": [21, 22, 25]
anchor: [16]
coverage:
  web: automated
---

# Disposal tercermin di daftar

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-044-1: aset `Kamera Mirrorless {runId} - 1`, Group `Cabang Bandung {runId}`, Unmanaged, Custody `Available`, tanpa penyusutan atau jurnal Posted.
  - DU-044-3: aset `Meja Rapat {runId} - 1`, Group `GA {runId}`, managed, Custody `Available`.
  - DU-044-4: aset `Lemari Arsip {runId} - 1`, Group `GA {runId}`, managed, Condition `Damaged`.
  - DU-044-5: aset `Kursi Tamu {runId} - 1`, Group `GA {runId}`, managed, Condition `Available`.
  - DU-044-6: aset `Rak Buku {runId} - 1`, Group `GA {runId}`, managed, Condition `Damaged`.
- Kondisi:
  - Jurnal pelepasan Disposal `Meja Rapat {runId} - 1` belum Posted sesudah Execute Disposal.

## Test Steps

### Report Disposal pada aset Unmanaged
1. Ketik Search `Kamera Mirrorless {runId}`, tekan Enter
2. Buka menu `⋯` baris `Kamera Mirrorless {runId} - 1`
3. Verifikasi menu aksi baris `Kamera Mirrorless {runId} - 1` yang Unmanaged menawarkan `Report Disposal`
4. Klik `Report Disposal`
5. Isi Reason `Aset sudah tidak dipakai {runId}`
6. Konfirmasi dialog Report Disposal
7. Verifikasi badge Status baris `Kamera Mirrorless {runId} - 1` berubah menjadi `Reported Disposal`, tanpa memuat ulang halaman
8. Verifikasi angka kartu `Issues` menjadi `1` untuk `Kamera Mirrorless {runId} - 1` karena Search hanya memuat aset itu
9. Buka menu `⋯` baris `Kamera Mirrorless {runId} - 1`
10. Arahkan kursor ke aksi `Delete Asset Data`
11. Verifikasi aksi `Delete Asset Data` tampil `Disabled` dengan tooltip `Asset has an open disposal report or request. Cancel or complete it first.`
12. Tutup menu aksi baris
13. Pada modul Disposal, Hendra Saputra membatalkan Report Disposal atas `Kamera Mirrorless {runId} - 1`, tanpa memuat ulang halaman
14. Verifikasi badge Status baris `Kamera Mirrorless {runId} - 1` kembali menjadi `Available` dengan badge overlay `Unmanaged` dan `Reported Disposal` tidak lagi tampil

### Submit Request dan Execute Disposal pada aset managed
15. Ketik Search `Meja Rapat {runId}`, tekan Enter
16. Verifikasi baris `Meja Rapat {runId} - 1` menampilkan `Available` sebelum Submit Request
17. Pada modul Disposal, Hendra Saputra mengirim Submit Request Disposal atas `Meja Rapat {runId} - 1`, tanpa memuat ulang halaman
18. Verifikasi badge Status baris `Meja Rapat {runId} - 1` berubah menjadi `In Disposal Process`
19. Verifikasi angka kartu `In Transaction` menjadi `1` karena Search hanya memuat aset ini
20. Pada modul Disposal, Hendra Saputra menjalankan Execute Disposal atas `Meja Rapat {runId} - 1`, tanpa memuat ulang halaman
21. Verifikasi badge Status baris `Meja Rapat {runId} - 1` berubah menjadi `Disposed`
22. Verifikasi angka kartu `All` menjadi `0` dan angka kartu `Disposed` menjadi `1` karena Search hanya memuat aset ini
23. Klik kartu `Disposed`
24. Buka menu `⋯` baris `Meja Rapat {runId} - 1`
25. Verifikasi menu aksi baris `Meja Rapat {runId} - 1` (Disposed) hanya memuat `Detail` dan `Delete Asset Data`
26. Arahkan kursor ke aksi `Delete Asset Data`
27. Verifikasi aksi `Delete Asset Data` pada `Meja Rapat {runId} - 1` tampil `Disabled` dengan tooltip `Asset has a disposal that is not posted yet.`

### Decline, Reject, dan Cancel mengembalikan Condition sebelumnya
28. Ketik Search `Lemari Arsip {runId}`, tekan Enter
29. Pada modul Disposal, Hendra Saputra membuat Report Disposal atas `Lemari Arsip {runId} - 1`, tanpa memuat ulang halaman
30. Verifikasi badge Status baris `Lemari Arsip {runId} - 1` berubah menjadi `Reported Disposal`
31. Pada modul Disposal, Hendra Saputra melakukan Decline atas Report Disposal `Lemari Arsip {runId} - 1`, tanpa memuat ulang halaman
32. Verifikasi badge Status baris `Lemari Arsip {runId} - 1` kembali menjadi `Damaged` dan `Reported Disposal` tidak lagi tampil
33. Ganti isi kotak Search dengan `Kursi Tamu {runId}`, tekan Enter
34. Pada modul Disposal, Hendra Saputra mengirim Submit Request Disposal atas `Kursi Tamu {runId} - 1`, tanpa memuat ulang halaman
35. Verifikasi badge Status baris `Kursi Tamu {runId} - 1` berubah menjadi `In Disposal Process` dan angka kartu `In Transaction` menjadi `1`
36. Pada modul Disposal, Hendra Saputra melakukan Reject atas Request Disposal `Kursi Tamu {runId} - 1`, tanpa memuat ulang halaman
37. Verifikasi badge Status baris `Kursi Tamu {runId} - 1` kembali menjadi `Available` dan angka kartu `In Transaction` turun menjadi `0`
38. Ganti isi kotak Search dengan `Rak Buku {runId}`, tekan Enter
39. Pada modul Disposal, Hendra Saputra mengirim Submit Request Disposal atas `Rak Buku {runId} - 1`, tanpa memuat ulang halaman
40. Verifikasi badge Status baris `Rak Buku {runId} - 1` berubah menjadi `In Disposal Process`
41. Pada modul Disposal, Hendra Saputra melakukan Cancel atas Request Disposal `Rak Buku {runId} - 1`, tanpa memuat ulang halaman
42. Verifikasi badge Status baris `Rak Buku {runId} - 1` kembali menjadi `Damaged` dan `In Disposal Process` tidak lagi tampil
43. Verifikasi angka kartu `In Transaction` menjadi `0` karena Search hanya memuat aset ini
