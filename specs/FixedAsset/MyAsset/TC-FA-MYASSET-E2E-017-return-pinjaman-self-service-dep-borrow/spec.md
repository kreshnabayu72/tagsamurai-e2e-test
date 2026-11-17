---
id: TC-FA-MYASSET-E2E-017-return-pinjaman-self-service-dep-borrow
title: "Return pinjaman self-service dari tab Borrowed: baris pindah ke tab History"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r6", "§4.1b#r14", "§4.1b#r28", "§4.1b#r29", "§4.1b#r31", "§4.1b#r32", "§4.1b#r33", "§4.1b#r34", "§4.8#r11", "§7.3#r10", "§9.6#r6", "§9.7#r14"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§2.1#r6": 14
  "§4.1b#r14": [4, 14]
  "§4.1b#r28": [3, 6]
  "§4.1b#r29": [4, 20]
  "§4.1b#r31": 6
  "§4.1b#r32": [8, 9]
  "§4.1b#r33": 12
  "§4.1b#r34": 11
  "§4.8#r11": 6
  "§7.3#r10": 11
  "§9.6#r6": [11, 12, 14, 25]
  "§9.7#r14": [14, 17]
anchor: [16, 19]
coverage:
  web: automated
---

# Return pinjaman self-service dari tab Borrowed: baris pindah ke tab History

## Prerequisites
- Aktor: Borrower, pengguna ber-akun login pemilik pinjaman.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-017-1: Pinjaman milik Borrower berstatus `Borrowed`, Source `Self-service`, satu aset: Name `Tablet Lenovo Tab P11 {runId}`, Asset ID `TAB-P11-{runId}`, Brand `Lenovo`, Model/Type `Tab P11`, Group `Head Office`, Duration `2 days`.
  - DU-017-2: Pinjaman milik Borrower berstatus `Borrowed`, Source `Admin`, satu aset: Name `Tablet Samsung Galaxy Tab A8 {runId}`, Asset ID `TAB-A8-{runId}`, Brand `Samsung`, Model/Type `Galaxy Tab A8`, Group `Head Office`, Duration `2 days`.

## Test Steps

### Return pinjaman Self-service: halaman Return terisi, toast, dan baris pindah ke tab History
1. Klik tab `Borrowed`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris `Tablet Lenovo Tab P11 {runId}` berstatus `Borrowed`
4. Verifikasi baris `Tablet Lenovo Tab P11 {runId}` memuat badge Source `Self-service`
5. Klik `⋯` pada baris `Tablet Lenovo Tab P11 {runId}`
6. Verifikasi opsi `Return` tersedia pada menu baris
7. Klik `Return`
8. Verifikasi field Borrower pada halaman Return terisi otomatis dengan nama Borrower pemilik pinjaman
9. Verifikasi aset `Tablet Lenovo Tab P11 {runId}` terisi otomatis pada halaman Return
10. Kirim Return dari halaman Return
11. Verifikasi toast sukses Return tampil
12. Verifikasi tab `History` aktif sesudah halaman Return selesai
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi baris `Tablet Lenovo Tab P11 {runId}` tampil di tab History dengan Status `Returned` dan Type `Borrow`

### Pinjaman Source Admin tidak memiliki aksi Return
15. Klik tab `Borrowed`
16. Verifikasi baris `Tablet Samsung Galaxy Tab A8 {runId}` tetap tampil dengan status `Borrowed`
17. Verifikasi baris `Tablet Lenovo Tab P11 {runId}` tidak tampil di tab Borrowed
18. Klik `⋯` pada baris `Tablet Samsung Galaxy Tab A8 {runId}`
19. Verifikasi opsi `Borrow Log` tersedia pada menu baris
20. Verifikasi opsi `Return` tidak tersedia pada menu baris

### Borrow Log mencatat Return self-service
21. Klik tab `History`
22. Ganti isi kotak search dengan `{runId}`, tekan Enter
23. Klik `⋯` pada baris `Tablet Lenovo Tab P11 {runId}`
24. Klik `Borrow Log`
25. Verifikasi Borrow Log pinjaman itu memuat entri `Returned via self-service`
