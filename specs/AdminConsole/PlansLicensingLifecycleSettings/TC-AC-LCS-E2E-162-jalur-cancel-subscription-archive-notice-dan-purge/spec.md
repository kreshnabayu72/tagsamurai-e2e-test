---
id: TC-AC-LCS-E2E-162-jalur-cancel-subscription-archive-notice-dan-purge
title: "Jalur Cancel Subscription: Archive Notice, Pelacak Purge Warning, dan Email Purge Confirmation ke Penerima Tersimpan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-680
  - TC-AC-LCS-682
  - TC-AC-LCS-683
coverage:
  web: automated
---

# Jalur Cancel Subscription: Archive Notice, Pelacak Purge Warning, dan Email Purge Confirmation ke Penerima Tersimpan

## Prerequisites

- Mode: FE+BE. Kelas harness d (harness eksternal: job lifecycle, jam server, dan mail-catcher sebagai objek uji).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Ganti akun ke pengguna Principal berizin Manage allocation (Pre-setup 11) memakai akun Pre-setup 15 `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net` (usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE), env password disediakan tim FE.
- Data Pre-setup yang dipakai: Client PT Maju Jaya (Direct, pengguna Total Control aktif pada produk terdampak, subscription Paid) dan Client lain sesuai Pre-setup 10; subscription dan rantai kepemilikan diatur per TC lewat Fixture BE dan dipulihkan di hook `after` suite.
- Akun Partner, Distributor, dan Principal berizin "Manage allocation" atau "Manage archived client" (Pre-setup 11) tertulis di Pre-setup 15 sebagai usulan pola Pre-setup 6 (keberadaan akun perlu dikonfirmasi tim FE): `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageArchivedClientPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`, `manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`; env password akun-akun itu belum terdaftar, jadi disediakan tim FE. Email pengguna Total Control produk terdampak tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal data uji subscription, mengatur jam server dan jam browser, memicu eksekusi job lifecycle dan job Email Trigger Engine, serta membaca log job; mail-catcher atau inbox riil dengan baseline jumlah email per alamat sebelum aksi (S-12). Acuan waktu archive T dibaca lewat Fixture BE dan jam server diatur absolut ke T ditambah N hari (bagian 8b butir 3); jam browser diatur bersama jam server.
- State global: jam server dan jam browser digeser, subscription uji PT Maju Jaya, antrean job, dan konfigurasi tab diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-680: Email Purge Confirmation tetap terkirim ke penerima yang disimpan sebelum Hard Purge walau akun penerima dibuang

1. Atur lewat Fixture BE: Subscription PT Maju Jaya jatuh tempo Hard Purge; email pengguna Total Control tercatat sebelum Hard Purge; catat baseline jumlah email pada alamat pengguna Total Control yang tercatat
2. Picu eksekusi job lifecycle hingga Hard Purge dieksekusi lewat Fixture BE
3. Verifikasi data client PT Maju Jaya termasuk akun penerima sudah dibuang (dibaca lewat Fixture BE)
4. Picu eksekusi job Email Trigger Engine lewat Fixture BE
5. Verifikasi inbox email pengguna Total Control yang tercatat sebelum Hard Purge menerima tepat satu email milestone Purge Confirmation (penerima di-resolve dan disimpan sebelum Hard Purge; selisih jumlah email terhadap baseline 1)

### TC-AC-LCS-682: Cancel Subscription memulai pelacak Archive, Archive Notice dikirim satu kali, reminder dan notifikasi kedaluwarsa tidak dikirim

6. Atur lewat Fixture BE: Subscription Paid PT Maju Jaya berstatus `Active` dengan sisa 20 hari; pengguna Principal berizin Manage allocation tersedia; catat baseline jumlah email inbox pengguna Total Control produk terdampak PT Maju Jaya dan baseline jumlah notifikasi Principal berizin
7. Buka Allocation > Client Subscription > List Subscriptions
8. Cancel Subscription PT Maju Jaya
9. Muat ulang daftar List Subscriptions
10. Verifikasi status subscription PT Maju Jaya `Archive` (Grace dilewati)
11. Picu eksekusi job Email Trigger Engine lewat Fixture BE
12. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya menerima tepat satu email milestone Grace Period End (Archive Notice; selisih jumlah email terhadap baseline 1)
13. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya tidak menerima email First Reminder, Second Reminder, maupun Final Reminder
14. Ganti akun ke pengguna Principal berizin Manage allocation lalu buka Overlay Notifikasi
15. Verifikasi Overlay Notifikasi tidak menerima notifikasi Plan Owner maupun notifikasi kedaluwarsa (selisih terhadap baseline 0)
16. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
17. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya tidak menerima email milestone tambahan (penanda pengiriman mencegah pengiriman ulang; selisih jumlah email terhadap baseline tetap 1)

### TC-AC-LCS-683: Pelacak jalur Cancel menghitung Purge Warning dari waktu archive ditambah Archive Period Duration

18. Atur lewat Fixture BE: Subscription PT Maju Jaya di-Cancel pada waktu archive T dengan Archive Period Duration `30` dan Purge Warning Email `10`; catat baseline jumlah email inbox pengguna Total Control produk terdampak PT Maju Jaya
19. Atur jam server dan jam browser ke waktu archive T (dibaca lewat Fixture BE) ditambah 19 hari lalu picu eksekusi job Email Trigger Engine lewat Fixture BE
20. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya tidak menerima email Purge Warning (selisih jumlah email terhadap baseline 0)
21. Atur jam server dan jam browser ke waktu archive T ditambah 20 hari lalu picu eksekusi job Email Trigger Engine lewat Fixture BE
22. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya menerima tepat satu email Purge Warning (tanggal pembersihan dikurangi 10 hari; selisih jumlah email terhadap baseline 1)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness d.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc` (680, 682, 683).
- Pemajuan jam pada TC 683 tidak mempengaruhi asersi lain karena jam dipulihkan oleh hook `beforeEach` suite sebelum spec berikutnya dan tidak ada akses log pada spec ini sesudah jam digeser (S-09).
- Temuan untuk QA:
  - Alamat email pengguna Total Control produk terdampak PT Maju Jaya tidak tertulis di Pre-setup TC; ditulis sebagai disediakan tim FE. Akun Principal berizin kini di Pre-setup 15 (usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE; env password disediakan tim FE).
  - TC 682 Expected b mensyaratkan pengamatan Overlay Notifikasi Principal berizin tanpa menyebut akun; spec memakai pengguna Principal berizin Manage allocation seperti TC 552.
  - TC 683 langkah 1 dan 2 menyebut "Majukan jam sistem hingga 19 hari setelah waktu archive"; spec mengatur jam absolut ke waktu archive T ditambah N hari (bagian 6 konvensi).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 4, 6-7, 9, 11, 14, 16, 18-19, 21.
