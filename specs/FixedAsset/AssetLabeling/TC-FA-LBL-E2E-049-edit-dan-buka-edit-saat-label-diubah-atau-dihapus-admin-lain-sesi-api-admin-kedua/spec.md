---
id: TC-FA-LBL-E2E-049-edit-dan-buka-edit-saat-label-diubah-atau-dihapus-admin-lain-sesi-api-admin-kedua
title: "Edit dan Buka Edit Saat Label Diubah atau Dihapus Admin Lain (Sesi API Admin Kedua)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-113
  - TC-FA-LBL-469
  - TC-FA-LBL-470
  - TC-FA-LBL-482
  - TC-FA-LBL-483
coverage:
  web: automated
---

# Edit dan Buka Edit Saat Label Diubah atau Dihapus Admin Lain (Sesi API Admin Kedua)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Admin kedua hanya memicu perubahan state lewat sesi API (bukan sesi UI kedua).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Admin kedua: Total Control sesi 2 (Pre-setup #9) `Fixture.assetLabeling.akun.totalControlSecond`, password `Spectra.env.FA_TC2_PASSWORD`, dipakai lewat login API password (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE dan dinyatakan di `suite.md`). Sesi UI tetap satu: sesi 1 (Pre-setup #1).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-049`):
  - `Edit Target 113 {runId}-049` (TC-FA-LBL-113)
  - `Race Open 470 {runId}-049` (TC-FA-LBL-470)
  - `Race Gone 469 {runId}-049` (TC-FA-LBL-469)
  - `Anchor Target 482 {runId}-049` (TC-FA-LBL-482)
  - `Anchor Base 483 {runId}-049` (TC-FA-LBL-483)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.totalControl` | `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1) |
  | `Fixture.assetLabeling.akun.totalControlSecond` | `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9) |

- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis di TC): fixture BE untuk membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log (S-12). Baseline log sesi 1 pada TC-FA-LBL-483 dicatat sebelum `[Save]` sesi 1.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` dan `Spectra.env.FA_TC2_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-113: Membuka Edit mengambil data terkini label, bukan data dari daftar yang basi

1. Ketik Search `Edit Target 113 {runId}-049`, tekan Enter
2. Admin kedua (sesi API): edit label `Edit Target 113 {runId}-049` menjadi nama `Edit Fresh 113 {runId}-049` hingga perubahan tersimpan
3. Sesi 1: klik `⋯` pada baris `Edit Target 113 {runId}-049` (daftar belum di-refresh), lalu klik `Edit`
4. Verifikasi Popup Edit Label di sesi 1 terisi nama terkini `Edit Fresh 113 {runId}-049`
5. Klik icon `[✕]`

### TC-FA-LBL-470: Membuka Edit untuk label yang sudah dihapus admin lain

6. Ganti isi kotak search dengan `Race Open 470 {runId}-049`, tekan Enter
7. Admin kedua (sesi API): hapus label `Race Open 470 {runId}-049` hingga penghapusan tersimpan
8. Sesi 1: klik `⋯` pada baris `Race Open 470 {runId}-049`, lalu klik `Edit`
9. Verifikasi toast `This label is no longer available.` tampil
10. Verifikasi Popup Edit Label tidak dibuka
11. Verifikasi tabel di-refresh dan baris `Race Open 470 {runId}-049` tidak tampil

### TC-FA-LBL-469: Edit label yang sudah dihapus admin lain

12. Ganti isi kotak search dengan `Race Gone 469 {runId}-049`, tekan Enter
13. Sesi 1: klik `⋯` pada baris `Race Gone 469 {runId}-049`, lalu klik `Edit`
14. Ganti isi Label Name dengan `Race Gone 469 {runId}-049 X`
15. Admin kedua (sesi API): hapus label `Race Gone 469 {runId}-049` hingga penghapusan tersimpan
16. Sesi 1: klik `[Save]`
17. Verifikasi toast `This label is no longer available.` tampil
18. Verifikasi modal Edit Label di sesi 1 tertutup
19. Verifikasi tabel di-refresh dan baris `Race Gone 469 {runId}-049` tidak tampil
20. Verifikasi tidak ada entri Edit untuk label `Race Gone 469 {runId}-049` di Changelog Labels, System Log aktor sesi 1, dan Activity Log (dicari berdasarkan nama bersuffix unik, baseline nol)

### TC-FA-LBL-482: Save tanpa perubahan setelah admin lain mengubah label dibandingkan dengan nilai tersimpan, bukan isian awal modal

21. Ganti isi kotak search dengan `Anchor Target 482 {runId}-049`, tekan Enter
22. Sesi 1: klik `⋯` pada baris `Anchor Target 482 {runId}-049`, lalu klik `Edit`, dan biarkan modal terbuka
23. Admin kedua (sesi API): edit label `Anchor Target 482 {runId}-049` menjadi `Anchor Other 482 {runId}-049` hingga perubahan tersimpan
24. Sesi 1: klik `[Save]` tanpa mengubah nama maupun warna
25. Verifikasi toast `Success, label has been updated.` (bukan `No changes to save.`)
26. Verifikasi nama akhir label `Anchor Target 482 {runId}-049`
27. Verifikasi Changelog Labels memuat entri Edit Field `Label Name` Old Value `Anchor Other 482 {runId}-049` New Value `Anchor Target 482 {runId}-049`

### TC-FA-LBL-483: Save dengan nama yang sudah sama dengan nilai tersimpan setelah admin lain mengubahnya dianggap zero-delta

28. Ganti isi kotak search dengan `Anchor Base 483 {runId}-049`, tekan Enter
29. Sesi 1: klik `⋯` pada baris `Anchor Base 483 {runId}-049`, lalu klik `Edit`, dan ubah Label Name menjadi `Anchor Same 483 {runId}-049` tanpa Save
30. Admin kedua (sesi API): edit label `Anchor Base 483 {runId}-049` menjadi `Anchor Same 483 {runId}-049` hingga perubahan tersimpan
31. Catat baseline jumlah entri System Log aktor sesi 1 dan Activity Log aktor sesi 1 lewat fixture BE
32. Sesi 1: klik `[Save]`
33. Verifikasi toast `No changes to save.` untuk sesi 1
34. Verifikasi modal Edit Label di sesi 1 tertutup
35. Verifikasi Changelog Labels memuat tepat satu entri Edit untuk label `Anchor Same 483 {runId}-049` (dari admin kedua)
36. Verifikasi System Log aktor sesi 1 dan Activity Log aktor sesi 1 sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6, 12, 21, 28 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 5, 31 menutup modal bersih (TC-FA-LBL-113) dan mencatat baseline log sesi 1 sebelum `[Save]` (TC-FA-LBL-483, S-12).
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-470 (membuka Edit tanpa Save) ditaruh sebelum TC-FA-LBL-469 (Save pada label yang dihapus); tiap TC memakai label seed sendiri.
- Asersi "tidak ada entri Edit" pada TC-FA-LBL-469 dan "sesi 1 tidak menambah entri" pada TC-FA-LBL-483 adalah asersi jumlah dengan baseline (bagian 3 prinsip 13g), bukan kelas g; TC-FA-LBL-469 dan TC-FA-LBL-483 tidak ada di spec absence log. Pada TC-FA-LBL-469 label sudah dihapus admin kedua sehingga Changelog memuat entri Delete; asersi hanya menyangkut entri Edit.
- Ukuran spec (36 langkah, di atas smell 35 langkah): kelima TC satu pola (modal Edit sesi 1 melawan perubahan admin kedua lewat sesi API), satu akun UI, label seed milik masing-masing, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-469 Expected "tidak ada entri log" tidak menyebut surface; spec memakai Changelog Labels, System Log aktor sesi 1, dan Activity Log.
  - TC-FA-LBL-469 menyebut hasil "nama `Race Gone 469 X`" sebagai data; spec memakai nama bersuffix `Race Gone 469 {runId}-049 X` supaya unik per run.
