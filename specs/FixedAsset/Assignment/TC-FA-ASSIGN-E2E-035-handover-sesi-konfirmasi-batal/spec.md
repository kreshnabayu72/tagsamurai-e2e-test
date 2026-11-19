---
id: TC-FA-ASSIGN-E2E-035-handover-sesi-konfirmasi-batal
title: "Sesi konfirmasi dibatalkan lewat Cancel Request"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [DO-ASG-01, DO-ASG-02, DO-ASG-03, DO-ASG-06]
smoke: []
dependsOn: []
trace:
  DO-ASG-01: [12, 28]
  DO-ASG-02: 21
  DO-ASG-03: [14, 30]
  DO-ASG-06: [8, 24]
anchor: [5, 19]
coverage:
  web: automated
---

# Sesi konfirmasi dibatalkan lewat Cancel Request

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah (sesi Aktor). Assignee `Budi S` memantau Task miliknya di sesi terpisah (sesi Assignee).
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-035-1: User `Budi Santoso`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-035-2: Aset `Handheld Scanner Zebra {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), butuh konfirmasi.
  - DU-035-3: Aset `Tablet Samsung Tab S8 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), butuh konfirmasi.
  - DU-035-4: ASG dengan Assignee `Budi S` (Employee), Group `Head Office`, memuat DU-035-2 dan DU-035-3, keduanya berstatus `Waiting for Handover` dengan Approval `Not required` dan Purpose `Survei lapangan kuartal ini {runId}`.
- Kondisi:
  - Need recipient confirmation efektif bernilai `Yes` untuk DU-035-2 dan DU-035-3.
  - Photo at start bernilai `OFF`.
  - Jendela konfirmasi Handover bernilai `15 menit`.
  - Akun `Budi S` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Cancel Request menutup sesi dan Task Assignee
1. Ketik Search `{runId}`, tekan Enter
2. Klik `Hand Over` pada menu ⋯ baris ASG DU-035-4
3. Klik `[Request Confirmation]`
4. Di sesi Assignee, buka daftar Task milik `Budi S`
5. Verifikasi di sesi Assignee, Task `Confirm Handover` untuk ASG DU-035-4 tampil
6. Di sesi Aktor, klik `[Cancel Request]`
7. Di sesi Assignee, muat ulang halaman
8. Verifikasi di sesi Assignee, Task `Confirm Handover` untuk ASG DU-035-4 tidak tampil

### Baris tetap Waiting for Handover dan log mencatat pembatalan
9. Di sesi Aktor, buka halaman Transactions > Assignment, tab Transactions
10. Ketik Search `{runId}`, tekan Enter
11. Klik Transaction ID pada baris hasil pencarian
12. Verifikasi kolom Status DU-035-2 dan DU-035-3 menampilkan `Waiting for Handover`
13. Klik `Assignment Log` pada menu ⋯ baris DU-035-2
14. Verifikasi Assignment Log memuat node `Confirmation not received`
15. Tutup dialog Assignment Log

### Jendela konfirmasi habis menutup sesi dan Task Assignee
16. Klik tombol `[Hand Over]` di bawah tabel Assets
17. Klik `[Request Confirmation]`
18. Di sesi Assignee, muat ulang halaman
19. Verifikasi di sesi Assignee, Task `Confirm Handover` untuk ASG DU-035-4 tampil
20. Waktu berlalu sampai 15 menit sejak permintaan konfirmasi dikirim
21. Verifikasi di sesi Aktor, popup `Waiting for Confirmation` menampilkan `Budi S didn't confirm. Try again.`
22. Klik `[Done]`
23. Di sesi Assignee, muat ulang halaman
24. Verifikasi di sesi Assignee, Task `Confirm Handover` untuk ASG DU-035-4 tidak tampil

### Baris tetap Waiting for Handover sesudah jendela habis
25. Di sesi Aktor, buka halaman Transactions > Assignment, tab Transactions
26. Ketik Search `{runId}`, tekan Enter
27. Klik Transaction ID pada baris hasil pencarian
28. Verifikasi kolom Status DU-035-2 dan DU-035-3 menampilkan `Waiting for Handover`
29. Klik `Assignment Log` pada menu ⋯ baris DU-035-2
30. Verifikasi Assignment Log memuat dua node `Confirmation not received`
