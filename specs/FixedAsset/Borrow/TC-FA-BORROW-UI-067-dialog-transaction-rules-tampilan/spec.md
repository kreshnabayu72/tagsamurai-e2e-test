---
id: TC-FA-BORROW-UI-067-dialog-transaction-rules-tampilan
title: "Dialog Transaction Rules: identitas aset, batas efektif, dan status per approver"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-BRW-10"]
smoke: []
dependsOn: []
trace:
  "D-BRW-10": [2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 16, 17, 19, 20, 22, 23, 25, 27, 28, 30, 31]
anchor: []
coverage:
  web: automated
---

# Dialog Transaction Rules: identitas aset, batas efektif, dan status per approver

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`.
- Layar awal: Tabel Transactions
- Komponen: Dialog Transaction Rules
- Data:
  - DU-067-1: baris pinjaman, Asset `Laptop Dell Latitude 5420 - 8` (identitas yang diharapkan `Asset : Laptop Dell Latitude 5420 - 8`), Max duration `14 days`, Max extensions `3`, Approval `Needs approval`, Approval type `All approvers`, approver snapshot `Rina W` berstatus `Approved` dan `Agus P` berstatus `Waiting for Approval`.
  - DU-067-2: baris pinjaman, Asset `Excavator PC200 - 3`, Max duration `7 days`, Max extensions `1`, Approval `Needs approval`, Approval type `Any one approver`, approver snapshot `Rina W` berstatus `Approved`, `Agus P` dan `Dewi Lestari` berstatus `Not Involved`.
  - DU-067-3: baris pinjaman, Asset `Toyota Avanza - 2`, Max duration `5 days`, Max extensions `2`, Approval `Needs approval`, Approval type `All approvers`, approver snapshot `Agus P` berstatus `Not Involved`, aktor override `Siti Nurhaliza` berstatus `Approved` dengan keterangan `Group Manager override`.
  - DU-067-4: baris pinjaman, Asset `Printer Epson L3110 - 1`, Max duration `3 days`, Max extensions `1`, Approval `Auto-approved`, tanpa approver.
  - DU-067-5: baris pinjaman, Asset `Monitor LG 24MK430`, Max duration `10 days`, Max extensions `2`, Approval `Not required`, tanpa approver.
  - DU-067-6: baris pinjaman dibatalkan, Asset `Kamera Canon EOS 200D`, Approval `Needs approval`, Approval type `All approvers`, approver snapshot `Rina W` berstatus `Approved` dan `Agus P` berstatus `Not Involved`.
- Kondisi:
  - K1: dialog dibuka dari baris DU-067-1.
  - K2: dialog dibuka dari baris DU-067-2.
  - K3: dialog dibuka dari baris DU-067-3.
  - K4: dialog dibuka dari baris DU-067-4.
  - K5: dialog dibuka dari baris DU-067-5.
  - K6: dialog dibuka dari baris DU-067-6.
  - K7: dialog dibuka dari form Borrow Request untuk Draft yang belum disubmit.

## Test Steps

### Identitas, batas efektif, dan Approval baris
1. Tampilkan Dialog Transaction Rules dengan kondisi K1
2. Verifikasi judul dialog `Transaction Rules` tampil
3. Verifikasi identitas `Asset : Laptop Dell Latitude 5420 - 8` tampil
4. Verifikasi dialog menampilkan `Max duration` dengan nilai `14 days`
5. Verifikasi dialog menampilkan `Max extensions` dengan nilai `3`
6. Verifikasi dialog menampilkan `Photo requirement`
7. Verifikasi dialog menampilkan Approval `Needs approval` dan Approval type `All approvers`
8. Verifikasi dialog tidak memiliki footer dan tombol Close
9. Klik ikon silang pada dialog `Transaction Rules`
10. Verifikasi dialog `Transaction Rules` tertutup

### Status per approver untuk All approvers
11. Tampilkan Dialog Transaction Rules dengan kondisi K1
12. Verifikasi approver `Rina W` tampil dengan status `Approved` dan waktu keputusan
13. Verifikasi approver `Agus P` tampil dengan status `Waiting for Approval`

### Status per approver untuk Any one approver
14. Tampilkan Dialog Transaction Rules dengan kondisi K2
15. Verifikasi dialog menampilkan Approval type `Any one approver`
16. Verifikasi approver `Rina W` tampil dengan status `Approved` dan waktu keputusan
17. Verifikasi approver `Agus P` dan `Dewi Lestari` tampil dengan status `Not Involved`

### Keterangan override
18. Tampilkan Dialog Transaction Rules dengan kondisi K3
19. Verifikasi baris tambahan `Siti Nurhaliza` tampil dengan status `Approved` dan keterangan `Group Manager override`
20. Verifikasi approver snapshot `Agus P` tampil dengan status `Not Involved`

### Approval Auto-approved tanpa approver
21. Tampilkan Dialog Transaction Rules dengan kondisi K4
22. Verifikasi dialog menampilkan Approval `Auto-approved`
23. Verifikasi dialog tidak menampilkan daftar approver

### Approval Not required tanpa approver
24. Tampilkan Dialog Transaction Rules dengan kondisi K5
25. Verifikasi dialog menampilkan Approval `Not required`

### Baris yang dibatalkan sebelum diputuskan
26. Tampilkan Dialog Transaction Rules dengan kondisi K6
27. Verifikasi dialog tidak memuat keterangan `Canceled by` (pembatalan tercatat di log)
28. Verifikasi approver `Agus P` tampil dengan status `Not Involved` dan approver `Rina W` tetap `Approved`

### Varian Draft dari form Borrow Request
29. Tampilkan Dialog Transaction Rules dengan kondisi K7
30. Verifikasi keterangan `Final rules are fixed when you submit` tampil
31. Verifikasi dialog tidak menampilkan bagian `Approval Progress` pada Draft
