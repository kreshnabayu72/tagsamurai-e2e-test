---
id: TC-AC-ACC-E2E-115-change-partner-oleh-distributor
title: "Change Partner oleh Distributor: Relasi Distributor-langsung, Tree Select Group, Tambah Partner, Remove Anchor, dan Partner Terakhir Jaringan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-958
  - TC-AC-ACC-592
  - TC-AC-ACC-593
  - TC-AC-ACC-601
  - TC-AC-ACC-182
coverage:
  web: automated
---

# Change Partner oleh Distributor: Relasi Distributor-langsung, Tree Select Group, Tambah Partner, Remove Anchor, dan Partner Terakhir Jaringan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Total Control A-13 (PT Distribusi Nusantara) `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`, password dari `AC_CLIENT_DIST_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup (Tabel A3) yang hanya dibaca: C-ROL-1 `PT Jalur Distributor Dulu` (relasi Distributor-langsung PT Distribusi Nusantara dan Partner CV Mitra Sejati; Residen) dan C-ROL-8 `PT Ubah Mitra 05` (satu-satunya Partner CV Mitra Sejati; dialog Change Partner dibuka lalu ditutup tanpa `[Confirm]`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): `PT Ubah Mitra 06 {runId}-115` (setara C-ROL-8: Active, satu-satunya Partner CV Mitra Sejati, Group Area Jakarta, tanpa subscription; target TC-AC-ACC-593, efek: relasi "CV Mitra Lestari" ditambahkan, baris Changelog `Change Partner` dan Last Updated bertambah); `PT Jalur Campur Uji {runId}-115` (setara C-ROL-3: Active, Partner CV Mitra Sejati 2026-01-05 dan Distributor-langsung PT Distribusi Nusantara 2026-02-10, Group Area Jakarta; target TC-AC-ACC-601); `PT Lintas Jaringan Uji {runId}-115` (setara C-ISO-6: Active, Anchor CV Mitra Sejati 2026-01-05 dan CV Mitra Timur, Group Area Jakarta, tanpa subscription; target TC-AC-ACC-182). Client C-ROL-3, C-ROL-8 `PT Ubah Mitra 06`, dan C-ISO-6 literal tidak disentuh.
- Partner pembanding: `CV Mitra Lestari` (jaringan PT Distribusi Nusantara), `CV Mitra Timur` (jaringan PT Distribusi Timur).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-958: Dialog Change Partner tidak menyediakan kontrol untuk melepas relasi Distributor-langsung

1. Ketik Search `PT Jalur Distributor Dulu`, tekan Enter
2. Klik `[⋯]` pada baris `PT Jalur Distributor Dulu` → klik `Change Partner`
3. Verifikasi list "Current Partners" memuat satu baris "CV Mitra Sejati" dengan tombol `[Remove]`
4. Verifikasi list tidak memuat baris "PT Distribusi Nusantara"
5. Verifikasi tidak ada tombol `[Remove]` untuk relasi Distributor-langsung
6. Klik `[✕]` pada header dialog

### TC-AC-ACC-592: Remove Partner terakhir oleh Distributor: tree Select Group memakai tree Group Distributor

7. Ketik Search `PT Ubah Mitra 05`, tekan Enter
8. Klik `[⋯]` pada baris `PT Ubah Mitra 05` → klik `Change Partner`
9. Klik `[Remove]` pada "CV Mitra Sejati"
10. Verifikasi field `[Group]` diganti `Select Group*`
11. Verifikasi callout "This client has no partner and requires a group to be selected manually."
12. Buka tree `Select Group*`
13. Verifikasi tree memuat "Area Jakarta" yang dapat dipilih
14. Verifikasi "Area Surabaya" tidak muncul di tree
15. Verifikasi "Regional Timur" tidak muncul di tree
16. Klik `[✕]` pada header dialog
17. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
18. Klik `[Leave]` pada dialog Unsaved Changes

### TC-AC-ACC-593: Distributor menambah Partner dalam jaringannya sampai sukses

