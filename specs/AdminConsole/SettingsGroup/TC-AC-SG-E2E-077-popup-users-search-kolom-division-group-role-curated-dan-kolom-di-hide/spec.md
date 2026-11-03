---
id: TC-AC-SG-E2E-077-popup-users-search-kolom-division-group-role-curated-dan-kolom-di-hide
title: "Popup Users: Search Kolom Division, Group Role, Curated, dan Kolom di-Hide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-281
  - TC-AC-SG-282
  - TC-AC-SG-283
  - TC-AC-SG-284
coverage:
  web: automated
---

# Popup Users: Search Kolom Division, Group Role, Curated, dan Kolom di-Hide

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Data tambahan (disediakan tim FE): sedikitnya satu user di `Region A` dengan Division yang mengandung `Finance`, sedikitnya satu user dengan Activation Status `Pending Activation` atau `Pending Email Confirmation`, dan sedikitnya satu user yang dipasangi TAG (kode TAG user uji). Pre-setup #18 hanya menyebut Division `Operations` untuk `Andi Pratama` dan tidak menyebut user Pending atau ber-TAG (lihat Temuan untuk QA).
- Perubahan Column Visibility popup dipulihkan lewat langkah penghubung eksplisit (Overlay tidak memakai `[Save]`).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total User pada baris `Region A`

### TC-AC-SG-281: Search popup Users by kolom Division

3. Ketik Search `finance` pada toolbar popup, tekan Enter
4. Verifikasi baris user dengan Division yang mengandung `Finance` tampil
5. Ganti isi kotak search dengan `FINANCE`, tekan Enter
6. Verifikasi daftar baris yang tampil identik dengan hasil Search `finance`
7. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
8. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
9. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel

### TC-AC-SG-282: Search popup Users by kolom Group Role

10. Ketik Search `group manager` pada toolbar popup, tekan Enter
11. Verifikasi baris `Andi Pratama` tampil
12. Ganti isi kotak search dengan `GROUP MANAGER`, tekan Enter
13. Verifikasi daftar baris yang tampil identik dengan hasil Search `group manager`
14. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
15. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
16. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel

### TC-AC-SG-283: Search kolom curated TAG, Activation Status, dan Temporary User setelah di-unhide

17. Buka Overlay Column Visibility popup dan centang TAG, Activation Status, dan Temporary User
18. Ketik Search `pending` pada toolbar popup, tekan Enter
19. Verifikasi baris user dengan Activation Status `Pending Activation` atau `Pending Email Confirmation` tampil
20. Ganti isi kotak search dengan kode TAG user uji, tekan Enter
21. Verifikasi baris user yang dipasangi TAG tersebut tampil
22. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel
23. Buka Overlay Column Visibility popup dan hilangkan centang TAG, Activation Status, dan Temporary User

### TC-AC-SG-284: Search popup tidak mencari kolom Position yang sedang di-hide

24. Hide kolom Position pada Overlay Column Visibility popup
25. Ketik Search `Manager` pada toolbar popup, tekan Enter
26. Verifikasi tidak ada baris yang cocok dari kolom Position: empty state `No results found` dengan Description `Try adjusting your search or filter.`
27. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel
28. Tampilkan kembali kolom Position pada Overlay Column Visibility popup
29. Tutup popup lewat `[✕]`
30. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), klik `(←)` pada Search popup di akhir tiap TC (S-09), pemulihan Column Visibility (centang TAG, Activation Status, Temporary User dihilangkan; kolom Position ditampilkan kembali), penutupan popup, dan klik `(←)` pada Search tabel utama di akhir. Urutan TC: 281, 282, 283, 284 (TC-AC-SG-284 terakhir karena menyembunyikan kolom).
- Temuan untuk QA:
  - Pre-setup #18 tidak memuat user ber-Division `Finance`, user Pending, maupun user ber-TAG di `Region A`; TC-AC-SG-281 dan TC-AC-SG-283 mengandaikannya ("kode TAG user uji" tidak tertulis). Kebutuhan ditulis sebagai data tambahan yang disediakan tim FE.
  - TC-AC-SG-284: kata `Manager` cocok dengan Group Role `Group Manager` (`Andi Pratama`, kolom Group Role tampil); bila Group Role searchable (TC-AC-SG-282), hasil Search tidak kosong dan Expected "tidak ada baris yang cocok" tidak tercapai. Spec mengikuti TC dan mengasersi empty state.
  - TC-AC-SG-283 tidak menyebut apakah perubahan Column Visibility melalui Overlay dipersistenkan; spec memulihkannya secara eksplisit.
