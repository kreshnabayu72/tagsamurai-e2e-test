---
id: TC-GS-USER-E2E-025-create-trim-spasi-first-last-employee-id-dan-email-via-stay-on-form
title: "Create User: Trim Spasi Awal/Akhir First Name, Last Name, Employee ID, dan Email lewat Stay on this form"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-137
  - TC-GS-USER-101
  - TC-GS-USER-102
  - TC-GS-USER-103
  - TC-GS-USER-104
coverage:
  web: automated
---

# Create User: Trim Spasi Awal/Akhir First Name, Last Name, Employee ID, dan Email lewat Stay on this form

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca): Master Data Division `Finance` (No. 23).
- Data Dinamis (dibuat lewat UI oleh spec; tidak di-seed). Seluruhnya dihapus di hook `after` lewat API menurut Email, tanpa mengandalkan Submit berhasil penuh:
  - U-1 (TC-GS-USER-137): Name `Budi Santoso {runId}-025-137`, Email `budisantoso+{runId}-025-137@qwertysystem.net`.
  - U-2 (TC-GS-USER-101): First Name `  Budi  ` (spasi di awal dan akhir), Last Name `Santoso {runId}-025-101`, Email `budisantoso+{runId}-025-101@qwertysystem.net`.
  - U-3 (TC-GS-USER-102): First Name `Budi`, Last Name `  Santoso {runId}-025-102  ` (spasi di awal dan akhir), Email `budisantoso+{runId}-025-102@qwertysystem.net`.
  - U-4 (TC-GS-USER-103): First Name `Budi`, Last Name `Santoso {runId}-025-103`, Employee ID `  EMP-0099-{runId}-025  ` (spasi di awal dan akhir), Email `budisantoso+{runId}-025-103@qwertysystem.net`.
  - U-5 (TC-GS-USER-104): First Name `Budi`, Last Name `Santoso {runId}-025-104`, Email `  budisantoso+{runId}-025-104@qwertysystem.net  ` (spasi di awal dan akhir).
  - Setiap user memakai Division `Finance` dan Access `Fixed Asset`.
- State global yang diubah: Custom Field `Emergency Phone` tidak Required selama spec ini (TC-GS-USER-137 dan 101 sampai 104 tidak mengisi Custom Field; Tabel Pre-setup No. 24 mendefinisikannya Required). Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal, hook `after` memulihkannya walau spec gagal di tengah. Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE bila belum ada): mengetik nilai dengan spasi di awal dan akhir ke field; Search di User List menurut Name (kolom yang dicari ditentukan tim FE); membaca teks Detail apa adanya (tanpa normalisasi spasi) untuk membedakan nilai ber-spasi tepi dan ter-trim.

## Test Steps

### Pembukaan layar

1. Pilih 100 baris per halaman pada Pagination
2. Klik `[+ User]` di Table Tools

### TC-GS-USER-137: Create dengan Stay on this form, Popup tetap terbuka dan form ter-reset

3. Isi First Name `Budi`, Last Name `Santoso {runId}-025-137`, Division `Finance`, Email `budisantoso+{runId}-025-137@qwertysystem.net`, pilih Access `Fixed Asset`
4. Centang `Stay on this form after submitting`
5. Klik `[Submit]`
6. Verifikasi toast sukses: "Success, user has been created."
7. Verifikasi Popup tetap terbuka
8. Verifikasi seluruh field kembali kosong
9. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
10. Verifikasi baris `Budi Santoso {runId}-025-137` muncul di tabel di belakang Popup

### TC-GS-USER-101, 102, 103, 104: pembuatan user dengan spasi tepi (Popup tetap terbuka karena Stay on this form)

11. Isi First Name `  Budi  `, Last Name `Santoso {runId}-025-101`, Division `Finance`, Email `budisantoso+{runId}-025-101@qwertysystem.net`, pilih Access `Fixed Asset`
12. Tunggu toast sukses hilang otomatis
13. Klik `[Submit]`
14. Verifikasi toast sukses: "Success, user has been created." (TC-GS-USER-101)
15. Isi First Name `Budi`, Last Name `  Santoso {runId}-025-102  `, Division `Finance`, Email `budisantoso+{runId}-025-102@qwertysystem.net`, pilih Access `Fixed Asset`
16. Tunggu toast sukses hilang otomatis
17. Klik `[Submit]`
18. Verifikasi toast sukses: "Success, user has been created." (TC-GS-USER-102)
19. Isi First Name `Budi`, Last Name `Santoso {runId}-025-103`, Division `Finance`, Email `budisantoso+{runId}-025-103@qwertysystem.net`, pilih Access `Fixed Asset`, Employee ID `  EMP-0099-{runId}-025  `
20. Tunggu toast sukses hilang otomatis
21. Klik `[Submit]`
22. Verifikasi toast sukses: "Success, user has been created." (TC-GS-USER-103)
23. Isi First Name `Budi`, Last Name `Santoso {runId}-025-104`, Division `Finance`, pilih Access `Fixed Asset`, Email `  budisantoso+{runId}-025-104@qwertysystem.net  `
24. Tunggu toast sukses hilang otomatis
25. Klik `[Submit]`
26. Verifikasi toast sukses: "Success, user has been created." (TC-GS-USER-104)
27. Klik `✕` di header Popup

### TC-GS-USER-101: Detail, First Name ter-trim

