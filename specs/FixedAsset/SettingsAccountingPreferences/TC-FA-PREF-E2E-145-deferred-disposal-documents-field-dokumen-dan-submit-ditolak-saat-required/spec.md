---
id: TC-FA-PREF-E2E-145-deferred-disposal-documents-field-dokumen-dan-submit-ditolak-saat-required
title: "[DEFERRED] Disposal Documents: field dokumen dan Submit ditolak saat Required"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-458
  - TC-FA-PREF-459
  - TC-FA-PREF-460
  - TC-FA-PREF-461
  - TC-FA-PREF-462
  - TC-FA-PREF-463
  - TC-FA-PREF-464
  - TC-FA-PREF-465
coverage:
  web: automated
---

# [DEFERRED] Disposal Documents: field dokumen dan Submit ditolak saat Required

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (Disposal Documents keenam jenis Optional). Data modul Disposal Execute dan Physical Count & Reconciliation (PC-16) disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Disposal Documents dibentuk lewat seed: keenam jenis Optional untuk TC-FA-PREF-458 dan 459, lalu keenam jenis Required untuk TC-FA-PREF-460 sampai 465 (tiap TC hanya mengasersi jenisnya sendiri).
- Jenis pelepasan yang diuji (langkah 7 sampai 13 diulang per baris; parameter hanya dari tabel ini):

  | TC | Jenis | Modul form | Pesan |
  |---|---|---|---|
  | TC-FA-PREF-460 | Sell | Disposal Execute | A document is required for sell disposals. |
  | TC-FA-PREF-461 | Scrap | Disposal Execute | A document is required for scrap disposals. |
  | TC-FA-PREF-462 | Lost | Disposal Execute | A document is required for lost disposals. |
  | TC-FA-PREF-463 | Donate | Disposal Execute | A document is required for donate disposals. |
  | TC-FA-PREF-464 | Trade-in | Disposal Execute | A document is required for trade-in disposals. |
  | TC-FA-PREF-465 | Write-off | Physical Count & Reconciliation | A document is required for write-off disposals. |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan data transaksi pelepasan; pengisian field wajib form transaksi pelepasan lewat UI modul pemilik.
- State global yang diubah: Disposal Documents company; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-458: Field dokumen selalu ada di form Execute walau Disposal Documents Optional

1. Seed Disposal Documents keenam jenis tersimpan Optional hingga tersimpan
2. Buka form Execute transaksi pelepasan jenis Sell pada Disposal Execute
3. Verifikasi field dokumen tampil pada form Execute

### TC-FA-PREF-459: Field dokumen selalu ada di form Write-off pada Reconciliation walau Optional

4. Buka form Write-off pada Physical Count & Reconciliation
5. Verifikasi field dokumen tampil pada form Write-off

### TC-FA-PREF-460 sampai TC-FA-PREF-465: Submit pelepasan tanpa dokumen ditolak saat Required (Sell, Scrap, Lost, Donate, Trade-in, Write-off)

6. Seed Disposal Documents keenam jenis tersimpan Required hingga tersimpan

Untuk setiap baris tabel "Jenis pelepasan yang diuji" (langkah 7 sampai 13):

7. Buka form transaksi pelepasan jenis `<Jenis>` pada `<Modul form>` dan isi semua field wajib tanpa melampirkan dokumen
8. Klik submit transaksi
9. Verifikasi pesan `<Pesan>` tampil di form transaksi
10. Verifikasi transaksi tidak tersubmit
11. Klik [×] pada form transaksi
12. Verifikasi dialog D-04 tampil tanpa Title dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
13. Klik [Leave] pada dialog D-04

14. Pulihkan Disposal Documents keenam jenis ke nilai awal PC-1 (Optional) lewat seed hingga tersimpan

## Notes

- Langkah 7 sampai 13 diulang enam kali (bagian 8b butir 7); parameter tiap iterasi hanya dari tabel di Prerequisites dan tidak ada langkah bersyarat. `Verifikasi` tiap iterasi satu per klausa (S-01). Ekspansi: 7 langkah x 6 iterasi = 42 langkah ditambah 7 langkah lain (49); penutupan form dirty memakai pola S-08 (klik [×], `Verifikasi` dialog D-04, klik [Leave]) sehingga tiap iterasi bertambah 2 langkah. Alasan melewati sekitar 35: seluruh blok satu kelas harness (fungsional, modul pemilik), strukturnya seragam, dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna.
- Langkah penghubung (S-03): langkah 6 (seed keenam jenis Required sekaligus; TC mensyaratkan hanya jenis uji Required dan jenis lain Optional dari PC-1, sedangkan asersi tiap TC hanya menyangkut jenisnya sendiri), langkah 11 dan 13 (menutup form transaksi yang terisi lewat [×] dan [Leave] sebelum iterasi berikutnya, S-08, S-09; `Verifikasi` dialog D-04 pada langkah 12 tidak perlu dicatat lagi), langkah 14 (pemulihan state, R-08).
- Search tidak dipakai: form transaksi dibuka dari modul pemilik tanpa memilih baris tabel.
- Temuan untuk QA:
  - TC-FA-PREF-458 dan 459 tidak menyebut label field dokumen; spec mengasersi "field dokumen" sesuai Expected TC.
  - TC-FA-PREF-460 sampai 465 menyebut Expected "transaksi tidak tersubmit" dan Post Condition "Transaksi tidak tersimpan" tanpa langkah observasi; langkah 10 mengasersi Expected "transaksi tidak tersubmit" tanpa tanda teramati yang ditetapkan di TC; Post Condition tidak diasersi (S-01).
  - TC-FA-PREF-460 sampai 465 menyebut "isi semua field wajib" tanpa menyebut nilai field wajib form transaksi; nilai disediakan tim FE sesuai modul pemilik.
  - TC-FA-PREF-465 memakai form Write-off pada Physical Count & Reconciliation (bukan Disposal Execute) dan pesan "write-off disposals"; tabel di Prerequisites memuatnya.
  - TC-FA-PREF-460 sampai 465 tidak menyebut cara menutup form transaksi yang terisi; perilaku penutupan form modul pemilik (Disposal Execute dan Physical Count & Reconciliation) tidak ada di sumber. Spec memakai pola S-08 baku ([×], dialog D-04, [Leave]) sampai TC/PRD modul pemilik ada (S-15).
  - TC-FA-PREF-460 sampai 465 menyebut "Klik submit transaksi" tanpa label tombol; spec memakai teks TC.
