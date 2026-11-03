---
id: TC-FA-LIC-E2E-020-banner-renewal-stage-expired-grace-dan-banner-tidak-dapat-ditutup
title: "Banner Renewal: Stage Expired (Grace) dan Banner Tidak Dapat Ditutup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-76
  - TC-FA-LIC-77
  - TC-FA-LIC-78
  - TC-FA-LIC-471
  - TC-FA-LIC-481
  - TC-FA-LIC-617
coverage:
  web: automated
---

# Banner Renewal: Stage Expired (Grace) dan Banner Tidak Dapat Ditutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Status term live Grace atau Expired diatur lewat fixture BE per blok; Grace End term live untuk TC-FA-LIC-617 diubah menjadi 20/01/27 lalu 25/01/27 lewat fixture BE (Lifecycle Settings tidak memuat durasi Grace).
- Jam browser (klien) dikendalikan lewat fake timer untuk melewati jeda muat ulang banner 60 detik (disediakan tim FE); jam server tidak digeser.
- TC-FA-LIC-471: sesi produk akun aktor dibuka sebelum term menjadi Expired (hook `before`), seat existing grandfathered.
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-76: Banner stage Expired status Grace: sisa hari Grace

1. Atur tanggal fixture hari ini ke `10/01/27` dan status term live `Grace` (Grace End 30/01/27) lewat fixture BE
2. Buka License > All License
3. Verifikasi banner severity Danger
4. Verifikasi Title banner `Subscription expired`
5. Verifikasi Body banner `Your account is read-only. Renew within 20 days to restore full access. Contact PT Maju Bersama.`
6. Verifikasi tidak ada tombol `[×]` pada banner
7. Verifikasi banner beratribut `role="alert"`
8. Klik Tab `Allocation Quota` lalu Tab `Concurrent User`

### TC-FA-LIC-77: Banner stage Expired sisa satu hari memakai bentuk tunggal

9. Atur tanggal fixture hari ini ke `29/01/27` dan status term live `Grace` (Grace End 30/01/27) lewat fixture BE
10. Buka License > All License
11. Verifikasi Body banner `Your account is read-only. Renew within 1 day to restore full access. Contact PT Maju Bersama.`
12. Klik Tab `Allocation Quota` lalu Tab `Concurrent User`

### TC-FA-LIC-78: Banner stage Expired pada hari Grace End memakai cabang satu hari

13. Atur tanggal fixture hari ini ke `30/01/27` dan status term live `Grace` (Grace End 30/01/27) lewat fixture BE
14. Buka License > All License
15. Verifikasi Body banner `Your account is read-only. Renew within 1 day to restore full access. Contact PT Maju Bersama.` (nilai sisa 0 hari memakai cabang satu hari)
16. Klik Tab `Allocation Quota` lalu Tab `Concurrent User`

### TC-FA-LIC-471: Banner status Expired sehari setelah End Date

17. Atur tanggal fixture hari ini ke `01/01/27` dan status term live `Expired` (Grace End 30/01/27) lewat fixture BE
18. Buka License > All License
19. Verifikasi banner stage Expired dengan Body `Your account is read-only. Renew within 29 days to restore full access. Contact PT Maju Bersama.`
20. Klik Tab `Allocation Quota` lalu Tab `Concurrent User`

### TC-FA-LIC-481: Stage Final dan Expired tidak dapat ditutup

21. Atur tanggal fixture hari ini ke `30/12/26` (stage Final) lewat fixture BE
22. Buka License > All License
23. Verifikasi tidak ada tombol `[×]` pada banner stage Final
24. Tekan `Esc`
25. Verifikasi banner stage Final tetap tampil (`Esc` tidak menutup banner)
26. Atur tanggal fixture hari ini ke `10/01/27` dan status term live `Grace` (Grace End 30/01/27) lewat fixture BE (stage Expired)
27. Buka License > All License
28. Verifikasi tidak ada tombol `[×]` pada banner stage Expired
29. Tekan `Esc`
30. Verifikasi banner stage Expired tetap tampil (`Esc` tidak menutup banner)

### TC-FA-LIC-617: Banner Expired: sisa hari Grace dihitung dari field Grace End pada data Subscription term live

31. Atur tanggal fixture hari ini ke `10/01/27`, status term live `Grace`, dan field Grace End term live `20/01/27` lewat fixture BE
32. Buka License > All License
33. Verifikasi Body banner `Your account is read-only. Renew within 10 days to restore full access. Contact PT Maju Bersama.` (Grace End 20/01/27 − 10/01/27 = 10 hari)
34. Ubah field Grace End term live menjadi `25/01/27` lewat fixture BE
35. Majukan jam browser 61 detik lewat fake timer
36. Klik Tab `Allocation Quota`
37. Verifikasi Body banner `Your account is read-only. Renew within 15 days to restore full access. Contact PT Maju Bersama.` (Grace End 25/01/27 − 10/01/27 = 15 hari)

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): penyetelan tanggal fixture, status term, dan Grace End; "Majukan jam browser 61 detik" (TC menulis "setelah lebih dari 60 detik", dipenuhi dengan fake timer, bukan menunggu); "Klik Tab `Allocation Quota`" pada langkah 33 memindahkan Tab setelah jeda 60 detik sehingga banner dimuat ulang tanpa reload manual.
- TC-FA-LIC-481: TC menyebut tanggal Final 30/12/26 dan Expired 10/01/27; status term untuk tanggal kedua mengikuti TC-FA-LIC-76 (Grace, Grace End 30/01/27).
- Spec di atas 35 langkah (37 langkah): seluruh blok adalah stage banner yang sama pada halaman yang sama, setiap blok menyetel tanggal dan status term sendiri dan berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-LIC-76 sampai 78 dan 471 memuat langkah 3 (klik Tab `Allocation Quota` lalu Tab `Concurrent User`) tanpa Expected untuk banner di kedua tab; spec hanya menjalankannya.
  - TC-FA-LIC-481 Expected tidak menyebut Title/Body; hanya ketiadaan `[×]` dan perilaku `Esc` yang diasersi.
