---
id: TC-FA-ASSIGN-E2E-072-foto-dihapus-admin-di-file-manager-dep-file-manager
title: "Handover Photo dan Unassign Photo dihapus admin di File Manager: rujukan kosong, hasil baris tetap"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceRules: ["ASSIGN-LOGIC-21a", "ASSIGN-LOGIC-21j", "ASSIGN-LOGIC-21k", "EC-ASG-127"]
smoke: []
dependsOn: ["File Manager: Delete File di tab Files"]
trace:
  "ASSIGN-LOGIC-21a": [3, 4, 13]
  "ASSIGN-LOGIC-21j": [12, 13, 14, 23, 24, 25, 34, 35]
  "ASSIGN-LOGIC-21k": [14, 25, 35]
  "EC-ASG-127": [12, 13, 14, 23, 24, 25, 34, 35]
anchor: [6, 8, 19, 30]
coverage:
  web: automated
---

# Handover Photo dan Unassign Photo dihapus admin di File Manager: rujukan kosong, hasil baris tetap

## Prerequisites
- Aktor: Total Control `Wulan Hartati {runId}` (DU-072-1) yang dapat membuka File Manager dan Assignment.
- Layar awal: Settings > File Manager, tab Files.
- Data:
  - DU-072-1: User (Aktor Total Control), Name `Wulan Hartati {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-072-2: User (Assignee Employee), Name `Budi Santoso {runId}`, Tampil sebagai `Budi S`; User (Assignee Employee), Name `Citra Dewi {runId}`, Tampil sebagai `Citra D`.
  - DU-072-3: Assignment (ASG Unassigned), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Camera Canon EOS R {runId}` berstatus `Unassigned` dengan Handover Photo dan Unassign Photo tersimpan (Photo at start `ON`, Photo at end `ON`).
  - DU-072-4: Assignment (ASG Assigned), Assignee `Citra Dewi {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Monitor Dell P2422H {runId}` berstatus `Assigned` dengan Handover Photo tersimpan (Photo at start `ON`).
- Kondisi:
  - Kamera tidak diperlukan; foto pada DU-072-3 dan DU-072-4 sudah tersimpan saat langkah Handover dan Unassign selesai.

## Test Steps

### File Manager mencatat foto Assignment menurut Source dan Delete Handover Photo
1. Buka halaman Settings > File Manager, tab Files
2. Ketik Search `Camera Canon EOS R {runId}`, tekan Enter
3. Verifikasi baris file dengan Source `Handover Photo` dan Reference Transaction ID ASG DU-072-3 tampil untuk aset `Camera Canon EOS R {runId}`
4. Verifikasi baris file dengan Source `Return Photo` dan Reference Transaction ID ASG DU-072-3 tampil untuk aset `Camera Canon EOS R {runId}`
5. Klik `Delete` pada baris file Source `Handover Photo` aset `Camera Canon EOS R {runId}`
6. Verifikasi dialog `Delete File` tampil
7. Klik `[Delete]`
8. Verifikasi toast `Success, [File Name] has been deleted.` tampil dengan `[File Name]` berisi nama file baris itu
9. Buka halaman Transactions > Assignment, tab Transactions
10. Ketik Search `Budi Santoso {runId}`, tekan Enter
11. Klik Transaction ID pada baris hasil pencarian
12. Verifikasi kolom `Handover Photo` baris `Camera Canon EOS R {runId}` menampilkan `—`
13. Verifikasi kolom `Unassign Photo` baris `Camera Canon EOS R {runId}` masih menampilkan thumbnail
14. Verifikasi kolom Status baris `Camera Canon EOS R {runId}` tetap menampilkan `Unassigned` tanpa pesan error foto

### Delete Unassign Photo
15. Buka halaman Settings > File Manager, tab Files
16. Ketik Search `Camera Canon EOS R {runId}`, tekan Enter
17. Klik `Delete` pada baris file Source `Return Photo` aset `Camera Canon EOS R {runId}`
18. Klik `[Delete]` pada dialog `Delete File`
19. Verifikasi toast `Success, [File Name] has been deleted.` tampil dengan `[File Name]` berisi nama file baris itu
20. Buka halaman Transactions > Assignment, tab Transactions
21. Ketik Search `Budi Santoso {runId}`, tekan Enter
22. Klik Transaction ID pada baris hasil pencarian
23. Verifikasi kolom `Handover Photo` baris `Camera Canon EOS R {runId}` menampilkan `—`
24. Verifikasi kolom `Unassign Photo` baris `Camera Canon EOS R {runId}` menampilkan `—`
25. Verifikasi kolom Status baris `Camera Canon EOS R {runId}` tetap menampilkan `Unassigned` tanpa pesan error foto

### Delete Handover Photo pada baris Assigned
26. Buka halaman Settings > File Manager, tab Files
27. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
28. Klik `Delete` pada baris file Source `Handover Photo` aset `Monitor Dell P2422H {runId}`
29. Klik `[Delete]` pada dialog `Delete File`
30. Verifikasi toast `Success, [File Name] has been deleted.` tampil dengan `[File Name]` berisi nama file baris itu
31. Buka halaman Transactions > Assignment, tab Transactions
32. Ketik Search `Citra Dewi {runId}`, tekan Enter
33. Klik Transaction ID pada baris hasil pencarian
34. Verifikasi kolom `Handover Photo` baris `Monitor Dell P2422H {runId}` menampilkan `—`
35. Verifikasi kolom Status baris `Monitor Dell P2422H {runId}` tetap menampilkan `Assigned` tanpa pesan error foto
