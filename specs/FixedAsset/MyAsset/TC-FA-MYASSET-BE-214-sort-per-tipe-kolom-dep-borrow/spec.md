---
id: TC-FA-MYASSET-BE-214-sort-per-tipe-kolom-dep-borrow
title: "Sort My Asset per tipe kolom dan urutan default tiap tabel"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["T-MYA-01", "T-MYA-04", "§4.1b#r2", "§4.1b#r3", "§4.1b#r4", "§4.1b#r5", "§4.1b#r6", "§4.1b#r7", "§4.1b#r8", "§4.1b#r9", "§4.1b#r10", "§4.1b#r11", "§4.1b#r12", "§4.1b#r13", "§4.1b#r14", "§4.1b#r15", "§4.1b#r16", "§4.1b#r17", "§4.1b#r18", "§4.1b#p7", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r14", "§4.1c#r17", "§4.1c#p4", "§5#r4", "EB-SRT-1"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "T-MYA-01": [128, 130, 132, 134, 136, 138, 140, 142, 144]
  "T-MYA-04": [98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126]
  "§4.1b#r2": [7, 9, 60]
  "§4.1b#r3": 11
  "§4.1b#r4": [23, 55, 56]
  "§4.1b#r5": 13
  "§4.1b#r6": 25
  "§4.1b#r7": [27, 29]
  "§4.1b#r8": [33, 35]
  "§4.1b#r9": 15
  "§4.1b#r10": [37, 39, 58]
  "§4.1b#r11": [41, 43]
  "§4.1b#r12": 19
  "§4.1b#r13": 21
  "§4.1b#r14": 31
  "§4.1b#r15": [49, 51]
  "§4.1b#r16": [45, 47]
  "§4.1b#r17": 53
  "§4.1b#r18": 17
  "§4.1b#p7": [2, 3, 5]
  "§4.1c#r2": 64
  "§4.1c#r3": 66
  "§4.1c#r4": 68
  "§4.1c#r5": 70
  "§4.1c#r6": 72
  "§4.1c#r7": [74, 80]
  "§4.1c#r8": 82
  "§4.1c#r9": 84
  "§4.1c#r10": 76
  "§4.1c#r11": 86
  "§4.1c#r12": 88
  "§4.1c#r13": [90, 92]
  "§4.1c#r14": [94, 96]
  "§4.1c#r17": 78
  "§4.1c#p4": 62
  "§5#r4": [2, 5, 62, 98, 128]
  "EB-SRT-1": [7, 21, 23, 33, 37, 39, 45, 55, 60, 64, 90, 94, 100, 124, 126, 130, 134, 136, 142, 144]
---

# Sort My Asset per tipe kolom dan urutan default tiap tabel

## Prerequisites
- Aktor: Borrower dan Assignee, yaitu pengguna ber-akun login `Rina Wulandari {runId}` (DU-214-1) yang membuka My Asset dan tidak punya baris lain selain DU-214-2 sampai DU-214-21. Aktor Borrow dan Aktor Assignment menyerahkan aset ke Aktor, masing-masing dengan hak atas Group aset yang diserahkannya; Aktor Borrow `Eko Susanto {runId}` dan `Eko Santoso {runId}`, yang bernama depan sama dan berinisial nama belakang sama, Aktor Assignment `Agus Pratama {runId}` dan `Siti Rahmawati {runId}`. Borrower tanpa akun `Hendra Wijaya {runId}` dan Division `Divisi Keuangan {runId}` memakai Aktor sebagai PIC.
- Data:
  - DU-214-1: Aktor pemegang semua baris di bawah, tanpa baris lain di My Asset: Name `Rina Wulandari {runId}`, Posisi `Borrower dan Assignee`.
  - DU-214-2: pinjaman Admin Borrowed, dua hari, tidak pernah di-Extend: Name `kabel HDMI {runId}`, Asset ID `CBL-0101 {runId}`, Brand `Anker`, Model/Type `A2142`, Group `Ruang Server`, Status `Borrowed`, TAG `RFID`, Category `Kabel`, Due Date `Due Date milik DU-214-2`, Remaining `Remaining milik DU-214-2`, Borrower `Me`, Transaction ID `nomor BRW milik DU-214-2`, Source `Admin`, Duration `2 days`, Handed Over At `waktu handover milik DU-214-2`, Extensions `0 / 3`, Purpose `Penggantian kabel jaringan`.
  - DU-214-3: pinjaman self-service Borrowed, sepuluh hari, satu Extend sudah berlaku: Name `Kamera CCTV {runId}`, Asset ID `CAM-0102 {runId}`, Brand `Hikvision`, Model/Type `DS-2CD2143`, Group `Lobi Utama`, Status `Borrowed`, TAG `NFC`, Category `Keamanan`, Due Date `Due Date milik DU-214-3`, Remaining `Remaining milik DU-214-3`, Borrower `Me`, Transaction ID `nomor BRW milik DU-214-3`, Source `Self-service`, Duration `10 days`, Handed Over At `waktu handover milik DU-214-3`, Extensions `1 / 2`, Purpose `Pemasangan kamera lobi`.
  - DU-214-4: pinjaman Admin dengan pengajuan Extend, satu hari: Name `Elan Printer {runId}`, Asset ID `PRT-0103 {runId}`, Brand `Epson`, Model/Type `L3250`, Group `Ruang Arsip`, Status `Extension Request`, TAG `RFID`, Category `Perangkat Cetak`, Due Date `Due Date milik DU-214-4`, Remaining `Remaining milik DU-214-4`, Borrower `Me`, Transaction ID `nomor BRW milik DU-214-4`, Source `Admin`, Duration `1 day`, Handed Over At `waktu handover milik DU-214-4`, Extensions `0 / 2`, Purpose `Cetak laporan bulanan`.
  - DU-214-5: pinjaman Admin Borrowed atas nama Borrower tanpa akun yang PIC-nya Aktor, delapan jam: Name `Élan Scanner {runId}`, Asset ID `SCN-0104 {runId}`, Brand `Canon`, Model/Type `LiDE 400`, Group `Ruang Arsip`, Status `Borrowed`, TAG `NFC`, Category `Perangkat Pindai`, Due Date `Due Date milik DU-214-5`, Remaining `Remaining milik DU-214-5`, Borrower `Hendra Wijaya {runId}`, Transaction ID `nomor BRW milik DU-214-5`, Source `Admin`, Duration `8 hours`, Handed Over At `waktu handover milik DU-214-5`, Extensions `0 / 1`, Purpose `Pemindaian arsip lama`.
  - DU-214-6: pinjaman self-service Waiting for Approval, belum punya Due Date: Name `Ezra Router {runId}`, Asset ID `RTR-0105 {runId}`, Brand `TP-Link`, Model/Type `Archer C6`, Group `Ruang Server`, Status `Waiting for Approval`, TAG `BLE`, Category `Jaringan`, Due Date `—`, Remaining `—`, Borrower `Me`, Transaction ID `nomor BRW milik DU-214-6`, Source `Self-service`, Duration `5 days`, Handed Over At `—`, Extensions `0 / 2`, Purpose `Uji jaringan kantor cabang`.
  - DU-214-7: pinjaman Admin Waiting for Handover, belum punya Due Date: Name `3D Printer {runId}`, Asset ID `3DP-0106 {runId}`, Brand `Creality`, Model/Type `Ender 3`, Group `Lab Prototipe`, Status `Waiting for Handover`, TAG `RFID`, Category `Perangkat Cetak`, Due Date `—`, Remaining `—`, Borrower `Me`, Transaction ID `nomor BRW milik DU-214-7`, Source `Admin`, Duration `3 days`, Handed Over At `—`, Extensions `0 / 2`, Purpose `Prototipe produk baru`.
  - DU-214-8: pinjaman Admin Borrowed pada aset tanpa TAG (Non TAG): Name `#Rak Gudang {runId}`, Asset ID `RAK-0107 {runId}`, Brand `Krisbow`, Model/Type `R200`, Group `Gudang Utama`, Status `Borrowed`, TAG `—`, Category `Peralatan`, Due Date `Due Date milik DU-214-8`, Remaining `Remaining milik DU-214-8`, Borrower `Me`, Transaction ID `nomor BRW milik DU-214-8`, Source `Admin`, Duration `7 days`, Handed Over At `waktu handover milik DU-214-8`, Extensions `0 / 2`, Purpose `Penataan gudang`.
  - DU-214-9: pinjaman self-service Borrowed, dua hari, tidak pernah di-Extend, handover sesudah DU-214-2: Name `Laptop Staf {runId}`, Asset ID `LTP-0108 {runId}`, Brand `Lenovo`, Model/Type `T14`, Group `Ruang IT`, Status `Borrowed`, TAG `NFC`, Category `Komputer`, Due Date `Due Date milik DU-214-9`, Remaining `Remaining milik DU-214-9`, Borrower `Me`, Transaction ID `nomor BRW milik DU-214-9`, Source `Self-service`, Duration `2 days`, Handed Over At `waktu handover milik DU-214-9`, Extensions `0 / 2`, Purpose `Kerja dari lokasi klien`.
  - DU-214-10: dua belas pinjaman Admin Borrowed atas aset bernama sama dengan brand sama, dibuat berurutan sehingga Increment 1 sampai 12: Name `Mouse Logitech {runId}`, Asset ID `MSE-{n} {runId}`, Brand `Logitech`, Model/Type `M170`, Group `Pusat Distribusi`, Status `Borrowed`, TAG `RFID`, Category `Aksesori Komputer`, Due Date `Due Date milik DU-214-10`, Remaining `Remaining milik DU-214-10`, Borrower `Me`, Transaction ID `nomor BRW milik DU-214-10`, Source `Admin`, Duration `3 days`, Handed Over At `waktu handover milik DU-214-10`, Extensions `0 / 2`, Purpose `Pembagian mouse karyawan baru`.
  - DU-214-11: pinjaman Returned milik Aktor, ditutup ke-3: Name `Mikrofon Studio {runId}`, Asset ID `MIC-0301 {runId}`, Brand `Shure`, Model/Type `SM58`, Group `Ruang Rekam`, Status `Returned`, Holder `Me`, TAG `RFID`, Category `Audio`, Type `Borrow`, Transaction ID `nomor BRW milik DU-214-11`, Handed Over At `waktu handover milik DU-214-11`, Closed At `waktu penutupan milik DU-214-11`, Purpose `Rekaman siaran internal`.
  - DU-214-12: penugasan Unassigned atas nama Division yang PIC-nya Aktor, ditutup ke-2: Name `Monitor Kerja {runId}`, Asset ID `MON-0302 {runId}`, Brand `Samsung`, Model/Type `S24C`, Group `Ruang Finance`, Status `Unassigned`, Holder `Divisi Keuangan {runId}`, TAG `NFC`, Category `Peripheral`, Type `Assignment`, Transaction ID `nomor ASG milik DU-214-12`, Handed Over At `waktu handover milik DU-214-12`, Closed At `waktu penutupan milik DU-214-12`, Purpose `Penggunaan harian tim keuangan`.
  - DU-214-13: pinjaman Rejected atas nama Borrower tanpa akun, tidak pernah diserahkan, ditutup ke-1: Name `Printer Kantor {runId}`, Asset ID `PRN-0303 {runId}`, Brand `Brother`, Model/Type `HL-L2320`, Group `Ruang Arsip`, Status `Rejected`, Holder `Hendra Wijaya {runId}`, TAG `—`, Category `Perangkat Cetak`, Type `Borrow`, Transaction ID `nomor BRW milik DU-214-13`, Handed Over At `—`, Closed At `waktu penutupan milik DU-214-13`, Purpose `Cetak dokumen audit`.
  - DU-214-14: pinjaman Canceled milik Aktor, tidak pernah diserahkan, ditutup ke-4: Name `Proyektor Aula {runId}`, Asset ID `PRJ-0304 {runId}`, Brand `Epson`, Model/Type `EB-X500`, Group `Ruang Rapat`, Status `Canceled`, Holder `Me`, TAG `BLE`, Category `Elektronik`, Type `Borrow`, Transaction ID `nomor BRW milik DU-214-14`, Handed Over At `—`, Closed At `waktu penutupan milik DU-214-14`, Purpose `Presentasi tahunan`.
  - DU-214-15: penugasan Assigned milik Aktor, diserahkan ke-1: Name `Notebook Staf {runId}`, Asset ID `NBK-0201 {runId}`, Brand `Lenovo`, Model/Type `T14`, Group `Ruang Staf`, Status `Assigned`, Assigned To `Me`, TAG `RFID`, Category `Laptop`, Transaction ID `nomor ASG milik DU-214-15`, Assigned Date `waktu serah terima milik DU-214-15`, Assigned By `Siti Rahmawati {runId}`.
  - DU-214-16: penugasan Waiting for Handover atas nama Division yang PIC-nya Aktor, belum diserahkan: Name `meja Kerja {runId}`, Asset ID `FRN-0202 {runId}`, Brand `Informa`, Model/Type `Oval 200`, Group `Ruang Direksi`, Status `Waiting for Handover`, Assigned To `Divisi Keuangan {runId}`, TAG `NFC`, Category `Furnitur`, Transaction ID `nomor ASG milik DU-214-16`, Assigned Date `—`, Assigned By `—`.
  - DU-214-17: penugasan Waiting for Approval milik Aktor, belum diserahkan: Name `Kursi Ergonomis {runId}`, Asset ID `FRN-0203 {runId}`, Brand `Ergotec`, Model/Type `E100`, Group `Ruang Staf`, Status `Waiting for Approval`, Assigned To `Me`, TAG `—`, Category `Furnitur`, Transaction ID `nomor ASG milik DU-214-17`, Assigned Date `—`, Assigned By `—`.
  - DU-214-18: penugasan Assigned milik Aktor, diserahkan ke-2: Name `Dispenser Air {runId}`, Asset ID `DSP-0204 {runId}`, Brand `Sanken`, Model/Type `HWD-770`, Group `Ruang Pantry`, Status `Assigned`, Assigned To `Me`, TAG `BLE`, Category `Elektronik`, Transaction ID `nomor ASG milik DU-214-18`, Assigned Date `waktu serah terima milik DU-214-18`, Assigned By `Agus Pratama {runId}`.
  - DU-214-19: Task Confirm Handover pinjaman, dibuat ke-1: Transaction ID `nomor BRW milik DU-214-19`, Task `Confirm Handover`, Group `Ruang IT`, Total Asset `2`, Handed Over By `Eko Susanto {runId}`, Expires At `waktu Expires At milik DU-214-19`.
  - DU-214-20: Task Confirm Handover penugasan, dibuat ke-2: Transaction ID `nomor ASG milik DU-214-20`, Task `Confirm Handover`, Group `Ruang Direksi`, Total Asset `7`, Handed Over By `Agus Pratama {runId}`, Expires At `waktu Expires At milik DU-214-20`.
  - DU-214-21: Task Confirm Handover pinjaman, dibuat ke-3: Transaction ID `nomor BRW milik DU-214-21`, Task `Confirm Handover`, Group `Gudang Utama`, Total Asset `4`, Handed Over By `Eko Santoso {runId}`, Expires At `waktu Expires At milik DU-214-21`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`
  - Kolom `TAG`, `Category`, `Extensions`, dan `Purpose` tampil pada tabel yang diurutkan
  - Ukuran halaman tabel bernilai `10`; tab Borrowed Aktor berisi 20 baris (DU-214-2 sampai DU-214-9 dan 12 baris DU-214-10), sehingga muat tepat di halaman 1 dan halaman 2
  - DU-214-2 dan DU-214-9 sama-sama `2 days` dan tidak pernah di-Extend, sehingga Due Date DU-214-2 lebih awal daripada DU-214-9 menurut urutan handover. Satu Extend DU-214-3 tidak memindahkan Due Date DU-214-3 dari urutan paling akhir di antara DU-214-2 sampai DU-214-9, karena Duration `10 days` jauh melampaui `7 days` milik DU-214-8
  - Urutan pembuatan data mengikuti urutan nomor DU di setiap tabel: DU-214-2 sampai DU-214-9 lalu DU-214-10 (12 baris berurutan) pada tab Borrowed; DU-214-11 sampai DU-214-14 pada tab History dengan penutupan DU-214-13, DU-214-12, DU-214-11, DU-214-14; DU-214-15 sampai DU-214-18 pada tab Assigned; DU-214-19 sampai DU-214-21 pada tab Task. Handover tab Borrowed berlangsung pada DU-214-2, DU-214-3, DU-214-4, DU-214-5, DU-214-8, DU-214-9, lalu DU-214-10

## Test Steps

### Urutan default tab Borrowed
1. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, tanpa urutan kolom
2. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 yang punya Due Date tampil dalam urutan relatif dari Due Date terdekat: DU-214-5, DU-214-4, DU-214-2, DU-214-9, DU-214-8, DU-214-3, dan baris tanpa Due Date (DU-214-6, DU-214-7) tampil sesudah semuanya
3. Verifikasi urutan default itu berbeda dari urutan pembuatan DU-214-2 sampai DU-214-9, yang dimulai dari DU-214-2 lalu DU-214-3
4. Aktor meminta ulang halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, tanpa urutan kolom
5. Verifikasi urutan relatif baris DU-214-2 sampai DU-214-9 sama dengan urutan default sebelumnya (DU-214-5, DU-214-4, DU-214-2, DU-214-9, DU-214-8, DU-214-3) dan berbeda dari urutan naik maupun turun menurut kolom `Name`

### Sort kolom teks tab Borrowed tidak peka huruf besar kecil dan menghormati aksen serta simbol
6. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Name`
7. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-8, DU-214-7, DU-214-4, DU-214-5, DU-214-6, DU-214-2, DU-214-3, DU-214-9, dengan `kabel HDMI` sebelum `Kamera CCTV` walau huruf awalnya kecil, `Élan Scanner` sebelum `Ezra Router`, dan baris bersimbol atau berangka (DU-214-8, DU-214-7) paling awal
8. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan turun menurut kolom `Name`
9. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-9, DU-214-3, DU-214-2, DU-214-6, DU-214-5, DU-214-4, DU-214-7, DU-214-8
10. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Asset ID`
11. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-7, DU-214-3, DU-214-2, DU-214-9, DU-214-4, DU-214-8, DU-214-6, DU-214-5
12. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Model/Type`
13. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-2, DU-214-6, DU-214-3, DU-214-7, DU-214-4, DU-214-5, DU-214-8, DU-214-9
14. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Category`
15. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-6, DU-214-2, DU-214-3, DU-214-9, DU-214-8, DU-214-4, DU-214-7, DU-214-5
16. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Purpose`
17. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-4, DU-214-9, DU-214-3, DU-214-5, DU-214-8, DU-214-2, DU-214-7, DU-214-6
18. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Borrower`
19. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-5, DU-214-4, DU-214-2, DU-214-9, DU-214-8, DU-214-3
20. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Transaction ID`
21. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif menurut nomor BRW naik secara natural, yaitu menurut urutan pembuatan: DU-214-2, DU-214-3, DU-214-4, DU-214-5, DU-214-6, DU-214-7, DU-214-8, DU-214-9

### Sort kolom badge dan ikon tab Borrowed
22. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Brand`
23. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-2, DU-214-5, DU-214-7, DU-214-4, DU-214-3, DU-214-8, DU-214-9, DU-214-6
24. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Group`
25. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-8, DU-214-7, DU-214-3, DU-214-5, DU-214-4, DU-214-9, DU-214-2, DU-214-6, dengan baris yang Group-nya sama diurutkan menurut urutan default tabel
26. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Status`
27. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-5, DU-214-2, DU-214-9, DU-214-8, DU-214-3, DU-214-4, DU-214-6, DU-214-7
28. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan turun menurut kolom `Status`
29. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-7, DU-214-6, DU-214-4, DU-214-5, DU-214-2, DU-214-9, DU-214-8, DU-214-3
30. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Source`
31. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-5, DU-214-4, DU-214-2, DU-214-8, DU-214-7, DU-214-9, DU-214-3, DU-214-6
32. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `TAG`
33. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-6, DU-214-5, DU-214-9, DU-214-3, DU-214-4, DU-214-2, DU-214-7, DU-214-8, dengan baris tanpa TAG (DU-214-8) paling akhir
34. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan turun menurut kolom `TAG`
35. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-8, DU-214-4, DU-214-2, DU-214-7, DU-214-5, DU-214-9, DU-214-3, DU-214-6, dengan baris tanpa TAG (DU-214-8) paling awal

### Sort kolom tanggal, Remaining, dan Duration tab Borrowed
36. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Due Date`
37. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-5, DU-214-4, DU-214-2, DU-214-9, DU-214-8, DU-214-3, dengan baris tanpa Due Date di akhir
38. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan turun menurut kolom `Due Date`
39. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-3, DU-214-8, DU-214-9, DU-214-2, DU-214-4, DU-214-5, dengan baris tanpa Due Date di awal
40. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Remaining`
41. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-5, DU-214-4, DU-214-2, DU-214-9, DU-214-8, DU-214-3, dengan baris tanpa Due Date di akhir
42. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan turun menurut kolom `Remaining`
43. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-3, DU-214-8, DU-214-9, DU-214-2, DU-214-4, DU-214-5, dengan baris tanpa Due Date di awal
44. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Handed Over At`
45. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-2, DU-214-3, DU-214-4, DU-214-5, DU-214-8, DU-214-9, dengan baris yang belum diserahkan di akhir
46. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan turun menurut kolom `Handed Over At`
47. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-9, DU-214-8, DU-214-5, DU-214-4, DU-214-3, DU-214-2, dengan baris yang belum diserahkan di awal
48. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Duration`
49. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-5, DU-214-4, DU-214-2, DU-214-9, DU-214-7, DU-214-6, DU-214-8, DU-214-3, menurut lama dalam jam sehingga `8 hours` sebelum `1 day`, `2 days`, dan `10 days`, bukan menurut teks
50. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan turun menurut kolom `Duration`
51. Verifikasi pada gabungan kedua halaman, baris DU-214-2 sampai DU-214-9 tampil dalam urutan relatif dari atas ke bawah: DU-214-3, DU-214-8, DU-214-6, DU-214-7, DU-214-2, DU-214-9, DU-214-4, DU-214-5
52. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, dan membaca kolom `Extensions` baris DU-214-3
53. Verifikasi nilai kolom `Extensions` baris DU-214-3 adalah `1 / 2`, yaitu `[terpakai] / [maks]` dengan satu Extend yang sudah berlaku

### Sort tab Borrowed menjaga urutan deterministik melintasi halaman
54. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Brand`
55. Verifikasi setiap baris DU-214-10 muncul tepat satu kali di gabungan kedua halaman dan tidak ada yang terlewat, walau seluruh 12 barisnya ber-Brand sama dan terbagi ke dua halaman
56. Verifikasi urutan gabungan kedua halaman sama dengan urutan satu daftar utuh: DU-214-2, DU-214-5, DU-214-7, DU-214-4, DU-214-3, DU-214-8, DU-214-9, lalu 12 baris DU-214-10 menurut Due Date terdekat, lalu DU-214-6
57. Aktor meminta halaman 1 dan halaman 2 tab Borrowed diurutkan naik menurut kolom `Due Date`
58. Verifikasi urutan gabungan kedua halaman tidak berubah antar permintaan berulang dan setiap baris DU-214-10 muncul tepat satu kali
59. Aktor meminta halaman 1 dan halaman 2 tab Borrowed, ukuran halaman `10`, diurutkan naik menurut kolom `Name`
60. Verifikasi 12 baris DU-214-10 tampil menurut nomor Increment naik secara natural, yaitu baris ke-1, ke-2, ke-3, sampai ke-10, ke-11, dan ke-12, bukan ke-1, ke-10, ke-11, ke-12, lalu ke-2

### Urutan default tab History
61. Aktor meminta daftar tab History tanpa urutan kolom
62. Verifikasi baris tampil berurutan dari Closed At terbaru: DU-214-14, DU-214-11, DU-214-12, DU-214-13

### Sort kolom teks dan badge tab History
63. Aktor meminta daftar tab History diurutkan naik menurut kolom `Name`
64. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-11, DU-214-12, DU-214-13, DU-214-14
65. Aktor meminta daftar tab History diurutkan naik menurut kolom `Asset ID`
66. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-11, DU-214-12, DU-214-14, DU-214-13
67. Aktor meminta daftar tab History diurutkan naik menurut kolom `Brand`
68. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-13, DU-214-14, DU-214-12, DU-214-11
69. Aktor meminta daftar tab History diurutkan naik menurut kolom `Model/Type`
70. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-14, DU-214-13, DU-214-12, DU-214-11
71. Aktor meminta daftar tab History diurutkan naik menurut kolom `Group`
72. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-13, DU-214-12, DU-214-14, DU-214-11
73. Aktor meminta daftar tab History diurutkan naik menurut kolom `Status`
74. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-14, DU-214-13, DU-214-11, DU-214-12
75. Aktor meminta daftar tab History diurutkan naik menurut kolom `Category`
76. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-11, DU-214-14, DU-214-13, DU-214-12
77. Aktor meminta daftar tab History diurutkan naik menurut kolom `Purpose`
78. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-13, DU-214-12, DU-214-14, DU-214-11
79. Aktor meminta daftar tab History diurutkan turun menurut kolom `Status`
80. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-12, DU-214-11, DU-214-13, DU-214-14
81. Aktor meminta daftar tab History diurutkan naik menurut kolom `Holder`
82. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-12, DU-214-13, DU-214-14, DU-214-11
83. Aktor meminta daftar tab History diurutkan naik menurut kolom `TAG`
84. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-14, DU-214-12, DU-214-11, DU-214-13, dengan baris tanpa TAG (DU-214-13) paling akhir
85. Aktor meminta daftar tab History diurutkan naik menurut kolom `Type`
86. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-12, DU-214-14, DU-214-11, DU-214-13, dengan baris yang Type-nya sama diurutkan menurut Closed At terbaru
87. Aktor meminta daftar tab History diurutkan naik menurut kolom `Transaction ID`
88. Verifikasi baris tampil berurutan menurut nomor naik secara natural, nomor ASG sebelum nomor BRW dan nomor BRW menurut urutan pembuatan: DU-214-12, DU-214-11, DU-214-13, DU-214-14

### Sort kolom tanggal tab History
89. Aktor meminta daftar tab History diurutkan naik menurut kolom `Handed Over At`
90. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-11, DU-214-12, DU-214-14, DU-214-13, dengan baris yang tidak pernah diserahkan di akhir
91. Aktor meminta daftar tab History diurutkan turun menurut kolom `Handed Over At`
92. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-14, DU-214-13, DU-214-12, DU-214-11, dengan baris yang tidak pernah diserahkan di awal
93. Aktor meminta daftar tab History diurutkan naik menurut kolom `Closed At`
94. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-13, DU-214-12, DU-214-11, DU-214-14
95. Aktor meminta daftar tab History diurutkan turun menurut kolom `Closed At`
96. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-14, DU-214-11, DU-214-12, DU-214-13

### Urutan default tab Assigned
97. Aktor meminta daftar tab Assigned tanpa urutan kolom
98. Verifikasi baris yang sudah diserahkan tampil berurutan dari Assigned Date terbaru: DU-214-18, DU-214-15

### Sort kolom teks, badge, ikon, dan tanggal tab Assigned
99. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Name`
100. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-18, DU-214-17, DU-214-16, DU-214-15
101. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Asset ID`
102. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-18, DU-214-16, DU-214-17, DU-214-15
103. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Brand`
104. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-17, DU-214-16, DU-214-15, DU-214-18
105. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Model/Type`
106. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-17, DU-214-18, DU-214-16, DU-214-15
107. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Group`
108. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-16, DU-214-18, DU-214-15
109. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Status`
110. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-18, DU-214-15, DU-214-17, DU-214-16
111. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Assigned To`
112. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-16, DU-214-18, DU-214-15
113. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `TAG`
114. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-18, DU-214-16, DU-214-15, DU-214-17
115. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Category`
116. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-18, DU-214-15
117. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Assigned By`
118. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-18, DU-214-15
119. Aktor meminta daftar tab Assigned diurutkan turun menurut kolom `Status`
120. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-16, DU-214-17, DU-214-18, DU-214-15
121. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Transaction ID`
122. Verifikasi baris tampil berurutan menurut nomor ASG naik secara natural, yaitu menurut urutan pembuatan: DU-214-15, DU-214-16, DU-214-17, DU-214-18
123. Aktor meminta daftar tab Assigned diurutkan naik menurut kolom `Assigned Date`
124. Verifikasi baris yang sudah diserahkan tampil berurutan: DU-214-15, DU-214-18, dan baris yang belum diserahkan (DU-214-16, DU-214-17) tampil sesudahnya
125. Aktor meminta daftar tab Assigned diurutkan turun menurut kolom `Assigned Date`
126. Verifikasi baris yang belum diserahkan (DU-214-16, DU-214-17) tampil lebih dulu, lalu DU-214-18, DU-214-15

### Sort tab Task per kolom dan urutan default
127. Aktor meminta daftar tab Task tanpa urutan kolom
128. Verifikasi Task pinjaman DU-214-19 tampil sebelum Task pinjaman DU-214-21, karena Expires At terdekat tampil dulu dan keduanya memakai jendela konfirmasi yang sama
129. Aktor meminta daftar tab Task diurutkan naik menurut kolom `Transaction ID`
130. Verifikasi baris tampil berurutan menurut nomor naik secara natural: DU-214-20 (nomor ASG), lalu DU-214-19 dan DU-214-21 menurut urutan pembuatan nomor BRW
131. Aktor meminta daftar tab Task diurutkan naik menurut kolom `Task`
132. Verifikasi DU-214-19 tampil sebelum DU-214-21, karena seluruh nilai `Confirm Handover` sama sehingga urutan mengikuti urutan default tabel
133. Aktor meminta daftar tab Task diurutkan naik menurut kolom `Group`
134. Verifikasi baris tampil berurutan dari atas ke bawah: DU-214-21, DU-214-20, DU-214-19
135. Aktor meminta daftar tab Task diurutkan naik menurut kolom `Total Asset`
136. Verifikasi baris tampil berurutan dari angka terkecil: DU-214-19 (`2`), DU-214-21 (`4`), DU-214-20 (`7`)
137. Aktor meminta daftar tab Task diurutkan turun menurut kolom `Total Asset`
138. Verifikasi baris tampil berurutan dari angka terbesar: DU-214-20, DU-214-21, DU-214-19
139. Aktor meminta daftar tab Task diurutkan naik menurut kolom `Handed Over By`
140. Verifikasi baris tampil berurutan menurut nama lengkap Handed Over By: DU-214-20 (`Agus Pratama {runId}`), DU-214-21 (`Eko Santoso {runId}`), DU-214-19 (`Eko Susanto {runId}`), yaitu DU-214-21 sebelum DU-214-19 walau urutan default tabel menempatkan DU-214-19 lebih dulu dan kedua nama berawal `Eko` dengan inisial nama belakang yang sama
141. Aktor meminta daftar tab Task diurutkan naik menurut kolom `Expires At`
142. Verifikasi DU-214-19 tampil sebelum DU-214-21
143. Aktor meminta daftar tab Task diurutkan turun menurut kolom `Expires At`
144. Verifikasi DU-214-21 tampil sebelum DU-214-19
