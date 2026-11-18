---
id: TC-FA-ASSIGN-E2E-034-handover-sebagian
title: "Handover sebagian: hanya sebagian aset diverifikasi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EC-ASG-19, FI-ASG-21, FI-ASG-22, FI-ASG-23, FI-ASG-17]
smoke: []
dependsOn: []
trace:
  EC-ASG-19: [17, 18, 19]
  FI-ASG-21: 18
  FI-ASG-22: 6
  FI-ASG-23: [7, 8, 12, 19]
  FI-ASG-17: [21, 22, 23]
anchor: []
coverage:
  web: automated
---

# Handover sebagian: hanya sebagian aset diverifikasi

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-034-1: User `Budi Santoso {runId}`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-034-2: Aset `Router Cisco 2901 {runId}`, Group `Head Office`, TAG `RFID`, butuh konfirmasi.
  - DU-034-3: Aset `Switch Cisco 2960 {runId}`, Group `Head Office`, TAG `RFID`, butuh konfirmasi.
  - DU-034-4: Aset `Access Point Ubiquiti {runId}`, Group `Head Office`, TAG `RFID`, butuh konfirmasi.
  - DU-034-5: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Head Office`, memuat DU-034-2, DU-034-3, dan DU-034-4 berstatus `Waiting for Handover` dengan Approval `Not required`, serta DU-034-7 berstatus `Waiting for Approval` dengan approver `Rina Wijaya` (DU-034-6), dengan Purpose `Perangkat jaringan kantor cabang {runId}`.
  - DU-034-6: User `Rina Wijaya`, Approver dengan cakupan Group `Head Office`, karyawan aktif dengan akun login.
  - DU-034-7: Aset `Toyota Avanza {runId}`, Category `Vehicle`, Group `Head Office`, TAG `RFID`, berstatus `Waiting for Approval`.
- Kondisi:
  - Need recipient confirmation efektif bernilai `Yes` untuk DU-034-2, DU-034-3, dan DU-034-4.
  - Photo at start bernilai `OFF`.
  - Require approval per Category bernilai `OFF untuk setiap Category kecuali Category Vehicle (ON)`.

## Test Steps

### Verifikasi dua dari tiga aset lalu minta konfirmasi
1. Ketik Search `{runId}`, tekan Enter
2. Klik `Hand Over` pada menu ⋯ baris ASG DU-034-5
3. Pindai TAG aset DU-034-2 lewat `[Verify Asset]`
4. Pindai TAG aset DU-034-3 lewat `[Verify Asset]`
5. Klik `[Request Confirmation]`
6. Verifikasi popup `Waiting for Confirmation` menampilkan `1 asset will stay Waiting for Handover.`
7. Verifikasi daftar aset pada popup memuat DU-034-2 dan DU-034-3
8. Verifikasi DU-034-4 tidak tampil pada daftar aset popup
9. Klik `[Confirm on This Device]`
10. Centang pernyataan `I confirm that Budi S is here and has received these assets and accepted responsibility for them.`
11. Klik `[Confirm]`
12. Verifikasi hasil pada popup mencakup hanya aset terpindai: `Budi S confirmed 2 assets.`
13. Klik `[Done]`

### Aset yang belum diverifikasi tetap Waiting for Handover
14. Buka halaman Transactions > Assignment, tab Transactions
15. Ketik Search `{runId}`, tekan Enter
16. Klik Transaction ID pada baris hasil pencarian
17. Verifikasi kolom Status DU-034-2 dan DU-034-3 menampilkan `Assigned`
18. Verifikasi kolom Status DU-034-4 menampilkan `Waiting for Handover`
19. Verifikasi badge status header menampilkan `Waiting for Handover`

### Halaman Handover hanya memuat baris Waiting for Handover
20. Klik tombol `[Hand Over]` di bawah tabel Assets
21. Verifikasi tabel Handover memuat DU-034-4
22. Verifikasi tabel Handover tidak memuat DU-034-2 dan DU-034-3
23. Verifikasi tabel Handover tidak memuat DU-034-7
