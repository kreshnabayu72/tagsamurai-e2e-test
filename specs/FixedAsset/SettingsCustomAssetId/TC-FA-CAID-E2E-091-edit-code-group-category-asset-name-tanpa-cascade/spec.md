---
id: TC-FA-CAID-E2E-091-edit-code-group-category-asset-name-tanpa-cascade
title: "Edit Code Group, Category, dan Asset Name: Tidak Memperbarui Asset ID Sampai Save Berikutnya"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-292
  - TC-FA-CAID-293
  - TC-FA-CAID-294
  - TC-FA-CAID-295
coverage:
  web: automated
---

# Edit Code Group, Category, dan Asset Name: Tidak Memperbarui Asset ID Sampai Save Berikutnya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Code Edit Code (Pre-setup No 36; akun sendiri, bukan akun Pre-setup No 1; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email dan env var password disediakan tim FE/BE, nama env tidak tertulis di TC), password `Spectra.env.FA_CODEEDITCODE_TC_PASSWORD` (nama usulan, perlu konfirmasi tim FE; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Settings > Groups, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Code Edit Code (No 36; milik spec ini, terpisah dari Company Alpha sehingga tidak mengubah master Pre-setup bersama): hook `before` men-seed konfigurasi baseline B1 dan aset A1 Active `JKT/LAP/T490/0926/1`, A2 Draft `JKT/LAP/T490/0926/2`, A3 Waiting for Approval `JKT/LAP/T490/0000/3`; master milik Company ini: Group `Jakarta Office` (Code `JKT`), Category `IT Equipment > Laptop` (Code `LAP`), Asset Name `ThinkPad T490` (Code `T490`).
- Fixture: nilai data Pre-setup di atas (akun Company, master data, Code awal, Asset ID seed) dibaca dari `Fixture.customAssetId.<kunci>`; berkas `fixtures/customAssetId.json` belum ada (prasyarat tahap script yang disediakan tim FE/BE).
- Kode master yang diubah (Dinamis No 13), dengan menu tempat mengubahnya:

| Master | Menu | Code awal | Code baru |
|---|---|---|---|
| Group `Jakarta Office` | Fixed Asset > Settings > Groups | `JKT` | `JKR` |
| Category `IT Equipment > Laptop` | Fixed Asset > Settings > Categories | `LAP` | `LPT` |
| Asset Name `ThinkPad T490` | Fixed Asset > Settings > Asset Master > Asset Name | `T490` | `TP490` |

- Data Dinamis: Code Group `JKR`, Category `LPT`, Asset Name `TP490`; dibersihkan oleh seed reset Company sebelum TC berikutnya.
- Efek permanen dan pemulihan Company Code Edit Code (S-06): Last Updated master Group, Category, dan Asset Name berubah dan entri audit trail perubahan Code bertambah (entri log tidak dapat dihapus); Code master dipulihkan ke `JKT`, `LAP`, `T490`, serta konfigurasi ke B1 dan aset A1 sampai A3, lewat seed API (kemampuan pemulihan Code master disediakan tim FE/BE) di hook `before` dan `after` spec ini; seed Company khusus ini juga dikembalikan tim FE/BE sebelum tiap run (`suite.md`).
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- State global: kode master dan konfigurasi Company Code Edit Code diubah; hook `after` memulihkan kode master ke `JKT`, `LAP`, `T490`, konfigurasi ke baseline B1, dan aset A1 sampai A3, lalu sesi ke akun default suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-292: Edit Code Group tidak mengubah Asset ID aset yang sudah terbit

1. Buka Fixed Asset > Settings > Groups
2. Ubah Code Group `Jakarta Office` dari `JKT` menjadi `JKR` lalu simpan
3. Tunggu aksi selesai
4. Buka Fixed Asset > Assets > All Assets dan perhatikan A1 sampai A3
5. Verifikasi A1, A2, A3 tetap `JKT/LAP/T490/0926/1`, `JKT/LAP/T490/0926/2`, `JKT/LAP/T490/0000/3`

### TC-FA-CAID-293: Edit Code Category tidak mengubah Asset ID aset yang sudah terbit

6. Buka Fixed Asset > Settings > Categories
7. Ubah Code Category `IT Equipment > Laptop` dari `LAP` menjadi `LPT` lalu simpan
8. Tunggu aksi selesai
9. Buka Fixed Asset > Assets > All Assets dan perhatikan A1 sampai A3
10. Verifikasi A1, A2, A3 tetap memuat segmen `LAP` seperti semula

### TC-FA-CAID-294: Edit Code Asset Name tidak mengubah Asset ID aset yang sudah terbit

11. Buka Fixed Asset > Settings > Asset Master > Asset Name
12. Ubah Code Asset Name `ThinkPad T490` dari `T490` menjadi `TP490` lalu simpan
13. Tunggu aksi selesai
14. Buka Fixed Asset > Assets > All Assets dan perhatikan A1 sampai A3
15. Verifikasi A1, A2, A3 tetap memuat segmen `T490` seperti semula

### TC-FA-CAID-295: Save berikutnya me-resolve ulang Code Group, Category, dan Asset Name dari master terkini

16. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, pilih Separator `- (Dash)` lalu klik `[Save]`
17. Tunggu aksi selesai
18. Buka Fixed Asset > Assets > All Assets
19. Verifikasi A1 menjadi `JKR-LPT-TP490-0926-1`, A2 menjadi `JKR-LPT-TP490-0926-2`, dan A3 menjadi `JKR-LPT-TP490-0000-3`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (buka halaman), 3, 8, 13, 17 (tunggu aksi selesai sebelum pindah surface). TC-FA-CAID-295 melanjutkan state TC-FA-CAID-292 sampai 294 (ketiganya mengubah Code master), jadi tidak ada pemulihan di antaranya.
- Tabel kode master di Prerequisites memetakan menu dan nilai tiap pengubahan; urutan langkah tiap blok tetap ditulis eksplisit karena menu dan label field berbeda.
- Temuan untuk QA:
  - TC-FA-CAID-292 sampai 294 hanya menyebut "simpan" tanpa Expected toast; hasil simpan teramati lewat TC-FA-CAID-295.
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
