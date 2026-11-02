---
id: TC-FA-GRP-E2E-046-new-subgroup-parent-excess-dan-parent-dihapus-saat-popup-terbuka
title: "Create Subgroup: Row Action Hidden untuk Parent Excess, Parent Menjadi Excess Setelah Popup Dibuka (CRU Lock Sebelum Cap), dan Parent Dihapus Sebelum Submit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-129
  - TC-FA-GRP-130
  - TC-FA-GRP-131
  - TC-FA-GRP-975
coverage:
  web: automated
---

# Create Subgroup: Row Action Hidden untuk Parent Excess, Parent Menjadi Excess Setelah Popup Dibuka (CRU Lock Sebelum Cap), dan Parent Dihapus Sebelum Submit

## Prerequisites

- Mode: FE+BE (backend nyata; kelas h state tenant: status Excess node akibat penurunan plan; TC-FA-GRP-130 dan TC-FA-GRP-975 memicu T-0 plan efektif).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Warehouse B (Assignable, Excess; TC-FA-GRP-129).
- Data Dinamis bersuffix `{runId}-046` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-130: parent `Excess Parent A {runId}-046` (level 1, Assignable) dengan subgroup baru `Sub A {runId}-046`; TC-FA-GRP-975: parent `Excess Parent B {runId}-046` dengan subgroup baru `Sub B {runId}-046` (dipakai sebagai pengganti Branch Office Pre-setup supaya Pre-setup tidak berubah menjadi Excess; S-06). TC-FA-GRP-131: `Temp Parent {runId}-046` dan subgroup baru `Sub C {runId}-046`.
- State global yang diubah (kelas h): penurunan plan berjalan dan T-0 plan efektif. TC-FA-GRP-130 membutuhkan `Excess Parent A` menjadi Excess saat popup terbuka (T-0 diterapkan); TC-FA-GRP-975 membutuhkan plan Growth (cap 3) sedang downgrade, jumlah group sama dengan cap, dan `Excess Parent B` menjadi Excess saat popup terbuka. Pemicu T-0 (perubahan cap langsung atau hook uji handler plan efektif di lingkungan non-produksi), akun pelaku, dan pengembalian plan/cap/status Excess disediakan tim FE/BE (tidak disebut di TC, PRD, atau LLD); langkah 16 dan 29 memakai kemampuan itu. Hook `after` memulihkan plan, cap, dan status Excess walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: sesi API aktor untuk menghapus `Temp Parent {runId}-046` sebagai pelaku kedua (langkah 9); pembacaan status respons simpan (422) lewat intercept pasif atau fixture BE (disediakan tim FE); pembacaan jumlah group lewat fixture BE (baseline di hook `before`; disediakan tim FE/BE).
- Pemulihan (hook `after`): pulihkan plan, cap, dan status Excess; hapus lewat API group dengan suffix `{runId}-046`.

## Test Steps

### TC-FA-GRP-129: Row action Add Subgroup tersembunyi untuk parent Excess

1. Buka elipsis (⋯) baris Warehouse B di tabel
2. Verifikasi menu elipsis baris Warehouse B terbuka
3. Verifikasi Add Subgroup tidak dirender di tabel
4. Tutup menu elipsis (Esc) lalu buka elipsis (⋯) node Warehouse B di sidebar
5. Verifikasi menu elipsis node Warehouse B di sidebar terbuka
6. Verifikasi Add Subgroup tidak dirender di sidebar
7. Tutup menu elipsis (Esc)

### TC-FA-GRP-131: Parent dihapus user lain sebelum submit

8. Buka Add Subgroup pada `Temp Parent {runId}-046` (popup terbuka)
9. Lewat sesi API aktor, hapus `Temp Parent {runId}-046` hingga terhapus
10. Isi Group Name `Sub C {runId}-046`, lalu klik [Submit]
11. Verifikasi popup ditutup
12. Verifikasi toast netral `This group is no longer available.`
13. Verifikasi tree di-refresh: `Temp Parent {runId}-046` tidak tampil di sidebar
14. Verifikasi tidak ada node dibuat: jumlah group lewat fixture BE sama dengan baseline setelah penghapusan

### TC-FA-GRP-130: Parent jadi Excess setelah popup dibuka

15. Buka Add Subgroup pada `Excess Parent A {runId}-046` (popup terbuka)
16. Terapkan T-0 sehingga `Excess Parent A {runId}-046` menjadi Excess (kemampuan tim FE/BE)
17. Isi Group Name `Sub A {runId}-046`, lalu klik [Submit]
18. Verifikasi server menolak dengan `422` (group excess terkunci)
19. Verifikasi dialog `Group Is Read-Only` tampil di atas popup dengan isi `This group is now read-only because it's over your plan's group limit.` dan hanya tombol [OK]
20. Verifikasi tidak ada toast
21. Tekan Esc, lalu klik backdrop
22. Verifikasi dialog tetap tampil (Esc dan klik backdrop tidak menutup dialog)
23. Klik [OK]
24. Verifikasi dialog dan popup tertutup
25. Verifikasi tree di-refresh: `Excess Parent A {runId}-046` tampil Excess (dim)
26. Verifikasi subgroup `Sub A {runId}-046` tidak dibuat

