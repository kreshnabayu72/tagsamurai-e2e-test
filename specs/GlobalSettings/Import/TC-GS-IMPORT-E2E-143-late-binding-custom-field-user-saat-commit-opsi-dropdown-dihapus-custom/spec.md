---
id: TC-GS-IMPORT-E2E-143-late-binding-custom-field-user-saat-commit-opsi-dropdown-dihapus-custom
title: "Late-binding Custom Field User saat commit: opsi Dropdown dihapus, Custom Field nonaktif, dan Decimal Places diganti"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-401
  - TC-GS-IMPORT-402
  - TC-GS-IMPORT-403
coverage:
  web: automated
---

# Late-binding Custom Field User saat commit: opsi Dropdown dihapus, Custom Field nonaktif, dan Decimal Places diganti

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua: Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, hanya lewat sesi API sebagai pemicu perubahan state (P-2); tidak ada asersi di sesi itu.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > User Login (Client E); perpindahan halaman lain ditulis sebagai langkah.
- Data Dinamis (draft lewat fixture `Fixture.import.lateBindingCf143`, fixture baru; nama literal dari Data Dinamis karena asersi bergantung pada nama dan jumlah): D-54 (user-login-commit-8.csv, 8 baris `pending`: Rizky Pratama Shift `Siang`, Sinta Maharani Shift `Siang`, Doni Kurniawan Shift `Pagi`, Eka Putri Overtime Hours `1.25`, Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata). Custom Field Client E (Pre-setup): Shift (Dropdown: Pagi, Siang, Malam) dan Overtime Hours (Numeric, 2 desimal). Produk organisasi Client E: Global Settings dan Fixed Asset.
- Kemampuan teknis (disediakan tim FE/BE): skrip reset Client E sesuai D-47 (hapus User Login hasil commit, draft, hasil commit terakhir) ditambah pemulihan Custom Field Shift (aktif, opsi Pagi, Siang, Malam) dan Overtime Hours (2 desimal); permintaan hapus opsi, nonaktifkan atau aktifkan Custom Field, dan ganti Decimal Places atas nama Admin kedua Client E lewat klien HTTP.
- State global: Custom Field Client E diubah lalu dipulihkan (R2). Suite Import berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 dan pulihkan state yang diubah spec (lihat kemampuan teknis).

## Test Steps

### TC-GS-IMPORT-401: Opsi Dropdown Custom Field dihapus tanpa pembacaan tabel, baris dengan opsi itu menjadi error dan baris lain terkomit

