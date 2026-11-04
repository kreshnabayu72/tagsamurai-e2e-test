---
id: TC-FA-LBL-E2E-013-multi-konteks-race-dua-admin-create-dan-edit-label
title: "Multi-konteks: race dua admin pada Create dan Edit label"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - E-FALB-19
  - F-FALB-02.k1
  - E-FALB-15
  - F-FALB-03.k4
coverage:
  web: automated
---

# Multi-konteks: race dua admin pada Create dan Edit label

## Prerequisites

- Mode: FE+BE
- Konteks A: akun Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Konteks B (browser kedua, pelaku kedua): akun Total Control `DU-31` (env `FA_TC2_EMAIL`, `FA_TC2_PASSWORD`).
- Login konteks A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Konteks B login dan membuka Settings > Asset Master > tab Labels di hook `before` spec ini; konteks B ditutup di hook `after` spec ini.
- Data uji: `DU-32` (Label Name untuk dua pembuat serentak, dinamis, bersuffix `{runId}-013`, dipakai blok `E-FALB-19`); `DU-49` (label seed bersuffix `{runId}-013`, warna `#3B82F6`, dibuat lewat sesi API aktor A di hook `before` spec ini dan sudah ada saat langkah pertama; dipakai blok `E-FALB-15`). Nama hasil Edit memakai nilai turunan `DU-49`: akhiran `-A` untuk Edit konteks A dan akhiran `-B` untuk Edit konteks B. `DU-25` (baseline jumlah entri Changelog, System Log, dan Activity Log sebelum aksi pemicu, dicatat pada langkah 9).
- Kemampuan teknis: sesi API aktor A dan fixture BE untuk seeding label (`DU-49`), fixture BE untuk membaca label (nama dan jumlah label bernama sama), dan kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log serta isi entri Changelog per label (audit trail permanen, tidak diturunkan dari seeding), keduanya disediakan tim FE/BE.
- State global: spec membuat satu label (`DU-32`) lewat UI dan satu label seed (`DU-49`) lewat API di hook `before`; hook `after` menghapus kedua label lewat fixture BE.

## Test Steps

### E-FALB-19: Dua admin membuat label dengan nama sama hampir serentak

1. Di konteks A, klik `[+ Label]`.
2. Di konteks A, ketik Label Name `DU-32`.
3. Di konteks B, klik `[+ Label]`.
4. Di konteks B, ketik Label Name `DU-32`.
5. Tunggu 1 detik di kedua konteks hingga debounce pengecekan keunikan (500 ms) selesai.
6. Di konteks A, klik `[Submit]`.
7. Verifikasi di konteks A toast `Success, label has been created.` tampil.
8. Verifikasi lewat kemampuan baca BE entri Create untuk label `DU-32` tercatat tepat satu di Changelog.
9. Catat baseline `DU-25`: jumlah entri Changelog, System Log, dan Activity Log lewat kemampuan baca BE.
10. Di konteks B, klik `[Submit]`.
11. Verifikasi di konteks B inline error `Label name already exists` tampil di bawah field Label Name.
12. Di konteks A, ketik Search `DU-32`, tekan Enter.
13. Verifikasi tabel Labels List di konteks A memuat tepat satu baris Label `DU-32` (tidak ada record ganda).
14. Di konteks B, klik `[✕]` pada header modal Create Label.
15. Verifikasi di konteks B dialog `Unsaved Changes` tampil.
16. Di konteks B, klik `[Leave]`.

### F-FALB-02.k1: Create ditolak karena nama duplikat

17. Verifikasi lewat fixture BE jumlah label bernama `DU-32` sama dengan 1 (permintaan Create konteks B ditolak dan tidak tersimpan).
18. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline `DU-25` sama dengan 0.

### E-FALB-15: Dua admin menyimpan Edit pada label yang sama hampir bersamaan

