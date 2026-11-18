---
id: TC-FA-ASSIGN-E2E-003-transactions-sort
title: "Sort pada tab Transactions"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r5", EB-SRT-1, EB-SRT-2, "EB-SRT-3@tabel-transactions"]
smoke: []
dependsOn: []
trace:
  "§5#r5": [3, 5, 9]
  EB-SRT-1: [5, 7, 15, 17, 19, 21, 29]
  EB-SRT-2: [11, 13, 25, 27]
  "EB-SRT-3@tabel-transactions": 9
anchor: [2, 23]
coverage:
  web: automated
---

# Sort pada tab Transactions

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-003-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-003-2: Group `Head Office {runId}`.
  - DU-003-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pengaju kelima ASG DU-003-11 sampai DU-003-15.
  - DU-003-4: User `Budi Santoso {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-003-5: User `Budi Hartono {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi H`, dari `Budi Hartono {runId}`.
  - DU-003-6: User `Dewi Anggraini {runId}`, karyawan aktif tanpa akses menu Assignment; PIC aktif semua Division di bawah.
  - DU-003-7: Division `Élan Store {runId}`.
  - DU-003-8: Division `acme Retail {runId}`.
  - DU-003-9: Division `3D Print Lab {runId}`.
  - DU-003-10: Sebelas Division `Unit Kerja {n} {runId}`.
  - DU-003-11: ASG berstatus `Assigned` untuk Assignee Division `Élan Store {runId}`, aset `Kursi Ergotec A {runId}`, `Kursi Ergotec B {runId}`, dan `Kursi Ergotec C {runId}`, Total Asset `3`; dibuat pertama.
  - DU-003-12: ASG berstatus `Waiting for Approval` untuk Assignee Division `acme Retail {runId}`, aset `Laptop HP ProBook A {runId}`, `Laptop HP ProBook B {runId}`, `Laptop HP ProBook C {runId}`, dan `Laptop HP ProBook D {runId}`, Total Asset `4`; dibuat kedua.
  - DU-003-13: ASG berstatus `Waiting for Handover` untuk Assignee DU-003-4, aset `Printer Canon G3010 {runId}` dan `Scanner Epson V39 {runId}`, Total Asset `2`; dibuat ketiga.
  - DU-003-14: ASG berstatus `Assigned` untuk Assignee Division `3D Print Lab {runId}`, aset `Printer 3D Creality {runId}`, Total Asset `1`; dibuat keempat.
  - DU-003-15: ASG berstatus `Assigned` untuk Assignee DU-003-5, sepuluh aset `Meja Lipat 01 {runId}` sampai `Meja Lipat 10 {runId}`, Total Asset `10`; dibuat kelima.
  - DU-003-16: Sebelas ASG berstatus `Assigned` untuk Assignee Division `Unit Kerja {n} {runId}`, aset `Lemari Arsip {n} {runId}`, Total Asset `1`, diajukan `Wulan Hartati {runId}` (Asset Admin pada Group `Head Office {runId}`); status yang sama pada semua baris.
  - DU-003-11 sampai DU-003-15 dibuat berurutan dari DU-003-11, sehingga Request Date dan Last Updated tiap ASG lebih baru daripada ASG dengan nomor di bawahnya.

## Test Steps

### Urutan awal tanpa sort pilihan pengguna
1. Ganti isi kotak search dengan `Agus Prasetyo {runId}`, tekan Enter
2. Verifikasi tabel memuat tepat 5 baris, yaitu baris untuk Assignee `Budi S`, `acme Retail {runId}`, `Budi H`, `3D Print Lab {runId}`, dan `Élan Store {runId}`
3. Verifikasi urutan awal baris dari atas ke bawah: `Budi S`, `acme Retail {runId}`, `Budi H`, `3D Print Lab {runId}`, `Élan Store {runId}`

### Sort kolom Total Asset dan kembali ke urutan awal
4. Klik header kolom `Total Asset`
5. Verifikasi kolom `Total Asset` terurut dari kecil ke besar: `3D Print Lab {runId}` (`1`), `Budi S` (`2`), `Élan Store {runId}` (`3`), `acme Retail {runId}` (`4`), `Budi H` (`10`)
6. Klik header kolom `Total Asset` sekali lagi
7. Verifikasi kolom `Total Asset` terurut dari besar ke kecil: `Budi H`, `acme Retail {runId}`, `Élan Store {runId}`, `Budi S`, `3D Print Lab {runId}`
8. Klik header kolom `Total Asset` sekali lagi
9. Verifikasi urutan baris kembali ke urutan awal: `Budi S`, `acme Retail {runId}`, `Budi H`, `3D Print Lab {runId}`, `Élan Store {runId}`

### Sort kolom Status dengan nilai sama
10. Klik header kolom `Status`
11. Verifikasi kolom `Status` terurut A-Z: tiga baris `Assigned` (`Budi H`, `3D Print Lab {runId}`, `Élan Store {runId}`) dengan urutan sama seperti urutan awal, lalu `acme Retail {runId}` (`Waiting for Approval`), lalu `Budi S` (`Waiting for Handover`)
12. Klik header kolom `Status` sekali lagi
13. Verifikasi kolom `Status` terurut Z-A: `Budi S`, `acme Retail {runId}`, lalu tiga baris `Assigned` dengan urutan sama seperti urutan awal, yaitu `Budi H`, `3D Print Lab {runId}`, `Élan Store {runId}`

### Sort kolom Assignee dan perpindahan kolom sort
14. Klik header kolom `Assignee`
15. Verifikasi kolom `Assignee` terurut A-Z tanpa membedakan huruf besar dan kecil, dengan aksen diurutkan seperti huruf dasarnya: `3D Print Lab {runId}`, `acme Retail {runId}`, `Budi H`, `Budi S`, `Élan Store {runId}`
16. Klik header kolom `Assignee` sekali lagi
17. Verifikasi kolom `Assignee` terurut Z-A: `Élan Store {runId}`, `Budi S`, `Budi H`, `acme Retail {runId}`, `3D Print Lab {runId}`

### Sort kolom Request Date
18. Klik header kolom `Request Date`
19. Verifikasi kolom `Request Date` terurut Oldest First menurut urutan pembuatan: `Élan Store {runId}`, `acme Retail {runId}`, `Budi S`, `3D Print Lab {runId}`, `Budi H`
20. Klik header kolom `Request Date` sekali lagi
21. Verifikasi kolom `Request Date` terurut Newest First: `Budi H`, `3D Print Lab {runId}`, `Budi S`, `acme Retail {runId}`, `Élan Store {runId}`

### Sort melintasi halaman
22. Ganti isi kotak search dengan `Wulan Hartati {runId}`, tekan Enter
23. Verifikasi halaman pertama memuat tepat 10 baris dari sebelas baris `Unit Kerja {n} {runId}`
24. Klik header kolom `Status`
25. Verifikasi halaman pertama tetap memuat tepat 10 baris `Unit Kerja {n} {runId}` walau semua baris bernilai `Assigned` sama
26. Klik halaman 2
27. Verifikasi halaman kedua memuat tepat satu baris `Unit Kerja {n} {runId}` yang berbeda dari kesepuluh baris di halaman pertama
28. Klik header kolom `Assignee`
29. Verifikasi halaman kedua tetap memuat tepat satu baris `Unit Kerja {n} {runId}`
