---
id: TC-FA-LBL-E2E-133-absence-log-edit-zero-delta-spasi-tepi-request-langsung-dan-label-lain
title: "Absence Log: Edit Zero-Delta, Spasi Tepi, Request Langsung, dan Label Lain"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-398
  - TC-FA-LBL-399
  - TC-FA-LBL-403
  - TC-FA-LBL-410
coverage:
  web: automated
---

# Absence Log: Edit Zero-Delta, Spasi Tepi, Request Langsung, dan Label Lain

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-133`):
  - `Log Edit 398 {runId}-133` (TC-FA-LBL-398)
  - `Log Edit 399 {runId}-133` (TC-FA-LBL-399)
  - `Api Zero 410 {runId}-133` (TC-FA-LBL-410)
  - `Log Edit 403 {runId}-133` (TC-FA-LBL-403); nama sesudah perubahan `Log Spur 403 {runId}-133`
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Asersi "tidak ada entri" memakai selisih jumlah entri terhadap baseline per surface (bagian 8b butir 2, surface agregat) karena audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12). Klien HTTP dengan token aktor Sarah Johnson (sesi API aktor, dinyatakan di `suite.md`) untuk permintaan langsung pada TC-FA-LBL-410.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-133`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-398: Edit zero-delta tidak menulis entri di ketiga surface

1. Ketik Search `Log Edit 398 {runId}-133`, tekan Enter
2. Catat baseline baris `Log Edit 398 {runId}-133`: Modified By dan Last Updated dari tabel
3. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log lewat fixture BE
4. Klik `⋯` pada baris `Log Edit 398 {runId}-133`, lalu klik `Edit`
5. Klik `[Save]` tanpa mengubah nama maupun warna
6. Verifikasi toast `No changes to save.`
7. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline langkah 3 (fixture BE)
8. Verifikasi Modified By dan Last Updated baris `Log Edit 398 {runId}-133` sama dengan baseline langkah 2

### TC-FA-LBL-399: Edit yang hanya menambah spasi tepi tidak menulis entri

9. Ganti isi kotak search dengan `Log Edit 399 {runId}-133`, tekan Enter
10. Catat baseline jumlah entri Changelog Labels lewat fixture BE
11. Klik `⋯` pada baris `Log Edit 399 {runId}-133`, lalu klik `Edit`
12. Ganti isi Label Name dengan spasi + `Log Edit 399 {runId}-133` + spasi
13. Klik `[Save]`
14. Verifikasi toast `No changes to save.`
15. Verifikasi jumlah entri Changelog Labels sama dengan baseline langkah 10 (tidak ada entri Edit baru; fixture BE)

### TC-FA-LBL-410: Edit zero-delta lewat API langsung menjawab sukses tanpa mutasi dan tanpa log

16. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log lewat fixture BE
17. Kirim permintaan Edit langsung ke server (token aktor Sarah Johnson) untuk `Api Zero 410 {runId}-133` dengan nama dan warna yang sama dengan nilai tersimpan hingga respons diterima
18. Verifikasi respons sukses 200
19. Verifikasi nama dan warna `Api Zero 410 {runId}-133` tidak berubah (fixture BE)
20. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline langkah 16 (fixture BE)

### TC-FA-LBL-403: Aksi pada satu label tidak menulis entri untuk label lain

21. Ganti isi kotak search dengan `Log Edit 403 {runId}-133`, tekan Enter
22. Catat baseline jumlah entri Changelog Labels lewat fixture BE
23. Klik `⋯` pada baris `Log Edit 403 {runId}-133`, lalu klik `Edit`
24. Ganti isi Label Name dengan `Log Spur 403 {runId}-133`
25. Klik `[Save]`
26. Tunggu aksi selesai (modal Edit Label tertutup)
27. Verifikasi jumlah entri Changelog Labels bertambah tepat satu dari baseline langkah 22 dan entri baru itu adalah Edit untuk `Log Spur 403 {runId}-133` (Old Value `Log Edit 403 {runId}-133`, New Value `Log Spur 403 {runId}-133`; fixture BE)
28. Verifikasi tidak ada entri baru untuk label lain di Changelog Labels (selisih jumlah entri satu, yaitu entri langkah 27)

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync) dan section yang memiliki TC pemicu. Subjudul `###` memetakan langkah ke TC granular.
- Langkah "Tunggu aksi selesai" mengikuti 8b butir 8: hasil aksi tidak diasersi langsung dan langkah berikutnya membaca log.
- P-5 (butir a): spec ini adalah spec absence (kelas g). Pemicu yang bukan objek uji (permintaan langsung ke server pada TC-FA-LBL-410) hanya membentuk kondisi yang diasersi tidak tercatat; tiap TC punya label dan baseline sendiri.
- Bagian 8b butir 1: pada TC-FA-LBL-410 yang diasersi hanya status respons dan state data lewat fixture BE; tampilan UI untuk respons yang sama tidak diasersi.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target pada Labels List.
- Baseline jumlah entri dibaca lewat fixture BE (TC menyebut pembukaan surface log lewat UI); selisih jumlah dipakai sebagai asersi "tidak ada entri". Toast `No changes to save.` (hasil server netral) dan Verifikasi respons menjadi anchor positif tiap TC (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-LBL-135 dan 136 (zero-delta pada spasi tepi dan hex huruf kecil) diuji dengan baseline di spec 044; spec ini memuat TC zero-delta lain dan Edit tanpa efek ke label lain.
- Temuan untuk QA:
  - TC-FA-LBL-398, 399, 410, dan 403: Post Condition tidak ada. TC-FA-LBL-398 Expected c ("Modified By dan Last Updated label tidak berubah") ditulis sebagai satu Verifikasi atas dua kolom baris yang sama.
  - TC-FA-LBL-403 menyebut "seluruh entri baru hanya merujuk Log Edit 403/Log Spur 403"; spec mengasersinya sebagai selisih tepat satu entri Edit (hanya Field `Label Name` yang berubah).
