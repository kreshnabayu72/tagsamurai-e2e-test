---
id: TC-FA-GRP-E2E-044-new-subgroup-screening-popup-konteks-under-dan-create-via-row-action-dan-sidebar
title: "Popup New Subgroup: Screening Baris Konteks Under, Create via Row Action dan Elipsis Sidebar, dan Tanpa Guard Parent Ber-Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-125
  - TC-FA-GRP-126
  - TC-FA-GRP-127
  - TC-FA-GRP-128
coverage:
  web: automated
---

# Popup New Subgroup: Screening Baris Konteks Under, Create via Row Action dan Elipsis Sidebar, dan Tanpa Guard Parent Ber-Aset

## Prerequisites

- Mode: FE+BE (backend nyata; Create Subgroup menulis data dan hasilnya diasersi di sidebar dan tabel).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): pohon group Tabel A, yaitu Head Office > Floor 2 (TC-FA-GRP-125, 126) dan Warehouse A (Assignable, 24 aset aktif; TC-FA-GRP-127, 128).
- Data Dinamis bersuffix `{runId}-044` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-126: `Meeting Room {runId}-044` (Function Assignable, di bawah Floor 2). TC-FA-GRP-127: `Rack Entry {runId}-044` (di bawah Warehouse A). TC-FA-GRP-128: `Rack 2 {runId}-044` (di bawah Warehouse A).
- Pemulihan (hook `after`): hapus lewat API semua subgroup dengan suffix `{runId}-044`.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-125: Screening Popup New Subgroup, baris konteks Under pre-filled path parent

1. Klik Head Office di sidebar
2. Buka elipsis (⋯) baris Floor 2 di tabel, lalu klik Add Subgroup
3. Verifikasi title `New Subgroup` (tanpa nama parent) dan icon (X)
4. Verifikasi baris konteks Under read-only tanpa placeholder, berisi full path `Head Office > Floor 2`
5. Verifikasi field Group Name * dengan placeholder `Enter group name`
6. Verifikasi field Code dengan placeholder `Enter code, or leave blank to auto-generate` dan helper `Letters, numbers, hyphens, underscores, and dots only`
7. Verifikasi field Description (textarea) dengan placeholder `Enter description`
8. Verifikasi radio Function None / Assignable masing-masing dengan icon info, None terpilih default
9. Verifikasi checkbox `Stay on this form after submitting` unchecked
10. Verifikasi footer: [Clear Field] dan [Submit]

### TC-FA-GRP-126: Create Subgroup happy path dari row action

11. Isi Group Name `Meeting Room {runId}-044`, pilih Function Assignable, lalu klik [Submit]
12. Verifikasi toast sukses `Success, group has been created.`
13. Verifikasi Meeting Room muncul di bawah Floor 2 di sidebar
14. Klik Floor 2 di sidebar
15. Verifikasi tabel saat Floor 2 dipilih menampilkan Meeting Room
16. Verifikasi Function badge Assignable pada baris Meeting Room

### TC-FA-GRP-127: Create Subgroup via elipsis sidebar (entry point kedua)

17. Buka elipsis (⋯) node Warehouse A di sidebar, lalu klik Add Subgroup
18. Verifikasi popup sama dengan dari row action: title `New Subgroup`, field, dan footer yang sama, dengan baris konteks Under = Warehouse A
19. Isi Group Name `Rack Entry {runId}-044`, lalu klik [Submit]
20. Verifikasi toast sukses `Success, group has been created.`
21. Verifikasi Rack Entry di bawah Warehouse A di sidebar

### TC-FA-GRP-128: Create Subgroup di bawah parent ber-aset tanpa guard

22. Buka elipsis (⋯) node Warehouse A di sidebar, lalu klik Add Subgroup
23. Isi Group Name `Rack 2 {runId}-044`, lalu klik [Submit]
24. Verifikasi subgroup dibuat sukses: toast `Success, group has been created.`
25. Verifikasi tidak ada dialog atau guard aset yang tampil

## Notes

- Mode: FE+BE (kelas fungsional, backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Popup TC-FA-GRP-125 tidak ditutup; langkah TC-FA-GRP-126 melanjutkannya sampai submit (jumlah buka popup tidak melebihi jumlah tutup, S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 14 (Klik Floor 2 di sidebar).
- Temuan untuk QA:
  - TC-FA-GRP-126 Expected b "tabel saat Floor 2 dipilih menampilkannya" tidak menyebut langkah memilih Floor 2; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-126 Post Condition "Changelog Action Create" dan "Tidak ada auto-assign creator (Total Control)" tidak punya langkah observasi di TC; tidak diasersi di spec ini.
  - TC-FA-GRP-128 Expected "tidak ada dialog/guard aset" adalah asersi absence; toast sukses dipakai sebagai anchor positif (8b butir 2).

