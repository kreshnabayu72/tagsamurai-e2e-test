---
id: TC-GS-USER-E2E-027-create-foto-profil-hover-file-picker-kompres-dan-batas-ukuran
title: "Create: foto profil (hover, file picker, kompres, batas ukuran, tutup tanpa Submit)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-126
  - TC-GS-USER-127
  - TC-GS-USER-128
  - TC-GS-USER-129
  - TC-GS-USER-130
  - TC-GS-USER-1040
coverage:
  web: automated
---

# Create: foto profil (hover, file picker, kompres, batas ukuran, tutup tanpa Submit)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Layar awal: hook `beforeEach` mengembalikan layar ke Global Settings > User > User List, sub-tab Login User.
- Data Pre-setup (hanya dibaca): Division `Finance` (No. 23); opsi Access `Fixed Asset` (No. 26).
- Berkas foto uji (disediakan tim FE sebagai fixture berkas, sampleImage): `budi.png` (PNG kecil, di bawah 1 MB), `large.jpg` (3 MB, JPG), `huge.jpg` (12 MB, JPG).
- Data Dinamis (dibuat oleh TC-GS-USER-128 lewat UI; tidak ada seeding): First Name `Budi`, Last Name `Santoso {runId}-027`, Email `budisantoso+{runId}-027@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`, Foto `large.jpg`.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut mekanismenya):
  - Memilih berkas pada file chooser browser tanpa dialog native (file chooser dikendalikan test runner).
  - Membaca filter tipe berkas yang ditawarkan file picker Photo (atribut tipe berkas yang diterima input file) untuk TC-GS-USER-129.
  - Memantau request jaringan ke server selama langkah Delete foto (TC-GS-USER-127).
  - Membaca ukuran berkas foto tersimpan milik user hasil TC-GS-USER-128, jumlah user Login pada entitas, dan jumlah berkas foto tersimpan di penyimpanan (TC-GS-USER-128 dan 130).
- Cleanup di hook `after` (tidak berasumsi alur berhasil penuh): hapus lewat API user bersuffix `{runId}-027` beserta berkas fotonya.
- State global yang diubah: Custom Field `Emergency Phone` tidak Required selama spec ini (Tabel Pre-setup No. 24: Required hanya aktif untuk TC-GS-USER-158 dan 349, TC Create dan Edit lain dijalankan saat Required nonaktif; TC-GS-USER-128 tidak mengisinya dan mengharapkan Create sukses). Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal, hook `after` memulihkannya walau spec gagal di tengah. Spec membuat data dalam suite serial.

## Test Steps

### TC-GS-USER-126: Hover Avatar sebelum memilih file hanya menampilkan [Edit]

1. Klik `[+ User]` di Table Tools
2. Hover avatar Photo
3. Verifikasi overlay `[Edit]` tampil pada avatar
4. Verifikasi `[Delete]` tidak tampil pada overlay avatar
5. Verifikasi avatar menampilkan placeholder kosong

### TC-GS-USER-129: File picker Photo hanya menawarkan PNG/JPG/JPEG

6. Klik `[Edit]` pada overlay avatar untuk membuka file picker
7. Verifikasi file picker memfilter PNG, JPG, JPEG
8. Verifikasi tidak ada pesan error format
9. Batalkan file picker tanpa memilih berkas

### TC-GS-USER-127: Setelah memilih file, hover Avatar menampilkan [Edit] dan [Delete]; [Delete] membatalkan pilihan

10. Klik `[Edit]` pada overlay avatar, pilih `budi.png`
11. Verifikasi avatar menampilkan preview `budi.png`
12. Hover avatar Photo
13. Verifikasi overlay avatar menampilkan `[Edit]` dan `[Delete]`
14. Mulai pantau request jaringan ke server
15. Klik `[Delete]` pada overlay avatar
16. Verifikasi tidak ada dialog konfirmasi
17. Verifikasi avatar kembali kosong
18. Verifikasi tidak ada request ke server selama langkah 15
19. Verifikasi tidak ada toast

### TC-GS-USER-1040: Foto lebih dari 10 MB ditolak dengan toast error

20. Isi First Name `Budi`, Last Name `Santoso {runId}-027`, Division `Finance`, Email `budisantoso+{runId}-027@qwertysystem.net`, pilih Access `Fixed Asset`
21. Klik `[Edit]` pada overlay avatar, pilih `huge.jpg` (12 MB)
22. Verifikasi toast error: "Error, failed to upload photo."
23. Verifikasi avatar tetap tanpa foto
24. Verifikasi Popup Create tetap terbuka
25. Verifikasi field lain tidak berubah: First Name `Budi`, Last Name `Santoso {runId}-027`, Division `Finance`, Email `budisantoso+{runId}-027@qwertysystem.net`, Access `Fixed Asset` terpilih
26. Tunggu toast error tertutup

