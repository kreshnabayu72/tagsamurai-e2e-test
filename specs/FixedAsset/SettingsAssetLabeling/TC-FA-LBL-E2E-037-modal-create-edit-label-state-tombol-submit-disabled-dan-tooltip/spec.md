---
id: TC-FA-LBL-E2E-037-modal-create-edit-label-state-tombol-submit-disabled-dan-tooltip
title: "Modal Create/Edit Label: state tombol (Disabled, Loading) dan tooltip lewat keyboard"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:component-states/buttons
  - FALB:component-states/disabled-vs-hidden
  - FALB:aksesibilitas/tooltip-dapat-diakses-lewat-keyboard-foc
coverage:
  web: automated
---

# Modal Create/Edit Label: state tombol (Disabled, Loading) dan tooltip lewat keyboard

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-67` (label seed `Mdl-{runId}-037` berwarna `#3B82F6`, dibuat lewat sesi API di hook `before`; dipakai sebagai target mode Edit dan sebagai nama duplikat pada form Create). Nama valid baru yang belum dipakai label lain pada langkah 4 dan 32 adalah `DU-67` dengan akhiran `-Baru`. Nama 121 karakter pada langkah 29 adalah karakter pengisi sepanjang 121 karakter tanpa suffix.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding dan penghapusan label. `Spectra.intercept()` untuk menahan respons permintaan simpan Edit Label (endpoint dari openapi dan LLD modul, ditentukan di tahap script).
- Jeda nyata: tidak ada penantian waktu; langkah 16 menunggu modal tertutup.
- State global: tidak ada yang diubah selain label `DU-67` (warna diubah pada langkah 10). Hook `after` melepas intercept bila masih terpasang dan menghapus label `DU-67` lewat sesi API walau spec gagal di tengah.

## Test Steps

### FALB:component-states/buttons: State tombol Normal, Disabled, dan Loading

1. Ketik Search `DU-67` (nama dasar `Mdl-{runId}-037`), tekan Enter
2. Klik `[+ Label]`
3. Verifikasi tombol `[Submit]` Disabled pada form Create dengan Label Name kosong
4. Ketik Label Name `DU-67` dengan akhiran `-Baru`
5. Verifikasi tombol `[Submit]` Enabled
6. Klik `[Clear Field]`
7. Klik `[✕]` pada header Modal Create Label
8. Klik `[⋯]` pada baris label `DU-67`, pilih `Edit`
9. Klik Swatch Trigger
10. Klik swatch preset baris 1 kolom 1 (`#EF4444`)
11. Klik Swatch Trigger untuk menutup Color Picker Overlay
12. Tahan respons permintaan simpan Edit Label lewat `Spectra.intercept()`
13. Klik `[Save]`
14. Verifikasi tombol `[Save]` menampilkan spinner yang menggantikan teks tombol (Loading)
15. Lepas tahanan respons
16. Tunggu hingga Modal Edit Label tertutup

### FALB:component-states/disabled-vs-hidden: Submit Disabled dengan tooltip dan fallback inline

17. Klik `[+ Label]`
18. Arahkan kursor ke tombol `[Submit]` yang Disabled
19. Verifikasi tooltip `Enter a label name to continue.` tampil pada tombol `[Submit]`
20. Ketik beberapa spasi saja pada field Label Name
21. Verifikasi tombol `[Submit]` Disabled
22. Tekan Enter pada field Label Name
23. Verifikasi inline error `Label name must not be empty` tampil di bawah field Label Name
24. Ganti isi field Label Name dengan `DU-67`
25. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name tanpa field kehilangan fokus
26. Verifikasi tombol `[Submit]` Disabled
27. Arahkan kursor ke tombol `[Submit]` yang Disabled
28. Verifikasi tooltip `Label name already exists` tampil pada tombol `[Submit]`
29. Ganti isi field Label Name dengan nama 121 karakter
30. Verifikasi inline error `Max. 120 characters` tampil di bawah field Label Name
31. Verifikasi tombol `[Submit]` Disabled
32. Ganti isi field Label Name dengan `DU-67` dengan akhiran `-Baru`
33. Verifikasi tombol `[Submit]` Enabled saat pengecekan keunikan debounce masih berjalan
34. Klik Swatch Trigger
35. Ketik kode hex kurang dari 6 digit pada kolom Hex
36. Verifikasi inline error `Invalid color format` tampil di dalam Color Picker Overlay
37. Verifikasi tombol `[Submit]` Disabled
38. Klik Swatch Trigger untuk menutup Color Picker Overlay
39. Verifikasi inline error `Invalid color format` hilang, kolom Hex kembali ke warna valid terakhir `#3B82F6`, dan tombol `[Submit]` Enabled

### FALB:aksesibilitas/tooltip-dapat-diakses-lewat-keyboard-foc: Tooltip lewat keyboard focus

40. Klik `[Clear Field]`
41. Tekan Tab hingga fokus keyboard berada pada tombol `[Submit]` yang Disabled
42. Verifikasi tooltip `Enter a label name to continue.` tampil pada tombol `[Submit]` lewat fokus keyboard
43. Klik `[✕]` pada header Modal Create Label

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit tabel ke label `DU-67`, R-16), langkah 2, 8, 17, dan 34 (membuka modal dan overlay), langkah 6 dan 7 (mengosongkan form lalu menutup modal bersih tanpa dialog), langkah 9 sampai 11 (menyiapkan perubahan warna agar `[Save]` dapat diklik), langkah 12 dan 15 (menahan dan melepas respons, bagian 8b butir 5), langkah 16 (menunggu aksi selesai), langkah 40 dan 43 (mengosongkan form dan menutup modal bersih).
- Asersi state sementara tepat waktu (bagian 8b butir 5): langkah 14 diasersi selama respons ditahan, sebelum langkah 15.
- Pembagian klausa lintas spec: klausa "elemen yang dibatasi otorisasi role disembunyikan (`Hidden`)" dari `FALB:component-states/disabled-vs-hidden` diasersi di spec 058 dan 059; spec ini mengasersi klausa Disabled (nama kosong atau hanya spasi, inline error), tooltip, dan V-01 sebagai fallback inline.
- Klausa di luar E2E: `FALB:component-states/disabled-vs-hidden` (Submit Disabled selama inline error `V-08` masih tampil): inline error `V-08` hanya muncul bila emoji lolos filter keystroke dan paste, dan PRD tidak menyediakan mekanisme UI untuk memicunya; klausa ini tidak diasersi. Rujukan tc-backend tidak ada.
- Temuan PRD: `FALB:component-states/buttons` menyebut state Hover dan Active tombol tanpa nilai tampilan yang dapat diasersi (PRD §4.5 hanya menyebut nama state); Hover dan Active tidak diasersi, sedangkan Normal, Disabled, dan Loading diasersi di spec ini.
- Spec ini di atas smell 35 langkah (43 langkah). Alasan dipertahankan: seluruh blok satu kelas harness (state tombol pada Modal yang sama), tiap blok dimulai dengan mengganti isi field atau membuka modal dari keadaan bersih, dan data blok (`DU-67`) disiapkan hook `before`; kegagalan satu blok tidak membuat blok lain kehilangan makna.
