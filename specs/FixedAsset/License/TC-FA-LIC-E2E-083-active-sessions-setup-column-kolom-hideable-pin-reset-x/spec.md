---
id: TC-FA-LIC-E2E-083-active-sessions-setup-column-kolom-hideable-pin-reset-x
title: "Active Sessions: Setup Column Pin dan Unpin, Reset to Default, X atau Esc, dan Satu Kolom Tersisa"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-286
  - TC-FA-LIC-290
  - TC-FA-LIC-291
  - TC-FA-LIC-292
coverage:
  web: automated
---

# Active Sessions: Setup Column Pin dan Unpin, Reset to Default, X atau Esc, dan Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #26 (fixture tabel sesi, dipulihkan fixture BE di hook `before`): tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso pada client Paid Pre-setup #1; Online Users 5/25. Susunan default modul (9 kolom tampil): `User Name`, `Email`, `Position`, `Division`, `IP Address`, `Device / OS`, `Browser`, `Login Time`, `Last Activity`. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.*` (berkas fixture belum ada, disiapkan tim FE).
- Data Dinamis: tidak ada.
- Tabel "Kolom Hideable Visible default untuk Pin" (parameter langkah 25 sampai 32): `User Name`, `Email`, `Position`, `Division`, `IP Address`, `Device / OS`, `Browser`, `Login Time`, `Last Activity`.
- Konfigurasi kolom: spec ini menyimpan Setup Column di browser. Konfigurasi dikembalikan ke susunan default oleh langkah `[Reset to Default]` dan `[Save]` di akhir spec, dan hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26; pemulihan konfigurasi kolom. Kemampuan teknis: seret-dan-lepas item daftar kolom, mengatur lebar viewport agar tabel dapat digeser horizontal, mengirim tombol `Esc`, membaca tooltip checkbox disabled.
- State yang diubah dan dipulihkan: viewport browser disempitkan pada langkah 24 agar tabel dapat digeser horizontal (pilihan spec; TC hanya menulis "geser tabel horizontal") dan dipulihkan pada langkah 33.

## Test Steps

### TC-FA-LIC-292: Satu kolom visible tersisa tidak dapat di-uncheck

1. Klik tab Concurrent User
2. Buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
3. Hilangkan centang semua kolom kecuali `User Name`
4. Coba hilangkan centang kolom terakhir `User Name`
5. Verifikasi checkbox kolom terakhir disabled
6. Arahkan kursor ke checkbox itu
7. Verifikasi tooltip `At least one column must remain visible.`
8. Klik `(×)` untuk menutup popup tanpa menyimpan

### TC-FA-LIC-291: X atau Esc membuang perubahan

9. Buka Popup Setup Column, hilangkan centang `Email`
10. Klik `(×)`
11. Verifikasi popup tertutup
12. Verifikasi tabel memakai konfigurasi tersimpan terakhir: kolom `Email` masih tampil
13. Buka Popup Setup Column, hilangkan centang `Email`
14. Tekan `Esc`
15. Verifikasi popup tertutup
16. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir: kolom `Email` masih tampil

### TC-FA-LIC-290: Reset to Default

17. Buka Popup Setup Column, hilangkan centang `Email`, dan seret `Browser` ke posisi pertama
18. Klik `[Reset to Default]`
19. Verifikasi Live Preview kembali ke susunan default modul: `User Name`, `Email`, `Position`, `Division`, `IP Address`, `Device / OS`, `Browser`, `Login Time`, `Last Activity`
20. Klik `[Save]`
21. Verifikasi susunan default tersimpan pada tabel
22. Muat ulang halaman (F5)
23. Verifikasi susunan default bertahan setelah F5

### TC-FA-LIC-286: Pin dan Unpin per kelas kolom Hideable Visible default

24. Sempitkan viewport browser sehingga tabel dapat digeser horizontal
25. Untuk setiap kolom pada tabel "Kolom Hideable Visible default untuk Pin" (langkah 25 sampai 32): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
26. Klik ikon Pin kolom itu, lalu klik `[Save]`
27. Geser tabel secara horizontal
28. Verifikasi kolom itu membeku (sticky) di kiri saat scroll horizontal
29. Muat ulang halaman (F5), lalu geser tabel secara horizontal
30. Verifikasi kolom itu tetap membeku (sticky) di kiri setelah F5
31. Buka Popup Setup Column, klik ikon Pin kolom itu untuk Unpin, lalu klik `[Save]`
32. Verifikasi kolom itu tidak lagi membeku (sticky) setelah Unpin
33. Pulihkan viewport browser ke ukuran semula

## Notes

- Langkah penghubung tanpa `Verifikasi`: menutup popup dengan `(×)` di TC-FA-LIC-292 (S-09), menyimpan tiap iterasi Pin, menyempitkan viewport (langkah 24) dan memulihkannya (langkah 33) agar tabel dapat digeser horizontal pada TC-FA-LIC-286, dan memulihkan konfigurasi lewat `[Reset to Default]` lalu `[Save]` pada TC-FA-LIC-290 sebagai penutup. Setup Column tidak memakai "Tunggu aksi selesai" karena aksi sisi klien (butir 8 bagian 8b).
- Blok ulang: langkah 25 sampai 32 dijalankan 9 kali. Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: semua blok satu popup Setup Column pada satu tabel dan satu dataset, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna; Pin dilepas di akhir tiap iterasi sehingga iterasi saling lepas.
- TC-FA-LIC-291 menyebut "klik `(×)` atau tekan Esc" tanpa menyebut salah satu; spec menjalankan keduanya berurutan sebagai dua varian.
- Temuan untuk QA: TC-FA-LIC-290 langkah 2 ("ubah visibilitas dan urutan beberapa kolom") tidak menyebut kolom yang diubah; spec memakai menyembunyikan `Email` dan menyeret `Browser` ke posisi pertama. TC-FA-LIC-286 langkah "geser tabel horizontal" mengandaikan tabel lebih lebar dari viewport tanpa menyebut lebar viewport; spec menyempitkan viewport pada langkah 24 dan memulihkannya pada langkah 33 (kemampuan dicatat di Prerequisites).
