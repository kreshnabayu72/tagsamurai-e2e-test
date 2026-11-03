---
id: TC-AC-RP-E2E-047-assign-user-to-group-role-screening-dan-validasi
title: "Assign User to Group Role: Field Group, Header Popup, Validasi, dan Tree Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-165
  - TC-AC-RP-166
  - TC-AC-RP-167
  - TC-AC-RP-170
coverage:
  web: automated
---

# Assign User to Group Role: Field Group, Header Popup, Validasi, dan Tree Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11 (tree group `Default Group`, `Region A` anak `Branch 1`, `Region Jawa` anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (`Alex Tan`), #15 (`Manage distributor` untuk `John Dohan`, `Alex Tan`).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Spec ini tidak menyimpan perubahan data (semua popup ditutup tanpa Assign). Pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`

### TC-AC-RP-166 dan TC-AC-RP-170: Field Group kosong, wajib dipilih, dan pilihan Tree Group

3. Verifikasi tombol "+ Assign" tampil dengan sidebar "All Groups"
4. Klik "+ Assign" dengan sidebar "All Groups"
5. Verifikasi field Group kosong dengan placeholder "Select group"
6. Buka field Group
7. Verifikasi seluruh node tree entitas dapat dipilih
8. Verifikasi tidak ada node hidden atau disabled pada tree
9. Tutup field Group tanpa memilih node
10. Centang `Alex Tan` lalu klik `[Assign]`
11. Verifikasi inline error "You must select a group" tampil
12. Klik `[Cancel]` untuk menutup popup
13. Verifikasi popup Assign User tertutup
14. Verifikasi dialog Unsaved Changes tidak tampil

### TC-AC-RP-165: Screening popup Group Role dengan default group dari sidebar

15. Klik node `Region Jawa`
16. Klik "+ Assign"
17. Verifikasi header popup "Assign User — Manage distributor (Region Jawa)"
18. Verifikasi field Group terisi `Region Jawa`
19. Verifikasi tombol "+ Assign" tampil dengan sidebar `Region Jawa`

### TC-AC-RP-167: Header popup Group Role mengikuti nilai field Group

20. Centang `Alex Tan`
21. Ganti field Group ke `Sumatera`
22. Verifikasi header berubah live menjadi "Assign User — Manage distributor (Sumatera)"
23. Verifikasi centangan `Alex Tan` dikosongkan
24. Verifikasi kandidat diambil ulang sesuai group `Sumatera`
25. Klik `[Cancel]` untuk menutup popup
26. Verifikasi popup Assign User tertutup
27. Verifikasi dialog Unsaved Changes tidak tampil

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan menyimpang dari nomor TC: TC-AC-RP-166 dan TC-AC-RP-170 di awal karena keduanya berjalan dengan sidebar "All Groups" dan field Group kosong; TC-AC-RP-165 dan TC-AC-RP-167 memakai satu pembukaan popup dengan `Region Jawa` (prinsip halaman dipakai berulang).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 9 (menutup dropdown Tree Group tanpa memilih node), langkah 12 dan 25 (`[Cancel]` menutup popup; PRD: `[Cancel]` menutup popup picker tanpa dialog Unsaved Changes dan membuang seleksi).
- Penutup popup: TC-AC-RP-166, 167, dan 170 menyebut tiga penutup (`[Cancel]`, `[✕]`, atau `Esc`); spec memilih satu penutup per blok, yaitu `[Cancel]` pada blok TC-AC-RP-166 dan 170 (langkah 12) dan pada blok TC-AC-RP-167 (langkah 25), karena Expected yang sama berlaku untuk ketiganya (S-03). Langkah 13 dan 26 (popup tertutup) menjadi anchor positif bagi absence dialog Unsaved Changes pada langkah 14 dan 27 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-RP-167 Expected: "kandidat diambil ulang sesuai `Sumatera`" tidak menyebut perbedaan kandidat yang dapat dilihat; spec hanya mengasersi pengambilan ulang sebagai klausa TC.
  - TC-AC-RP-165 Expected: klausa "tombol + Assign selalu tampil terlepas pilihan sidebar" ditulis dengan dua keadaan sidebar ("All Groups" dan `Region Jawa`); TC tidak menyebut keadaan sidebar lain.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
