---
id: TC-FA-GRP-E2E-066-edit-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi
title: "Popup Edit Group: Tutup Tanpa/Dengan Perubahan, Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-212
  - TC-FA-GRP-213
  - TC-FA-GRP-214
  - TC-FA-GRP-1029
  - TC-FA-GRP-1032
coverage:
  web: automated
---

# Popup Edit Group: Tutup Tanpa/Dengan Perubahan, Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser

## Prerequisites

- Mode: FE+BE (backend nyata; tidak ada perubahan yang disimpan, pembacaan nilai Group Name node target lewat fixture BE dipakai untuk asersi "tanpa menyimpan").
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-066` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): node `Edit Target {runId}-066` (level 1, Code `ET`, Description `Edit me`, Function None) di-seed lewat API di hook `before` (Pre-setup tambahan "Edit Target"). Nilai yang diketik (tidak disimpan): TC-FA-GRP-213 Group Name `Dirty Close Edit {runId}-066`; TC-FA-GRP-214 Group Name `Reload Guard Edit {runId}-066`; TC-FA-GRP-1029 Group Name `Backdrop Test`; TC-FA-GRP-1032 Group Name `Route Test`.
- Kemampuan teknis: penanganan dialog native `beforeunload` (batalkan dan lanjutkan, TC-FA-GRP-214); tombol Back browser; pembacaan nilai Group Name node target lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD).
- Pemulihan: tiap blok yang berakhir dengan form kotor ditutup lewat langkah pemulihan eksplisit (`✕`, `Unsaved changes`, `[Leave]`); hook `before` dan `after` menghapus node dengan suffix `{runId}-066` dan group ber-Code literal `ET`.
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target {runId}-066`, tekan Enter

### TC-FA-GRP-212: Tutup tanpa perubahan langsung tertutup

2. Buka elipsis (⋯) baris `Edit Target {runId}-066`, lalu klik Edit
3. Tanpa mengubah field, klik (X)
4. Verifikasi popup tertutup langsung
5. Verifikasi dialog `Unsaved changes` tidak muncul
6. Buka elipsis (⋯) baris `Edit Target {runId}-066`, klik Edit, lalu tekan Esc
7. Verifikasi popup tertutup langsung
8. Verifikasi dialog `Unsaved changes` tidak muncul
9. Buka elipsis (⋯) baris `Edit Target {runId}-066`, klik Edit, lalu klik backdrop (area di luar popup)
10. Verifikasi popup tetap terbuka (klik backdrop tidak menutup popup)
11. Verifikasi dialog `Unsaved changes` tidak muncul

### TC-FA-GRP-213: Tutup dengan perubahan memunculkan dialog Unsaved changes

12. Ubah Group Name menjadi `Dirty Close Edit {runId}-066`
13. Klik (X)
14. Verifikasi dialog tanpa title `You have unsaved changes. Are you sure you want to leave?` dengan [Cancel] dan [Leave] ([Leave] destruktif)
15. Klik [Cancel] pada dialog
16. Verifikasi kembali ke popup dengan input `Dirty Close Edit {runId}-066` dipertahankan
17. Klik (X) lagi
18. Verifikasi dialog `Unsaved changes` tampil kembali
19. Klik [Leave]
20. Verifikasi popup tertutup tanpa menyimpan: Group Name node target lewat fixture BE tetap `Edit Target {runId}-066`

### TC-FA-GRP-214: Reload dengan perubahan memicu guard browser

21. Buka elipsis (⋯) baris `Edit Target {runId}-066`, klik Edit, lalu ubah Group Name menjadi `Reload Guard Edit {runId}-066`
22. Tekan F5
23. Verifikasi dialog native browser leave-page muncul
24. Batalkan dialog native (tetap di halaman)
25. Verifikasi popup dan input `Reload Guard Edit {runId}-066` tetap
26. Klik (X)
27. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil
28. Klik [Leave] (pemulihan form kotor)

### TC-FA-GRP-1029: Klik backdrop saat ada perubahan tidak menutup popup dan tanpa dialog Unsaved changes

29. Buka elipsis (⋯) baris `Edit Target {runId}-066`, klik Edit, lalu ubah Group Name menjadi `Backdrop Test`
30. Klik backdrop (area di luar popup)
31. Verifikasi popup tetap terbuka dengan input `Backdrop Test` dipertahankan
32. Verifikasi dialog `Unsaved changes` tidak muncul
33. Klik (X)
34. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil
35. Klik [Leave] (pemulihan form kotor)

### TC-FA-GRP-1032: Navigasi sidebar dan Back browser dengan perubahan memunculkan dialog Unsaved changes

36. Buka elipsis (⋯) baris `Edit Target {runId}-066`, klik Edit, lalu ubah Group Name menjadi `Route Test`
37. Klik menu lain di sidebar
38. Verifikasi perubahan route dicegat dan dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil pada jalur klik menu sidebar
39. Klik [Cancel] pada dialog
40. Verifikasi navigasi dibatalkan: popup tetap terbuka dengan input `Route Test` dipertahankan
41. Klik tombol Back browser
42. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil pada jalur tombol Back browser
43. Klik [Leave]
44. Verifikasi navigasi dilanjutkan dan popup ditutup tanpa menyimpan: Group Name node target lewat fixture BE tetap `Edit Target {runId}-066`

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Edit Target {runId}-066`, tekan Enter); langkah 26 (Klik (X)) dan langkah 28 (Klik [Leave], pemulihan form kotor); langkah 33 (Klik (X)) dan langkah 35 (Klik [Leave], pemulihan form kotor).
- Alasan spec melewati ~35 langkah (44 langkah): kelima TC satu kelas (UI tutup popup dan guard Unsaved changes pada Popup Edit Group), satu dataset (node `Edit Target` milik spec, tidak berubah), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); blok ditutup bersih sebelum blok berikutnya (S-09); langkah banyak karena `Verifikasi` per klausa Expected (S-01).
- Reload TC-FA-GRP-214 memakai dialog `beforeunload` yang ditangani (S-08); kemampuannya tertulis di Prerequisites. Langkah Search mencari baris target (R-16).
- Temuan untuk QA:
  - TC-FA-GRP-212 Langkah Uji "Buka lagi" tidak menyebut cara membuka lagi; spec membuka lewat elipsis baris target, Edit.
  - TC-FA-GRP-212 Expected menyatakan klik backdrop tidak menutup popup tetapi tidak menyebut cara menutupnya sesudah itu; popup dibiarkan terbuka (tanpa perubahan) dan dipakai blok TC-FA-GRP-213 berikutnya.
  - TC-FA-GRP-1032 Langkah Uji menyebut dialog muncul "pada kedua jalur" tetapi tidak menyebut apakah [Cancel] setelah jalur Back dipakai; spec mengikuti urutan Langkah Uji TC.

