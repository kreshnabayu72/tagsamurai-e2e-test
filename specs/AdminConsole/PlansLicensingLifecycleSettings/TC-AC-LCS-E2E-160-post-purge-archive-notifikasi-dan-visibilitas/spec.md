---
id: TC-AC-LCS-E2E-160-post-purge-archive-notifikasi-dan-visibilitas
title: "Post-Purge Archive Matching: Principal Berizin, Notifikasi Gagal, Visibilitas Penanda, True Hard Delete, dan Principal di Luar Rantai Group"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-566
  - TC-AC-LCS-567
  - TC-AC-LCS-568
  - TC-AC-LCS-569
  - TC-AC-LCS-681
coverage:
  web: automated
---

# Post-Purge Archive Matching: Principal Berizin, Notifikasi Gagal, Visibilitas Penanda, True Hard Delete, dan Principal di Luar Rantai Group

## Prerequisites

- Mode: FE+BE. Kelas harness d (harness eksternal: job lifecycle, True Hard Delete, kegagalan layanan notifikasi, dan pencocokan indeks arsip).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Akun lain dalam spec: Distributor `distributorUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_DIST_PASSWORD`, TC 568); User Client PT Baru Mandiri `clientUserBaruMandiri_automated_{namaCompany}@qwertysystem.net` (Pre-setup 14, usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE; env password disediakan tim FE; Client baru dibuat spec dengan email User `ops@ptlamasejahtera.example`); Principal berizin dan pengguna A dan B (Pre-setup 11 dan 15, env password disediakan tim FE).
- Data Pre-setup yang dipakai: Client baru PT Baru Mandiri, Company PT Lama Sejahtera (purged), dan Principal berizin Update pada role "Manage archived client" (Pre-setup 10 dan 11). Email `ops@ptlamasejahtera.example` dan nama Client PT Baru Mandiri adalah data TC yang dicocokkan dengan indeks arsip (literal, bukan data bersuffix); Client hasil spec dibuang lewat Fixture BE antar-TC dan di hook `after` suite. Form pembuatan Client memakai field wajib lain yang disediakan tim FE.
- Akun Partner, Distributor, dan Principal berizin "Manage allocation" atau "Manage archived client" (Pre-setup 11) tertulis di Pre-setup 15 sebagai usulan pola Pre-setup 6 (keberadaan akun perlu dikonfirmasi tim FE): `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageArchivedClientPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`, `manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`; env password akun-akun itu belum terdaftar, jadi disediakan tim FE. Email pengguna Total Control produk terdampak tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal data uji subscription, mengatur jam server dan jam browser, memicu eksekusi job lifecycle dan job Email Trigger Engine, serta membaca log job; mail-catcher atau inbox riil dengan baseline jumlah email per alamat sebelum aksi (S-12). Indeks arsip, notifikasi match, dan log job dibaca lewat Fixture BE; layanan notifikasi dipaksa gagal lewat Fixture BE dan dipulihkan sebelum TC berikutnya serta di hook `after` suite.
- Notifikasi yang diasersi memakai baseline jumlah notifikasi sebelum aksi (S-12).
- State global: jam server dan jam browser digeser, subscription uji PT Maju Jaya, antrean job, dan konfigurasi tab diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-566: Tidak ada Principal berizin Manage archived client, notifikasi tidak dibuat, penanda tetap disematkan, Client tetap dibuat

1. Atur lewat Fixture BE: email `ops@ptlamasejahtera.example` pada indeks arsip dalam retensi; tidak ada pengguna Principal dengan Update pada role "Manage archived client" pada Group tempat Client baru ditempatkan maupun ancestor-nya; catat baseline jumlah notifikasi match arsip
2. Buat Client baru PT Baru Mandiri dengan email User `ops@ptlamasejahtera.example`
3. Verifikasi Client PT Baru Mandiri berhasil dibuat
4. Verifikasi tidak ada notifikasi dibuat (selisih jumlah notifikasi match arsip pada Fixture BE terhadap baseline 0)
5. Buka Detail Client PT Baru Mandiri
6. Verifikasi penanda match tetap disematkan pada Client
7. Verifikasi log job (Fixture BE) mencatat kejadian

### TC-AC-LCS-567: Notifikasi internal gagal terkirim, pembuatan Client tetap sukses

8. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: Principal berizin Update pada role "Manage archived client" tersedia pada Group tempat Client baru PT Baru Mandiri ditempatkan (atau salah satu ancestor-nya); email `ops@ptlamasejahtera.example` pada indeks arsip dalam retensi; layanan notifikasi dipaksa gagal
9. Buat Client baru PT Baru Mandiri dengan email User `ops@ptlamasejahtera.example`
10. Verifikasi Client PT Baru Mandiri berhasil dibuat tanpa pesan error
11. Verifikasi pembuatan Client selesai tanpa penundaan
12. Pulihkan layanan notifikasi lewat Fixture BE

