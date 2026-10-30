---
id: TC-GS-USER-E2E-006-guided-tooltip-flag-skip-done-replay-dan-navigasi-keluar
title: "Guided Tooltip Halaman User: Flag Seen, Skip, Done, Replay Tombol [?], dan Navigasi Keluar Tanpa Selesai"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-34
  - TC-GS-USER-35
  - TC-GS-USER-37
  - TC-GS-USER-38
coverage:
  web: automated
---

# Guided Tooltip Halaman User: Flag Seen, Skip, Done, Replay Tombol [?], dan Navigasi Keluar Tanpa Selesai

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Guided Tooltip: hook suite menyetel flag `gs-user` = seen (lihat `suite.md`). Spec ini menguji flag itu, sehingga flag `gs-user` akun Total Control dihapus (belum tercatat) lewat langkah eksplisit sesudah hook suite, sebelum bagian TC-GS-USER-34, TC-GS-USER-35, dan TC-GS-USER-38. Bagian TC-GS-USER-37 memakai flag yang sudah tercatat sebagai hasil `[Done]` di TC-GS-USER-35. Hook `after` suite memulihkan nilai awal flag walau spec gagal di tengah.
- Kemampuan teknis: menghapus (mereset) flag Guided Tooltip `gs-user` akun aktor lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); muat ulang halaman (F5).
- Data: memakai data Pre-setup (hanya dibaca); spec tidak membuat data.
- State global yang diubah: flag Guided Tooltip `gs-user` (dipulihkan seperti di atas).

## Test Steps

### TC-GS-USER-34: Guided tooltip Skip menutup walkthrough dan tidak muncul otomatis lagi

1. Hapus flag Guided Tooltip `gs-user` akun Total Control lewat API sehingga flag belum tercatat
2. Buka Global Settings > User
3. Klik `[Skip]` di Step 1
4. Verifikasi walkthrough tertutup
5. Muat ulang halaman (F5)
6. Verifikasi tabel User List tampil
7. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang

### TC-GS-USER-35: Guided tooltip Done di Step 5 menutup walkthrough dan menandai selesai

8. Hapus flag Guided Tooltip `gs-user` akun Total Control lewat API sehingga flag belum tercatat
9. Muat ulang halaman Global Settings > User
10. Klik `[Next]` (ke Step 2)
11. Klik `[Next]` (ke Step 3)
12. Klik `[Next]` (ke Step 4)
13. Klik `[Next]` (ke Step 5)
14. Klik `[Done]`
15. Verifikasi walkthrough tertutup setelah `[Done]`
16. Klik menu lain di sidebar (bukan User)
17. Klik menu User di sidebar Global Settings
18. Verifikasi tabel User List tampil
19. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### TC-GS-USER-37: Guided tooltip replay via tombol [?] mulai dari Step 1

20. Klik tombol `[?]` di header
21. Verifikasi walkthrough mulai dari Step 1
22. Klik `[Skip]`
23. Klik menu lain di sidebar (bukan User)
24. Klik menu User di sidebar Global Settings
25. Verifikasi tabel User List tampil
26. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### TC-GS-USER-38: Guided tooltip ditutup oleh navigasi keluar tanpa menandai selesai

27. Hapus flag Guided Tooltip `gs-user` akun Total Control lewat API sehingga flag belum tercatat
28. Muat ulang halaman Global Settings > User
29. Klik `[Next]` (ke Step 2)
30. Verifikasi Step 2 tampil
31. Klik menu lain di sidebar (bukan User)
32. Verifikasi walkthrough tertutup saat navigasi
33. Klik menu User di sidebar Global Settings
34. Verifikasi walkthrough muncul otomatis lagi dari Step 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. TC-GS-USER-37 berjalan sesudah TC-GS-USER-35 dalam satu spec karena precondition-nya (flag sudah tercatat, walkthrough pernah diselesaikan) dipenuhi oleh state akhir TC-GS-USER-35 (`[Done]`); TC-GS-USER-38 mereset flag lagi karena TC-GS-USER-37 meninggalkan flag tercatat.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 8, dan 27 (reset flag lewat API sebagai precondition "flag belum tercatat"), 9 dan 28 (muat ulang untuk kunjungan pertama berikutnya), 10 sampai 13 (`[Next]` ke Step 5, dasar langkah 2 TC-GS-USER-35), 22 (menutup walkthrough hasil replay), 23 dan 24 (pindah menu lalu kembali untuk mengamati "kunjungan berikutnya" TC-GS-USER-37), 29 (`[Next]` ke Step 2, precondition langkah 2 TC-GS-USER-38).
- Langkah 6, 18, dan 25 (Verifikasi tabel User List tampil) dan langkah 30 (Verifikasi Step 2 tampil) menjadi anchor positif sebelum asersi "walkthrough tidak muncul" atau sebelum navigasi keluar; langkah itu tidak ada di Expected TC dan ditambahkan sebagai pembanding state halaman.
- Menu lain di sidebar yang dituju di langkah 16, 23, dan 31 ditentukan tim FE (TC tidak menyebut nama menu).
- Isi 5 step, Back, Next, dan navigasi keyboard diuji di spec TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard.
- Temuan untuk QA:
  - TC-GS-USER-35 langkah 4 dan TC-GS-USER-38 langkah 2 ("Buka menu lain", "klik menu lain di sidebar") tidak menyebut menu tujuan; ditentukan tim FE.
  - TC-GS-USER-37 Expected b ("setelah ditutup, kunjungan berikutnya tetap tidak muncul otomatis") tidak menyebut cara menutup; spec memakai `[Skip]`.
  - Cara mereset dan membaca flag `gs-user` tidak didefinisikan di TC dan PRD; disediakan tim FE/BE.
  - TC-GS-USER-34, 35, 37, dan 38 bertanda FE Test `Need API`, tetapi TC tidak menyebut cara membaca flag; spec mengasersi flag lewat perilaku halaman (walkthrough muncul atau tidak), bukan lewat API.
