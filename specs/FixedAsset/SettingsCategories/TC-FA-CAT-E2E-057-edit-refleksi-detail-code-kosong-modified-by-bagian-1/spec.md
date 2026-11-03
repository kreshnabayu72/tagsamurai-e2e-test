---
id: TC-FA-CAT-E2E-057-edit-refleksi-detail-code-kosong-modified-by-bagian-1
title: "Edit: Refleksi Popup Detail, Code Kosong Auto-generate, dan Dedup Edit (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-199
  - TC-FA-CAT-200
  - TC-FA-CAT-202
coverage:
  web: automated
---

# Edit: Refleksi Popup Detail, Code Kosong Auto-generate, dan Dedup Edit (Bagian 1)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite.
- Akun aktor kedua (TC-202): Total Control (Pre-setup #1) client CatCode (Pre-setup #34), `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` client CatCode, password `Spectra.env.FA_TC_PASSWORD`. Login dilakukan lewat langkah ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca. CatCode (#34): baris `Dedup 1` (Code `ELEC`) dibaca; baris `Dedup 2` (Code `ELEC2`) menjadi target Edit TC-202 sesuai TC (data tidak dapat dimiliki spec karena Code `ELEC2` sudah dipakai seed). Efek pada Pre-setup: Category Name `Dedup 2` berubah menjadi `Elec`, Last Updated dan Modified By berubah, serta audit trail bertambah (Changelog, Activity Log, System Log). Hook `before` memastikan keadaan dasar #34 (Dedup 1 sampai Dedup 7) dan hook `after` mengembalikan Category Name `Dedup 2` lewat seed API (disediakan tim FE).
- Data milik spec di CatMain (seed API di hook `before` lewat jalur Create resmi, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Edit Root {runId}-057` | `E057ROOT` | L1; dipilih di sidebar |
  | Ancestor TC-199 | `Electronics {runId}-057` | `E057ELEC` | anak `Edit Root`, internal |
  | Descendant TC-199 | `Laptop {runId}-057` | `E057LT` | anak `Electronics {runId}-057`, leaf |
  | Descendant TC-199 | `Monitor {runId}-057` | `E057MN` | anak `Electronics {runId}-057`, leaf |
  | Target TC-200 | `Furniture {runId}-057` | `E057FURN` | anak `Edit Root`, leaf; menggantikan `Furniture` (Code `FURN`) |

- TC-200 memakai Category Name literal `Office Furniture` (tanpa suffix) karena Code hasil generate (`OF`) diturunkan dari nama; keunikan nama berlaku per parent sehingga nama itu hanya ada di bawah `Edit Root {runId}-057`. Hook `before` menghapus sisa kategori ber-Code `OF` dari run atau spec lain agar hasil generate tidak menjadi `OF2` (R-13); hook `after` menghapus kategori itu.
- Hook `before` menunggu sampai menit berganti bila diperlukan agar asersi tidak bergantung pada ketelitian menit.
- Kemampuan teknis: Modal Changelog dapat dibaca dan dicari; jumlah baris hasil Search dicatat sebagai baseline (S-12, 8b butir 10); jam server dan jam browser sinkron.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-199: Rename kategori langsung terlihat di Popup Detail dan sidebar

1. Klik node `Edit Root {runId}-057` di sidebar
2. Klik elipsis (⋯) pada baris `Electronics {runId}-057` > `Edit`
3. Ubah Category Name menjadi `Electronics Renamed {runId}-057`
4. Klik `[Save]`
5. Tunggu aksi selesai (popup Edit tertutup)
6. Klik node `Electronics Renamed {runId}-057` di sidebar
7. Verifikasi sidebar menampilkan `Electronics Renamed {runId}-057` dengan anak `Laptop {runId}-057` dan `Monitor {runId}-057`
8. Klik elipsis (⋯) pada baris `Laptop {runId}-057` > `Detail`
9. Verifikasi header Popup Detail `Laptop {runId}-057` menampilkan full path `Edit Root {runId}-057 › Electronics Renamed {runId}-057 › Laptop {runId}-057`
10. Tutup Popup Detail dengan `✕`

### TC-FA-CAT-200: Edit yang mengosongkan Code memicu auto-generate dalam transaksi yang sama

11. Klik node `Edit Root {runId}-057` di sidebar
12. Klik elipsis (⋯) pada baris `Furniture {runId}-057` > `Edit`
13. Kosongkan Code
14. Ubah Category Name menjadi `Office Furniture`
15. Klik `[Save]`
16. Verifikasi toast `Success, category has been updated.`
17. Verifikasi kolom Code baris `Office Furniture` berubah dari `E057FURN` menjadi `OF`

### TC-FA-CAT-202: Edit yang mengosongkan Code dengan kandidat bentrok kategori lain memakai dedup

18. Logout
19. Login sebagai Total Control client CatCode (Pre-setup #34)
20. Buka Fixed Asset > Settings > Categories
21. Buka Modal Changelog
22. Ketik Search `ELEC2`, tekan Enter
23. Catat jumlah baris hasil Search sebagai baseline
24. Tutup Modal Changelog
25. Ketik Search `ELEC2`, tekan Enter
26. Klik elipsis (⋯) pada baris `Dedup 2` (Code `ELEC2`) > `Edit`
27. Ubah Category Name menjadi `Elec`
28. Kosongkan Code
29. Klik `[Save]`
30. Verifikasi kolom Code baris `Elec` tampil `ELEC2` (kandidat `ELEC` bentrok dengan `Dedup 1`; Code lama node itu sendiri tidak dihitung bentrok, Code tetap `ELEC2`)
31. Buka Modal Changelog
32. Ketik Search `ELEC2`, tekan Enter
33. Verifikasi jumlah baris hasil Search sama dengan baseline (tidak ada baris Edit Field `Code` baru)
34. Ganti isi kotak search dengan `Dedup 2`, tekan Enter
35. Verifikasi baris teratas hasil Search adalah Edit Field `Category Name` Old Value `Dedup 2` New Value `Elec`
36. Tutup Modal Changelog

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-199, TC-200, dan TC-202 ada di spec ini; TC-204, TC-206, dan TC-625 ada di spec 058.
- Penyesuaian data (S-06, S-12): TC-199 dan TC-200 memakai baris `Electronics`, `Laptop`, dan `Furniture` Pre-setup #20 sebagai target; spec memakai node milik spec bersuffix `{runId}-057` di bawah `Edit Root`, sehingga path pada header Popup Detail memuat segmen `Edit Root {runId}-057` di depan path TC (`Electronics Renamed › Laptop`). Pengecualian nama literal `Office Furniture` pada TC-200 dijelaskan di Prerequisites (Code hasil generate diturunkan dari nama).
- Langkah penghubung (S-03, tanpa awalan Verifikasi): memilih node di sidebar agar baris target tampil tanpa Search; menunggu aksi selesai setelah `[Save]` TC-199; menutup Popup Detail; ganti akun ke client CatCode (Logout, Login, buka halaman); membuka, Search, dan menutup Modal Changelog; Search `ELEC2` untuk menemukan baris target (R-16). Search di Modal Changelog dan baseline jumlah baris dipakai karena audit trail permanen (S-12).
- Urutan Expected TC-199: butir b (sidebar) ditulis sebelum butir a (header Popup Detail) mengikuti urutan state; Popup Detail membuka di atas sidebar (8b butir 5).
- Temuan untuk QA:
  - TC-199 dan TC-200 Post Condition (Asset Name terkait, Changelog Edit Field `Category Name` dan `Code` Old `FURN` New `OF`) tanpa langkah observasi di TC sehingga tidak diasersi (S-01).
  - TC-199 Expected a menyebut header Popup Detail `Electronics Renamed › Laptop`; spec memakai path dengan segmen root milik spec (lihat Notes penyesuaian data).
  - TC-200 tidak menyatakan bahwa Code `OF` harus bebas sebelum Edit; bila `OF` sudah dipakai data lain, hasil generate menjadi `OF2` (dedup Tier 1). Spec menjamin kebebasan `OF` lewat hook `before`.
  - TC-202 Expected b menyebut "Changelog hanya mencatat Field Category Name" tetapi TC tidak memberi langkah membuka Changelog; spec menambah langkah observasi Changelog sebagai langkah verifikasi Expected, dengan baseline karena Changelog adalah audit trail permanen.
  - TC-202 mengedit baris Pre-setup `Dedup 2`; kategori ber-Code `ELEC2` tidak dapat dimiliki spec selama seed #34 ada (Code unik global). Pemulihan nama oleh seed API menulis entri Changelog tambahan (efek dicatat di Prerequisites).
- Spec melewati 35 langkah (36 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