### TC-AC-LCS-568: Penanda match dan notifikasi tidak terlihat oleh Distributor pembuat Client maupun pengguna Client baru

13. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: Principal berizin Update pada role "Manage archived client" tersedia; email `ops@ptlamasejahtera.example` pada indeks arsip dalam retensi
14. Ganti akun ke Distributor (`distributorUser_automated_{namaCompany}@qwertysystem.net`)
15. Buat Client baru PT Baru Mandiri dengan email User `ops@ptlamasejahtera.example`
16. Verifikasi Client PT Baru Mandiri berhasil dibuat
17. Verifikasi pembuatan Client tidak menampilkan UI atau pesan khusus tentang match
18. Buka Detail Client PT Baru Mandiri sebagai Distributor pembuat
19. Verifikasi Detail Client PT Baru Mandiri tampil
20. Verifikasi Detail Client tidak menampilkan penanda match
21. Ganti akun ke User Client PT Baru Mandiri
22. Verifikasi halaman utama User Client tampil
23. Verifikasi User Client baru tidak melihat indikator match apa pun

### TC-AC-LCS-569: True Hard Delete membersihkan indeks arsip setelah masa retensi berakhir

24. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: Principal berizin Update pada role "Manage archived client" tersedia; Company PT Lama Sejahtera di-Hard Purge 731 hari lalu (retensi 730 hari berakhir); catat baseline jumlah notifikasi Principal berizin
25. Picu eksekusi job True Hard Delete lewat Fixture BE
26. Ganti akun ke Total Control
27. Buat Client baru dengan email User milik PT Lama Sejahtera
28. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
29. Verifikasi indeks arsip PT Lama Sejahtera sudah dibersihkan (dibaca lewat Fixture BE)
30. Verifikasi tidak ada notifikasi baru (selisih terhadap baseline 0)
31. Buka Detail Client yang baru dibuat sebagai Principal berizin
32. Verifikasi tidak ada penanda match

### TC-AC-LCS-681: Principal berizin Manage archived client pada Group di luar rantai Group Client baru tidak menerima notifikasi match

33. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: dua pengguna Principal berizin Update pada role "Manage archived client" (pengguna A pada Group tempat Client baru PT Baru Mandiri ditempatkan, pengguna B pada Group lain yang bukan ancestor-nya); email `ops@ptlamasejahtera.example` pada indeks arsip dalam retensi; catat baseline jumlah notifikasi pengguna A dan pengguna B
34. Ganti akun ke Total Control
35. Buat Client baru PT Baru Mandiri dengan email User `ops@ptlamasejahtera.example`
36. Ganti akun ke pengguna A lalu buka Overlay Notifikasi
37. Verifikasi pengguna A menerima tepat satu notifikasi dalam aplikasi view-only match arsip (selisih terhadap baseline 1)
38. Ganti akun ke pengguna B lalu buka Overlay Notifikasi
39. Verifikasi pengguna B tidak menerima notifikasi (selisih terhadap baseline 0)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness d.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc` (566 sampai 569, lalu 681).
- `Verifikasi` Client berhasil dibuat dan `Verifikasi` Detail Client tampil pada TC 568 adalah anchor positif untuk asersi absence berikutnya (bagian 8b butir 2); keduanya asersi tambahan tanpa butir Expected padanan dan dicatat di sini (S-03).
- TC 566 Expected b ditulis sebagai dua `Verifikasi` (tidak ada notifikasi, penanda tetap disematkan) sesuai klausa; pengamatan penanda memerlukan langkah penghubung membuka Detail Client.
- Temuan untuk QA:
  - Akun Principal berizin kini di Pre-setup 15 (usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE); pengguna A dan B pada TC 681 tidak punya akun tersendiri di Pre-setup, ditulis sebagai disediakan tim FE.
  - TC 568 langkah 3 "Login sebagai User Client PT Baru Mandiri" dirujuk ke akun Pre-setup 14 (usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE); env password belum terdaftar sehingga disediakan tim FE.
  - TC 567 Expected "tanpa penundaan" tidak punya ambang waktu; spec mengasersi pembuatan selesai tanpa menunggu notifikasi internal.
  - TC 569 Expected "tidak ada penanda match" tanpa langkah yang membuka Detail Client; spec membuka Detail Client sebagai langkah penghubung.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1, 5, 8, 12-14, 18, 21, 24-26, 28, 31, 33-34, 36, 38.
- Alasan jumlah langkah (39 langkah, di atas smell sekitar 35): semua blok satu kelas harness dan berdiri sendiri: tiap TC memakai data fixture dan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; memecah spec hanya menggandakan pola ganti akun yang sama.
