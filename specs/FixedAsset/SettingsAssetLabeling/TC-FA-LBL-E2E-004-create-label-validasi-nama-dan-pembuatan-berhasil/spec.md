---
id: TC-FA-LBL-E2E-004-create-label-validasi-nama-dan-pembuatan-berhasil
title: "Create Label: validasi nama duplikat dan trim, lalu pembuatan berhasil"
priority: Critical
caseType: Positive
status: draft
sourceRules:
  - FALB-LOGIC-01a
  - FALB-LOGIC-01b
  - FALB-LOGIC-01c
  - E-FALB-01
  - F-FALB-02.k1
  - FALB:must-not/mengizinkan-duplikasi-nama-label-case-insensitive-dalam
coverage:
  web: automated
---

# Create Label: validasi nama duplikat dan trim, lalu pembuatan berhasil

## Prerequisites

- Mode: FE+BE
- Akun: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Akun kedua: Read Only di group, departemen, dan divisi kedua `DU-47` (env `FA_G2RO_EMAIL`, `FA_G2RO_PASSWORD`; group, departemen, dan divisi `DU-46` berbeda dari milik `DU-01`), dipakai setelah ganti akun eksplisit (langkah 39). Hook `after` mengembalikan sesi ke `DU-01`.
- Data uji: `DU-13` (nama label yang dibuat langkah 33 sampai 36), `DU-14` (nama berspasi depan dan belakang, dibuat langkah 21 sampai 23), `DU-15` (nama duplikat berbeda huruf besar-kecil dari label pembanding), `DU-25` (baseline jumlah entri Changelog, System Log, dan Activity Log untuk client ini, dicatat pada langkah 1), `DU-46` (group, departemen, dan divisi kedua milik akun `DU-47`), `DU-47` (akun Read Only di group kedua).
- Kemampuan teknis: sesi API aktor `DU-01` dan fixture BE disediakan tim FE/BE (dinyatakan di `suite.md`). Kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log serta isi entri System Log dan Activity Log per label (audit trail permanen, tidak diturunkan dari seeding; disediakan tim FE/BE). Hook `before` menyiapkan label pembanding lewat sesi API; nama dasarnya adalah nama yang `DU-15` ketik dengan kapitalisasi dibalik, bersuffix `{runId}-004`. Baseline `DU-25` dicatat sesudah seeding hook selesai dan sebelum aksi pertama; suite serial (`parallel: false`).
- Cleanup: hook `after` menghapus label pembanding, label hasil `DU-14`, dan label hasil `DU-13` lewat sesi API; cleanup tidak berasumsi seeding atau pembuatan berhasil penuh.
- Spec ini membuat data (label `DU-13` dan `DU-14`) sehingga dipisah dari spec yang tidak membuat data.

## Test Steps

1. Catat baseline `DU-25`: jumlah entri Changelog, System Log, dan Activity Log untuk client ini lewat kemampuan baca BE
2. Klik `[+ Label]`

### E-FALB-01: Create dengan nama yang sudah terpakai

3. Ketik Label Name `DU-15`
4. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name

### F-FALB-02.k1: Nama duplikat ditolak

5. Verifikasi tombol `[Submit]` Disabled
6. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline `DU-25` sama dengan 0

### FALB:must-not/mengizinkan-duplikasi-nama-label-case-insensitive-dalam: Tidak ada duplikasi nama label

7. Klik `[✕]` pada header Modal Create Label
8. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
9. Klik `[Leave]`
10. Ketik Search nama label pembanding (nama dasar `DU-15`), tekan Enter
11. Verifikasi hasil Search memuat tepat satu baris, yaitu label pembanding
12. Klik `(←)` pada kotak Search

### FALB-LOGIC-01a: Nama unik, case-insensitive, setelah trim

13. Klik `[+ Label]`
14. Ketik Label Name `DU-15`
15. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name
16. Ganti isi Label Name dengan `DU-15` yang diapit satu spasi di depan dan belakang
17. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name
18. Klik `[✕]` pada header Modal Create Label
19. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
20. Klik `[Leave]`

### FALB-LOGIC-01c: Label Name disimpan ter-trim

21. Klik `[+ Label]`
22. Ketik Label Name `DU-14`
23. Klik `[Submit]`
24. Ketik Search nama `DU-14` tanpa spasi depan dan belakang, tekan Enter
25. Verifikasi baris label tampil dengan chip pada kolom Label bernama persis `DU-14` tanpa spasi depan dan belakang
26. Klik ikon Changelog pada toolbar tabel
27. Ketik Search nama `DU-14` tanpa spasi depan dan belakang di toolbar Modal Changelog, tekan Enter
28. Verifikasi entri Create dengan Label Name dan New Value bernama persis `DU-14` tanpa spasi depan dan belakang
29. Verifikasi lewat kemampuan baca BE entri Create untuk label `DU-14` di System Log memuat Label Name ter-trim persis
30. Verifikasi lewat kemampuan baca BE entri Create untuk label `DU-14` di Activity Log memuat Label Name ter-trim persis
31. Klik `[✕]` pada header Modal Changelog
32. Klik `(←)` pada kotak Search

