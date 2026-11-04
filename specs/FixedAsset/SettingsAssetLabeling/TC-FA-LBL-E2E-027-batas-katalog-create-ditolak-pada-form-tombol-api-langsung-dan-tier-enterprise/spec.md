---
id: TC-FA-LBL-E2E-027-batas-katalog-create-ditolak-pada-form-tombol-api-langsung-dan-tier-enterprise
title: "Batas katalog: Create ditolak pada jalur form, tombol [➕], API langsung, dan tier Enterprise saat katalog sudah di batas"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - E-FALB-25
  - F-FALB-02.k3
  - F-FALB-10.k2
  - FALB-LOGIC-08b
  - FALB:must-not/membuat-label-baru-di-atas-batas-katalog-di-jalur-form-t
coverage:
  web: automated
---

# Batas katalog: Create ditolak pada jalur form, tombol [➕], API langsung, dan tier Enterprise saat katalog sudah di batas

## Prerequisites

- Mode: FE+BE
- Akun Total Control client uji batas katalog `DU-36` (env `FA_LIM_TC_EMAIL`, `FA_LIM_TC_PASSWORD`): katalog Label kosong di awal run dan katalog Asset Name belum mencapai ceiling; akun Total Control client tier Enterprise yang katalog Labelnya sudah di batas `DU-38` (env `FA_LIM_ENT_TC_EMAIL`, `FA_LIM_ENT_TC_PASSWORD`).
- Login `DU-36` di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun `DU-38` dipakai pada langkah ganti akun eksplisit (langkah 20 sampai 22). Hook `after` spec ini mengembalikan sesi ke akun default suite.
- Data uji: `DU-37` (katalog Label client `DU-36` diisi sampai tepat Master Data Count Limit; nilai batas dari System Limits, disediakan tim FE/BE). Hook `before` mengisi katalog client `DU-36` sampai tepat batas lewat fixture BE sebelum halaman dibuka, sehingga `totalRecords` List sudah sama dengan batas saat spec mulai. Client `DU-38` sudah berada di batas sebagai data pre-setup. Label Name uji Create memakai nilai turunan `DU-37`: akhiran `-baru`.
- Kemampuan teknis: sesi API aktor `DU-36` (login API password; token tidak dihitung sebagai sesi web) dan klien HTTP untuk request langsung, fixture BE untuk mengisi dan membaca katalog Label, serta kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log (semuanya disediakan tim FE/BE).
- State global: katalog Label client `DU-36` diisi sampai batas; katalog Asset Name client `DU-36` tidak diubah; hook `after` menghapus label seed `DU-37` lewat fixture BE dan memulihkan katalog ke keadaan awal. Client `DU-38` tidak diubah.

## Test Steps

### E-FALB-25: Create saat total katalog mencapai batas

1. Catat baseline jumlah entri Changelog, System Log, dan Activity Log lewat kemampuan baca BE.
2. Klik `[+ Label]` saat katalog sudah di batas dan Search serta Filter tidak aktif.
3. Verifikasi dialog dengan judul `Label Limit Reached`, isi `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` dengan `[Limit]` sama dengan nilai batas `DU-37`, dan tombol `[OK]` tampil.
4. Verifikasi modal Create Label tidak dibuka.
5. Klik `[OK]`.
6. Buka tab Asset Name pada Settings > Asset Master.
7. Klik `[+ Asset Name]`.
8. Verifikasi Modal Create Asset Name tampil.
9. Klik `[➕]` di samping caption Default Label.
10. Verifikasi dialog dengan judul `Label Limit Reached`, isi `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` dengan `[Limit]` sama dengan nilai batas `DU-37`, dan tombol `[OK]` tampil.
11. Verifikasi modal Create Label tidak dibuka.
12. Klik `[OK]`.
13. Klik `[✕]` pada header Modal Create Asset Name.
14. Kirim request Create label langsung lewat sesi API `DU-36` dengan Label Name `DU-37` berakhiran `-baru`, hingga respons diterima.
15. Verifikasi respons ditolak server (bukan sukses) dan memuat batas sama dengan nilai batas `DU-37`.
16. Verifikasi lewat fixture BE total katalog Label client tetap sama dengan batas `DU-37`.

### F-FALB-02.k3: Create ditolak saat batas katalog tercapai

17. Verifikasi lewat fixture BE tidak ada label bernama `DU-37` berakhiran `-baru`.

### FALB:must-not/membuat-label-baru-di-atas-batas-katalog-di-jalur-form-t: Tidak membuat label baru di atas batas katalog

18. Verifikasi lewat fixture BE total katalog Label client sama dengan batas `DU-37`, tidak di atas batas, sesudah jalur form `[+ Label]`, jalur tombol `[➕]` pada tab Asset Name, dan jalur API langsung.

### F-FALB-10.k2: Penolakan Create karena batas katalog menulis nol entri log

19. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog sama dengan 0, selisih jumlah entri System Log sama dengan 0, dan selisih jumlah entri Activity Log sama dengan 0 terhadap baseline langkah 1.

### FALB-LOGIC-08b: Batas sama di semua tier plan termasuk Enterprise

20. Ganti akun: logout dari `DU-36`.
21. Login sebagai `DU-38`.
22. Buka Settings > Asset Master > tab Labels.
23. Klik `[+ Label]`.
24. Verifikasi dialog dengan judul `Label Limit Reached`, isi `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` dengan `[Limit]` sama dengan nilai batas `DU-37` (batas yang sama dengan client tier biasa), dan tombol `[OK]` tampil.
25. Verifikasi modal Create Label tidak dibuka.
26. Klik `[OK]`.

## Notes

