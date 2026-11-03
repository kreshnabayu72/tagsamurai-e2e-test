---
id: TC-FA-LIC-E2E-019-banner-renewal-stage-notice-reminder-final-satu-hari
title: "Banner Renewal: Stage Notice, Reminder, dan Final Satu Hari"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-72
  - TC-FA-LIC-73
  - TC-FA-LIC-74
  - TC-FA-LIC-75
coverage:
  web: automated
---

# Banner Renewal: Stage Notice, Reminder, dan Final Satu Hari

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Konfigurasi Client Lifecycle (hari pengingat final) diubah menjadi 3 untuk TC-FA-LIC-75 lewat fixture BE dan dipulihkan ke 1 di hook `after`.
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-72: Banner stage Notice: Default, closable, copy S-FALIC-08

1. Atur tanggal fixture hari ini ke `01/12/26` (N = 30) lewat fixture BE
2. Buka License > All License
3. Verifikasi satu banner full width tampil di atas Tabs Bar
4. Verifikasi banner severity Default (info)
5. Verifikasi Title banner `Subscription expires in 30 days`
6. Verifikasi Body banner `Contact PT Maju Bersama to renew and keep your license and assets uninterrupted.`
7. Verifikasi tombol `[×]` tampil pada banner (closable)
8. Verifikasi banner beratribut `role="status"`
9. Klik Tab `Allocation Quota`
10. Verifikasi banner yang sama tampil di Tab Allocation Quota
11. Klik Tab `Concurrent User`
12. Verifikasi banner yang sama tampil di Tab Concurrent User
13. Verifikasi banner tidak memuat tombol aksi Renew

### TC-FA-LIC-73: Banner stage Reminder: Warning, closable, copy S-FALIC-09

14. Atur tanggal fixture hari ini ke `24/12/26` (N = 7) lewat fixture BE
15. Buka License > All License
16. Verifikasi banner severity Warning
17. Verifikasi Title banner `Subscription expires in 7 days`
18. Verifikasi Body banner `Renew soon to avoid read-only access. Contact PT Maju Bersama.`
19. Verifikasi tombol `[×]` tampil pada banner
20. Verifikasi banner beratribut `role="status"`
21. Klik Tab `Allocation Quota` lalu Tab `Concurrent User`

### TC-FA-LIC-74: Banner stage Final satu hari: Danger, tidak closable, Subscription expires tomorrow

22. Atur tanggal fixture hari ini ke `30/12/26` (N = 1) lewat fixture BE
23. Buka License > All License
24. Verifikasi banner severity Danger
25. Verifikasi Title banner `Subscription expires tomorrow`
26. Verifikasi Body banner `After expiry your account becomes read-only. Contact PT Maju Bersama to renew now.`
27. Verifikasi tidak ada tombol `[×]` pada banner
28. Verifikasi banner beratribut `role="alert"`
29. Klik Tab `Allocation Quota` lalu Tab `Concurrent User`

### TC-FA-LIC-75: Banner stage Final lebih dari satu hari memakai bentuk jamak

30. Ubah hari pengingat final Client Lifecycle menjadi `3` lewat fixture BE
31. Atur tanggal fixture hari ini ke `28/12/26` (N = 3) lewat fixture BE
32. Buka License > All License
33. Verifikasi banner severity Danger
34. Verifikasi Title banner `Subscription expires in 3 days`
35. Verifikasi tidak ada tombol `[×]` pada banner
36. Klik Tab `Allocation Quota` lalu Tab `Concurrent User`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): langkah "Atur tanggal fixture hari ini" dan "Ubah hari pengingat final" menyetel precondition TC; langkah "Klik Tab `Allocation Quota` lalu Tab `Concurrent User`" pada TC-FA-LIC-73, 74, 75 mengikuti langkah TC.
- Banner dibuka dengan tanggal fixture BE, bukan dengan menggeser jam server (jam server tidak digeser).
- Spec di atas 35 langkah (36 langkah): keempat blok adalah stage satu komponen banner pada halaman yang sama, setiap blok menyetel tanggal fixturenya sendiri dan berdiri sendiri, sehingga kegagalan satu stage tidak membuat stage lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-73, 74, dan 75 memuat langkah 3 (klik Tab `Allocation Quota` lalu Tab `Concurrent User`) tanpa Expected yang mengasersi banner di kedua tab; spec hanya menjalankannya. Banner di kedua tab diasersi di TC-FA-LIC-72.
  - TC-FA-LIC-75 tidak memuat Body banner pada Expected bentuk jamak; Body tidak diasersi.
