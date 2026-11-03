---
id: TC-FA-LIC-E2E-025-sinkron-konfigurasi-banner-terhadap-renewal-di-admin
title: "Sinkron Konfigurasi Banner terhadap Renewal di Admin Console, Lifecycle Settings, dan T-0"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-417
  - TC-FA-LIC-418
  - TC-FA-LIC-419
  - TC-FA-LIC-611
coverage:
  web: automated
---

# Sinkron Konfigurasi Banner terhadap Renewal di Admin Console, Lifecycle Settings, dan T-0

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): Used 4.320, Reserved 15, Remaining 665, Unmanaged 27; fixture modul aset untuk TC-FA-LIC-611: lima aset Active menjadi Unmanaged pada T-0 (aset terdampak ditentukan `plans.md` §5 dan `plans-licensing-config.md` §1); disediakan tim FE/BE.
- Persetujuan Renewal di Admin Console dan perubahan hari pengingat pertama di Lifecycle Settings dilakukan pelaku kedua lewat sesi API (akun pelaku disediakan tim FE); successor Renewal `Pending` dengan plan rank lebih rendah untuk TC-FA-LIC-418 diatur lewat fixture BE.
- Jam browser (klien) dikendalikan lewat fake timer (disediakan tim FE) untuk memenuhi jeda 60 detik dan jeda idle; jam server tidak digeser.
- Hari pengingat pertama Client Lifecycle diubah menjadi 14 di TC-FA-LIC-419 dan dipulihkan ke 30; tanggal fixture hari ini dan status term dipulihkan ke bawaan Pre-setup di hook `after`.
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-417: Banner Expiry hilang saat Renewal disetujui di Admin Console dan halaman License terbuka

1. Atur tanggal fixture hari ini ke `01/12/26` (N = 30); status term Active lewat fixture BE
2. Buka License > All License
3. Setujui Renewal di Admin Console lewat sesi API hingga successor `Pending` tersimpan
4. Majukan jam browser 61 detik lewat fake timer
5. Klik Tab `Allocation Quota`
6. Verifikasi Tabs Bar tampil
7. Verifikasi banner hilang pada muat ulang otomatis berikutnya tanpa reload manual

### TC-FA-LIC-418: Renewal ke plan ber-rank lebih rendah: banner Expiry tidak dirender dan peringatan Downgrade hanya di Dashboard

8. Atur tanggal fixture hari ini ke `01/12/26` (N = 30) lewat fixture BE
9. Atur successor Renewal `Pending` dengan plan rank lebih rendah lewat fixture BE
10. Buka License > All License
11. Verifikasi Tabs Bar tampil
12. Verifikasi halaman License tidak menampilkan banner Expiry maupun peringatan Downgrade
13. Buka Dashboard
14. Verifikasi peringatan Downgrade tampil di Dashboard

### TC-FA-LIC-419: Perubahan config Client Lifecycle berlaku pada muat berikutnya

15. Atur tanggal fixture hari ini ke `10/12/26` (N = 21); status term Active, konfigurasi Client Lifecycle 30/7/1; successor Renewal dihapus lewat fixture BE
16. Buka License > All License
17. Verifikasi banner Notice dengan Title `Subscription expires in 21 days`
18. Ubah hari pengingat pertama menjadi `14` di Lifecycle Settings lewat sesi API hingga perubahan tersimpan
19. Muat ulang halaman License
20. Verifikasi Tabs Bar tampil
21. Verifikasi tidak ada banner (N = 21 > 14)
22. Pulihkan hari pengingat pertama menjadi `30` lewat fixture BE

### TC-FA-LIC-611: T-0: term live berakhir tanpa Renewal dan menjadi Expired: License Summary dan banner Expired konsisten tanpa jeda

23. Pulihkan tanggal fixture hari ini dan status term live ke bawaan Pre-setup (term Active, tanpa Renewal) lewat fixture BE
24. Buka License > All License
25. Verifikasi License Summary: Used 4320, Reserved 15, Remaining 665, Unmanaged 27
26. Klik Sub-Tab `Subscription History`
27. Verifikasi Status term live `Active`
28. Geser jam fixture ke T-0 (tanggal fixture hari ini `01/01/27`): term berakhir tanpa Renewal, status menjadi `Expired`, dan lima aset Active menjadi Unmanaged lewat fixture modul aset
29. Buka License > All License
30. Verifikasi License Summary pada muat ulang pertama tanpa jeda: Used 4315, Reserved 15, Remaining 670, Unmanaged 32
31. Klik Sub-Tab `Subscription History`
32. Verifikasi Status term live `Expired`
33. Verifikasi Title banner stage Expired `Subscription expired`
34. Verifikasi Body banner `Your account is read-only. Renew within 29 days to restore full access. Contact PT Maju Bersama.`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): penyetelan tanggal fixture dan successor, "Majukan jam browser 61 detik" (TC menulis "lebih dari 60 detik", dipenuhi dengan fake timer), "Buka Dashboard", "Pulihkan hari pengingat pertama", dan "Pulihkan tanggal fixture hari ini ..." sebelum TC-FA-LIC-611.
- Pelaku kedua (Admin Console, Lifecycle Settings) memakai sesi API, sehingga `P-2` tidak dipakai.
- Spec mencapai 34 langkah dengan empat blok: perubahan konfigurasi atau status sisi Admin yang mengubah banner, dan setiap blok menyetel state sendiri serta berdiri sendiri.
- Asersi "banner hilang" atau "tidak dirender" didahului `Verifikasi Tabs Bar tampil` sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-LIC-417 tidak menyebut akun yang menyetujui Renewal di Admin Console; akun pelaku disediakan tim FE.
  - TC-FA-LIC-418 menyebut pengujian rinci peringatan Downgrade disitir ke TC `wizard-reconciliation`; spec hanya mengasersi peringatan tampil di Dashboard.
  - TC-FA-LIC-419 tidak menyebut tempat penyimpanan hari pengingat selain "Lifecycle Settings"; perubahan dilakukan lewat sesi API aktor kedua.
  - TC-FA-LIC-611 tidak menyebut tanggal fixture "awal" sebelum T-0; spec memulihkan kondisi bawaan Pre-setup. Kontrak ledger `Used` diacu PRD License §12 Open Item #4.
