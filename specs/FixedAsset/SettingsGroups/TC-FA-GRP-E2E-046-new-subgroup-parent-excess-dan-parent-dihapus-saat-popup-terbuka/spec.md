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
- State global yang diubah (kelas h): penurunan plan berjalan dan T-0 plan efektif. TC-FA-GRP-130 membutuhkan `Excess Parent A` menjadi Excess saat popup terbuka (T-0 diterapkan); TC-FA-GRP-975 membutuhkan plan Growth (cap 3) sedang downgrade, jumlah group cap − 1 saat popup dibuka (T-0 pada langkah 34 menaikkannya ke >= cap), dan `Excess Parent B` menjadi Excess saat popup terbuka. Pemicu T-0 (perubahan cap langsung atau hook uji handler plan efektif di lingkungan non-produksi), akun pelaku, dan pengembalian plan/cap/status Excess disediakan tim FE/BE (tidak disebut di TC, PRD, atau LLD); langkah 20 dan 33 memakai kemampuan itu. Hook `after` memulihkan plan, cap, dan status Excess walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: sesi API aktor untuk menghapus `Temp Parent {runId}-046` sebagai pelaku kedua (langkah 11); pembacaan status respons simpan (422) lewat intercept pasif atau fixture BE (disediakan tim FE); pembacaan jumlah group lewat fixture BE (baseline di hook `before`; disediakan tim FE/BE).
- Pemulihan (hook `after`): pulihkan plan, cap, dan status Excess; hapus lewat API group dengan suffix `{runId}-046`.

## Test Steps

### TC-FA-GRP-129: Row action Add Subgroup tersembunyi untuk parent Excess

1. Ketik Search `Warehouse B`, tekan Enter
2. Buka elipsis (⋯) baris Warehouse B di tabel
3. Verifikasi menu elipsis baris Warehouse B terbuka
4. Verifikasi Add Subgroup tidak dirender di tabel
5. Tutup menu elipsis (Esc) lalu buka elipsis (⋯) node Warehouse B di sidebar
6. Verifikasi menu elipsis node Warehouse B di sidebar terbuka
7. Verifikasi Add Subgroup tidak dirender di sidebar
8. Tutup menu elipsis (Esc)

### TC-FA-GRP-131: Parent dihapus user lain sebelum submit

9. Ganti isi kotak search dengan `Temp Parent {runId}-046`, tekan Enter
10. Buka Add Subgroup pada `Temp Parent {runId}-046` (popup terbuka)
11. Lewat sesi API aktor, hapus `Temp Parent {runId}-046` hingga terhapus
12. Catat jumlah group lewat fixture BE sebagai baseline setelah penghapusan
13. Isi Group Name `Sub C {runId}-046`, lalu klik [Submit]
14. Verifikasi popup ditutup
15. Verifikasi toast netral `This group is no longer available.`
16. Verifikasi tree di-refresh: `Temp Parent {runId}-046` tidak tampil di sidebar
17. Verifikasi tidak ada node dibuat: jumlah group lewat fixture BE sama dengan yang dicatat pada langkah 12

### TC-FA-GRP-130: Parent jadi Excess setelah popup dibuka

18. Ganti isi kotak search dengan `Excess Parent A {runId}-046`, tekan Enter
19. Buka Add Subgroup pada `Excess Parent A {runId}-046` (popup terbuka)
20. Terapkan T-0 sehingga `Excess Parent A {runId}-046` menjadi Excess (kemampuan tim FE/BE)
21. Isi Group Name `Sub A {runId}-046`, lalu klik [Submit]
22. Verifikasi server menolak dengan `422` (group excess terkunci)
23. Verifikasi dialog `Group Is Read-Only` tampil di atas popup dengan isi `This group is now read-only because it's over your plan's group limit.` dan hanya tombol [OK]
24. Verifikasi tidak ada toast
25. Tekan Esc, lalu klik backdrop
26. Verifikasi dialog tetap tampil (Esc dan klik backdrop tidak menutup dialog)
27. Klik [OK]
28. Verifikasi dialog dan popup tertutup
29. Verifikasi tree di-refresh: `Excess Parent A {runId}-046` tampil Excess (dim)
30. Verifikasi subgroup `Sub A {runId}-046` tidak dibuat

### TC-FA-GRP-975: Parent Excess dan cap tercapai bersamaan, CRU Lock diperiksa sebelum re-check cap