- Pengecualian P-1 (state berat): klausa absence log milik `F-FALB-10.k2` (langkah 19) diasersi di spec ini karena konteksnya bergantung pada katalog yang diisi sampai batas oleh hook `before`. Baseline log dicatat sebelum aksi pemicu (langkah 1). `F-FALB-10.k2` juga dikutip spec 014 dan 025 (state tenant), 015 (batas tercapai antara modal dan Submit), 017 (guard Default Label dan guard saat konfirmasi), dan 018 (label dipakai 500 aset).
- Pembagian klausa lintas spec: spec ini mengasersi batas yang sudah tercapai sejak awal; kasus balapan (batas tercapai antara klik `[+ Label]` dan `[Submit]`, jalur Submit, `FALB-LOGIC-08a`) ada di spec 015. `E-FALB-25`, `F-FALB-02.k3`, dan `F-FALB-10.k2` dikutip spec 015 dan spec ini, masing-masing atas jalurnya sendiri. Butir Must NOT batas katalog diasersi di sini untuk jalur form, tombol `[➕]`, dan API langsung; jalur Submit diasersi spec 015 pada langkah 9 (total katalog sama dengan batas).
- Pengecualian P-5 butir (b): langkah 14 sampai 16 adalah satu blok objek-uji ringan kelas a (request langsung tanpa harness eksternal dan tanpa state berat sendiri) yang berada di spec volume katalog. Sesuai bagian 8b butir 1, hanya respons server dan state data (fixture BE) yang diasersi; dialog tidak diasersi pada request langsung.
- Klausa `E-FALB-25` "berlaku di semua tier plan termasuk Enterprise" diasersi pada langkah 24 dan 25 di bawah `FALB-LOGIC-08b` karena membutuhkan ganti akun ke client Enterprise.
- Anchor positif (S-03): langkah 3 (dialog `Label Limit Reached` tampil) menjadi anchor untuk `Verifikasi` absence modal pada langkah 4, langkah 10 untuk langkah 11, dan langkah 24 untuk langkah 25; langkah 8 (Modal Create Asset Name tampil) menjadi anchor bahwa klik `[➕]` terjadi pada form yang sudah termuat.
- Langkah penghubung (S-03): langkah 1 (baseline sebelum aksi pemicu, S-12), 5, 6 (membuka tab Asset Name; pembukaan tab memuat List sehingga `totalRecords` disegarkan, PRD labeling `FALB-LOGIC-08c`), 7 (membuka Modal Create Asset Name), 12 dan 13 (menutup dialog dan Modal Create Asset Name yang masih pristine, sehingga tidak ada dialog `Unsaved Changes`), 20 sampai 22 (ganti akun eksplisit, S-07), dan 26.
- Alur dependensi dari PRD `settings-asset-name` (dikutip, dimiliki modul itu; langkah 6 sampai 13 bergantung pada PRD tersebut, bukan pada PRD ini). Kutipan memakai nomor baris file PRD inti `settings-asset-name`:
  - L226: "`G-CREATE` | Form (UI Asset Name) | ✅ | ❌ | Create | ❌ | `[+ Asset Name]` (§4.1 Asset Name List — Row Actions); `[➕]` Default Label (§4.1 Popup Create / Edit)"; Total Control ✅ (langkah 7 dan 9);
  - L407: "`[+ Asset Name]` | `G-CREATE`; Hidden bagi lainnya | Buka Modal Create (§4.1 Popup Create / Edit); bila ceiling katalog Asset Name sudah tercapai, dialog blok `D-07` tampil sebagai gantinya" (langkah 7; alasan syarat data `DU-36`);
  - L418: "Di sebelah caption label ada tombol icon `[➕]` (tooltip 🔖 `"Create label"`)" (langkah 9);
  - L439 `FI-08`: "Klik `[➕]` | Membuka Modal Create Label milik `settings-asset-labeling/` ...; Bila batas katalog Label sudah tercapai, dialog blok `D-06` milik `settings-asset-labeling/` (§4.4 di sana) tampil dan modal tidak dibuka (`FALB-LOGIC-08`)" (langkah 9 sampai 11);
  - L440 `FI-09`: "Tombol `[➕]` hanya tampil bagi `G-CREATE`" (langkah 9);
  - L787: dialog Unsaved Changes hanya untuk form kotor (langkah 13).
  - Kutipan ini dependensi: isi dialog `D-06` pada langkah 10 diasersi sebagai klausa `E-FALB-25` milik PRD labeling; PRD labeling menyebut tombol `[➕]` pada `FALB-LOGIC-08a`, `E-FALB-25`, dan butir Must NOT batas katalog.
- Temuan PRD: PRD labeling menyatakan nilai `totalRecords` disegarkan saat "List dimuat ulang" (`FALB-LOGIC-08c`) tetapi tidak menyatakan List mana yang menjadi sumber untuk klik `[➕]` pada tab Asset Name; langkah 6 membuka tab Asset Name (pembukaan tab memuat List), dan klausanya hanya teramati lewat dialog langkah 10.
- Temuan PRD: jalur Import `[Create Missing Labels]` (disebut `FALB-LOGIC-08a` dan butir Must NOT batas katalog) milik `import/` dan tidak dinyatakan di PRD ini, sehingga jalur itu tidak diasersi.
- Temuan PRD: `E-FALB-25` menyatakan `D-06` tampil dan modal tetap terbuka juga untuk "API" langsung, padahal request langsung tidak melewati browser; PRD tidak menyatakan tampilan apa yang dimaksud. Klausa tampilan itu tidak diasersi untuk jalur API; hanya respons server dan state data yang diasersi (langkah 15 dan 16, bagian 8b butir 1).
- Klausa nol entri log `F-FALB-02.k3` (Aksi/Log: nol entri log) dipenuhi pada langkah 19: selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline langkah 1 sama dengan 0, di bawah `F-FALB-10.k2`.
