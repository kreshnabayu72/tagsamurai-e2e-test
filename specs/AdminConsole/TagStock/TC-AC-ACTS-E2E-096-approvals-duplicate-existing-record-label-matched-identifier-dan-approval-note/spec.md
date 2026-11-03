---
id: TC-AC-ACTS-E2E-096-approvals-duplicate-existing-record-label-matched-identifier-dan-approval-note
title: "Approvals Duplicate: Nama User Dengan Hover, Placeholder Approval Note, Existing Record Deleted, Label Stock/Client, dan Matched Identifier RFID, NFC, BLE, GPS"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-300
  - TC-AC-ACTS-301
  - TC-AC-ACTS-302
  - TC-AC-ACTS-729
  - TC-AC-ACTS-750
  - TC-AC-ACTS-764
coverage:
  web: automated
---

# Approvals Duplicate: Nama User Dengan Hover, Placeholder Approval Note, Existing Record Deleted, Label Stock/Client, dan Matched Identifier RFID, NFC, BLE, GPS

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: Approvals > TAG Stock > Tab Active (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data Subject pending disiapkan seeding fixture BE (disediakan tim FE/BE): Subject dengan Existing Record Available (`TAG-4F7K2XQ9`, entitas `PT Principal`), Damaged/Missing, dan In Use (Client pemegang); Subject RFID dengan UID cocok dan Subject RFID dengan hanya EPC cocok; Subject NFC, BLE, dan GPS; Subject Register Duplicate dengan Existing Record didaftarkan `Budi Santoso` dan New Request dipindai `Sari Dewi` (Data Dinamis #3); Subject Register Duplicate dengan Existing Record unit In Use hasil BYO Jalur B milik Client `PT XYZ`.
- Pelaku `PT XYZ` menghapus tag di Global Settings > TAG lewat sesi API aktor (disediakan tim FE/BE; akun tidak ada di Pre-setup TC).
- Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-300: Existing Record menampilkan label Stock untuk Available atau Damaged/Missing dan Client untuk In Use

1. Buka Approvals > TAG Stock > Tab Active
2. Lihat kolom Existing Record pada tiga Subject (Existing Record Available, Damaged/Missing, dan In Use)
3. Verifikasi Subject Available menampilkan `TAG-4F7K2XQ9 — Available (Stock: PT Principal)`
4. Verifikasi Subject Damaged/Missing memakai pola `Stock: [Entity Name]`
5. Verifikasi Subject In Use memakai `Client: [Client Name]`
6. Verifikasi Subject Activation Collision selalu In Use
7. Verifikasi hanya dua pola Label itu yang ada, unit Waiting for Approval atau Rejected tidak pernah tampil sebagai Existing Record

### TC-AC-ACTS-301: Matched Identifier RFID, UID menang tampilan dengan badge UID dan EPC saja dengan badge EPC

8. Lihat kolom Matched Identifier pada Subject RFID dengan UID cocok dan Subject RFID dengan hanya EPC cocok
9. Verifikasi Subject UID cocok menampilkan nilai UID dengan badge `[UID]`
10. Verifikasi Subject hanya EPC menampilkan nilai EPC dengan badge `[EPC]`

### TC-AC-ACTS-302: Matched Identifier NFC, BLE, GPS tanpa badge sumber

11. Lihat kolom Matched Identifier pada Subject NFC, BLE, dan GPS
12. Verifikasi hanya nilai identifier tampil tanpa badge sumber

### TC-AC-ACTS-729: Dialog Review menulis nama user sebagai first name dan inisial dengan hover nama lengkap

13. Klik `Review` pada Subject Register Duplicate dengan Existing Record didaftarkan Budi Santoso dan New Request dipindai Sari Dewi
14. Verifikasi `Registered by` pada blok Existing Record menampilkan ikon user dan `Budi S`
15. Verifikasi `Scanned by` pada blok New Request menampilkan ikon user dan `Sari D`
16. Hover `Budi S`
17. Verifikasi tooltip nama lengkap `Budi Santoso`
18. Hover `Sari D`
19. Verifikasi tooltip nama lengkap `Sari Dewi`
20. Klik `[Cancel]`

### TC-AC-ACTS-750: Approval Note di dialog Review memiliki placeholder dan tanpa helper text

21. Klik `Review` pada satu Subject
22. Verifikasi label `Approval Note`
23. Verifikasi placeholder `Enter approval note` tampil saat field kosong
24. Verifikasi tidak ada helper text
25. Verifikasi tidak ada live counter karakter
26. Verifikasi default state field adalah placeholder
27. Klik `[Cancel]`

### TC-AC-ACTS-764: Existing Record menampilkan TAG Code dengan Deleted bila unit sudah dihapus dan Subject pending tetap valid

28. Lihat kolom Existing Record Subject Register Duplicate dengan Existing Record unit In Use hasil BYO Jalur B milik Client PT XYZ
29. Verifikasi kolom Existing Record menampilkan `[TAG Code] — In Use (Client: PT XYZ)`
30. Client PT XYZ menghapus tag tersebut di Global Settings > TAG hingga tersimpan (sesi API aktor; unit Jalur B ikut dihapus)
31. Muat ulang Tab Active setiap 5 detik sampai event Delete TAG diproses (batas tunggu 2 menit)
32. Verifikasi kolom Existing Record menampilkan `[TAG Code] — Deleted`
33. Klik `Review` pada Subject itu
34. Verifikasi blok Existing Record di dialog menampilkan `[TAG Code] — Deleted`
35. Verifikasi Subject tetap Pending di Tab Active (tidak Canceled)
36. Verifikasi radio Approve dan Reject masih dapat dipilih
37. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (37 langkah); alasan: semua blok satu halaman dan satu kelas harness (pembacaan Tab Active), tanpa aksi tulis kecuali satu pemicu sesi API pada TC-AC-ACTS-764, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa Verifikasi (S-03): `[Cancel]` menutup dialog Review sebelum TC berikutnya (S-09); langkah memuat ulang Tab Active tiap 5 detik memakai idiom baku "polling worker commit" (bagian 6, batas tunggu 2 menit).
- Pemicu pelaku kedua lewat sesi API (langkah "hingga tersimpan") bukan konteks kedua (P-2 tidak dipakai; keputusan 2026-10-30).
- TC-AC-ACTS-764 memakai Subject berbeda dari TC lain; Subject itu dipakai spec ini saja dan dipulihkan lewat fixture BE di hook `after`.
- Temuan untuk QA:
  - TC-AC-ACTS-764 menyebut "Muat ulang Tab Active" dan "ulangi pengamatan Tab Active" tanpa batas waktu event Delete TAG; spec memakai idiom polling 2 menit.
  - TC-AC-ACTS-300 memuat `TAG-4F7K2XQ9 — Available (Stock: PT Principal)` sebagai nilai literal Pre-setup; spec mengasersinya apa adanya.
