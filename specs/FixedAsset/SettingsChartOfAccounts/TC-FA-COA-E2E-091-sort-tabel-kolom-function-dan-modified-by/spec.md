---
id: TC-FA-COA-E2E-091-sort-tabel-kolom-function-dan-modified-by
title: "Sort Tabel: Siklus Tiga Tahap pada Kolom Function dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-173
coverage:
  web: automated
---

# Sort Tabel: Siklus Tiga Tahap pada Kolom Function dan Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hanya dibaca, tidak diubah; disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):

  | Akun | Account Code | Account Name | Function |
  |---|---|---|---|
  | P1 | `5-6001` | Depreciation Expense – Admin | Depreciation Expense |
  | P2 | `6-2001` | Repairs & Maintenance Expense | Capitalization Offset |
  | P3 | `4-7001` | Gain on Disposal | Gain on Disposal |
  | P4 | `1-1002` | Equipment – Legacy Code | Asset Cost |

- Kolom Modified By tidak tampil secara default dan ditampilkan lewat Setup Column pada langkah 2 sampai 3 (precondition TC-FA-COA-173); langkah 22 sampai 23 memulihkannya (R-24).
- Nilai Modified By akun P1 sampai P4: sedikitnya dua user pengubah dengan nama lengkap berbeda (S-11). Identitas user pengubah tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE.
- Urutan relatif yang diasersi pada sort Function (label): Asset Cost (P4), Capitalization Offset (P2), Depreciation Expense (P1), Gain on Disposal (P3). Ukuran halaman diubah ke 100 pada langkah 1 agar akun P terlihat di satu halaman dan dipulihkan ke 10 pada langkah 24.
- State yang diubah spec: ukuran halaman, kolom Modified By (ditampilkan lalu disembunyikan lagi), dan sort (tiap siklus berakhir netral). Tidak ada data yang ditulis. Hook `after` menghapus preferensi kolom dan tabel di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-173: Sort siklus tiga tahap pada kolom Function dan Modified By

1. Ubah jumlah baris per halaman menjadi 100
2. Klik header Actions ⋯ > `Setup Column...`
3. Centang kolom `Modified By`, klik `[Save]`
4. Klik header Function satu kali
5. Verifikasi indikator naik (↑) aktif pada header Function
6. Verifikasi baris urut A-Z menurut label: Asset Cost (P4), Capitalization Offset (P2), Depreciation Expense (P1), Gain on Disposal (P3)
7. Klik header Function kedua kali
8. Verifikasi indikator turun (↓) aktif pada header Function
9. Verifikasi urutan Z-A: Gain on Disposal (P3), Depreciation Expense (P1), Capitalization Offset (P2), Asset Cost (P4)
10. Klik header Function ketiga kali
11. Verifikasi indikator header Function netral
12. Verifikasi urutan kembali ke default Account Code A-Z: urutan relatif P4, P3, P1, P2
13. Klik header Modified By satu kali
14. Verifikasi indikator naik (↑) aktif pada header Modified By
15. Verifikasi baris urut A-Z tanpa membedakan huruf besar-kecil menurut nama lengkap user pengubah (nama yang mendasari tampilan `[First Name] [Last Initial]`)
16. Klik header Modified By kedua kali
17. Verifikasi indikator turun (↓) aktif pada header Modified By
18. Verifikasi urutan Z-A menurut nama lengkap user pengubah
19. Klik header Modified By ketiga kali
20. Verifikasi indikator header Modified By netral
21. Verifikasi urutan kembali ke default Account Code A-Z: urutan relatif P4, P3, P1, P2
22. Klik header Actions ⋯ > `Setup Column...`
23. Hilangkan centang kolom `Modified By`, klik `[Save]`
24. Ubah jumlah baris per halaman kembali menjadi 10

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 dan 24 (ukuran halaman 100 agar akun P terlihat bersama, lalu dipulihkan); langkah 2 dan 3 (menampilkan kolom Modified By, precondition d TC-FA-COA-173); langkah 22 dan 23 (pemulihan Setup Column eksplisit, R-24 dan 8b.13).
- Tiap siklus sort berakhir netral sehingga tidak ada langkah reset sort tambahan.
- Kolom Modified By ditampilkan `[First Name] [Last Initial]` (R-14); sortingnya menurut nama lengkap sesuai Expected d TC-FA-COA-173, sehingga langkah 15 dan 18 mengasersi urutan menurut nama lengkap.
- Spec ini hanya memuat TC-FA-COA-173.
- Temuan untuk QA:
  - TC-FA-COA-173 tidak menyebut ukuran halaman ataupun identitas user pengubah akun P1 sampai P4; spec memakai ukuran halaman 100 dan mengasumsikan sedikitnya dua nama lengkap berbeda tersedia (S-11).
  - Butir d dan e TC-FA-COA-173 tidak memberi urutan konkret nama; spec mengasersi urutan menurut nama lengkap tanpa nama literal.
  - Dengan akun Pre-setup lebih dari 100 baris, akun P1 sampai P4 mungkin tidak seluruhnya berada di halaman 1 pada sort Modified By; perlu konfirmasi tim FE tentang urutan baris seed.
