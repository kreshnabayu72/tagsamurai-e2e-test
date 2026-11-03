---
id: TC-FA-GRP-E2E-052-new-subgroup-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi
title: "Popup New Subgroup: Tutup Tanpa/Dengan Perubahan, Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-154
  - TC-FA-GRP-155
  - TC-FA-GRP-156
  - TC-FA-GRP-1028
  - TC-FA-GRP-1031
coverage:
  web: automated
---

# Popup New Subgroup: Tutup Tanpa/Dengan Perubahan, Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser

## Prerequisites

- Mode: FE+BE (backend nyata; tidak ada subgroup yang disimpan, pembacaan jumlah group lewat fixture BE dipakai untuk asersi "tanpa menyimpan").
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data uji (diketik, tidak disubmit; nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`, berkas fixture belum ada): TC-FA-GRP-155 Group Name `Dirty Close Sub {runId}-052`; TC-FA-GRP-156 Group Name `Reload Guard Sub {runId}-052`; TC-FA-GRP-1028 Group Name `Backdrop Test`; TC-FA-GRP-1031 Group Name `Route Test`.
- Kemampuan teknis: penanganan dialog native `beforeunload` (batalkan dan lanjutkan, TC-FA-GRP-156); tombol Back browser; pembacaan jumlah group lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD).
- Pemulihan: tiap blok yang berakhir dengan form kotor ditutup lewat langkah pemulihan eksplisit (`✕`, `Unsaved changes`, `[Leave]`); hook `after` tidak menyimpan apa pun.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-154: Tutup tanpa perubahan langsung tertutup

1. Ketik Search `Head Office`, tekan Enter
2. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
3. Tanpa mengubah field, klik (X)
4. Verifikasi popup tertutup langsung
5. Verifikasi dialog `Unsaved changes` tidak muncul
6. Buka elipsis (⋯) baris Head Office, klik Add Subgroup, lalu tekan Esc
7. Verifikasi popup tertutup langsung
8. Verifikasi dialog `Unsaved changes` tidak muncul
9. Buka elipsis (⋯) baris Head Office, klik Add Subgroup, lalu klik backdrop (area di luar popup)
10. Verifikasi popup tetap terbuka (klik backdrop tidak menutup popup)
11. Verifikasi dialog `Unsaved changes` tidak muncul

### TC-FA-GRP-155: Tutup dengan perubahan memunculkan dialog Unsaved changes

12. Ubah Group Name menjadi `Dirty Close Sub {runId}-052`
13. Klik (X)
14. Verifikasi dialog tanpa title `You have unsaved changes. Are you sure you want to leave?` dengan [Cancel] dan [Leave] ([Leave] destruktif)
15. Klik [Cancel] pada dialog
16. Verifikasi kembali ke popup dengan input `Dirty Close Sub {runId}-052` dipertahankan
17. Klik (X) lagi
18. Verifikasi dialog `Unsaved changes` tampil kembali
19. Klik [Leave]
20. Verifikasi popup tertutup tanpa menyimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-156: Reload dengan perubahan memicu guard browser

21. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
22. Ubah Group Name menjadi `Reload Guard Sub {runId}-052`
23. Tekan F5
24. Verifikasi dialog native browser leave-page muncul
25. Batalkan dialog native (tetap di halaman)
26. Verifikasi popup dan input `Reload Guard Sub {runId}-052` tetap
27. Klik (X)
28. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil
29. Klik [Leave] (pemulihan form kotor)

### TC-FA-GRP-1028: Klik backdrop saat ada perubahan tidak menutup popup dan tanpa dialog Unsaved changes

30. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
31. Ketik Group Name `Backdrop Test`
32. Klik backdrop (area di luar popup)
33. Verifikasi popup tetap terbuka dengan input `Backdrop Test` dipertahankan
34. Verifikasi dialog `Unsaved changes` tidak muncul
35. Klik (X)
36. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil
37. Klik [Leave] (pemulihan form kotor)

### TC-FA-GRP-1031: Navigasi sidebar dan Back browser dengan perubahan memunculkan dialog Unsaved changes

38. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
39. Ketik Group Name `Route Test`
40. Klik menu lain di sidebar
41. Verifikasi perubahan route dicegat dan dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil pada jalur klik menu sidebar
42. Klik [Cancel] pada dialog
43. Verifikasi navigasi dibatalkan: popup tetap terbuka dengan input `Route Test` dipertahankan
44. Klik tombol Back browser
45. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil pada jalur tombol Back browser
46. Klik [Leave]
47. Verifikasi navigasi dilanjutkan dan popup ditutup tanpa menyimpan: jumlah group lewat fixture BE sama dengan baseline

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 27 (Klik (X)) dan langkah 29 (Klik [Leave], pemulihan form kotor); langkah 35 (Klik (X)) dan langkah 37 (Klik [Leave], pemulihan form kotor).
- Pencarian baris target (S-03, R-16): langkah 1 (Ketik Search `Head Office`, tekan Enter) menemukan baris Head Office; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris Head Office tidak dijamin berada di halaman 1 All Groups.
- Alasan spec melewati ~35 langkah (47 langkah): kelima TC satu kelas (UI tutup popup dan guard Unsaved changes pada Popup New Subgroup), satu dataset (tanpa data tulis), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); blok ditutup bersih sebelum blok berikutnya (S-09); langkah banyak karena `Verifikasi` per klausa Expected (S-01).
- Reload TC-FA-GRP-156 memakai dialog `beforeunload` yang ditangani (S-08); kemampuannya tertulis di Prerequisites.
- Temuan untuk QA:
  - TC-FA-GRP-154 Langkah Uji "Buka lagi" tidak menyebut cara membuka lagi; spec membuka lewat elipsis baris Head Office, Add Subgroup.
  - TC-FA-GRP-154 Expected menyatakan klik backdrop tidak menutup popup tetapi tidak menyebut cara menutupnya sesudah itu; popup dibiarkan terbuka (tanpa perubahan) dan dipakai blok TC-FA-GRP-155 berikutnya.
  - TC-FA-GRP-1031 Langkah Uji menyebut dialog muncul "pada kedua jalur" tetapi tidak menyebut apakah [Cancel] setelah jalur Back dipakai; spec mengikuti urutan Langkah Uji TC.

