---
id: TC-AC-RP-E2E-048-assign-user-to-group-role-aksi-berhasil
title: "Assign User to Group Role: Group Berbeda dari Sidebar dan Pool per Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-168
  - TC-AC-RP-169
coverage:
  web: automated
---

# Assign User to Group Role: Group Berbeda dari Sidebar dan Pool per Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11 (tree group), #12 (`Alex Tan`, `John Dohan`), #15 (`John Dohan` memegang `Manage distributor` di `Region A` dan `Branch 1`; `Alex Tan` memegang `Manage distributor` di `Region A` saja).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`

### TC-AC-RP-169: Pool Group Role mengecualikan pemegang role di group terpilih saja

3. Klik node `Branch 1`
4. Klik "+ Assign"
5. Verifikasi sedikitnya satu kandidat tampil di Table User Picker
6. Ketik Search "John Dohan", tekan Enter
7. Verifikasi `John Dohan` tidak muncul di hasil (sudah memegang role di `Branch 1`)
8. Ganti field Group popup ke `Sumatera`
9. Ketik Search "John Dohan", tekan Enter
10. Verifikasi `John Dohan` muncul sebagai kandidat (belum memegang role di `Sumatera`)
11. Klik `[Cancel]` untuk menutup popup

### TC-AC-RP-168: Assign User ke Group Role pada group berbeda dari sidebar

12. Klik node `Region Jawa`
13. Klik "+ Assign"
14. Ganti field Group ke `Sumatera`
15. Centang `Alex Tan` lalu klik `[Assign]`
16. Verifikasi toast "Success, role has been assigned."
17. Verifikasi tabel tetap tersaring `Region Jawa` dengan sedikitnya satu baris tampil
18. Verifikasi baris `Alex Tan` — `Sumatera` tidak tampil
19. Klik node `Sumatera`
20. Verifikasi baris `Alex Tan` — `Sumatera` tampil dengan R checked + disabled
21. Pulihkan baseline: lepas `Alex Tan` dari `Manage distributor` di `Sumatera` lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: TC-AC-RP-169 (hanya membaca) lebih dulu, TC-AC-RP-168 (aksi tulis) di akhir (S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 6 dan 9 (Search untuk menemukan kandidat target), langkah 11 (`[Cancel]` menutup popup tanpa Assign), langkah 21 (pemulihan baseline).
- Asersi tambahan (S-03): langkah 5 adalah pembanding generik sebagai anchor positif absence `John Dohan` (bagian 8b butir 2); "dengan sedikitnya satu baris tampil" pada asersi tabel tersaring adalah pembanding untuk asersi universal "tetap tersaring".
- Temuan untuk QA:
  - TC-AC-RP-169 tidak menyatakan apakah kotak Search popup tetap berisi atau kosong sesudah field Group diganti; langkah 9 ditulis "Ketik Search" sebagai awal Search baru.
  - TC-AC-RP-168: "baris `Alex Tan` — `Sumatera`" tidak ada di Pre-setup #15 sehingga baris dibuat oleh assignment spec; TC tidak menyebut Last Updated atau Modified By baris baru.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
