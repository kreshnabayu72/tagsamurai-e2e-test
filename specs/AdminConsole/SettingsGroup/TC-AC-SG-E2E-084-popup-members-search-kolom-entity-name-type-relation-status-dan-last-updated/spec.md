---
id: TC-AC-SG-E2E-084-popup-members-search-kolom-entity-name-type-relation-status-dan-last-updated
title: "Popup Members: Search Kolom Entity Name, Type, Relation Status, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-311
  - TC-AC-SG-312
  - TC-AC-SG-313
  - TC-AC-SG-314
coverage:
  web: automated
---

# Popup Members: Search Kolom Entity Name, Type, Relation Status, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total Member pada baris `Region A`

### TC-AC-SG-311: Search popup Members by kolom Entity Name

3. Ketik Search `alpha` pada toolbar popup, tekan Enter
4. Verifikasi baris `Distributor Alpha` tampil
5. Ganti isi kotak search dengan `ALPHA`, tekan Enter
6. Verifikasi daftar baris yang tampil identik dengan hasil Search `alpha`
7. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
8. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
9. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel

### TC-AC-SG-312: Search popup Members by kolom Type

10. Ketik Search `distributor` pada toolbar popup, tekan Enter
11. Verifikasi baris `Distributor Alpha`, `Distributor Beta`, `Distributor Delta`, dan `Distributor Gamma` tampil karena kolom Type bernilai `Distributor`
12. Ganti isi kotak search dengan `DISTRIBUTOR`, tekan Enter
13. Verifikasi daftar baris yang tampil identik dengan hasil Search `distributor`
14. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
15. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
16. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel

### TC-AC-SG-313: Search popup Members by kolom Relation Status

17. Ketik Search `suspended` pada toolbar popup, tekan Enter
18. Verifikasi baris `Distributor Beta` dan `Distributor Gamma` tampil
19. Ganti isi kotak search dengan `SUSPENDED`, tekan Enter
20. Verifikasi daftar baris yang tampil identik dengan hasil Search `suspended`
21. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
22. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
23. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel

### TC-AC-SG-314: Search popup Members tidak mencocokkan kolom Last Updated

24. Salin teks Last Updated baris pertama, tempel ke Search pada toolbar popup, tekan Enter
25. Verifikasi tidak ada baris yang cocok: empty state `No results found` dengan Description `Try adjusting your search or filter.`
26. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel
27. Tutup popup lewat `[✕]`
28. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), klik `(←)` pada Search popup di akhir tiap TC (S-09), penutupan popup, dan klik `(←)` pada Search tabel utama di akhir. Popup dibuka satu kali untuk keempat TC.
- Temuan untuk QA:
  - TC-AC-SG-312 dan TC-AC-SG-313: Search `distributor` dan `suspended` diasersi sebagai keberadaan baris yang disebut Expected; TC tidak menyatakan baris lain tidak tampil.
  - TC-AC-SG-314: kolom tanggal hanya lewat Filter (penjelasan di Expected); pencocokan Last Updated lewat Filter diasersi di spec 085 (TC-AC-SG-318).
  - Expected b ("hasil identik pada huruf kapital") tidak menyebut apa yang diperbandingkan; spec membandingkan daftar baris dengan hasil Search huruf kecil.
