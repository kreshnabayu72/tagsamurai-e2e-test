---
id: TC-FA-COA-E2E-075-multi-konteks-delete-dan-guard-berubah-antara-dialog-dan-confirm
title: "Multi-Konteks: Delete Single dan Guard Berubah antara Dialog Dibuka dan Confirm (Akun Dihapus, Diekspor, atau Dipakai Asset Class)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-64
  - TC-FA-COA-66
  - TC-FA-COA-137
  - TC-FA-COA-349
coverage:
  web: automated
---

# Multi-Konteks: Delete Single dan Guard Berubah antara Dialog Dibuka dan Confirm (Akun Dihapus, Diekspor, atau Dipakai Asset Class)

## Prerequisites

- Mode: FE+BE (backend nyata; tanpa intercept).
- Akun aktor sesi A: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi API aktor: pelaku kedua (sesi B pada TC) hanya memicu perubahan state (hapus akun, ekspor akun, membuat Asset Class pemakai akun) dan memakai sesi API sesuai butir "Sesi API aktor" di `suite.md`. TC-FA-COA-66 tidak menyebut sesi kedua; ekspor J-06 pada TC itu dipicu lewat sesi API.
- Seed dan pemulihan lewat API: mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; jalur ekspor Journal J-06 dan pembuatan Asset Class yang memakai akun sebagai Depreciation Expense disediakan tim FE/BE tanpa endpoint karangan.
- Flag Guided Tooltip halaman Chart of Accounts: di-set true oleh hook `before` suite (lihat `suite.md`).
- Data Pre-setup (akun sekali pakai milik spec, identitas di `Fixture.settings-chart-of-accounts` yang disediakan tim FE; nama kunci ditetapkan tim FE):

  | Akun | Code dan Name | State awal | TC |
  |---|---|---|---|
  | P56 | `CAP-8103` · `Capitalization Clearing – Delete Race` · Function Capitalization Offset | Active, Used By 0, Last Used in Journal kosong | TC-FA-COA-64 |
  | P61 | `4-7106` · `Gain on Disposal – Export Race` · Function Gain on Disposal | Inactive, Used By 0, Last Used in Journal kosong | TC-FA-COA-66 |
  | P10 | `5-6900` · `Depreciation Expense – Pool` · Function Depreciation Expense | Active, Used By 0 | TC-FA-COA-137 |
  | P96 | `5-6116` · `Depreciation Expense – Single Delete Race Used` · Function Depreciation Expense | Active, Used By 0, belum pernah diekspor, bukan nilai default company | TC-FA-COA-349 |

- Data Dinamis: Asset Class pemakai P10 dan P96 (dibuat sesi API pada langkah 20 dan 28; Name memuat suffix `{runId}-075`, dihapus di hook `after`; disediakan tim FE).
- Efek pada Pre-setup (S-06): P56 terhapus; P61 terisi Last Used in Journal; P10 dan P96 terpakai satu Asset Class (Used By 1) sampai Asset Class dihapus hook `after`. Hook `before` dan `after` mengembalikan keempat akun ke state awal lewat seeding (disediakan tim FE/BE). Last Updated tidak berubah pada P10 dan P96 (aksi ditolak).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): menghapus akun lewat sesi API; ekspor akun lewat jalur J-06; membuat dan menghapus Asset Class pemakai akun; membaca jumlah entri log penghapusan akun (L-04). Jam server dan jam browser sinkron untuk nilai bulan-tahun ekspor.
- Suite berjalan serial (`parallel: false`): spec mengubah akun Pre-setup bersama dan memakai Used By.
- Env var yang dipakai: `FA_TC_PASSWORD` (terdaftar).

## Test Steps

### TC-FA-COA-64: Konfirmasi Delete menjadi ditolak karena akun sudah dihapus user lain

1. Ketik Search `CAP-8103`, tekan Enter
2. Sesi A: klik row action `Delete` pada akun P56 untuk membuka dialog D-07
3. Hapus P56 lewat sesi API hingga penghapusan tersimpan
4. Catat baseline jumlah entri log penghapusan (L-04) atas P56 (kemampuan baca disediakan tim FE/BE)
5. Sesi A: klik `[Delete]`
6. Verifikasi toast netral "This account is no longer available." (severity Info) tampil
7. Verifikasi tabel disegarkan dan akun P56 tidak tampil
8. Verifikasi tidak ada entri log tambahan: jumlah entri log L-04 atas P56 sama dengan baseline langkah 4
9. Verifikasi dialog D-07 tertutup

### TC-FA-COA-66: Akun menjadi pernah diekspor setelah dialog Delete dibuka: server mengecek ulang dan menolak dengan D-05 tanpa toast

10. Ganti isi kotak search dengan `4-7106`, tekan Enter
11. Klik row action `Delete` pada akun P61 untuk membuka dialog D-07
12. Ekspor P61 melalui jalur API J-06 lewat sesi API hingga Last Used in Journal P61 tersimpan
13. Klik `[Delete]`
14. Verifikasi dialog blok `Cannot Delete Account` dengan bullet `• 4-7106 – Gain on Disposal – Export Race` dan teks D-05 "This account was last used in a journal in [Month Year]. Deleting it may break historical records." dengan [Month Year] = bulan dan tahun ekspor langkah 12 (format `Mon YYYY`)
15. Verifikasi tidak ada toast tambahan
16. Klik `[OK]`
17. Verifikasi akun P61 tetap ada di tabel

