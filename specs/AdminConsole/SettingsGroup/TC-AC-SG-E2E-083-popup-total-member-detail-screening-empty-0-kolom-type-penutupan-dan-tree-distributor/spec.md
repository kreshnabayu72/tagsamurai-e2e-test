---
id: TC-AC-SG-E2E-083-popup-total-member-detail-screening-empty-0-kolom-type-penutupan-dan-tree-distributor
title: "Popup Total Member Detail: Screening, Empty 0, Kolom Type, Penutupan, dan Tree Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-307
  - TC-AC-SG-308
  - TC-AC-SG-309
  - TC-AC-SG-310
  - TC-AC-SG-397
coverage:
  web: automated
---

# Popup Total Member Detail: Screening, Empty 0, Kolom Type, Penutupan, dan Tree Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Akun kedua (ganti akun pada TC-AC-SG-397): Total Control entitas `Distributor Anggota` (Pre-setup #45, tree milik Distributor: `Default Group` dan `Wilayah Timur` dengan 4 anggota langsung `Client Alpha` Client Active, `Client Beta` Client Suspended, `Partner Delta` Partner Active, `Partner Gamma` Partner Suspended) `totalControlAnggota_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_ANGGOTA_PASSWORD`.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter

### TC-AC-SG-307: Screening Popup Total Member Detail

2. Klik angka Total Member pada baris `Region A`
3. Verifikasi Header popup: Title `Members` tampil
4. Verifikasi Header popup: ikon close `[✕]` tampil
5. Verifikasi identitas record berupa teks polos satu baris `Region A (4)` di bawah title dan di atas toolbar
6. Verifikasi Body: toolbar Search dan Filter tampil
7. Verifikasi tabel memuat kolom Entity Name, Type, Relation Status, Last Updated serta kolom Actions kosong
8. Verifikasi tabel memuat 4 baris bertipe Distributor: `Distributor Alpha` (Active), `Distributor Beta` (Suspended), `Distributor Delta` (Active), `Distributor Gamma` (Suspended)
9. Verifikasi Footer: Pagination tampil

### TC-AC-SG-309: Kolom Type menampilkan tipe sah pohon Principal (Distributor) sebagai badge

10. Verifikasi kolom Type tampil sebagai badge `Distributor` pada keempat baris
11. Verifikasi kolom Relation Status tampil sebagai badge nilai modul pemilik entitas (`Active` dan `Suspended`)

### TC-AC-SG-310: Popup Members ditutup lewat ikon close atau Esc

12. Klik `[✕]`
13. Verifikasi popup tertutup
14. Klik angka Total Member pada baris `Region A`
15. Verifikasi tidak ada tombol teks `Close`
16. Tekan Esc
17. Verifikasi popup tertutup

### TC-AC-SG-308: Popup Members dengan 0 entitas tetap terbuka dengan empty state

18. Ganti isi kotak search tabel utama dengan `Finance Dept`, tekan Enter
19. Klik angka Total Member baris `Finance Dept`
20. Verifikasi popup terbuka dengan teks identitas `Head Office > Finance Dept (0)`
21. Verifikasi empty state standar tampil tanpa baris
22. Verifikasi popup tidak menampilkan error
23. Tutup popup lewat `[✕]`
24. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

### TC-AC-SG-397: Popup Members pada tree milik Distributor hanya memuat tipe sah Partner dan Client

25. Ganti akun: Logout, lalu login sebagai Total Control entitas `Distributor Anggota`
26. Buka halaman `Settings > Group` lewat sidebar
27. Verifikasi Total Member pada baris `Wilayah Timur` bernilai 4
28. Klik angka Total Member pada baris `Wilayah Timur`
29. Verifikasi teks identitas popup `Wilayah Timur (4)`
30. Verifikasi popup memuat `Client Alpha` (Client, Active), `Client Beta` (Client, Suspended), `Partner Delta` (Partner, Active), dan `Partner Gamma` (Partner, Suspended)
31. Verifikasi kolom Type hanya bernilai `Client` atau `Partner`
32. Klik ikon Filter pada toolbar popup
33. Buka dropdown Type
34. Verifikasi opsi Type hanya `Client` dan `Partner` (tanpa `Distributor`)
35. Pilih `Partner` lalu klik `[Apply]`
36. Verifikasi baris `Partner Delta` dan `Partner Gamma` tampil
37. Tutup popup lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), Search `Finance Dept` (R-16), penutupan popup, dan klik `(←)` pada Search tabel utama sebelum ganti akun.
- Spec ini melewati sekitar 35 langkah. Alasan: blok TC-AC-SG-397 memakai akun dan entitas lain sesudah Step ganti akun eksplisit dan berdiri sendiri, sehingga kegagalan blok TC-AC-SG-307 sampai TC-AC-SG-308 tidak membuatnya kehilangan makna (bagian 3 butir b). Seluruh blok satu kelas (popup Members, baca saja).
- Urutan TC dalam spec: 307, 309, 310, 308, 397 (TC-AC-SG-309 memakai popup yang sudah terbuka dari TC-AC-SG-307; TC-AC-SG-397 memakai akun lain sehingga paling akhir).
- Temuan untuk QA:
  - TC-AC-SG-308 tidak menulis judul dan deskripsi empty state "standar" untuk popup dengan 0 entitas; spec mengasersi empty state standar tanpa teks literal.
  - TC-AC-SG-308 tidak menyebut cara menemukan baris `Finance Dept` (level 2); spec memakai Search tabel utama (R-16).
  - TC-AC-SG-397 menyebut "Total Member pada baris `Wilayah Timur`" tanpa Search; tree `Distributor Anggota` hanya berisi dua group sehingga baris terlihat tanpa Search.
