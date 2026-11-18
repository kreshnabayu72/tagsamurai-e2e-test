---
id: TC-FA-ASSIGN-BE-222-nasib-dependen-dan-sinkronisasi
title: "Nasib data dependen dan sinkronisasi state lintas modul"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.7#p1", "EB-EDG-3"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.7#p1": [2, 4, 6, 15]
  "EB-EDG-3": [8, 10, 12, 14]
---

# Nasib data dependen dan sinkronisasi state lintas modul

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); `Tono Wibowo {runId}` (Total Control); pembuat Draft `Nina Marlina {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Assignee Employee ber-akun login seperti di entri data.
- Data:
  - DU-222-1: User, Aktor Assignment: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-222-2: User, Total Control yang berhak menghapus Group dan Division: Nama `Tono Wibowo {runId}`, Role `Total Control`, Cakupan Group `seluruh entitas`.
  - DU-222-3: Assignment, ASG dengan satu baris Waiting for Handover dan satu baris Waiting for Approval: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Acer Swift {runId}`, Baris 2 `Monitor LG UltraWide {runId}`, Status baris 1 `Waiting for Handover`, Status baris 2 `Waiting for Approval`, Nama Aktor sebelum rename `Rina Wijaya {runId}`, Allow Assign override Asset baris 2 `Allow, lalu diubah menjadi Deny`.
  - DU-222-4: Assignment, ASG Division yang dipakai baris aktif: Assignee `Operasional {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Perkins {runId}`, Status baris `Assigned`, PIC `Indah Permata {runId}`.
  - DU-222-5: Assignment, ASG di Group yang punya baris aktif: Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`, Group `Cabang Semarang {runId}`, Baris 1 `Meja Rapat Olympic {runId}`, Status baris `Waiting for Handover`.
  - DU-222-6: Draft, Draft yang memuat aset yang kemudian dihapus: Assignee `Dedi Prasetyo {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Kursi Staff {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Lemari Arsip Brother {runId}`, Group aset 2 `Head Office {runId}`.
  - DU-222-7: Draft, Draft yang pembuatnya kemudian dinonaktifkan: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Pembuat `Nina Marlina {runId}`, Aset 1 `Rak Gudang Besi {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-222-8: User, Pembuat Draft yang kemudian dinonaktifkan: Nama `Nina Marlina {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
- Kondisi:
  - Condition awal semua aset `Normal`.

## Test Steps

### Status baris disimpan, status header dihitung, Custody tercermin, dan log membeku
1. Rina membaca ASG `Budi Santoso {runId}` pada DU-222-3 yang memuat baris `Laptop Acer Swift {runId}` berstatus `Waiting for Handover` dan baris `Monitor LG UltraWide {runId}` berstatus `Waiting for Approval`
2. Verifikasi status header ASG itu `Waiting for Handover` sebagai turunan dari status baris yang tersimpan di tiap baris
3. Rina membatalkan baris `Laptop Acer Swift {runId}`
4. Verifikasi status header dihitung ulang menjadi `Waiting for Approval` tanpa diubah langsung dan Custody aset `Laptop Acer Swift {runId}` `Available` tercermin di semua tampilan aset
5. Allow Assign pada override Asset `Monitor LG UltraWide {runId}` diubah menjadi `Deny` dan nama Aktor `Rina Wijaya {runId}` diganti
6. Verifikasi snapshot aturan efektif baris `Monitor LG UltraWide {runId}` tidak berubah dan log lama tetap memuat nama pelaku `Rina Wijaya {runId}` sebagai nilai saat peristiwa

### Nasib dependen saat induknya dihapus atau diubah
7. Tono menghapus Assignee `Operasional {runId}` bertipe `Division` pada DU-222-4 yang dipakai baris aktif `Genset Perkins {runId}`
8. Verifikasi penghapusan ditolak oleh in-use guard dan baris `Genset Perkins {runId}` tetap `Assigned`
9. Tono menghapus Group `Cabang Semarang {runId}` pada DU-222-5 yang punya baris aktif `Meja Rapat Olympic {runId}`
10. Verifikasi penghapusan Group ditolak sampai semua baris aktif selesai dan baris tetap `Waiting for Handover`
11. Aset `Kursi Staff {runId}` pada DU-222-6 dihapus saat berada di Draft `Dedi Prasetyo {runId}`
12. Verifikasi Draft `Dedi Prasetyo {runId}` tetap tersimpan dan baris `Kursi Staff {runId}` ditandai tidak layak, bukan dihapus diam-diam
13. Pembuat Draft `Nina Marlina {runId}` pada DU-222-8 dinonaktifkan
14. Verifikasi Draft `Eko Wijaya {runId}` pada DU-222-7 tetap ada dan dapat dilanjutkan Rina sebagai Aktor lain dalam cakupan

### Log yang sudah ada tidak berubah oleh aksi berikutnya
15. Verifikasi entri Assignment Log baris `Laptop Acer Swift {runId}` yang tercatat sebelum pembatalan pada DU-222-3 tidak berubah oleh pembatalan baris itu