### TC-FA-COA-137: Akun menjadi dipakai Asset Class antara dialog Deactivate dibuka dan Confirm

18. Ganti isi kotak search dengan `5-6900`, tekan Enter
19. Sesi A: klik switch Status akun P10 untuk membuka dialog `Deactivate Account` (D-01)
20. Buat Asset Class baru dengan P10 sebagai Depreciation Expense lewat sesi API hingga tersimpan (Used By P10 menjadi 1)
21. Sesi A: klik `[Deactivate]`
22. Verifikasi dialog blok `Cannot Deactivate Account` dengan bullet `• 5-6900 – Depreciation Expense – Pool` dan teks "This account is used by 1 Asset Class and cannot be deactivated."
23. Verifikasi tidak ada toast tambahan
24. Klik `[OK]`
25. Verifikasi switch Status P10 tetap Active

### TC-FA-COA-349: Akun menjadi dipakai Asset Class setelah dialog Delete dibuka: server mengecek ulang dan menolak dengan D-06 tanpa toast

26. Ganti isi kotak search dengan `5-6116`, tekan Enter
27. Sesi A: klik row action `Delete` pada akun P96 untuk membuka dialog D-07
28. Buat Asset Class baru dengan P96 sebagai Depreciation Expense lewat sesi API hingga tersimpan (Used By P96 menjadi 1)
29. Sesi A: klik `[Delete]`
30. Verifikasi dialog blok `Cannot Delete Account` (D-06) dengan bullet `• 5-6116 – Depreciation Expense – Single Delete Race Used` dan teks "This account is used by 1 Asset Class and cannot be deleted."
31. Verifikasi tidak ada toast tambahan
32. Klik `[OK]`
33. Verifikasi akun P96 tetap ada di tabel
34. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Empat blok berdiri sendiri, satu kelas harness (state akun berubah antara dialog dibuka dan Confirm); jumlah langkah 34.
- Pelaku kedua adalah sesi API yang hanya memicu state, bukan konteks kedua; tidak ada sesi UI kedua.
- Langkah penghubung (S-03, S-09): langkah 1, 10, 18, dan 26 (Search untuk menemukan akun target, R-16, butir 8b.12) dan langkah 34 (mengosongkan Search); langkah 16, 24, dan 32 (menutup dialog blok dengan `[OK]` agar tabel dapat diasersi; TC tidak memberi langkah ini); langkah 2, 11, 19, dan 27 membuka dialog konfirmasi sesuai langkah TC.
- Asersi absence: "tidak ada toast tambahan" (langkah 15, 23, 31) didahului dialog blok sebagai anchor positif (butir 8b.2 dan 8b.11). Absence log TC-FA-COA-64 (Expected c) diasersi di spec ini dengan baseline (langkah 4 dan 8) dan anchor toast netral (langkah 6); butir `P-1`: asersi absence log milik TC-FA-COA-64 tetap di spec asalnya karena bergantung pada state yang dibangun langkah 3 dan sesi API yang sama (S-05).
- TC-FA-COA-137 Expected a ("Cek ulang menolak") adalah kesimpulan dari Expected b dan tidak teramati terpisah; dikerjakan lewat `Verifikasi` dialog langkah 22 (S-03).
- Temuan untuk QA:
  - TC-FA-COA-64 Expected c ("tidak ada entri log tambahan") tidak menyebut surface log; spec memakai jumlah entri log L-04 atas P56 lewat kemampuan baca disediakan tim FE/BE dan mengasumsikan baseline dicatat sesudah penghapusan oleh sesi API (langkah 4).
  - TC-FA-COA-66 Expected a menulis "teks guard 1 (D-05)" tanpa teks; spec memakai teks D-05 dari TC-FA-COA-59 dan 60 (cabang Inactive tanpa baris saran "Deactivate it instead."). TC-FA-COA-66 hanya memakai satu sesi (precondition tidak "dua sesi") sehingga pelaku kedua (ekspor J-06) ditulis sebagai pemicu sesi API.
  - TC-FA-COA-66, 137, 349 tidak menyebut cara menutup dialog blok sebelum asersi baris atau switch; spec menambah `[OK]` (asumsi tombol tersedia pada dialog blok, sesuai pola D-05/D-06) dan TC-FA-COA-66 dan 349 Post Condition "tidak ada perubahan data dan tidak ada log" tidak punya langkah observasi sehingga tidak diasersi.
  - TC-FA-COA-137 Post Condition "tidak ada log" tidak punya langkah observasi, tidak diasersi.
  - TC tidak menyebut kolom yang dicari Search; spec mencari berdasarkan Account Code.
  - P10 dan P96 adalah akun Pre-setup bersama yang menjadi target aksi UI yang selalu ditolak guard (tidak ada perubahan pada akun itu); yang berubah hanya Used By lewat Asset Class pemicu, dicatat di Prerequisites (S-06).
