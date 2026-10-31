---
id: TC-GS-GSET-E2E-035-changelog-setup-column-pin-hide-reorder-dan-reset-dengan-save
title: "Changelog General Settings: Setup Column Pin/Unpin, Hide/Unhide, Reorder, dan Reset to Default dengan Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-88
  - TC-GS-GSET-90
  - TC-GS-GSET-91
  - TC-GS-GSET-93
coverage:
  web: automated
---

# Changelog General Settings: Setup Column Pin/Unpin, Hide/Unhide, Reorder, dan Reset to Default dengan Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10).
- Seeding di hook `before` (precondition TC "Changelog berisi baris riwayat", dipakai sebagai precondition TC, tidak diasersi): satu PUT `/v2/enterprise-management/general-settings` (full-replace, `global-settings/general-settings/API/openapi.yaml`) oleh sesi API Budi Santoso yang mengubah `sessionIdleTimeout` dari 30 ke 60 menit, lalu satu PUT yang mengembalikannya ke 30 menit, sehingga Changelog memuat sedikitnya satu baris riwayat. Total entri Changelog tidak diasersi.
- Data uji: kolom `Date` (Pin/Unpin), `Action`, `Old Value`, `New Value` (hide/unhide), `Modified By` (drag ke posisi pertama), urutan default Date | Action | Field | Old Value | New Value | Modified By.
- Konfigurasi kolom Modal Changelog (visibilitas, urutan, pin) tersimpan per pengguna di cache browser dan permanen setelah `[Save]` (PRD general-settings.md §4.2c); "muat ulang halaman (F5)" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada. Pemulihan: langkah 38 dan 40 mengembalikan konfigurasi ke default lewat `[Reset to Default]` lalu `[Save]` (bagian dari TC-93); hook `after` (tetap jalan walau spec gagal di tengah) mengembalikan konfigurasi kolom Changelog ke default lewat penghapusan preferensi kolom Changelog di browser dan memulihkan lebar viewport awal (mekanisme disediakan tim FE).
- Kemampuan teknis: mengubah lebar viewport browser dan memulihkannya; scroll horizontal pada tabel Changelog; drag and drop baris pada Modal Setup Column; membaca dan menghapus preferensi kolom di penyimpanan browser.
- Suite berjalan serial (`parallel: false`): konfigurasi kolom Changelog bersifat state bersama dengan spec Setup Column dan Download lain.

## Test Steps

### TC-GS-GSET-88: Setup Column: Pin dan Unpin kolom lalu Save

1. Klik icon Changelog di pojok kanan atas halaman
2. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`
3. Klik icon Pin pada baris kolom `Date`
4. Verifikasi Live Preview menandai kolom `Date` beku (freeze)
5. Klik `[Save]`
6. Persempit lebar viewport hingga tabel Changelog dapat di-scroll horizontal, lalu scroll tabel ke kanan
7. Verifikasi kolom `Date` tetap terlihat saat tabel di-scroll
8. Refresh (F5)
9. Klik icon Changelog di pojok kanan atas halaman
10. Scroll tabel ke kanan
11. Verifikasi kolom `Date` tetap terlihat saat tabel di-scroll (status pin bertahan setelah F5)
12. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, klik icon Unpin pada baris kolom `Date`, klik `[Save]`
13. Scroll tabel ke kanan
14. Verifikasi kolom `Date` ikut bergeser keluar dari area terlihat saat tabel di-scroll
15. Pulihkan lebar viewport ke ukuran awal

### TC-GS-GSET-90: Setup Column: uncheck dan check kolom Action, Old Value, dan New Value lalu Save

16. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`
17. Hilangkan centang kolom `Action`, `Old Value`, dan `New Value`
18. Verifikasi Live Preview menyembunyikan kolom `Action`, `Old Value`, dan `New Value`
19. Klik `[Save]`
20. Verifikasi kolom `Date`, `Field`, dan `Modified By` tampil di tabel
21. Verifikasi kolom `Action`, `Old Value`, dan `New Value` tidak tampil di tabel
22. Refresh (F5)
23. Klik icon Changelog di pojok kanan atas halaman
24. Verifikasi kolom `Date`, `Field`, dan `Modified By` tampil di tabel
25. Verifikasi kolom `Action`, `Old Value`, dan `New Value` tetap tersembunyi setelah F5
26. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, centang kembali kolom `Action`, `Old Value`, dan `New Value`, klik `[Save]`
27. Verifikasi kolom `Action`, `Old Value`, dan `New Value` tampil kembali di tabel