28. Klik icon Search, ketik `{runId}-025-101`, tekan Enter
29. Buka Detail user baru `Budi Santoso {runId}-025-101`
30. Verifikasi First Name tersimpan tanpa spasi awal/akhir: nama lengkap Detail sama persis `Budi Santoso {runId}-025-101`

### TC-GS-USER-102: Detail, Last Name ter-trim

31. Buka Global Settings > User > User List (sub-tab Login User)
32. Klik icon Search, ketik `{runId}-025-102`, tekan Enter
33. Buka Detail user baru `Budi Santoso {runId}-025-102`
34. Verifikasi Last Name tersimpan tanpa spasi awal/akhir: nama lengkap Detail sama persis `Budi Santoso {runId}-025-102`

### TC-GS-USER-103: Detail, Employee ID ter-trim

35. Buka Global Settings > User > User List (sub-tab Login User)
36. Klik icon Search, ketik `{runId}-025-103`, tekan Enter
37. Buka Detail user baru `Budi Santoso {runId}-025-103`
38. Verifikasi Employee ID tersimpan tanpa spasi awal/akhir: Employee ID di Detail sama persis `EMP-0099-{runId}-025`

### TC-GS-USER-104: Detail, Email ter-trim

39. Buka Global Settings > User > User List (sub-tab Login User)
40. Klik icon Search, ketik `{runId}-025-104`, tekan Enter
41. Buka Detail user baru `Budi Santoso {runId}-025-104`
42. Verifikasi Email tersimpan tanpa spasi awal/akhir: Email di Detail sama persis `budisantoso+{runId}-025-104@qwertysystem.net`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: TC-GS-USER-137, lalu pembuatan TC-GS-USER-101 sampai 104, lalu Detail TC-GS-USER-101 sampai 104. TC-GS-USER-101 sampai 104 pada TC sumber masing-masing membuka Popup baru, menekan `[Submit]` (Popup menutup), lalu membuka Detail. Spec memakai checkbox `Stay on this form after submitting` yang tetap tercentang dari TC-GS-USER-137 supaya keempat user dibuat dalam satu pembukaan Popup (prinsip 8 bagian 3 konvensi), lalu menutup Popup dan membuka Detail tiap user. Asersi toast tiap TC berada tepat sesudah `[Submit]`-nya; asersi Detail berada sesudah Popup ditutup.
- Popup ditutup lewat `✕` sesudah `[Submit]` terakhir dengan form kosong (ter-reset oleh Stay on this form), sehingga tidak ada form dirty dan tidak ada dialog `Unsaved Changes`.
- Spec melewati sekitar 35 langkah (42 langkah) karena seluruh blok berada di satu kelas harness (Create sukses dengan trim spasi, tanpa harness eksternal), memakai satu sesi Popup untuk lima pembuatan, dan tiap blok Detail berdiri sendiri pada user miliknya sendiri (kegagalan satu blok Detail tidak membuat blok lain kehilangan makna). Pembukaan User List yang berulang pada blok Detail tidak dihitung.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): memilih 100 baris per halaman supaya baris `Budi Santoso {runId}-025-137` tampil di tabel di belakang Popup tanpa Search (Search tidak dapat dipakai saat Popup terbuka; sort default Name A-Z); `✕` di header Popup; Search menurut `{runId}-025-<TC>` untuk menemukan baris sebelum membuka Detail; membuka User List di awal tiap blok Detail.
- Tiap Verifikasi toast mengacu pada toast yang muncul sesudah `[Submit]` pada langkah sebelumnya; toast sukses identik tampil berurutan (kelima `[Submit]`), sehingga sebelum `[Submit]` ke-2 sampai ke-5 ada langkah `Tunggu toast sukses hilang otomatis` (langkah 12, 16, 20, dan 24) agar tiap `Verifikasi` toast membaca toast milik `[Submit]`-nya sendiri, bukan toast sebelumnya (R-12).
- Temuan untuk QA:
  - TC-GS-USER-101 sampai 104 memakai Email dan nama `Budi Santoso` / `budisantoso@qwertysystem.net` yang sama dengan TC-GS-USER-137; Email unik global, sehingga kelima user tidak dapat ada bersamaan. Spec memakai suffix `{runId}-025-<TC>` per user.
  - TC-GS-USER-101 sampai 104 menyebut "Buka Detail user baru" dan Expected "tersimpan tanpa spasi awal/akhir" tanpa menyebut elemen Detail yang diperiksa dan tanpa cara membedakan spasi (HTML menormalkan spasi saat dirender). Spec mengasersi teks Detail apa adanya: nama lengkap (First Name dan Last Name), Employee ID, dan Email; kemampuan membaca teks apa adanya disediakan tim FE.
  - TC-GS-USER-101 Langkah Uji mengisi First Name `Budi` lalu mengisinya lagi dengan `  Budi  `; spec mengisi `  Budi  ` sekali (hasil akhir sama). Hal yang sama berlaku untuk TC-GS-USER-102, 103, dan 104.
  - TC-GS-USER-137 Expected d menyebut baris muncul "di belakang popup" tanpa menyebut halaman tabel; spec memilih 100 baris per halaman.
  - Tabel Pre-setup No. 24 mendefinisikan `Emergency Phone` Required, sedangkan TC-GS-USER-137 dan 101 sampai 104 tidak mengisi Custom Field; spec mensyaratkan status Required dimatikan selama spec (disediakan tim FE/BE).
