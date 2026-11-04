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
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE; Account Name bersuffix `{runId}-075`):

  | Akun | Code dan Name | State awal | Padanan | TC |
  |---|---|---|---|---|
  | A | `DID075A` · `Capitalization Clearing – Delete Race {runId}-075` · Function Capitalization Offset | Active, Used By 0, Last Used in Journal kosong | P56 | TC-FA-COA-64 |
  | B | `DID075B` · `Gain on Disposal – Export Race {runId}-075` · Function Gain on Disposal | Inactive, Used By 0, Last Used in Journal kosong | P61 | TC-FA-COA-66 |
  | C | `DID075C` · `Depreciation Expense – Pool {runId}-075` · Function Depreciation Expense | Active, Used By 0 | P10 | TC-FA-COA-137 |
  | D | `DID075D` · `Depreciation Expense – Single Delete Race Used {runId}-075` · Function Depreciation Expense | Active, Used By 0, belum pernah diekspor, bukan nilai default company | P96 | TC-FA-COA-349 |

  Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID075A` sampai `DID075D` memuat nomor spec supaya unik per spec dan dibersihkan di hook `before` dan `after` (R-13).
- Data Dinamis: Asset Class pemakai akun C dan D (dibuat sesi API pada langkah 20 dan 28; Name memuat suffix `{runId}-075`, dihapus di hook `after`; disediakan tim FE).
- Efek pada data (S-06): semua target adalah akun milik spec sehingga data Pre-setup bersama tidak berubah. Akun A terhapus; akun B terisi Last Used in Journal; akun C dan D terpakai satu Asset Class (Used By 1) sampai Asset Class dihapus hook `after`; hook `after` menghapus keempat akun.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): menghapus akun lewat sesi API; ekspor akun lewat jalur J-06; membuat dan menghapus Asset Class pemakai akun; membaca jumlah entri log penghapusan akun (L-04). Jam server dan jam browser sinkron untuk nilai bulan-tahun ekspor.
- Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD` (terdaftar).

## Test Steps

### TC-FA-COA-64: Konfirmasi Delete menjadi ditolak karena akun sudah dihapus user lain

1. Ketik Search `DID075A`, tekan Enter
2. Sesi A: klik row action `Delete` pada akun A untuk membuka dialog D-07
3. Hapus akun A lewat sesi API hingga penghapusan tersimpan
4. Catat baseline jumlah entri log penghapusan (L-04) atas akun A (kemampuan baca disediakan tim FE/BE)
5. Sesi A: klik `[Delete]`
6. Verifikasi toast netral "This account is no longer available." (severity Info) tampil
7. Verifikasi tabel disegarkan dan akun A tidak tampil
8. Verifikasi tidak ada entri log tambahan: jumlah entri log L-04 atas akun A sama dengan baseline langkah 4
9. Verifikasi dialog D-07 tertutup

### TC-FA-COA-66: Akun menjadi pernah diekspor setelah dialog Delete dibuka: server mengecek ulang dan menolak dengan D-05 tanpa toast

10. Ganti isi kotak search dengan `DID075B`, tekan Enter
11. Klik row action `Delete` pada akun B untuk membuka dialog D-07
12. Ekspor akun B melalui jalur API J-06 lewat sesi API hingga Last Used in Journal akun B tersimpan
13. Klik `[Delete]`
14. Verifikasi dialog blok `Cannot Delete Account` dengan bullet `• DID075B – Gain on Disposal – Export Race {runId}-075` dan teks D-05 "This account was last used in a journal in [Month Year]. Deleting it may break historical records." dengan [Month Year] = bulan dan tahun ekspor langkah 12 (format `Mon YYYY`)
15. Verifikasi tidak ada toast tambahan
16. Klik `[OK]`
17. Verifikasi akun B tetap ada di tabel

### TC-FA-COA-137: Akun menjadi dipakai Asset Class antara dialog Deactivate dibuka dan Confirm

18. Ganti isi kotak search dengan `DID075C`, tekan Enter
19. Sesi A: klik switch Status akun C untuk membuka dialog `Deactivate Account` (D-01)
20. Buat Asset Class baru dengan akun C sebagai Depreciation Expense lewat sesi API hingga tersimpan (Used By akun C menjadi 1)
21. Sesi A: klik `[Deactivate]`
22. Verifikasi dialog blok `Cannot Deactivate Account` dengan bullet `• DID075C – Depreciation Expense – Pool {runId}-075` dan teks "This account is used by 1 Asset Class and cannot be deactivated."
23. Verifikasi tidak ada toast tambahan
24. Klik `[OK]`
25. Verifikasi switch Status akun C tetap Active