### TC-GS-GSET-91: Setup Column: drag reorder kolom lalu Save

28. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`
29. Drag kolom `Modified By` ke posisi pertama
30. Verifikasi Live Preview menempatkan `Modified By` di urutan pertama
31. Klik `[Save]`
32. Verifikasi tabel menempatkan `Modified By` di urutan pertama
33. Refresh (F5)
34. Klik icon Changelog di pojok kanan atas halaman
35. Verifikasi tabel menempatkan `Modified By` di urutan pertama (urutan bertahan setelah F5)

### TC-GS-GSET-93: Setup Column: Reset to Default mengembalikan keenam kolom ke default

36. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, hilangkan centang kolom `Action`, geser kolom `Modified By` ke posisi pertama, klik `[Save]`
37. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...` lagi
38. Klik `[Reset to Default]`
39. Verifikasi Live Preview kembali ke 6 kolom default berurutan Date | Action | Field | Old Value | New Value | Modified By
40. Klik `[Save]`
41. Refresh (F5)
42. Klik icon Changelog di pojok kanan atas halaman
43. Verifikasi tabel memakai 6 kolom default berurutan Date | Action | Field | Old Value | New Value | Modified By (urutan default bertahan setelah F5)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE (Changelog dimuat dari backend nyata; konfigurasi kolom tersimpan di browser).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (88, 90, 91, 93) dipertahankan: TC-93 di akhir karena `[Reset to Default]` plus `[Save]` sekaligus memulihkan konfigurasi hasil TC-88, 90, dan 91 ke default.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 9, 23, 34, dan 42 (membuka Modal Changelog; Modal Changelog tertutup oleh F5), langkah 6 dan 10 serta 13 (scroll sebagai aksi pemicu asersi), langkah 15 (memulihkan viewport sebelum TC berikutnya), dan langkah 36 (menyiapkan konfigurasi awal sebagai langkah 1 TC-93).
- Save Setup Column (langkah 5, 12, 19, 26, 31, 36, 40) adalah aksi sisi klien tanpa request tulis ke server, jadi tidak diikuti langkah "Tunggu aksi selesai".
- Asersi tambahan (konkretisasi, S-03): langkah 20 dan 24 (kolom lain tetap tampil) adalah pembanding positif bagi asersi absence kolom `Action`, `Old Value`, dan `New Value` pada langkah 21 dan 25; absence sesudah F5 (langkah 25) didahului `Verifikasi` kolom lain pada tabel yang sama (langkah 24), sesuai bagian 8b butir 2 konvensi. Status pin sesudah F5 (Expected b TC-88) diamati lewat scroll tabel (langkah 10 dan 11) karena tidak ada indikator lain yang disebut TC.
- Langkah 7 dan 14 dipisah per klausa Expected TC-88; "tetap terlihat saat tabel di-scroll" (langkah 7) dan "status pin bertahan setelah F5" (langkah 11) adalah dua klausa Expected b.
- Spec melewati sekitar 35 langkah (43 langkah) karena empat TC memakai Modal Setup Column dan tabel Changelog yang sama pada satu kelas harness (fungsional), tiap TC memerlukan F5 dan pembukaan ulang Modal Changelog (langkah 8 dan 9, 22 dan 23, 33 dan 34, 41 dan 42 adalah prefix berulang), serta Expected dipecah satu `Verifikasi` per klausa (S-01). Tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-GSET-84, 87, 89, dan 94 (panel Column Visibility, screening Setup Column, pencarian kolom, tutup tanpa simpan) ada di spec 034; TC-GS-GSET-92 dan 95 (kolom visible terakhir, Reset to Default belum disimpan) di spec 054; TC-GS-GSET-70 di spec 028; TC-GS-GSET-100 dan 159 di spec 036.
- Temuan untuk QA:
  - TC-GS-GSET-88: langkah 5 tidak menyebut lebar viewport (px) yang membuat tabel dapat di-scroll horizontal; spec memakai kemampuan "persempit viewport hingga tabel dapat di-scroll" tanpa nilai tetap. Expected b ("status pin bertahan setelah F5") tidak menyebut cara mengamati status pin; spec mengamati lewat scroll tabel.
  - TC-GS-GSET-93: langkah 1 meminta "geser `Modified By` ke posisi pertama", tetapi bila TC dijalankan berurutan sesudah TC-91 kolom itu sudah di posisi pertama; spec menulis langkah 36 sesuai langkah 1 TC-93 sehingga blok berdiri sendiri.
  - Mekanisme menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE.