### FALB-LOGIC-01b: Katalog flat tanpa hierarki dan berlaku lintas departemen, divisi, dan group

33. Klik `[+ Label]`
34. Verifikasi form Create memuat field Label Name dan Color, tanpa field parent atau hierarki
35. Ketik Label Name `DU-13`
36. Klik `[Submit]`
37. Ketik Search `DU-13`, tekan Enter
38. Verifikasi baris `DU-13` tampil di Labels List sebagai satu daftar flat
39. Ganti akun: logout, login dengan akun `DU-47`
40. Buka Settings > Asset Master > tab Labels
41. Ketik Search `DU-13`, tekan Enter
42. Verifikasi baris `DU-13` tampil di Labels List akun `DU-47` (group, departemen, dan divisi `DU-46` berbeda dari pembuat label)

## Notes

- Langkah penghubung (S-03): langkah 1, 2, 7 sampai 9, 12, 13, 18 sampai 21, 23, 26, 31 sampai 33, 36, 39, dan 40. Langkah 7 sampai 9 dan 18 sampai 20 menutup form dirty secara deterministik (S-08). Langkah 12 dan 32 mengosongkan Search sebelum blok berikutnya (S-09). Langkah 10, 24, 27, 37, dan 41 adalah Search untuk menemukan baris atau entri target (R-16). Langkah 39 adalah ganti akun eksplisit tanpa `Verifikasi` (S-07).
- Anchor positif (bagian 8b butir 2): hasil Search di langkah 11 berisi baris pembanding yang tampil sebelum asersi bahwa tidak ada label ber-nama `DU-15` yang lain.
- Tunggu aksi selesai (bagian 8b butir 8): sesudah `[Submit]` di langkah 23 dan 36, langkah Search berikutnya baru dijalankan setelah modal tertutup dan tabel menyegarkan diri; hasil `[Submit]` langkah 36 diasersi pada langkah 38 sebelum ganti akun.
- Alasan spec melewati 35 langkah: satu kelas harness (fungsional), satu form Create dan satu Labels List; tiap blok berdiri sendiri dan tidak memakai data yang dibuat blok lain (blok `FALB-LOGIC-01a` memakai label pembanding seed hook `before`, blok `FALB-LOGIC-01c` dan `FALB-LOGIC-01b` memakai label yang dibuatnya sendiri). Blok ganti akun `DU-47` (langkah 39 sampai 42) menambah satu konteks login tetapi tetap dalam kelas dan halaman yang sama, dan bagian sesudah ganti akun tetap bermakna karena label `DU-13` dibuat dan diasersi oleh blok `FALB-LOGIC-01b` sendiri (langkah 33 sampai 38). Memecah spec hanya menambah login, hook, dan seeding tanpa mengurangi langkah.
- Pembagian klausa lintas spec: `FALB-LOGIC-01a` dan `FALB-LOGIC-01c` diasersi di sini pada form Create; klausa form Edit `FALB-LOGIC-01a` ada di spec 008 (`FALB-LOGIC-01a` dikutip spec 004 dan spec 008), dan klausa form Edit `FALB-LOGIC-01c` ada di spec 023. `F-FALB-02.k1` diasersi di sini untuk nama duplikat di jalur form, termasuk klausa nol entri log (langkah 6); klausa log untuk balapan dua admin (`E-FALB-19`) ada di spec 013. Klausa `E-FALB-18` dan `F-FALB-02.k4` (nama kosong, hanya spasi, dan lebih dari 120 karakter) ada di spec 021; klausa log `F-FALB-02.k4` ada di spec 021.
- Langkah 14 mengetik `DU-15` seperti langkah 3 karena kedua blok memakai label pembanding seed yang sama; langkah 14 menguji klausa unik case-insensitive `FALB-LOGIC-01a`, langkah 3 klausa `E-FALB-01`.
- Langkah 16 mengetik `DU-15` diapit satu spasi di depan dan belakang untuk klausa "setelah trim" `FALB-LOGIC-01a`; nilai yang diketik tetap `DU-15`.
- Temuan PRD: PRD §8.2 dan §8.3 menyebut System Log dan Activity Log tanpa jalur baca per label, sehingga entri keduanya dibaca lewat kemampuan baca BE (langkah 6, 29, dan 30; pola spec 009).
- Temuan PRD: `FALB-LOGIC-01c` menyebut nilai ter-trim dipakai di ekspor, tetapi PRD tidak menyatakan isi berkas ekspor per sel untuk Label Name; isi berkas (kelas f) tidak diasersi.
- Isi dialog `Unsaved Changes` mengikuti konvensi platform, bukan PRD modul; spec hanya mengasersi judul dan tombolnya.
