---
id: TC-FA-MISS-E2E-040-hapus-group-dep-settings-groups
title: "Hapus Group dengan record berjalan ditolak; Group yang hanya dirujuk History boleh dihapus"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§6#r15", "§9.2#b19", "§9.4.2#r18", "§9.4.4#r6", "§10#r6", "§9.4.1#r14", "§11#r14", "EB-EDG-3"]
smoke: []
dependsOn: ["Settings Groups: aksi Delete Group"]
trace:
  "§6#r15": [4]
  "§9.2#b19": [4]
  "§9.4.2#r18": [4]
  "§9.4.4#r6": [4, 27]
  "§10#r6": [13, 14, 19, 21]
  "§9.4.1#r14": [4, 13, 14]
  "§11#r14": [4]
  "EB-EDG-3": [4, 13, 14, 19]
anchor: [12, 26]
coverage:
  web: automated
---

# Hapus Group dengan record berjalan ditolak; Group yang hanya dirujuk History boleh dihapus

## Prerequisites
- Aktor: Total Control `Rina W`.
- Layar awal: Global Settings > Groups.
- Data:
  - DU-040-1: Group `Gudang Cabang Surabaya {runId}`, dirujuk aset `Toyota Innova {runId}` yang punya record Missing berjalan berstatus `Missing`, dengan Missing Log yang memuat satu node `Reported missing by`.
  - DU-040-2: Group `Ruang Server Cadangan {runId}`, tanpa aset dan tanpa record Missing.
  - DU-040-3: Group `Ruang Arsip {runId}`, hanya dirujuk record Missing yang sudah selesai berstatus `Found` atas aset `Camera Canon EOS {runId}`.
  - DU-040-4: Pengguna `Rina W`, Total Control.
- Kondisi:
  - Akun `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Hapus Group yang punya record berjalan ditolak
1. Ketik Search `Gudang Cabang Surabaya {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Gudang Cabang Surabaya {runId}`
3. Klik `Delete`
4. Verifikasi penghapusan Group `Gudang Cabang Surabaya {runId}` ditolak dan Group tetap tampil di daftar Group

### Group tanpa record dan Group yang hanya dirujuk History dapat dihapus
5. Ganti isi kotak search dengan `Ruang Server Cadangan {runId}`, tekan Enter
6. Buka menu `⋯` pada baris `Ruang Server Cadangan {runId}`
7. Klik `Delete`
8. Ganti isi kotak search dengan `Ruang Arsip {runId}`, tekan Enter
9. Buka menu `⋯` pada baris `Ruang Arsip {runId}`
10. Klik `Delete`
11. Ganti isi kotak search dengan `{runId}`, tekan Enter
12. Verifikasi Group `Gudang Cabang Surabaya {runId}` tampil di daftar Group
13. Verifikasi Group `Ruang Server Cadangan {runId}` tidak lagi tampil di daftar Group
14. Verifikasi Group `Ruang Arsip {runId}` tidak lagi tampil di daftar Group

### Baris History tetap menampilkan Group yang sudah dihapus
15. Buka halaman `Assets`
16. Klik tab `Missing`
17. Klik sub-tab `History`
18. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
19. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Found` dengan Group `Ruang Arsip {runId}` sebagai nilai yang tersimpan saat record selesai
20. Buka Filter
21. Verifikasi opsi `Ruang Arsip {runId}` tampil pada filter Group

### Penolakan hapus Group tidak menambah node di Missing Log
22. Buka halaman `Assets`
23. Klik tab `Missing`
24. Ketik Search `Toyota Innova {runId}`, tekan Enter
25. Klik `Toyota Innova {runId}` pada kolom Name
26. Verifikasi dialog Missing Log memuat node `Reported missing by`
27. Verifikasi node lain selain `Reported missing by` tidak tampil pada dialog Missing Log
28. Tutup dialog Missing Log dengan `✕`
