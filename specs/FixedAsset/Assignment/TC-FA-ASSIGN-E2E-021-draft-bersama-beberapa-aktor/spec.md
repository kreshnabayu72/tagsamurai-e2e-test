---
id: TC-FA-ASSIGN-E2E-021-draft-bersama-beberapa-aktor
title: "Draft bersama: aktor lain melanjutkan, baris di luar cakupan, dan perubahan bersamaan"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["D-ASG-13", "FI-ASG-16", "EC-ASG-63", "EC-ASG-64", "EC-ASG-65", "EB-AKS-6"]
smoke: []
dependsOn: []
trace:
  "D-ASG-13": [17, 18]
  "FI-ASG-16": [17, 23]
  "EC-ASG-63": [17, 20]
  "EC-ASG-64": [5, 7, 8, 11]
  "EC-ASG-65": [34, 35, 36, 37]
  "EB-AKS-6": [41, 43]
anchor: [42]
coverage:
  web: automated
---

# Draft bersama: aktor lain melanjutkan, baris di luar cakupan, dan perubahan bersamaan

## Prerequisites
- Aktor:
  - Aktor A: Group Manager dengan cakupan Group `Head Office` dan `Branch Surabaya`.
  - Aktor B1: Asset Admin dengan cakupan Group `Branch Surabaya`.
  - Aktor B2: Asset Admin dengan cakupan Group `Head Office` dan `Branch Surabaya`.
  - Aktor operator: Total Control, hanya memicu pencabutan cakupan dan hak.
- Layar awal: Transactions > Assignment, tab Drafts.
- Data:
  - DU-021-1: Aktor A `Rina Hartono {runId}`, Group Manager, cakupan `Head Office` dan `Branch Surabaya`.
  - DU-021-2: Aktor B1 `Agus Prasetyo {runId}`, Asset Admin, cakupan `Branch Surabaya`.
  - DU-021-3: Aktor B2 `Hendra Kurniawan {runId}`, Asset Admin, cakupan `Head Office` dan `Branch Surabaya`.
  - DU-021-4: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, dan `Printer HP M404 {runId}`, Group `Branch Surabaya`, keduanya `Available` dan `Normal`.
  - DU-021-5: Aset `Monitor LG 24 {runId}`, Group `Head Office`, dan `Scanner Epson DS-530 {runId}`, Group `Branch Surabaya`, keduanya `Available` dan `Normal`.
  - DU-021-6: Aset `Projector Epson EB-X49 {runId}`, Group `Branch Surabaya`, `Available` dan `Normal`.
  - DU-021-7: Draft Assignee `Sari Dewi`, berisi `Laptop Dell Latitude 5420 {runId}` (Purpose `Kerja harian`) dan `Printer HP M404 {runId}` (Purpose `Operasional cabang`).
  - DU-021-8: Draft Assignee `Budi Setiawan`, berisi `Monitor LG 24 {runId}` (Purpose `Kerja harian`) dan `Scanner Epson DS-530 {runId}` (Purpose `Arsip kantor`).
  - DU-021-9: Draft Assignee `Dewi Anggraini`, berisi `Projector Epson EB-X49 {runId}` (Purpose `Presentasi`).
  - DU-021-10: Assignee Employee `Sari Dewi`, karyawan aktif dengan akun login.
  - DU-021-11: Assignee Employee `Budi Setiawan`, karyawan aktif dengan akun login.
  - DU-021-12: Assignee Employee `Dewi Anggraini`, karyawan aktif dengan akun login.
  - DU-021-13 dan DU-021-14: Purpose yang diketik di langkah: `Administrasi cabang`, `Presentasi tim`, `Rapat vendor`, `Presentasi vendor`, `Arsip cabang`, `Rapat bulanan`, dan `Rapat internal`.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Akun Aktor A, Aktor B1, dan Aktor B2 aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Draft dengan aset di luar cakupan Aktor B1 tampil read-only