19. Ketik Search `PT Ubah Mitra 06 {runId}-115`, tekan Enter
20. Klik `[⋯]` pada baris `PT Ubah Mitra 06 {runId}-115` → klik `Change Partner`
21. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
22. Verifikasi "CV Mitra Lestari" masuk list dengan badge `New`
23. Klik `[Confirm]`
24. Verifikasi toast sukses "Success, partner has been updated."
25. Verifikasi Managed By baris `PT Ubah Mitra 06 {runId}-115` adalah "CV Mitra Sejati" diikuti `+1 more`

### TC-AC-ACC-601: Remove Partner Anchor sementara relasi Distributor-langsung tersisa: Client bukan Direct dan Group pindah

26. Ketik Search `PT Jalur Campur Uji {runId}-115`, tekan Enter
27. Verifikasi Managed By baris `PT Jalur Campur Uji {runId}-115` diawali "CV Mitra Sejati"
28. Verifikasi Group baris `PT Jalur Campur Uji {runId}-115` adalah "Cabang Menteng"
29. Klik `[⋯]` pada baris `PT Jalur Campur Uji {runId}-115` → klik `Change Partner`
30. Klik `[Remove]` pada "CV Mitra Sejati"
31. Verifikasi field `[Group]` read-only menampilkan "Area Jakarta"
32. Verifikasi `Select Group*` tidak tampil
33. Verifikasi `[Confirm]` aktif
34. Klik `[Confirm]`
35. Verifikasi toast sukses "Success, partner has been updated."
36. Verifikasi Managed By baris `PT Jalur Campur Uji {runId}-115` adalah "PT Distribusi Nusantara (Direct)"
37. Verifikasi Group baris `PT Jalur Campur Uji {runId}-115` adalah "Area Jakarta"

### TC-AC-ACC-182: Remove Partner terakhir di jaringan Distributor sementara relasi jaringan lain ada

38. Ketik Search `PT Lintas Jaringan Uji {runId}-115`, tekan Enter
39. Klik `[⋯]` pada baris `PT Lintas Jaringan Uji {runId}-115` → klik `Change Partner`
40. Klik `[Remove]` pada "CV Mitra Sejati" (semua Partner jaringan PT Distribusi Nusantara)
41. Verifikasi `Select Group*` tidak diminta
42. Verifikasi Client bukan Direct (relasi CV Mitra Timur tetap)
43. Verifikasi field `[Group]` tidak tampil
44. Klik `[Confirm]`
45. Tunggu aksi selesai (dialog Change Partner tertutup)
46. Ketik Search `PT Lintas Jaringan Uji {runId}-115`, tekan Enter
47. Verifikasi empty state Title "No results found" dengan Description "Try adjusting your search or filter."

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas lima TC satu topik (Change Partner oleh Distributor), satu akun; tiap blok memakai Client sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Aksi yang menghabiskan data (Remove Anchor TC-AC-ACC-601 dan Partner terakhir jaringan TC-AC-ACC-182) ditaruh paling akhir.
- Langkah penghubung (tanpa awalan Verifikasi): `[✕]` menutup dialog bersih (blok 958); `[✕]` dan `[Leave]` penutup dialog dirty (blok 592); langkah "Tunggu aksi selesai" sesudah `[Confirm]` TC-AC-ACC-182 karena langkah berikutnya mencari ulang di List (butir 8 bagian 8b).
- Search pada langkah 46 mengganti isi kotak Search yang sudah berisi nama Client yang sama; hasilnya empty state berfungsi sebagai anchor positif absence baris (butir 2 bagian 8b).
- Post Condition TC-AC-ACC-593 butir b (Changelog `Change Partner`, Field `Partner` satu baris), TC-AC-ACC-601 dan TC-AC-ACC-182 (seed ulang fixture): tanpa langkah observasi di TC, tidak diasersi; pemulihan TC-AC-ACC-593 (Remove "CV Mitra Lestari" lalu `[Confirm]`) tidak dijalankan karena target adalah replika milik spec yang dibersihkan hook `after`.
- Temuan untuk QA:
  - TC-AC-ACC-592 tidak menyebut penutupan dialog yang dirty; spec menutupnya lewat `[✕]` dan `[Leave]` (S-08, S-09).
  - TC-AC-ACC-182 Expected a menyebut "field [Group] tidak tampil (Anchor tersisa CV Mitra Timur tidak terlihat viewer Distributor)" tanpa langkah observasi tersendiri; spec mengasersinya setelah Remove, sebelum [Confirm].
