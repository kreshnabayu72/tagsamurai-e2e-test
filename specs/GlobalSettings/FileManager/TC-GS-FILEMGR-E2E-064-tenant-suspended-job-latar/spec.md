---
id: TC-GS-FILEMGR-E2E-064-tenant-suspended-job-latar
title: "State Tenant: Auto-Purge dan Cascade Purge Tetap Berjalan saat Client Suspended"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-113
  - TC-GS-FILEMGR-288
coverage:
  web: automated
---

# State Tenant: Auto-Purge dan Cascade Purge Tetap Berjalan saat Client Suspended

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini (saat Client Active, sebelum status diubah); kredensial `Spectra.env.GS_TC_PASSWORD`. Langkah "login" pada TC-113 dan TC-288 sesudah Client diaktifkan kembali dipenuhi oleh sesi hook ini. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah status Client uji. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE; mekanisme tidak didefinisikan di TC, lihat Temuan untuk QA): mengubah status Client uji menjadi Suspended dan Active; memicu job auto-purge harian dan cascade purge untuk satu user lewat fixture BE. Menunggu job selesai: muat ulang halaman dan ulangi Search hingga kondisi tercapai, maksimum 12 kali dengan jeda 5 detik (usulan, dapat disesuaikan tim FE; TC hanya menyebut refresh berulang tanpa batas angka). Job auto-purge harian di environment e2e dijeda kecuali dipicu spec ini (Q-3).
- State global yang diubah: status Client uji. Hook `after` (tetap jalan walau spec gagal di tengah) mengembalikan status ke Active.
- Data milik spec (suffix `{runId}-064`, seeding lewat fixture BE di hook `before`):
  - `expired-avatar-{runId}-064.jpg` (salinan R03) di Recycle Bin dengan batas retensi terlampaui (Deleted Date sekarang - 31 hari, retensi 30 hari), dipakai TC-113.
  - User milik spec `Dewi Kartika {runId}-064` dengan foto profil aktif `dewi-kartika-{runId}-064.jpg` (salinan F04) dan satu file di Recycle Bin `due-photo-{runId}-064.png` (salinan R04, Deleted Date sekarang - 5 hari agar tidak terhapus oleh job auto-purge TC-113), dipakai TC-288.
- Baseline log: nama file bersuffix unik, sehingga jumlah entri awal Changelog File Manager untuk semua nama di atas adalah nol.
- Dependensi TC (TC-111 auto-purge, TC-109 cascade purge) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): kembalikan status Client ke Active, hapus permanen lewat API file bersuffix `{runId}-064` yang masih ada dan hapus user milik spec.

## Test Steps

### TC-GS-FILEMGR-113: Auto-purge tetap berjalan saat Client Suspended

1. Ubah status Client uji menjadi Suspended
2. Picu job auto-purge harian lewat fixture BE
3. Aktifkan kembali Client uji (status Active)
4. Muat ulang halaman File Manager, klik tombol Recycle Bin di toolbar, ketik Search `expired-avatar-{runId}-064`, tekan Enter; ulangi muat ulang dan Search hingga baris tidak ada (batas di Prerequisites)
5. Verifikasi `expired-avatar-{runId}-064.jpg` tidak lagi ada di Recycle Bin (empty state "No results found")
6. Tutup modal Recycle Bin lewat `✕`, klik ikon Changelog di toolbar, ketik Search `expired-avatar-{runId}-064`, tekan Enter
7. Verifikasi Changelog memuat baris Action `Permanently Delete` untuk `expired-avatar-{runId}-064.jpg` dengan Modified By `System`
8. Tutup modal Changelog lewat `✕`

### TC-GS-FILEMGR-288: Cascade purge tetap berjalan saat Client Suspended

9. Ubah status Client uji menjadi Suspended
10. Picu cascade purge untuk user `Dewi Kartika {runId}-064` lewat fixture BE
11. Aktifkan kembali Client uji (status Active)
12. Muat ulang halaman File Manager, ketik Search `dewi-kartika-{runId}-064`, tekan Enter; ulangi muat ulang dan Search hingga baris tidak ada (batas di Prerequisites)
13. Verifikasi `dewi-kartika-{runId}-064.jpg` terhapus permanen dan tidak ada di tabel utama (empty state "No results found")
14. Klik tombol Recycle Bin di toolbar, ketik Search `due-photo-{runId}-064`, tekan Enter
15. Verifikasi `due-photo-{runId}-064.png` terhapus permanen dan tidak ada di Recycle Bin (empty state "No results found")
16. Tutup modal Recycle Bin lewat `✕`, klik ikon Changelog di toolbar, ketik Search `-{runId}-064`, tekan Enter
17. Verifikasi Changelog memuat baris untuk `expired-avatar-{runId}-064.jpg` (pembanding dari TC-113)
18. Verifikasi modal Changelog File Manager tidak memuat baris untuk `dewi-kartika-{runId}-064.jpg` dan `due-photo-{runId}-064.png`
19. Tutup modal Changelog lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas state tenant dengan pemicu job latar (h + d); job auto-purge dan cascade purge hanya memicu kondisi yang diuji (P-2: proses sistem sebagai pemicu), objek uji adalah tidak adanya gate status Client. Pengujian job itu sendiri ada di spec `TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry` dan `TC-GS-FILEMGR-E2E-028-cascade-purge-delete-user-dan-non-login-user`.
- Urutan TC sama dengan sumber dibalik menjadi 113 lalu 288 (TC-288 bergantung pada TC-113 menurut kolom Dependensi). Kedua blok memakai data milik masing-masing; tidak ada ketergantungan hasil.
- Perbedaan dari data TC: `due-photo.png` pada TC-288 (R04) berumur 31 hari; spec memakai salinan berumur 5 hari agar job auto-purge pada TC-113 tidak menghapusnya lebih dulu. Hasil cascade purge sama.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 3, 9, 11 (status Client dijadikan langkah eksplisit; mengaktifkan kembali Client adalah langkah TC), langkah 4 dan 12 (muat ulang berulang menunggu job), langkah 6, 8, 16, 19 (membuka dan menutup modal), langkah 14 (Search pada Recycle Bin).
- Asersi tidak ada baris Changelog untuk file TC-288 (langkah 18) memakai baseline nol karena nama bersuffix unik, dengan anchor positif baris `expired-avatar-{runId}-064.jpg` pada langkah 17 (surface yang sama) dan empty state hasil Search pada langkah 13 dan 15. Keputusan D-1 opsi B: tidak ada spec absence terpisah; P-1 (state berat: cascade purge dibangun pada langkah 10 saat Client Suspended).
- Temuan untuk QA:
  - Pemicu job (auto-purge, cascade purge) dan pengubah status Client tidak didefinisikan di TC (Q-4); ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-288 mencantumkan R04 `due-photo.png` berumur 31 hari yang juga dihapus job auto-purge harian; spec memakai salinan 5 hari (lihat di atas).
  - Batas tunggu job tidak disebut TC (Q-3); usulan 12 kali dengan jeda 5 detik.
