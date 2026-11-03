---
id: TC-FA-CF-E2E-158-multi-konteks-race-dua-sesi-pada-kuota
title: "Multi-Konteks: Race Dua Sesi pada Kuota Plafon dan Cap per Asset Name"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-198
  - TC-FA-CF-199
  - TC-FA-CF-604
coverage:
  web: automated
---

# Multi-Konteks: Race Dua Sesi pada Kuota Plafon dan Cap per Asset Name

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor sesi 1: Total Control Company Plafon (Pre-setup #17). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PLAFON_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Akun sesi UI kedua (Pre-setup #28: dua sesi Total Control aktif sekaligus), dibuka sebagai konteks browser kedua pada langkah 1, 12, dan 28 (konteks UI kedua yang menjadi objek asersi, kelas c). Email akun sesi 2 Company Plafon dan Company Cap tidak tertulis di Pre-setup TC (Pre-setup #10 hanya untuk Company Alpha); disediakan tim FE.

| Konteks | Company | Pre-setup | Env password |
|---|---|---|---|
| Sesi 1 TC-FA-CF-198 dan 199 | Company Plafon | #17 | `Spectra.env.FA_TC_PLAFON_PASSWORD` |
| Sesi 2 TC-FA-CF-198 dan 199 | Company Plafon | #17, #28 | `Spectra.env.FA_TC2_PLAFON_PASSWORD` |
| Sesi 1 TC-FA-CF-604 | Company Cap | #16 | `Spectra.env.FA_TC_CAP_PASSWORD` |
| Sesi 2 TC-FA-CF-604 | Company Cap | #16, #28 | `Spectra.env.FA_TC2_CAP_PASSWORD` |

  Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Plafon varian 999 field (limit 1000; TC-FA-CF-198) dan varian 998 field (TC-FA-CF-199) (Pre-setup #17, seed fixture; kemampuan disediakan tim FE/BE). Company Cap (cap 2 per Asset Name; Pre-setup #16): `Generator` memiliki 1 field Active, `Cap Gen Inactive` Inactive ber-Scope {Generator}. Nilai data mengacu `Fixture.faCustomFields.cap` dan `Fixture.faCustomFields.plafon` (fixture belum ada, disediakan tim FE).
- Data Dinamis: Field Name `Race A {runId}-158`, `Race B {runId}-158`, `Late Block {runId}-158`, `Late Last {runId}-158`, dan `Cap Race {runId}-158`. Cleanup di hook `after`: hapus lewat API semua field Company Plafon dan Company Cap yang namanya memuat `{runId}-158`.
- Kemampuan teknis: dua konteks browser dengan sesi web berbeda; aksi serentak pada dua sesi (klik `[Submit]` bersamaan); fixture BE untuk membaca total field dan jumlah field Active per Asset Name; seed reset Company Plafon varian (disediakan tim FE/BE). Kuota Master Data Count Limit dan cap hanya menjadi pemicu state, bukan objek uji (`P-2`, keputusan 2026-10-21).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk setiap akun sesi dan hook `after` memulihkannya (lihat `suite.md`).
- State global: dataset Company Plafon dan Company Cap diubah spec ini; hook `before` dan `after` memulihkannya lewat seed reset. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-198: dua Create bersamaan pada sisa kuota terakhir

1. Buka konteks browser sesi 2: login sebagai Total Control sesi 2 Company Plafon dan buka Settings > Custom Fields
2. Sesi 1 dan sesi 2 klik `[+ Custom Field]` dan mengisi modal Create: sesi 1 Field Name `Race A {runId}-158`, sesi 2 Field Name `Race B {runId}-158`, Data Type `Text`
3. Kedua sesi klik `[Submit]` bersamaan
4. Verifikasi tepat satu Create berhasil dengan toast `Success, custom field has been created.`
5. Verifikasi sesi lain menerima dialog `Limit Reached` dengan teks `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.`
6. Verifikasi modal Create sesi lain tetap terbuka dengan input dipertahankan
7. Verifikasi total field tersimpan 1000 dan tidak melebihi plafon (dibaca lewat fixture BE)
8. Klik `[OK]` pada dialog `Limit Reached` di sesi yang menerimanya
9. Tutup kedua konteks browser tanpa menyimpan

### TC-FA-CF-199: plafon penuh di antara klik tombol dan Submit

10. Pulihkan Company Plafon ke varian 998 field lewat seed reset
11. Buka konteks browser sesi 1: login sebagai Total Control Company Plafon dan buka Settings > Custom Fields
12. Buka konteks browser sesi 2: login sebagai Total Control sesi 2 Company Plafon dan buka Settings > Custom Fields
13. Sesi 1 klik `[+ Custom Field]`
14. Sesi 1 isi Field Name `Late Block {runId}-158` dan Data Type `Text`
15. Sesi 2 membuat field `Late Last {runId}-158` (Data Type `Text`) lewat UI hingga tersimpan sehingga total mencapai 1000
16. Sesi 1 klik `[Submit]`
17. Verifikasi dialog `Limit Reached` plafon tampil di atas modal Create
18. Klik `[OK]` pada dialog
19. Verifikasi modal Create tetap terbuka dengan input dipertahankan
20. Verifikasi tabel sesi 1 memuat sedikitnya satu baris field
21. Verifikasi tabel sesi 1 tidak memuat baris `Late Block {runId}-158` (baris `Late Last {runId}-158` dari sesi 2 boleh muncul bila tabel tersegarkan otomatis, tidak diasersi)
22. Verifikasi field `Late Block {runId}-158` tidak tersimpan (dibaca lewat fixture BE)
23. Klik icon close `[✕]` pada modal Create sesi 1
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik `[Leave]`

### TC-FA-CF-604: Create dan Activate bersamaan pada sisa kuota terakhir sebuah Asset Name

26. Tutup kedua konteks browser
27. Buka konteks browser sesi 1: login sebagai Total Control Company Cap dan buka Settings > Custom Fields
28. Buka konteks browser sesi 2: login sebagai Total Control sesi 2 Company Cap dan buka Settings > Custom Fields
29. Sesi 1 klik `[+ Custom Field]`, isi Field Name `Cap Race {runId}-158`, Data Type `Text`, dan Scope `Specific Asset Name` dengan `Generator`
30. Sesi 1 klik `[Submit]` dan sesi 2 mengaktifkan `Cap Gen Inactive` (Scope `Generator`) bersamaan
31. Verifikasi tepat satu aksi berhasil sehingga `Generator` memiliki 2 field Active
32. Verifikasi aksi lain ditolak dengan dialog `Limit Reached`
33. Verifikasi jumlah field Active `Generator` tidak melebihi 2 (dibaca lewat fixture BE)
34. Klik `[OK]` pada dialog `Limit Reached` di sesi yang menerimanya
35. Tutup kedua konteks browser tanpa menyimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec kelas c (multi-konteks): hasil di kedua sesi UI diasersi, sehingga sesi kedua adalah sesi UI, bukan sesi API. Kuota pada TC-FA-CF-198, 199, dan 604 hanya pemicu state (`P-2`, keputusan 2026-10-21); spec tidak dipindah ke kelas e.
- Sesi yang menang pada race tidak ditentukan; `Verifikasi` langkah 4, 5, 6, 31, dan 32 ditulis "tepat satu" dan "sesi lain" supaya tidak bergantung pada siapa yang menang. Langkah 8, 34, 9, dan 35 menutup dialog dan konteks tanpa langkah bersyarat; penutupan konteks membuang modal yang masih dirty (S-08 tidak berlaku pada konteks yang dibuang).
- Teks dialog plafon pada TC-FA-CF-198 dan 199 ditulis "teks plafon" tanpa kalimat; spec memakai teks `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.` dari TC lain pada modul yang sama (Create di plafon).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8, 9, 10, 11, 12, 18, 26, 27, 28, 34, dan 35 (menutup dialog, mengganti varian dataset, membuka dan menutup konteks). Langkah 23 sampai 25 menutup form dirty (S-08).
- Langkah 20 adalah pembanding generik (anchor positif, 8b butir 2) untuk absence baris pada langkah 21 (TC-FA-CF-199 butir b): `Verifikasi` langkah 21 hanya mengasersi `Late Block {runId}-158` tidak tampil di tabel sesi 1 dan tidak mengasersi baris `Late Last {runId}-158`, karena TC menyatakan baris sesi lain boleh muncul bila tabel tersegarkan otomatis.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Plafon dan Company Cap, maupun akun sesi 2 pada kedua Company itu (Pre-setup #10 dan #28 hanya Company Alpha); akun disediakan tim FE.
  - TC-FA-CF-199 menyebut "Dari sesi lain buat field terakhir" tanpa nama field; spec memakai `Late Last {runId}-158`.
  - TC-FA-CF-198 dan 604 tidak menyebut sesi mana yang menang; spec mengasersi "tepat satu" tanpa menentukan sesi.
  - TC-FA-CF-199 butir b ("tabel sesi 1 tidak memuat baris `Late Block`, baris yang dibuat sesi lain boleh muncul bila tabel tersegarkan otomatis") ambigu terhadap TC-FA-CF-606 (tabel sesi lain menyegarkan diri diam-diam dan menambahkan baris sesi lain): tidak jelas apakah baris `Late Last {runId}-158` harus tampil atau tidak. Spec hanya mengasersi absence `Late Block` (langkah 21) dan tidak mengasersi `Late Last`; pembanding yang didefinisikan perlu dari TC.
