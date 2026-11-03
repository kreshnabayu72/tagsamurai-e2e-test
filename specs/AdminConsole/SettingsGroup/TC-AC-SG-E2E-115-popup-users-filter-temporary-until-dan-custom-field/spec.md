---
id: TC-AC-SG-E2E-115-popup-users-filter-temporary-until-dan-custom-field
title: "Popup Users: Filter Temporary Until, Custom Field Aktif, dan Kolom Curated Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-292
  - TC-AC-SG-293
coverage:
  web: automated
---

# Popup Users: Filter Temporary Until, Custom Field Aktif, dan Kolom Curated Custom Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Data tambahan (disediakan tim FE): sedikitnya satu Temporary User di `Region A` dengan tanggal Temporary Until diketahui, sedikitnya satu user non-Temporary, dan sedikitnya satu custom field aktif bertipe Dropdown dengan sedikitnya satu user bernilai pilihan (Pre-setup #18 tidak memuatnya; lihat Temuan untuk QA).
- Perubahan Column Visibility popup dipulihkan lewat langkah penghubung eksplisit (Overlay tidak memakai `[Save]`).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total User pada baris `Region A`
3. Buka Overlay Column Visibility popup dan centang Temporary Until

### TC-AC-SG-292: Filter Temporary Until memakai date range inklusif

4. Klik ikon Filter pada toolbar popup
5. Pilih rentang Temporary Until yang mencakup tanggal satu Temporary User uji lalu klik `[Apply]`
6. Verifikasi sedikitnya satu baris tampil
7. Verifikasi setiap baris yang tampil adalah Temporary User dengan Temporary Until dalam rentang yang dipilih
8. Klik ikon Filter lalu klik `[Clear Field]` dan `[Apply]` untuk membersihkan filter
9. Verifikasi sel Temporary Until baris user non-Temporary menampilkan `—`

### TC-AC-SG-293: Filter custom field aktif dan kolom curated custom field

10. Verifikasi kolom custom field Dropdown tidak tampil secara default
11. Klik ikon Filter pada toolbar popup
12. Pilih satu nilai pada field custom field Dropdown lalu klik `[Apply]`
13. Buka Overlay Column Visibility popup dan centang kolom custom field tersebut
14. Verifikasi kolom custom field muncul setelah dicentang
15. Verifikasi sedikitnya satu baris tampil
16. Verifikasi setiap baris yang tampil bernilai pilihan pada kolom custom field tersebut
17. Klik ikon Filter lalu klik `[Clear Field]` dan `[Apply]` untuk membersihkan filter
18. Buka Overlay Column Visibility popup dan hilangkan centang kolom custom field dan Temporary Until
19. Tutup popup lewat `[✕]`
20. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), langkah 3 (menampilkan kolom Temporary Until agar hasil filter dapat dibaca), pembersihan filter di akhir tiap blok (S-09), pemulihan Column Visibility, penutupan popup, dan klik `(←)` di akhir.
- Pembagian TC lintas spec: TC-AC-SG-290 dan TC-AC-SG-291 ada di spec TC-AC-SG-E2E-079.
- Temuan untuk QA:
  - TC-AC-SG-292 mengandaikan Temporary User uji tanpa tanggal; Pre-setup #18 tidak memuat Temporary User maupun nilai Temporary Until. Spec memakai tanggal user uji yang disediakan tim FE.
  - TC-AC-SG-293 menyebut "field custom field Dropdown" tanpa nama dan nilai; Pre-setup #16 sampai #20 tidak memuat custom field entitas Principal. Spec mengasersi tanpa nama literal.
  - TC-AC-SG-293: Expected "kolom custom field tidak tampil secara default" diasersi sebelum dicentang; tabel yang sudah tampil menjadi anchor.
