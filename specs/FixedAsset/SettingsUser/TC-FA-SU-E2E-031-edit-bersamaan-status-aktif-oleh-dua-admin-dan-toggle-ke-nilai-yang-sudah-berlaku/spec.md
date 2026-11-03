---
id: TC-FA-SU-E2E-031-edit-bersamaan-status-aktif-oleh-dua-admin-dan-toggle-ke-nilai-yang-sudah-berlaku
title: "Edit Bersamaan Status Aktif oleh Dua Admin dan Toggle ke Nilai yang Sudah Berlaku"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-99
  - TC-FA-SU-100
coverage:
  web: automated
---

# Edit Bersamaan Status Aktif oleh Dua Admin dan Toggle ke Nilai yang Sudah Berlaku

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`; Admin A adalah sesi UI akun ini. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Admin B (Pre-setup #13): pelaku kedua lewat sesi API (login API password, token tidak dihitung sebagai sesi web) yang hanya memicu perubahan state; identitas akun dan password Admin B tidak tertulis di Pre-setup TC dan "disediakan tim FE" (lihat Temuan untuk QA). Tidak ada sesi UI kedua.
- Data Pre-setup: Client `FaUserMain` (#20). Target memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE):
  - `Gita Permata {runId}-031-A`, email `gita.permata+{runId}-031-a@qwertysystem.net`: Active (TC-FA-SU-99).
  - `Gita Permata {runId}-031-B`, email `gita.permata+{runId}-031-b@qwertysystem.net`: Active (TC-FA-SU-100).
- Kemampuan teknis: pencatat request jaringan Spectra (status respons permintaan Admin A dan Admin B); kemampuan baca jumlah entri `Deactivate` pada Tab Changelog target (disediakan tim FE/BE, tanpa endpoint karangan). Log muncul eventual (NC-03): langkah yang menunggu entri memuat ulang tiap 5 detik, batas 2 menit.
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-99: Toggle ke nilai yang sudah berlaku dari tampilan basi

1. Ketik Search `Gita Permata {runId}-031-A`, tekan Enter
2. Admin B menonaktifkan `Gita Permata {runId}-031-A` lewat sesi API hingga status Inactive tersimpan
3. Catat jumlah entri `Deactivate` pada Tab Changelog `Gita Permata {runId}-031-A` setelah entri dari Admin B tampil
4. Klik sakelar Active pada baris `Gita Permata {runId}-031-A` (tampilan Admin A belum di-refresh)
5. Klik `[Deactivate]`
6. Verifikasi toast "Success, user has been deactivated." tampil
7. Verifikasi tidak ada dialog atau pesan konflik versi
8. Verifikasi daftar di-refresh dan sakelar Active baris `Gita Permata {runId}-031-A` OFF
9. Buka Detail `Gita Permata {runId}-031-A` > Tab Changelog, muat ulang
10. Verifikasi jumlah entri `Deactivate` sama dengan jumlah yang dicatat pada langkah 3

### TC-FA-SU-100: Edit bersamaan oleh dua admin pada aksi yang sama

11. Kembali ke halaman User List
12. Ganti isi kotak search dengan `Gita Permata {runId}-031-B`, tekan Enter
13. Klik sakelar Active pada baris `Gita Permata {runId}-031-B`
14. Klik `[Deactivate]` pada dialog Admin A dan pada saat yang sama Admin B mengirim Deactivate untuk `Gita Permata {runId}-031-B` lewat sesi API; tunggu kedua permintaan selesai hingga status Inactive tersimpan
15. Verifikasi status aktif `Gita Permata {runId}-031-B` Inactive (sakelar baris OFF) sebagai nilai akhir permintaan yang terakhir diterima server
16. Verifikasi tidak ada dialog konflik versi
17. Verifikasi tidak ada respons HTTP 409 pada kedua permintaan

## Notes

- Langkah penghubung (S-03): langkah 1 dan 12 (Search untuk menemukan baris target, R-16), langkah 3 (mencatat baseline jumlah entri setelah aksi Admin B), dan langkah 11 (kembali ke User List).
- Admin B memakai sesi API (R-20), bukan konteks UI kedua; butir `P-2` tidak dipakai (keputusan 2026-10-30).
- Tampilan Admin A pada TC-FA-SU-99 diasumsikan tidak ter-refresh otomatis sesudah langkah 2 (TC menyebutnya "tampilan basi"); tidak ada langkah yang mengasersi hal itu.
- Pembagian TC lintas spec: TC-FA-SU-97 dan TC-FA-SU-98 (sesi target terputus, login pengguna nonaktif) ada di spec 353 sampai 357.
- Temuan untuk QA:
  - Pre-setup #13 (Admin B) tidak menyebut email dan password akun; spec menulisnya "disediakan tim FE".
  - TC-FA-SU-100 langkah 4 meminta pemeriksaan Tab Changelog tetapi Expected dan Post Condition tidak menyatakan isi log; Tab Changelog tidak diasersi. Post Condition TC-FA-SU-100 diasersi sebatas status Inactive (langkah 15) karena langkah 4 TC memeriksa status.
  - Post Condition TC-FA-SU-99 ("jumlah entri `Deactivate` tidak bertambah dari tindakan sesi kedua") diasersi pada langkah 10 terhadap jumlah yang dicatat sesudah entri Admin B tampil, karena aksi Admin B sendiri menulis satu entri.
  - "Hampir bersamaan" pada TC-FA-SU-100 tidak punya batas waktu; spec memicu kedua permintaan pada langkah yang sama.
  - Target TC (Gita Permata) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06).
