---
id: TC-FA-LBL-E2E-015-hak-akses-dicabut-saat-modal-atau-dialog-terbuka
title: "Hak Akses Dicabut Saat Modal atau Dialog Terbuka"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-109
  - TC-FA-LBL-155
  - TC-FA-LBL-176
coverage:
  web: automated
---

# Hak Akses Dicabut Saat Modal atau Dialog Terbuka

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Role yang diuji (Create-Only login di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite; role lain lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Create-Only | #3 | `Fixture.assetLabeling.akun.createOnly` | `Spectra.env.FA_CREATEONLY_PASSWORD` | TC-FA-LBL-109 | 1 sampai 11 |
| Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` | TC-FA-LBL-155 | 12 sampai 25 |
| Delete-Only | #5 | `Fixture.assetLabeling.akun.deleteOnly` | `Spectra.env.FA_DELETEONLY_PASSWORD` | TC-FA-LBL-176 | 26 sampai 38 |

- Admin pencabut permission: sesi API Total Control sesi 2 (Pre-setup #9, `Fixture.assetLabeling.akun.totalControlSecond`, `Spectra.env.FA_TC2_PASSWORD`), dipilih spec karena TC hanya menyebut "sesi admin lain". Kemampuan mencabut dan memulihkan permission Create, Update, dan Delete pada role Create-Only, Update-Only, dan Delete-Only disediakan tim FE/BE (mekanisme tidak ditulis TC, PRD, atau LLD). Pemulihan dilakukan pada langkah 11, 25, dan 38 serta di hook `after` sebagai cadangan; state global ini (capability role) membuat suite berjalan serial.
- Environment variable: `FA_CREATEONLY_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, `FA_DELETEONLY_PASSWORD`, `FA_TC2_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Dinamis (Company Alpha, di-seed lewat sesi API di hook `before`, bersuffix `{runId}-015`, dibersihkan di hook `after`):

| Label | Dipakai di | Kondisi |
|---|---|---|
| `Edit Target 155 {runId}-015` | TC-FA-LBL-155 | Color `#EF4444`, Total Asset 0, bukan Default Label |
| `Delete Target 176 {runId}-015` | TC-FA-LBL-176 | bersih (Total Asset 0, bukan Default Label) |

- Label `Revoked 109 {runId}-015` adalah nama yang diketik pada langkah 2 dan tidak boleh terbentuk (TC-FA-LBL-109).
- Kemampuan teknis: sesi API aktor dan fixture BE (lihat `suite.md`).
- State global: capability role Create-Only, Update-Only, dan Delete-Only dicabut sementara dan dipulihkan (langkah 11, 25, 38; cadangan di hook `after`). Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Create-Only: TC-FA-LBL-109

1. Klik `[+ Label]`
2. Isi Label Name dengan `Revoked 109 {runId}-015`
3. Cabut permission Create dari role Create-Only lewat sesi API admin hingga perubahan tersimpan
4. Klik `[Submit]`
5. Verifikasi toast error `You don't have permission to do this.`
6. Verifikasi modal ditutup otomatis
7. Verifikasi tabel di-refresh
8. Verifikasi tombol `[+ Label]` Hidden setelah refresh
9. Ketik Search `Revoked 109`, tekan Enter
10. Verifikasi hasil Search tidak memuat baris `Revoked 109 {runId}-015`
11. Pulihkan permission Create pada role Create-Only lewat sesi API admin hingga perubahan tersimpan

### Update-Only: TC-FA-LBL-155

12. Ganti akun: Logout, login sebagai Update-Only `Fixture.assetLabeling.akun.updateOnly` (`Spectra.env.FA_UPDATEONLY_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
13. Ketik Search `Edit Target 155`, tekan Enter
14. Klik `⋯` pada baris `Edit Target 155 {runId}-015` lalu `Edit`
15. Ganti Label Name dengan `Revoked Edit 155 {runId}-015`
16. Cabut permission Update dari role Update-Only lewat sesi API admin hingga perubahan tersimpan
17. Klik `[Save]`
18. Verifikasi toast error `You don't have permission to do this.`
19. Verifikasi modal ditutup otomatis
20. Verifikasi tabel di-refresh
21. Verifikasi baris `Edit Target 155 {runId}-015` tampil dengan nama yang tidak berubah
22. Klik `⋯` pada baris `Edit Target 155 {runId}-015`
23. Verifikasi menu `⋯` memuat `Detail` dan opsi `Edit` Hidden
24. Tutup menu `⋯` dengan Esc
25. Pulihkan permission Update pada role Update-Only lewat sesi API admin hingga perubahan tersimpan

### Delete-Only: TC-FA-LBL-176

26. Ganti akun: Logout, login sebagai Delete-Only `Fixture.assetLabeling.akun.deleteOnly` (`Spectra.env.FA_DELETEONLY_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
27. Ketik Search `Delete Target 176`, tekan Enter
28. Klik `⋯` pada baris `Delete Target 176 {runId}-015` lalu klik `Delete`
29. Cabut permission Delete dari role Delete-Only lewat sesi API admin hingga perubahan tersimpan
30. Klik `[Delete]`
31. Verifikasi toast error `You don't have permission to do this.`
32. Verifikasi dialog ditutup
33. Verifikasi tabel di-refresh
34. Verifikasi baris `Delete Target 176 {runId}-015` masih tampil di tabel
35. Klik `⋯` pada baris `Delete Target 176 {runId}-015`
36. Verifikasi menu `⋯` memuat `Detail` dan opsi `Delete` Hidden
37. Tutup menu `⋯` dengan Esc
38. Pulihkan permission Delete pada role Delete-Only lewat sesi API admin hingga perubahan tersimpan

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 12 dan 26) karena akun pertama login di hook `before` dan langkah tiap role berbeda (bagian 3a, varian A).
- Langkah 3, 16, dan 29 ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (S-03): langkah 11, 25, dan 38 (memulihkan permission setelah tiap blok, R-08), langkah 9, 13, dan 27 (Search untuk menemukan baris target atau memeriksa absence, R-16), langkah 22 dan 35 (membuka menu `⋯` untuk menampilkan opsi yang Hidden), langkah 24 dan 37 (menutup menu).
- Absence (langkah 10, 23, 34 dan Hidden langkah 8, 36): toast error server (langkah 5, 18, 31) dan menu `⋯` yang tampil dengan `Detail` (langkah 23 dan 36) menjadi anchor positif (bagian 8b butir 2).
- Alasan di atas sekitar 35 langkah (38 langkah): tiga blok role berdiri sendiri dengan data seed sendiri, satu pola yang sama (hak dicabut di tengah aksi), kelas harness tunggal.
- Temuan untuk QA:
  - TC-FA-LBL-109, 155, dan 176 tidak menyebut cara mengamati "tabel di-refresh"; langkah 7, 20, dan 33 mengasersi tabel Labels List termuat ulang tanpa menyebut indikator tertentu.
  - TC-FA-LBL-109 Expected "tidak ada label dibuat" dan TC-FA-LBL-155 "nama label tidak berubah" ditulis lewat baris pada tabel (langkah 10 dan 21); TC tidak menyebut pemeriksaan di surface lain.
