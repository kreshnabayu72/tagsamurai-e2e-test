---
id: TC-AC-ACAL-E2E-018-perubahan-hubungan-entitas-reassign-partner-dan-pindah-staf
title: "Perubahan Hubungan Entitas: Reassign Partner dan Pindah Staf"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACAL-149
  - TC-AC-ACAL-162
  - TC-AC-ACAL-169
coverage:
  web: automated
---

# Perubahan Hubungan Entitas: Reassign Partner dan Pindah Staf

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); spec ini mengubah hubungan entitas global (Reassign Partner Beta, pindah `Tono`) dan direkomendasikan dijalankan paling akhir (urutan jalan rekomendasi di suite.md; runner belum terbukti mengikuti nomor folder, sehingga spec tetap mandiri dan tidak bergantung pada urutan); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen halaman Activity Log untuk akun Total Control Distributor Alfa dan Distributor Gamma (kemampuan disediakan tim FE/BE; lihat suite.md).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)):

| Akun | Email (Pre-setup TC) | Env var password |
|---|---|---|
| Total Control (Distributor Alfa) | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |
| Total Control (Distributor Gamma) | `totalControlAdminConsoleDistributorGamma_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_GAMMA_TC_PASSWORD` |
| Total Control (Principal), hanya sesi API pemicu | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 1) | `Spectra.env.AC_TC_PASSWORD` |

- Login akun pertama (Total Control Distributor Alfa) di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (Pre-setup No 8, 12; nama literal, pengecualian S-12 A-3 karena asersi bergantung pada nama dan singkatan; seeding idempotent, dan kedua staf tidak dihapus): Partner Beta di jaringan Distributor Alfa, staf `Tono` (Partner Beta, punya sesi lama `Session started` dan `Session ended`), staf `Hendra Pratama` (Partner Beta, punya sesi AC), serta entri User Action lama `Partner Beta` (Pre-setup No 10). Kredensial sesi API `Tono` dan `Hendra Pratama` disediakan tim FE/BE (TC tidak menyebut akun staf).
- State global yang diubah dan dipulihkan: (1) staf `Tono` berpindah entitas, yaitu Partner Beta menjadi Distributor Gamma, dikembalikan di langkah 16; (2) Partner Beta di-Reassign dari Distributor Alfa ke Distributor Gamma, dikembalikan di langkah 36. Butir S-06: pemulihan ada di hook `before` (lebih dulu mengembalikan `Tono` ke Partner Beta dan Partner Beta ke Distributor Alfa lewat sesi API Principal bila sisa run sebelumnya masih berubah) dan di hook `after` (memulihkan keduanya bila masih berubah, walau spec gagal di tengah). Efek: entri User Action Reassign dan entri Session `Tono` bertambah di audit trail; Last Updated Partner Beta dan `Tono` berubah pada tiap pemindahan dan pengembalian, tidak diasersi spec ini, dan tidak dapat dipulihkan.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor Principal (Reassign Partner, pindah staf), sesi API staf `Tono` (login, membuka, dan menutup Admin Console); pembacaan jumlah baris Tab Session dengan kueri Search `Tono` (jenis kueri sama dengan Search UI pada langkah 6 dan 12) lewat sesi API aktor Total Control Distributor Alfa dan Distributor Gamma sebagai baseline (S-12: jumlah dibaca sebelum aksi pemicu, tanpa sesi UI tambahan).

## Test Steps

### TC-AC-ACAL-162: Sesi staf yang pindah entitas tetap ter-scope ke entitas pemilik saat event

1. Baca lewat sesi API aktor Total Control (Distributor Alfa) jumlah baris Tab Session dengan kueri Search `Tono` sebagai baseline A0
2. Baca lewat sesi API aktor Total Control (Distributor Gamma) jumlah baris Tab Session dengan kueri Search `Tono` sebagai baseline G0
3. Pemicu API: Principal memindahkan `Tono` dari Partner Beta ke Distributor Gamma hingga tersimpan
4. Pemicu API: `Tono` login, membuka Admin Console, lalu menutupnya hingga baris `Session started` dan `Session ended` baru tersimpan
5. Tunggu aksi selesai: sesi API `Tono` selesai
6. Ketik Search `Tono`, tekan Enter (Distributor Alfa)
7. Verifikasi sedikitnya satu baris sesi lama `Tono` (saat di Partner Beta) tampil
8. Verifikasi jumlah total hasil pada footer `Showing X–Y of Z entries` sama dengan A0, sehingga sesi baru setelah pindah tidak tampil
9. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
10. Ganti akun: logout, lalu login sebagai Total Control (Distributor Gamma) dengan `Spectra.env.AC_GAMMA_TC_PASSWORD`
11. Klik menu Activity Log di sidebar Admin Console
12. Ketik Search `Tono`, tekan Enter (Distributor Gamma)
13. Verifikasi dua baris teratas adalah `Session ended` dan `Session started` milik `Tono` dari sesi baru setelah pindah
14. Verifikasi jumlah total hasil pada footer `Showing X–Y of Z entries` sama dengan G0 ditambah 2, sehingga sesi lama (saat di Partner Beta) tidak tampil
15. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
16. Pemicu API: Principal mengembalikan `Tono` ke Partner Beta hingga tersimpan

