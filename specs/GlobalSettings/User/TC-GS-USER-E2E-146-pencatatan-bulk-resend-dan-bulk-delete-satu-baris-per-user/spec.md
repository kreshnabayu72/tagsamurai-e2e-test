---
id: TC-GS-USER-E2E-146-pencatatan-bulk-resend-dan-bulk-delete-satu-baris-per-user
title: "Pencatatan Bulk Resend Activation Email dan Bulk Delete: Satu Baris Log per User yang Diproses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-914
  - TC-GS-USER-915
coverage:
  web: automated
---

# Pencatatan Bulk Resend Activation Email dan Bulk Delete: Satu Baris Log per User yang Diproses

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor pertama: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup: akun aktor Siti Nurhaliza (No. 2) sebagai pelaku. Tidak ada data Pre-setup lain yang dipakai; Mike Tan, Andre Kurniawan, Tono Wijaya, dan Rani Lestari memakai user seed milik spec (S-06).
- Data Dinamis milik spec, di-seed lewat API di hook `before` (HK1) dan dibersihkan di hook `after`, semuanya Division `Finance`, Access `Fixed Asset`:
  - `Mike Tan {runId}-146`, Email `miketan+{runId}-146@qwertysystem.net`, Pending Activation, cooldown Resend Activation Email masih aktif saat Bulk Resend dijalankan (TC-GS-USER-914).
  - `Andre Kurniawan {runId}-146`, Email `andrekurniawan+{runId}-146@qwertysystem.net`, Pending Activation, cooldown Resend Activation Email sudah lewat (siap) saat Bulk Resend dijalankan (TC-GS-USER-914).
  - `Tono Wijaya {runId}-146`, Email `tonowijaya+{runId}-146@qwertysystem.net`, Activated, tanpa aset dan approval (TC-GS-USER-915).
  - `Rani Lestari {runId}-146`, Email `ranilestari+{runId}-146@qwertysystem.net`, Activated, tanpa aset dan approval (TC-GS-USER-915).
