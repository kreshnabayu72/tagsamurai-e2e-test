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
- Data Pre-setup (Tabel A3): C-ROL-1 `PT Jalur Distributor Dulu` (relasi Distributor-langsung PT Distribusi Nusantara dan Partner CV Mitra Sejati; Residen, hanya dibaca); C-ROL-8 `PT Ubah Mitra 05` (hanya dibaca) dan `PT Ubah Mitra 06` (dikonfirmasi lalu dipulihkan), keduanya satu-satunya Partner CV Mitra Sejati; C-ROL-3 `PT Jalur Campur Uji` (relasi Partner CV Mitra Sejati 2026-01-05 dan Distributor-langsung PT Distribusi Nusantara 2026-02-10; Dikonsumsi); C-ISO-6 `PT Lintas Jaringan Uji` (Anchor CV Mitra Sejati + CV Mitra Timur; Dikonsumsi).
- Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang C-ROL-3, C-ISO-6, dan C-ROL-8 `PT Ubah Mitra 06` di hook `before` dan `after`. Pemulihan lewat UI untuk `PT Ubah Mitra 06` (Remove "CV Mitra Lestari" + [Confirm]) menjadikan relasi "CV Mitra Lestari" `transferred`: baris Changelog `Change Partner` dan Last Updated bertambah.
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

19. Ketik Search `PT Ubah Mitra 06`, tekan Enter
20. Klik `[⋯]` pada baris `PT Ubah Mitra 06` → klik `Change Partner`
21. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
22. Verifikasi "CV Mitra Lestari" masuk list dengan badge `New`
23. Klik `[Confirm]`
24. Verifikasi toast sukses "Success, partner has been updated."
25. Verifikasi Managed By baris `PT Ubah Mitra 06` adalah "CV Mitra Sejati" diikuti `+1 more`
26. Klik `[⋯]` pada baris `PT Ubah Mitra 06` → klik `Change Partner`
27. Klik `[Remove]` pada "CV Mitra Lestari"
28. Klik `[Confirm]`

### TC-AC-ACC-601: Remove Partner Anchor sementara relasi Distributor-langsung tersisa: Client bukan Direct dan Group pindah

29. Ketik Search `PT Jalur Campur Uji`, tekan Enter
30. Verifikasi Managed By baris `PT Jalur Campur Uji` diawali "CV Mitra Sejati"
31. Verifikasi Group baris `PT Jalur Campur Uji` adalah "Cabang Menteng"
32. Klik `[⋯]` pada baris `PT Jalur Campur Uji` → klik `Change Partner`
33. Klik `[Remove]` pada "CV Mitra Sejati"
34. Verifikasi field `[Group]` read-only menampilkan "Area Jakarta"
35. Verifikasi `Select Group*` tidak tampil
36. Verifikasi `[Confirm]` aktif
37. Klik `[Confirm]`
38. Verifikasi toast sukses "Success, partner has been updated."
39. Verifikasi Managed By baris `PT Jalur Campur Uji` adalah "PT Distribusi Nusantara (Direct)"
40. Verifikasi Group baris `PT Jalur Campur Uji` adalah "Area Jakarta"

### TC-AC-ACC-182: Remove Partner terakhir di jaringan Distributor sementara relasi jaringan lain ada

41. Ketik Search `PT Lintas Jaringan Uji`, tekan Enter
42. Klik `[⋯]` pada baris `PT Lintas Jaringan Uji` → klik `Change Partner`
43. Klik `[Remove]` pada "CV Mitra Sejati" (semua Partner jaringan PT Distribusi Nusantara)
44. Verifikasi `Select Group*` tidak diminta
45. Verifikasi Client bukan Direct (relasi CV Mitra Timur tetap)
46. Verifikasi field `[Group]` tidak tampil
47. Klik `[Confirm]`
48. Tunggu aksi selesai (dialog Change Partner tertutup)
49. Ketik Search `PT Lintas Jaringan Uji`, tekan Enter
50. Verifikasi empty state Title "No results found" dengan Description "Try adjusting your search or filter."

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas lima TC satu topik (Change Partner oleh Distributor), satu akun; tiap blok memakai Client sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Aksi yang menghabiskan data (Remove Anchor TC-AC-ACC-601 dan Partner terakhir jaringan TC-AC-ACC-182) ditaruh paling akhir.
- Langkah penghubung (tanpa awalan Verifikasi): `[✕]` menutup dialog bersih (blok 958); `[✕]` dan `[Leave]` penutup dialog dirty (blok 592); pemulihan `PT Ubah Mitra 06` (Remove "CV Mitra Lestari" dan `[Confirm]`, Post Condition TC-AC-ACC-593); langkah "Tunggu aksi selesai" sesudah `[Confirm]` TC-AC-ACC-182 karena langkah berikutnya mencari ulang di List (butir 8 bagian 8b).
- Search pada langkah 49 mengganti isi kotak Search yang sudah berisi nama Client yang sama; hasilnya empty state berfungsi sebagai anchor positif absence baris (butir 2 bagian 8b).
- Post Condition TC-AC-ACC-593 butir b (Changelog `Change Partner`, Field `Partner` satu baris), TC-AC-ACC-601 dan TC-AC-ACC-182 (seed ulang fixture): tanpa langkah observasi di TC, tidak diasersi.
- Temuan untuk QA:
  - TC-AC-ACC-592 tidak menyebut penutupan dialog yang dirty; spec menutupnya lewat `[✕]` dan `[Leave]` (S-08, S-09).
  - TC-AC-ACC-182 Expected a menyebut "field [Group] tidak tampil (Anchor tersisa CV Mitra Timur tidak terlihat viewer Distributor)" tanpa langkah observasi tersendiri; spec mengasersinya setelah Remove, sebelum [Confirm].
