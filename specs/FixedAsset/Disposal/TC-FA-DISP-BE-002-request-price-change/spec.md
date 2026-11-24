---
id: TC-FA-DISP-BE-002-request-price-change
title: "Request Price Change mengembalikan baris Sell atau Trade-in ke approver dengan Proposed price baru"
layer: be-e2e
priority: High
caseType: Positive
status: draft
owner: BE
sourceRules: ["FLD-43", "DISP-LOGIC-21", "D-DISP-21", "TS-DISP-21", "F-FATR-07.p4g", "EC-DISP-157"]
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
trace:
  "DISP-LOGIC-21": [2, 3, 8, 9, 10, 11, 12, 13, 14, 15]
  "D-DISP-21": [2, 3, 4, 5]
  "TS-DISP-21": [7]
  "F-FATR-07.p4g": [9]
  "EC-DISP-157": [6, 7, 8, 9, 10, 11]
anchor: []
---

# Request Price Change mengembalikan baris Sell atau Trade-in ke approver dengan Proposed price baru

## Prerequisites
- Aktor: Aktor Disposal `Dian Pratama {runId}` (DU-002-1) dan Staff Disposal `Sari Utami {runId}` (DU-002-4) yang mengajukan perubahan harga; Approver `Agus Salim {runId}` (DU-002-2).
- Data:
  - DU-002-1: User, Aktor Disposal: Name `Dian Pratama {runId}`; Role Transaksi `Aktor Disposal`; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-002-2: User, Approver Disposal: Name `Agus Salim {runId}`; Role Transaksi `Approver` Disposal; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-002-3: Group, Group asal aset: Name `Gudang Harga {runId}`.
  - DU-002-4: User, Staff Disposal: Name `Sari Utami {runId}`; Role Transaksi `Staff Disposal`; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-002-5: Category: Name `Mesin Harga {runId}`; Require approval `ON`; Approval type `Any one approver`; Max price drop from approved price nilai sendiri `10`.
  - DU-002-6: Asset: Name `Mesin Ubah Harga A {runId}`; Category `Mesin Harga {runId}`; Group `Gudang Harga {runId}`; Tag `Ber-tag`; Disposal `Sell` berstatus `Waiting for Execution`, disetujui `Agus Salim {runId}`; Proposed price `10.000.000`.
  - DU-002-7: Asset: Name `Mesin Ubah Harga B {runId}`; sama dengan DU-002-6 tetapi jenis `Trade-in`; diajukan perubahan harga oleh `Sari Utami {runId}`.
  - DU-002-8: Asset: Name `Mesin Scrap {runId}`; Category `Mesin Harga {runId}`; Group `Gudang Harga {runId}`; Disposal `Scrap` berstatus `Waiting for Execution`, disetujui.
- Kondisi:
  - Nilai FLD-43 `10` di-snapshot di setiap baris saat Submit.
  - Notifikasi `disposal_waiting_approval` varian `Price change` terkirim ke approver baris itu; isi dan jalur klik dimiliki `notification.md` dan tidak diasersi rinci di spec ini.
  - Akun `Dian Pratama {runId}`, `Sari Utami {runId}`, dan `Agus Salim {runId}` aktif dan kredensialnya disediakan fase 2.
  - Spec ini belum pernah dijalankan; status `draft` sampai dijalankan.

## Test Steps

### Dialog Request Price Change dan pengajuan harga baru
1. `Dian Pratama {runId}` membuka halaman Execute Disposal dan memilih baris Sell aset `Mesin Ubah Harga A {runId}`
2. `Dian Pratama {runId}` memilih aksi baris `Request Price Change`
3. Verifikasi dialog `Request Price Change` tampil dengan daftar aset `Mesin Ubah Harga A {runId}`, teks `Approved price: 10.000.000`, field `New proposed price` dan `Price justification` yang wajib, serta teks `The asset goes back to the approver. You can execute it after the new price is approved.`
4. `Dian Pratama {runId}` mengisi New proposed price `7.500.000` tanpa Price justification lalu klik `Request Approval`
5. Verifikasi pengajuan ditolak karena Price justification wajib, dan dialog tetap terbuka
6. `Dian Pratama {runId}` mengisi Price justification `Pembeli menawar lebih rendah` lalu klik `Request Approval`
7. Verifikasi toast `Success, new price has been submitted for approval to Agus Salim {runId}.` tampil

### Efek pada baris
8. Verifikasi baris `Mesin Ubah Harga A {runId}` berstatus `Waiting for Approval` dengan Proposed price `7.500.000`, dan Condition aset tetap `In Disposal Process`
9. Verifikasi hitungan Transaction timeout baris dimulai ulang dari waktu pengajuan perubahan harga, bukan dari waktu baris pertama menunggu
10. Verifikasi Disposal Log baris memuat node `Price change requested by Dian Pratama {runId}` dengan harga lama `10.000.000`, Proposed price baru `7.500.000`, dan Price justification `Pembeli menawar lebih rendah`
11. Verifikasi `Agus Salim {runId}` menerima notifikasi `disposal_waiting_approval` varian `Price change` untuk baris itu

### Setelah disetujui, harga baru menjadi dasar batas
12. `Agus Salim {runId}` menyetujui baris `Mesin Ubah Harga A {runId}`
13. Verifikasi baris berstatus `Waiting for Execution` dengan Proposed price `7.500.000`
14. `Dian Pratama {runId}` meng-Execute baris itu dengan Final price `6.500.000` (di bawah batas baru `6.750.000`)
15. Verifikasi baris diblokir dengan caption di bawah field Final price, karena batas dihitung dari Proposed price baru `7.500.000`
16. `Dian Pratama {runId}` meng-Execute baris itu dengan Final price `7.000.000`
17. Verifikasi baris berstatus `Executed`, karena `7.000.000` di atas batas `6.750.000`

### Staff Disposal dan jenis Trade-in
18. `Sari Utami {runId}` memilih aksi baris `Request Price Change` pada baris Trade-in aset `Mesin Ubah Harga B {runId}` dan mengajukan New proposed price `8.000.000` dengan Price justification `Nilai tukar turun`
19. Verifikasi baris `Mesin Ubah Harga B {runId}` berstatus `Waiting for Approval` dengan Proposed price `8.000.000`

### Aksi tidak tersedia untuk jenis tanpa harga
20. Verifikasi baris Scrap aset `Mesin Scrap {runId}` tidak menyediakan aksi `Request Price Change`, karena aksi hanya untuk baris Sell dan Trade-in
