---
id: TC-AC-LCS-E2E-156-email-engine-job-terlambat-dan-tahapan-dilewati
title: "Email Trigger Engine: Job Terlambat, Konfigurasi Berubah, Tahapan Sebelum Pembuatan Subscription, dan Eksekusi Terlewat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-547
  - TC-AC-LCS-548
  - TC-AC-LCS-549
  - TC-AC-LCS-550
  - TC-AC-LCS-678
coverage:
  web: automated
---

# Email Trigger Engine: Job Terlambat, Konfigurasi Berubah, Tahapan Sebelum Pembuatan Subscription, dan Eksekusi Terlewat

## Prerequisites

- Mode: FE+BE. Kelas harness d (harness eksternal: job lifecycle, jam, dan mail-catcher sebagai objek uji).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: Client PT Maju Jaya (Direct, pengguna Total Control aktif pada produk terdampak, subscription Paid) dan Client lain sesuai Pre-setup 10; subscription dan rantai kepemilikan diatur per TC lewat Fixture BE dan dipulihkan di hook `after` suite. TC 549 memakai Client PT Sentosa Abadi dengan Subscription Free baru.
- Akun Partner, Distributor, dan Principal berizin "Manage allocation" atau "Manage archived client" (Pre-setup 11) tertulis di Pre-setup 15 sebagai usulan pola Pre-setup 6 (keberadaan akun perlu dikonfirmasi tim FE): `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageArchivedClientPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`, `manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`; env password akun-akun itu belum terdaftar, jadi disediakan tim FE. Email pengguna Total Control produk terdampak tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal data uji subscription, mengatur jam server dan jam browser, memicu eksekusi job lifecycle dan job Email Trigger Engine, serta membaca log job; mail-catcher atau inbox riil dengan baseline jumlah email per alamat sebelum aksi (S-12).
- Data konfigurasi: TC 548 mengubah tab Client Lifecycle lewat UI (First Reminder Before Event `30` menjadi `60`); TC 549 mengatur Free Plan Duration `1` dan Final Reminder Before Event `1` lewat Fixture BE (dipakai sebagai precondition TC, tidak diasersi).
- State global: jam server dan jam browser digeser, subscription uji PT Maju Jaya, antrean job, dan konfigurasi tab diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-547: Job terlambat, hanya Second Reminder dikirim dan First Reminder ditandai dilewati

1. Atur lewat Fixture BE: Subscription Paid PT Maju Jaya berakhir 3 hari lagi; First Reminder dan Second Reminder belum terkirim; catat baseline jumlah email inbox pengguna Total Control produk terdampak PT Maju Jaya (mail-catcher)
2. Picu eksekusi job Email Trigger Engine lewat Fixture BE
3. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya menerima tepat satu email Second Reminder (selisih jumlah email terhadap baseline 1)
4. Verifikasi log job (Fixture BE) mencatat First Reminder ditandai dilewati
5. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya tidak menerima email First Reminder
6. Verifikasi Final Reminder belum terkirim: inbox pengguna Total Control produk terdampak PT Maju Jaya tidak menerima email Final Reminder (tanggalnya belum tercapai)

### TC-AC-LCS-548: Konfigurasi diubah sehingga tanggal tahapan sudah lewat, tahapan terbaru dikirim pada eksekusi berikutnya

7. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, atur Subscription Paid PT Maju Jaya berakhir 40 hari lagi (First Reminder `30` belum tercapai), dan catat baseline jumlah email inbox pengguna Total Control produk terdampak PT Maju Jaya
8. Klik tab Client Lifecycle
9. Ubah First Reminder Before Event dari `30` menjadi `60` lalu klik `[Save]`
10. Tunggu aksi `[Save]` selesai (tombol `[Save]` tidak lagi dalam state loading)
11. Picu eksekusi job Email Trigger Engine lewat Fixture BE
12. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya menerima tepat satu email First Reminder (batas 60 hari sudah tercapai; selisih jumlah email terhadap baseline 1)

