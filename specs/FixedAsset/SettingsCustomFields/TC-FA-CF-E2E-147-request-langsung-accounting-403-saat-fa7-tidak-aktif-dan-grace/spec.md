---
id: TC-FA-CF-E2E-147-request-langsung-accounting-403-saat-fa7-tidak-aktif-dan-grace
title: "Request Langsung Field Accounting Ditolak 403 Saat FA-7 Tidak Aktif dan Grace Period"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-577
  - TC-FA-CF-578
  - TC-FA-CF-579
  - TC-FA-CF-580
  - TC-FA-CF-673
coverage:
  web: automated
---

# Request Langsung Field Accounting Ditolak 403 Saat FA-7 Tidak Aktif dan Grace Period

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor blok pertama: Total Control Company License Lapse (Pre-setup #24). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_LICENSELAPSE_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Akun aktor blok kedua (ganti akun eksplisit di langkah 16 dan 17): Total Control Company Grace (Pre-setup #25). Email tidak tertulis di Pre-setup TC; disediakan tim FE. Password lewat `Spectra.env.FA_TC_GRACE_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company License Lapse (Pre-setup #24): field Accounting `Cost Center` Active Required Yes, FA-7 sudah dicabut dan Grace Period sudah berakhir (T+31 hari). Company Grace (Pre-setup #25): Grace Period berjalan (T+10 hari), `Cost Center` bernilai `CC-100` pada aset `A1`. Nilai data mengacu `Fixture.faCustomFields.licenseLapse` dan `Fixture.faCustomFields.grace` (fixture belum ada, disediakan tim FE). Seed reset Company oleh hook `before` dan `after`.
- Kemampuan teknis: klien HTTP dengan token Total Control tiap Company (sesi API aktor, lihat `suite.md`; kemampuan disediakan tim BE/FE); fixture BE untuk membaca field Accounting dan nilai aset.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah (semua request ditolak). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-577 sampai TC-FA-CF-580: Company License Lapse

1. Kirim request Deactivate untuk `Cost Center` langsung
2. Verifikasi request Deactivate direspons 403 Forbidden
3. Kirim request Activate untuk `Cost Center` langsung
4. Verifikasi request Activate direspons 403 Forbidden
5. Verifikasi status `Cost Center` tidak berubah (dibaca lewat fixture BE)
6. Kirim request Delete untuk `Cost Center` langsung
7. Verifikasi server merespons 403 Forbidden
8. Verifikasi field `Cost Center` tetap ada (dibaca lewat fixture BE)
9. Kirim request Bulk Deactivate untuk field Accounting langsung
10. Verifikasi request Bulk Deactivate direspons 403 Forbidden
11. Kirim request Bulk Delete untuk field Accounting langsung
12. Verifikasi request Bulk Delete direspons 403 Forbidden
13. Verifikasi tidak ada perubahan sebagian pada field Accounting (dibaca lewat fixture BE)
14. Kirim request baca daftar field grup Accounting langsung
15. Verifikasi pembacaan berhasil tanpa 403

### TC-FA-CF-673: Company Grace

16. Ganti akun: `Logout` dari Total Control Company License Lapse
17. Login sebagai Total Control Company Grace dengan `Spectra.env.FA_TC_GRACE_PASSWORD`
18. Kirim request Edit aset `A1` langsung dengan nilai `Cost Center` diubah
19. Verifikasi server merespons 403 Forbidden
20. Verifikasi data aset `A1` tidak berubah (dibaca lewat fixture BE)
21. Buka Detail aset `A1`
22. Verifikasi nilai `Cost Center` aset `A1` tetap nilai tersimpan `CC-100`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a dengan Expected respons API (TC-FA-CF-577 sampai 580, 673) tetap di spec FE+BE ini; langkah request hanya mengasersi status respons dan state data lewat fixture BE (bagian 8b butir 1). Tidak ada perilaku FE yang diasersi pada request langsung; Detail aset di langkah 21 dan 22 adalah langkah observasi TC-FA-CF-673.
- S-05: klausa "tanpa entri log" TC-FA-CF-575 dan 576 (Company License Lapse) diasersi di spec 132, dan TC-FA-CF-666 (Company Grace) di spec 179; TC-FA-CF-577 sampai 580 dan 673 tidak memuat klausa log pada Expected.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 dan 17 (ganti akun eksplisit ke Company Grace). Request langsung (langkah 1, 3, 6, 9, 11, 14, 18) langsung diikuti `Verifikasi` status respons.
- Urutan TC: TC-FA-CF-580 (pembacaan diizinkan) ditaruh sesudah request ditolak; tidak ada dependensi data antar TC karena semua request ditolak.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company License Lapse dan Company Grace; akun disediakan tim FE.
  - TC-FA-CF-579 tidak menyebut field Accounting untuk Bulk; spec memakai field Accounting yang ada pada Pre-setup #24.
  - TC-FA-CF-580 (kelas a, Positive) mengasersi pembacaan berhasil dan merujuk TC-FA-CF-545 untuk penyembunyian field; TC-FA-CF-545 ada di spec 144.
