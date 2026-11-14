---
id: TC-FA-DAMAGED-E2E-056-notifikasi-dep-notification
title: "Confirm memicu damaged_review_resolved kepada pelapor dan Mark as Repaired memicu damaged_resolved yang tampil di notifikasi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.8#r3", "§9.8#r4", "§9.8#p4"]
smoke: []
dependsOn:
  - "Notification: daftar notifikasi in-app"
trace:
  "§9.8#r3": [6]
  "§9.8#r4": [13]
  "§9.8#p4": [6, 13]
anchor: []
coverage:
  web: automated
---

# Confirm memicu damaged_review_resolved kepada pelapor dan Mark as Repaired memicu damaged_resolved yang tampil di notifikasi

## Prerequisites
- Aktor: Pelapor `Budi Santoso {runId}`, pengguna aktif ber-akun yang memegang kedua aset di bawah dan belum punya notifikasi atas kedua aset itu. Aktor Damaged (Total Control) hanya memicu perubahan.
- Layar awal: halaman utama aplikasi.
- Data:
  - DU-056-1: aset Name `Laptop HP ProBook 450 {runId}`, Group `Head Office`, tanpa TAG, dipegang `Budi Santoso {runId}`, dengan record `Waiting for Confirmation` Source `Reported by holder` dari laporan `Budi Santoso {runId}` dengan What happened `Keyboard laptop beberapa tombol tidak berfungsi`.
  - DU-056-2: aset Name `Tablet Samsung Galaxy Tab S7 {runId}`, Group `Head Office`, tanpa TAG, dipegang `Budi Santoso {runId}`, dengan record `Damaged` Source `Reported by holder` dari laporan `Budi Santoso {runId}` dengan What happened `Layar tablet retak di sudut kanan atas`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Confirm laporan memicu notifikasi hasil review kepada pelapor
1. Buka daftar notifikasi
2. Catat jumlah notifikasi pada daftar notifikasi Pelapor
3. Tutup daftar notifikasi
4. Aktor Damaged melakukan Confirm atas laporan `Budi Santoso {runId}` untuk aset `Laptop HP ProBook 450 {runId}`
5. Buka daftar notifikasi
6. Verifikasi jumlah notifikasi pada daftar notifikasi Pelapor bertambah satu dari jumlah yang dicatat sebelum Confirm, sebagai notifikasi atas event `damaged_review_resolved` untuk aset `Laptop HP ProBook 450 {runId}`
7. Tutup daftar notifikasi

### Mark as Repaired memicu notifikasi record selesai kepada pelapor
8. Buka daftar notifikasi
9. Catat jumlah notifikasi pada daftar notifikasi Pelapor
10. Tutup daftar notifikasi
11. Aktor Damaged melakukan Mark as Repaired atas record aset `Tablet Samsung Galaxy Tab S7 {runId}` dengan Repair note `Layar sudah diganti dan sentuhan normal kembali`
12. Buka daftar notifikasi
13. Verifikasi jumlah notifikasi pada daftar notifikasi Pelapor bertambah satu dari jumlah yang dicatat sebelum Mark as Repaired, sebagai notifikasi atas event `damaged_resolved` untuk aset `Tablet Samsung Galaxy Tab S7 {runId}`