### TC-AC-LCS-549: Tahapan dengan tanggal sebelum waktu pembuatan subscription ditandai dilewati tanpa email

13. Atur lewat Fixture BE: ketujuh tab pada nilai default kecuali Free Plan Duration `1` dan Final Reminder Before Event `1`; buat Subscription Free baru PT Sentosa Abadi dengan masa aktif 1 hari; catat baseline jumlah email inbox pengguna Total Control produk terdampak PT Sentosa Abadi
14. Picu eksekusi job Email Trigger Engine lewat Fixture BE
15. Verifikasi inbox pengguna Total Control produk terdampak PT Sentosa Abadi tidak menerima email First Reminder, Second Reminder, maupun Final Reminder (seluruh tanggal tahapan sama dengan atau sebelum waktu pembuatan; selisih jumlah email terhadap baseline 0)

### TC-AC-LCS-550: Grace Period End dan Purge Confirmation dikirim bila tercapai walau job terlambat

16. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, atur Subscription PT Maju Jaya melewati akhir masa tenggang 5 hari lalu dengan Grace Period End belum ditandai, dan catat baseline jumlah email inbox pengguna Total Control produk terdampak PT Maju Jaya
17. Picu eksekusi job Email Trigger Engine lewat Fixture BE
18. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya menerima tepat satu email Grace Period End (peristiwa tunggal dikirim bila tercapai dan belum ditandai; selisih jumlah email terhadap baseline 1)

### TC-AC-LCS-678: Satu eksekusi job lifecycle terlewat, eksekusi berikutnya memproses status terkini satu fase tanpa transisi ganda

19. Atur lewat Fixture BE: Subscription Paid PT Maju Jaya berstatus `Grace` dan batas Grace Period Duration (`30` hari) terlewati sejak satu hari lalu; satu eksekusi job lifecycle harian dilewati
20. Picu eksekusi job lifecycle lewat Fixture BE
21. Buka Allocation > Client Subscription > List Subscriptions
22. Ketik Search `PT Maju Jaya`, tekan Enter
23. Verifikasi status subscription PT Maju Jaya `Archive` (satu fase dari `Grace`)
24. Picu eksekusi job lifecycle sekali lagi pada hari yang sama lewat Fixture BE
25. Muat ulang daftar List Subscriptions
26. Ketik Search `PT Maju Jaya`, tekan Enter
27. Verifikasi status subscription PT Maju Jaya tetap `Archive` (tidak ada transisi ganda)

## Notes

- Urutan TC mengikuti urutan nomor kolom `sourceTc` (547, 548, 549, 550, lalu 678).
- Asersi "tidak menerima email" memakai baseline jumlah email per alamat dan didahului `Verifikasi` email atau log yang seharusnya ada pada surface yang sama (anchor, bagian 8b butir 2); TC 547 memakai email Second Reminder sebagai anchor.
- Pembuatan data uji dan pemicu job (Fixture BE) ditulis sebagai langkah penghubung karena TC menyebutnya sebagai precondition dan pemicu tanpa Expected.
- Temuan untuk QA:
  - Email pengguna Total Control produk terdampak PT Maju Jaya dan PT Sentosa Abadi tidak tertulis di Pre-setup TC; Pre-setup 12 hanya menyebut mail catcher atau inbox riil.
  - TC 547 Expected b menyebut First Reminder "ditandai dilewati" tanpa menyebut surface pengamatan; spec membaca log job lewat Fixture BE (TC 544 dan 545 menyebut log job lewat Fixture BE).
  - TC 678 langkah 1 dan 2 menyebut "amati status subscription" tanpa menyebut layar; spec memakai Allocation > Client Subscription > List Subscriptions seperti TC 552.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 7-8, 10-11, 13-14, 16-17, 19-22, 24-26; langkah 22 dan 26 (`Ketik Search `PT Maju Jaya`, tekan Enter`) mendahului `Verifikasi` status baris List Subscriptions (R-16, bagian 8b butir 13, R-23).
