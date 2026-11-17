---
id: TC-FA-PREF-E2E-113-changelog-paginasi-105-entri-ukuran-halaman-dan-input-nomor-halaman
title: "Changelog paginasi 105 entri: ukuran halaman dan input nomor halaman"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-342
  - TC-FA-PREF-343
  - TC-FA-PREF-344
  - TC-FA-PREF-345
  - TC-FA-PREF-346
sourceRules: ["§4.1.4#r1", "§9.5#r8"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#r1": 2
  "§9.5#r8": 2
anchor: [4, 8, 9, 13, 15, 19, 23, 25, 27]
coverage:
  web: automated
---

# Changelog paginasi 105 entri: ukuran halaman dan input nomor halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 105 entri (PB-C2; 11 halaman pada ukuran halaman bawaan 10) sebagai seluruh isi Changelog; seed disediakan tim FE/BE. Jumlah 105 berasal dari seed, bukan dari tabel yang hanya menampilkan satu halaman.
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-342: Paginasi bawaan 10 baris per halaman dengan pilihan ukuran halaman

1. Klik ikon View history di header tab Preferences
2. Verifikasi halaman 1 menampilkan 10 baris Changelog dari yang terbaru
3. Buka pilihan ukuran halaman
4. Verifikasi pilihan ukuran halaman memuat 10, 25, 50, dan 100 tanpa opsi "All"

### TC-FA-PREF-343: Mengganti ukuran halaman ke 25 kembali ke halaman 1

5. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
6. Pindah ke halaman 2
7. Pilih ukuran halaman 25
8. Verifikasi tabel menampilkan halaman 1
9. Verifikasi tabel menampilkan 25 baris
10. Pilih ukuran halaman 10

### TC-FA-PREF-344: Ukuran halaman 100 menampilkan 100 baris dan halaman 2 menyisakan 5 baris

11. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
12. Pilih ukuran halaman 100
13. Verifikasi halaman 1 menampilkan 100 baris
14. Pindah ke halaman 2
15. Verifikasi halaman 2 menampilkan 5 baris
16. Pilih ukuran halaman 10

### TC-FA-PREF-345: Input nomor halaman langsung lalu Enter membuka halaman tersebut

17. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
18. Ketik 3 pada input nomor halaman, tekan Enter
19. Verifikasi tabel menampilkan halaman 3 (baris ke-21 sampai ke-30)

### TC-FA-PREF-346: Nomor halaman tidak valid diabaikan

20. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
21. Pindah ke halaman 2
22. Ketik 0 pada input nomor halaman, tekan Enter
23. Verifikasi tabel tetap di halaman 2 setelah input 0
24. Ketik 12 pada input nomor halaman, tekan Enter
25. Verifikasi tabel tetap di halaman 2 setelah input 12 (melebihi halaman terakhir 11)
26. Ketik abc pada input nomor halaman, tekan Enter
27. Verifikasi tabel tetap di halaman 2 setelah input abc

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC.
- Langkah penghubung (S-03): "Pilih ukuran halaman 10" setelah TC-FA-PREF-343 dan TC-FA-PREF-344 memulihkan ukuran halaman bawaan sebelum TC berikutnya (S-09).
- Spec kelas e (volume data): seed 105 entri berada di atas ambang 100 baris; tidak ada kelas harness lain di spec ini.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-342 sampai 346; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Expected TC menyebut jumlah absolut Changelog (105 entri, 100 baris pada halaman 1, 5 baris pada halaman 2), sedangkan audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12). Spec mengikuti TC dan mengasumsikan seed PB-C2 menjadi seluruh isi Changelog; perlu dikonfirmasi tim FE/BE.
