---
id: TC-AC-RP-E2E-133-notifikasi-in-app-tanpa-notifikasi-dan-auto-revert-detail-user-deferred
title: "Notifikasi In-App [DEFERRED]: Tanpa Notifikasi untuk Assign dan Group Deleted, dan Auto-Revert dari Detail User"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-343
  - TC-AC-RP-344
coverage:
  web: unsupported
---

# Notifikasi In-App [DEFERRED]: Tanpa Notifikasi untuk Assign dan Group Deleted, dan Auto-Revert dari Detail User

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Ganti akun di tengah spec ke akun target notifikasi: `Alex Tan` dan `Fajar Nugroho` (TC-AC-RP-343), dan `Rina Wijaya` (TC-AC-RP-344). Email dan password akun ini tidak tertulis di Pre-setup #1 sampai #10 dan disediakan tim FE (Email akun ini tidak tertulis di Pre-setup TC; lihat Temuan untuk QA). Setelah tiap akun sesi dikembalikan ke `Siti Nurhaliza`.
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard: `Alex Tan`), #13 (pemegang Total Control `Rina Wijaya`), #14 (penugasan Group Manager: `Fajar Nugroho` di `Sumatera`), dan #15 (penugasan peran individual). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini. Pengiriman notifikasi berstatus future implementation sampai modul Admin Console > Notification tersedia (`[DEFERRED]`, kontrak event normatif PRD §8.8).
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > Group` (aksi hapus group) dan `Settings > User > Detail User` (Tab Role) tersedia untuk akun Total Control; reset data Pre-setup (group `Sumatera` beserta GM) disediakan tim FE/BE.
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC; kemampuan reset dinyatakan di `suite.md` (Pemulihan baseline automation); dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-343: [DEFERRED] Assign dan Remove (Group Deleted) tidak memicu notifikasi

1. Klik tombol "+ Assign"
2. Centang `Alex Tan` lalu klik `[Assign]`
3. Hapus group `Sumatera` (GM `Fajar Nugroho`) dari Settings > Group
4. Tunggu aksi selesai
5. Ganti akun: Logout, lalu login sebagai `Alex Tan`
6. Buka notifikasi
7. Verifikasi panel notifikasi tampil
8. Verifikasi tidak ada notifikasi untuk Assign Total Control
9. Ganti akun: Logout, lalu login sebagai `Fajar Nugroho`
10. Buka notifikasi
11. Verifikasi panel notifikasi tampil
12. Verifikasi tidak ada notifikasi untuk pelepasan Group Manager akibat Delete Group
13. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
14. Pulihkan baseline: `Alex Tan` kembali Standard serta group `Sumatera` dan GM `Fajar Nugroho` dipulihkan

### TC-AC-RP-344: [DEFERRED] Auto-revert dari Tab Role Settings > User juga mengirim notifikasi

15. Buka `Settings > User > Detail User` `Rina Wijaya` > Tab Role
16. Hapus centang D satu Global Role lalu konfirmasi
17. Catat waktu aksi sesaat setelah konfirmasi
18. Ganti akun: Logout, lalu login sebagai `Rina Wijaya`
19. Buka notifikasi
20. Verifikasi notifikasi Auto-Revert Total Control diterima
21. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
22. Pulihkan baseline: `Rina Wijaya` kembali Total Control dan D Global Role tercentang

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness d (harness eksternal: notifikasi in-app dari modul Admin Console > Notification) dan `[DEFERRED]`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 4, 13, 14, 17, 21, 22.
- `[DEFERRED]`: pengiriman notifikasi berstatus future implementation sampai modul Admin Console > Notification tersedia; spec ditandai `coverage.web: unsupported` karena modul Notification belum ada dan pengiriman notifikasi tidak dapat diverifikasi; spec diaktifkan lagi (`coverage.web: automated`) saat modul Notification selesai.
- Ganti akun eksplisit pada langkah 5, 9, dan 18 (S-07); pengembalian sesi ke `Siti Nurhaliza` adalah langkah penghubung.
- Asersi absence notifikasi (TC-AC-RP-343) diletakkan segera setelah pemicu dan didahului Verifikasi panel notifikasi tampil sebagai anchor positif (bagian 8b butir 2 dan 11).
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-343 langkah 3 "Hapus group `Sumatera` (GM `Fajar Nugroho`) dari Settings > Group" tidak menyatakan alur penghapusan; spec mengikuti teks TC.
  - TC-AC-RP-344 langkah 2 tidak menyebut Global Role mana yang dihapus D-nya; spec memakai "satu Global Role" sesuai TC dan memilih Global Role yang pilihannya disediakan tim FE.
  - TC-AC-RP-344 Expected tidak menyebut Title dan Body notifikasi; spec hanya mengasersi notifikasi Auto-Revert Total Control diterima.
  - Email dan password `Alex Tan`, `Fajar Nugroho`, dan `Rina Wijaya` sebagai penerima notifikasi tidak tertulis di Pre-setup #1 sampai #10; disediakan tim FE.
  - `[DEFERRED]`: `coverage.web: unsupported` sampai modul Notification tersedia; kolom Automation TC menyatakan `Automatable`, sehingga spec diaktifkan lagi saat modul Notification selesai.