1. Masuk sebagai Aktor B1
2. Klik tab `Drafts`
3. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
4. Klik Assignee `Sari Dewi` pada baris Draft
5. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` read-only dengan Group `Head Office` dan teks `Outside your groups`
6. Isi Purpose baris `Printer HP M404 {runId}` dengan `Administrasi cabang`
7. Verifikasi Purpose baris `Printer HP M404 {runId}` menampilkan `Administrasi cabang`
8. Verifikasi `[Submit]` disabled dengan alasan `Some assets are outside your groups. Ask another admin to submit.` tersampaikan pada tombol
9. Klik `[Cancel]` pada form
10. Klik `[Leave]` pada dialog Unsaved Changes
11. Verifikasi aksi `Delete` pada baris Draft `Sari Dewi` disabled dengan alasan `Some assets are outside your groups. Ask another admin to delete.` tersampaikan pada aksi

### Perubahan bersamaan atas Draft yang sama memunculkan Draft Changed
12. Ganti isi kotak search dengan `Projector Epson EB-X49 {runId}`, tekan Enter
13. Klik Assignee `Dewi Anggraini` pada baris Draft
14. Aktor A mengubah Purpose baris `Projector Epson EB-X49 {runId}` pada Draft `Dewi Anggraini` menjadi `Presentasi tim` dan menyimpannya dengan `[Save Draft]`
15. Ganti isi Purpose baris `Projector Epson EB-X49 {runId}` dengan `Rapat vendor`
16. Klik `[Save Draft]`
17. Verifikasi dialog `Draft Changed` tampil dengan teks `This draft was changed by` diikuti nama Aktor A `Rina Hartono {runId}`, lalu waktu Aktor A menyimpan pada langkah 14 sebagaimana tampil pada dialog, lalu `Reload to see the latest version; your unsaved changes will be lost.`
18. Verifikasi dialog `Draft Changed` menyediakan tombol `[Cancel]` dan `[Reload]`
19. Klik `[Reload]`
20. Verifikasi Purpose baris `Projector Epson EB-X49 {runId}` menampilkan `Presentasi tim` dari penyimpan pertama
21. Aktor A mengubah Purpose baris `Projector Epson EB-X49 {runId}` pada Draft `Dewi Anggraini` menjadi `Presentasi vendor` dan menyimpannya dengan `[Save Draft]`
22. Klik `[Submit]`
23. Verifikasi dialog `Draft Changed` juga tampil saat `[Submit]` ditekan pada Draft yang sudah diubah Aktor A
24. Klik `[Cancel]` pada dialog `Draft Changed`
25. Klik `[Cancel]` pada form (form belum diubah, tanpa dialog Unsaved Changes)

### Cakupan Group dicabut saat Draft terbuka menolak penyimpanan
26. Masuk sebagai Aktor B2
27. Klik tab `Drafts`
28. Ketik Search `Monitor LG 24 {runId}`, tekan Enter
29. Klik Assignee `Budi Setiawan` pada baris Draft
30. Aktor operator Total Control mencabut cakupan Group `Branch Surabaya` dari Aktor B2
31. Ganti isi Purpose baris `Scanner Epson DS-530 {runId}` dengan `Arsip cabang`
32. Ganti isi Purpose baris `Monitor LG 24 {runId}` dengan `Rapat bulanan`
33. Klik `[Save Draft]`
34. Verifikasi penyimpanan ditolak dengan toast `You don't have permission to do this.`
35. Verifikasi Draft dimuat ulang dengan baris `Scanner Epson DS-530 {runId}` read-only
36. Verifikasi Purpose baris `Scanner Epson DS-530 {runId}` tetap `Arsip kantor`
37. Verifikasi Purpose baris `Monitor LG 24 {runId}` tetap `Kerja harian`, sehingga perubahan pada baris dalam cakupan di simpanan yang sama ikut ditolak

### Hak Asset Admin dicabut saat halaman terbuka
38. Aktor operator Total Control mencabut hak Asset Admin Aktor B2 pada Group `Head Office`
39. Ganti isi Purpose baris `Monitor LG 24 {runId}` dengan `Rapat internal`
40. Klik `[Save Draft]`
41. Verifikasi aksi ditolak dengan toast `You don't have permission to do this.`
42. Verifikasi `[Cancel]` tampil pada form
43. Verifikasi `[Save Draft]` dan `[Submit]` tidak tampil lagi pada form