19. Di konteks A, ganti isi kotak search dengan `DU-49`, tekan Enter.
20. Di konteks A, klik `[⋯]` pada baris Label `DU-49`, pilih `Edit`.
21. Di konteks B, muat ulang halaman (F5), lalu klik tab Labels.
22. Di konteks B, ketik Search `DU-49`, tekan Enter.
23. Di konteks B, klik `[⋯]` pada baris Label `DU-49`, pilih `Edit`.
24. Di konteks A, ganti isi Label Name dengan `DU-49` berakhiran `-A`.
25. Di konteks A, klik `[Save]`.
26. Verifikasi di konteks A toast `Success, label has been updated.` tampil.
27. Di konteks B, ganti isi Label Name dengan `DU-49` berakhiran `-A`.
28. Verifikasi di konteks B inline error `Label name already exists` tampil di bawah field Label Name.
29. Di konteks B, ganti isi Label Name dengan `DU-49` berakhiran `-B`.
30. Di konteks B, klik `[Save]`.
31. Verifikasi di konteks B toast `Success, label has been updated.` tampil.
32. Verifikasi di konteks B tidak ada dialog konflik yang tampil.
33. Verifikasi tabel Labels List di konteks B menampilkan baris Label `DU-49` berakhiran `-B` dan tidak menampilkan baris `DU-49` berakhiran `-A`.
34. Di konteks B, klik icon Changelog.
35. Di konteks B, ketik Search `DU-49` pada modal Changelog: Labels, tekan Enter.
36. Verifikasi modal Changelog: Labels memuat tepat dua baris Action `Edit` pada Field `Label Name`, satu baris untuk tiap Edit.
37. Di konteks B, klik `[✕]` pada modal Changelog: Labels.

### F-FALB-03.k4: Edit bersamaan pada label yang sama

38. Verifikasi lewat fixture BE nama label tersimpan `DU-49` berakhiran `-B` (Save yang terakhir diterima menimpa nilai tersimpan).

## Notes

- Pembagian klausa lintas spec: `F-FALB-02.k1` memuat dua kejadian dan satu klausa log. Klausa `E-FALB-19` (race dua admin) dan klausa log "nol entri log" untuk penolakan konteks B diasersi di spec ini (langkah 18); klausa `E-FALB-01` (nama duplikat tanpa race) dan klausa log jalur form diasersi di spec 004. Baseline log dicatat sesudah entri Create konteks A terbaca (langkah 8 dan 9) supaya entri Create A tidak terhitung.
- Urutan race ditetapkan deterministik: kedua konteks mengisi nama yang sama dan menunggu debounce, konteks A submit lebih dulu, lalu konteks B submit; konteks B menerima penolakan dari pengecekan atomik saat Submit. Dua Save pada Edit memakai urutan yang sama (A lebih dulu, B terakhir).
- Spec ini 38 langkah, di atas smell 35 langkah; satu kelas harness (c) (dua konteks browser, dua admin), dua blok yang berdiri sendiri: blok `E-FALB-19` membuat dan memakai label `DU-32` lewat UI, blok `E-FALB-15` memakai label seed `DU-49` dari hook `before` dan tidak bergantung pada data blok lain. Pemecahan menjadi dua spec tetap akan membangun ulang dua konteks browser (login konteks B, membuka tab Labels) di kedua spec; karena itu spec ini dipertahankan sebagai satu spec, dengan menyadari jumlah langkahnya melampaui 35.
- Anchor positif (S-03): langkah 7 dan 26 (toast sukses konteks A) membuktikan permintaan pertama sudah commit sebelum permintaan kedua dikirim; langkah 8 (entri Create tercatat tepat satu) menjadi anchor `Verifikasi` selisih log nol pada langkah 18; langkah 31 (toast sukses konteks B) menjadi anchor `Verifikasi` tidak adanya dialog konflik pada langkah 32.
- Langkah penghubung (S-03): langkah 5, 9 (baseline log), 12, 14 sampai 16 (menutup modal dirty konteks B menurut S-08), 19 (Search label seed `DU-49` di konteks A menurut R-16), 21 dan 22 (memuat ulang daftar konteks B dan mencari baris target menurut R-16), 34, 35, dan 37.
- Klausa di luar E2E: E-FALB-15 (tanpa penanda versi): tidak ada penanda versi pada record yang teramati lewat UI atau kemampuan baca BE yang dinyatakan di Prerequisites.
- Klausa `E-FALB-15` "keunikan nama tetap dicek" diasersi pada langkah 27 dan 28 memakai nama hasil Edit konteks A sebagai nama bentrok.
- Pembersihan: hook `after` menutup konteks B dan menghapus label bernama `DU-32` dan label seed `DU-49` (nama terakhir berakhiran `-B`) lewat fixture BE.
