---
id: TC-FA-ASSIGN-BE-207-field-division-aset-untuk-assignee-division
title: "Field Division aset diisi dan dikembalikan untuk Assignee Division"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASSIGN-LOGIC-06n", "ASSIGN-LOGIC-06o", "ASSIGN-LOGIC-06p", "ASSIGN-LOGIC-06q", "ASSIGN-LOGIC-06r", "ASSIGN-LOGIC-06v", "ASSIGN-LOGIC-06w", "EC-ASG-96", "§9.7#r13"]
smoke: []
dependsOn: []
trace:
  "ASSIGN-LOGIC-06n": [3, 4]
  "ASSIGN-LOGIC-06o": 10
  "ASSIGN-LOGIC-06p": [12, 27, 28, 33, 39]
  "ASSIGN-LOGIC-06q": [18, 34]
  "ASSIGN-LOGIC-06r": 6
  "ASSIGN-LOGIC-06v": [23, 40]
  "ASSIGN-LOGIC-06w": [5, 13]
  "EC-ASG-96": [18, 23, 34, 40]
  "§9.7#r13": [3, 5, 7, 12, 13, 28, 34, 40]
owner: BE
---

# Field Division aset diisi dan dikembalikan untuk Assignee Division

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Grup Field Division {runId}`, sebagai pengaju, pemberi handover, dan penerima Unassign. Pengelola data aset dan pengelola master `Division` pada langkah yang menyebutnya.
- Data:
  - DU-207-1: Category beserta Asset Name, Category `Kategori Field {runId}`, Asset Name `Nama Field {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Photo at end `OFF`, Override Category Require approval `OFF`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`.
  - DU-207-2: Group aset, Group `Grup Field Division {runId}`.
  - DU-207-3: Division Assignee, Division `Gudang {runId}`.
  - DU-207-4: Division asal field aset, Division `Operasional {runId}`.
  - DU-207-5: Division tujuan edit data aset, Division `Pemasaran {runId}`.
  - DU-207-6: Division asal field aset yang akan dihapus dari master, Division `Keuangan Lama {runId}`.
  - DU-207-7: Assignee Employee dengan akun login, Name `Budi Santoso {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-207-8: PIC ber-akun login Division Gudang, Name `Joko Prasetyo {runId}`, Division `Gudang {runId}`, Status `Aktif`, Akun login `Ada`.
  - DU-207-9: Aset Aset Field Satu, Name `Aset Field Satu {runId}`, Group `Grup Field Division {runId}`, Category `Kategori Field {runId}`, Asset Name `Nama Field {runId}`, Division `Operasional {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-207-10: Aset Aset Field Employee, Name `Aset Field Employee {runId}`, Group `Grup Field Division {runId}`, Category `Kategori Field {runId}`, Asset Name `Nama Field {runId}`, Division `Operasional {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-207-11: Aset Aset Field Edit, Name `Aset Field Edit {runId}`, Group `Grup Field Division {runId}`, Category `Kategori Field {runId}`, Asset Name `Nama Field {runId}`, Division `Operasional {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-207-12: Aset Aset Field Terhapus, Name `Aset Field Terhapus {runId}`, Group `Grup Field Division {runId}`, Category `Kategori Field {runId}`, Asset Name `Nama Field {runId}`, Division `Keuangan Lama {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-207-13: Aset Aset Field Hilang, Name `Aset Field Hilang {runId}`, Group `Grup Field Division {runId}`, Category `Kategori Field {runId}`, Asset Name `Nama Field {runId}`, Division `Operasional {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-207-14: Input pengajuan untuk Assignee Division, Assignee `Gudang {runId}`, Tipe Assignee `Division`, PIC `Joko Prasetyo {runId}`, Purpose `Daily work`.
  - DU-207-15: Input pengajuan untuk Assignee Employee, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Purpose `Daily work`.
  - DU-207-16: Perubahan field Division lewat edit data aset, Division `Pemasaran {runId}`.
  - DU-207-17: Aset Aset Field Edit Hilang, Name `Aset Field Edit Hilang {runId}`, Group `Grup Field Division {runId}`, Category `Kategori Field {runId}`, Asset Name `Nama Field {runId}`, Division `Operasional {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-207-18: Aset Aset Field Terhapus Hilang, Name `Aset Field Terhapus Hilang {runId}`, Group `Grup Field Division {runId}`, Category `Kategori Field {runId}`, Asset Name `Nama Field {runId}`, Division `Keuangan Lama Dua {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-207-19: Division asal field aset yang akan dihapus dari master sebelum Report Missing, Division `Keuangan Lama Dua {runId}`.
- Kondisi:
  - Level Feature Suite Assignment pada plan adalah `Full`.
  - Setiap aset berada di Custody `Available` dan tidak berada di ASG aktif maupun Draft mana pun. Asset ID setiap aset dibentuk server dan menjadi milik entri aset itu.

## Test Steps

### Baris Assigned mengisi field Division aset dengan Division Assignee
1. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Field Satu {runId}` dan Purpose `Daily work`
2. Aktor Assignment menyelesaikan handover aset `Aset Field Satu {runId}` tanpa konfirmasi Assignee
3. Verifikasi field `Division` aset `Aset Field Satu {runId}` berisi `Gudang {runId}` setelah baris `Assigned`
4. Verifikasi nilai field `Division` sebelumnya `Operasional {runId}` tersimpan di baris sebagai snapshot
5. Verifikasi Asset ID aset `Aset Field Satu {runId}` tidak berubah dan label fisik tetap cocok
6. Verifikasi perubahan hanya terjadi pada field `Division`, sedangkan Name, Category, dan Group aset `Aset Field Satu {runId}` tidak berubah
7. Verifikasi perubahan field `Division` dicatat di Changelog Asset dengan pelaku pemberi handover

### Assignee Employee tidak mengubah field Division
8. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Field Employee {runId}` dan Purpose `Daily work`
9. Aktor Assignment menyelesaikan handover aset `Aset Field Employee {runId}` tanpa konfirmasi Assignee
10. Verifikasi field `Division` aset `Aset Field Employee {runId}` tetap `Operasional {runId}` setelah baris `Assigned`

### Unassign mengembalikan field Division ke snapshot
11. Aktor Assignment melakukan Unassign atas aset `Aset Field Satu {runId}`
12. Verifikasi field `Division` aset `Aset Field Satu {runId}` kembali menjadi `Operasional {runId}` sesuai snapshot setelah baris `Unassigned`
13. Verifikasi Asset ID aset `Aset Field Satu {runId}` tetap tidak berubah dan pengembalian field `Division` dicatat di Changelog Asset

### Field Division yang diedit selama Assigned dipertahankan
14. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Field Edit {runId}` dan Purpose `Daily work`
15. Aktor Assignment menyelesaikan handover aset `Aset Field Edit {runId}` tanpa konfirmasi Assignee
16. Pengelola data aset mengubah field `Division` aset `Aset Field Edit {runId}` menjadi `Pemasaran {runId}` lewat edit data aset
17. Aktor Assignment melakukan Unassign atas aset `Aset Field Edit {runId}`
18. Verifikasi field `Division` aset `Aset Field Edit {runId}` tetap `Pemasaran {runId}` setelah baris `Unassigned`, karena nilai hasil edit dipertahankan

### Division snapshot yang sudah dihapus dari master mengosongkan field
19. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Field Terhapus {runId}` dan Purpose `Daily work`
20. Aktor Assignment menyelesaikan handover aset `Aset Field Terhapus {runId}` tanpa konfirmasi Assignee
21. Pengelola master `Division` menghapus `Division` `Keuangan Lama {runId}`
22. Aktor Assignment melakukan Unassign atas aset `Aset Field Terhapus {runId}`
23. Verifikasi field `Division` aset `Aset Field Terhapus {runId}` kosong setelah baris `Unassigned`, karena snapshot-nya sudah dihapus dari master

### Report Missing mengembalikan field Division ke snapshot
24. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Field Hilang {runId}` dan Purpose `Daily work`
25. Aktor Assignment menyelesaikan handover aset `Aset Field Hilang {runId}` tanpa konfirmasi Assignee
26. Aktor Assignment melakukan `Report Missing` atas aset `Aset Field Hilang {runId}`
27. Verifikasi baris aset `Aset Field Hilang {runId}` berstatus `Unassigned` dengan marker `Missing`
28. Verifikasi field `Division` aset `Aset Field Hilang {runId}` kembali menjadi `Operasional {runId}` sesuai snapshot setelah penutupan oleh Report Missing

### Field Division yang diedit selama Assigned dipertahankan setelah Report Missing
29. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Field Edit Hilang {runId}` dan Purpose `Daily work`
30. Aktor Assignment menyelesaikan handover aset `Aset Field Edit Hilang {runId}` tanpa konfirmasi Assignee
31. Pengelola data aset mengubah field `Division` aset `Aset Field Edit Hilang {runId}` menjadi `Pemasaran {runId}` lewat edit data aset
32. Aktor Assignment melakukan `Report Missing` atas aset `Aset Field Edit Hilang {runId}`
33. Verifikasi baris aset `Aset Field Edit Hilang {runId}` berstatus `Unassigned` dengan marker `Missing`
34. Verifikasi field `Division` aset `Aset Field Edit Hilang {runId}` tetap `Pemasaran {runId}` setelah penutupan oleh Report Missing, karena nilai hasil edit dipertahankan

### Division snapshot yang sudah dihapus dari master mengosongkan field setelah Report Missing
35. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Field Terhapus Hilang {runId}` dan Purpose `Daily work`
36. Aktor Assignment menyelesaikan handover aset `Aset Field Terhapus Hilang {runId}` tanpa konfirmasi Assignee
37. Pengelola master `Division` menghapus `Division` `Keuangan Lama Dua {runId}`
38. Aktor Assignment melakukan `Report Missing` atas aset `Aset Field Terhapus Hilang {runId}`
39. Verifikasi baris aset `Aset Field Terhapus Hilang {runId}` berstatus `Unassigned` dengan marker `Missing`
40. Verifikasi field `Division` aset `Aset Field Terhapus Hilang {runId}` kosong setelah penutupan oleh Report Missing, karena snapshot-nya sudah dihapus dari master