### TC-FA-COA-349: Akun menjadi dipakai Asset Class setelah dialog Delete dibuka: server mengecek ulang dan menolak dengan D-06 tanpa toast

26. Ganti isi kotak search dengan `DID075D`, tekan Enter
27. Sesi A: klik row action `Delete` pada akun D untuk membuka dialog D-07
28. Buat Asset Class baru dengan akun D sebagai Depreciation Expense lewat sesi API hingga tersimpan (Used By akun D menjadi 1)
29. Sesi A: klik `[Delete]`
30. Verifikasi dialog blok `Cannot Delete Account` (D-06) dengan bullet `• DID075D – Depreciation Expense – Single Delete Race Used {runId}-075` dan teks "This account is used by 1 Asset Class and cannot be deleted."
31. Verifikasi tidak ada toast tambahan
32. Klik `[OK]`
33. Verifikasi akun D tetap ada di tabel
34. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Empat blok berdiri sendiri, satu kelas harness (state akun berubah antara dialog dibuka dan Confirm); jumlah langkah 34.
- Pelaku kedua adalah sesi API yang hanya memicu state, bukan konteks kedua; tidak ada sesi UI kedua.
- Langkah penghubung (S-03, S-09): langkah 1, 10, 18, dan 26 (Search untuk menemukan akun target, R-16, butir 8b.13) dan langkah 34 (mengosongkan Search); langkah 16, 24, dan 32 (menutup dialog blok dengan `[OK]` agar tabel dapat diasersi; TC tidak memberi langkah ini); langkah 2, 11, 19, dan 27 membuka dialog konfirmasi sesuai langkah TC.
- Asersi absence: "tidak ada toast tambahan" (langkah 15, 23, 31) didahului dialog blok sebagai anchor positif (butir 8b.2 dan 8b.11). Absence log TC-FA-COA-64 (Expected c) diasersi di spec ini dengan baseline (langkah 4 dan 8) dan anchor toast netral (langkah 6); butir `P-1`: asersi absence log milik TC-FA-COA-64 tetap di spec asalnya karena bergantung pada state yang dibangun langkah 3 dan sesi API yang sama (S-05).
- Target aksi memakai akun milik spec (S-06): TC memakai P56, P61, P10, dan P96, spec memakai akun A sampai D (`DID075A` sampai `DID075D`) dengan state yang sama.
- TC-FA-COA-137 Expected a ("Cek ulang menolak") adalah kesimpulan dari Expected b dan tidak teramati terpisah; dikerjakan lewat `Verifikasi` dialog langkah 22 (S-03).
- `A-18`: Account Code literal tanpa suffix menjadi objek asersi pada dialog blok dan pencarian: `DID075A` (TC-FA-COA-64; langkah 1 dan 7), `DID075B` (TC-FA-COA-66; langkah 14 dan 17), `DID075C` (TC-FA-COA-137; langkah 22 dan 25), dan `DID075D` (TC-FA-COA-349; langkah 30 dan 33); keempatnya dibersihkan di hook `before` dan `after`.
- Temuan untuk QA:
  - TC-FA-COA-64 Expected c ("tidak ada entri log tambahan") tidak menyebut surface log; spec memakai jumlah entri log L-04 atas akun A lewat kemampuan baca disediakan tim FE/BE dan mengasumsikan baseline dicatat sesudah penghapusan oleh sesi API (langkah 4).
  - TC-FA-COA-66 Expected a menulis "teks guard 1 (D-05)" tanpa teks; spec memakai teks D-05 dari TC-FA-COA-59 dan 60 (cabang Inactive tanpa baris saran "Deactivate it instead."). TC-FA-COA-66 hanya memakai satu sesi (precondition tidak "dua sesi") sehingga pelaku kedua (ekspor J-06) ditulis sebagai pemicu sesi API.
  - TC-FA-COA-66, 137, 349 tidak menyebut cara menutup dialog blok sebelum asersi baris atau switch; spec menambah `[OK]` (asumsi tombol tersedia pada dialog blok, sesuai pola D-05/D-06) dan TC-FA-COA-66 dan 349 Post Condition "tidak ada perubahan data dan tidak ada log" tidak punya langkah observasi sehingga tidak diasersi.
  - TC-FA-COA-137 Post Condition "tidak ada log" tidak punya langkah observasi, tidak diasersi.
  - TC tidak menyebut kolom yang dicari Search; spec mencari berdasarkan Account Code.
