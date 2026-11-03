---
id: TC-AC-LCS-E2E-158-state-machine-perpanjangan-renew-dan-downgrade-paralel
title: "State Machine Lifecycle: Perpanjangan Membatalkan Lifecycle, Renew, Downgrade Paralel, dan Tanpa Aksi Renew pada Archive"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-556
  - TC-AC-LCS-557
  - TC-AC-LCS-558
  - TC-AC-LCS-559
  - TC-AC-LCS-560
  - TC-AC-LCS-687
coverage:
  web: automated
---

# State Machine Lifecycle: Perpanjangan Membatalkan Lifecycle, Renew, Downgrade Paralel, dan Tanpa Aksi Renew pada Archive

## Prerequisites

- Mode: FE+BE. Kelas harness h (state tenant: Grace, Active, Expired, Archive, Downgrade).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: Client PT Maju Jaya (Direct, pengguna Total Control aktif pada produk terdampak, subscription Paid) dan Client lain sesuai Pre-setup 10; subscription dan rantai kepemilikan diatur per TC lewat Fixture BE dan dipulihkan di hook `after` suite. Rantai kepemilikan: Partner PT Mitra Satu dan Distributor PT Distribusi Utama dengan pengguna berizin Manage allocation di setiap level.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal data uji subscription, mengatur jam server dan jam browser, memicu eksekusi job lifecycle dan job Email Trigger Engine, serta membaca log job; mail-catcher atau inbox riil dengan baseline jumlah email per alamat sebelum aksi (S-12). Penetapan Downgrade dan pembacaan pelacak lifecycle berada di luar modul ini dan dilakukan lewat Fixture BE; aksi Renew dilakukan lewat UI Allocation > Client Subscription > List Subscriptions.
- State global: jam server dan jam browser digeser, subscription uji PT Maju Jaya, antrean job, dan konfigurasi tab diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-556: Subscription Expired atau Grace yang diperpanjang membatalkan lifecycle tanpa menghapus record

1. Atur lewat Fixture BE: Subscription PT Maju Jaya berstatus `Grace` (rantai kepemilikan Partner PT Mitra Satu dan Distributor PT Distribusi Utama dengan pengguna berizin Manage allocation)
2. Buka Allocation > Client Subscription > List Subscriptions
3. Ketik Search `PT Maju Jaya`, tekan Enter
4. Perpanjang (Renew) subscription PT Maju Jaya
5. Tunggu aksi selesai (Renew tersimpan)
6. Picu eksekusi job lifecycle lewat Fixture BE
7. Muat ulang daftar List Subscriptions
8. Ketik Search `PT Maju Jaya`, tekan Enter
9. Verifikasi subscription lama PT Maju Jaya berstatus `Renewed`
10. Verifikasi term baru PT Maju Jaya berstatus `Active`
11. Verifikasi pelacak lifecycle dibatalkan (dibaca lewat Fixture BE)
12. Verifikasi record subscription lama tetap ada (tidak dihapus) pada List Subscriptions
13. Verifikasi data klien dapat diakses instan

### TC-AC-LCS-557: Renew pada subscription Active yang data berlebihnya berada di Archive membatalkan pelacak Downgrade dan memulihkan data sekitar 24 jam

14. Atur lewat Fixture BE: Subscription PT Maju Jaya berstatus `Active` dengan pelacak Downgrade aktif dan data berlebih pada fase Archive
15. Ketik Search `PT Maju Jaya`, tekan Enter
16. Perpanjang (Renew) subscription PT Maju Jaya dengan plan semula pada Allocation > Client Subscription > List Subscriptions
17. Tunggu aksi selesai (Renew tersimpan)
18. Muat ulang daftar List Subscriptions
19. Ketik Search `PT Maju Jaya`, tekan Enter
20. Verifikasi term baru PT Maju Jaya berstatus `Active`
21. Verifikasi pelacak Downgrade dibatalkan (dibaca lewat Fixture BE)
22. Verifikasi record lama tidak dihapus pada List Subscriptions
23. Verifikasi data berlebih dipulihkan dari cold storage sekitar 24 jam sesuai fase Archive

### TC-AC-LCS-558: Principal menetapkan Downgrade pada subscription yang sudah memiliki pelacak Expired aktif, tidak diblok dan berjalan paralel

