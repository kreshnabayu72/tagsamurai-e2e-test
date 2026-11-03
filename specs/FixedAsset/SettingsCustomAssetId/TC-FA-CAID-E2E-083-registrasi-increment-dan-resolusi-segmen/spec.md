---
id: TC-FA-CAID-E2E-083-registrasi-increment-dan-resolusi-segmen
title: "Registrasi Aset: Increment Berurutan, Resolusi Segmen, Separator, dan Legacy Register"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-256
  - TC-FA-CAID-257
  - TC-FA-CAID-258
  - TC-FA-CAID-259
  - TC-FA-CAID-260
coverage:
  web: automated
---

# Registrasi Aset: Increment Berurutan, Resolusi Segmen, Separator, dan Legacy Register

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Register (Pre-setup No 24; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email akun Company Register disediakan tim FE/BE menurut Pre-setup TC; lihat Temuan untuk QA), password `Spectra.env.FA_REGISTER_TC_PASSWORD` (nama env dari kolom `Akun dan Env Var` Pre-setup No 24; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Register (No 24): plan Professional, tanpa aset, master data Division `Human Resources` (Code `HR`), Asset Name `ThinkPad T490` (Code `T490`), Group `Jakarta Office` (Code `JKT`), Category `Laptop` (Code `LAP`), Brand `Lenovo`. Konfigurasi per TC di-seed lewat seed API: B1 (TC-FA-CAID-256, 257), B4 (258: Initial Company `ABC`, kedelapan segmen tercentang, Separator Slash), B1 dengan Separator None (259), B5 (260: Group, Category, Asset Name, Increment, tanpa Purchase Date, Slash). Tiap blok TC dimulai dari Company Register tanpa aset.
- Data Dinamis: aset Draft dan aset Active hasil registrasi (Dinamis No 1 sampai 4); dibersihkan oleh seed reset Company sebelum TC berikutnya. Nilai field khusus Legacy (Tanggal Perolehan Historis, Status Berkas Dokumen Fisik, Status Label Fisik Lama) valid apa pun (G-12), diambil dari `Fixture.customAssetId.<kunci>` dan tidak diasersi.
- Fixture: nilai data Pre-setup di atas (akun Company, master data, nilai field khusus Legacy) dibaca dari `Fixture.customAssetId.<kunci>`; berkas `fixtures/customAssetId.json` belum ada (prasyarat tahap script yang disediakan tim FE/BE). Nilai field Quick Register pada langkah 2 sampai 30 (Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`) adalah data master Pre-setup No 24.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- State global: konfigurasi singleton Company Register diubah (Separator Space pada TC-FA-CAID-259) dan aset dibuat; hook `after` memulihkan Company Register ke konfigurasi B1 tanpa aset dan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-256: Quick Register menerbitkan Asset ID format kustom berstatus Draft dengan Purchase Date 0000

1. Buka Fixed Asset > Assets > Registration
2. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
3. Verifikasi toast sukses `Success, asset registered as draft.` tampil
4. Perhatikan baris aset baru pada tabel Registration
5. Verifikasi baris aset baru berstatus Draft
6. Verifikasi baris aset baru menampilkan Asset ID `JKT/LAP/T490/0000/1` (segmen Purchase Date `0000` karena belum terisi, Increment `1`)

### TC-FA-CAID-257: Registrasi berurutan menghasilkan Increment 1, 2, 3 tanpa padding nol

7. Pulihkan Company Register ke konfigurasi B1 tanpa aset (seed API)
8. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]` (registrasi pertama)
9. Ulangi registrasi kedua
10. Ulangi registrasi ketiga
11. Verifikasi Asset ID ketiga aset berurutan `JKT/LAP/T490/0000/1`, `JKT/LAP/T490/0000/2`, `JKT/LAP/T490/0000/3`

### TC-FA-CAID-258: Resolusi kedelapan segmen saat registrasi: Division terisi dan Division kosong

12. Pulihkan Company Register ke konfigurasi B4 (Initial Company `ABC`, kedelapan segmen tercentang, Separator Slash) tanpa aset (seed API)
13. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Division `Human Resources`, Condition `Normal`, lalu klik `[Save as Draft]`
14. Registrasi aset kedua tanpa memilih Division
15. Verifikasi aset pertama bernilai `ABC/JKT/LAP/T490/HR/0000/0000/1` (Initial Company `ABC`, Group `JKT`, Category `LAP`, Asset Name `T490`, Division `HR`, Account `0000`, Purchase Date `0000`, Increment `1`)
16. Verifikasi aset kedua bernilai `ABC/JKT/LAP/T490/0000/0000/0000/2` dengan segmen Division `0000` karena aset tanpa Division

### TC-FA-CAID-259: Separator None menyambung segmen dan Space memakai spasi tunggal

17. Pulihkan Company Register ke konfigurasi B1 dengan Separator `None` tanpa aset (seed API)
18. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]` (aset pertama)
19. Perhatikan Asset ID aset pertama
20. Verifikasi aset pertama bernilai `JKTLAPT49000001`
21. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, ubah Separator menjadi `Space`, lalu klik `[Save]`
22. Tunggu aksi selesai
23. Buka Fixed Asset > Assets > Registration
24. Verifikasi aset pertama bernilai `JKT LAP T490 0000 1`
25. Registrasi aset kedua: klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
26. Perhatikan Asset ID kedua aset
27. Verifikasi aset kedua bernilai `JKT LAP T490 0000 2` tanpa spasi tambahan di kiri-kanan pemisah

### TC-FA-CAID-260: Legacy Register langsung Active dan menerbitkan Asset ID dengan Increment

28. Pulihkan Company Register ke konfigurasi B5 tanpa aset (seed API)
29. Buka Fixed Asset > Assets > Registration, lalu klik `[+ Legacy Register]`
30. Isi field Quick Register: Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, dan field khusus Legacy (Tanggal Perolehan Historis, Status Berkas Dokumen Fisik, Status Label Fisik Lama) dengan nilai valid dari fixture (lihat Prerequisites), lalu simpan
31. Tunggu aksi selesai
32. Buka Fixed Asset > Assets > All Assets dan cari aset baru
33. Verifikasi aset baru berstatus Active
34. Verifikasi aset baru menampilkan Asset ID `JKT/LAP/T490/1`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1, 23, 29, 32 (buka halaman), 4 dan 19 dan 26 (perhatikan), 7, 12, 17, 28 (pemulihan Company Register antar TC lewat seed, sesuai Dinamis "dibersihkan oleh seed reset Company"), 22 dan 31 (tunggu aksi selesai sebelum pindah surface, bagian 8b butir 8; hasil simpan Legacy Register pada langkah 30 tidak diasersi langsung).
- Penyimpangan urutan TC-FA-CAID-259: Expected b (aset pertama setelah Save Separator Space) diamati sebelum registrasi aset kedua agar nilai aset pertama diasersi pada keadaan yang sama dengan Expected; urutan state, bukan urutan penulisan Expected TC.
- Temuan untuk QA:
  - Email akun Total Control Company Register tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}` dan "email disediakan tim FE/BE").
  - TC-FA-CAID-260 tidak menyebut nilai field khusus Legacy selain "valid apa pun" (G-12) dan tidak mengasersinya; nilai diambil dari fixture yang disediakan tim FE/BE. Asersi penanda aset warisan tidak ditulis karena Expected TC hanya memuat status Active dan teks Asset ID.
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
