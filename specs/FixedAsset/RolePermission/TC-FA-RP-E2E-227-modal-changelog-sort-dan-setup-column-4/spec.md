---
id: TC-FA-RP-E2E-227-modal-changelog-sort-dan-setup-column-4
title: "Modal Changelog: Sort dan Setup Column (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-739
  - TC-FA-RP-740
  - TC-FA-RP-741
  - TC-FA-RP-742
coverage:
  web: automated
---

# Modal Changelog: Sort dan Setup Column (4/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed) dan #37 (Tab Read Only empat baris: Dewi Anggraini, Maya Anggraeni, Yoga Pratama, Gilang Prakoso; tabel lain pada TC 742). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed. Spec ini tidak mengubah data.
- Konfigurasi kolom Setup Column disimpan di browser; langkah 8 mengembalikan konfigurasi ke default lewat `[Reset to Default]` yang menjadi objek uji TC 739, dan hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Kolom bawaan tampil Tab Read Only (TC 742): `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`.

## Test Steps

### Reset to Default (TC 739)

1. Klik ikon Changelog pada toolbar.
2. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
3. Hapus centang kolom `Old Value`.
4. Seret kolom `Action` ke posisi paling akhir pada daftar.
5. Klik ikon Pin pada kolom `Date`.
6. Klik `[Save]`.
7. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
8. Klik `[Reset to Default]`.
9. Klik `[Save]`.
10. Muat ulang halaman (F5), klik ikon Changelog pada toolbar kembali, lalu buka popup Setup Column.
11. Verifikasi kolom `Old Value` tampil kembali dan tercentang.
12. Verifikasi kolom `Action` kembali ke urutan semula.
13. Verifikasi kolom `Date` tidak ter-pin.

### Tutup popup Setup Column membuang perubahan (TC 740)

14. Klik `(X)` untuk menutup popup Setup Column.
15. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
16. Hapus centang kolom `Field`.
17. Klik `(X)`.
18. Verifikasi perubahan preview dibatalkan dan tabel memakai konfigurasi tersimpan terakhir (kolom `Field` tetap tampil).
19. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
20. Hapus centang kolom `Field`.
21. Tekan Esc.
22. Verifikasi perubahan preview dibatalkan dan tabel memakai konfigurasi tersimpan terakhir (kolom `Field` tetap tampil).

### Guard satu kolom tersisa (TC 741)

23. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
24. Hapus centang semua kolom kecuali `Date`.
25. Arahkan kursor ke checkbox kolom terakhir (`Date`).
26. Verifikasi checkbox kolom terakhir Disabled dengan tooltip `At least one column must remain visible.`
27. Klik `(X)` untuk menutup popup Setup Column tanpa menyimpan.

### Konfigurasi kolom tidak memengaruhi tabel lain (TC 742)

28. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
29. Hapus centang kolom `Old Value`, lalu klik `[Save]`.
30. Tutup modal Changelog.
31. Klik Tab `Read Only`.
32. Verifikasi tabel Tab Read Only tetap memakai konfigurasi kolomnya sendiri: kolom `Name`, `Position`, `Division`, `Status`, `Modified By`, dan `Last Updated` tampil.
33. Klik Tab `Total Control`.

## Notes

- Langkah penghubung (S-03): langkah 14 dan 27 (menutup popup Setup Column tanpa menyimpan), 30 (menutup modal), dan 33 (kembali ke Tab `Total Control`). Konfigurasi kolom hasil langkah 29 tidak dipulihkan di dalam spec; hook `after` menghapus preferensi kolom di browser.
- Pada TC 739, 740, 741, dan 742 butir Expected tunggal ditulis sesuai TC; TC 740 ditulis sebagai satu `Verifikasi` per penutupan (langkah 18 dan 22) dan kolom `Field` dipilih sebagai "satu centang".
- Tabel lain pada TC 742 dipilih Tab Read Only (opsi "tab lain" pada TC).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 739 mengasersi persistensi sesudah F5 dalam satu butir; spec mengasersi susunan default pada langkah 11 sampai 13 setelah F5 dan pembukaan ulang popup.
  - TC 740 dan 742 tidak menyebut kolom yang diubah; spec memilih `Field` (TC 740) dan `Old Value` (TC 742).
  - TC 739 sampai 742 tidak menyebut apakah modal Changelog tetap terbuka sesudah `[Save]` Setup Column; spec mengasumsikan modal tetap terbuka.
