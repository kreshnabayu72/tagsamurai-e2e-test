---
id: TC-FA-MYASSET-UI-118-dialog-confirm-handover-borrower
title: "Dialog Confirm Handover varian Borrower: isi, centang awal, dan validasi tanpa aset tercentang"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FI-01", "FI-02", "FLD-01", "FLD-02", "FLD-04", "V-03", "§4.1#p1", "§4.2.5#p2", "§4.4#r35", "§4.4#r36", "§4.4#r37", "§4.4#r38", "§4.5#p1", "§6#p1", "§7.2#r1"]
smoke: []
dependsOn: []
trace:
  "FI-01": 14
  "FI-02": 23
  "FLD-01": [14, 21, 32]
  "FLD-02": 23
  "FLD-04": 10
  "V-03": [32, 33, 34]
  "§4.1#p1": 13
  "§4.2.5#p2": [4, 5, 7, 9, 11, 14, 15, 16, 30]
  "§4.4#r35": 30
  "§4.4#r36": 32
  "§4.4#r37": 34
  "§4.4#r38": 15
  "§4.5#p1": [40, 42, 43]
  "§6#p1": 32
  "§7.2#r1": [4, 5, 10, 11, 16]
anchor: [12]
coverage:
  web: automated
---

# Dialog Confirm Handover varian Borrower: isi, centang awal, dan validasi tanpa aset tercentang

## Prerequisites
- Aktor: Borrower.
- Layar awal: My Asset > Task.
- Komponen: Dialog Confirm Handover (D-MYA-01)
- Data:
  - DU-118-1: Task Confirm Handover (Borrow) dengan Transaction ID `BRW-2026-0152`, Task `Confirm Handover`, Group `Room 301` (hierarki lengkap `Head Office A > Floor 1 > Room 301`), Total Asset `3`, Handed Over By `Rina W`, Expires At `09/11/26, 20:41`, Borrower `Budi Santoso` (tampil `Budi S`, dari nama depan `Budi` dan inisial last name `S`).
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
5. Verifikasi Info dialog memuat label `Borrower`, `Group`, dan `Handed Over By` dengan nilai `Budi S`, `Room 301`, dan `Rina W` pada labelnya masing-masing
6. Arahkan kursor ke nilai Borrower `Budi S`
7. Verifikasi nama lengkap `Budi Santoso` tersampaikan
8. Arahkan kursor ke badge Group `Room 301`
9. Verifikasi hierarki lengkap `Head Office A > Floor 1 > Room 301` tersampaikan
10. Verifikasi teks bantu `Uncheck any asset you didn't receive. The due date will be set from now for the checked assets.` tampil di atas tabel aset
11. Verifikasi tabel aset memuat kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, dan `Return by`
12. Verifikasi tabel aset memuat baris `Projector Epson EB-X06 - 12`, `Laptop Dell Latitude 5420 - 21`, dan `Meeting Mic Set - 5`
13. Verifikasi tabel aset tidak memiliki kontrol Setup Column
14. Verifikasi semua baris aset tercentang
15. Verifikasi `Return by` baris `Projector Epson EB-X06 - 12` bernilai `12/11/26`, baris `Laptop Dell Latitude 5420 - 21` bernilai `13/11/26`, dan baris `Meeting Mic Set - 5` bernilai `14/11/26`, sama dengan Due date tiap baris itu
16. Verifikasi footer dialog memuat tombol `[Cancel]` dan `[Confirm]`

### Checkbox header memilih semua baris
17. Tampilkan Dialog Confirm Handover dengan kondisi K1
18. Klik `⋯` pada baris Task `BRW-2026-0152`
19. Klik `Confirm Handover`
20. Hapus centang baris `Laptop Dell Latitude 5420 - 21`
21. Verifikasi baris `Laptop Dell Latitude 5420 - 21` tidak tercentang, sedangkan baris `Projector Epson EB-X06 - 12` dan `Meeting Mic Set - 5` tetap tercentang
22. Klik checkbox header tabel aset
23. Verifikasi semua baris aset tercentang

### Confirm tanpa aset tercentang ditolak di klien
24. Tampilkan Dialog Confirm Handover dengan kondisi K1
25. Klik `⋯` pada baris Task `BRW-2026-0152`
26. Klik `Confirm Handover`
27. Hapus centang baris `Projector Epson EB-X06 - 12`
28. Hapus centang baris `Laptop Dell Latitude 5420 - 21`
29. Hapus centang baris `Meeting Mic Set - 5`
30. Verifikasi tombol `[Confirm]` aktif walau tidak ada aset tercentang
31. Klik `[Confirm]`
32. Verifikasi error `Check at least one asset you received` tampil di bawah tabel aset
33. Verifikasi tidak ada toast yang tampil
34. Verifikasi dialog `Confirm Handover` tetap terbuka

### Dialog dioperasikan dengan keyboard dan fokus kembali ke pemicu
35. Tampilkan Dialog Confirm Handover dengan kondisi K1
36. Klik `⋯` pada baris Task `BRW-2026-0152`
37. Klik `Confirm Handover`
38. Pindahkan fokus ke checkbox baris `Projector Epson EB-X06 - 12` dengan Tab
39. Tekan Space
40. Verifikasi baris `Projector Epson EB-X06 - 12` tidak tercentang
41. Klik `[Cancel]`
42. Verifikasi dialog `Confirm Handover` tertutup
43. Verifikasi fokus kembali ke tombol `⋯` pada baris Task `BRW-2026-0152`
