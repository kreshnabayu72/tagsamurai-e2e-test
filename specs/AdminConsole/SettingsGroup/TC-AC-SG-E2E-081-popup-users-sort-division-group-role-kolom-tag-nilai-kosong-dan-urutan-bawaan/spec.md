---
id: TC-AC-SG-E2E-081-popup-users-sort-division-group-role-kolom-tag-nilai-kosong-dan-urutan-bawaan
title: "Popup Users: Sort Division dan Group Role, Kolom TAG, Nilai Kosong, dan Urutan Bawaan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-299
  - TC-AC-SG-300
  - TC-AC-SG-301
  - TC-AC-SG-305
  - TC-AC-SG-306
coverage:
  web: automated
---

# Popup Users: Sort Division dan Group Role, Kolom TAG, Nilai Kosong, dan Urutan Bawaan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Data tambahan (disediakan tim FE): sedikitnya dua nilai Division distinct di antara user `Region A`, sedikitnya satu user yang dipasangi TAG (kode TAG user uji), sedikitnya satu user bukan Temporary User, dan sedikitnya satu user yang belum dipasangkan TAG. Pre-setup #18 hanya menyebut Division `Operations` untuk `Andi Pratama` (lihat Temuan untuk QA).
- Perubahan Column Visibility popup dipulihkan lewat langkah penghubung eksplisit (Overlay tidak memakai `[Save]`).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total User pada baris `Region A`

### TC-AC-SG-306: Urutan bawaan popup Users adalah Name A-Z case-insensitive

3. Verifikasi baris terurut `Andi Pratama`, `Budi Santoso`, `Dewi Lestari`, `Rina Wijaya`, `Sari Dewi` (A-Z, tanpa membedakan huruf besar kecil)

### TC-AC-SG-299: Sort popup Users kolom Division: siklus tiga klik

4. Klik header Division sekali
5. Verifikasi klik pertama mengurutkan Division ascending (A-Z)
6. Klik header Division kedua kali
7. Verifikasi klik kedua mengurutkan Division descending
8. Klik header Division ketiga kali
9. Verifikasi klik ketiga netral kembali ke Name A-Z

### TC-AC-SG-300: Sort popup Users kolom Group Role: siklus tiga klik

10. Klik header Group Role sekali
11. Verifikasi klik pertama mengurutkan Group Role ascending (A-Z)
12. Klik header Group Role kedua kali
13. Verifikasi klik kedua mengurutkan Group Role descending
14. Klik header Group Role ketiga kali
15. Verifikasi klik ketiga netral kembali ke Name A-Z

### TC-AC-SG-301: Kolom TAG tidak memiliki ikon sort

16. Centang kolom TAG di Overlay Column Visibility popup
17. Verifikasi header kolom lain pada tabel popup Users tampil
18. Verifikasi header TAG tidak memiliki ikon sort (not sortable)
19. Ketik Search kode TAG user uji pada toolbar popup, tekan Enter
20. Verifikasi baris user yang dipasangi TAG tersebut tampil (kolom TAG searchable)
21. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel
22. Hilangkan centang kolom TAG di Overlay Column Visibility popup

### TC-AC-SG-305: Nilai kosong kolom Temporary Until dan TAG tampil sebagai tanda strip

23. Centang kolom Temporary Until dan TAG di Overlay Column Visibility popup
24. Verifikasi sel Temporary Until baris user bukan Temporary User menampilkan `—`
25. Verifikasi sel TAG baris user yang belum dipasangkan TAG menampilkan `—`
26. Hilangkan centang kolom Temporary Until dan TAG di Overlay Column Visibility popup
27. Tutup popup lewat `[✕]`
28. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), klik `(←)` pada Search popup, pemulihan Column Visibility (kolom TAG, Temporary Until dihilangkan centangnya), penutupan popup, dan klik `(←)` pada Search tabel utama di akhir. Tiap TC sort berakhir pada sort netral (S-09).
- Urutan TC dalam spec: 306, 299, 300, 301, 305 (urutan bawaan diasersi sebelum sort mana pun; TC-AC-SG-301 dan TC-AC-SG-305 mengubah Column Visibility sehingga paling akhir, S-10).
- Temuan untuk QA:
  - TC-AC-SG-301 langkah 5 mencari dengan kode TAG yang tampil pada salah satu baris; kode TAG user uji tidak tertulis di Pre-setup, spec memakai kode TAG user yang dipasangi TAG dari data tambahan tim FE.
  - TC-AC-SG-300: urutan Group Role ditulis "A-Z berdasarkan label badge atau jumlah" tanpa menyatakan mana yang berlaku untuk nilai `2 roles`; spec mengasersi urutan A-Z menurut label teks sel.
  - TC-AC-SG-299: Pre-setup #18 hanya menyebut Division `Operations` untuk `Andi Pratama`; sort Division membutuhkan sedikitnya dua nilai distinct (S-11), disediakan tim FE sebagai data tambahan.
  - TC-AC-SG-305 menyebut "user yang bukan Temporary User dan belum dipasangkan TAG" tanpa nama user; spec memakai user tersebut dari data tambahan tim FE.
