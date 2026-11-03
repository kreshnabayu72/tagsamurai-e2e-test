---
id: TC-AC-ACTS-E2E-105-resilience-approvals-error-detail-gagal-muat-timeout-dan-download-gagal
title: "Resilience Approvals: Approve atau Reject Gagal 5xx, Detail Approval Gagal Dimuat, Tanpa Respons (T-24), Detail History Gagal Dimuat, dan Download Gagal dengan Nama Sub-Menu"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-293
  - TC-AC-ACTS-295
  - TC-AC-ACTS-730
  - TC-AC-ACTS-776
  - TC-AC-ACTS-810
coverage:
  web: automated
---

# Resilience Approvals: Approve atau Reject Gagal 5xx, Detail Approval Gagal Dimuat, Tanpa Respons (T-24), Detail History Gagal Dimuat, dan Download Gagal dengan Nama Sub-Menu

## Prerequisites

- Mode: FE+BE. Intercept respons 5xx dan penahanan respons sampai timeout lewat `Spectra.intercept()` di atas backend nyata; intercept dilepas segera setelah asersi (S-09).
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: Approvals > TAG Stock > Tab Active (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data Subject disiapkan seeding fixture BE (disediakan tim FE/BE): Subject pending di Tab Active (Register Duplicate dan Activation Collision) dan sedikitnya satu Subject Approved di Tab History. Spec ini tidak mengubah Subject karena semua Submit gagal. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-295: Detail Approval gagal dimuat menampilkan error di body dialog

1. Buka Approvals > TAG Stock > Tab Active
2. Intercept data Subject dengan 5xx
3. Klik `Review` pada Subject pending
4. Verifikasi body dialog menampilkan `Unable to load this data.` dan `[Try Again]`
5. Verifikasi footer hanya memuat `[Cancel]`
6. Verifikasi `[Submit]` disabled
7. Lepas intercept data Subject
8. Klik `[Cancel]`

### TC-AC-ACTS-730: Detail Approval Tab History gagal dimuat, error di body dialog dengan footer hanya Close

9. Buka Tab History
10. Intercept data Subject dengan 5xx
11. Klik (⋯) > `Detail` pada baris Approved
12. Verifikasi body dialog menampilkan `Unable to load this data.` dan `[Try Again]`
13. Verifikasi footer hanya memuat `[Close]`
14. Lepas intercept data Subject
15. Klik `[Close]`

### TC-AC-ACTS-776: Download Approvals > TAG Stock gagal menampilkan toast error dengan nama sub-menu (Tab Active dan Tab History)

16. Intercept respons Download dengan 5xx
17. Pada Tab History, klik Download, pilih Download as CSV
18. Verifikasi toast error "Error, failed to download TAG-Stock."
19. Verifikasi tidak ada toast sukses Download pada Tab History
20. Buka Tab Active, klik Download, pilih Download as CSV
21. Verifikasi toast error "Error, failed to download TAG-Stock."
22. Verifikasi tidak ada toast sukses Download pada Tab Active
23. Lepas intercept respons Download

### TC-AC-ACTS-293: Approve atau Reject gagal 5xx, toast T-14 dan pilihan dipertahankan

24. Klik `Review` pada Subject pending
25. Pilih Approve dan isi Approval Note `Setuju`
26. Intercept respons Submit dengan 5xx
27. Klik `[Submit]`
28. Verifikasi toast "Error, failed to process approval."
29. Verifikasi dialog tetap terbuka
30. Verifikasi radio Approve dan Approval Note `Setuju` dipertahankan
31. Verifikasi `[Submit]` aktif lagi
32. Lepas intercept respons Submit
33. Klik `[Cancel]`

### TC-AC-ACTS-810: Approve atau Reject tanpa respons (timeout jaringan), toast T-24 dan pilihan dipertahankan

34. Klik `Review` pada Subject pending
35. Pilih Approve dan isi Approval Note `Setuju`
36. Tahan respons request Submit sampai timeout (tanpa respons)
37. Klik `[Submit]`
38. Verifikasi toast "Connection problem. Please try again."
39. Verifikasi toast "Error, failed to process approval." tidak tampil
40. Verifikasi dialog tetap terbuka
41. Verifikasi radio Approve dan Approval Note `Setuju` dipertahankan
42. Verifikasi `[Submit]` aktif lagi
43. Lepas tahanan respons request Submit
44. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Spec ini satu spec resilience (kelas b) untuk Approvals; semua kegagalan dipaksa lewat intercept di atas backend nyata. Spec ini melewati sekitar 35 langkah (44 langkah); alasan: semua blok satu kelas harness (kelas b ringan) dan satu halaman, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-AC-ACTS-295, TC-AC-ACTS-730, dan TC-AC-ACTS-776 (kegagalan baca dan unduh) sebelum TC-AC-ACTS-293 dan TC-AC-ACTS-810 (kegagalan Submit) supaya urutan intercept bersih (S-10).
- Langkah penghubung tanpa Verifikasi (S-03): `[Cancel]` atau `[Close]` menutup dialog, serta melepas intercept (S-09). Absence toast sukses Download pada TC-AC-ACTS-776 didahului toast error sebagai anchor positif (8b butir 2). Absence toast "Error, failed to process approval." pada TC-AC-ACTS-810 didahului toast "Connection problem. Please try again." sebagai anchor positif (8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-776 menyebut nama sub-menu `TAG-Stock` untuk Tab Active dan Tab History; spec mengasersi toast yang sama pada keduanya.
  - TC-AC-ACTS-293 menyebut "isi note" tanpa nilai; spec memakai `Setuju` (nilai TC-AC-ACTS-810).
