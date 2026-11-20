---
id: TC-FA-ASSIGN-E2E-073-foto-handover-dan-unassign-sekali-kirim
title: "Foto Handover dan Unassign pada baris tersimpan tidak dapat diganti atau dikosongkan dari Assignment"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["ASSIGN-LOGIC-21a", "ASSIGN-LOGIC-21i"]
smoke: []
dependsOn: []
trace:
  "ASSIGN-LOGIC-21a": 3
  "ASSIGN-LOGIC-21i": [8, 12, 16, 22]
anchor: [4, 5, 7, 11, 15, 21]
coverage:
  web: automated
---

# Foto Handover dan Unassign pada baris tersimpan tidak dapat diganti atau dikosongkan dari Assignment

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office {runId}`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-073-1: User (Assignee Employee), Name `Budi Santoso {runId}`, Tampil sebagai `Budi S`; User (Assignee Employee), Name `Citra Dewi {runId}`, Tampil sebagai `Citra D`.
  - DU-073-2: Assignment (ASG Unassigned), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Tablet Lenovo M10 {runId}` berstatus `Unassigned` dengan Handover Photo dan Unassign Photo tersimpan.
  - DU-073-3: Assignment (ASG Assigned), Assignee `Citra Dewi {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Mouse Logitech M170 {runId}` berstatus `Assigned` dengan Handover Photo tersimpan.

## Test Steps

### Foto pada baris Unassigned hanya dapat dilihat
1. Ketik Search `Budi Santoso {runId}`, tekan Enter
2. Klik Transaction ID pada baris hasil pencarian
3. Verifikasi header kolom `Handover Photo` dan `Unassign Photo` tampil pada tabel Assets
4. Verifikasi kolom `Handover Photo` baris `Tablet Lenovo M10 {runId}` menampilkan thumbnail
5. Verifikasi kolom `Unassign Photo` baris `Tablet Lenovo M10 {runId}` menampilkan thumbnail
6. Klik thumbnail kolom `Handover Photo` baris `Tablet Lenovo M10 {runId}`
7. Verifikasi pratinjau foto handover aset `Tablet Lenovo M10 {runId}` terbuka
8. Verifikasi pratinjau foto handover tidak memuat aksi untuk mengganti atau menghapus foto
9. Tutup pratinjau foto
10. Klik `⋯` pada baris `Tablet Lenovo M10 {runId}`
11. Verifikasi menu ⋯ memuat aksi `Assignment Log`
12. Verifikasi menu ⋯ tidak memuat aksi untuk mengganti atau menghapus Handover Photo maupun Unassign Photo
13. Tutup menu ⋯
14. Klik thumbnail kolom `Unassign Photo` baris `Tablet Lenovo M10 {runId}`
15. Verifikasi pratinjau foto unassign aset `Tablet Lenovo M10 {runId}` terbuka
16. Verifikasi pratinjau foto unassign tidak memuat aksi untuk mengganti atau menghapus foto
17. Tutup pratinjau foto

### Foto pada baris Assigned hanya dapat dilihat
18. Buka tab Assigned Assets di halaman Transactions > Assignment
19. Ketik Search `Mouse Logitech M170 {runId}`, tekan Enter
20. Klik `⋯` pada baris aset `Mouse Logitech M170 {runId}`
21. Verifikasi menu ⋯ memuat aksi `Unassign`
22. Verifikasi menu ⋯ tidak memuat aksi untuk mengganti atau menghapus Handover Photo
