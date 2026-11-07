---
id: TC-FA-LBL-E2E-132-absence-log-delete-bulk-delete-campuran-dialog-ok-dan-penolakan-guard
title: "Absence Log: Bulk Delete Campuran atau Gagal, Dialog OK Tanpa Mutasi, dan Penolakan Guard"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-168
  - TC-FA-LBL-396
  - TC-FA-LBL-397
  - TC-FA-LBL-400
coverage:
  web: automated
---

# Absence Log: Bulk Delete Campuran atau Gagal, Dialog OK Tanpa Mutasi, dan Penolakan Guard

## Prerequisites

- Mode: FE+BE. Backend nyata. `Spectra.intercept()` hanya memaksa respons 5xx pada TC-FA-LBL-397 (pemicu, bukan objek uji).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label bersih milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-132`):
  - `Log Mixed 396 {runId}-132` (TC-FA-LBL-396)
  - `Log Mid A 397 {runId}-132`, `Log Mid B 397 {runId}-132`, `Log Mid C 397 {runId}-132` (TC-FA-LBL-397)
- Data Pre-setup: katalog Company Alpha (Pre-setup #12) dengan `High Priority` Total Asset 3 dan aset terkait (Pre-setup #13). `High Priority` hanya dipakai sebagai label dipakai yang aksinya diblokir atau dilewati guard dan tidak diubah (S-06 pengecualian); Modified By dan Last Updated tidak berubah.
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Asersi "tidak ada entri" memakai selisih jumlah entri terhadap baseline per surface (bagian 8b butir 2, surface agregat) karena audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12). `Spectra.intercept()` untuk memaksa respons 5xx pada penghapusan item kedua (endpoint ditentukan tim FE; intercept dilepas segera sesudah pemicu selesai, S-09; hook `after` melepasnya bila spec gagal di tengah).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-132`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-396: Bulk Delete campuran hanya mencatat label yang berhasil dihapus

1. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log lewat fixture BE
2. Atur ukuran halaman 25 pada Labels List supaya `High Priority` dan label seed spec tampil tanpa Search
3. Centang baris `Log Mixed 396 {runId}-132`
4. Centang baris `High Priority`
5. Klik `Bulk Action` lalu klik `Delete`
6. Klik `[Continue]` pada dialog D-04
7. Tunggu aksi selesai (dialog D-04 tertutup)
8. Verifikasi pada Changelog Labels, System Log aktor, dan Activity Log jumlah entri bertambah tepat satu dari baseline langkah 1 dan entri baru itu adalah Delete untuk `Log Mixed 396 {runId}-132` (fixture BE)
9. Verifikasi pada ketiga surface itu tidak ada entri Delete baru untuk `High Priority`

### TC-FA-LBL-397: Bulk Delete yang gagal 5xx di tengah hanya mencatat label yang benar-benar terhapus

10. Catat baseline jumlah entri Changelog Labels lewat fixture BE
11. Ketik Search `397 {runId}-132`, tekan Enter
12. Centang baris `Log Mid A 397 {runId}-132`
13. Centang baris `Log Mid B 397 {runId}-132`
14. Centang baris `Log Mid C 397 {runId}-132`
15. Klik `Bulk Action` lalu klik `Delete`
16. Paksa respons 5xx untuk item kedua (`Spectra.intercept()`)
17. Klik `[Delete]` pada dialog D-03
18. Lepas intercept
19. Tunggu aksi selesai (tabel di-refresh)
20. Catat label di antara `Log Mid A 397 {runId}-132`, `Log Mid B 397 {runId}-132`, dan `Log Mid C 397 {runId}-132` yang masih ada di tabel
21. Klik `Unselect All` untuk menghapus seleksi
22. Verifikasi sedikitnya satu dari ketiga label hilang dari tabel dan sedikitnya satu masih ada (langkah 20)
23. Verifikasi setiap label yang tidak lagi ada di tabel (langkah 20) memiliki tepat satu entri Delete baru di Changelog Labels (fixture BE)
24. Verifikasi jumlah entri Changelog Labels bertambah sebanyak label yang hilang dari baseline langkah 10 dan tidak ada entri Delete baru untuk label yang masih ada di tabel

### TC-FA-LBL-168: OK pada D-02 menutup dialog tanpa mutasi dan tanpa log

