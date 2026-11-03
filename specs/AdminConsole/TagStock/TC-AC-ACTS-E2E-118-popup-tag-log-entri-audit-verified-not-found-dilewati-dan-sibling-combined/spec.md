---
id: TC-AC-ACTS-E2E-118-popup-tag-log-entri-audit-verified-not-found-dilewati-dan-sibling-combined
title: "Popup TAG Log Entri Audit: Verified dengan Recovery, Not Found dengan dan Tanpa Centang, Unit Dilewati Tanpa Entri, dan Sibling Combined Tanpa Entri"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-967
  - TC-AC-ACTS-968
  - TC-AC-ACTS-969
  - TC-AC-ACTS-972
coverage:
  web: automated
---

# Popup TAG Log Entri Audit: Verified dengan Recovery, Not Found dengan dan Tanpa Centang, Unit Dilewati Tanpa Entri, dan Sibling Combined Tanpa Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: Detail SKU `RFID-ASSET-CORE-R5` > Tab Available (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kelas d (harness eksternal): simulator reader RFID untuk sesi Audit TAG (`[Start Scan]`, scan, `[Stop]`) disediakan tim FE; mekanismenya tidak dikarang di spec.
- Unit milik spec disiapkan seeding fixture BE (disediakan tim FE/BE) pada SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12): unit Damaged/Missing U-rusak (TC-AC-ACTS-967); unit Available U-hilang yang tidak ter-scan (TC-AC-ACTS-968); unit Available U-lewat yang tidak ter-scan dengan sesi memuat sedikitnya satu perubahan status lain (TC-AC-ACTS-969); unit RFID R1 combined dengan NFC N1 (TC-AC-ACTS-972). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Unit hasil Audit dipulihkan lewat fixture BE di hook `after`.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-967: Audit Verified dengan recovery menulis entri Audit Result Verified, Damaged/Missing ke Available

1. Buka Popup Audit TAG dari Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
2. Klik `[Start Scan]`, scan U-rusak lewat simulator reader RFID, klik `[Stop]`
3. Klik `[Submit]`
4. Verifikasi dialog `D-03` "Confirm Audit" tampil dengan checkbox `Mark all as Damaged/Missing — uncheck to keep their current status instead.` tercentang
5. Biarkan checkbox tercentang, klik `[Confirm]`
6. Tunggu aksi selesai (Popup Audit TAG tertutup)
7. Klik (⋯) > `TAG Log` pada U-rusak di Tab Available
8. Verifikasi entri berjudul `TAG Audited by [pelaku admin yang Submit]` dengan Description `Result: Verified` dan `Status: Damaged/Missing → Available`
9. Tutup popup lewat (X)

### TC-AC-ACTS-968: Audit Not Found dengan checkbox dicentang menulis entri Audit Available ke Damaged/Missing

10. Reset dataset: U-rusak Damaged/Missing, U-hilang dan U-lewat Available lewat fixture BE
11. Buka Popup Audit TAG, klik `[Start Scan]`, scan unit lain tanpa memindai U-hilang, klik `[Stop]`
12. Klik `[Submit]`
13. Pastikan checkbox pada dialog Confirm Audit dicentang, klik `[Confirm]`
14. Tunggu aksi selesai (Popup Audit TAG tertutup)
15. Klik (⋯) > `TAG Log` pada U-hilang di Tab Available
16. Verifikasi entri berjudul `TAG Audited by [pelaku admin yang Submit]` dengan Description `Result: Not Found` dan `Status: Available → Damaged/Missing`
17. Tutup popup lewat (X)

### TC-AC-ACTS-969: Audit Not Found dengan checkbox tidak dicentang tetap menulis entri Audit tanpa perubahan status

