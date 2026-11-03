---
id: TC-FA-LBL-E2E-044-edit-save-zero-delta-tanpa-perubahan-spasi-tepi-hex-huruf-kecil
title: "Edit: Save Zero-Delta (Tanpa Perubahan, Spasi Tepi, Hex Huruf Kecil)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-134
  - TC-FA-LBL-135
  - TC-FA-LBL-136
coverage:
  web: automated
---

# Edit: Save Zero-Delta (Tanpa Perubahan, Spasi Tepi, Hex Huruf Kecil)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-044`):
  - `Edit Target 134 {runId}-044` (satu label seed untuk ketiga TC; zero-delta tidak mengubah label sehingga dapat dipakai berurutan)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.hexKecilSama` | `#ef4444` |

- Kemampuan teknis: mengetik ke kolom Hex dan memakai fixture BE untuk membaca jumlah entri Changelog Labels, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; S-12).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `Edit Target 134 {runId}-044`, tekan Enter
2. Catat baseline baris `Edit Target 134 {runId}-044`: nama, Color Hex, Modified By, dan Last Updated dari tabel
3. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log lewat fixture BE

### TC-FA-LBL-134: Save tanpa perubahan dianggap sukses tanpa mutasi dan menampilkan toast netral

4. Klik `⋯` pada baris `Edit Target 134 {runId}-044`, lalu klik `Edit`
5. Klik `[Save]` tanpa mengubah nama maupun warna
6. Verifikasi toast `No changes to save.` (bukan `Success, label has been updated.`)
7. Verifikasi modal Edit Label tertutup normal

### TC-FA-LBL-135: Save dengan perbedaan hanya spasi tepi pada nama dianggap zero-delta

8. Klik `⋯` pada baris `Edit Target 134 {runId}-044`, lalu klik `Edit`
9. Ubah Label Name menjadi dua spasi + `Edit Target 134 {runId}-044` + dua spasi
10. Klik `[Save]`
11. Verifikasi toast `No changes to save.`
12. Verifikasi modal Edit Label tertutup
13. Verifikasi baris `Edit Target 134 {runId}-044` menampilkan nama dan Color Hex sama dengan baseline
14. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline

### TC-FA-LBL-136: Save dengan hex huruf kecil untuk warna yang sama dianggap zero-delta

15. Klik `⋯` pada baris `Edit Target 134 {runId}-044`, lalu klik `Edit`
16. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
17. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexKecilSama`
18. Verifikasi kolom Hex menampilkan `Fixture.assetLabeling.warnaSeed`
19. Klik `[Save]`
20. Verifikasi toast `No changes to save.`
21. Verifikasi modal Edit Label tertutup
22. Verifikasi Last Updated baris `Edit Target 134 {runId}-044` sama dengan baseline
23. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 2, 3 mencatat baseline baris dan baseline jumlah entri log sebelum aksi pertama (S-12).
- Asersi jumlah entri sama dengan baseline pada TC-FA-LBL-135 dan TC-FA-LBL-136 adalah asersi jumlah, bukan kelas g (bagian 3 prinsip 13g); asersi absence murni untuk zero-delta ada di spec nomor 132 (TC-FA-LBL-398 dan TC-FA-LBL-399) dengan aksi dan baseline sendiri.
- Seeding minimal (S-11): ketiga TC memakai satu label seed; zero-delta tidak mengubah label, sehingga Precondition "Label seed `Edit Target <nomor TC>`" tiap TC terpenuhi oleh label yang sama.
- Temuan untuk QA:
  - TC-FA-LBL-134 Post Condition a (Modified By dan Last Updated tidak berubah) dan b (Changelog, System Log aktor, dan Activity Log tidak bertambah, detail di Section 5) tidak punya langkah observasi di TC dan tidak diasersi di TC-FA-LBL-134; baseline baris dan log dicatat pada langkah 2, 3 dan dipakai TC-FA-LBL-135 dan TC-FA-LBL-136.
  - TC-FA-LBL-135 Expected b dan TC-FA-LBL-136 Expected c ("tidak ada entri log") tidak menyebut surface log; spec memakai tiga surface sebagaimana Post Condition TC-FA-LBL-134 (Changelog, System Log aktor, Activity Log).
