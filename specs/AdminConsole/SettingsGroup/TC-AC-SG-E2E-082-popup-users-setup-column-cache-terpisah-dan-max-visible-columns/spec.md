---
id: TC-AC-SG-E2E-082-popup-users-setup-column-cache-terpisah-dan-max-visible-columns
title: "Popup Users: Setup Column, Cache Terpisah, dan Max Visible Columns"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-302
  - TC-AC-SG-303
  - TC-AC-SG-304
coverage:
  web: automated
---

# Popup Users: Setup Column, Cache Terpisah, dan Max Visible Columns

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Akun kedua (ganti akun pada TC-AC-SG-304): Total Control entitas `Distributor Custom Field` (Pre-setup #44, 12 custom field User aktif sehingga popup Users memiliki 9 kolom ditambah 12 kolom curated) `totalControlCustomField_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CUSTOMFIELD_PASSWORD`.
- State global: Max Visible Columns di System Limits bernilai 20 (default, Pre-setup #34); spec ini tidak mengubahnya.
- Preferensi kolom tabel di browser dihapus di hook `before` dan `after` spec ini (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE (lihat `suite.md`). Spec ini menyimpan konfigurasi kolom popup Users (TC-AC-SG-303).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total User pada baris `Region A`

### TC-AC-SG-302: Setup Column popup Users: kolom default visible dan curated hidden

3. Klik header Actions popup
4. Klik `Setup Column...`
5. Verifikasi kolom default visible: Name, Email, Position, Division, dan Group Role
6. Verifikasi kolom curated tidak tercentang: Activation Status, Temporary User, Temporary Until, TAG, dan satu kolom per custom field aktif
7. Verifikasi trigger Column Visibility tersedia di tabel popup walau tanpa row action

### TC-AC-SG-303: Pengaturan kolom popup Users tersimpan terpisah dan bertahan setelah ditutup

8. Catat daftar kolom tabel utama sebelum Save
9. Centang Activation Status dan hide Division di Setup Column
10. Klik `[Save]`
11. Tutup popup lewat `[✕]`
12. Klik angka Total User pada baris `Region A`
13. Verifikasi Activation Status tampil setelah popup dibuka kembali
14. Verifikasi Division tersembunyi setelah popup dibuka kembali
15. Muat ulang halaman dengan F5
16. Ketik Search `Branch 1` pada toolbar tabel utama, tekan Enter
17. Klik angka Total User pada baris `Branch 1`
18. Verifikasi Activation Status tampil pada popup node `Branch 1`
19. Verifikasi Division tersembunyi pada popup node `Branch 1`
20. Tutup popup lewat `[✕]`
21. Verifikasi kolom tabel utama sama dengan daftar yang dicatat pada langkah 8
22. Klik angka Total Member pada baris `Branch 1`
23. Verifikasi popup Members memuat kolom Entity Name, Type, Relation Status, dan Last Updated tanpa perubahan
24. Tutup popup lewat `[✕]`
25. Klik ikon Changelog pada toolbar
26. Verifikasi modal Changelog memuat tujuh kolom default tanpa perubahan
27. Tutup modal Changelog lewat `[✕]`
28. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

### TC-AC-SG-304: Max Visible Columns di popup Users dengan banyak custom field

29. Ganti akun: Logout, lalu login sebagai Total Control entitas `Distributor Custom Field`
30. Buka halaman `Settings > Group` lewat sidebar
31. Klik angka Total User baris `Default Group`
32. Klik header Actions popup
33. Klik `Setup Column...`
34. Centang seluruh kolom hingga 20 kolom tercentang
35. Hover checkbox kolom ke-21
36. Verifikasi checkbox kolom yang belum dicentang disabled dengan tooltip `Maximum 20 columns can be shown at once. Uncheck another column first.`
37. Verifikasi kolom yang sudah tercentang tidak berubah
38. Tutup Setup Column lewat `[✕]` tanpa `[Save]`
39. Tutup popup lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), langkah 8 (baseline kolom tabel utama), penutupan popup dan modal, Search `Branch 1` sesudah F5 (R-16), klik `(←)` pada Search tabel utama, penutupan Setup Column tanpa menyimpan, dan penutupan popup Users `Distributor Custom Field` di akhir (S-10).
- Spec ini melewati sekitar 35 langkah. Alasan: blok TC-AC-SG-304 memakai akun dan entitas lain dan berdiri sendiri; kegagalan blok TC-AC-SG-302 atau TC-AC-SG-303 tidak membuat blok itu kehilangan makna (bagian 3 butir b, Step ganti akun eksplisit). Ketiga blok satu kelas (Setup Column popup Users).
- Temuan untuk QA:
  - TC-AC-SG-303 menyebut "tidak memengaruhi tabel utama, popup Members, maupun Changelog" tanpa menyebut apa yang diperbandingkan; spec membandingkan daftar kolom default tiap tabel (tabel utama dicatat sebelum Save).
  - TC-AC-SG-304 berlabel Manual Only di TC; spec tetap menuliskannya sebagai langkah (Max Visible Columns 20 adalah state default, Pre-setup #34).
  - TC-AC-SG-304 menyebut "Total User baris `Default Group`" tanpa langkah Search; spec memakai baris itu langsung karena `Distributor Custom Field` bertree kecil.
