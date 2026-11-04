---
id: TC-FA-LBL-E2E-021-create-label-validasi-nama-kosong-spasi-dan-panjang
title: "Create Label: validasi nama kosong, hanya spasi, dan lebih dari 120 karakter"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - E-FALB-18
  - F-FALB-02.k4
coverage:
  web: automated
---

# Create Label: validasi nama kosong, hanya spasi, dan lebih dari 120 karakter

## Prerequisites

- Mode: FE+BE
- Akun: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-16` (nama hanya berisi spasi), `DU-17` (nama 121 karakter setelah trim, bersuffix `{runId}-021`), `DU-25` (baseline jumlah entri Changelog, System Log, dan Activity Log untuk client ini, dicatat pada langkah 1).
- Kemampuan teknis: kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log (audit trail permanen, tidak diturunkan dari seeding; disediakan tim FE/BE). Baseline dicatat sebelum aksi pertama; suite serial (`parallel: false`).
- Spec ini tidak pernah menekan `[Submit]` yang berhasil dan menutup form tanpa menyimpan (langkah 16 sampai 18), sehingga tidak membuat data dan tidak butuh cleanup.

## Test Steps

1. Catat baseline `DU-25`: jumlah entri Changelog, System Log, dan Activity Log untuk client ini lewat kemampuan baca BE
2. Klik `[+ Label]`

### F-FALB-02.k4: Nama kosong, hanya spasi, atau lebih dari 120 karakter ditolak

3. Verifikasi tombol `[Submit]` Disabled saat Label Name kosong
4. Ketik Label Name `DU-16`
5. Verifikasi tombol `[Submit]` Disabled saat Label Name hanya berisi spasi
6. Ganti isi Label Name dengan `DU-17`
7. Verifikasi tombol `[Submit]` Disabled saat Label Name lebih dari 120 karakter
8. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline `DU-25` sama dengan 0

### E-FALB-18: Create dengan nama hanya berisi spasi atau 121 karakter setelah trim

9. Ganti isi Label Name dengan `DU-16`
10. Verifikasi tombol `[Submit]` Disabled karena nama yang hanya berisi spasi dianggap kosong
11. Tekan Enter pada field Label Name
12. Verifikasi inline error `Label name must not be empty` tampil di bawah field Label Name
13. Ganti isi Label Name dengan `DU-17`
14. Verifikasi inline error `Max. 120 characters` tampil langsung saat nama diketik
15. Verifikasi tombol `[Submit]` Disabled
16. Klik `[✕]` pada header Modal Create Label
17. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
18. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1, 2, 4, 6, 9, 11, 13, 16, dan 18. Langkah 1 mencatat baseline sebelum aksi pertama; langkah 16 sampai 18 menutup form dirty secara deterministik (S-08).
- Pembagian klausa lintas spec: `E-FALB-18` berlaku untuk Create dan Edit; klausa Create diasersi di sini, klausa Edit ada di spec 008 (`E-FALB-18` dikutip spec 021 dan spec 008). `F-FALB-02.k4` hanya dikutip di sini, termasuk klausa nol entri log (langkah 8); klausa nol entri log `F-FALB-03.k5` untuk Edit ada di spec 008.
- Pasangan langkah 5 dan 10 (nama hanya spasi) serta langkah 7 dan 15 (121 karakter) mengasersi keadaan yang sama untuk dua aturan berbeda, `F-FALB-02.k4` dan `E-FALB-18`; pengulangan itu disengaja karena tiap aturan menuntut `Verifikasi` di bawah subjudulnya sendiri.
- Pesan fallback `V-01` diasersi lewat tombol Enter (langkah 11 dan 12) mengikuti kalimat §4.5; label tidak pernah tersimpan karena `[Submit]` Disabled pada ketiga kondisi.
- Temuan PRD: §4.5 menyatakan Submit Disabled untuk nama hanya spasi dan sekaligus menyatakan `V-01` tampil "bila Submit tetap tercapai lewat tombol Enter" (`E-FALB-18` menyatakan hal yang sama); PRD tidak menyatakan apakah Enter pada field dengan `[Submit]` Disabled mengirim form. Langkah 11 dan 12 mengikuti kalimat §4.5 tanpa menafsirkan lebih lanjut.
- Isi dialog `Unsaved Changes` mengikuti konvensi platform, bukan PRD modul; spec hanya mengasersi judul dan tombolnya.
