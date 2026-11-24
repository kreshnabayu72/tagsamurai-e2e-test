---
id: TC-FA-DISP-BE-001-execute-batas-penurunan-harga
title: "Execute Disposal Sell dan Trade-in diblokir bila Final price turun melebihi Max price drop from approved price"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
owner: BE
sourceRules: ["FLD-43", "DISP-LOGIC-21", "DISP-LOGIC-07", "V-DISP-36", "S-DISP-24", "EC-DISP-154", "EC-DISP-155", "EC-DISP-156"]
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
trace:
  "FLD-43": [3, 6, 8]
  "DISP-LOGIC-21": [3, 6, 8, 10, 12, 14, 16]
  "DISP-LOGIC-07": [14, 15, 16]
  "V-DISP-36": [3, 6, 12, 14]
  "S-DISP-24": [3, 12, 14]
  "EC-DISP-154": [2, 3, 4]
  "EC-DISP-155": [7, 8]
  "EC-DISP-156": [9, 10]
anchor: []
---

# Execute Disposal Sell dan Trade-in diblokir bila Final price turun melebihi Max price drop from approved price

## Prerequisites
- Aktor: Aktor Disposal `Dian Pratama {runId}` (DU-001-1) yang melakukan Execute; Approver `Agus Salim {runId}` (DU-001-2) yang sudah menyetujui seluruh baris uji.
- Data:
  - DU-001-1: User, Aktor Disposal: Name `Dian Pratama {runId}`; Role Transaksi `Aktor Disposal`; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-001-2: User, Approver Disposal: Name `Agus Salim {runId}`; Role Transaksi `Approver` Disposal; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-001-3: Group, Group asal aset: Name `Gudang Harga {runId}`.
  - DU-001-4: Category: Name `Mesin Harga {runId}`; Require approval `ON`; Approval type `Any one approver`; Max price drop from approved price nilai sendiri `10` (sama dengan default Company); Allowed disposal types `Sell`, `Scrap`, `Donate`, `Trade-in`.
  - DU-001-5: Asset: Name `Mesin Harga M1 {runId}`; Category `Mesin Harga {runId}`; Group `Gudang Harga {runId}`; Tag `Ber-tag`; Disposal `Sell` berstatus `Waiting for Execution`, disetujui `Agus Salim {runId}`; Proposed price `10.000.000`.
  - DU-001-6: Asset: Name `Mesin Harga M2 {runId}`; sama dengan DU-001-5 (Sell, Proposed price `10.000.000`, disetujui).
  - DU-001-7: Asset: Name `Mesin Harga M3 {runId}`; sama dengan DU-001-5 (Sell, Proposed price `10.000.000`, disetujui).
  - DU-001-8: Asset: Name `Mesin Harga M4 {runId}`; sama dengan DU-001-5 (Sell, Proposed price `10.000.000`, disetujui).
  - DU-001-9: Asset: Name `Mesin Harga M5 {runId}`; Category `Mesin Harga {runId}`; Group `Gudang Harga {runId}`; Tag `Ber-tag`; Disposal `Trade-in` berstatus `Waiting for Execution`, disetujui; Proposed price `10.000.000`.
- Kondisi:
  - Nilai FLD-43 `10` sudah di-snapshot di setiap baris saat Submit (`DISP-LOGIC-01`), sehingga batas bawah Final price tiap baris adalah `10.000.000` x (1 - 10 / 100) = `9.000.000`.
  - Entitas memiliki lisensi Accounting & Depreciation (FA-7) aktif, sehingga baris yang berhasil di-Execute berstatus `Executed`.
  - Akun `Dian Pratama {runId}` aktif dan kredensialnya disediakan fase 2.
  - Spec ini belum pernah dijalankan; status `draft` sampai dijalankan.

## Test Steps

### Final price di bawah batas diblokir (Sell)
1. `Dian Pratama {runId}` membuka halaman Execute Disposal dan memilih baris Sell aset `Mesin Harga M1 {runId}`
2. `Dian Pratama {runId}` mengisi Final price `7.000.000` (30% di bawah harga yang disetujui) lalu klik Execute
3. Verifikasi baris diblokir dan caption `Final price is 30% below the approved price. Request approval for the new price.` tampil di bawah field Final price
4. Verifikasi baris tetap berstatus `Waiting for Execution`, Condition aset `Mesin Harga M1 {runId}` tetap `In Disposal Process`, dan Lifecycle aset tidak menjadi `Disposed`
5. `Dian Pratama {runId}` mengganti Final price baris yang sama menjadi `8.999.000` lalu klik Execute
6. Verifikasi baris tetap diblokir karena Final price masih di bawah batas `9.000.000`

### Final price tepat di batas dan di atas harga yang disetujui lolos
7. `Dian Pratama {runId}` meng-Execute baris Sell aset `Mesin Harga M2 {runId}` dengan Final price `9.000.000`
8. Verifikasi baris berstatus `Executed` tanpa persetujuan ulang, karena Final price tepat di batas lolos
9. `Dian Pratama {runId}` meng-Execute baris Sell aset `Mesin Harga M3 {runId}` dengan Final price `12.000.000`
10. Verifikasi baris berstatus `Executed` tanpa persetujuan ulang, karena Final price di atas harga yang disetujui tidak butuh persetujuan ulang

### Trade-in tunduk pada batas yang sama
11. `Dian Pratama {runId}` meng-Execute baris Trade-in aset `Mesin Harga M5 {runId}` dengan Final price `7.000.000`
12. Verifikasi baris diblokir dan caption `Final price is 30% below the approved price. Request approval for the new price.` tampil di bawah field Final price

### Satu baris diblokir tidak menggagalkan aset lain setelah dicentang ulang
13. `Dian Pratama {runId}` mencentang baris `Mesin Harga M1 {runId}` (Final price `7.000.000`) dan baris `Mesin Harga M4 {runId}` (Final price `10.000.000`) lalu klik Execute satu kali
14. Verifikasi pesan di baris `Mesin Harga M1 {runId}` berupa caption `Final price is 30% below the approved price. Request approval for the new price.`, dan baris `Mesin Harga M4 {runId}` tidak diproses serta tetap `Waiting for Execution`, karena satu aset gagal membuat tidak ada yang diproses
15. `Dian Pratama {runId}` menghapus centang baris `Mesin Harga M1 {runId}` lalu klik Execute
16. Verifikasi baris `Mesin Harga M4 {runId}` berstatus `Executed` dan baris `Mesin Harga M1 {runId}` tetap `Waiting for Execution`
