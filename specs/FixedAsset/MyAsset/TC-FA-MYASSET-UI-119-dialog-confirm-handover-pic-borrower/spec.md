---
id: TC-FA-MYASSET-UI-119-dialog-confirm-handover-pic-borrower
title: "Dialog Confirm Handover varian PIC Borrower: pernyataan wajib dan pesannya"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-06", "FLD-03", "FLD-04", "§1.2#r42", "§4.2.5#p4"]
smoke: []
dependsOn: []
trace:
  "FI-06": 13
  "FLD-03": [6, 7, 11, 13]
  "FLD-04": 5
  "§1.2#r42": [4, 6, 13]
  "§4.2.5#p4": [4, 5, 6, 13]
anchor: []
coverage:
  web: automated
---

# Dialog Confirm Handover varian PIC Borrower: pernyataan wajib dan pesannya

## Prerequisites
- Aktor: PIC Borrower, yaitu PIC dari Borrower tanpa akun `Dewi Lestari`.
- Layar awal: My Asset > Task.
- Komponen: Dialog Confirm Handover (D-MYA-01)
- Data:
  - DU-119-1: Task Confirm Handover (Borrow) atas nama Borrower tanpa akun dengan Transaction ID `BRW-2026-0160`, Task `Confirm Handover`, Group `Head Office`, Total Asset `1`, Handed Over By `Rina W`, Expires At `09/11/26, 20:50`, Borrower `Dewi Lestari`.
  - DU-119-2: aset sesi Handover dengan Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 33`, Asset ID `LPT-2026-0033`, Brand `Dell`, Model/Type `Latitude 5420`, Return by `13/11/26`.
  - DU-119-3: pernyataan PIC `I confirm that Dewi Lestari has received the checked assets.` yang belum dicentang.
- Kondisi:
  - K1: Task DU-119-1 tampil di tab Task, jendela konfirmasinya masih berjalan, dan sesi Handover-nya memuat aset DU-119-2. Date Format bernilai `dd/MM/yy`.

## Test Steps

### Info Borrower, teks bantu, dan pernyataan PIC pada dialog
1. Tampilkan Dialog Confirm Handover dengan kondisi K1
2. Klik `⋯` pada baris Task `BRW-2026-0160`
3. Klik `Confirm Handover`
4. Verifikasi Info memuat `Borrower` dengan nilai `Dewi Lestari`
5. Verifikasi teks bantu `Uncheck any asset you didn't receive. The due date will be set from now for the checked assets.` tampil di atas tabel aset
6. Verifikasi pernyataan `I confirm that Dewi Lestari has received the checked assets.` tampil sebagai checkbox
7. Verifikasi checkbox pernyataan belum tercentang

### Pernyataan PIC wajib dicentang sebelum Confirm
8. Tampilkan Dialog Confirm Handover dengan kondisi K1
9. Klik `⋯` pada baris Task `BRW-2026-0160`
10. Klik `Confirm Handover`
11. Verifikasi checkbox pernyataan `I confirm that Dewi Lestari has received the checked assets.` belum tercentang
12. Klik `[Confirm]`
13. Verifikasi error `Check the statement to confirm` tampil
