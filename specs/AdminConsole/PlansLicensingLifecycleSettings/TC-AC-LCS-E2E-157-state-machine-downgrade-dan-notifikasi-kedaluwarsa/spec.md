---
id: TC-AC-LCS-E2E-157-state-machine-downgrade-dan-notifikasi-kedaluwarsa
title: "Scheduled Downgrade dan Transisi Active ke Expired pada T-0: Pengingat, Notifikasi Kedaluwarsa, Downgrade, dan Daftar Penerima Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-551
  - TC-AC-LCS-552
  - TC-AC-LCS-553
  - TC-AC-LCS-554
  - TC-AC-LCS-555
coverage:
  web: automated
---

# Scheduled Downgrade dan Transisi Active ke Expired pada T-0: Pengingat, Notifikasi Kedaluwarsa, Downgrade, dan Daftar Penerima Kosong

## Prerequisites

- Mode: FE+BE. Kelas harness h (state tenant: transisi status subscription Active, Expired, dan Downgrade pada T-0).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: Client PT Maju Jaya (Direct, pengguna Total Control aktif pada produk terdampak, subscription Paid) dan Client lain sesuai Pre-setup 10; subscription dan rantai kepemilikan diatur per TC lewat Fixture BE dan dipulihkan di hook `after` suite. Rantai kepemilikan: Partner PT Mitra Satu dan Distributor PT Distribusi Utama; pengguna Partner, Distributor, dan Principal berizin "Manage allocation" (Pre-setup 11).
- Akun Partner, Distributor, dan Principal berizin "Manage allocation" atau "Manage archived client" (Pre-setup 11) tertulis di Pre-setup 15 sebagai usulan pola Pre-setup 6 (keberadaan akun perlu dikonfirmasi tim FE): `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageArchivedClientPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`, `manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`; env password akun-akun itu belum terdaftar, jadi disediakan tim FE. Email pengguna Total Control produk terdampak tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA). Ganti akun ke ketiga pengguna berizin memakai kredensial yang disediakan tim FE.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal data uji subscription, mengatur jam server dan jam browser, memicu eksekusi job lifecycle dan job Email Trigger Engine, serta membaca log job; mail-catcher atau inbox riil dengan baseline jumlah email per alamat sebelum aksi (S-12). Penetapan Downgrade berada di luar modul ini dan dilakukan lewat Fixture BE. Kemampuan membaca jumlah notifikasi kedaluwarsa per penerima (Partner, Distributor, Principal) dan log notifikasi lewat Fixture BE untuk baseline (S-12).
- Jendela amat notifikasi in-app (pilihan spec, bukan nilai TC atau PRD): asersi absence notifikasi Overlay Notifikasi didahului langkah "Tunggu 5 detik tanpa memuat ulang halaman" (bagian 8b butir 11, bagian 6) sampai TC menyatakan durasinya.
- State global: jam server dan jam browser digeser, subscription uji PT Maju Jaya, antrean job, dan konfigurasi tab diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-551: Scheduled Downgrade, pengingat dihitung dari tanggal efektif downgrade yang ditetapkan Principal

1. Atur lewat Fixture BE: Downgrade subscription PT Maju Jaya ditetapkan Principal dengan tanggal efektif 30 hari lagi (Subscription Active)
2. Catat baseline jumlah email inbox pengguna Total Control produk terdampak PT Maju Jaya
3. Picu eksekusi job Email Trigger Engine lewat Fixture BE
4. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya menerima tepat satu email First Reminder (30 hari sebelum tanggal efektif downgrade; selisih jumlah email terhadap baseline 1)
5. Buka Allocation > Client Subscription > List Subscriptions
6. Ketik Search `PT Maju Jaya`, tekan Enter
7. Verifikasi status subscription PT Maju Jaya tetap `Active`

### TC-AC-LCS-552: Transisi Active ke Expired pada T-0 mengirim notifikasi kedaluwarsa dalam aplikasi ke penerima rantai kepemilikan

8. Atur lewat Fixture BE: Client PT Maju Jaya di bawah Partner PT Mitra Satu dan Distributor PT Distribusi Utama dengan pengguna berizin Manage allocation di setiap level; Subscription Paid PT Maju Jaya mencapai tanggal berakhir
9. Catat baseline jumlah notifikasi kedaluwarsa per pengguna berizin (Partner, Distributor, Principal)
10. Picu eksekusi job lifecycle lewat Fixture BE
11. Muat ulang daftar List Subscriptions
12. Ketik Search `PT Maju Jaya`, tekan Enter
13. Verifikasi status subscription PT Maju Jaya `Expired`
14. Ganti akun ke pengguna Partner berizin Manage allocation lalu buka Overlay Notifikasi
15. Verifikasi pengguna Partner menerima tepat satu notifikasi dalam aplikasi langganan kedaluwarsa (selisih terhadap baseline 1)
16. Ganti akun ke pengguna Distributor berizin Manage allocation lalu buka Overlay Notifikasi
17. Verifikasi pengguna Distributor menerima tepat satu notifikasi dalam aplikasi langganan kedaluwarsa (selisih terhadap baseline 1)
18. Ganti akun ke pengguna Principal berizin Manage allocation lalu buka Overlay Notifikasi
19. Verifikasi pengguna Principal berizin menerima tepat satu notifikasi dalam aplikasi langganan kedaluwarsa (selisih terhadap baseline 1)

### TC-AC-LCS-553: Eksekusi job ulang tidak mengirim notifikasi kedaluwarsa kedua

