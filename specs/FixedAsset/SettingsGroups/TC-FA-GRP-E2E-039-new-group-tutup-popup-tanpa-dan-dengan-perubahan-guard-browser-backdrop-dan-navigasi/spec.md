---
id: TC-FA-GRP-E2E-039-new-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi
title: "Popup New Group: Tutup Tanpa/Dengan Perubahan (Unsaved Changes), Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-106
  - TC-FA-GRP-107
  - TC-FA-GRP-108
  - TC-FA-GRP-1027
  - TC-FA-GRP-1030
coverage:
  web: automated
---

# Popup New Group: Tutup Tanpa/Dengan Perubahan (Unsaved Changes), Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser

## Prerequisites

- Mode: FE+BE (backend nyata; tidak ada group yang disimpan, pembacaan jumlah group lewat fixture BE dipakai untuk asersi "tanpa menyimpan").
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data uji (diketik, tidak disubmit; nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`, berkas fixture belum ada): TC-FA-GRP-107 Group Name `Dirty Close {runId}-039`; TC-FA-GRP-108 Group Name `Reload Guard {runId}-039`; TC-FA-GRP-1027 Group Name `Backdrop Test`; TC-FA-GRP-1030 Group Name `Route Test`.
- Kemampuan teknis: penanganan dialog native `beforeunload` (batalkan dan lanjutkan, TC-FA-GRP-108); tombol Back browser; pembacaan jumlah group lewat fixture BE (baseline di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD).
- Pemulihan: tiap blok yang berakhir dengan form kotor ditutup lewat langkah pemulihan eksplisit (`✕`, `Unsaved changes`, `[Leave]`); hook `after` tidak menyimpan apa pun.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-106: Tutup tanpa perubahan langsung tertutup

1. Klik [+] Group di sidebar
2. Tanpa mengubah field, klik (X)
3. Verifikasi popup tertutup langsung
4. Verifikasi dialog `Unsaved changes` tidak muncul
5. Klik [+] Group di sidebar, lalu tekan Esc
6. Verifikasi popup tertutup langsung
7. Verifikasi dialog `Unsaved changes` tidak muncul
8. Klik [+] Group di sidebar, lalu klik backdrop (area di luar popup)
9. Verifikasi popup tetap terbuka (klik backdrop tidak menutup popup)
10. Verifikasi dialog `Unsaved changes` tidak muncul

### TC-FA-GRP-107: Tutup dengan perubahan memunculkan dialog Unsaved changes

11. Ubah Group Name menjadi `Dirty Close {runId}-039`
12. Klik (X)
13. Verifikasi dialog tanpa title `You have unsaved changes. Are you sure you want to leave?` dengan [Cancel] dan [Leave] ([Leave] destruktif)
14. Klik [Cancel] pada dialog
15. Verifikasi kembali ke popup dengan input `Dirty Close {runId}-039` dipertahankan
16. Klik (X) lagi
17. Verifikasi dialog `Unsaved changes` tampil kembali
18. Klik [Leave]
19. Verifikasi popup tertutup tanpa menyimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-108: Reload dengan perubahan memicu guard browser

20. Klik [+] Group di sidebar
21. Ubah Group Name menjadi `Reload Guard {runId}-039`
22. Tekan F5
23. Verifikasi dialog native browser leave-page muncul
24. Batalkan dialog native (tetap di halaman)
25. Verifikasi popup dan input `Reload Guard {runId}-039` tetap
26. Klik (X)
27. Verifikasi dialog `Unsaved changes` tampil
28. Klik [Leave] (pemulihan form kotor)

### TC-FA-GRP-1027: Klik backdrop saat ada perubahan tidak menutup popup dan tanpa dialog Unsaved changes

29. Klik [+] Group di sidebar
30. Ketik Group Name `Backdrop Test`
31. Klik backdrop (area di luar popup)
32. Verifikasi popup tetap terbuka dengan input `Backdrop Test` dipertahankan
33. Verifikasi dialog `Unsaved changes` tidak muncul
34. Klik (X)
35. Verifikasi dialog `Unsaved changes` tampil
36. Klik [Leave] (pemulihan form kotor)

### TC-FA-GRP-1030: Navigasi sidebar dan Back browser dengan perubahan memunculkan dialog Unsaved changes

37. Klik [+] Group di sidebar
38. Ketik Group Name `Route Test`
39. Klik menu lain di sidebar
40. Verifikasi perubahan route dicegat dan dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil pada jalur klik menu sidebar
41. Klik [Cancel] pada dialog
42. Verifikasi navigasi dibatalkan: popup tetap terbuka dengan input `Route Test` dipertahankan
43. Klik tombol Back browser
44. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil pada jalur tombol Back browser
45. Klik [Leave]
46. Verifikasi navigasi dilanjutkan dan popup ditutup tanpa menyimpan: jumlah group lewat fixture BE sama dengan baseline

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 26 dan 28, serta langkah 34 dan 36 (Klik (X), lalu klik [Leave] pada dialog `Unsaved changes` sebagai pemulihan form kotor; keduanya langkah penghubung, `Verifikasi` dialognya mengikuti S-08 dan tidak dicatat lagi).
- Alasan spec melewati ~35 langkah (46 langkah): kelima TC satu kelas (UI tutup popup dan guard Unsaved changes pada Popup New Group), satu dataset (tanpa data tulis), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); blok ditutup bersih sebelum blok berikutnya (S-09); langkah banyak karena `Verifikasi` per klausa Expected (S-01).
- Reload TC-FA-GRP-108 memakai dialog `beforeunload` yang ditangani (S-08); kemampuannya tertulis di Prerequisites.
- Temuan untuk QA:
  - TC-FA-GRP-106 Langkah Uji "Buka lagi" tidak menyebut apakah popup dibuka lagi dari [+] Group; spec memakai [+] Group di sidebar.
  - TC-FA-GRP-106 Expected menyatakan klik backdrop tidak menutup popup tetapi tidak menyebut cara menutupnya sesudah itu; popup dibiarkan terbuka (tanpa perubahan) dan dipakai blok TC-FA-GRP-107 berikutnya.
  - TC-FA-GRP-1030 Langkah Uji menyebut dialog muncul "pada kedua jalur" tetapi tidak menyebut apakah [Cancel] setelah jalur Back dipakai; spec mengikuti urutan Langkah Uji TC.

