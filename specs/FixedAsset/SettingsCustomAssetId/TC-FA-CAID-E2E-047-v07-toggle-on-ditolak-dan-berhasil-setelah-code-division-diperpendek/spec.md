---
id: TC-FA-CAID-E2E-047-v07-toggle-on-ditolak-dan-berhasil-setelah-code-division-diperpendek
title: "V-07: Toggle ON Ditolak lalu Berhasil Setelah Code Division Diperpendek"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-92
  - TC-FA-CAID-93
coverage:
  web: automated
---

# V-07: Toggle ON Ditolak lalu Berhasil Setelah Code Division Diperpendek

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `Company V07 65` (Pre-setup No 19). Email akun disediakan tim FE/BE (Pre-setup No 19); password `Spectra.env.FA_V0765_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (No 19): `Company V07 65` dengan satu aset Draft; Group Code `GRP-LONG-000001`, Category Code `CAT-LONG-000001`, Asset Name Code `AST-LONG-000001`, Separator `- (Dash)`, formula tanpa Purchase Date dan memuat Division Code; Master Switch OFF; Division Code `DIVISION-ABC-15` di-assign ke aset Draft itu. Keadaan Master Switch OFF dengan formula memuat Division Code disiapkan hook `before` lewat seed API.
- Kemampuan teknis: seed `Company V07 65` dan pengembalian ke keadaan awal sebelum run disediakan tim FE/BE; sesi API aktor untuk seed dan pemulihan (suite.md).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Code Division `DIVISION-ABC-15` diubah menjadi `DIVISION-AB-14` dan Master Switch menjadi ON. Hook `after` memulihkan Code Division ke `DIVISION-ABC-15` dan Master Switch ke OFF lewat seed API. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-92: Toggle ON ditolak V-07

1. Buka Fixed Asset > Assets > All Assets dan catat Asset ID aset sebagai nilai awal
2. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
3. Geser Master Switch ke ON
4. Verifikasi Master Switch kembali ke posisi OFF
5. Verifikasi kontrol form tetap di-dim dan disabled
6. Verifikasi alert inline tetap tampil di atas `[Save]` berbunyi `Asset ID would exceed 64 characters. Shorten the codes in your master data and try again.`
7. Buka Fixed Asset > Assets > All Assets
8. Verifikasi Asset ID aset sama dengan nilai awal pada langkah 1

### TC-FA-CAID-93: Toggle ON diulang dan berhasil setelah Code Division diperpendek

9. Buka Global Settings > User > Division
10. Ubah Code Division `DIVISION-ABC-15` menjadi `DIVISION-AB-14`, lalu klik `[Save]`
11. Tunggu aksi selesai
12. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
13. Geser Master Switch ke ON
14. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
15. Verifikasi Master Switch berada pada posisi ON
16. Buka Fixed Asset > Assets > All Assets
17. Verifikasi Asset ID aset menjadi `GRP-LONG-000001-CAT-LONG-000001-AST-LONG-000001-DIVISION-AB-14-1` (64 karakter)

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (mencatat Asset ID awal, S-12), membuka halaman tujuan, dan langkah 11 (tunggu aksi selesai karena langkah berikutnya berpindah surface).
- Urutan TC mengikuti nomor TC: Toggle ON yang ditolak mendahului Toggle ON yang berhasil.
- Efek permanen (S-06): `Company V07 65` adalah Company khusus milik skenario ini (bukan Company Alpha); langkah 10 mengubah Code Division `DIVISION-ABC-15` menjadi `DIVISION-AB-14` sehingga Last Updated Division berubah, dan Toggle ON pada langkah 13 mengubah Status konfigurasi serta menulis entri audit trail Custom Asset ID yang bersifat permanen (tidak dihapus). Hook `after` hanya memulihkan Code Division dan Master Switch lewat seed API; Last Updated dan entri audit trail yang sudah tercatat tidak dipulihkan.
- Pembagian TC lintas spec: TC-FA-CAID-86 sampai 89 ada di spec 031; TC-FA-CAID-90, TC-FA-CAID-91, dan TC-FA-CAID-334 ada di spec 032.
- Temuan untuk QA:
  - Tombol penyimpan perubahan Code Division di Global Settings > User > Division tidak disebut TC-FA-CAID-93 ("lalu simpan"); spec memakai `[Save]` mengikuti konvensi label form Edit.
  - Post Condition TC-FA-CAID-92 dan TC-FA-CAID-93 tidak diasersi karena TC tidak memberi langkah observasinya.