20. Atur lewat Fixture BE: Subscription PT Maju Jaya sudah `Expired` dan notifikasi kedaluwarsa sudah terkirim (rantai kepemilikan dan pengguna berizin sama dengan TC 552)
21. Catat baseline jumlah notifikasi kedaluwarsa subscription PT Maju Jaya milik pengguna Principal berizin
22. Picu eksekusi job lifecycle sekali lagi lewat Fixture BE
23. Tunggu 5 detik tanpa memuat ulang halaman
24. Muat ulang Overlay Notifikasi pada sesi pengguna Principal berizin
25. Verifikasi jumlah notifikasi kedaluwarsa untuk subscription PT Maju Jaya milik pengguna Principal berizin tidak bertambah dari baseline (selisih 0, tetap satu)

### TC-AC-LCS-554: Downgrade pada T-0 tidak memicu notifikasi kedaluwarsa dan status tetap Active

26. Atur lewat Fixture BE: Downgrade subscription PT Maju Jaya ke plan lain mencapai tanggal efektif
27. Catat baseline jumlah notifikasi kedaluwarsa pengguna Principal berizin
28. Picu eksekusi job lifecycle lewat Fixture BE
29. Ganti akun ke Total Control lalu buka Allocation > Client Subscription > List Subscriptions
30. Ketik Search `PT Maju Jaya`, tekan Enter
31. Verifikasi status subscription PT Maju Jaya tetap `Active` dengan plan baru
32. Ganti akun ke pengguna Principal berizin Manage allocation lalu buka Overlay Notifikasi
33. Tunggu 5 detik tanpa memuat ulang halaman
34. Verifikasi tidak ada notifikasi kedaluwarsa langganan untuk subscription PT Maju Jaya (selisih terhadap baseline 0)

### TC-AC-LCS-555: Notifikasi kedaluwarsa dengan daftar penerima kosong ditandai tanpa penerima tanpa retry

35. Atur lewat Fixture BE: tidak ada pengguna berizin Manage allocation di seluruh level rantai kepemilikan client; Subscription Paid PT Maju Jaya mencapai tanggal berakhir
36. Catat baseline jumlah notifikasi pada log notifikasi Fixture BE
37. Picu eksekusi job lifecycle lewat Fixture BE
38. Picu eksekusi job lifecycle sekali lagi lewat Fixture BE
39. Ganti akun ke Total Control lalu buka Allocation > Client Subscription > List Subscriptions
40. Ketik Search `PT Maju Jaya`, tekan Enter
41. Verifikasi status subscription PT Maju Jaya `Expired`
42. Verifikasi tidak ada notifikasi terkirim (jumlah notifikasi pada log notifikasi Fixture BE sama dengan baseline, selisih 0)
43. Verifikasi log job (Fixture BE) mencatat notifikasi Expired ditandai tanpa penerima sekali dan tanpa retry

## Notes

- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Sesi akun Principal berizin dari TC 552 dipakai ulang oleh TC 553; TC 554 dan 555 mengganti akun ke Total Control untuk mengamati status di List Subscriptions, sesuai langkah TC.
- Asersi "tidak ada notifikasi" pada TC 554 memakai baseline jumlah notifikasi kedaluwarsa sebelum aksi; anchor positifnya `Verifikasi` status subscription `Active` pada langkah sebelumnya dan Overlay Notifikasi yang dibuka.
- Temuan untuk QA:
  - Akun pengguna Partner, Distributor, dan Principal berizin "Manage allocation" tertulis di Pre-setup 15 (usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE); env password tidak terdaftar sehingga disediakan tim FE.
  - TC 553 dan 554 langkah 2 dan 3 tidak menyebut akun pengamat status subscription; spec memakai Total Control untuk status dan Principal berizin untuk Overlay Notifikasi (TC 552 langkah 3).
  - TC 555 Expected b menyebut "Tidak ada notifikasi terkirim" tanpa menyebut surface pengamatan; spec membaca log notifikasi lewat Fixture BE.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-3, 5-6, 8-12, 14, 16, 18, 20-24, 26-30, 32-33, 35-40. Langkah "Ketik Search `PT Maju Jaya`, tekan Enter" (6, 12, 30, 40) mendahului `Verifikasi` status baris List Subscriptions (R-16, bagian 8b butir 13, R-23). Baseline (langkah 2, 9, 21, 27, 36) dicatat per penerima sebelum pemicu job sebagai langkah terpisah agar `Verifikasi` selisih memakai baseline itu (S-12); baseline langkah 21 menjalankan asersi selisih 0 pada TC 553 sebelum job diulang (langkah 22). Langkah 23 dan 33 "Tunggu 5 detik tanpa memuat ulang halaman" mendahului absence notifikasi in-app pada langkah 25 (TC 553, sesudah pemuatan ulang Overlay Notifikasi langkah 24) dan langkah 34 (TC 554) (bagian 8b butir 11, bagian 6); anchor positif TC 553 adalah state fixture Expired dengan satu notifikasi sudah ada pada baseline langkah 21, dan anchor positif TC 554 adalah `Verifikasi` status `Active` dengan plan baru pada langkah 31.
- Alasan lebih dari sekitar 35 langkah: lima blok (TC 551 sampai 555) satu kelas harness h, tiap blok diseed ulang lewat Fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan blok TC 552 sendiri memuat tiga pergantian akun penerima.
- Temuan untuk QA: TC 553, 554, dan 555 tidak menyebut cara membaca jumlah notifikasi per penerima; spec membacanya lewat Fixture BE atau Overlay Notifikasi sesuai surface langkah.
