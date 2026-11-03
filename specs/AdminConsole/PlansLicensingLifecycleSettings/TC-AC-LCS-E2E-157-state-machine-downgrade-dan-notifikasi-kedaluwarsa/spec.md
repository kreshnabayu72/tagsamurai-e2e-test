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
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal data uji subscription, mengatur jam server dan jam browser, memicu eksekusi job lifecycle dan job Email Trigger Engine, serta membaca log job; mail-catcher atau inbox riil dengan baseline jumlah email per alamat sebelum aksi (S-12). Penetapan Downgrade berada di luar modul ini dan dilakukan lewat Fixture BE.
- State global: jam server dan jam browser digeser, subscription uji PT Maju Jaya, antrean job, dan konfigurasi tab diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-551: Scheduled Downgrade, pengingat dihitung dari tanggal efektif downgrade yang ditetapkan Principal

1. Atur lewat Fixture BE: Downgrade subscription PT Maju Jaya ditetapkan Principal dengan tanggal efektif 30 hari lagi (Subscription Active); catat baseline jumlah email inbox pengguna Total Control produk terdampak PT Maju Jaya
2. Picu eksekusi job Email Trigger Engine lewat Fixture BE
3. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya menerima tepat satu email First Reminder (30 hari sebelum tanggal efektif downgrade; selisih jumlah email terhadap baseline 1)
4. Buka Allocation > Client Subscription > List Subscriptions
5. Verifikasi status subscription PT Maju Jaya tetap `Active`

### TC-AC-LCS-552: Transisi Active ke Expired pada T-0 mengirim notifikasi kedaluwarsa dalam aplikasi ke penerima rantai kepemilikan

6. Atur lewat Fixture BE: Client PT Maju Jaya di bawah Partner PT Mitra Satu dan Distributor PT Distribusi Utama dengan pengguna berizin Manage allocation di setiap level; Subscription Paid PT Maju Jaya mencapai tanggal berakhir; catat baseline jumlah notifikasi kedaluwarsa per pengguna berizin
7. Picu eksekusi job lifecycle lewat Fixture BE
8. Muat ulang daftar List Subscriptions
9. Verifikasi status subscription PT Maju Jaya `Expired`
10. Ganti akun ke pengguna Partner berizin Manage allocation lalu buka Overlay Notifikasi
11. Verifikasi pengguna Partner menerima tepat satu notifikasi dalam aplikasi langganan kedaluwarsa (selisih terhadap baseline 1)
12. Ganti akun ke pengguna Distributor berizin Manage allocation lalu buka Overlay Notifikasi
13. Verifikasi pengguna Distributor menerima tepat satu notifikasi dalam aplikasi langganan kedaluwarsa (selisih terhadap baseline 1)
14. Ganti akun ke pengguna Principal berizin Manage allocation lalu buka Overlay Notifikasi
15. Verifikasi pengguna Principal berizin menerima tepat satu notifikasi dalam aplikasi langganan kedaluwarsa (selisih terhadap baseline 1)

### TC-AC-LCS-553: Eksekusi job ulang tidak mengirim notifikasi kedaluwarsa kedua

16. Atur lewat Fixture BE: Subscription PT Maju Jaya sudah `Expired` dan notifikasi kedaluwarsa sudah terkirim (rantai kepemilikan dan pengguna berizin sama dengan TC 552)
17. Picu eksekusi job lifecycle sekali lagi lewat Fixture BE
18. Muat ulang Overlay Notifikasi pada sesi pengguna Principal berizin
19. Verifikasi jumlah notifikasi kedaluwarsa untuk subscription PT Maju Jaya tetap satu

### TC-AC-LCS-554: Downgrade pada T-0 tidak memicu notifikasi kedaluwarsa dan status tetap Active

20. Atur lewat Fixture BE: Downgrade subscription PT Maju Jaya ke plan lain mencapai tanggal efektif; catat baseline jumlah notifikasi kedaluwarsa pengguna Principal berizin
21. Picu eksekusi job lifecycle lewat Fixture BE
22. Ganti akun ke Total Control lalu buka Allocation > Client Subscription > List Subscriptions
23. Verifikasi status subscription PT Maju Jaya tetap `Active` dengan plan baru
24. Ganti akun ke pengguna Principal berizin Manage allocation lalu buka Overlay Notifikasi
25. Verifikasi tidak ada notifikasi kedaluwarsa langganan untuk subscription PT Maju Jaya (selisih terhadap baseline 0)

### TC-AC-LCS-555: Notifikasi kedaluwarsa dengan daftar penerima kosong ditandai tanpa penerima tanpa retry

26. Atur lewat Fixture BE: tidak ada pengguna berizin Manage allocation di seluruh level rantai kepemilikan client; Subscription Paid PT Maju Jaya mencapai tanggal berakhir
27. Picu eksekusi job lifecycle lewat Fixture BE
28. Picu eksekusi job lifecycle sekali lagi lewat Fixture BE
29. Ganti akun ke Total Control lalu buka Allocation > Client Subscription > List Subscriptions
30. Verifikasi status subscription PT Maju Jaya `Expired`
31. Verifikasi tidak ada notifikasi terkirim (jumlah notifikasi pada log notifikasi Fixture BE tidak bertambah)
32. Verifikasi log job (Fixture BE) mencatat notifikasi Expired ditandai tanpa penerima sekali dan tanpa retry

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness h.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Sesi akun Principal berizin dari TC 552 dipakai ulang oleh TC 553; TC 554 dan 555 mengganti akun ke Total Control untuk mengamati status di List Subscriptions, sesuai langkah TC.
- Asersi "tidak ada notifikasi" pada TC 554 memakai baseline jumlah notifikasi kedaluwarsa sebelum aksi; anchor positifnya `Verifikasi` status subscription `Active` pada langkah sebelumnya dan Overlay Notifikasi yang dibuka.
- Temuan untuk QA:
  - Akun pengguna Partner, Distributor, dan Principal berizin "Manage allocation" kini tertulis di Pre-setup 15 (usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE); env password tidak terdaftar sehingga disediakan tim FE.
  - TC 553 dan 554 langkah 2 dan 3 tidak menyebut akun pengamat status subscription; spec memakai Total Control untuk status dan Principal berizin untuk Overlay Notifikasi (TC 552 langkah 3).
  - TC 555 Expected b menyebut "Tidak ada notifikasi terkirim" tanpa menyebut surface pengamatan; spec membaca log notifikasi lewat Fixture BE.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 4, 6-8, 10, 12, 14, 16-18, 20-22, 24, 26-29.
