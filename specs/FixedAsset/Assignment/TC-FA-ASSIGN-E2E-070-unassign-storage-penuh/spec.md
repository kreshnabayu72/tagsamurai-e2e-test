---
id: TC-FA-ASSIGN-E2E-070-unassign-storage-penuh
title: "Unassign berfoto ditolak seluruhnya saat Storage penuh dan kirim ulang berhasil setelah kuota ditambah"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceRules: ["TS-ASG-36", "V-ASG-37", "ASSIGN-LOGIC-21d", "ASSIGN-LOGIC-21f", "ASSIGN-LOGIC-21g", "ASSIGN-LOGIC-21h", "EC-ASG-123", "EC-ASG-126"]
smoke: []
dependsOn: []
trace:
  "TS-ASG-36": [7, 27]
  "V-ASG-37": [7, 8, 27]
  "ASSIGN-LOGIC-21d": [7, 27]
  "ASSIGN-LOGIC-21f": [11, 12]
  "ASSIGN-LOGIC-21g": [11, 12, 28]
  "ASSIGN-LOGIC-21h": [32, 35]
  "EC-ASG-123": [7, 11, 12, 27, 32, 35]
  "EC-ASG-126": [23, 24]
anchor: []
coverage:
  web: automated
---

# Unassign berfoto ditolak seluruhnya saat Storage penuh dan kirim ulang berhasil setelah kuota ditambah

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office {runId}`, bukan Assignee maupun PIC pada ASG di bawah, di entitas khusus yang Storage-nya penuh dan tidak dipakai spec lain.
- Layar awal: Transactions > Assignment, tab Assigned Assets.
- Data:
  - DU-070-1: User `Citra Dewi {runId}`, karyawan aktif dengan akun login, Assignee DU-070-4 dan DU-070-5.
  - DU-070-2: Aset `Kamera Fujifilm {runId}`, Group `Head Office {runId}`, tanpa TAG (`Non TAG`).
  - DU-070-3: Aset `Speaker Bose {runId}`, Group `Head Office {runId}`, tanpa TAG (`Non TAG`).
  - DU-070-4: ASG dengan Assignee `Citra Dewi {runId}` (Employee), Group `Head Office {runId}`, memuat DU-070-2 berstatus `Assigned`, Photo at end `ON`.
  - DU-070-5: ASG dengan Assignee `Citra Dewi {runId}` (Employee), Group `Head Office {runId}`, memuat DU-070-3 berstatus `Assigned`, Photo at end `ON`.
  - DU-070-6: Aset `Router Cisco {runId}`, Group `Head Office {runId}`, ber-TAG `QR-RTR-0091-{runId}` yang tidak terbaca.
  - DU-070-7: ASG dengan Assignee `Dimas Prasetyo {runId}` (Employee), Group `Head Office {runId}`, memuat DU-070-6 berstatus `Assigned`, Photo at end `OFF`.
- Kondisi:
  - Storage client penuh: Total Used `50.0 GB` dan Storage Quota `50.0 GB`.
  - Kamera tersedia di sesi Aktor Assignment.

## Test Steps

### Unassign dua ASG satu Assignee ditolak seluruhnya
1. Ketik Search `Kamera Fujifilm {runId}`, tekan Enter
2. Klik `⋯` pada baris aset `Kamera Fujifilm {runId}`
3. Klik `Unassign`
4. Ambil foto Unassign untuk baris aset `Kamera Fujifilm {runId}`
5. Ambil foto Unassign untuk baris aset `Speaker Bose {runId}`
6. Klik `[Submit]`
7. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
8. Verifikasi tidak ada pesan error inline di atas tombol `[Submit]` maupun pada baris aset
9. Klik `[Cancel]` pada halaman Unassign
10. Ganti isi kotak search dengan `Citra Dewi {runId}`, tekan Enter
11. Verifikasi kolom Status baris aset `Kamera Fujifilm {runId}` tetap menampilkan `Assigned`
12. Verifikasi kolom Status baris aset `Speaker Bose {runId}` tetap menampilkan `Assigned`

### Kewajiban foto didahulukan, lalu Unassign Photo wajib karena TAG tidak terbaca tetap diblokir
13. Ganti isi kotak search dengan `Router Cisco {runId}`, tekan Enter
14. Klik `⋯` pada baris aset `Router Cisco {runId}`
15. Klik `Unassign`
16. Klik `⋯` pada baris aset `Router Cisco {runId}` di halaman Unassign
17. Klik `I Can't Scan the TAG`
18. Centang TAG `QR-RTR-0091-{runId}`
19. Pilih Report Type `Unreadable`
20. Isi Note `TAG QR router rusak`
21. Kirim dialog `Report TAG` varian identifikasi manual
22. Klik `[Submit]` tanpa foto Unassign
23. Verifikasi pesan `1 asset needs an unassign photo.` tampil di atas tombol meskipun Photo at end `OFF`
24. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tidak tampil
25. Ambil foto Unassign untuk baris aset `Router Cisco {runId}`
26. Klik `[Submit]`
27. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil walau Photo at end `OFF`
28. Verifikasi toast `Success, 1 asset has been unassigned.` tidak tampil

### Kirim ulang berhasil setelah kuota ditambah
29. Kuota Storage client ditambah sehingga pemakaian berada di bawah kuota
30. Ambil ulang foto Unassign untuk baris aset `Router Cisco {runId}`
31. Klik `[Submit]`
32. Verifikasi toast `Success, 1 asset has been unassigned.` tampil
33. Buka tab History di halaman Transactions > Assignment, sub-tab By Asset
34. Ketik Search `Router Cisco {runId}`, tekan Enter
35. Verifikasi kolom Status baris aset `Router Cisco {runId}` menampilkan `Unassigned`
