---
id: TC-GS-FILEMGR-E2E-058-log-snapshot-nama-aktor-dan-delete-user
title: "Pencatatan Log: Snapshot Nama Aktor setelah Rename dan Hapus Akun, serta Entri Delete User"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-231
  - TC-GS-FILEMGR-232
  - TC-GS-FILEMGR-233
coverage:
  web: automated
---

# Pencatatan Log: Snapshot Nama Aktor setelah Rename dan Hapus Akun, serta Entri Delete User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Akun ini hanya mengubah dan menghapus akun klon milik spec di bawah, bukan dirinya sendiri. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`). Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Data milik spec (suffix `{runId}-058`, seeding lewat fixture BE di hook `before`; mekanisme seeding tidak didefinisikan di TC, disediakan tim FE/BE). TC-232 dan TC-233 mengubah dan menghapus akun aktor Pre-setup (Sinta Maharani, Agus Wibowo); karena Pre-setup bersama tidak boleh diubah (S-06), spec memakai akun klon (disediakan tim FE, email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA):
  - Akun klon `Sinta Maharani {runId}-058` (Total Control, tampil `Sinta M`) sebagai pelaku entri Changelog `retired-photo-{runId}-058.jpg` (Permanently Delete, salinan C02) dan file Recycle Bin `old-avatar-{runId}-058.png` dengan Deleted By akun klon itu (salinan R01), dipakai TC-232.
  - Akun klon `Agus Wibowo {runId}-058` (Manage files: Delete, tampil `Agus W`) sebagai pelaku entri Changelog `stale-avatar-{runId}-058.png` (Permanently Delete, salinan C03) dan file Recycle Bin `expired-avatar-{runId}-058.jpg` dengan Deleted By akun klon itu (salinan R03; Deleted Date belum melewati retensi), dipakai TC-233.
  - User klon `Dewi Kartika {runId}-058` dengan foto profil aktif `dewi-kartika-{runId}-058.jpg` dan satu file di Recycle Bin `due-photo-{runId}-058.png` (Deleted Date belum melewati retensi); kedua file adalah precondition TC-231, dipakai sebagai precondition TC, tidak diasersi.
- Dependensi TC (TC-28 Changelog, TC-109 cascade purge Delete User) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus akun klon bersuffix `{runId}-058` yang masih ada (termasuk setelah rename) dan hapus permanen file bersuffix `{runId}-058`.
- Tidak ada state global yang diubah.

## Test Steps

### TC-GS-FILEMGR-232: Nama aktor tetap seperti saat aksi setelah akun aktor di-rename

1. Di Global Settings > User ubah nama `Sinta Maharani {runId}-058` menjadi `Sinta Pertiwi {runId}-058`, lalu klik [Save]
2. Tunggu aksi selesai
3. Buka Global Settings > File Manager, klik ikon Changelog di toolbar, ketik Search `retired-photo-{runId}-058`, tekan Enter
4. Verifikasi Modified By entri `retired-photo-{runId}-058.jpg` tetap `Sinta M` (nilai saat aksi)
5. Tutup modal Changelog lewat `✕`, klik tombol Recycle Bin di toolbar, ketik Search `old-avatar-{runId}-058`, tekan Enter
6. Verifikasi Deleted By `old-avatar-{runId}-058.png` tetap `Sinta M`
7. Tutup modal Recycle Bin lewat `✕`

### TC-GS-FILEMGR-233: Nama aktor tetap tampil setelah akun aktor dihapus

8. Di Global Settings > User hapus akun `Agus Wibowo {runId}-058` dan konfirmasi
9. Tunggu aksi selesai
10. Buka Global Settings > File Manager, klik ikon Changelog di toolbar, ketik Search `stale-avatar-{runId}-058`, tekan Enter
11. Verifikasi Modified By entri `stale-avatar-{runId}-058.png` tetap `Agus W`
12. Tutup modal Changelog lewat `✕`, klik tombol Recycle Bin di toolbar, ketik Search `expired-avatar-{runId}-058`, tekan Enter
13. Verifikasi Deleted By `expired-avatar-{runId}-058.jpg` tetap `Agus W`
14. Tutup modal Recycle Bin lewat `✕`

### TC-GS-FILEMGR-231: Entri log Delete User hanya memuat nama user tanpa jumlah file

15. Di Global Settings > User, Delete User `Dewi Kartika {runId}-058` lalu konfirmasi
16. Buka modal Changelog User, ketik Search `Dewi Kartika {runId}-058`, tekan Enter
17. Verifikasi entri Delete User hanya memuat nama `Dewi Kartika {runId}-058`
18. Verifikasi entri Delete User tidak memuat informasi jumlah file yang terhapus

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas pencatatan (snapshot nama aktor); P-3 tidak dipakai, tiap TC memakai akun klon sendiri.
- Urutan TC di spec berbeda dari sumber (232, 233, 231): rename (tidak menghabiskan data) lebih dulu, lalu dua penghapusan akun; Delete User Dewi Kartika dengan cascade purge file ditaruh paling akhir (prinsip 5).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2 dan 9 (Tunggu aksi selesai sebelum pindah surface), langkah 5, 7, 12, 14 (menutup modal dan membuka Recycle Bin), langkah 3 dan 10 (Search entri target pada Changelog; TC sumber menyebut "baca Modified By entri C02/C03").
- TC-232 dan TC-233 menyebut entri C02/C03 dan R01/R03 lewat kode Pre-setup; spec menggantinya dengan salinan bersuffix yang pelakunya akun klon.
- Temuan untuk QA:
  - Akun klon aktor (Sinta Maharani, Agus Wibowo) tidak ada di Tabel A1 (Q-5); email dan pembuatannya disediakan tim FE.
  - TC-231 tidak menyebut surface log yang dimaksud selain "modal Changelog User" (Q-11); spec mengasersi hanya di Changelog User, tidak di Activity Log atau System Log.
  - TC-231 mengasersi "tidak ada informasi jumlah file" tanpa menyebut kolom yang diperiksa; spec memeriksa seluruh kolom entri.
