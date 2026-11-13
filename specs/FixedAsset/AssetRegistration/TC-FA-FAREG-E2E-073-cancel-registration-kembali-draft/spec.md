---
id: TC-FA-FAREG-E2E-073-cancel-registration-kembali-draft
title: "Cancel Registration dengan Save as Draft to edit"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-06n, "§4.4#r14", "§9.7#r11", "§9.7#r17", D-REG-14, T-REG-10]
smoke: [D-REG-14, T-REG-10]
dependsOn: []
trace:
  FAREG-LOGIC-06n: 23
  "§4.4#r14": [5, 10, 11]
  "§9.7#r11": 19
  "§9.7#r17": [13, 16, 19]
  D-REG-14: [4, 5, 6, 7, 8]
  T-REG-10: 10
anchor: [3, 22]
coverage:
  web: automated
---

# Cancel Registration dengan Save as Draft to edit

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, pengaju pengajuan; Group terkelola `Gudang Batal {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Waiting for Approval.
- Data:
  - DU-073-1: Group `Gudang Batal {runId}`, ada di entitas aktor.
  - DU-073-2: pengajuan Waiting for Approval di Group `Gudang Batal {runId}`, diajukan Rina W.
  - DU-073-3: satu Item pada pengajuan itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `3`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `3`.
- Kondisi:
  - Group `Gudang Batal {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Cancel Registration dengan Save as Draft to edit membuat pengajuan Canceled
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Cancel registration` pada baris Group `Gudang Batal {runId}`
3. Verifikasi baris pengajuan Group `Gudang Batal {runId}` tampil di sub tab `Waiting for Approval` dengan Total Asset `3`
4. Verifikasi dialog `Cancel Registration` terbuka
5. Verifikasi dialog memuat bullet Registration ID pengajuan berformat `REG-YYYYMMDD-NNNNN`
6. Verifikasi checkbox `Save as Draft to edit` tercentang
7. Verifikasi teks bantu `The assets return to Draft and their reserved quota is released.` tampil
8. Verifikasi dialog memuat pertanyaan `Are you sure you want to cancel it?`
9. Klik `[Cancel Registration]`
10. Verifikasi toast `Success, registration has been canceled.` tampil
11. Verifikasi halaman kembali ke Registration dengan sub tab `History` aktif

12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi baris pengajuan Group `Gudang Batal {runId}` tampil di sub tab `History` dengan Status `Canceled` dan Approver `—`
14. Klik sub tab `Waiting for Approval`
15. Ketik Search `{runId}`, tekan Enter
16. Verifikasi tabel Waiting for Approval menampilkan `No results found` sehingga baris pengajuan `Gudang Batal {runId}` tidak ada

### Aset kembali ke Draft sebagai batch baru tanpa Alert
17. Klik sub tab `Draft`
18. Ketik Search `{runId}`, tekan Enter
19. Verifikasi baris Group `Gudang Batal {runId}` tampil di sub tab `Draft` dengan Total Asset `3` dan kolom `Origin` berisi Registration ID pengajuan yang dibatalkan
20. Klik ikon `Edit` pada baris Group `Gudang Batal {runId}`
21. Klik tab `General Information`
22. Verifikasi tabel Item memuat Item `Office Desk` dengan Quantity `3`
23. Verifikasi `Alert` Danger tidak tampil di atas form
