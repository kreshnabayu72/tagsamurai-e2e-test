---
id: TC-FA-MYASSET-E2E-053-tab-assigned-toolbar-dep-assignment
title: "Toolbar tab Assigned pada data nyata: urutan default, Search dengan kolom tersembunyi, dan nama berkas Download"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["T-MYA-04", "§5#r4", "§5#r6", "EB-SRC-5@tabel-assigned"]
smoke: []
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "T-MYA-04": [4, 7, 8, 11, 12, 13, 17, 23, 24]
  "§5#r4": 4
  "§5#r6": [36, 39]
  "EB-SRC-5@tabel-assigned": [28, 32]
anchor: [3, 15]
coverage:
  web: automated
---

# Toolbar tab Assigned pada data nyata: urutan default, Search dengan kolom tersembunyi, dan nama berkas Download

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}` (karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`).
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-053-1: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa penugasan lain selain DU-053-3, DU-053-4, dan DU-053-5.
  - DU-053-2: pengguna `Rina Wijaya {runId}`, role `Asset Admin`, cakupan Group `Head Office`, akun aktif, Aktor Assignment penyerah DU-053-3 dan DU-053-4.
  - DU-053-3: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, TAG `RFID`, status `Assigned` kepada `Budi Santoso {runId}`, diserahkan lebih dulu daripada DU-053-4.
  - DU-053-4: aset `Monitor Dell 24 inch {runId}`, Group `Head Office`, TAG `NFC`, status `Assigned` kepada `Budi Santoso {runId}`, diserahkan sesudah DU-053-3.
  - DU-053-5: aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, TAG `Non TAG`, status `Waiting for Handover` kepada `Budi Santoso {runId}`, belum diserahkan sehingga tanpa Assigned Date.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24 jam`.
  - Kolom `TAG` pada tab Assigned tersembunyi (kolom Curated, keadaan awal).

## Test Steps

### Urutan default tab Assigned
1. Klik tab `Assigned`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi tepat tiga baris tampil pada tab `Assigned`, yaitu aset `Laptop Dell Latitude 5420 {runId}`, `Monitor Dell 24 inch {runId}`, dan `Printer HP LaserJet M404 {runId}`
4. Verifikasi urutan baris dari atas ke bawah adalah `Printer HP LaserJet M404 {runId}` (belum diserahkan), `Monitor Dell 24 inch {runId}` (diserahkan terbaru), lalu `Laptop Dell Latitude 5420 {runId}`
5. Klik `(←)` pada kotak Search

### Search pada kolom Text
6. Ketik Search `M404 {runId}`, tekan Enter
7. Verifikasi baris `Printer HP LaserJet M404 {runId}` tampil
8. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak tampil
9. Klik `(←)` pada kotak Search

### Search pada kolom Badge
10. Ketik Search `Waiting for Handover`, tekan Enter
11. Verifikasi baris `Printer HP LaserJet M404 {runId}` tampil
12. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak tampil
13. Verifikasi baris `Monitor Dell 24 inch {runId}` tidak tampil
14. Klik `(←)` pada kotak Search

### Search dengan nilai yang hanya ada di kolom Assigned Date
15. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil dengan kolom `Assigned Date` terisi
16. Ketik Search tanggal (bagian `dd/MM/yy`) dari kolom `Assigned Date` baris `Laptop Dell Latitude 5420 {runId}` seperti tampil di tabel, tekan Enter
17. Verifikasi `No results found` tampil karena kolom `Assigned Date` bukan kolom Searchable
18. Klik `(←)` pada kotak Search

### Search pada kolom TAG yang ditampilkan, disembunyikan, dan ditampilkan lagi
19. Klik header kolom `⋯`
20. Centang kolom `TAG` pada panel Column Visibility
21. Tutup panel Column Visibility
22. Ketik Search `RFID`, tekan Enter
23. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil
24. Verifikasi baris `Monitor Dell 24 inch {runId}` tidak tampil
25. Klik header kolom `⋯`
26. Hapus centang kolom `TAG` pada panel Column Visibility
27. Tutup panel Column Visibility
28. Verifikasi `No results found` tampil karena kolom `TAG` tersembunyi tidak lagi dicari
29. Klik header kolom `⋯`
30. Centang kolom `TAG` pada panel Column Visibility
31. Tutup panel Column Visibility
32. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil lagi karena kolom `TAG` ditampilkan kembali
33. Klik `(←)` pada kotak Search

### Nama berkas Download tab Assigned
34. Klik ikon `Download` pada toolbar
35. Klik `Download as CSV`
36. Verifikasi berkas terunduh bernama `My-Asset-Assigned` dengan ekstensi sesuai pilihan `Download as CSV`
37. Klik ikon `Download` pada toolbar
38. Klik `Download as XLSX`
39. Verifikasi berkas terunduh bernama `My-Asset-Assigned` dengan ekstensi sesuai pilihan `Download as XLSX`