31. Pulihkan status Excess dan siapkan plan Growth (cap 3) sedang downgrade dengan jumlah group = cap − 1, `Excess Parent B {runId}-046` belum Excess (kemampuan tim FE/BE)
32. Ganti isi kotak search dengan `Excess Parent B {runId}-046`, tekan Enter
33. Di konteks A, buka Add Subgroup pada `Excess Parent B {runId}-046` dan isi Group Name `Sub B {runId}-046` (belum Submit)
34. Terapkan T-0 sehingga `Excess Parent B {runId}-046` menjadi Excess dan jumlah group >= cap (kemampuan tim FE/BE)
35. Klik [Submit]
36. Verifikasi server menolak dengan `422` (group excess terkunci), bukan `409`
37. Verifikasi dialog `Group Is Read-Only` tampil di atas popup dengan isi `This group is now read-only because it's over your plan's group limit.` dan hanya tombol [OK]
38. Verifikasi tidak ada toast
39. Tekan Esc, lalu klik backdrop
40. Verifikasi dialog tetap tampil (Esc dan klik backdrop tidak menutup dialog)
41. Klik [OK]
42. Verifikasi dialog dan popup tertutup
43. Verifikasi tree di-refresh
44. Verifikasi dialog plan gating D-06 tidak muncul
45. Verifikasi subgroup `Sub B {runId}-046` tidak dibuat
46. Pulihkan plan, cap, dan status Excess

## Notes

- Mode: FE+BE (backend nyata, kelas h state tenant; bagian 3 prinsip 13 butir h). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-129 dan TC-FA-GRP-131 (tanpa mengubah plan) lebih dulu, lalu TC-FA-GRP-130 dan TC-FA-GRP-975 yang memicu T-0 (S-10); berbeda dari urutan nomor TC sumber.
- Pelaku kedua pada TC-FA-GRP-131 memakai sesi API aktor (bukan konteks UI kedua), sehingga tanpa butir `P-2`. Tab A pada TC-FA-GRP-975 adalah satu-satunya konteks UI; "Tab A" pada TC sumber adalah konteks aktor.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 5 (Tutup menu elipsis (Esc) lalu buka elipsis (⋯) node Warehouse B di sidebar); langkah 8 (Tutup menu elipsis (Esc)); langkah 20 (Terapkan T-0 sehingga `Excess Parent A {runId}-046` menjadi Excess (kemampuan tim FE/BE)); langkah 31 (Pulihkan status Excess dan siapkan plan Growth (cap 3) sedang downgrade dengan jumlah group = cap, `Excess Parent B {runId}-046` belum Excess (kemampuan tim FE/BE)); langkah 34 (Terapkan T-0 sehingga `Excess Parent B {runId}-046` menjadi Excess dan jumlah group >= cap (kemampuan tim FE/BE)); langkah 46 (Pulihkan plan, cap, dan status Excess); langkah 1, 9, 18, dan 32 (Ketik Search atau ganti isi kotak search dengan `Warehouse B`, `Temp Parent {runId}-046`, `Excess Parent A {runId}-046`, dan `Excess Parent B {runId}-046`) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1 (R-16).
- Asersi absence "Add Subgroup tidak dirender" didahului `Verifikasi` menu elipsis terbuka sebagai anchor permukaan (8b butir 2). "dialog plan gating D-06 tidak muncul" didahului `Verifikasi` dialog `Group Is Read-Only` tampil sebagai anchor.
- Alasan spec melewati ~35 langkah (46 langkah): keempat TC satu kelas (Create Subgroup pada parent Excess atau dihapus, kelas h state tenant), tiap blok berdiri sendiri (precondition dibangun ulang lewat langkah penghubung), dan langkah banyak karena `Verifikasi` per klausa Expected (S-01), terutama TC-FA-GRP-130 dan TC-FA-GRP-975 yang masing-masing memuat dialog, toast, dan refresh tree.
- Temuan untuk QA:
  - TC-FA-GRP-130 dan TC-FA-GRP-975 menyebut Branch Office (Pre-setup); spec memakai node milik spec yang dijadikan Excess supaya Pre-setup tidak berubah.
  - TC-FA-GRP-130 dan TC-FA-GRP-975 tidak menyebut pelaku dan mekanisme T-0 / penurunan plan; dicatat sebagai kemampuan "disediakan tim FE/BE".
  - TC-FA-GRP-129 tidak menyebut isi menu elipsis node Excess selain Add Subgroup yang tidak dirender; spec memakai menu terbuka sebagai anchor.
  - TC-FA-GRP-131 Expected "tree di-refresh" tidak menyebut apa yang teramati; spec mengasersi `Temp Parent` tidak lagi tampil di sidebar.
  - TC-FA-GRP-975 Precondition menyebut count group = cap, padahal TC-FA-GRP-113 dan 117 menyatakan Add Subgroup pada count = cap langsung diblok dialog count sehingga popup (Langkah Uji 2) tidak terbuka. Spec membaca langkah 3 TC secara harfiah: count = cap − 1 saat popup dibuka, lalu T-0 menaikkan count ke >= cap. Butuh keputusan QA untuk menyelaraskan Precondition TC.
  - TC-FA-GRP-975 Langkah Uji memakai istilah "Tab A" tanpa Tab B; spec memakai satu konteks.

