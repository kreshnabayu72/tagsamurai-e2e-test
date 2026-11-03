---
id: TC-FA-FAAM-E2E-058-edit-screening-clear-field-dan-aksesibilitas
title: "Edit: Screening Popup Nilai Tersimpan, Clear Field Bukan Revert, dan Aksesibilitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-170
  - TC-FA-FAAM-171
  - TC-FA-FAAM-172
coverage:
  web: automated
---

# Edit: Screening Popup Nilai Tersimpan, Clear Field Bukan Revert, dan Aksesibilitas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`. Pada spec ini baris itu hanya dibuka, divalidasi, dan dibatalkan atau ditolak validasi; tidak ada yang disimpan sehingga Last Updated tidak berubah (S-06, pengecualian aksi dibatalkan atau ditolak).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-170: Screening Popup Edit Asset Name dengan nilai tersimpan

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Verifikasi Title `Edit Asset Name` dan icon `[✕]` tampil
4. Verifikasi field Asset Name pre-filled `Edit Target Item`
5. Verifikasi field Code pre-filled `ETI`
6. Verifikasi teks Category pre-filled `IT Equipment`
7. Verifikasi chip TAG Type `QR` terpilih
8. Verifikasi chip Brand `Dell` terpilih
9. Verifikasi tabel Model/Type baris Dell berisi `5420`
10. Verifikasi field UoM pre-filled `Unit`
11. Verifikasi footer berisi `[Clear Field]` dan `[Save]`
12. Verifikasi checkbox `Stay on this form after submitting` tidak ada

### TC-FA-FAAM-171: Clear Field pada Edit mengosongkan semua field dan bukan revert ke nilai tersimpan

13. Klik `[Clear Field]`
14. Verifikasi field Asset Name kosong
15. Verifikasi field Code kosong
16. Verifikasi field Category kosong
17. Verifikasi field TAG Type kosong
18. Verifikasi field Brand kosong
19. Verifikasi field UoM kosong
20. Verifikasi tabel Model/Type per Brand hilang
21. Verifikasi modal tetap terbuka (Title `Edit Asset Name` tampil)
22. Verifikasi tidak ada dialog Unsaved Changes
23. Verifikasi fokus berada di field Asset Name
24. Klik `[✕]` pada modal Edit
25. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
26. Klik `[Leave]`

### TC-FA-FAAM-172: Accessibility Popup Edit: aria-required, aria-describedby, focus trap, Esc

27. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
28. Kosongkan field Asset Name
29. Klik `[Save]`
30. Verifikasi field Asset Name memiliki `aria-describedby` yang merujuk pesan error `Asset name must not be empty`
31. Verifikasi field wajib Asset Name, Category, TAG Type, Brand, dan UoM memiliki `aria-required`
32. Tekan Tab berulang kali
33. Verifikasi fokus tetap berada di dalam modal
34. Klik `[✕]` pada modal Edit
35. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
36. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `Edit Target Item` pada langkah 1 untuk menemukan baris target (R-16) dan penutupan modal pada langkah 24 dan 34 sampai 36 (✕, dialog Unsaved Changes, `[Leave]`, S-08).
- TC-FA-FAAM-170 dan 171 dijalankan pada popup yang sama (satu pembukaan untuk dua kasus tanpa submit); `[Clear Field]` pada TC-FA-FAAM-171 dijalankan sesudah screening nilai tersimpan TC-FA-FAAM-170. TC-FA-FAAM-172 membuka popup baru karena membutuhkan field terisi.
- Temuan untuk QA:
  - TC-FA-FAAM-171 Expected a menulis "Semua field kosong"; spec mengasersi enam field (Asset Name, Code, Category, TAG Type, Brand, UoM) satu per satu (S-01).
  - TC-FA-FAAM-172 judul menyebut "Esc" tetapi Langkah Uji dan Expected tidak memuat penekanan Esc; spec mengikuti Langkah Uji dan Expected (tanpa Esc).
  - TC-FA-FAAM-172 Expected b menyebut pesan error tanpa teksnya; spec memakai `Asset name must not be empty` dari TC-FA-FAAM-182 untuk Asset Name kosong.
- Alasan melewati sekitar 35 langkah: seluruh blok memakai popup Edit dari satu dataset yang tidak disimpan (`Edit Target Item`) dan berdiri sendiri; tiap TC membuka dan menutup form sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
