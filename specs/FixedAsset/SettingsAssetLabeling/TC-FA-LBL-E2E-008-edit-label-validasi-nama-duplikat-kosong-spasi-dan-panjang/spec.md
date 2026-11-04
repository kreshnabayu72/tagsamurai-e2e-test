---
id: TC-FA-LBL-E2E-008-edit-label-validasi-nama-duplikat-kosong-spasi-dan-panjang
title: "Edit Label: validasi nama (duplikat, kosong, hanya spasi, dan 121 karakter)"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - FALB:FI-06
  - FALB-LOGIC-01a
  - E-FALB-17
  - F-FALB-03.k2
  - E-FALB-18
  - F-FALB-03.k5
coverage:
  web: automated
---

# Edit Label: validasi nama (duplikat, kosong, hanya spasi, dan 121 karakter)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: label seed milik spec dengan nama awal `DU-49` (`Urgent-{runId}-008`); `DU-22` (nama hasil ubah kapitalisasi `URGENT-{runId}-008`, diketik pada langkah 12); `DU-23` (label pembanding `Other-{runId}-008`); `DU-15` (nama pembanding `DU-23` dengan kapitalisasi dibalik); `DU-16` (nama hanya berisi spasi); `DU-17` (nama 121 karakter setelah trim); `DU-25` (baseline jumlah entri Changelog, System Log, dan Activity Log untuk client ini, dicatat pada langkah 1). Label seed dan pembanding dibuat lewat API di hook `before` dan dihapus di hook `after`.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, disediakan tim FE/BE. Kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log (audit trail permanen, tidak diturunkan dari seeding), disediakan tim FE/BE; baseline dicatat sesudah seeding hook selesai dan sebelum aksi pertama.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat baseline `DU-25`: jumlah entri Changelog, System Log, dan Activity Log untuk client ini lewat kemampuan baca BE

### FALB:FI-06: Checkbox Stay on this form after submitting hanya tampil pada mode Create

2. Ketik Search label seed (nama awal `DU-49`), tekan Enter
3. Klik `[⋯]` pada baris label seed, pilih `Edit`
4. Verifikasi Modal `Edit Label` tampil dengan field Label Name terisi nama awal `DU-49`
5. Verifikasi checkbox `Stay on this form after submitting` tidak tampil pada Modal Edit

### FALB-LOGIC-01a: Nama unik tanpa membedakan huruf besar-kecil setelah di-trim

6. Ganti isi field Label Name dengan `DU-15`
7. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name
8. Ganti isi field Label Name dengan `DU-15` yang diapit satu spasi di depan dan belakang
9. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name

### E-FALB-17: Edit Label dengan nama baru yang sudah dipakai label lain

10. Ganti isi field Label Name dengan `DU-23`
11. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name
12. Ganti isi field Label Name dengan `DU-22`
13. Verifikasi field Label Name terisi `DU-22`
14. Verifikasi inline error `Label name already exists` tidak tampil di bawah field Label Name

### F-FALB-03.k2: Edit ditolak karena nama bentrok dengan label lain

15. Ganti isi field Label Name dengan `DU-23`
16. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name
17. Klik `[×]` pada header Modal Edit Label
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`
20. Verifikasi baris label seed tampil dengan nama awal `DU-49` pada Labels List

### E-FALB-18: Edit Label dengan nama hanya spasi atau 121 karakter

21. Klik `[⋯]` pada baris label seed, pilih `Edit`
22. Ganti isi field Label Name dengan `DU-16`
23. Verifikasi tombol `[Save]` Disabled
24. Tekan Enter pada field Label Name
25. Verifikasi inline error `Label name must not be empty` tampil di bawah field Label Name
26. Ganti isi field Label Name dengan `DU-17`
27. Verifikasi inline error `Max. 120 characters` tampil di bawah field Label Name
28. Verifikasi tombol `[Save]` Disabled

### F-FALB-03.k5: Edit ditolak untuk nama kosong, hanya spasi, atau lebih dari 120 karakter

29. Klik `[Clear Field]`
30. Verifikasi tombol `[Save]` Disabled untuk nama kosong
31. Ganti isi field Label Name dengan `DU-16`
32. Verifikasi tombol `[Save]` Disabled untuk nama `DU-16`
33. Klik `[×]` pada header Modal Edit Label
34. Verifikasi dialog `Unsaved Changes` tampil
35. Klik `[Leave]`
36. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline `DU-25` sama dengan 0

## Notes

- Langkah penghubung: Search label seed (langkah 2) menemukan baris target dan tetap aktif untuk langkah 21; klik `[⋯]` membuka menu baris; langkah 17, 19, 33, dan 35 menutup form dirty secara deterministik (`[×]`, dialog `Unsaved Changes`, `[Leave]`); langkah 29 mengosongkan field sebelum langkah 31; langkah 1 mencatat baseline sebelum aksi pertama.
- Anchor absence: field Label Name terisi `DU-22` (langkah 13) mendahului asersi inline error tidak tampil (langkah 14); Modal Edit Label tampil dengan nama awal (langkah 4) mendahului asersi checkbox `Stay on this form after submitting` tidak tampil (langkah 5).
- Langkah 8 mengetik `DU-15` dengan satu spasi di depan dan belakang untuk klausa "setelah di-trim"; nilai yang diketik tetap `DU-15`.
- Pembagian klausa lintas spec: `FALB-LOGIC-01a` dikutip spec 004 dan spec ini; spec 004 mengasersi jalur Create, spec ini mengasersi jalur Edit. `E-FALB-18` dikutip spec 021 dan spec ini; spec 021 mengasersi jalur Create, spec ini mengasersi jalur Edit. `FALB:FI-06` dikutip spec 002 dan spec ini; spec 002 mengasersi checkbox tampil pada mode Create, spec ini mengasersi checkbox tidak tampil pada mode Edit. Klausa nol entri log `F-FALB-03.k5` dipegang spec ini (langkah 36); klausa nol entri log `F-FALB-02.k4` ada di spec 021.
- Verifikasi `[Save]` Disabled pada langkah 23 dan 28 memenuhi klausa Submit Disabled `E-FALB-18`; langkah 28 (121 karakter), 30 (kosong), dan 32 (hanya spasi) juga memenuhi penolakan `F-FALB-03.k5` untuk tiga keadaan nama, sehingga langkah 28 menjadi bukti dua aturan sekaligus tanpa asersi ganda berurutan.
- Alasan spec melewati 35 langkah: semua blok satu kelas harness (fungsional) pada Modal Edit Label dari satu label seed dan satu Labels List; kegagalan validasi satu blok tidak menghilangkan makna blok lain, dan pemecahan menambah login, seeding, dan baseline log per spec tanpa mengurangi langkah.
- Temuan PRD: §4.5 menyatakan Submit Disabled untuk nama hanya spasi dan sekaligus menyatakan `V-01` tampil "bila Submit tetap tercapai lewat tombol Enter"; PRD tidak menyatakan apakah Enter pada field dengan `[Save]` Disabled mengirim form. Langkah 24 dan 25 mengikuti kalimat §4.5 tanpa menafsirkan lebih lanjut.