18. Reset dataset: U-rusak kembali Damaged/Missing, U-hilang dan U-lewat kembali Available lewat fixture BE
19. Buka Popup Audit TAG, klik `[Start Scan]`, scan unit yang berstatus Damaged/Missing (perubahan status lain) tanpa memindai U-lewat, klik `[Stop]`
20. Klik `[Submit]`
21. Hilangkan centang checkbox pada dialog Confirm Audit, klik `[Confirm]`
22. Tunggu aksi selesai (Popup Audit TAG tertutup)
23. Klik (⋯) > `TAG Log` pada U-lewat di Tab Available
24. Verifikasi entri berjudul `TAG Audited by [pelaku admin yang Submit]` dengan Description `Result: Not Found` dan `Status: Available → Available`
25. Tutup popup lewat (X)

### TC-AC-ACTS-972: Sibling combined tidak mendapat entri Audit dari unit yang diaudit

26. Reset dataset: R1 (RFID) dan N1 (NFC) berstatus Available dan combined, serta unit Available U-hilang yang tidak ter-scan (supaya dialog `D-03` muncul), lewat fixture BE
27. Buka Popup Audit TAG, klik `[Start Scan]`, scan R1 (RFID combined dengan NFC N1), klik `[Stop]`
28. Klik `[Submit]`
29. Verifikasi dialog `D-03` "Confirm Audit" tampil
30. Biarkan checkbox tercentang, klik `[Confirm]`
31. Tunggu aksi selesai (Popup Audit TAG tertutup)
32. Klik (⋯) > `TAG Log` pada R1
33. Verifikasi R1 mendapat entri `TAG Audited by ...`
34. Tutup popup lewat (X)
35. Klik (⋯) > `TAG Log` pada N1
36. Verifikasi TAG Log N1 memuat sedikitnya satu entri lain
37. Verifikasi N1 tidak mendapat entri `TAG Audited by ...`
38. Verifikasi status N1 tidak berubah
39. Tutup popup lewat (X)

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (39 langkah); alasan: semua blok satu kelas harness (kelas d, simulator reader RFID) dan satu dataset, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Kelas d: simulator reader RFID hanya untuk sesi Audit; semua blok memakai harness yang sama.
- Dialog `D-03` pada TC-AC-ACTS-967 dan TC-AC-ACTS-972 muncul secara deterministik: seeding menyisakan unit Available yang tidak ter-scan (U-hilang dan U-lewat pada TC-AC-ACTS-967; U-hilang pada TC-AC-ACTS-972), sehingga TC menulis "dialog `D-03` muncul" tanpa kondisi.
- Langkah penghubung tanpa Verifikasi (S-03): menutup popup lewat (X) sebelum langkah berikutnya (S-09), membuka Popup Audit TAG, langkah Reset dataset sebelum TC-AC-ACTS-968, TC-AC-ACTS-969, dan TC-AC-ACTS-972 (S-09; sesudah Confirm dengan checkbox tercentang pada TC-AC-ACTS-967 unit U-hilang dan U-lewat berstatus Damaged/Missing, sedangkan TC-AC-ACTS-968 membutuhkan U-hilang Available), dan "Tunggu aksi selesai" sesudah Submit atau Confirm Audit sebelum membuka TAG Log (bagian 8b butir 8).
- Absence entri `TAG Audited by ...` pada N1 didahului anchor positif (TAG Log N1 memuat entri lain; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-967 sampai TC-AC-ACTS-972 menyebut "sesi Audit men-scan ..." tanpa unit lain yang ter-scan atau tidak; spec menuliskan seeding dan scan unit lain sesuai precondition tiap TC.
  - Teks dialog Confirm Audit (checkbox "Mark all as Damaged/Missing") hanya disalin di Expected TC-AC-ACTS-967; TC-AC-ACTS-968 dan TC-AC-ACTS-972 hanya menyebut centang dan `[Confirm]`, sehingga Verifikasi dialog pada TC-AC-ACTS-972 hanya menyatakan dialog tampil.
  - Cara membuka Popup Audit TAG (label tombol) tidak disebut TC; spec memakai "Popup Audit TAG dari Detail SKU".
