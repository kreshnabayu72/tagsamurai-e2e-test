---
id: TC-FA-LIC-E2E-023-banner-renewal-dismiss-penyimpanan-state-dismiss
title: "Banner Renewal: Dismiss dan Penyimpanan State Dismiss"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-477
  - TC-FA-LIC-478
  - TC-FA-LIC-480
  - TC-FA-LIC-525
coverage:
  web: automated
---

# Banner Renewal: Dismiss dan Penyimpanan State Dismiss

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Rantai Renewal untuk TC-FA-LIC-525 (Pre-setup #25): term pengganti Start 01/01/27, End 31/12/27; term lama menjadi `Renewed` dan term pengganti `Active` diatur lewat fixture BE (disediakan tim FE/BE).
- Jumlah panggilan ke endpoint banner dapat dihitung lewat `Spectra.intercept()` (Pre-setup #15).
- Jam browser (klien) dikendalikan lewat fake timer (disediakan tim FE) untuk memenuhi jeda 60 detik dan jeda idle; jam server tidak digeser.
- TC-FA-LIC-480: kemampuan memblokir penyimpanan browser (mode privat atau storage dimatikan) disediakan tim FE; dipulihkan di hook `after`.
- State dismiss banner tersimpan per sesi login; sesi login aktor dibuat di hook `before`, sehingga state dismiss spec lain tidak terbawa.
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-477: Tidak ada polling terjadwal untuk banner

1. Atur tanggal fixture hari ini ke `01/12/26` lewat fixture BE
2. Pasang penghitung panggilan endpoint banner lewat intercept
3. Buka License > All License
4. Catat jumlah panggilan endpoint banner
5. Majukan jam browser 5 menit tanpa interaksi lewat fake timer
6. Verifikasi jumlah panggilan endpoint banner tidak bertambah dari yang dicatat selama idle

### TC-FA-LIC-478: Dismiss: tutup Notice bertahan setelah muat ulang otomatis; muncul lagi saat stage berubah

7. Atur tanggal fixture hari ini ke `01/12/26`; stage Notice lewat fixture BE
8. Buka License > All License
9. Klik `[×]` pada banner Notice
10. Verifikasi Tabs Bar tampil
11. Verifikasi banner hilang
12. Majukan jam browser 61 detik lewat fake timer
13. Klik Tab `Allocation Quota` (muat ulang otomatis)
14. Verifikasi Tabs Bar tampil
15. Verifikasi stage tetap Notice: banner tetap tertutup
16. Atur tanggal fixture hari ini ke `24/12/26`; stage Reminder lewat fixture BE
17. Majukan jam browser 61 detik lewat fake timer
18. Klik Tab `Concurrent User` (muat ulang otomatis)
19. Verifikasi banner stage Reminder muncul lagi

### TC-FA-LIC-525: Dismiss banner: term pengganti dengan stage sama memunculkan banner lagi pada sesi login yang sama

20. Atur tanggal fixture hari ini ke `01/12/26` (N = 30) lewat fixture BE
21. Buka License > All License
22. Klik `[×]` pada banner Notice
23. Verifikasi Tabs Bar tampil
24. Verifikasi banner Notice hilang
25. Atur tanggal fixture hari ini ke `01/12/27`, term lama `Renewed`, dan term pengganti `Active` (End Date 31/12/27, N = 30) lewat fixture BE
26. Majukan jam browser 61 detik lewat fake timer
27. Klik Tab `Concurrent User`
28. Klik Tab `All License` tanpa logout
29. Verifikasi banner Notice `Subscription expires in 30 days` tampil lagi untuk term pengganti walau Notice term sebelumnya sudah ditutup pada sesi login yang sama

### TC-FA-LIC-480: Dismiss: bila state tidak dapat disimpan banner tetap tampil tiap muat

30. Blokir penyimpanan browser (mode privat atau storage dimatikan)
31. Atur tanggal fixture hari ini ke `01/12/26`; stage Notice lewat fixture BE
32. Buka License > All License
33. Klik `[×]` pada banner Notice
34. Muat ulang halaman License
35. Verifikasi banner Notice tampil lagi

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): penyetelan tanggal fixture, pemasangan intercept, "Catat jumlah panggilan", "Majukan jam browser" (TC menulis "setelah lebih dari 60 detik" dan "5 menit", dipenuhi dengan fake timer, bukan menunggu), "Klik Tab ..." yang memicu muat ulang otomatis, dan pemblokiran penyimpanan.
- Urutan blok: TC-FA-LIC-480 terakhir karena memblokir penyimpanan browser; hook `after` memulihkannya.
- Asersi "banner hilang" atau "tetap tertutup" didahului `Verifikasi Tabs Bar tampil` sebagai anchor positif.
- Spec mencapai 35 langkah: keempat blok adalah perilaku dismiss banner yang sama pada halaman yang sama, dan setiap blok menyetel tanggal fixture sendiri serta berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-LIC-480 tidak menyatakan dampak pemblokiran penyimpanan terhadap sesi login yang sudah berjalan; kemampuan pemblokirannya disediakan tim FE.
  - TC-FA-LIC-477 tidak menyebut jumlah panggilan awal; asersi memakai selisih terhadap jumlah yang dicatat sesudah halaman dibuka.
