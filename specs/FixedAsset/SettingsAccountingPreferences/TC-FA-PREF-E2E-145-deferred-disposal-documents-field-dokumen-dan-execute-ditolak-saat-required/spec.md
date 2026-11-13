---
id: TC-FA-PREF-E2E-145-deferred-disposal-documents-field-dokumen-dan-execute-ditolak-saat-required
title: "[DEFERRED] Disposal Documents: field dokumen dan Execute ditolak saat Required"
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

# [DEFERRED] Disposal Documents: field dokumen dan Execute ditolak saat Required

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (Disposal Documents keenam jenis Optional). Data modul Disposal Execute (PC-16) disediakan tim FE setelah modul tersedia: baris pelepasan jenis Sell berstatus Waiting for Execution untuk TC-FA-PREF-458, dan satu baris pelepasan per jenis (Sell, Scrap, Lost, Donate, Trade-in, Write-off) berstatus Waiting for Execution untuk TC-FA-PREF-460 sampai 465. Untuk TC-FA-PREF-459: aset yang dapat ditandai tidak ditemukan pada wizard-reconciliation, dan persetujuan Disposal Write-off yang diajukan pada langkah 6 sampai berstatus Waiting for Execution disediakan tim FE/BE lewat seed atau API. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Disposal Documents dibentuk lewat seed: keenam jenis Optional untuk TC-FA-PREF-458 dan 459, lalu keenam jenis Required untuk TC-FA-PREF-460 sampai 465 (tiap TC hanya mengasersi jenisnya sendiri).
- Jenis pelepasan yang diuji (langkah 15 sampai 21 diulang per baris; parameter hanya dari tabel ini):

  | TC | Jenis | Pesan |
  |---|---|---|
  | TC-FA-PREF-460 | Sell | A document is required for sell disposals. |
  | TC-FA-PREF-461 | Scrap | A document is required for scrap disposals. |
  | TC-FA-PREF-462 | Lost | A document is required for lost disposals. |
  | TC-FA-PREF-463 | Donate | A document is required for donate disposals. |
  | TC-FA-PREF-464 | Trade-in | A document is required for trade-in disposals. |
  | TC-FA-PREF-465 | Write-off | A document is required for write-off disposals. |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan baris pelepasan dengan status yang ditentukan; pengisian field wajib form Execute lewat UI modul pemilik; persetujuan Disposal lewat API.
- State global yang diubah: Disposal Documents company dan data record Missing, Report, serta Disposal yang dibuat TC-FA-PREF-459; Disposal Documents dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-458: Field dokumen selalu ada di form Execute walau Disposal Documents Optional

1. Seed Disposal Documents keenam jenis tersimpan Optional hingga tersimpan
2. Buka form Execute baris pelepasan jenis Sell pada Disposal Execute
3. Verifikasi field dokumen tampil pada form Execute

### TC-FA-PREF-459: Write-off aset tidak ditemukan saat rekonsiliasi lewat record Missing

4. Pada wizard-reconciliation, tandai aset sebagai tidak ditemukan sehingga record Missing dibuat
5. Dari record Missing, klik Report Disposal dengan Reason
6. Di Transactions > Disposal tab Reported, klik Dispose pada Report itu, pilih jenis Write-off, lalu klik Submit
7. Setujui pelepasan Write-off itu hingga berstatus Waiting for Execution
8. Buka form Execute pelepasan Write-off itu
9. Verifikasi field dokumen tampil pada form Execute pelepasan Write-off
10. Tutup form Execute
11. Buka pilihan Source pada Disposal
12. Verifikasi pilihan Source memuat sedikitnya satu opsi
13. Verifikasi pilihan Source tidak memuat Reconciliation

### TC-FA-PREF-460 sampai TC-FA-PREF-465: Execute pelepasan tanpa dokumen ditolak saat Required (Sell, Scrap, Lost, Donate, Trade-in, Write-off)

14. Seed Disposal Documents keenam jenis tersimpan Required hingga tersimpan

Untuk setiap baris tabel "Jenis pelepasan yang diuji" (langkah 15 sampai 21):

