---
id: TC-FA-MYASSET-UI-118-dialog-confirm-handover-borrower
title: "Dialog Confirm Handover varian Borrower: isi, centang awal, dan validasi tanpa aset tercentang"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FI-01", "FI-02", "FLD-01", "FLD-02", "FLD-04", "V-03", "§4.1#p1", "§4.2.5#p2", "§4.4#r35", "§4.4#r36", "§4.4#r37", "§4.4#r38", "§4.5#p1", "§6#p1", "§7.2#r1"]
smoke: []
dependsOn: []
trace:
  "FI-01": 10
  "FI-02": 19
  "FLD-01": [10, 17, 28]
  "FLD-02": 19
  "FLD-04": 6
  "V-03": [28, 29]
  "§4.1#p1": 9
  "§4.2.5#p2": [4, 5, 7, 10, 11, 12, 26]
  "§4.4#r35": 26
  "§4.4#r36": 28
  "§4.4#r37": 29
  "§4.4#r38": 11
  "§4.5#p1": [35, 37, 38]
  "§6#p1": 28
  "§7.2#r1": [4, 5, 6, 7, 12]
anchor: [8]
coverage:
  web: automated
---

# Dialog Confirm Handover varian Borrower: isi, centang awal, dan validasi tanpa aset tercentang

## Prerequisites
- Aktor: Borrower.
- Layar awal: My Asset > Task.
- Komponen: Dialog Confirm Handover (D-MYA-01)
- Data:
  - DU-118-1: Task Confirm Handover (Borrow) dengan Transaction ID `BRW-2026-0152`, Task `Confirm Handover`, Group `Head Office`, Total Asset `3`, Handed Over By `Rina W`, Expires At `09/11/26, 20:41`, Borrower `Budi Santoso`.
  - DU-118-2: aset sesi Handover dengan Photo `projector-epson-eb-x06.jpg`, Name `Projector Epson EB-X06 - 12`, Asset ID `PRJ-2026-0012`, Brand `Epson`, Model/Type `EB-X06`, Return by `12/11/26`.
  - DU-118-3: aset sesi Handover dengan Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 21`, Asset ID `LPT-2026-0021`, Brand `Dell`, Model/Type `Latitude 5420`, Return by `13/11/26`.
  - DU-118-4: aset sesi Handover dengan Photo `meeting-mic-set.jpg`, Name `Meeting Mic Set - 5`, Asset ID `MIC-2026-0005`, Brand `Jabra`, Model/Type `Speak 510`, Return by `14/11/26`.
  - DU-118-5: pilihan aset tanpa satu pun tercentang: `Projector Epson EB-X06 - 12`, `Laptop Dell Latitude 5420 - 21`, dan `Meeting Mic Set - 5` semuanya dihapus centangnya.
- Kondisi:
  - K1: Task DU-118-1 tampil di tab Task, jendela konfirmasinya masih berjalan, dan sesi Handover-nya memuat aset DU-118-2 sampai DU-118-4. Date Format bernilai `dd/MM/yy`.

## Test Steps

### Isi dialog Confirm Handover varian Borrower
1. Tampilkan Dialog Confirm Handover dengan kondisi K1
2. Klik `⋯` pada baris Task `BRW-2026-0152`
3. Klik `Confirm Handover`
4. Verifikasi judul dialog `Confirm Handover` tampil
5. Verifikasi Info satu baris memuat `Borrower`, `Group`, dan `Handed Over By` dengan nilai `Budi Santoso`, `Head Office`, dan `Rina W` pada labelnya masing-masing
6. Verifikasi teks bantu `Uncheck any asset you didn't receive. The due date will be set from now for the checked assets.` tampil di atas tabel aset
7. Verifikasi tabel aset memuat kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, dan `Return by`
8. Verifikasi tabel aset memuat baris `Projector Epson EB-X06 - 12`, `Laptop Dell Latitude 5420 - 21`, dan `Meeting Mic Set - 5`
9. Verifikasi tabel aset tidak memiliki kontrol Setup Column
10. Verifikasi semua baris aset tercentang
11. Verifikasi `Return by` baris `Projector Epson EB-X06 - 12` bernilai `12/11/26`, baris `Laptop Dell Latitude 5420 - 21` bernilai `13/11/26`, dan baris `Meeting Mic Set - 5` bernilai `14/11/26`, sama dengan Due date tiap baris itu
12. Verifikasi footer dialog memuat tombol `[Cancel]` dan `[Confirm]`

### Checkbox header memilih semua baris
13. Tampilkan Dialog Confirm Handover dengan kondisi K1
14. Klik `⋯` pada baris Task `BRW-2026-0152`
15. Klik `Confirm Handover`
16. Hapus centang baris `Laptop Dell Latitude 5420 - 21`
17. Verifikasi baris `Laptop Dell Latitude 5420 - 21` tidak tercentang, sedangkan baris `Projector Epson EB-X06 - 12` dan `Meeting Mic Set - 5` tetap tercentang
18. Klik checkbox header tabel aset
19. Verifikasi semua baris aset tercentang

### Confirm tanpa aset tercentang ditolak di klien
20. Tampilkan Dialog Confirm Handover dengan kondisi K1
21. Klik `⋯` pada baris Task `BRW-2026-0152`
22. Klik `Confirm Handover`
23. Hapus centang baris `Projector Epson EB-X06 - 12`
24. Hapus centang baris `Laptop Dell Latitude 5420 - 21`
25. Hapus centang baris `Meeting Mic Set - 5`
26. Verifikasi tombol `[Confirm]` aktif walau tidak ada aset tercentang
27. Klik `[Confirm]`
28. Verifikasi error `Check at least one asset you received` tampil di bawah tabel aset
29. Verifikasi dialog `Confirm Handover` tetap terbuka

### Dialog dioperasikan dengan keyboard dan fokus kembali ke pemicu
30. Tampilkan Dialog Confirm Handover dengan kondisi K1
31. Klik `⋯` pada baris Task `BRW-2026-0152`
32. Klik `Confirm Handover`
33. Pindahkan fokus ke checkbox baris `Projector Epson EB-X06 - 12` dengan Tab
34. Tekan Space
35. Verifikasi baris `Projector Epson EB-X06 - 12` tidak tercentang
36. Klik `[Cancel]`
37. Verifikasi dialog `Confirm Handover` tertutup
38. Verifikasi fokus kembali ke elemen pemicu dialog
