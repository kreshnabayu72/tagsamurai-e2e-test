---
id: TC-FA-ASSIGN-BE-226-storage-penuh-handover-dan-unassign-server
title: "Storage penuh: Handover dan Unassign berfoto ditolak sebelum transaksi dimulai"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: ["ASSIGN-LOGIC-21b", "ASSIGN-LOGIC-21c", "ASSIGN-LOGIC-21d", "ASSIGN-LOGIC-21e", "ASSIGN-LOGIC-21f", "ASSIGN-LOGIC-21g", "ASSIGN-LOGIC-21h", "V-ASG-37", "EC-ASG-121", "EC-ASG-122", "EC-ASG-123", "EC-ASG-124", "EC-ASG-126"]
smoke: []
dependsOn: []
owner: BE
trace:
  "ASSIGN-LOGIC-21b": [3, 12]
  "ASSIGN-LOGIC-21c": [3, 15, 27, 34]
  "ASSIGN-LOGIC-21d": [15, 18, 27]
  "ASSIGN-LOGIC-21e": 18
  "ASSIGN-LOGIC-21f": 22
  "ASSIGN-LOGIC-21g": [4, 5, 16, 23]
  "ASSIGN-LOGIC-21h": [9, 12, 31]
  "V-ASG-37": [3, 15, 21, 22, 27]
  "EC-ASG-121": [3, 4, 5, 9, 12]
  "EC-ASG-122": [15, 16]
  "EC-ASG-123": [21, 22, 23, 27, 31]
  "EC-ASG-124": 34
  "EC-ASG-126": 18
anchor: []
---

