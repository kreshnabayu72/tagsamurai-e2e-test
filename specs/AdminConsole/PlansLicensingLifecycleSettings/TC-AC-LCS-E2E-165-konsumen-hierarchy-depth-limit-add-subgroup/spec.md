---
id: TC-AC-LCS-E2E-165-konsumen-hierarchy-depth-limit-add-subgroup
title: "Konsumen Hierarchy Depth Limit pada Add Subgroup Settings Group"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-579
  - TC-AC-LCS-580
  - TC-AC-LCS-581
coverage:
  web: automated
---

# Konsumen Hierarchy Depth Limit pada Add Subgroup Settings Group

## Prerequisites

- Mode: FE+BE. Kelas harness: fungsional (konsumen lintas modul: nilai Hierarchy Depth Limit dibaca langsung oleh Settings > Group tanpa logout).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: pohon Group pada Settings > Group diatur per TC lewat Fixture BE (node level 5 Site 1 dengan jalur Region A > Branch 1 > Area 1 > Zone 1 > Site 1; kedalaman 8 level untuk TC 581) dan dipulihkan di hook `after` suite; nilai Hierarchy Depth Limit awal `50` (default).
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): Fixture BE untuk membangun pohon Group, mengisi tab System Limits dengan nilai tertentu, dan memulihkan ketujuh tab ke nilai default.
- State global: konfigurasi tab System Limits dan pohon Group diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-579: Hierarchy Depth Limit diturunkan ke 5, Add Subgroup pada node level 5 diblok dengan dialog platform limit

1. Atur lewat Fixture BE: Settings > Group memuat pohon Group dengan node pada level 5 (Region A > Branch 1 > Area 1 > Zone 1 > Site 1)
2. Klik tab System Limits
3. Ubah Hierarchy Depth Limit dari `50` menjadi `5` lalu klik `[Save]`
4. Tunggu aksi `[Save]` selesai (tombol `[Save]` tidak lagi dalam state loading)
5. Buka Settings > Group tanpa logout
6. Verifikasi tombol `+ Add Subgroup` pada node Site 1 (level 5) tetap enabled
7. Klik `+ Add Subgroup` pada node Site 1
8. Verifikasi dialog dengan Dialog Title "Cannot Add Group", Body "You've reached the platform limit of 5 levels. Contact support if you need a higher limit.", dan tombol `[OK]` tampil
9. Verifikasi popup Create Group tidak terbuka
10. Klik `[OK]` pada dialog

### TC-AC-LCS-580: Hierarchy Depth Limit dinaikkan ke 6, Add Subgroup pada node level 5 membuka popup Create Group

11. Atur lewat Fixture BE: Hierarchy Depth Limit tersimpan `5`; Settings > Group memuat node Site 1 pada level 5
12. Buka Plans & Licensing > Lifecycle Settings > System Limits
13. Ubah Hierarchy Depth Limit dari `5` menjadi `6` lalu klik `[Save]`
14. Tunggu aksi `[Save]` selesai (tombol `[Save]` tidak lagi dalam state loading)
15. Buka Settings > Group tanpa logout
16. Klik `+ Add Subgroup` pada node Site 1
17. Verifikasi popup Create Group terbuka dengan parent Site 1
18. Verifikasi tidak ada dialog "Cannot Add Group"
19. Tutup popup Create Group lewat `✕` di header

### TC-AC-LCS-581: Menurunkan Hierarchy Depth Limit di bawah kedalaman pohon existing tidak memangkas node yang ada

20. Atur lewat Fixture BE: ketujuh tab pada nilai default; Settings > Group memuat pohon Group dengan kedalaman 8 level
21. Buka Plans & Licensing > Lifecycle Settings > System Limits
22. Ubah Hierarchy Depth Limit dari `50` menjadi `5` lalu klik `[Save]`
23. Tunggu aksi `[Save]` selesai (tombol `[Save]` tidak lagi dalam state loading)
24. Buka Settings > Group
25. Verifikasi seluruh node sampai level 8 tetap tampil (tidak dihapus atau dipangkas)
26. Klik `+ Add Subgroup` pada node level 8
27. Verifikasi Dialog Title "Cannot Add Group" tampil
28. Verifikasi penambahan Group baru diblokir: popup Create Group tidak terbuka
29. Klik `[OK]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Tiap TC memuat langkah menuju keadaannya: membuka tab System Limits, menyimpan nilai, lalu membuka Settings > Group tanpa logout (S-14).
- TC 579 Expected a memuat tombol `+ Add Subgroup` tetap enabled dan dialog sesudah klik; kedua klausa ditulis sebagai dua `Verifikasi` dengan aksi klik di antaranya (bagian 8b butir 5).
- Temuan untuk QA:
  - TC 579 dan 580 memakai node Site 1 tanpa menyebut cara membangun pohon Group; spec mengaturnya lewat Fixture BE sebagai precondition TC.
  - TC 581 tidak menyebut apakah node level 8 perlu dibuka (expand) pada pohon; spec mengasersi seluruh node tampil sesuai Expected.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 4-5, 10-12, 14-15, 19-21, 23-24, 29.
