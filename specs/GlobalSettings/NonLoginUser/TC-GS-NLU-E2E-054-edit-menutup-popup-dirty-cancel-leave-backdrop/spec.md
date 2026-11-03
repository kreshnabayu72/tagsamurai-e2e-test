---
id: TC-GS-NLU-E2E-054-edit-menutup-popup-dirty-cancel-leave-backdrop
title: "Edit: menutup Popup dirty, Cancel, Leave, backdrop"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-138
  - TC-GS-NLU-139
  - TC-GS-NLU-140
  - TC-GS-NLU-446
  - TC-GS-NLU-447
coverage:
  web: automated
---

# Edit: menutup Popup dirty, Cancel, Leave, backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Non-Login User Budi Kurniawan (First Name `Budi`, Field Technician, Operations, Represented By Ahmad Fauzi). Popup Edit Budi Kurniawan hanya dibuka dan ditutup tanpa Save sehingga data tidak berubah.
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Klik `⋯` pada baris Budi Kurniawan > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-138: Menutup Popup Edit tanpa perubahan tidak memunculkan dialog Unsaved Changes

3. Klik `✕`
4. Verifikasi Popup Edit langsung tertutup tanpa dialog (cara `✕`)
5. Klik `⋯` pada baris Budi Kurniawan > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
6. Tekan `Esc`
7. Verifikasi Popup Edit langsung tertutup tanpa dialog (cara `Esc`)
8. Klik `⋯` pada baris Budi Kurniawan > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-140: Klik backdrop pada Popup Edit tidak menutup popup

9. Klik area gelap di luar popup
10. Verifikasi Popup Edit tetap terbuka (klik pertama)
11. Verifikasi tidak ada dialog (klik pertama)
12. Ubah First Name menjadi `Budi2`
13. Klik area gelap di luar popup
14. Verifikasi Popup Edit tetap terbuka (klik kedua)
15. Verifikasi tidak ada dialog (klik kedua)

### TC-GS-NLU-139: Menutup Popup Edit yang sudah diubah memunculkan dialog Unsaved Changes

16. Klik `✕`
17. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
18. Verifikasi Popup Edit masih terbuka di belakang dialog

### TC-GS-NLU-446: Cancel pada dialog Unsaved Changes Edit mempertahankan perubahan

19. Klik `[Cancel]` pada dialog
20. Verifikasi dialog tertutup
21. Verifikasi Popup Edit tetap terbuka
22. Verifikasi First Name tetap `Budi2`

### TC-GS-NLU-447: Leave pada dialog Unsaved Changes Edit membuang perubahan dan menutup popup

23. Klik `✕`
24. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
25. Klik `[Leave]` pada dialog
26. Verifikasi dialog dan Popup Edit tertutup
27. Verifikasi nilai First Name baris Budi Kurniawan di tabel tetap `Budi` dan tidak ada perubahan tersimpan

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC diubah: TC-GS-NLU-138 (tanpa perubahan) lebih dulu, lalu TC-GS-NLU-140, TC-GS-NLU-139, TC-GS-NLU-446, dan TC-GS-NLU-447 pada satu pembukaan popup dengan First Name `Budi2` yang sama. Alasan: TC-GS-NLU-446 dan TC-GS-NLU-447 bergantung pada keadaan dirty TC-GS-NLU-139 (Dependensi), dan TC-GS-NLU-140 mengubah First Name menjadi `Budi2` sehingga dipakai sebagai keadaan dirty yang sama (halaman yang sama dipakai berulang). Jumlah pembukaan popup tidak melebihi jumlah penutupan (S-10).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search untuk menemukan baris target, R-16) dan langkah 8 (membuka kembali Popup Edit sesudah penutupan TC-GS-NLU-138).
- Spec berakhir dengan popup tertutup lewat `[Leave]` sehingga tidak ada form dirty tersisa.
- Temuan untuk QA:
  - TC-GS-NLU-139 dan TC-GS-NLU-140 memakai First Name `Budi2` pada langkah berbeda; spec memakai perubahan First Name yang sama untuk keduanya.
  - TC-GS-NLU-447 langkah 4 menyatakan nilai First Name di tabel tetap `Budi`, sedangkan tabel menampilkan Name lengkap; spec mengasersi First Name pada baris Budi Kurniawan.
