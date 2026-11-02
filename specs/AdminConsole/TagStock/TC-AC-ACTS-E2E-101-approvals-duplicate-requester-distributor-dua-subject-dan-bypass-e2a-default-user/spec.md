---
id: TC-AC-ACTS-E2E-101-approvals-duplicate-requester-distributor-dua-subject-dan-bypass-e2a-default-user
title: "Approvals Duplicate: Bypass E2a Total Control dan Default User, Requester Distributor Diputuskan Principal, serta Dua Subject Satu Existing Record"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-285
  - TC-AC-ACTS-286
  - TC-AC-ACTS-297
  - TC-AC-ACTS-299
coverage:
  web: automated
---

# Approvals Duplicate: Bypass E2a Total Control dan Default User, Requester Distributor Diputuskan Principal, serta Dua Subject Satu Existing Record

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Default User `defaultUser_automated_{namaCompany}@qwertysystem.net` (Pre-setup #2), password dari `Spectra.env.AC_DU_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `RFID-ASSET-CORE-R5` (dari Stock List lewat row action Add Stock), dibuka oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kelas d (harness eksternal): simulator reader RFID (scan, `[Add by Scan]`, `[Stop]`) disediakan tim FE; mekanismenya tidak dikarang di spec.
- SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12). TAG yang discan cocok unit existing Available (identifier Data Dinamis #1: EPC `E280116060000208A1B2C3` dan UID `A1B2C3D4E5F6`, disiapkan seeding). Identifier tetap tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini; unit dan Subject yang dibuat spec ini dihapus lewat fixture BE di hook `after`. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- User Distributor kedua (Local Registration aktif) pada TC-AC-ACTS-299 tidak ada di Pre-setup TC; disediakan tim FE dan memicu batch lewat sesi API aktor (hingga tersimpan), tanpa endpoint karangan.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca jumlah Subject Tab Active, jumlah baris Event Log SKU, jumlah entri Activity Log, dan saldo Stock Ledger entitas requester (Device Allocation > Stock Balance Summary Panel) sebagai baseline (S-12).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DU_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-285: Bypass E2a, requester Total Control Principal tidak membuat Subject

1. Catat baseline jumlah Subject Tab Active, jumlah baris Event Log SKU, jumlah entri Activity Log, dan saldo Stock Ledger entitas requester
2. Klik `[Add by Scan]`, scan TAG yang cocok existing, klik `[Stop]`
3. Klik `[Submit]`
4. Tunggu aksi selesai (Preview kosong dan tombol `[Submit]` aktif kembali)
5. Buka Approvals > TAG Stock > Tab Active
6. Verifikasi tidak ada Subject baru (jumlah Subject sama dengan baseline)
7. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
8. Verifikasi unit langsung Available dengan TAG Code baru
9. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo entitas requester
10. Verifikasi saldo Stock Ledger bertambah 1 terhadap baseline
11. Buka Activity Log
12. Verifikasi jumlah entri Activity Log bertambah tepat 1 terhadap baseline
13. Verifikasi entri baru teratas `Duplicate Approved` dengan Field `Status`, Old Value `—`, New Value `Available`, dan Modified By requester
14. Buka modal Event Log SKU (Tab Add Stock)
15. Verifikasi Event Log memuat baris pembanding milik SKU itu
16. Verifikasi Event Log tidak memuat baris untuk unit bypass dan tidak memuat baris Duplicate (jumlah baris sama dengan baseline)
17. Verifikasi kolom Success batch itu tidak menghitung unit bypass
18. Tutup modal Event Log
19. Catat baseline jumlah entri Activity Log

### TC-AC-ACTS-286: Requester Default User diperlakukan sama dengan Total Control (bypass E2a)

20. Ganti akun: klik Logout
21. Login sebagai Default User (`defaultUser_automated_{namaCompany}@qwertysystem.net`)
22. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5` dari Stock List lewat row action Add Stock
23. Klik `[Add by Scan]`, scan TAG yang cocok existing, klik `[Stop]`, klik `[Submit]`
24. Tunggu aksi selesai (Preview kosong dan tombol `[Submit]` aktif kembali)
25. Buka Approvals > TAG Stock > Tab Active
26. Verifikasi tidak ada Subject baru (jumlah Subject sama dengan baseline)
27. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
28. Verifikasi unit langsung Available dengan TAG Code baru
29. Buka Activity Log
30. Verifikasi jumlah entri Activity Log bertambah tepat 1 terhadap baseline
31. Verifikasi entri baru teratas `Duplicate Approved` dengan Modified By requester

### TC-AC-ACTS-297: Requester Distributor, Subject diputuskan approver Principal bukan Distributor

32. Ganti akun: klik Logout
33. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
34. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5` dari Stock List lewat row action Add Stock
35. Catat baseline jumlah Subject Tab Active (kemampuan baca, Distributor tidak punya menu Approvals)
36. Klik `[Add by Scan]`, scan identifier yang cocok existing, klik `[Stop]`, klik `[Submit]`
37. Tunggu aksi selesai (Preview kosong dan tombol `[Submit]` aktif kembali)
38. Amati sidebar Distributor
39. Verifikasi sidebar Distributor memuat menu TAG
40. Verifikasi sidebar Distributor tidak memuat menu Approvals
41. Ganti akun: klik Logout
42. Login sebagai Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`)
43. Buka Approvals > TAG Stock > Tab Active
44. Verifikasi jumlah Subject Tab Active bertambah tepat 1 terhadap baseline, dengan Requested By `[Entity Name] (Distributor)`

### TC-AC-ACTS-299: Dua Subject pending dapat merujuk Existing Record yang sama

45. Catat baseline jumlah Subject Tab Active
46. Kirim batch Add Stock RFID berisi identifier yang cocok unit existing yang sama oleh dua user Distributor (Distributor Toggle ON dan user Distributor kedua) hingga kedua batch tersimpan (sesi API aktor)
47. Buka Approvals > TAG Stock > Tab Active
48. Verifikasi terdapat dua Subject baru berbeda dengan Existing Record sama (jumlah Subject bertambah 2 terhadap baseline; Waiting tidak dihitung sebagai target match)

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (48 langkah); alasan: semua blok satu kelas harness (kelas d, simulator reader RFID) dan satu dataset identifier, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; penggantian akun (Total Control, Default User, Distributor, lalu Total Control untuk membaca Approvals) dituntut TC.
- P-1 (state berat): asersi tidak adanya Subject, baris Event Log, dan baris Duplicate pada TC-AC-ACTS-285 memakai baseline (asersi jumlah, bukan kelas g) karena state bypass E2a baru dibangun langkah sebelumnya.
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline (S-12), "Tunggu aksi selesai" sesudah `[Submit]` yang berlanjut ke Approvals (bagian 8b butir 8), langkah ganti akun dan buka halaman, serta membuka layar baca (Approvals, Detail SKU, Device Allocation, Activity Log). Pemicu batch user Distributor kedua lewat sesi API aktor bukan konteks kedua (P-2 tidak dipakai). Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09). Langkah "Tunggu aksi selesai" ditambahkan sebelum pindah surface atau ganti akun sesudah aksi yang hasilnya tidak diasersi langsung (bagian 8b butir 8).
- Temuan untuk QA:
  - TC-AC-ACTS-285 menyebut kolom Success batch "tidak menghitung unit bypass" tanpa nilai; spec mengasersi klausa itu apa adanya.
  - TC-AC-ACTS-286, TC-AC-ACTS-297, dan TC-AC-ACTS-299 menyebut "TAG yang cocok existing" tanpa identifier; spec memakai identifier Data Dinamis #1.
  - TC-AC-ACTS-299 menyebut "dua user Distributor" tanpa menyebut akun kedua.