### TC-AC-ACAL-149 dan TC-AC-ACAL-169: Reassign Partner mengubah scope log lama dan sesi staf sesuai jaringan saat query

17. Pemicu API: Principal me-Reassign Partner Beta dari Distributor Alfa ke Distributor Gamma hingga tersimpan
18. Tunggu aksi selesai: Reassign Partner Beta selesai
19. Klik tab "User Action" (Distributor Gamma)
20. Ketik Search `Partner Beta`, tekan Enter
21. Verifikasi baris log lama Object `Partner` Name `Partner Beta` tampil untuk Distributor Gamma (TC-AC-ACAL-149)
22. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
23. Klik tab "Session"
24. Ketik Search `Hendra Pratama`, tekan Enter
25. Verifikasi sesi lama `Hendra P` tampil untuk Distributor Gamma (TC-AC-ACAL-169)
26. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
27. Ganti akun: logout, lalu login sebagai Total Control (Distributor Alfa) dengan `Spectra.env.AC_ALFA_TC_PASSWORD`
28. Klik menu Activity Log di sidebar Admin Console, lalu klik tab "User Action"
29. Ketik Search `Partner Beta`, tekan Enter
30. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, sehingga log lama Partner Beta tidak tampil untuk Distributor Alfa (TC-AC-ACAL-149)
31. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
32. Klik tab "Session"
33. Ketik Search `Hendra Pratama`, tekan Enter
34. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, sehingga sesi lama `Hendra P` tidak tampil untuk Distributor Alfa (TC-AC-ACAL-169)
35. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
36. Pemicu API: Principal mengembalikan Partner Beta ke Distributor Alfa hingga tersimpan

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-149, 162, 169).
- Urutan TC di spec berbeda dari urutan sumber: TC-AC-ACAL-162 ditaruh pertama karena membutuhkan Partner Beta masih di Distributor Alfa; TC-AC-ACAL-149 dan TC-AC-ACAL-169 memiliki precondition Reassign yang sama dan Post Condition yang sama, sehingga satu siklus Reassign (langkah 17 dan 36) dipakai bersama dan pengamatan diurutkan per pengamat (Gamma lalu Alfa) untuk membatasi ganti akun. Pengamatan Distributor Alfa lalu Gamma pada langkah TC tersebut ditukar menjadi Gamma lalu Alfa dengan hasil yang sama.
- Spec 36 langkah, satu langkah di atas smell 35. Alasan: seluruh TC satu topik (scope log setelah perubahan hubungan entitas) dan satu permukaan; blok TC-AC-ACAL-162 serta blok TC-AC-ACAL-149 dan TC-AC-ACAL-169 berdiri sendiri dengan baseline dan pengamat sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pelaku kedua (Principal dan `Tono`) memakai sesi API (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`): bukan konteks kedua, tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (tanpa awalan `Verifikasi`): membaca baseline (langkah 1 dan 2), memicu aksi lewat sesi API (langkah 3, 4, 16, 17, 36), "Tunggu aksi selesai" (langkah 5 dan 18, bagian 8b butir 8), mengetik dan menutup Search (langkah 6, 9, 12, 15, 20, 22, 24, 26, 29, 31, 33, 35), ganti akun (langkah 10 dan 27), serta membuka menu dan tab (langkah 11, 19, 23, 28, 32).
- Asersi absence (langkah 8, 30, 34) memakai anchor positif: baris sesi lama `Tono` pada surface yang sama (langkah 7) dan empty state `No results found` hasil Search (langkah 30, 34). Asersi jumlah memakai baseline selisih (S-12), bukan angka absolut.
- TC-AC-ACAL-162 dan TC-AC-ACAL-169 menulis "filter User"; spec memakai Search karena opsi User untuk staf yang tidak punya baris dalam scope tidak ada di dropdown filter; baseline API (langkah 1 dan 2) memakai kueri Search yang sama dengan Search UI (langkah 6 dan 12) supaya jumlah sebanding.
- Temuan untuk QA:
  - TC-AC-ACAL-162 dan 169 menulis "filter User `Tono`" dan "filter User `Hendra Pratama`" sehingga opsi tidak dapat dipilih bila scope tidak memuat baris staf itu; spec memakai Search.
  - TC-AC-ACAL-162 Expected b ("hanya sesi baru setelah pindah yang tampil; sesi lama tidak tampil") tidak menyebut cara membedakan sesi lama dan baru; spec memakai baseline jumlah dan dua baris teratas.
  - TC-AC-ACAL-149 dan 169 memuat Reassign Partner Beta pada precondition tanpa menyebut aktor (Principal) kecuali di langkah; spec memakai sesi API Principal. Kredensial `Tono` dan `Hendra Pratama` tidak ada di TC; email akun memakai placeholder `{namaCompany}` password: `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`; `AC_ALFA_TC_PASSWORD`, `AC_GAMMA_TC_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
  - TC-AC-ACAL-149 tidak menyebut nama entri log lama Partner Beta; spec memakai baris Object `Partner` Name `Partner Beta` dari seed No 10.
  - TC-AC-ACAL-149 dan 162 mencatat Post Condition pengembalian state tanpa langkah observasi; dilakukan sebagai langkah pemulihan (langkah 16 dan 36) tanpa asersi.