### TC-FA-GRP-975: Parent Excess dan cap tercapai bersamaan, CRU Lock diperiksa sebelum re-check cap

27. Pulihkan status Excess dan siapkan plan Growth (cap 3) sedang downgrade dengan jumlah group = cap, `Excess Parent B {runId}-046` belum Excess (kemampuan tim FE/BE)
28. Di konteks A, buka Add Subgroup pada `Excess Parent B {runId}-046` dan isi Group Name `Sub B {runId}-046` (belum Submit)
29. Terapkan T-0 sehingga `Excess Parent B {runId}-046` menjadi Excess dan jumlah group >= cap (kemampuan tim FE/BE)
30. Klik [Submit]
31. Verifikasi server menolak dengan `422` (group excess terkunci), bukan `409`
32. Verifikasi dialog `Group Is Read-Only` tampil di atas popup dengan isi `This group is now read-only because it's over your plan's group limit.` dan hanya tombol [OK]
33. Verifikasi tidak ada toast
34. Tekan Esc, lalu klik backdrop
35. Verifikasi dialog tetap tampil (Esc dan klik backdrop tidak menutup dialog)
36. Klik [OK]
37. Verifikasi dialog dan popup tertutup
38. Verifikasi tree di-refresh
39. Verifikasi dialog plan gating D-06 tidak muncul
40. Verifikasi subgroup `Sub B {runId}-046` tidak dibuat
41. Pulihkan plan, cap, dan status Excess

## Notes

- Mode: FE+BE (backend nyata, kelas h state tenant; bagian 3 prinsip 13 butir h). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-129 dan TC-FA-GRP-131 (tanpa mengubah plan) lebih dulu, lalu TC-FA-GRP-130 dan TC-FA-GRP-975 yang memicu T-0 (S-10); berbeda dari urutan nomor TC sumber.
- Pelaku kedua pada TC-FA-GRP-131 memakai sesi API aktor (bukan konteks UI kedua), sehingga tanpa butir `P-2`. Tab A pada TC-FA-GRP-975 adalah satu-satunya konteks UI; "Tab A" pada TC sumber adalah konteks aktor.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 4 (Tutup menu elipsis (Esc) lalu buka elipsis (⋯) node Warehouse B di sid...); langkah 7 (Tutup menu elipsis (Esc)); langkah 16 (Terapkan T-0 sehingga `Excess Parent A {runId}-046` menjadi Excess (ke...); langkah 27 (Pulihkan status Excess dan siapkan plan Growth (cap 3) sedang downgrad...); langkah 29 (Terapkan T-0 sehingga `Excess Parent B {runId}-046` menjadi Excess dan...); langkah 41 (Pulihkan plan, cap, dan status Excess).
- Asersi absence "Add Subgroup tidak dirender" didahului `Verifikasi` menu elipsis terbuka sebagai anchor permukaan (8b butir 2). "dialog plan gating D-06 tidak muncul" didahului `Verifikasi` dialog `Group Is Read-Only` tampil sebagai anchor.
- Alasan spec melewati ~35 langkah (41 langkah): keempat TC satu kelas (Create Subgroup pada parent Excess atau dihapus, kelas h state tenant), tiap blok berdiri sendiri (precondition dibangun ulang lewat langkah penghubung), dan langkah banyak karena `Verifikasi` per klausa Expected (S-01), terutama TC-FA-GRP-130 dan TC-FA-GRP-975 yang masing-masing memuat dialog, toast, dan refresh tree.
- Temuan untuk QA:
  - TC-FA-GRP-130 dan TC-FA-GRP-975 menyebut Branch Office (Pre-setup); spec memakai node milik spec yang dijadikan Excess supaya Pre-setup tidak berubah.
  - TC-FA-GRP-130 dan TC-FA-GRP-975 tidak menyebut pelaku dan mekanisme T-0 / penurunan plan; dicatat sebagai kemampuan "disediakan tim FE/BE".
  - TC-FA-GRP-129 tidak menyebut isi menu elipsis node Excess selain Add Subgroup yang tidak dirender; spec memakai menu terbuka sebagai anchor.
  - TC-FA-GRP-131 Expected "tree di-refresh" tidak menyebut apa yang teramati; spec mengasersi `Temp Parent` tidak lagi tampil di sidebar.
  - TC-FA-GRP-975 Langkah Uji memakai istilah "Tab A" tanpa Tab B; spec memakai satu konteks.

