---
id: TC-FA-LBL-E2E-134-absence-log-batas-katalog-dan-import-di-batas-company-limit
title: "Absence Log: Batas Katalog dan Import di Batas (Company Limit)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-401
  - TC-FA-LBL-458
  - TC-FA-LBL-484
coverage:
  web: automated
---

# Absence Log: Batas Katalog dan Import di Batas (Company Limit)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Limit (Pre-setup #11, pengguna `Total Control Limit`; email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Fixture.assetLabeling.akun.totalControlLimit`, password `Spectra.env.FA_TC_LIMIT_PASSWORD`. Login di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (nama bersuffix `{runId}-134`): `Limit Reject 401 {runId}-134` (TC-FA-LBL-401, tidak tersimpan), `Limit Direct 458 {runId}-134` (TC-FA-LBL-458, ditolak), `Import Limit 484 {runId}-134` (TC-FA-LBL-484; Default Label dalam berkas Import Asset Name, belum ada di katalog, berkas disediakan tim FE/BE; Pre-setup #14).
- Data Pre-setup: Company Limit (Pre-setup #11) dengan `Total Control Limit`; Master Data Count Limit diturunkan ke nilai terendah yang diizinkan (1000) dan katalog diisi lewat seed API tepat di batas.
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.akun.totalControlLimit` | identitas akun Total Control Company Limit (email disediakan tim FE) |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Klien HTTP dengan token aktor Total Control Limit (sesi API aktor) untuk permintaan langsung pada TC-FA-LBL-458. Import Asset Name dengan opsi `[Create Missing Labels]` dijalankan lewat UI tab Asset Name (rincian kontrol mengikuti TC `import/`; lihat Temuan untuk QA).
- State global: Master Data Count Limit Company Limit diturunkan ke 1000 dan katalog dipenuhi tepat di batas di hook `before`, dipulihkan di hook `after` (S-13: pelaku dan kemampuan disediakan tim FE/BE). Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label seed pengisi katalog dan label yang dibuat spec (nama bersuffix `{runId}-134`) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_TC_LIMIT_PASSWORD` (Total Control Company Limit) terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-401: Create yang ditolak batas katalog tidak menulis entri

1. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log lewat fixture BE
2. Klik `[+ Label]`
3. Isi Label Name `Limit Reject 401 {runId}-134`
4. Klik `[Submit]`
5. Verifikasi dialog dengan title `Label Limit Reached` dan body `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` tampil
6. Klik `[OK]` pada dialog D-06
7. Klik `✕` pada header modal Create Label
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`
10. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline langkah 1 (tidak ada entri Create baru untuk percobaan yang ditolak; fixture BE)

### TC-FA-LBL-458: Create di atas batas katalog lewat permintaan langsung ditolak

11. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log dan jumlah label katalog lewat fixture BE
12. Kirim permintaan langsung ke server (token aktor Total Control Limit) untuk membuat label `Limit Direct 458 {runId}-134` hingga respons diterima
13. Verifikasi permintaan ditolak
14. Verifikasi respons penolakan membawa nilai batas
15. Verifikasi label `Limit Direct 458 {runId}-134` tidak dibuat dan jumlah label katalog sama dengan baseline langkah 11 (fixture BE)
16. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline langkah 11 (fixture BE)

### TC-FA-LBL-484: Import [Create Missing Labels] saat katalog di batas tidak membuat label dan tidak menulis log

17. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log dan jumlah label katalog lewat fixture BE
18. Klik tab `Asset Name`
19. Jalankan Import Asset Name dengan berkas berisi Default Label `Import Limit 484 {runId}-134` yang belum ada dan pilih opsi `[Create Missing Labels]`
20. Tunggu aksi selesai (Import selesai)
21. Klik tab `Labels`
22. Ketik Search `Import Limit 484 {runId}-134`, tekan Enter
23. Verifikasi empty state `No results found` tampil
24. Verifikasi jumlah label katalog sama dengan baseline langkah 17 (fixture BE)
25. Klik icon Changelog di Table Tools
26. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline langkah 17 (tidak ada entri Create baru; fixture BE)
27. Klik `[✕]` pada Modal Changelog

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync) dan section yang memiliki TC pemicu. Subjudul `###` memetakan langkah ke TC granular.
- P-5 (butir a): spec ini adalah spec absence (kelas g). Pemicu yang bukan objek uji (permintaan langsung pada TC-FA-LBL-458 dan Import di batas pada TC-FA-LBL-484) hanya membentuk kondisi yang diasersi tidak tercatat; tiap TC punya label dan baseline sendiri.
- Bagian 8b butir 1: pada TC-FA-LBL-458 yang diasersi hanya penolakan, nilai batas pada respons, state data, dan jumlah entri log; kode status respons tidak ditulis karena TC tidak menyebutnya.
- Anchor positif absence (bagian 8b butir 2): dialog D-06 (TC-FA-LBL-401), Verifikasi penolakan (TC-FA-LBL-458), dan empty state `No results found` hasil Search (TC-FA-LBL-484); jumlah entri log dibandingkan dengan baseline per surface.
- Langkah penghubung (S-03): langkah menutup modal Create Label yang dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]` (S-08), Search `Import Limit 484` untuk menemukan baris (R-16), dan penutupan Modal Changelog.
- Baseline jumlah entri dibaca lewat fixture BE (TC menyebut pembukaan Modal Changelog); selisih jumlah dipakai sebagai asersi "tidak ada entri".
- Copy penolakan di sisi Import (TC-FA-LBL-484 Expected c) diasersi di TC `import/` dan tidak diasersi di spec ini.
- Temuan untuk QA:
  - Email akun Total Control Company Limit tidak tertulis di Pre-setup TC (#11 hanya menyebut `Total Control Limit`); disediakan tim FE.
  - TC-FA-LBL-401, 458, dan 484: Post Condition tidak ada. TC-FA-LBL-458 tidak menyebut kode status respons dan bentuk nilai batas di respons; spec hanya mengasersi bahwa permintaan ditolak dan respons membawa nilai batas.
  - TC-FA-LBL-484 tidak merinci langkah UI Import (halaman, berkas, dan tombol); spec menulis satu langkah aksi Import dan mekanisme rincinya mengikuti TC `import/`.
