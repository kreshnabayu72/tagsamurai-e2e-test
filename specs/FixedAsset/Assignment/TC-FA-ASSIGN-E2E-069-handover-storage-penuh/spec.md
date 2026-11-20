---
id: TC-FA-ASSIGN-E2E-069-handover-storage-penuh
title: "Handover berfoto ditolak saat Storage penuh dan toast menyebut pemakaian dan kuota"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceRules: ["TS-ASG-36", "V-ASG-37", "ASSIGN-LOGIC-21e", "ASSIGN-LOGIC-21g", "EC-ASG-121", "EC-ASG-122", "EC-ASG-126"]
smoke: []
dependsOn: []
trace:
  "TS-ASG-36": [5, 18]
  "V-ASG-37": [5, 6, 18]
  "ASSIGN-LOGIC-21e": [6, 30]
  "ASSIGN-LOGIC-21g": [7, 11, 12, 19, 23, 24]
  "EC-ASG-121": [5, 7, 11, 12]
  "EC-ASG-122": [18, 19, 23, 24]
  "EC-ASG-126": [29, 30]
anchor: []
coverage:
  web: automated
---

# Handover berfoto ditolak saat Storage penuh dan toast menyebut pemakaian dan kuota

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office {runId}`, bukan Assignee maupun PIC pada ASG di bawah, di entitas khusus yang Storage-nya penuh dan tidak dipakai spec lain.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-069-1: User `Budi Santoso {runId}`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-069-2: Aset `Laptop Asus Vivobook {runId}`, Group `Head Office {runId}`, tanpa TAG (`Non TAG`).
  - DU-069-3: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Head Office {runId}`, memuat DU-069-2 berstatus `Waiting for Handover`, Approval `Not required`, Need recipient confirmation `Yes`, Photo at start `ON`.
  - DU-069-4: Aset `Printer Brother HL {runId}`, Group `Head Office {runId}`, tanpa TAG (`Non TAG`).
  - DU-069-5: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Head Office {runId}`, memuat DU-069-4 berstatus `Waiting for Handover`, Approval `Not required`, Need recipient confirmation `No`, Photo at start `ON`.
- Kondisi:
  - Storage client penuh: Total Used `50.0 GB` dan Storage Quota `50.0 GB`.
  - Kamera tersedia di sesi Aktor Assignment.

## Test Steps

### Request Confirmation ditolak saat Storage penuh
1. Ketik Search `Budi Santoso {runId}`, tekan Enter
2. Klik `Hand Over` pada menu ⋯ baris ASG DU-069-3
3. Ambil foto untuk baris aset `Laptop Asus Vivobook {runId}`
4. Klik `[Request Confirmation]`
5. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
6. Verifikasi tidak ada pesan error inline di atas tombol `[Request Confirmation]` maupun pada baris aset
7. Verifikasi popup `Waiting for Confirmation` tidak tampil
8. Buka halaman Transactions > Assignment, tab Transactions
9. Ketik Search `Budi Santoso {runId}`, tekan Enter
10. Klik Transaction ID pada baris ASG DU-069-3
11. Verifikasi kolom Status baris `Laptop Asus Vivobook {runId}` tetap menampilkan `Waiting for Handover`
12. Verifikasi kolom Confirmation baris `Laptop Asus Vivobook {runId}` tetap menampilkan `Yes`

### Complete Handover ditolak saat Storage penuh
13. Buka halaman Transactions > Assignment, tab Transactions
14. Ketik Search `Budi Santoso {runId}`, tekan Enter
15. Klik `Hand Over` pada menu ⋯ baris ASG DU-069-5
16. Ambil foto untuk baris aset `Printer Brother HL {runId}`
17. Klik `[Complete Handover]`
18. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
19. Verifikasi toast `Success, 1 asset has been assigned to Budi S.` tidak tampil
20. Buka halaman Transactions > Assignment, tab Transactions
21. Ketik Search `Budi Santoso {runId}`, tekan Enter
22. Klik Transaction ID pada baris ASG DU-069-5
23. Verifikasi kolom Status baris `Printer Brother HL {runId}` tetap menampilkan `Waiting for Handover`
24. Verifikasi kolom Confirmation baris `Printer Brother HL {runId}` tetap menampilkan `No`

### Kewajiban foto didahulukan atas cek Storage
25. Buka halaman Transactions > Assignment, tab Transactions
26. Ketik Search `Budi Santoso {runId}`, tekan Enter
27. Klik `Hand Over` pada menu ⋯ baris ASG DU-069-5
28. Klik `[Complete Handover]` tanpa mengambil foto
29. Verifikasi pesan `1 asset needs a handover photo.` tampil di atas tombol
30. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tidak tampil