24. Atur lewat Fixture BE: Subscription PT Maju Jaya memiliki pelacak Expired aktif
25. Tetapkan Downgrade subscription PT Maju Jaya lewat Fixture BE
26. Verifikasi penetapan Downgrade berhasil tanpa blok
27. Verifikasi pelacak Expired tidak dibatalkan oleh penetapan Downgrade
28. Verifikasi pelacak Downgrade baru berjalan paralel dengan pelacak Expired

### TC-AC-LCS-559: Penetapan Downgrade kedua pada subscription dengan Downgrade aktif ditolak

29. Atur lewat Fixture BE: Subscription PT Maju Jaya memiliki pelacak Downgrade aktif
30. Tetapkan Downgrade kedua pada subscription yang sama lewat Fixture BE
31. Verifikasi penetapan ditolak dengan pesan "This subscription already has an active downgrade in progress"

### TC-AC-LCS-560: Pelacak Expired dan Downgrade mencapai T-0 hampir bersamaan, diproses independen dan pelacak Downgrade tetap tersimpan

32. Atur lewat Fixture BE: Subscription PT Maju Jaya memiliki pelacak Expired dan pelacak Downgrade dengan tanggal T-0 hampir bersamaan
33. Picu eksekusi job lifecycle lewat Fixture BE
34. Buka Allocation > Client Subscription > List Subscriptions
35. Ketik Search `PT Maju Jaya`, tekan Enter
36. Verifikasi pelacak Expired dan Downgrade diproses independen sesuai urutan masing-masing (status dan pelacak dibaca lewat Fixture BE dan List Subscriptions)
37. Verifikasi pelacak Downgrade tetap tersimpan apa adanya walau efeknya teredam oleh siklus Expired yang cakupannya lebih luas

### TC-AC-LCS-687: Subscription berstatus Archive pada Skenario Expired tidak punya aksi Renew

38. Atur lewat Fixture BE: Subscription Paid PT Maju Jaya berstatus `Archive` (Skenario Expired)
39. Buka Allocation > Client Subscription > List Subscriptions
40. Ketik Search `PT Maju Jaya`, tekan Enter
41. Verifikasi row action pada baris subscription PT Maju Jaya memuat `Detail`
42. Verifikasi row action pada baris subscription PT Maju Jaya tidak memuat `Renew`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness h.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc` (556 sampai 560, lalu 687).
- Asersi pada TC 558 dan 559 hanya memakai hasil penetapan lewat Fixture BE karena penetapan Downgrade berada di luar modul ini (bagian 8b butir 1).
- Temuan untuk QA:
  - Alur Renew (dialog, field, dan konfirmasi) tidak dirinci di TC 556 dan 557; spec menulis satu langkah aksi Renew sesuai TC tanpa mengarang field.
  - TC 556 Expected c "Data klien dapat diakses instan" tidak menyebut cara pengamatan; spec menulisnya sebagai satu `Verifikasi` sesuai teks TC.
  - TC 557 Expected b "sekitar 24 jam" tidak menyebut cara membaca durasi pemulihan; spec mengasersi pemulihan dari cold storage sesuai fase Archive tanpa mengarang ambang.
  - TC 558 Expected b dan TC 560 Expected b mengamati pelacak lifecycle yang tidak terlihat di UI; spec membacanya lewat Fixture BE yang disediakan tim FE/BE.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-3, 5-8, 14-15, 17-19, 24-25, 29-30, 32-35, 38-40. Langkah "Ketik Search `PT Maju Jaya`, tekan Enter" mendahului aksi Renew dan `Verifikasi` baris di List Subscriptions (R-16, R-23); "Tunggu aksi selesai" (langkah 5, 17) menyusul Renew yang hasilnya tidak diasersi langsung dan diikuti pemicu job atau muat ulang (bagian 8b butir 8); langkah 34 membuka List Subscriptions sebagai layar `Verifikasi` status di TC 560 (TC menyebut List Subscriptions tanpa langkah buka).
- Alasan di atas sekitar 35 langkah: keenam blok TC (556 sampai 560 dan 687) satu kelas harness h tentang state machine lifecycle, memakai List Subscriptions dan Fixture BE yang sama, dan tiap blok menetapkan state subscription sendiri lalu memulihkannya lewat langkah penghubung; sebagian besar langkah tambahan adalah langkah penghubung (pemulihan, pengaturan data, ganti akun), sehingga memecahnya hanya mengulang pengaturan Fixture BE dan ganti akun yang sama, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
