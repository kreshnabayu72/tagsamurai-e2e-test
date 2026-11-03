---
id: TC-AC-SG-E2E-086-popup-members-sort-keempat-kolom-dan-setup-column
title: "Popup Members: Sort Keempat Kolom dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-320
  - TC-AC-SG-321
  - TC-AC-SG-322
  - TC-AC-SG-323
  - TC-AC-SG-324
coverage:
  web: automated
---

# Popup Members: Sort Keempat Kolom dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Preferensi kolom tabel di browser dihapus di hook `before` dan `after` spec ini (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE (lihat `suite.md`). Spec ini menyimpan konfigurasi kolom popup Members (TC-AC-SG-324).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total Member pada baris `Region A`

### TC-AC-SG-320: Sort popup Members kolom Entity Name: siklus tiga klik

3. Klik header Entity Name sekali
4. Verifikasi klik pertama mengurutkan Entity Name ascending (A-Z case-insensitive)
5. Klik header Entity Name kedua kali
6. Verifikasi klik kedua mengurutkan Entity Name descending
7. Klik header Entity Name ketiga kali
8. Verifikasi klik ketiga netral kembali ke Entity Name A-Z

### TC-AC-SG-321: Sort popup Members kolom Type: siklus tiga klik

9. Klik header Type sekali
10. Verifikasi klik pertama mengurutkan Type ascending (A-Z berdasarkan label badge)
11. Klik header Type kedua kali
12. Verifikasi klik kedua mengurutkan Type descending
13. Klik header Type ketiga kali
14. Verifikasi klik ketiga netral kembali ke Entity Name A-Z

### TC-AC-SG-322: Sort popup Members kolom Relation Status: siklus tiga klik

15. Klik header Relation Status sekali
16. Verifikasi klik pertama mengurutkan Relation Status ascending (A-Z berdasarkan label badge)
17. Klik header Relation Status kedua kali
18. Verifikasi klik kedua mengurutkan Relation Status descending
19. Klik header Relation Status ketiga kali
20. Verifikasi klik ketiga netral kembali ke Entity Name A-Z

### TC-AC-SG-323: Sort popup Members kolom Last Updated: siklus tiga klik

21. Klik header Last Updated sekali
22. Verifikasi klik pertama mengurutkan Last Updated ascending (Oldest First)
23. Klik header Last Updated kedua kali
24. Verifikasi klik kedua mengurutkan Last Updated descending
25. Klik header Last Updated ketiga kali
26. Verifikasi klik ketiga netral kembali ke Entity Name A-Z

### TC-AC-SG-324: Setup Column popup Members: keempat kolom default visible dan cache terpisah

27. Klik header Actions popup lalu `Setup Column...`
28. Verifikasi keempat kolom default (Entity Name, Type, Relation Status, Last Updated) Visible dan Hideable
29. Hide Last Updated lalu klik `[Save]`
30. Tutup popup lewat `[✕]`
31. Klik angka Total Member pada baris `Region A`
32. Verifikasi kolom Last Updated tetap tersembunyi setelah popup dibuka kembali
33. Tutup popup lewat `[✕]`
34. Klik angka Total User pada baris `Region A`
35. Verifikasi popup Users memuat kolom default Name, Email, Position, Division, dan Group Role tanpa perubahan (tidak memengaruhi tabel lain)
36. Tutup popup lewat `[✕]`
37. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), penutupan popup, dan klik `(←)` pada Search tabel utama di akhir. Tiap TC sort berakhir pada sort netral (S-09). Popup dibuka satu kali untuk kelima TC sampai TC-AC-SG-324 menutupnya.
- Spec ini melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (popup Members pada node yang sama) dan blok sort (320 sampai 323) berdiri sendiri dari blok Setup Column (324), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; tiap sort adalah tiga klik dengan tiga Verifikasi (S-01).
- Temuan untuk QA:
  - TC-AC-SG-321: keempat baris `Region A` bertipe `Distributor` sehingga hasil sort Type tidak memiliki dua nilai distinct (S-11, S-14); urutan tidak teruji secara bermakna. Usulan: asersi indikator sort saja, atau gunakan node dengan dua tipe berbeda.
  - TC-AC-SG-323 menulis "ascending (Oldest First lalu Newest First)" untuk klik pertama; spec mengasersi klik pertama Oldest First (ascending) dan klik kedua descending.
  - TC-AC-SG-324 menyebut "tanpa memengaruhi tabel lain" tanpa menyebut tabel yang dimaksud; spec membandingkan popup Users (kolom default).
