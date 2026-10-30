---
id: TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard
title: "Guided Tooltip Halaman User: Isi 5 Step, Back, Next, Done, dan Navigasi Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-29
  - TC-GS-USER-30
  - TC-GS-USER-31
  - TC-GS-USER-32
  - TC-GS-USER-33
  - TC-GS-USER-36
  - TC-GS-USER-39
coverage:
  web: automated
---

# Guided Tooltip Halaman User: Isi 5 Step, Back, Next, Done, dan Navigasi Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Guided Tooltip: hook suite menyetel flag `gs-user` = seen (lihat `suite.md`). Spec ini menguji walkthrough, sehingga flag `gs-user` akun Total Control dihapus (belum tercatat) lewat langkah eksplisit sesudah hook suite, sebelum bagian TC-GS-USER-29 dan sebelum bagian TC-GS-USER-39. Hook `after` suite memulihkan nilai awal flag walau spec gagal di tengah.
- Kemampuan teknis: menghapus (mereset) flag Guided Tooltip `gs-user` akun aktor lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); tombol keyboard `Enter`, `←`, `Esc`.
- Data: memakai data Pre-setup (hanya dibaca); spec tidak membuat data.
- State global yang diubah: flag Guided Tooltip `gs-user` (dipulihkan seperti di atas).

## Test Steps

### TC-GS-USER-29: Guided tooltip muncul otomatis pada kunjungan pertama halaman User

1. Hapus flag Guided Tooltip `gs-user` akun Total Control lewat API sehingga flag belum tercatat
2. Buka Global Settings > User
3. Verifikasi walkthrough tampil mulai Step 1 dengan target Toolbar Search & Filter
4. Verifikasi Step 1 Title `Search & Filters`
5. Verifikasi Step 1 Description `Narrow down the list to find a specific user. Available filters depend on the table you are viewing.`
6. Verifikasi tombol `[Back]` Hidden di Step 1
7. Verifikasi tombol `[Next]` dan `[Skip]` tampil di Step 1

### TC-GS-USER-30: Guided tooltip Step 2 menampilkan target, title, dan description

8. Klik `[Next]`
9. Verifikasi Step 2 menyorot Toolbar `[+ User]`
10. Verifikasi Step 2 Title `Create User`
11. Verifikasi Step 2 Description `Add a new user and choose which products they can access.`
12. Verifikasi tombol `[Back]` dan `[Next]` tampil di Step 2

### TC-GS-USER-36: Guided tooltip Back kembali ke step sebelumnya

13. Klik `[Back]`
14. Verifikasi kembali ke Step 1 dengan Title `Search & Filters`
15. Verifikasi tombol `[Back]` Hidden lagi

### TC-GS-USER-31: Guided tooltip Step 3 menampilkan target, title, dan description

16. Klik `[Next]` (ke Step 2)
17. Klik `[Next]` (ke Step 3)
18. Verifikasi Step 3 menyorot kolom Toggle Active
19. Verifikasi Step 3 Title `Active Toggle`
20. Verifikasi Step 3 Description `Activate or deactivate users. Some actions are locked for protected users (Default User, yourself, or higher access tiers).`
21. Verifikasi tombol `[Back]` dan `[Next]` tampil di Step 3

### TC-GS-USER-32: Guided tooltip Step 4 menampilkan target, title, dan description

22. Klik `[Next]` (ke Step 4)
23. Verifikasi Step 4 menyorot kolom Access
24. Verifikasi Step 4 Title `Access`
25. Verifikasi Step 4 Description `Shows which products this user can access, displayed as product badges (e.g. "Fixed Asset", "Global Settings"). This is not the user's access level — Total Control and Read Only are managed separately from Role & Permission.`
26. Verifikasi tombol `[Back]` dan `[Next]` tampil di Step 4

### TC-GS-USER-33: Guided tooltip Step 5 menampilkan target, title, dan description

27. Klik `[Next]` (ke Step 5)
28. Verifikasi Step 5 menyorot header kolom Actions `(⋯)`
29. Verifikasi Step 5 Title `Table Columns`
30. Verifikasi Step 5 Description `Choose which columns the table shows and pin the ones you need. Row actions for each user are in the same column.`
31. Verifikasi tombol `[Next]` berganti `[Done]` di Step 5

### TC-GS-USER-39: Accessibility guided tooltip, navigasi keyboard Esc, Enter, dan panah

32. Hapus flag Guided Tooltip `gs-user` akun Total Control lewat API sehingga flag belum tercatat
33. Buka Global Settings > User (muat ulang halaman)
34. Tekan `Enter`
35. Verifikasi `Enter` berpindah ke Step 2
36. Tekan `←`
37. Verifikasi `←` kembali ke Step 1
38. Tekan `Esc`
39. Verifikasi `Esc` menutup walkthrough

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (39 langkah) karena tujuh TC Guided Tooltip berada di satu kelas harness (fungsional, state flag Guided Tooltip akun aktor). TC-GS-USER-29, 30, 36, 31, 32, dan 33 dijalankan berurutan dalam satu walkthrough (Step 1 sampai Step 5) supaya tidak membuka ulang halaman tiga kali; TC-GS-USER-39 berdiri sendiri dengan reset flag dan pembukaan ulang sendiri.
- Urutan TC sumber diubah: TC-GS-USER-36 (Back dari Step 2 ke Step 1) diasersi sebelum TC-GS-USER-31, 32, dan 33 karena walkthrough bergerak maju satu arah. Klik `[Next]` di langkah 8 dipakai bersama oleh TC-GS-USER-30 dan TC-GS-USER-36 (langkah 2 kedua TC identik); langkah 16 mengulang `[Next]` ke Step 2 sebagai langkah penghubung menuju Step 3 untuk TC-GS-USER-31.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 32 (reset flag lewat API sebagai precondition "flag belum tercatat"), 16 (kembali maju ke Step 2), dan 33 (muat ulang untuk kunjungan pertama berikutnya).
- Perilaku `[Skip]`, `[Done]`, penyimpanan flag, replay `[?]`, dan navigasi keluar diuji di spec TC-GS-USER-E2E-006-guided-tooltip-flag-skip-done-replay-dan-navigasi-keluar. Klik `[Done]` pada Step 5 tidak dilakukan di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-39 Expected c menyebut `Esc` menutup walkthrough "sama seperti Skip" tanpa menyatakan apakah flag `gs-user` tercatat; spec hanya mengasersi walkthrough tertutup.
  - Cara menghapus flag `gs-user` tidak didefinisikan di TC dan PRD; disediakan tim FE/BE.
  - TC-GS-USER-30, 31, 32, dan 33 bertanda FE Test `UI Only` sedangkan precondition-nya mensyaratkan flag belum tercatat; spec menjalankannya terhadap backend nyata dalam satu walkthrough bersama TC-GS-USER-29.