15. Buka form Execute baris pelepasan jenis `<Jenis>` berstatus Waiting for Execution pada Disposal Execute dan isi semua field wajib tanpa melampirkan dokumen
16. Klik Execute
17. Verifikasi pesan `<Pesan>` tampil di form Execute
18. Verifikasi baris pelepasan tidak ter-Execute
19. Klik [×] pada form Execute
20. Verifikasi dialog D-04 tampil tanpa Title dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
21. Klik [Leave] pada dialog D-04

22. Pulihkan Disposal Documents keenam jenis ke nilai awal PC-1 (Optional) lewat seed hingga tersimpan

## Notes

- Langkah 15 sampai 21 diulang enam kali (bagian 8b butir 7); parameter tiap iterasi hanya dari tabel di Prerequisites dan tidak ada langkah bersyarat. `Verifikasi` tiap iterasi satu per klausa (S-01). Ekspansi: 7 langkah x 6 iterasi = 42 langkah ditambah 15 langkah lain (57); penutupan form dirty memakai pola S-08 (klik [×], `Verifikasi` dialog D-04, klik [Leave]) sehingga tiap iterasi bertambah 2 langkah. Alasan melewati sekitar 35 (di atas smell): seluruh blok satu kelas harness (fungsional, modul pemilik), strukturnya seragam, dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna.
- Langkah penghubung (S-03): langkah 7 (persetujuan Disposal Write-off lewat API; TC menulis "Setelah disetujui" tanpa pelaku), langkah 10 (menutup form Execute sebelum membuka pilihan Source), langkah 14 (seed keenam jenis Required sekaligus; TC mensyaratkan hanya jenis uji Required dan jenis lain Optional dari PC-1, sedangkan asersi tiap TC hanya menyangkut jenisnya sendiri), langkah 19 dan 21 (menutup form Execute yang terisi lewat [×] dan [Leave] sebelum iterasi berikutnya, S-08, S-09; `Verifikasi` dialog D-04 pada langkah 20 tidak perlu dicatat lagi), langkah 22 (pemulihan state, R-08).
- Asersi absence "pilihan Source tidak memuat Reconciliation" (langkah 13) memakai anchor positif langkah 12 (pilihan Source sudah termuat dan memuat opsi lain; bagian 8b butir 2).
- Search tidak dipakai: form Execute dibuka dari modul pemilik tanpa memilih baris tabel.
- Temuan untuk QA:
  - TC-FA-PREF-458 tidak menyebut label field dokumen; spec mengasersi "field dokumen" sesuai Expected TC.
  - TC-FA-PREF-459 langkah 5 ("Amati pilihan Source pada Disposal") tidak menyebut layar atau form tempat pilihan Source berada; spec membukanya pada Disposal setelah form Execute ditutup (langkah 10 dan 11) dan tidak menyebut opsi Source lain yang diharapkan sebagai anchor.
  - TC-FA-PREF-459 langkah 3 menyebut "Submit" dan langkah 4 "Setelah disetujui" tanpa pelaku persetujuan dan tanpa label tombol persetujuan; spec memakai Submit dari TC dan menyetujui lewat API (langkah 7).
  - TC-FA-PREF-460 sampai 465 menyebut Expected "baris tidak ter-Execute" dan Post Condition "Baris tetap Waiting for Execution" tanpa langkah observasi terpisah; langkah 18 mengasersi Expected "baris tidak ter-Execute" tanpa tanda teramati yang ditetapkan di TC; Post Condition tidak diasersi (S-01).
  - TC-FA-PREF-460 sampai 465 menyebut "isi semua field wajib" tanpa menyebut nilai field wajib form Execute; nilai disediakan tim FE sesuai modul pemilik.
  - TC-FA-PREF-460 sampai 465 tidak menyebut cara menutup form Execute yang terisi; perilaku penutupan form modul Disposal tidak ada di sumber. Spec memakai pola S-08 baku ([×], dialog D-04, [Leave]) sampai TC/PRD modul Disposal ada (S-15).
