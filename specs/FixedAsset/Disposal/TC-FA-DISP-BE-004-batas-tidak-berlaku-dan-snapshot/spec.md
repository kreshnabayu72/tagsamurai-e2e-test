---
id: TC-FA-DISP-BE-004-batas-tidak-berlaku-dan-snapshot
title: "Max price drop from approved price tidak berlaku tanpa approval, nilai 100, dan perubahan setting tidak berlaku surut"
layer: be-e2e
priority: High
caseType: Positive
status: draft
owner: BE
sourceRules: ["FLD-43", "FLD-43d", "FLD-43f", "DISP-LOGIC-21", "DISP-LOGIC-01", "DISP-LOGIC-20", "EC-DISP-158"]
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
  - "Transaction Rules: Save Changes"
trace:
  "FLD-43": [2, 3]
  "FLD-43d": [5, 6]
  "FLD-43f": [9, 10, 11, 12]
  "DISP-LOGIC-21": [2, 3, 6, 10, 12]
  "DISP-LOGIC-01": [10, 12]
  "DISP-LOGIC-20": [10, 12]
  "EC-DISP-158": [2, 3]
anchor: []
---

# Max price drop from approved price tidak berlaku tanpa approval, nilai 100, dan perubahan setting tidak berlaku surut

## Prerequisites
- Aktor: Aktor Disposal `Dian Pratama {runId}` (DU-004-1) yang melakukan Execute; Approver `Agus Salim {runId}` (DU-004-2); Admin Total Control `Teguh Wibowo {runId}` (DU-004-4) yang mengubah setting.
- Data:
  - DU-004-1: User, Aktor Disposal: Name `Dian Pratama {runId}`; Role Transaksi `Aktor Disposal`; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-004-2: User, Approver Disposal: Name `Agus Salim {runId}`; Role Transaksi `Approver` Disposal; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-004-3: Group, Group asal aset: Name `Gudang Harga {runId}`.
  - DU-004-4: User, Admin Total Control: Name `Teguh Wibowo {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-004-5: Category tanpa approval: Name `Mesin Tanpa Approval {runId}`; Require approval `OFF`; Max price drop from approved price nilai sendiri `10`.
  - DU-004-6: Category batas 100: Name `Mesin Batas Seratus {runId}`; Require approval `ON`; Approval type `Any one approver`; Max price drop from approved price nilai sendiri `100`.
  - DU-004-7: Category snapshot: Name `Mesin Snapshot {runId}`; Require approval `ON`; Approval type `Any one approver`; Max price drop from approved price nilai sendiri `10`.
  - DU-004-8: Asset: Name `Mesin Tanpa Approval M1 {runId}`; Category `Mesin Tanpa Approval {runId}`; Group `Gudang Harga {runId}`; Tag `Ber-tag`; Disposal `Sell` berstatus `Waiting for Execution` dengan Proposed price `10.000.000`.
  - DU-004-9: Asset: Name `Mesin Batas Seratus M1 {runId}`; Category `Mesin Batas Seratus {runId}`; Group `Gudang Harga {runId}`; Tag `Ber-tag`; Disposal `Sell` berstatus `Waiting for Execution`, disetujui, Proposed price `10.000.000`.
  - DU-004-10: Asset: Name `Mesin Snapshot M1 {runId}`; Category `Mesin Snapshot {runId}`; Group `Gudang Harga {runId}`; Tag `Ber-tag`; Disposal `Sell` berstatus `Waiting for Execution`, disetujui, Proposed price `10.000.000`, snapshot FLD-43 `10`.
  - DU-004-11: Asset: Name `Mesin Snapshot M2 {runId}`; Category `Mesin Snapshot {runId}`; Group `Gudang Harga {runId}`; Tag `Ber-tag`; Status `Active`; diajukan Disposal `Sell` pada langkah 11 setelah setting diubah.
- Kondisi:
  - Baris DU-004-10 sudah diajukan dan disetujui sebelum setting pada langkah 9 diubah.
  - Entitas memiliki lisensi Accounting & Depreciation (FA-7) aktif.
  - Akun `Dian Pratama {runId}`, `Agus Salim {runId}`, dan `Teguh Wibowo {runId}` aktif dan kredensialnya disediakan fase 2.
  - Spec ini belum pernah dijalankan; status `draft` sampai dijalankan.

## Test Steps

### Tanpa approval, batas tidak berlaku
1. Verifikasi Category `Mesin Tanpa Approval {runId}` memiliki Require approval `OFF`
2. `Dian Pratama {runId}` meng-Execute baris Sell aset `Mesin Tanpa Approval M1 {runId}` dengan Final price `1.000.000` (90% di bawah Proposed price)
3. Verifikasi baris berstatus `Executed` tanpa caption pemblokiran, karena FLD-43 tidak berlaku saat Require approval OFF

### Nilai 100 menonaktifkan pemblokiran
4. Verifikasi Category `Mesin Batas Seratus {runId}` memiliki Max price drop from approved price `100`
5. `Dian Pratama {runId}` meng-Execute baris Sell aset `Mesin Batas Seratus M1 {runId}` dengan Final price `1.000`
6. Verifikasi baris berstatus `Executed` tanpa caption pemblokiran, karena batas bawah Final price menjadi 0

### Perubahan setting tidak berlaku surut
7. Verifikasi baris `Mesin Snapshot M1 {runId}` sudah menyimpan snapshot Max price drop from approved price `10`
8. `Teguh Wibowo {runId}` membuka Transaction Rules, memilih Category `Mesin Snapshot {runId}`, mengubah Max price drop from approved price menjadi `50` lalu Save Changes
9. Verifikasi Save Changes berhasil dan nilai efektif Category `Mesin Snapshot {runId}` menjadi `50`
10. `Dian Pratama {runId}` meng-Execute baris `Mesin Snapshot M1 {runId}` dengan Final price `6.000.000`
11. Verifikasi baris diblokir dengan caption `Final price is 40% below the approved price. Request approval for the new price.`, karena snapshot `10` tetap berlaku dan perubahan setting hanya berlaku untuk Request berikutnya
12. `Dian Pratama {runId}` mengajukan Disposal Sell aset `Mesin Snapshot M2 {runId}` dengan Proposed price `10.000.000`, `Agus Salim {runId}` menyetujuinya, lalu `Dian Pratama {runId}` meng-Execute baris itu dengan Final price `6.000.000`
13. Verifikasi baris `Mesin Snapshot M2 {runId}` berstatus `Executed`, karena baris yang diajukan sesudah perubahan memakai snapshot `50` dan Final price `6.000.000` masih di atas batas `5.000.000`
