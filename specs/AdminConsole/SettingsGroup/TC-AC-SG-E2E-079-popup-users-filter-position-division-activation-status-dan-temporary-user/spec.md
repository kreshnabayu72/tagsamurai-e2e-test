---
id: TC-AC-SG-E2E-079-popup-users-filter-position-division-activation-status-dan-temporary-user
title: "Popup Users: Filter Position, Division, Activation Status, dan Temporary User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-290
  - TC-AC-SG-291
coverage:
  web: automated
---

# Popup Users: Filter Position, Division, Activation Status, dan Temporary User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Data tambahan (disediakan tim FE): sedikitnya satu user dengan Activation Status `Activated` dan sedikitnya satu Temporary User di `Region A` (Pre-setup #18 tidak menyebut Temporary User; lihat Temuan untuk QA).
- Data tambahan (disediakan tim FE): sedikitnya satu user di `Region A` ber-status `Pending Activation` dan satu `Pending Email Confirmation`. Pre-setup #18 tidak menyebut user berstatus Pending (lihat Temuan untuk QA).
- Perubahan Column Visibility popup dipulihkan lewat langkah penghubung eksplisit (Overlay tidak memakai `[Save]`).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total User pada baris `Region A`
3. Buka Overlay Column Visibility popup dan centang Activation Status dan Temporary User

### TC-AC-SG-290: Opsi Position dan Division diambil dari data popup dan filter dapat dikombinasikan

4. Catat nilai distinct kolom Position dan Division pada baris popup `Region A`
5. Klik ikon Filter pada toolbar popup
6. Buka dropdown Position
7. Verifikasi opsi Position hanya nilai distinct yang dicatat pada langkah 4
8. Buka dropdown Division
9. Verifikasi opsi Division hanya nilai distinct yang dicatat pada langkah 4
10. Pilih Position `Manager` dan Division `Operations` lalu klik `[Apply]`
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi setiap baris yang tampil bernilai Position `Manager` dan Division `Operations` (AND antar field, OR dalam field)
13. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter

### TC-AC-SG-291: Filter Activation Status dan Temporary User

14. Buka dropdown Activation Status
15. Verifikasi opsi Activation Status mengikuti nilai yang ada pada data: `Activated`, `Pending Activation`, dan `Pending Email Confirmation`
16. Pilih Activation Status `Activated` lalu klik `[Apply]`
17. Verifikasi sedikitnya satu baris tampil
18. Verifikasi setiap baris yang tampil bernilai Activation Status `Activated`
19. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter
20. Buka dropdown Temporary User
21. Verifikasi opsi Temporary User `Yes` dan `No`
22. Pilih Temporary User `Yes` lalu klik `[Apply]`
23. Verifikasi sedikitnya satu baris tampil
24. Verifikasi setiap baris yang tampil bernilai Temporary User `Yes`
25. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter
26. Buka Overlay Column Visibility popup dan hilangkan centang Activation Status dan Temporary User
27. Tutup popup lewat `[✕]`
28. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), langkah 3 (menampilkan kolom Activation Status dan Temporary User agar hasil filter dapat dibaca), pembersihan filter di akhir tiap blok (S-09), pemulihan Column Visibility, penutupan popup, dan klik `(←)` di akhir.
- TC-AC-SG-292 dan TC-AC-SG-293 ada di spec TC-AC-SG-E2E-115.
- Temuan untuk QA:
  - Perilaku panel Filter sesudah `[Apply]` di popup/modal tidak dinyatakan PRD; spec mengasumsikan panel tetap terbuka (pola spec 051 sampai 054 dan 070), sehingga klik ikon Filter berikutnya tidak diulang. Perlu konfirmasi FE.
  - Pre-setup #18 tidak menyebut Temporary User maupun user berstatus Pending di `Region A`; opsi Activation Status dibaca sebagai tiga nilai yang tertulis di Expected ("mengikuti nilai yang ada pada data"), dan baris Temporary User `Yes` mengandaikan data tambahan dari tim FE.
  - TC-AC-SG-290 menyebut "pilih satu Position dan satu Division" tanpa nilai; spec memakai Position `Manager` dan Division `Operations` (Pre-setup #18, `Andi Pratama`).
