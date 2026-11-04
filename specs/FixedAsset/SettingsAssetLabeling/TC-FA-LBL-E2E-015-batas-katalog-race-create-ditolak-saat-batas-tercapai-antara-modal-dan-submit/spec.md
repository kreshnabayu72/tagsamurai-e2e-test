---
id: TC-FA-LBL-E2E-015-batas-katalog-race-create-ditolak-saat-batas-tercapai-antara-modal-dan-submit
title: "Batas katalog: Create ditolak saat katalog mencapai batas antara pembukaan modal dan Submit"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - E-FALB-25
  - F-FALB-02.k3
  - F-FALB-10.k2
  - FALB-LOGIC-08a
coverage:
  web: automated
---

# Batas katalog: Create ditolak saat katalog mencapai batas antara pembukaan modal dan Submit

## Prerequisites

- Mode: FE+BE
- Akun Total Control client uji batas katalog `DU-36` (env `FA_LIM_TC_EMAIL`, `FA_LIM_TC_PASSWORD`): katalog Label kosong di awal run dan katalog Asset Name belum mencapai ceiling.
- Login `DU-36` di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec ini mengembalikan sesi ke akun default suite.
- Data uji: `DU-37` (katalog Label client `DU-36` diisi sampai Master Data Count Limit; nilai batas dari System Limits, disediakan tim FE/BE). Hook `before` mengisi katalog client `DU-36` sampai batas minus 1 lewat fixture BE; label ke-batas dibuat pelaku kedua pada langkah 4 sehingga total katalog sama dengan batas. Label Name uji Create memakai nilai turunan `DU-37`: akhiran `-baru`.
- Kemampuan teknis: sesi API aktor `DU-36` (login API password; token tidak dihitung sebagai sesi web), fixture BE untuk mengisi dan membaca katalog Label, serta kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log (semuanya disediakan tim FE/BE).
- State global: katalog Label client `DU-36` diisi sampai batas; katalog Asset Name client `DU-36` tidak diubah; hook `after` menghapus label seed `DU-37` lewat fixture BE dan memulihkan katalog ke keadaan awal.

## Test Steps

### FALB-LOGIC-08a: Total katalog Label tidak boleh dilampaui Create, nilai batas dari Master Data Count Limit

1. Klik `[+ Label]` saat katalog satu label di bawah batas dan Search serta Filter tidak aktif.
2. Verifikasi modal Create Label tampil.
3. Ketik Label Name `DU-37` berakhiran `-baru`.
4. Pelaku kedua (sesi API `DU-36`) membuat satu label hingga total katalog sama dengan batas `DU-37` tersimpan.
5. Tunggu aksi selesai.
6. Catat baseline jumlah entri Changelog, System Log, dan Activity Log lewat kemampuan baca BE.
7. Klik `[Submit]`.
8. Verifikasi dialog dengan judul `Label Limit Reached`, isi `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` dengan `[Limit]` sama dengan nilai batas `DU-37`, dan tombol `[OK]` tampil.
9. Verifikasi lewat fixture BE total katalog Label client sama dengan batas `DU-37` (tidak melampaui batas).

### E-FALB-25: Create saat total katalog mencapai batas

10. Verifikasi modal Create Label tetap terbuka dan field Label Name masih berisi `DU-37` berakhiran `-baru`.
11. Klik `[OK]`.
12. Klik `[✕]` pada header modal Create Label.
13. Verifikasi dialog `Unsaved Changes` tampil.
14. Klik `[Leave]`.

### F-FALB-02.k3: Create ditolak saat batas katalog tercapai

15. Verifikasi lewat fixture BE tidak ada label bernama `DU-37` berakhiran `-baru`.

### F-FALB-10.k2: Penolakan Create karena batas katalog menulis nol entri log

16. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog sama dengan 0, selisih jumlah entri System Log sama dengan 0, dan selisih jumlah entri Activity Log sama dengan 0 terhadap baseline langkah 6.

## Notes

- Pengecualian P-1 (state berat): klausa absence log milik `F-FALB-10.k2` (langkah 16) diasersi di spec ini karena konteksnya bergantung pada katalog yang baru diisi sampai batas pada langkah 4. Baseline log dicatat sesudah label ke-batas dibuat (langkah 6), supaya entri Create pelaku kedua tidak terhitung. `F-FALB-10.k2` juga dikutip spec 014 dan 025 (state tenant), 017 (guard Default Label dan guard saat konfirmasi), 018 (label dipakai 500 aset), dan 027 (batas katalog sudah tercapai sejak awal).
- Pembagian klausa lintas spec: spec ini mengasersi kasus balapan, yaitu batas tercapai antara klik `[+ Label]` dan `[Submit]` (jalur Submit); spec 027 mengasersi kasus batas yang sudah tercapai sejak awal pada jalur form `[+ Label]`, tombol `[➕]`, API langsung, dan client tier Enterprise. `E-FALB-25`, `F-FALB-02.k3`, dan `F-FALB-10.k2` dikutip spec ini dan spec 027, masing-masing atas jalurnya sendiri.
- Anchor positif (S-03): langkah 2 membuktikan Create masih diizinkan saat katalog di bawah batas, sehingga penolakan langkah 8 berasal dari batas yang baru tercapai antara klik `[+ Label]` dan `[Submit]`; langkah 8 menjadi anchor untuk `Verifikasi` modal tetap terbuka pada langkah 10.
- Langkah penghubung (S-03): langkah 5, 11 sampai 14 (menutup dialog dan modal dirty menurut S-08).
- Klausa nol entri log `F-FALB-02.k3` (Aksi/Log: nol entri log) dipenuhi pada langkah 16: selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline langkah 6 sama dengan 0, di bawah `F-FALB-10.k2`.
