---
id: TC-FA-FAREG-E2E-076-detail-pengajuan-isi
title: "Detail pengajuan: isi salinan saat Submit, Result, dan Reason"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#b1", "§4.1#b3", "§9.7#p1"]
smoke: []
dependsOn: []
trace:
  "§4.1#b1": [4, 5, 6, 7, 16]
  "§4.1#b3": [9, 10, 11, 12]
  "§9.7#p1": 6
anchor: []
coverage:
  web: automated
---

# Detail pengajuan: isi salinan saat Submit, Result, dan Reason

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, pengaju pengajuan; Group terkelola `Gudang Salinan {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > History.
- Data:
  - DU-076-1: Group `Gudang Salinan {runId}`, ada di entitas aktor.
  - DU-076-2: pengajuan berstatus Partially Approved di Group `Gudang Salinan {runId}`, diajukan Rina W dan diputuskan Budi S.
  - DU-076-3: satu Item pada pengajuan itu saat Submit: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `3`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `3`.
  - DU-076-4: keputusan Budi S per aset: aset ke-1 `Approve` tanpa Reason; aset ke-2 `Return to Draft` dengan Reason `Photo is missing`; aset ke-3 `Reject` dengan Reason `Duplicate entry`.

## Test Steps

### Detail dari History memuat salinan form saat Submit
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Detail` pada baris Group `Gudang Salinan {runId}`
3. Klik tab `General Information`
4. Verifikasi header halaman Detail memuat Group `Gudang Salinan {runId}`
5. Verifikasi form tampil read-only tanpa tombol `[Save draft]`
6. Verifikasi tabel Item memuat Item `Office Desk` dengan Brand `Kayu Jati`, Model `No Model`, dan Quantity `3`
7. Verifikasi tab General Information tidak memuat field `Group`

### Result dan Reason dari keputusan approver
8. Klik tab `Asset`
9. Verifikasi aset ke-1 kolom Result `Approved`
10. Verifikasi aset ke-2 kolom Result `Returned` dengan Reason `Photo is missing`
11. Verifikasi aset ke-3 kolom Result `Rejected` dengan Reason `Duplicate entry`
12. Verifikasi aset ke-1 kolom Reason kosong

### Registration ID membuka Detail yang sama
13. Klik `[Close]` pada footer halaman Detail
14. Ketik Search `{runId}`, tekan Enter
15. Klik Registration ID pada baris Group `Gudang Salinan {runId}`
16. Verifikasi halaman Detail terbuka dengan tab `General Information` dan tab `Asset`
