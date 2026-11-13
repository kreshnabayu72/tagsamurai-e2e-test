---
id: TC-FA-FAREG-E2E-067-activate-approval-off
title: "Submit pada Group approval OFF: aset langsung aktif"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06o, FAREG-LOGIC-20h, FAREG-LOGIC-01o, D-REG-03, T-REG-02]
smoke: [FAREG-LOGIC-01o, D-REG-03, T-REG-02]
dependsOn: []
trace:
  FAREG-LOGIC-06o: [20, 21]
  FAREG-LOGIC-20h: [10, 12]
  FAREG-LOGIC-01o: [15]
  D-REG-03: [5, 6, 7]
  T-REG-02: 9
anchor: [2]
coverage:
  web: automated
---

# Submit pada Group approval OFF: aset langsung aktif

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang Aktivasi {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-067-1: Group `Gudang Aktivasi {runId}`, ada di entitas aktor.
  - DU-067-2: batch Draft milik Rina W di Group `Gudang Aktivasi {runId}`.
  - DU-067-3: satu Item pada batch itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `3`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `3`; seluruh aset memenuhi Tingkat 2.
  - Bullet dialog yang diharapkan `Gudang Aktivasi {runId} · 3 assets`, dari Group `Gudang Aktivasi {runId}` dan Total Asset `3`.
- Kondisi:
  - Group `Gudang Aktivasi {runId}` ber-toggle `Require Approval for Registration` OFF.

## Test Steps

### Submit mengaktifkan batch dan kembali ke History
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris Group `Gudang Aktivasi {runId}` tampil di tabel Draft dengan Total Asset `3`
3. Klik ikon `Edit` pada baris Group `Gudang Aktivasi {runId}`
4. Klik `[Submit]`
5. Verifikasi dialog konfirmasi memuat bullet `Gudang Aktivasi {runId} · 3 assets`
6. Verifikasi dialog konfirmasi memuat pertanyaan `Are you sure you want to activate it?`
7. Verifikasi tombol `[Activate]` tampil di dialog konfirmasi
8. Klik `[Activate]`
9. Verifikasi toast `Success, asset has been activated.` tampil
10. Verifikasi halaman kembali ke Registration dengan sub tab `History` aktif
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi baris Group `Gudang Aktivasi {runId}` tampil dengan Total Asset `3` dan Status `Approved`
13. Klik sub tab `Draft`
14. Ketik Search `{runId}`, tekan Enter
15. Verifikasi tabel Draft menampilkan `No results found` sehingga batch `Gudang Aktivasi {runId}` tidak lagi berstatus Draft

### Detail pengajuan approval OFF: Result Approved dan Reason kosong
16. Klik sub tab `History`
17. Ketik Search `{runId}`, tekan Enter
18. Klik ikon `Detail` pada baris Group `Gudang Aktivasi {runId}`
19. Klik tab `Asset`
20. Verifikasi kolom Result bernilai `Approved` pada ketiga aset
21. Verifikasi kolom Reason kosong pada ketiga aset
