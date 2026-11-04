---
id: TC-FA-LBL-E2E-023-edit-label-nama-ter-trim-dan-kapitalisasi-nama-tersimpan-dan-tercatat
title: "Edit Label: perubahan kapitalisasi nama tersimpan dan tercatat, serta nama disimpan ter-trim"
priority: Critical
caseType: Positive
status: draft
sourceRules:
  - F-FALB-03.k1
  - E-FALB-07
  - FALB-LOGIC-07a
  - FALB-LOGIC-01c
coverage:
  web: automated
---

# Edit Label: perubahan kapitalisasi nama tersimpan dan tercatat, serta nama disimpan ter-trim

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: label seed milik spec dengan nama awal `DU-49` (`Urgent-{runId}-023`; sufiks `{runId}-023` dipakai bersama `DU-22` sebagai kata kunci Search Changelog pada langkah 2 dan 13); `DU-22` (nama baru hasil ubah kapitalisasi `URGENT-{runId}-023`, diketik pada langkah 7 dan menjadi Old Value pada langkah 25); `DU-14` (nama baru dengan spasi di depan dan belakang, `Trim-{runId}-023`). Label seed dibuat lewat API di hook `before` dan dihapus di hook `after`.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, disediakan tim FE/BE. Modal Changelog: Labels dibaca lewat UI; jumlah baris hasil Search dicatat sebagai baseline sebelum aksi pemicu (audit trail permanen, tidak diturunkan dari seeding). Kemampuan baca BE untuk isi entri System Log dan Activity Log per label (audit trail permanen; disediakan tim FE/BE).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### F-FALB-03.k1: Batas zero-delta: perubahan kapitalisasi nama saja

1. Klik icon `Changelog` pada Table Tools
2. Ketik Search sufiks `{runId}-023` pada Modal Changelog: Labels, tekan Enter
3. Catat jumlah baris hasil Search sebagai baseline N
4. Klik `[✕]` pada Modal Changelog: Labels
5. Ketik Search `DU-49` pada Labels List, tekan Enter
6. Klik `[⋯]` pada baris label seed, pilih `Edit`
7. Ganti isi field Label Name dengan `DU-22`
8. Klik `[Save]`
9. Verifikasi toast `Success, label has been updated.` tampil
10. Verifikasi toast `No changes to save.` tidak tampil

### E-FALB-07: Edit tersimpan dan tercatat di Changelog bila hanya kapitalisasi nama yang berubah

11. Verifikasi baris label tampil dengan nama `DU-22` pada Labels List
12. Klik icon `Changelog` pada Table Tools
13. Ketik Search sufiks `{runId}-023` pada Modal Changelog: Labels, tekan Enter
14. Verifikasi jumlah baris hasil Search sama dengan baseline N ditambah satu
15. Verifikasi baris teratas hasil Search: Action `Edit`, Field `Label Name`, Old Value nama awal label seed, New Value `DU-22`

### FALB-LOGIC-07a: Perubahan kapitalisasi nama saja bukan zero-delta dan menulis entri

16. Verifikasi entri Changelog untuk label bertambah satu dari baseline N, bukan nol
17. Klik `[✕]` pada Modal Changelog: Labels

### FALB-LOGIC-01c: Label Name disimpan dalam bentuk ter-trim

18. Klik `[⋯]` pada baris label bernama `DU-22`, pilih `Edit`
19. Ganti isi field Label Name dengan `DU-14`
20. Klik `[Save]`
21. Ganti isi kotak search dengan nama `DU-14` tanpa spasi tepi, tekan Enter
22. Verifikasi chip label pada Labels List bernama `DU-14` tanpa spasi di depan dan belakang
23. Klik icon `Changelog` pada Table Tools
24. Ketik Search `DU-14` tanpa spasi tepi pada Modal Changelog: Labels, tekan Enter
25. Verifikasi satu baris hasil Search: Action `Edit`, Field `Label Name`, Old Value `DU-22`, New Value `DU-14` tanpa spasi di depan dan belakang
26. Verifikasi lewat kemampuan baca BE entri Edit untuk label di System Log memuat New Value ter-trim persis `DU-14` tanpa spasi tepi
27. Verifikasi lewat kemampuan baca BE entri Edit untuk label di Activity Log memuat New Value ter-trim persis `DU-14` tanpa spasi tepi
28. Klik `[✕]` pada Modal Changelog: Labels

## Notes

- Langkah penghubung: Search (langkah 2, 5, 13, 21, 24) menemukan baris target atau entri Changelog; klik `[⋯]` membuka menu baris; langkah 3 mencatat baseline sebelum aksi pemicu; langkah 4, 17, dan 28 menutup Modal Changelog.
- Kata kunci Search Changelog pada langkah 2 dan 13 sama (sufiks `{runId}-023` yang dimiliki `DU-49` dan `DU-22`), sehingga baseline N dan jumlah baris sesudah Edit dihitung dari kumpulan baris yang sama tanpa bergantung pada Search yang tidak membedakan huruf besar dan kecil.
- Cara baca Changelog: selisih jumlah baris dibuktikan lebih dulu (langkah 14), lalu baris teratas pada urutan default Date terbaru dibaca (langkah 15); langkah 25 memakai nama bersuffix unik sehingga baseline nol.
- Anchor absence: toast `Success, label has been updated.` (langkah 9) mendahului asersi toast `No changes to save.` tidak tampil (langkah 10).
- Pembagian klausa lintas spec: `E-FALB-07` dan `F-FALB-03.k1` dikutip spec 009 dan spec ini; `FALB-LOGIC-07a` dikutip spec 009 dan spec ini. Spec 009 mengasersi sisi zero-delta (sukses tanpa mutasi, tanpa entri di tiga surface log, toast `No changes to save.`); spec ini mengasersi batasnya: perubahan kapitalisasi nama saja bukan zero-delta, Edit disimpan (toast `Success, label has been updated.`), dan Changelog bertambah satu. Klausa nol entri log `F-FALB-03.k1` dipegang spec 009. `FALB-LOGIC-01c` diasersi di sini untuk jalur form Edit (langkah 18 sampai 27); jalur form Create ada di spec 004. `F-FALB-10.k1` hanya dikutip spec 009.
- Temuan PRD: PRD §8.2 dan §8.3 menyebut System Log dan Activity Log tanpa jalur baca per label, sehingga isi entri keduanya dibaca lewat kemampuan baca BE (langkah 26 dan 27; pola spec 009).
- Temuan PRD: `FALB-LOGIC-01c` menyebut nilai ter-trim dipakai di ekspor, tetapi PRD tidak menyatakan isi berkas ekspor per sel untuk Label Name; isi berkas (kelas f) tidak diasersi.