### TC-GS-USER-128: Foto lebih dari 1 MB otomatis dikompres tanpa error

27. Klik `[Edit]` pada overlay avatar, pilih `large.jpg` (3 MB)
28. Verifikasi avatar menampilkan preview `large.jpg`
29. Verifikasi tidak ada pesan error ukuran file
30. Klik `[Submit]`
31. Verifikasi toast sukses: "Success, user has been created."
32. Verifikasi foto user `Budi Santoso {runId}-027` tersimpan dengan ukuran 1 MB atau kurang

### TC-GS-USER-130: Tutup Popup setelah memilih foto tanpa Submit tidak menyimpan foto

33. Catat baseline jumlah user Login pada entitas dan jumlah berkas foto tersimpan
34. Klik `[+ User]` di Table Tools
35. Klik `[Edit]` pada overlay avatar, pilih `budi.png`
36. Klik `✕`
37. Verifikasi dialog `Unsaved Changes` tampil
38. Klik `[Leave]`
39. Verifikasi Popup Create tertutup
40. Verifikasi jumlah user Login pada entitas sama dengan baseline
41. Verifikasi jumlah berkas foto tersimpan sama dengan baseline

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (41 langkah) karena seluruh TC berada di satu kelas (foto profil di Popup Create) dan satu layar, dengan satu pembukaan form dipakai bersama oleh TC-GS-USER-126, 129, 127, 1040, dan 128. Tiap blok mengamati state avatar yang berbeda dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan form dilakukan dua kali (langkah 1 dan 34) sesuai dua kejadian penutupan form (Submit sukses pada langkah 30 dan penutupan dirty pada langkah 36).
- Urutan TC sumber diubah: TC-GS-USER-129 diasersi sesudah TC-GS-USER-126 karena keduanya mengamati avatar sebelum ada berkas terpilih (8b butir 5), TC-GS-USER-1040 sebelum TC-GS-USER-128 karena TC-GS-USER-1040 harus berlangsung pada avatar tanpa foto dan field lain sudah terisi agar "field lain tidak berubah" dapat diasersi; TC-GS-USER-128 berakhir dengan Submit sukses, dan TC-GS-USER-130 (menutup form dirty) paling akhir (bagian 3 prinsip 6). Field wajib diisi pada langkah 20 (langkah 3 TC-GS-USER-128) dan dipakai bersama oleh TC-GS-USER-1040 dan TC-GS-USER-128.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 9 (membatalkan file picker agar TC-GS-USER-127 dapat melanjutkan di Popup yang sama), 14 (memulai pemantauan request), 26 (menunggu toast error tertutup agar asersi absence error pada langkah 29 tidak terganggu toast TC-GS-USER-1040), 33 (baseline).
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 28 (preview `large.jpg`) menjadi anchor positif untuk asersi absence error ukuran file pada langkah 29 (8b butir 2); langkah 37 (dialog `Unsaved Changes`) memenuhi penutupan form dirty yang deterministik (S-08).
- Temuan untuk QA:
  - TC-GS-USER-129 bertanda Automation `Manual Only` (satu-satunya dari enam TC spec ini) padahal Expected dapat dicek dari atribut tipe berkas input file; spec memasukkannya (bagian 2 konvensi) dan kemampuan membaca filter file picker disediakan tim FE.
  - TC-GS-USER-129 Expected b "Tidak ada pesan error format" tidak punya pemicu (tidak ada berkas dipilih); spec mengasersi tidak ada pesan error saat file picker terbuka.
  - TC-GS-USER-127 Expected c "tanpa request ke server" tidak menyebut cara memantau request; kemampuan disediakan tim FE.
  - TC-GS-USER-128 Expected c "Foto tersimpan dengan ukuran ≤1 MB" dan TC-GS-USER-130 Expected b "Tidak ada user dan file foto baru tersimpan" tidak menyebut cara membaca ukuran dan jumlah berkas di penyimpanan; kemampuan disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-GS-USER-130 Expected b: TC tidak mengisi field wajib sehingga user tidak mungkin dibuat walau Popup ditutup tanpa dialog; spec mengasersi jumlah user dan berkas foto sama dengan baseline.
  - TC-GS-USER-1040 Expected c "field lain tidak berubah" tidak bermakna bila tidak ada field terisi; spec mengisi field wajib sebelum memilih `huge.jpg` (langkah 20).
  - TC-GS-USER-1040 langkah 3 "Amati avatar dan toast" tidak menyebut nama berkas yang dihasilkan; `huge.jpg` 12 MB disediakan tim FE.
  - TC-GS-USER-128: langkah TC tidak mengisi `Emergency Phone`; Tabel Pre-setup No. 24 menyatakan Required hanya aktif untuk TC-GS-USER-158 dan 349. Spec mengikuti TC; Required nonaktif selama spec (lihat Prerequisites, State global).
