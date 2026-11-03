---
id: TC-FA-CF-E2E-116-retensi-state-f5-sidebar-dan-pindah-tab
title: "Retensi State F5, Reset Sidebar, dan Pindah Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-443
  - TC-FA-CF-444
  - TC-FA-CF-445
  - TC-FA-CF-446
  - TC-FA-CF-447
coverage:
  web: automated
---

# Retensi State F5, Reset Sidebar, dan Pindah Tab

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Alpha (Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) dan tab Purchasing empat field (Pre-setup #13: `Vendor Code`, `Warranty Months`, `Rated Precision`, `Long Option Field`), dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` dan `Fixture.faCustomFields.baselinePurchasing` (fixture belum ada, disediakan tim FE). Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: muat ulang halaman (F5) dan pembacaan state Search, Filter, Sort, paginasi, dan tab aktif.
- State global: tidak ada yang diubah (state Search, Filter, Sort, paginasi, dan tab hanya state tampilan).

## Test Steps

### TC-FA-CF-447: Pertama masuk halaman tab General aktif

1. Amati halaman Fixed Asset > Settings > Custom Fields yang dibuka hook `beforeEach` suite sebagai kunjungan pertama pada sesi login hook `before`
2. Verifikasi tab `General` aktif

### TC-FA-CF-443: Refresh F5 mempertahankan tab aktif beserta Search, Filter, Sort, dan paginasi

3. Klik tab `Purchasing`
4. Ketik Search `vendor`, tekan Enter
5. Klik icon Filter, pilih Data Type `Text`, klik `[Apply]`
6. Urutkan Field Name menurun (klik header `Field Name` hingga menurun)
7. Muat ulang halaman (F5)
8. Verifikasi tab `Purchasing` tetap aktif setelah reload
9. Verifikasi Search `vendor` dipertahankan
10. Verifikasi Filter Data Type `Text` dipertahankan
11. Verifikasi Sort Field Name menurun dipertahankan
12. Verifikasi paginasi dipertahankan (halaman 1, 10 baris per halaman)

### TC-FA-CF-444: Refresh F5 mempertahankan state tab yang tidak aktif

13. Klik menu `Custom Fields` dari sidebar
14. Ketik Search `serial`, tekan Enter
15. Klik tab `Purchasing`
16. Muat ulang halaman (F5)
17. Verifikasi tab `Purchasing` aktif setelah reload
18. Klik tab `General`
19. Verifikasi Search `serial` masih terpasang pada tab General

### TC-FA-CF-445: Klik ulang menu sidebar mereset state dan kembali ke tab General

20. Klik tab `Purchasing`
21. Ketik Search `vendor`, tekan Enter
22. Klik icon Filter, pilih Data Type `Text`, klik `[Apply]`
23. Urutkan Field Name menurun (klik header `Field Name` hingga menurun)
24. Klik menu `Custom Fields` dari sidebar
25. Verifikasi tabel kembali ke tab `General`
26. Verifikasi Search dalam keadaan default (kosong)
27. Verifikasi Filter dalam keadaan default (tidak ada filter terpasang)
28. Verifikasi Sort dalam keadaan default (tanpa urutan aktif)
29. Verifikasi paginasi dalam keadaan default (halaman 1, 10 baris per halaman)

### TC-FA-CF-446: Pindah tab grup me-refresh tabel dan menyimpan state tiap tab

30. Ketik Search `serial`, tekan Enter
31. Verifikasi Breadcrumb `Settings > Custom Fields` pada tab General
32. Klik tab `Purchasing`
33. Verifikasi tabel me-refresh untuk grup Purchasing: tabel memuat `Vendor Code`, `Warranty Months`, `Rated Precision`, dan `Long Option Field`
34. Verifikasi Breadcrumb `Settings > Custom Fields` pada tab Purchasing
35. Klik tab `General`
36. Verifikasi state tab General pulih (Search `serial` terpasang)
37. Verifikasi Breadcrumb `Settings > Custom Fields` pada tab General kembali

## Notes

- Spec memuat 37 langkah, di atas smell 35 langkah. Alasan: satu topik (retensi state halaman dan tab), satu akun, satu dataset (Company Alpha baseline) tanpa mengubah data; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-CF-448 dan 449 ada di spec 177.
- Urutan TC di spec: 447, 443, 444, 445, 446. TC-FA-CF-447 di awal supaya pembukaan halaman oleh hook `beforeEach` suite adalah kunjungan pertama pada sesi (langkah 1); TC berikutnya memulihkan state dengan klik sidebar (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mengamati halaman yang sudah dibuka hook sebagai pengganti langkah buka TC-FA-CF-447), langkah 13 (klik sidebar mereset Search, Sort, Filter, dan kembali ke tab General sebelum TC-FA-CF-444), langkah 20 sampai 23 (pengaturan state sebelum klik sidebar sesuai langkah uji TC-FA-CF-445; Search pada langkah 4, 14, 21, dan 30 menyaring baris target, R-16).
- Anchor absence: langkah 26 sampai 28 membuktikan state default setelah langkah 25 menampilkan tab General (halaman termuat).
- Temuan untuk QA:
  - TC-FA-CF-443 Search `vendor` dengan Filter `Text` pada tab Purchasing menghasilkan satu baris (`Vendor Code`); urutan Sort menurun tidak teramati dari urutan baris, sehingga langkah 11 memeriksa indikator Sort pada header `Field Name`.
  - TC-FA-CF-443 Expected ("paginasi dipertahankan") tidak menyebut nilainya; spec memakai halaman 1 dan 10 baris per halaman.
  - TC-FA-CF-445 langkah 1 ("Atur Search, Filter, Sort") tidak menyebut nilainya; spec memakai Search `vendor`, Filter Data Type `Text`, dan Sort Field Name menurun (sama dengan TC-FA-CF-443).
  - TC-FA-CF-447 Langkah Uji ("Buka ... untuk pertama kali pada sesi") tidak dapat diulang dalam satu sesi; spec memakai pembukaan halaman pertama oleh hook `beforeEach` suite.
  - TC-FA-CF-446 Expected a ("seketika me-refresh tabel") tidak menyebut ukuran waktu; spec memeriksa isi tabel Purchasing langsung setelah klik tab.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