# Storage penuh: Handover dan Unassign berfoto ditolak sebelum transaksi dimulai

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Assignee `Budi Santoso {runId}` yang mengonfirmasi penerimaan; Aktor Assignment `Dewi Lestari {runId}` di entitas khusus tanpa kuota Storage.
- Data:
  - DU-226-1: User, Aktor Assignment: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-226-2: User, Assignee Employee ber-akun login: Nama `Budi Santoso {runId}`.
  - DU-226-3: Assignment, ASG dengan dua baris Waiting for Handover dan konfirmasi penerima: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Asus Vivobook {runId}`, Baris 2 `Proyektor Optoma {runId}`, keduanya Non TAG, Need recipient confirmation `Yes`, Photo at start `ON`, Approval `Not required`.
  - DU-226-4: Assignment, ASG dengan satu baris Waiting for Handover tanpa konfirmasi penerima: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Printer Brother HL {runId}`, Non TAG, Need recipient confirmation `No`, Photo at start `ON`, Approval `Not required`.
  - DU-226-5: User, Assignee dengan dua ASG Assigned: Nama `Citra Dewi {runId}`, Tipe Assignee `Employee`, ASG 1 Group `Head Office {runId}` Baris `Kamera Fujifilm {runId}`, ASG 2 Group `Head Office {runId}` Baris `Speaker Bose {runId}`, keduanya Non TAG, Photo at end `ON`.
  - DU-226-6: Assignment, ASG Assigned dengan satu baris ber-tag yang tidak terbaca: Assignee `Dimas Prasetyo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Router Cisco {runId}`, TAG `QR-RTR-0091-{runId}` yang tidak terbaca, Photo at end `OFF`.
  - DU-226-7: User, Aktor Assignment di entitas khusus yang Storage-nya belum pernah dialokasikan: Nama `Dewi Lestari {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-226-8: Assignment, ASG di entitas DU-226-7 dengan satu baris Waiting for Handover: Assignee `Hana Permatasari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kursi Ergonomis {runId}`, Non TAG, Need recipient confirmation `No`, Photo at start `ON`, Approval `Not required`.
- Kondisi:
  - Storage client entitas DU-226-1 penuh: pemakaian sama dengan kuota, kecuali dinyatakan lain pada langkah.
  - Entitas DU-226-7 adalah entitas khusus yang tidak dipakai spec lain, tanpa kuota Storage yang dialokasikan.

## Test Steps

### Request Confirmation ditolak sebelum sesi konfirmasi dibuat
1. Rina mengambil satu foto Handover untuk baris `Laptop Asus Vivobook {runId}` dan `Proyektor Optoma {runId}` pada ASG DU-226-3
2. Rina menekan `[Request Confirmation]` untuk ASG DU-226-3
3. Verifikasi pengiriman ditolak karena Storage penuh sebelum transaksi langkah dimulai
4. Verifikasi kedua baris ASG DU-226-3 tetap `Waiting for Handover`
5. Verifikasi tidak ada sesi konfirmasi aktif, Task `Confirm Handover`, maupun notifikasi `assignment_confirmation_required` untuk Assignee `Budi Santoso {runId}`

### Penolakan tidak mengunci ASG dan kirim ulang berhasil setelah kuota ditambah
6. Kuota Storage client ditambah sehingga pemakaian berada di bawah kuota
7. Rina mengambil ulang satu foto Handover untuk baris `Laptop Asus Vivobook {runId}` dan `Proyektor Optoma {runId}`
8. Rina menekan `[Request Confirmation]` untuk ASG DU-226-3
9. Verifikasi sesi konfirmasi aktif untuk ASG DU-226-3 terbentuk pada pengiriman ulang dan Assignee `Budi Santoso {runId}` menerima Task `Confirm Handover`
10. Unggahan file lain mengisi Storage client hingga pemakaian sama dengan kuota
11. Assignee `Budi Santoso {runId}` mengonfirmasi penerimaan kedua aset lewat Task `Confirm Handover`
12. Verifikasi konfirmasi Assignee berhasil walau Storage penuh dan kedua baris ASG DU-226-3 menjadi `Assigned`, karena konfirmasi tidak menyimpan file baru

### Complete Handover ditolak dan tidak ada jalur tanpa foto
13. Rina mengambil satu foto Handover untuk baris `Printer Brother HL {runId}` pada ASG DU-226-4
14. Rina menekan `[Complete Handover]` untuk ASG DU-226-4
15. Verifikasi pengiriman ditolak karena Storage penuh dan baris `Printer Brother HL {runId}` tetap `Waiting for Handover`
16. Verifikasi Custody aset `Printer Brother HL {runId}` tidak menjadi `Assigned` dan tidak ada Confirmation `Not required` atau notifikasi Handover
17. Rina menekan `[Complete Handover]` untuk ASG DU-226-4 tanpa foto Handover
18. Verifikasi pengiriman tanpa foto ditolak karena foto wajib, bukan karena Storage penuh, dan baris tetap `Waiting for Handover`

### Unassign ditolak seluruhnya sebelum ASG mana pun diproses
19. Rina mengambil satu foto Unassign untuk baris `Kamera Fujifilm {runId}` dan `Speaker Bose {runId}`
20. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Citra Dewi {runId}` dengan kedua baris
21. Verifikasi pengiriman ditolak karena Storage penuh
22. Verifikasi tidak ada baris dari kedua ASG yang diproses sebagian
23. Verifikasi kedua baris tetap `Assigned`, Custody kedua aset tidak menjadi `Available`, dan tidak ada Damage Report maupun notifikasi `assignment_unassigned` untuk Assignee `Citra Dewi {runId}`

### Unassign Photo wajib karena TAG tidak terbaca tetap diblokir
24. Rina melaporkan tag baris `Router Cisco {runId}` tidak terbaca lewat `I Can't Scan the TAG` pada halaman Unassign untuk Assignee `Dimas Prasetyo {runId}`
25. Rina mengambil satu foto Unassign untuk baris `Router Cisco {runId}`
26. Rina menekan `[Submit]` untuk baris `Router Cisco {runId}`
27. Verifikasi pengiriman ditolak karena Storage penuh walau Photo at end `OFF`, dan baris `Router Cisco {runId}` tetap `Assigned`
28. Kuota Storage client ditambah sehingga pemakaian berada di bawah kuota
29. Rina mengambil ulang satu foto Unassign untuk baris `Router Cisco {runId}`
30. Rina menekan `[Submit]` untuk baris `Router Cisco {runId}`
31. Verifikasi baris `Router Cisco {runId}` berstatus `Unassigned` pada pengiriman ulang

### Client tanpa kuota Storage tidak diblokir
32. Dewi mengambil satu foto Handover untuk baris `Kursi Ergonomis {runId}` pada ASG DU-226-8
33. Dewi menekan `[Complete Handover]` untuk ASG DU-226-8
34. Verifikasi baris `Kursi Ergonomis {runId}` berstatus `Assigned` tanpa penolakan Storage
