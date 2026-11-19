---
id: TC-FA-ASSIGN-E2E-060-group-in-use-guard-dep-settings-groups
title: "Group dengan baris aktif tidak dapat dihapus"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EC-ASG-93]
smoke: []
dependsOn: ["Settings Groups: hapus Group"]
trace:
  EC-ASG-93: [5, 11, 15, 17, 24, 29, 42]
anchor: [7, 38]
coverage:
  web: automated
---
# Group dengan baris aktif tidak dapat dihapus

## Prerequisites
- Aktor: Total Control `Fajar Nugroho {runId}` (DU-060-1).
- Layar awal: Settings > Groups.
- Data:
  - DU-060-1: Karyawan `Fajar Nugroho {runId}`, role Total Control, Status `Active`.
  - DU-060-2: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee DU-060-4 dan Assignee Draft DU-060-5.
  - DU-060-3: Group `Gudang Pusat {runId}`, berisi aset `Genset Perkins 20kVA {runId}`.
  - DU-060-4: ASG `Assigned` untuk Assignee `Budi Santoso {runId}` berisi aset `Genset Perkins 20kVA {runId}` dari Group `Gudang Pusat {runId}`.
  - DU-060-5: Draft Assignee `Budi Santoso {runId}` berisi aset `Monitor Gaming MSI G27 {runId}` dari Group `Showroom {runId}`, Purpose `Demo pelanggan`, tanpa ASG aktif di Group `Showroom {runId}`.
  - DU-060-6: Group `Showroom {runId}`, berisi aset `Monitor Gaming MSI G27 {runId}`.
  - DU-060-7: Group `Kantor Cabang {runId}`, berisi aset `Printer Epson L3250 {runId}`.
  - DU-060-8: ASG `Waiting for Approval` untuk Assignee `Budi Santoso {runId}` berisi aset `Printer Epson L3250 {runId}` dari Group `Kantor Cabang {runId}`.
  - DU-060-9: Group `Bengkel {runId}`, berisi aset `Bor Listrik Bosch GSB {runId}`.
  - DU-060-10: ASG `Waiting for Handover` untuk Assignee `Budi Santoso {runId}` berisi aset `Bor Listrik Bosch GSB {runId}` dari Group `Bengkel {runId}`.

## Test Steps

### Group dengan ASG aktif tidak dapat dihapus
1. Ketik Search `Gudang Pusat {runId}`, tekan Enter
2. Klik `⋯` pada baris Group `Gudang Pusat {runId}`
3. Klik `Delete`
4. Konfirmasi penghapusan pada dialog hapus Group
5. Verifikasi penghapusan Group `Gudang Pusat {runId}` ditolak dan Group tetap tampil di daftar karena masih ada baris `Assigned`

### Group yang hanya punya Draft dapat dihapus, Draft dibiarkan dan asetnya ditandai saat dibuka
6. Ganti isi kotak search dengan `Showroom {runId}`, tekan Enter
7. Verifikasi baris Group `Showroom {runId}` tampil di daftar sebelum dihapus
8. Klik `⋯` pada baris Group `Showroom {runId}`
9. Klik `Delete`
10. Konfirmasi penghapusan pada dialog hapus Group
11. Verifikasi Group `Showroom {runId}` tidak tampil lagi di daftar
12. Buka halaman Transactions > Assignment
13. Buka tab Drafts
14. Ketik Search `Monitor Gaming MSI G27 {runId}`, tekan Enter
15. Verifikasi baris Draft untuk aset `Monitor Gaming MSI G27 {runId}` tetap tampil di tab Drafts
16. Klik ikon `Edit` pada baris Draft untuk aset `Monitor Gaming MSI G27 {runId}`
17. Verifikasi baris aset `Monitor Gaming MSI G27 {runId}` ditandai dengan caption `This asset can no longer be assigned.`
18. Klik `[Cancel]` pada form Draft yang belum diubah

### Group yang dipakai ASG Waiting for Approval tidak dapat dihapus
19. Buka halaman Settings > Groups
20. Ketik Search `Kantor Cabang {runId}`, tekan Enter
21. Klik `⋯` pada baris Group `Kantor Cabang {runId}`
22. Klik `Delete`
23. Konfirmasi penghapusan pada dialog hapus Group
24. Verifikasi penghapusan Group `Kantor Cabang {runId}` ditolak dan Group tetap tampil di daftar karena masih ada baris `Waiting for Approval`

### Group yang dipakai ASG Waiting for Handover tidak dapat dihapus
25. Ganti isi kotak search dengan `Bengkel {runId}`, tekan Enter
26. Klik `⋯` pada baris Group `Bengkel {runId}`
27. Klik `Delete`
28. Konfirmasi penghapusan pada dialog hapus Group
29. Verifikasi penghapusan Group `Bengkel {runId}` ditolak dan Group tetap tampil di daftar karena masih ada baris `Waiting for Handover`

### Group dapat dihapus setelah baris aktifnya selesai
30. Buka halaman Transactions > Assignment
31. Buka tab Transactions
32. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
33. Klik `⋯` pada baris ASG untuk aset `Printer Epson L3250 {runId}`
34. Klik `Cancel Assignment`
35. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
36. Buka halaman Settings > Groups
37. Ketik Search `Kantor Cabang {runId}`, tekan Enter
38. Verifikasi baris Group `Kantor Cabang {runId}` tampil di daftar sebelum dihapus
39. Klik `⋯` pada baris Group `Kantor Cabang {runId}`
40. Klik `Delete`
41. Konfirmasi penghapusan pada dialog hapus Group
42. Verifikasi Group `Kantor Cabang {runId}` tidak tampil lagi di daftar karena baris `Waiting for Approval` sudah dibatalkan
