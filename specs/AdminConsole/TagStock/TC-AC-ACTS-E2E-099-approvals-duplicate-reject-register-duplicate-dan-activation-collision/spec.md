---
id: TC-AC-ACTS-E2E-099-approvals-duplicate-reject-register-duplicate-dan-activation-collision
title: "Approvals Duplicate: Reject Register Duplicate (Unit Rejected Tidak Masuk Stok) dan Reject Activation Collision (Alasan Tidak Diteruskan ke Client)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-281
  - TC-AC-ACTS-282
coverage:
  web: automated
---

# Approvals Duplicate: Reject Register Duplicate (Unit Rejected Tidak Masuk Stok) dan Reject Activation Collision (Alasan Tidak Diteruskan ke Client)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: Approvals > TAG Stock > Tab Active (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data Subject disiapkan seeding fixture BE (disediakan tim FE/BE): Subject Register Duplicate pending dari requester Distributor dengan Total Registered SKU = 10 dan saldo Stock Ledger entitas requester dicatat; Subject Activation Collision pending dari Client pemohon di Global Settings. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Akun Client pemohon di Global Settings tidak ada di Pre-setup TC; disediakan tim FE (kredensial dan akses Notification Center), tanpa karangan di spec.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca saldo Stock Ledger (Device Allocation > Stock Balance Summary Panel) dan kemampuan baca jumlah notifikasi Client pemohon (baseline, S-12).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-281: Reject Register Duplicate, unit Rejected tidak masuk stok

1. Buka Approvals > TAG Stock > Tab Active
2. Klik `Review` pada Subject Register Duplicate pending, catat Total Registered SKU dan saldo Stock Ledger entitas requester
3. Pilih Reject
4. Isi Approval Note `Duplicate hardware`
5. Klik `[Submit]`
6. Verifikasi toast "Success, duplicate TAG has been rejected."
7. Buka Approvals > Tab History
8. Verifikasi Subject masuk Tab History dengan Approval `Rejected`
9. Verifikasi TAG Code Subject itu `—`
10. Buka TAG > Stock dan baca Total Registered SKU itu
11. Verifikasi Total Registered tetap `10`
12. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo
13. Verifikasi saldo Stock Ledger entitas requester tidak berubah

### TC-AC-ACTS-282: Reject Activation Collision, alasan tidak diteruskan ke Client

14. Catat baseline jumlah notifikasi Client pemohon (kemampuan baca BE)
15. Buka Approvals > TAG Stock > Tab Active
16. Klik `Review` pada Subject Activation Collision pending
17. Pilih Reject
18. Isi Approval Note `Tag milik client lain`
19. Klik `[Submit]`
20. Verifikasi toast "Success, request has been rejected."
21. Buka Approvals > Tab History
22. Verifikasi Subject masuk Tab History dengan Approval `Rejected`
23. Ganti akun: klik Logout
24. Login sebagai Client pemohon di Global Settings (akun disediakan tim FE)
25. Buka Notification Center
26. Verifikasi notifikasi hasil penolakan untuk Client tampil (jumlah notifikasi bertambah tepat 1 terhadap baseline)
27. Verifikasi notifikasi ke Client tidak memuat alasan reviewer `Tag milik client lain`

## Notes

- Mode: FE+BE.
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline Total Registered, saldo, dan jumlah notifikasi Client (S-12), serta langkah ganti akun dan buka Notification Center. Absence alasan reviewer didahului anchor positif (notifikasi hasil penolakan tampil; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-282 menyebut "Client pemohon di Global Settings" tanpa email atau akun di Pre-setup; spec menulis akun itu "disediakan tim FE".
  - TC-AC-ACTS-281 menyebut Total Registered SKU = 10 sebagai nilai awal absolut; spec memakai nilai seeding yang sama dan mengasersi tidak berubah.