1. Reset Client E ke tanpa draft (D-47), siapkan draft User Login 8 baris dari user-login-commit-8.csv (D-54, Shift `Siang` pada baris #1 dan #2, Shift `Pagi` pada baris #3) lewat fixture
2. Buka Import > User Login dan tunggu Staging Table termuat
3. Verifikasi footer menampilkan `[Import (8)]` Enabled
4. Hapus opsi `Siang` dari Custom Field Shift (Dropdown) di halaman User > Custom Field atas nama Admin kedua Client E lewat sesi API hingga tersimpan
5. Pada halaman yang sama (tanpa memuat ulang) klik [Import (8)]
6. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
7. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 2 errors remain." tampil
8. Verifikasi Staging Table menampilkan 2 baris berstatus `error`: Rizky Pratama dan Sinta Maharani (Shift `Siang`)
9. Verifikasi Error Summary Callout memuat "Shift: Invalid option"
10. Verifikasi Error Summary Callout menampilkan badge "2 rows"
11. Buka halaman User > User List > Login User
12. Atur Rows per page 100
13. Verifikasi halaman User > User List > Login User Client E memuat 6 user baru: Doni Kurniawan, Eka Putri, Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata

### TC-GS-IMPORT-402: Nilai pada Custom Field nonaktif ditulis ke User saat commit, tersembunyi selama field nonaktif dan tampil saat diaktifkan kembali

14. Reset Client E ke tanpa draft (D-47), siapkan draft User Login 8 baris dari user-login-commit-8.csv (D-54, Shift `Siang` pada baris #1 dan #2, Shift `Pagi` pada baris #3) lewat fixture
15. Nonaktifkan Custom Field Shift di halaman User > Custom Field atas nama Admin kedua Client E lewat sesi API hingga tersimpan (tanpa membuka Staging Table)
16. Buka Import > User Login
17. Klik [Import (8)]
18. Muat ulang halaman Import > User Login setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
19. Verifikasi Dropzone tampil menggantikan Staging Table
20. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
21. Buka halaman User > User List > Login User
22. Atur Rows per page 100
23. Verifikasi halaman User > User List > Login User Client E memuat 8 user baru: Rizky Pratama, Sinta Maharani, Doni Kurniawan, Eka Putri, Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata
24. Buka Detail user `Rizky Pratama`
25. Verifikasi Detail user `Rizky Pratama` tampil
26. Verifikasi Custom Field Shift tidak tampil pada Detail `Rizky Pratama` selama Custom Field Shift nonaktif
27. Aktifkan kembali Custom Field Shift di halaman User > Custom Field atas nama Admin kedua Client E lewat sesi API hingga tersimpan
28. Muat ulang Detail user `Rizky Pratama` (F5)
29. Verifikasi Detail user `Rizky Pratama` tampil
30. Verifikasi Custom Field Shift bernilai `Siang` pada Detail `Rizky Pratama`

### TC-GS-IMPORT-403: Decimal Places Numeric diganti sebelum commit, nilai melampaui presisi baru menjadi error

31. Reset Client E ke tanpa draft (D-47), siapkan draft User Login 8 baris dari user-login-commit-8.csv (D-54, Overtime Hours `1.25` pada baris #4); Custom Field Overtime Hours (Numeric, 2 desimal) belum memiliki nilai pada user Client E lewat fixture
32. Buka Import > User Login dan tunggu Staging Table termuat
33. Verifikasi footer menampilkan `[Import (8)]` Enabled
34. Ganti Decimal Places Custom Field Overtime Hours (Numeric) dari 2 menjadi 1 di halaman User > Custom Field atas nama Admin kedua Client E lewat sesi API hingga tersimpan
35. Pada halaman yang sama (tanpa memuat ulang) klik [Import (8)]
36. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
37. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
38. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Eka Putri (Overtime Hours `1.25`)
39. Verifikasi Error Summary Callout memuat "Overtime hours must have at most 1 decimal place"
40. Verifikasi Error Summary Callout menampilkan badge "1 row"
41. Buka halaman User > User List > Login User
42. Atur Rows per page 100
43. Verifikasi halaman User > User List > Login User Client E memuat 7 user baru
44. Verifikasi user Eka Putri tidak ada

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (401, 402, 403) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah pertama tiap blok (reset Client E dan penyiapan draft karena Precondition tiap TC mensyaratkan Client E direset sebelum TC), langkah pemicu Admin kedua, langkah menunggu commit, langkah pindah halaman, Rows per page 100, dan membuka Detail user.
- P-2: Admin kedua Client E hanya memicu perubahan Custom Field lewat sesi API dan bukan objek asersi.
- Absence `Custom Field Shift tidak tampil` pada Detail user didahului `Verifikasi` Detail user tampil (anchor surface). Absence user tertentu pada daftar didahului verifikasi daftar user baru.
- Spec melewati sekitar 35 langkah. Alasan: tiga blok TC homogen (late-binding Custom Field User saat commit) yang berdiri sendiri, masing-masing mereset Client E dan Custom Field; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pola halaman basi (late-binding saat commit, TC-GS-IMPORT-401, 403): halaman Import dimuat dan Staging Table dibaca sebelum pemicu, lalu `[Import (N)]` diklik pada halaman yang sama tanpa dimuat ulang, dengan N dari sebelum pemicu. Referensi, duplikat, dan opsi dievaluasi ulang saat commit selain saat pembacaan Staging Table (PRD `import.md` baris 994, 1164, 1195). `Verifikasi` footer `[Import (N)]` sebelum pemicu adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan draft sudah dibaca pada halaman itu.
- Temuan untuk QA:
  - TC-GS-IMPORT-402: Post Condition b (Custom Field Shift berisi `Siang` pada `Rizky Pratama` dan `Sinta Maharani`, `Pagi` pada `Doni Kurniawan`, kosong pada lima record lain) hanya teramati untuk `Rizky Pratama` lewat Expected d; sisanya tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-GS-IMPORT-403: syarat penggantian Decimal Places (Overtime Hours belum memiliki nilai pada user Client E) tidak punya mekanisme seeding di Data Dinamis; dicatat sebagai kebutuhan reset Client E.
  - TC-GS-IMPORT-401 sampai 403: Post Condition (draft berisi baris `error`; opsi Shift `Siang` tidak ada; Decimal Places bernilai 1) tidak punya langkah observasi di TC selain Expected; tidak diasersi.
  - Data Dinamis D-54 literal tanpa suffix per run karena asersi bergantung pada nama; pengecualian S-12 untuk data ini belum dinyatakan di konvensi, dipertahankan dengan reset D-47 dan suite serial.
