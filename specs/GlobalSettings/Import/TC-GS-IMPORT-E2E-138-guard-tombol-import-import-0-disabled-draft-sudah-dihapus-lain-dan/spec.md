---
id: TC-GS-IMPORT-E2E-138-guard-tombol-import-import-0-disabled-draft-sudah-dihapus-lain-dan
title: "Guard tombol Import: Import (0) Disabled, draft sudah dihapus admin lain, dan tidak ada baris pending dari halaman basi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-362
  - TC-GS-IMPORT-363
  - TC-GS-IMPORT-738
coverage:
  web: automated
---

# Guard tombol Import: Import (0) Disabled, draft sudah dihapus admin lain, dan tidak ada baris pending dari halaman basi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua: Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, hanya lewat sesi API sebagai pemicu perubahan state (Discard Draft dan Remove baris); tidak ada asersi di sesi itu.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand (Client E).
- Data Pre-setup Client E (tidak diubah): Brand `Samsung`.
- Data Dinamis (draft lewat fixture `Fixture.import.importGuard138`, fixture baru; nama literal dari Data Uji TC karena asersi bergantung pada nama): brand-no-pending-4.csv (3 baris `error` Brand Name 121 karakter huruf `A`, `B`, `C`, dan `Samsung` `duplicate`); brand-nikon-1.csv (`Nikon` `pending`); brand-nikon-error-2.csv (`Nikon` `pending` dan Brand Name 121 karakter huruf `A` `error`).
- Kemampuan teknis (disediakan tim FE/BE): skrip reset Client E sesuai D-47; penyiapan draft lewat fixture; permintaan Discard Draft dan Remove baris atas nama Admin kedua Client E lewat klien HTTP.
- State global: Client E dimutasi lalu direset. Suite Import berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 (hapus Brand `Nikon` hasil commit bila ada dan draft).

## Test Steps

### TC-GS-IMPORT-362: Import (0) Disabled dengan tooltip bila draft hanya berisi baris error dan duplicate

1. Reset Client E ke tanpa draft (D-47), siapkan draft Brand 4 baris dari brand-no-pending-4.csv lewat fixture, lalu muat ulang halaman Import > Brand
2. Hover `[Import (0)]` di footer
3. Verifikasi `[Import (0)]` tetap tampil
4. Verifikasi `[Import (0)]` Disabled
5. Verifikasi tooltip "No rows are ready to import."
6. Klik `[Import (0)]`
7. Verifikasi tidak ada dialog terbuka
8. Verifikasi tidak ada toast tampil
9. Verifikasi Staging Metric Cards Ready to Import 0
10. Verifikasi Staging Metric Cards Errors 3
11. Verifikasi Staging Metric Cards Duplicates 1

### TC-GS-IMPORT-363: Import dari halaman basi setelah draft dihapus menampilkan toast netral Draft Tidak Ditemukan

12. Reset Client E ke tanpa draft (D-47), siapkan draft Brand 1 baris dari brand-nikon-1.csv lewat fixture
13. Muat halaman Import > Brand sebagai Total Control Client E
14. Verifikasi footer menampilkan `[Import (1)]` Enabled
15. Hapus draft Brand Client E atas nama Admin kedua Client E lewat permintaan Discard Draft sesi API hingga tersimpan
16. Pada halaman langkah 13 (tanpa muat ulang) klik `[Import (1)]`
17. Verifikasi toast netral (Info) "This draft is no longer available."
18. Verifikasi Dropzone tampil
19. Verifikasi `[Import (0)]` Disabled

### TC-GS-IMPORT-738: Import dari halaman basi saat draft sudah tanpa baris pending ditolak dengan toast gagal Import

20. Tunggu toast lama hilang otomatis atau tutup toast
21. Reset Client E ke tanpa draft (D-47), siapkan draft Brand 2 baris dari brand-nikon-error-2.csv (`Nikon` `pending`, Brand Name 121 karakter huruf `A` `error`) lewat fixture
22. Muat halaman Import > Brand sebagai Total Control Client E
23. Verifikasi footer menampilkan `[Import (1)]` Enabled
24. Hapus baris `Nikon` atas nama Admin kedua Client E lewat permintaan Remove sesi API hingga tersimpan
25. Pada halaman langkah 22 (tanpa muat ulang) klik `[Import (1)]`
26. Verifikasi toast error persisten "Error, failed to import record."
27. Muat ulang halaman Import > Brand
28. Verifikasi Staging Table menampilkan 1 baris `error`
29. Verifikasi kartu Ready to Import 0
30. Hover `[Import (0)]`
31. Verifikasi `[Import (0)]` tetap tampil
32. Verifikasi `[Import (0)]` Disabled
33. Verifikasi tooltip "No rows are ready to import."
34. Buka halaman Master Reference > Brand
35. Ketik Search `Samsung`, tekan Enter
36. Verifikasi tabel Brand Client E menampilkan baris bernama `Samsung`
37. Ganti isi kotak search dengan `Nikon`, tekan Enter
38. Verifikasi tabel Brand Client E tidak menampilkan hasil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Spec berisi 38 langkah, di atas 35 langkah. Alasan: tiga TC satu kelas (guard tombol Import) pada Client E; tiap TC berdiri sendiri dengan reset Client E sebelumnya (langkah 1, 12, 21).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- P-2: Admin kedua Client E hanya memicu perubahan state lewat sesi API (Discard Draft pada langkah 15, Remove baris pada langkah 24) dan tidak menjadi objek asersi; sesi UI kedua tidak dipakai.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 12, dan 21 (reset Client E dan penyiapan draft karena tiap TC mensyaratkan Client E direset sebelum TC); langkah 13 dan 22 (memuat halaman yang menjadi halaman basi); langkah 20 (menutup toast TC-363 sebelum toast error TC-738 diasersi); langkah 34 (pindah halaman).
- Anchor positif: langkah 36 (baris `Samsung` tampil di tabel Brand Client E) menjadi pembanding sebelum asersi hasil kosong pada langkah 38; Search dikosongkan lewat penggantian isi kotak (butir 9 bagian 8b).
- Pembagian TC lintas spec: `Import (0)` Disabled pada state hanya `error` dan `duplicate` dikerjakan di sini; TC-GS-IMPORT-738 menjadi satu-satunya TC dengan Remove dari sesi lain pada baris `pending`.
- Temuan untuk QA:
  - TC-GS-IMPORT-362: Post Condition (draft tetap berisi 3 baris `error` dan 1 baris `duplicate`) teramati hanya sebagian lewat kartu Errors 3 dan Duplicates 1; tidak ada observasi tambahan.
  - TC-GS-IMPORT-363: Post Condition (tidak ada record Brand baru) tidak punya langkah observasi di TC; tidak diasersi.
  - TC-GS-IMPORT-738: Post Condition (draft berisi 1 baris `error`; tidak ada record Brand baru) dicakup langkah 28 dan 38; precondition b menyebut halaman Import > Brand terbuka sebelum fixture Remove, spec memuat halaman setelah draft disiapkan (langkah 22).
  - Toast TC-363 dan TC-738 memakai Admin kedua lewat sesi API, bukan tab kedua; TC tidak menyebut jenis sesi.