25. Catat baseline jumlah entri Changelog Labels lewat fixture BE
26. Ganti isi kotak search dengan `High Priority`, tekan Enter
27. Klik `⋯` pada baris `High Priority`, lalu klik `Delete`
28. Klik `[OK]` pada dialog D-02
29. Verifikasi dialog D-02 tertutup
30. Verifikasi tidak ada toast yang tampil
31. Verifikasi baris `High Priority` masih tampil dengan Total Asset `3`
32. Klik icon Changelog di Table Tools
33. Verifikasi jumlah entri Changelog Labels sama dengan baseline langkah 25 (fixture BE)
34. Ketik Search `High Priority` di toolbar Modal Changelog, tekan Enter
35. Verifikasi hasil Search memuat sedikitnya satu entri untuk `High Priority` (mis. Create `High Priority`) atau empty state `No results found`
36. Verifikasi hasil Search tidak memuat entri dengan Action `Delete` untuk `High Priority`
37. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-400: Delete yang ditolak guard tidak menulis entri

38. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log lewat fixture BE
39. Klik `⋯` pada baris `High Priority`, lalu klik `Delete`
40. Klik `[OK]` pada dialog D-02
41. Tunggu aksi selesai (dialog D-02 tertutup)
42. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline langkah 38 (fixture BE): tidak ada entri baru di ketiga surface

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync) dan section yang memiliki TC pemicu. Subjudul `###` memetakan langkah ke TC granular.
- Langkah "Tunggu aksi selesai" mengikuti 8b butir 8: hasil aksi tidak diasersi langsung dan langkah berikutnya membaca log.
- P-5 (butir a): spec ini adalah spec absence (kelas g). Pemicu yang bukan objek uji (respons 5xx pada TC-FA-LBL-397) hanya membentuk kondisi yang diasersi tidak tercatat; tiap TC punya label dan baseline sendiri.
- Anchor absence (bagian 8b butir 2): langkah 35 memverifikasi hasil Search Changelog memuat sedikitnya satu entri (mis. Create `High Priority`) atau empty state sebelum langkah 36 mengasersi tidak adanya entri Delete, supaya asersi absence tidak lolos hanya karena Search belum selesai atau tidak berjalan; bukan bagian Expected TC (S-03).
- Anchor TC-FA-LBL-397 (S-01, S-15): langkah 22 memastikan hasil run bukan vakum (sedikitnya satu label hilang dan satu masih ada) sebelum asersi log pada langkah 23 dan 24; bukan bagian Expected TC (S-03).
- Langkah penghubung (S-03): langkah 2 (ukuran halaman 25 supaya label seed dan `High Priority` tampil tanpa Search), langkah penutup seleksi `Unselect All` (S-09), Search `High Priority` (R-16), dan penutupan Modal Changelog.
- Pembagian TC lintas spec: dialog D-02 lain diuji di spec 051 dan 052; TC-FA-LBL-168 hanya ada di spec ini karena Expected-nya memuat absence log (S-05).
- Baseline jumlah entri dibaca lewat fixture BE (TC menyebut pembukaan surface log lewat UI); selisih jumlah dipakai sebagai asersi "tidak ada entri" dan entri positif (Delete Log Mixed 396 {runId}-132) menjadi anchor tiap surface (bagian 8b butir 2).
- Spec ini di atas smell (42 langkah) karena langkah pencatatan baseline dan pembandingan jumlah entri log (pola baca-log berulang) dikecualikan menurut bagian 3 prinsip 13; selebihnya 30 langkah. Semua blok satu kelas (absence log atas aksi Delete) dan berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-LBL-396, 397, 168, dan 400: Post Condition tidak ada. TC-FA-LBL-397 Expected tidak mengandalkan hasil per item ("hasil per item tidak diasumsikan"): asersi memakai label yang hilang dari tabel sebagai penentu.
  - TC-FA-LBL-397 hasil per item sengaja tidak diasumsikan ("hasil per item tidak diasumsikan"), sehingga langkah 23 dan 24 bersyarat hasil run dan tidak deterministik; spec mengikuti TC dengan anchor langkah 22 dan menunggu TC memutuskan hasil yang diharapkan (T-308) untuk dideterministikkan.
  - TC-FA-LBL-168 Expected b (Total Asset `3` tidak berubah) bergantung pada Pre-setup #12; Total Asset diasersi sebagai angka karena seed Pre-setup tidak diubah spec lain (S-06).
