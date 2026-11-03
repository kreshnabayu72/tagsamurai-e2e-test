---
id: TC-AC-SG-E2E-076-popup-users-search-kolom-name-email-dan-position
title: "Popup Users: Search Kolom Name, Email, dan Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-278
  - TC-AC-SG-279
  - TC-AC-SG-280
coverage:
  web: automated
---

# Popup Users: Search Kolom Name, Email, dan Position

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total User pada baris `Region A`

### TC-AC-SG-278: Search popup Users by kolom Name

3. Ketik Search `sari` pada toolbar popup, tekan Enter
4. Verifikasi baris `Sari Dewi` tampil
5. Ganti isi kotak search dengan `SARI`, tekan Enter
6. Verifikasi daftar baris yang tampil identik dengan hasil Search `sari`
7. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
8. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
9. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel

### TC-AC-SG-279: Search popup Users by kolom Email

10. Ketik Search `andi@` pada toolbar popup, tekan Enter
11. Verifikasi baris `Andi Pratama` tampil
12. Ganti isi kotak search dengan `ANDI@`, tekan Enter
13. Verifikasi daftar baris yang tampil identik dengan hasil Search `andi@`
14. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
15. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
16. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel

### TC-AC-SG-280: Search popup Users by kolom Position

17. Ketik Search `manager` pada toolbar popup, tekan Enter
18. Verifikasi baris user dengan Position yang mengandung `Manager` tampil
19. Ganti isi kotak search dengan `MANAGER`, tekan Enter
20. Verifikasi daftar baris yang tampil identik dengan hasil Search `manager`
21. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
22. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
23. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel
24. Tutup popup lewat `[✕]`
25. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), klik `(←)` pada kotak Search popup di akhir tiap TC (S-09), penutupan popup, dan klik `(←)` pada Search tabel utama di akhir. Popup dibuka satu kali untuk ketiga TC.
- Temuan untuk QA:
  - TC-AC-SG-280: kata `manager` juga cocok dengan nilai Group Role `Group Manager` (`Andi Pratama`), sehingga hasil Search tidak hanya dari kolom Position; spec mengasersi baris user dengan Position yang mengandung `Manager` tampil (Pre-setup #18: Position `Manager` hanya tertulis untuk `Andi Pratama`).
  - Expected b ("hasil identik pada huruf kapital") tidak menyebut apa yang diperbandingkan; spec membandingkan daftar baris dengan hasil Search huruf kecil.
