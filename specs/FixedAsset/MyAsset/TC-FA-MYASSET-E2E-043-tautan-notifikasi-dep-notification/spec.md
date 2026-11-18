---
id: TC-FA-MYASSET-E2E-043-tautan-notifikasi-dep-notification
title: "Tautan notifikasi membuka tab dan baris terkait di My Asset"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§3#p3", "§4.2.1#b4", "§4.2.2b#p1", "§4.4#r48", "§4.4#r49", "§9.2#b16", "§9.4.2#r11"]
smoke: []
dependsOn: ["Notification: notifikasi Borrow dan Assignment yang bertautan ke My Asset", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§3#p3": [4, 5, 14, 16]
  "§4.2.1#b4": [11, 15, 16, 17, 19]
  "§4.2.2b#p1": 6
  "§4.4#r48": [4, 14, 16]
  "§4.4#r49": [5, 15]
  "§9.2#b16": [4, 5, 14, 16]
  "§9.4.2#r11": [14, 16]
anchor: [10]
coverage:
  web: automated
---

# Tautan notifikasi membuka tab dan baris terkait di My Asset

## Prerequisites
- Aktor: Assignee dan Borrower `Fitri Handayani {runId}` (DU-043-1).
- Layar awal: halaman masuk Fixed Asset.
- Data:
  - DU-043-1: pengguna `Fitri Handayani {runId}`, role `Read Only`, Group `Head Office`.
  - DU-043-2: penugasan aset `Laptop HP ProBook 450 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Assignee `Fitri Handayani {runId}`. Task `Confirm Handover` dengan Total Asset `1`.
  - DU-043-3: notifikasi `assignment_confirmation_required` untuk `Fitri Handayani {runId}`, bertautan ke penugasan DU-043-2.
  - DU-043-4: pinjaman aset `Kamera Canon M200 {runId}`, Group `Head Office`, Status `Returned`, Source `Admin`, Borrower `Me`.
  - DU-043-5: notifikasi `borrow_extension_resolved` untuk `Fitri Handayani {runId}`, bertautan ke pinjaman DU-043-4. Notifikasi diterima saat pinjaman masih Borrowed.
  - DU-043-6: pinjaman aset `Webcam Logitech C920 {runId}`, Group `Head Office`, Status `Returned`, Source `Admin`, Borrower `Me`.
- Kondisi:
  - Notifikasi DU-043-3 dan DU-043-5 belum dibaca.
  - Sesi Handover DU-043-2 menunggu konfirmasi Assignee dan jendela konfirmasinya belum habis.
  - Tab History aktor memuat 2 baris, yaitu DU-043-4 dan DU-043-6.

## Test Steps

### Tautan notifikasi Confirm Handover penugasan membuka tab Task, baris disorot, dan dialog
1. Masuk sebagai `Fitri Handayani {runId}`
2. Klik ikon notifikasi pada navbar
3. Klik notifikasi `assignment_confirmation_required` untuk penugasan DU-043-2
4. Verifikasi tab `Task` terbuka
5. Verifikasi baris Task `Confirm Handover` untuk penugasan DU-043-2 disorot
6. Verifikasi dialog `Confirm Handover` terbuka dengan pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
7. Klik `[Cancel]` pada dialog `Confirm Handover`

### Tautan notifikasi pinjaman yang barisnya sudah berpindah membuka tab History dan mereset Search
8. Klik tab `History`
9. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
10. Verifikasi baris `Webcam Logitech C920 {runId}` tampil
11. Verifikasi baris `Kamera Canon M200 {runId}` tidak tampil karena tersaring oleh Search
12. Klik ikon notifikasi pada navbar
13. Klik notifikasi `borrow_extension_resolved` untuk pinjaman DU-043-4
14. Verifikasi tab `History` terbuka
15. Verifikasi baris `Kamera Canon M200 {runId}` disorot
16. Verifikasi baris `Kamera Canon M200 {runId}` tampil
17. Verifikasi kotak Search tab `History` kosong
18. Waktu berlalu sampai 4 detik sejak baris disorot, lebih lama dari durasi sorotan 3 detik
19. Verifikasi baris `Kamera Canon M200 {runId}` tidak lagi disorot
