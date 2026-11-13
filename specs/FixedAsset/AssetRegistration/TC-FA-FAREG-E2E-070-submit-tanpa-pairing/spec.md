---
id: TC-FA-FAREG-E2E-070-submit-tanpa-pairing
title: "Submit tanpa pairing TAG dengan alasan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-04p, "§9.4.2#r56", V-REG-11]
smoke: [V-REG-11]
dependsOn: []
trace:
  FAREG-LOGIC-04p: [13, 14]
  "§9.4.2#r56": [4, 14, 16]
  V-REG-11: 7
anchor: []
coverage:
  web: automated
---

# Submit tanpa pairing TAG dengan alasan

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang Tanpa Tag {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-070-1: Group `Gudang Tanpa Tag {runId}`, ada di entitas aktor.
  - DU-070-2: batch Draft milik Rina W di Group `Gudang Tanpa Tag {runId}`.
  - DU-070-3: satu Item pada batch itu: Asset Name `Laptop`, Brand `Dell`, Model `Latitude 5440`, Quantity `2`, TAG Type `RFID`; Total Asset `2`. Seluruh field Tingkat 2 selain Tag terpenuhi pada kedua aset.
  - DU-070-4: Tag RFID `RFID-070-{runId}` terpasang pada aset ke-1 dengan Badge `Verified`. Slot Tag RFID aset ke-2 kosong (`Unverified`), sehingga aset ke-2 hanya kurang Tag.
- Kondisi:
  - Group `Gudang Tanpa Tag {runId}` ber-toggle `Require Approval for Registration` OFF.

## Test Steps

### Skip pairing wajib beralasan, lalu Submit memproses seluruh aset
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Edit` pada baris Group `Gudang Tanpa Tag {runId}`
3. Klik `[Submit]`
4. Verifikasi dialog konfirmasi memuat peringatan `1 asset is not paired to a TAG yet.`
5. Centang `Submit them without pairing TAGs (pair later)`
6. Klik `[Activate]` tanpa memilih reason
7. Verifikasi pesan `You must pick a reason` tampil
8. Pilih reason `TAG not yet available` pada Select reason
9. Klik `[Activate]`
10. Ketik Search `{runId}`, tekan Enter
11. Klik ikon `Detail` pada baris Group `Gudang Tanpa Tag {runId}`
12. Klik tab `Asset`
13. Verifikasi kolom TAG aset ke-1 menampilkan Badge `Verified` dengan kode Tag `RFID-070-{runId}`
14. Verifikasi kolom TAG aset ke-2 menampilkan Badge `Skipped`
15. Arahkan kursor ke Badge `Skipped` aset ke-2
16. Verifikasi tooltip Badge `Skipped` memuat alasan `TAG not yet available`
