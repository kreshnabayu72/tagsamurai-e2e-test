---
id: TC-AC-SG-E2E-075-popup-total-user-detail-screening-identitas-path-group-role-kolom-name-dan-penutupan
title: "Popup Total User Detail: Screening, Identitas Path, Group Role, Kolom Name, dan Penutupan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-273
  - TC-AC-SG-274
  - TC-AC-SG-275
  - TC-AC-SG-276
  - TC-AC-SG-277
coverage:
  web: automated
---

# Popup Total User Detail: Screening, Identitas Path, Group Role, Kolom Name, dan Penutupan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter

### TC-AC-SG-273: Screening Popup Total User Detail

2. Klik angka Total User pada baris `Region A`
3. Verifikasi Header popup: Title `Users` (flat, tanpa nama group)
4. Verifikasi Header popup: ikon close `[✕]` tampil
5. Verifikasi tidak ada tombol teks `Close`
6. Verifikasi identitas record berupa teks polos satu baris `Region A (5)` di bawah title dan di atas toolbar
7. Verifikasi Body: toolbar Search dan Filter tampil
8. Verifikasi tabel memuat kolom default Name, Email, Position, Division, Group Role serta kolom Actions kosong sebagai trigger Column Visibility
9. Verifikasi tabel memuat 5 baris
10. Verifikasi Footer: Pagination tampil

### TC-AC-SG-275: Kolom Group Role: Total Control, Read Only, Group Manager, agregat "2 roles", dan satu role

11. Verifikasi Group Role `Budi Santoso` bernilai `Total Control`
12. Verifikasi Group Role `Rina Wijaya` bernilai `Read Only`
13. Verifikasi Group Role `Andi Pratama` bernilai `Group Manager`
14. Verifikasi Group Role `Sari Dewi` bernilai `2 roles`
15. Verifikasi Group Role `Dewi Lestari` bernilai `Manage active client` (satu role menampilkan nama role)
16. Verifikasi agregat Group Role berformat `[N] roles` dengan [N] jumlah role
17. Hover `2 roles` pada baris `Sari Dewi`
18. Verifikasi hover menampilkan nama-nama role `Manage allocation` dan `Manage partner`

### TC-AC-SG-276: Kolom Name menampilkan Avatar dan nama lengkap dengan tooltip

19. Hover nama `Andi Pratama`
20. Verifikasi sel Name menampilkan avatar (placeholder generik bila belum upload) dan nama lengkap
21. Verifikasi hover menampilkan tooltip nama lengkap `Andi Pratama`

### TC-AC-SG-277: Popup Users ditutup lewat ikon close atau Esc

22. Klik `[✕]`
23. Verifikasi popup tertutup
24. Klik angka Total User pada baris `Region A`
25. Verifikasi tidak ada tombol teks `Close`
26. Tekan Esc
27. Verifikasi popup tertutup

### TC-AC-SG-274: Identitas record popup Users menampilkan full path untuk subgroup

28. Ganti isi kotak search tabel utama dengan `Room 301`, tekan Enter
29. Klik angka Total User pada baris `Room 301`
30. Verifikasi teks identitas di bawah title: `Region A > Branch 1 > Floor 1 > Room 301 (2)`
31. Tutup popup lewat `[✕]`
32. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16; Pohon Uji Utama memiliki 14 group sehingga baris target tidak dijamin di halaman pertama), penggantian Search ke `Room 301`, penutupan popup, dan klik `(←)` di akhir (S-09).
- Urutan TC dalam spec: 273, 275, 276, 277, 274 (TC-AC-SG-275 dan TC-AC-SG-276 memakai popup yang sudah terbuka dari TC-AC-SG-273; TC-AC-SG-274 memakai node lain sehingga paling akhir).
- Temuan untuk QA:
  - TC-AC-SG-273 butir c menyebut "5 baris" sebagai jumlah baris popup `Region A` (Pre-setup #17, data Pre-setup tetap, bukan audit trail); diasersi absolut.
  - TC-AC-SG-275 butir b: "hover `2 roles` menampilkan nama-nama role"; TC tidak menyebut apakah daftar tooltip berurutan, sehingga urutan tidak diasersi.
  - Akun `Budi Santoso` (Total Control) dan `Rina Wijaya` (Read Only) tertulis di Pre-setup #1 dan #2; password aktor memakai `AC_TC_PASSWORD` (Total Control Principal).