- Kemampuan teknis, disediakan tim FE/BE (TC tidak menyebut cara dan PRD/LLD tidak menyebut endpoint): membuat dua keadaan cooldown Resend yang berbeda pada saat aksi (Mike Tan aktif, Andre Kurniawan sudah lewat), termasuk bila tim FE memilih mengatur jam server dan jam browser; keadaan itu sudah terbentuk sebelum baseline dicatat. Seeding user Pending Activation dan Activated lewat API dengan endpoint aplikasi sehingga entri log seed ditulis sebelum baseline dicatat. Kemampuan baca jumlah baris Modal Changelog User per user dan Action lewat BE disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut endpoint).
- State global: tidak ada. Suite berjalan serial (`suite.md`). Email tidak diasersi (Expected TC hanya log), sehingga mail-catcher tidak dipakai.
- Baseline log: jumlah entri Changelog (audit trail permanen) tidak dapat diturunkan dari seeding. Sebelum aksi pemicu tiap TC, spec mencatat baseline jumlah baris per user dan Action di Modal Changelog User lewat kemampuan baca BE, sesudah hook `before` selesai (cooldown Mike Tan dan Andre Kurniawan sudah terbentuk). Asersi memakai selisih terhadap baseline (S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua user bersuffix `{runId}-146` yang masih ada. Hook `before` menghapus sisa user bersuffix `-146` dari run lama. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### TC-GS-USER-914: Bulk Resend menulis 1 baris per user yang diproses, baris di-skip tanpa log

1. Catat baseline di Modal Changelog User lewat kemampuan baca BE: `{n0-andre}` dan `{n0-mike}` = jumlah baris Action `Resend Activation Email` untuk `Andre Kurniawan {runId}-146` dan `Mike Tan {runId}-146`
2. Klik icon Search, ketik `{runId}-146`, tekan Enter
3. Centang baris `Mike Tan {runId}-146` dan `Andre Kurniawan {runId}-146`
4. Klik Bulk Action, pilih `Resend Activation Email`
5. Tunggu aksi selesai (Bulk Action Bar hilang)
6. Klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `{runId}-146`, tekan Enter
7. Verifikasi Modal Changelog User: jumlah baris dengan Action `Resend Activation Email` untuk User Name `Andre Kurniawan {runId}-146` bertambah tepat 1 dari baseline `{n0-andre}`
8. Verifikasi Modal Changelog User: jumlah baris dengan Action `Resend Activation Email` untuk User Name `Mike Tan {runId}-146` tetap sama dengan baseline `{n0-mike}` (tidak bertambah)
9. Tutup Modal Changelog User, hapus centang baris yang terpilih

### TC-GS-USER-915: Bulk Delete menulis baris Delete per user

10. Catat baseline di Modal Changelog User lewat kemampuan baca BE: `{n0-tono}` dan `{n0-rani}` = jumlah baris Action `Delete` dengan Field `Name` untuk `Tono Wijaya {runId}-146` dan `Rani Lestari {runId}-146`
11. Centang baris `Tono Wijaya {runId}-146` dan `Rani Lestari {runId}-146` (hasil Search `{runId}-146` tetap tampil)
12. Klik Bulk Action, pilih `Delete`
13. Klik [Delete] pada dialog Delete
14. Tunggu aksi selesai (Bulk Action Bar hilang)
15. Klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `{runId}-146`, tekan Enter
16. Verifikasi Modal Changelog User: jumlah baris dengan Action `Delete` dan Field `Name` untuk User Name `Tono Wijaya {runId}-146` bertambah tepat 1 dari baseline `{n0-tono}` dan untuk User Name `Rani Lestari {runId}-146` bertambah tepat 1 dari baseline `{n0-rani}`
17. Tutup Modal Changelog User

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Urutan TC di spec: 914, 915. 915 (Bulk Delete) paling akhir karena menghapus data (bagian 3, prinsip 5).
- P-1 (state berat) untuk TC-GS-USER-914: klausa "Tidak ada baris untuk Mike Tan" ditulis sebagai `Verifikasi` berbaseline di spec ini, bukan dipindah ke spec absence, karena keadaan cooldown aktif Mike Tan dan cooldown lewat Andre Kurniawan dibangun khusus untuk aksi Bulk Resend TC ini. Anchor positif pada surface yang sama adalah baris `Resend Activation Email` milik Andre Kurniawan dari aksi yang sama.
- Pembagian TC lintas spec: Bulk Resend dengan baris cooldown di-skip (toast, cooldown, partial) diverifikasi di spec `TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend`. Bulk Delete (dialog, toast, hasil list) diverifikasi di spec `TC-GS-USER-E2E-055-bulk-delete-homogen-campuran-dan-cancel`. Spec ini hanya memverifikasi pencatatan di Modal Changelog User.
- Mike Tan ditulis sebagai user dengan cooldown aktif dan Andre Kurniawan sebagai user siap sesuai precondition TC; baris log dikenali lewat Search nama bersuffix `{runId}-146` (bukan Search Action, yang akan memuat baris semua user) dan Action, bukan posisi teratas, dan dihitung terhadap baseline per user dan Action.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline jumlah baris di awal tiap TC (S-12), Search `{runId}-146` (satu Search dipakai untuk kedua TC, hasilnya memuat keempat user seed) dan pemilihan baris di User List, "Tunggu aksi selesai" (8b butir 8), pembukaan Modal Changelog User beserta Search, serta penutupan modal dan pelepasan centang di antara TC (S-03, S-09).
- Temuan untuk QA:
  - TC-GS-USER-914 Precondition ("Mike Tan cooldown aktif; Andre Kurniawan siap") tidak menyebut cara membuat dua keadaan cooldown pada saat yang sama. Spec menyebutnya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-USER-914 Expected Result tidak menyebut toast Bulk Resend ("Success, activation email has been sent. Some items were skipped (cooldown not finished).") yang ada di TC-GS-USER-303; spec tidak mengasersinya (S-02).
  - TC-GS-USER-915 menyebut "Bulk Delete keduanya" tanpa menyebut dialog konfirmasi; spec memakai [Delete] pada dialog Delete sesuai TC-GS-USER-299.
  - Slice ini tidak punya Post Condition pada TC sumber.
