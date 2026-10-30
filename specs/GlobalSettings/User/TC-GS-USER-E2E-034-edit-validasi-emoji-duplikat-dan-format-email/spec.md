---
id: TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email
title: "Edit User: Validasi Emoji, Duplikat Email dan Employee ID, dan Format Email Tidak Valid"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-176
  - TC-GS-USER-177
  - TC-GS-USER-178
  - TC-GS-USER-179
  - TC-GS-USER-180
  - TC-GS-USER-181
  - TC-GS-USER-182
  - TC-GS-USER-183
coverage:
  web: automated
---

# Edit User: Validasi Emoji, Duplikat Email dan Employee ID, dan Format Email Tidak Valid

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup yang dipakai: Position `Staff` (No. 22), Division `Finance` (No. 23), dan produk `Fixed Asset` (subscription Client, No. 26); hanya dibaca. Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Kedua user: Position `Staff`, Division `Finance`, Access `Fixed Asset` dan `Global Settings`, permanen, Active ON.
  - U-1 (target Edit): First Name `Dewi`, Last Name `Lestari {runId}-034` (Name `Dewi Lestari {runId}-034`), Email `dewilestari+{runId}-034@qwertysystem.net`, Employee ID `EMP-{runId}-034-A`. Pengganti Dewi Lestari (Pre-setup No. 12).
  - U-2 (sumber nilai duplikat): Name `Maya Anggraini {runId}-034`, Email `mayaanggraini+{runId}-034@qwertysystem.net`, Employee ID `EMP-{runId}-034-B`. Pengganti John Doe dan `EMP-0001` pada TC sumber.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-1 dan U-2 lewat API.
- Kemampuan teknis: mengetik karakter emoji lewat keyboard; menyetel nilai field langsung di DOM (bypass filter keystroke FE) untuk TC-GS-USER-177 dan 179; jeda pendek ±500 ms (debounce validasi duplikat) sebagai satu-satunya jeda waktu; membaca inline error.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-USER-176: Emoji diblok saat diketik di First Name

1. Buka Global Settings > User > User List, sub-tab Login User
2. Klik icon Search, ketik `Dewi Lestari {runId}-034`, tekan Enter
3. Buka row action baris `Dewi Lestari {runId}-034` lalu klik `Edit`
4. Ketik `😊` di akhir First Name
5. Verifikasi emoji tidak masuk field: First Name tetap `Dewi`
6. Verifikasi tidak ada pesan error pada First Name

### TC-GS-USER-177: Emoji First Name yang lolos filter input ditolak validasi FE real-time

7. Injeksi value `Dewi😊` langsung ke DOM field First Name (bypass filter keystroke FE)
8. Verifikasi inline error `First name contains invalid characters` muncul langsung di field, tanpa menunggu Submit
9. Klik `[Save]`
10. Tunggu aksi selesai
11. Isi kembali First Name dengan `Dewi`

### TC-GS-USER-178: Emoji diblok saat diketik di Last Name

12. Ketik `😊` di akhir Last Name
13. Verifikasi emoji tidak masuk field: Last Name tetap `Lestari {runId}-034`
14. Verifikasi tidak ada pesan error pada Last Name

### TC-GS-USER-179: Emoji Last Name yang lolos filter input ditolak validasi FE real-time

15. Injeksi value `Dewi😊` langsung ke DOM field Last Name (bypass filter keystroke FE)
16. Verifikasi inline error `Last name contains invalid characters` muncul langsung di field, tanpa menunggu Submit
17. Klik `[Save]`
18. Tunggu aksi selesai
19. Isi kembali Last Name dengan `Lestari {runId}-034`

### TC-GS-USER-180: Email diubah ke email user lain

20. Ubah Email ke `mayaanggraini+{runId}-034@qwertysystem.net`
21. Tunggu ±500 ms
22. Verifikasi inline error `Email already exists`
23. Isi kembali Email dengan `dewilestari+{runId}-034@qwertysystem.net`

### TC-GS-USER-181: Email milik target sendiri yang diketik ulang identik

24. Hapus 1 karakter di akhir Email lalu ketik ulang karakter yang sama
25. Tunggu ±500 ms
26. Verifikasi Email berisi `dewilestari+{runId}-034@qwertysystem.net`
27. Verifikasi tidak ada error `Email already exists`

### TC-GS-USER-182: Employee ID diubah ke milik user lain

28. Ubah Employee ID ke `EMP-{runId}-034-B`
29. Tunggu ±500 ms
30. Verifikasi inline error `Employee ID already exists`
31. Isi kembali Employee ID dengan `EMP-{runId}-034-A`

### TC-GS-USER-183: Format Email tidak valid ditolak saat Save

32. Ubah Email ke `dewi.qwertysystem.net`
33. Klik `[Save]`
34. Verifikasi inline error `Invalid email format`

### Penutupan form dan data tidak berubah (butir "data tidak berubah" TC-GS-USER-177 dan 179)

35. Klik `[✕]`
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`
38. Verifikasi Popup Edit tertutup
39. Verifikasi baris `Dewi Lestari {runId}-034` di tabel tidak berubah: Name, Email, dan Employee ID sama dengan data seed

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md` (TC-GS-USER-176 sampai 183). Mode FE+BE; kelas harness: validasi form Edit (satu kelas). TC-GS-USER-177 dan 179 bertipe Security di sumber, tetapi memakai injeksi DOM sebagai cara mencapai kondisi, bukan defense-in-depth server (kelas a); asersinya hanya validasi FE real-time sehingga tetap di spec ini.
- Satu pembukaan Edit dengan field dikembalikan ke nilai seed di antara kasus; setiap kasus berakhir tanpa data tersimpan. Form ditutup deterministik lewat `[✕]`, `Unsaved Changes`, `[Leave]` (S-08).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 3 (membuka layar dan form), 10 dan 18 (Tunggu aksi selesai sesudah `[Save]` yang hasilnya tidak diasersi langsung, bagian 8b butir 8), 11, 19, 23, 31 (mengembalikan field ke nilai seed), 35 dan 37 (penutupan). Verifikasi dialog `Unsaved Changes` (langkah 36) dan Popup tertutup (langkah 38) adalah asersi tambahan penutupan deterministik S-08; tidak ada di Expected TC sumber.
- Butir "Setelah klik `[Save]`, data tidak berubah" (TC-GS-USER-177 dan 179) diasersi sekali pada langkah 39 setelah form ditutup.
- Nilai duplikat TC sumber (email John Doe, `EMP-0001`) diganti data U-2 milik spec (S-06); makna tidak berubah karena kasus hanya membutuhkan nilai yang sudah dipakai user lain.
- Pembagian TC lintas spec: TC-GS-USER-176 sampai 183 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-177 dan 179 menjelaskan injeksi DOM tanpa menyebut cara; kemampuan menyetel nilai field langsung di DOM disediakan tim FE.
  - TC-GS-USER-177 dan 179 butir b ("data tidak berubah") tidak menyebut cara memeriksa; spec memeriksa baris tabel setelah form ditutup.
  - TC-GS-USER-181 dan 183 tidak menyebut hasil `[Save]` setelah verifikasi (TC-GS-USER-181 tidak menyimpan; TC-GS-USER-183 hanya error); spec tidak menyimpan data pada kasus apa pun.
- Spec melewati sekitar 35 langkah (39 langkah) karena memuat satu kelas (validasi form Edit), satu layar, satu pembukaan form dipakai bersama, dan tiap blok berdiri sendiri (kegagalan satu field tidak membuat blok field lain kehilangan makna).
