---
id: TC-FA-PREF-E2E-114-changelog-paginasi-105-entri-search-filter-sort-dan-paginasi-saling-mempengaruhi
title: "Changelog paginasi 105 entri: Search, Filter, Sort, dan paginasi saling mempengaruhi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-347
  - TC-FA-PREF-348
  - TC-FA-PREF-349
sourceRules: ["§4.1.4#r2"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#r2": 21
anchor: [4, 8, 13, 20]
coverage:
  web: automated
---

# Changelog paginasi 105 entri: Search, Filter, Sort, dan paginasi saling mempengaruhi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 105 entri (PB-C2; 11 halaman pada ukuran halaman bawaan 10) sebagai seluruh isi Changelog; seed disediakan tim FE/BE. Jumlah 105 berasal dari seed, bukan dari tabel yang hanya menampilkan satu halaman.
- Seed PB-C2 memuat lebih dari 25 entri dengan Modified By Rina A agar halaman berikutnya tersedia pada TC-FA-PREF-349 (jumlah entri Rina A tidak tertulis di TC; lihat Temuan untuk QA); disediakan tim FE/BE.
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-347: Search dan Apply Filter dari halaman 2 kembali ke halaman 1

1. Klik ikon View history di header tab Preferences
2. Pindah ke halaman 2
3. Ketik Search "Rina", tekan Enter
4. Verifikasi tabel menampilkan halaman 1
5. Klik `✕` pada Search, tekan Enter
6. Pindah ke halaman 2
7. Klik ikon Filter, pilih opsi Edit pada dropdown Action, lalu klik `[Apply]`
8. Verifikasi tabel menampilkan halaman 1
9. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-PREF-348: Mengganti sort tetap di nomor halaman sekarang

10. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
11. Pindah ke halaman 2
12. Klik header kolom Action satu kali
13. Verifikasi tabel tetap berada di halaman 2 setelah sort diganti
14. Klik header kolom Action dua kali hingga indikator sort hilang

### TC-FA-PREF-349: Mengganti halaman dan ukuran halaman tidak mereset Search, Filter, dan Sort

15. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
16. Ketik Search "Rina", tekan Enter
17. Klik header kolom Action satu kali
18. Pilih ukuran halaman 25
19. Pindah ke halaman berikutnya
20. Verifikasi kata kunci Search "Rina" tetap aktif setelah ukuran halaman diganti
21. Verifikasi sort Action ascending tetap aktif setelah ukuran halaman diganti
22. Pilih ukuran halaman 10
23. Klik `✕` pada Search, tekan Enter
24. Klik header kolom Action dua kali hingga indikator sort hilang

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC.
- Langkah penghubung (S-03): langkah pemulihan di akhir tiap TC (kosongkan filter, kosongkan Search, kembalikan sort netral, kembalikan ukuran halaman 10) menjaga TC berikutnya mulai dari keadaan bersih (S-09); langkah "Klik `✕` pada Search, tekan Enter" di tengah TC-FA-PREF-347 mengosongkan Search sebelum Filter diuji sesuai langkah 4 TC.
- Spec kelas e (volume data): seed 105 entri berada di atas ambang 100 baris.
- Pada TC-FA-PREF-349 Verifikasi Search dan sort ditulis setelah langkah "Pindah ke halaman berikutnya" karena Expected menyebut keadaan "setelah ukuran halaman diganti" sedangkan langkah TC memuat ukuran halaman lalu halaman berikutnya; keadaan akhir kedua aksi diamati sekali.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-347 sampai 349; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - TC-FA-PREF-349 langkah 5 ("Pindah ke halaman berikutnya bila tersedia") bersyarat dan jumlah entri Modified By Rina A pada seed PB-C2 tidak tertulis; spec menuliskan langkahnya tanpa syarat dan mencatat kebutuhan seed di Prerequisites.
  - Expected TC menyebut jumlah absolut Changelog (105 entri), sedangkan audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12). Spec mengikuti TC dan mengasumsikan seed PB-C2 menjadi seluruh isi Changelog; perlu dikonfirmasi tim FE/BE.
